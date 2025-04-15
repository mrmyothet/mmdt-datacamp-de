import json
import requests
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.operators.email import EmailOperator


default_args = {
    "owner": "airflow",
}

process_sales_dag = DAG(dag_id="process_sales_dag", default_args=default_args)


def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, "wb") as f:
        f.write(r.content)
    # Use the print method for logging
    print(f"File pulled from {URL} and saved to {savepath}")


def parse_file(inputfile, outputfile):
    with open(inputfile) as infile:
        data = json.load(infile)
        with open(outputfile, "w") as outfile:
            json.dump(data, outfile)


pull_file_task = PythonOperator(
    task_id="pull_file",
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={"URL": "http://dataserver/sales.json", "savepath": "latestsales.json"},
    dag=process_sales_dag,
)


parse_file_task = PythonOperator(
    task_id="parse_file",
    # Set the function to call
    python_callable=parse_file,
    # Add the arguments
    op_kwargs={"inputfile": "latestsales.json", "outputfile": "parsedfile.json"},
    dag=process_sales_dag,
)


email_manager_task = EmailOperator(
    task_id="email_manager",
    to="manager@datacamp.com",
    subject="Latest sales JSON",
    html_content="Attached is the latest sales JSON file as requested.",
    files="parsedfile.json",
    dag=process_sales_dag,
)


# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task
