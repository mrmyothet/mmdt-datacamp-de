# Import the timedelta object
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

# Create the dictionary entry
default_args = {"start_date": datetime(2024, 1, 20), "sla": timedelta(minutes=30)}

# Add to the DAG
test_dag = DAG("test_workflow", default_args=default_args, schedule=None)


# Create the task with the SLA
task1 = BashOperator(
    task_id="first_task",
    sla=timedelta(hours=3),
    bash_command="initialize_data.sh",
    dag=test_dag,
)

generate_report = BashOperator(
    task_id="generate_report",
    bash_command="generate_report.sh",
    start_date=datetime(2024, 1, 20),
    dag=test_dag,
)

# Define the email task
email_report = EmailOperator(
    task_id="email_report",
    to="airflow@datacamp.com",
    subject="Airflow Monthly Report",
    html_content="""Attached is your monthly workflow report - please refer to it for more detail""",
    files=["monthly_report.pdf"],
    dag=test_dag,
)

# Set the email task to run after the report is generated
email_report << generate_report
