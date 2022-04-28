from prefect.deployments import DeploymentSpec, SubprocessFlowRunner

from prefect.deployments import DeploymentSpec, SubprocessFlowRunner

DeploymentSpec(
    name="my-first-deployment",
    flow_location="./etl.py",
    flow_name="Previously unreliable pipeline",
    parameters={'msg':'Hello from my first deployment!'},
    tags=['ETL'],
    flow_runner=SubprocessFlowRunner()
)