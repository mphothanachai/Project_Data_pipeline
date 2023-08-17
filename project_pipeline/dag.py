from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
import pandas as pd
from datetime import datetime, timedelta

#path and  {{ ds }} = date today
raw_output_path = "gs://datalakelake/raw_data/raw_data_{{ ds }}.csv"
clean_output_path = "gs://datalakelake/clean_data/clean_data_{{ ds }}.csv"

def extract_DB(raw_path):
    postgres = PostgresHook(postgres_conn_id='postgres_default')

    df = postgres.get_pandas_df(sql="SELECT * FROM userbase")
    df.to_csv(raw_path, index=False)

def clean_data(raw_path, clean_path):
    
    df = pd.read_csv(raw_path)

    df['Join_Date'] = pd.to_datetime(df['Join_Date'])
    df['Last_Payment_Date'] = pd.to_datetime(df['Last_Payment_Date'])

    df['Subscription_period'] = (df['Last_Payment_Date'].dt.year - df['Join_Date'].dt.year) * 12 + \
                               df['Last_Payment_Date'].dt.month - df['Join_Date'].dt.month
    df = df.rename(columns={'Subscription_period': 'Subscription_period_(Month)'})

    df["Plan_Duration"] = df["Plan_Duration"].apply(lambda x: x.replace(" Month", "")).astype(int)

    df = df.rename(columns={'Plan_Duration': 'Plan_Duration_(Month)'})

    df['THB_Bath'] = df['Subscription_Type'].map({'Basic': 169, 'Standard': 349, 'Premium': 419})

    df["Revenue(Bath)"] = df["Plan_Duration_(Month)"] * df["Subscription_period_(Month)"] * df["THB_Bath"]

   
    df.to_csv(clean_path, index=False)

with DAG(
    "dag",
    schedule_interval=" 0 0 * * * ", #work on midnight(with cron)
    tags=["project"]
) as dag:

    t1 = PythonOperator(
        task_id="extract_postgresql",
        python_callable=extract_DB,
        op_kwargs={"raw_path": raw_output_path},
    )
    t2 = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
        op_kwargs={
            "raw_path": raw_output_path,
            "clean_path": clean_output_path,
        },
    )
    t3 = BashOperator(
        task_id="copy_to_stage_snowflake",
        bash_command="gsutil cp gs://datalakelake/clean_data/clean_data_{{ ds }}.csv gs://us-south1-airflow-c53bbfb7-bucket/data/",
    )
    t4 = BashOperator(
        task_id="romove_lastdate_file",
        bash_command='gsutil rm gs://us-south1-airflow-c53bbfb7-bucket/data/clean_data_$(date -d "yesterday" +%Y-%m-%d).csv',
    )
t1 >> t2 >> t3 >> t4