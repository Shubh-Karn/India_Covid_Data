from airflow import DAG

from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 8, 4),
    'email': ['s2.shubh2@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=120),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

with DAG(
    'airflow_covid_schedule',
    default_args=default_args,
    description='A scheduler to run python script which will extract covid data from HoHFW website',
    schedule_interval="00 04 * * *",
    tags=['scheduler'],
) as dag:

    t1 = BashOperator(
        task_id='run_script',
        bash_command = 'bash ~/Projects/India_Covid_Data/run_covid_data.sh ',

    )
