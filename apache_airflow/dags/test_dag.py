from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
}

with DAG(dag_id="test_dag", default_args=default_args) as analytics_dag:
    cleanup = BashOperator(
        task_id="cleanup_task",
        bash_command="cleanup.sh",
    )

    # Define a second operator to run the `consolidate_data.sh` script
    consolidate = BashOperator(
        task_id="consolidate_task", bash_command="consolidate_data.sh"
    )

    # Define a final operator to execute the `push_data.sh` script
    push_data = BashOperator(task_id="push_data", bash_command="push_data.sh")

    # Define a new pull_sales task
    pull_sales = BashOperator(
        task_id="pullsales_task",
        bash_command="wget https://salestracking/latestinfo?json",
    )

    # Set pull_sales to run prior to cleanup
    pull_sales >> cleanup

    # Configure consolidate to run after cleanup
    cleanup >> consolidate

    # Set push_data to run last
    consolidate >> push_data
