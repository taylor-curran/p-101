import random
from prefect import flow, task

@task(name="Get data from API", retries=4, retry_delay_seconds=2)
def call_unreliable_api():
    choices = [{"data": 42}, "failure"]
    res = random.choice(choices)
    if res == "failure":
        raise Exception("Our unreliable service failed")
    else:
        return res

@task(name="Add message to data")
def augment_data(data: dict, msg: str):
    data["message"] = msg
    return data

@task(name="Write results to database")
def write_results_to_database(data: dict):
    print(f"Wrote {data} to database successfully!")
    return "Success!"

@flow(name="Previously unreliable pipeline")
def pipeline(msg: str):
    api_result = call_unreliable_api()
    augmented_data = augment_data(data=api_result, msg=msg)
    write_results_to_database(augmented_data)

if __name__ == '__main__':
    pipeline(msg="Now we're cooking")