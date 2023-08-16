# Project_Data_pipeline
Data pipeline with (postgresql to googlecloud to snowflek) base on airfow

## 1. Introduction
In the current data is  importance for businesses and dicide something, creating a Data Pipeline to use data is extremely important. Managing and presenting data in an easily understandable Being a critical factor in achieving business success, as a data engineer, we undertake this project to study the steps creating a Data Pipeline. This pipeline connects the database using PostgreSQL with Google Cloud storage to backup data storage and management. and then, we transfer this data to Snowflake, a Data Warehouse, which is linked with the potential to analyze and utilize data effectively.

![image](https://github.com/mphothanachai/Project_Data_pipeline/assets/137395742/48beab67-eb61-4439-91ae-9f83d12f481a)

## 2.Objective
**Create a Data Pipeline for Data analyst and Data Science** to analyze and manage data for users of a Movie Streaming service in various formats. To enhance understanding  and Effective management , find some opportunities for expanding promotional spaces or organizing promotions.

 1. Analysis and forecasting of behavior user.
   (For example, the average duration that users remain subscribed to the same package.)
 2. Development or improvement for decision.
 (Develop dashboards and summary reports that are essential for executives, help in decision with sales figures, package selection, and other activities.)

 ![image](https://github.com/mphothanachai/Project_Data_pipeline/assets/137395742/6c9cec96-68af-4346-95c7-aad194a3312a)

## 3. Design
I will use **ETL** method ([Credit picture ](https://www.informatica.com/content/dam/informatica-com/en/images/misc/etl-process-explained-diagram.png))

![image](https://github.com/mphothanachai/Project_Data_pipeline/assets/137395742/57cdd074-0b1d-4eb5-af2a-12f937b63495)

Let design **ETL pipeline**

![image](https://github.com/mphothanachai/Project_Data_pipeline/assets/137395742/9c43af59-097b-4078-af26-16239c118ce9)

Let delve into the details of the ETL pipeline .

![image](https://github.com/mphothanachai/Project_Data_pipeline/assets/137395742/9bd5d903-6b7b-4346-b9b7-f02b98fa24cd)

## 4. Prepare (before use gcp,postgreSQL and snowflek)
1.	Account [Google cloud platfrom](https://console.cloud.google.com/) (gcp) if you have it you can use service on gcp (composer , google cloud and sql server).
2.	Account [snowflek](https://app.snowflake.com/) (Data warehouse).
3.	  Download [pgAdmin](https://www.pgadmin.org/) tool for manage postgreSQL.
4.	Account [github](https://github.com/) use to push code to git.

## 5.Postgre Database (Prepare)

1. First of all prepare  **Database** with gcp 
> Search SQL server (in gcp) 

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/904498de-0c53-401b-a991-6ac2e035f19e)

> Create Instance

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/2a16359f-c22c-4f48-9399-b9a25e86ca66)

>Choose PostgreSQL
 
![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/75f38977-6e62-4474-a3d8-84e642f1505c)

>Config Resourse

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/50ba72a2-6668-44c2-b410-3f113cb9f901)

2. Second one prepare [pgAdmin](https://www.pgadmin.org/) (download) tool for managing and working with PostgreSQL databases
> Register => server => Create name postgre

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/249f2c1e-604f-42c3-906a-1b42bd444674)

3. And then connect with pgAdmin (port 5432 is the commonly used port for PostgreSQL)
![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/9241c047-c83b-4805-ae64-d6ff2931fa72)

4. **( Important before connect )** Connection from a public IP is currently not possible due to **firewall** restrictions. Network settings need to be edited in Connections to allow access
> Edit (SQL server on gcp) => Connections  => Add a network

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/30eb8765-30bb-4cfc-b89c-18af0a89970b)

5. If u connect success (The image will appear below)

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/25d8fd3d-393f-42da-9189-9773b24c77cc)

## 6.pgAdmin (postgresql)
1. Before we can use DB we just create DB from pgAdmin before
![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/2dd64fa0-e813-4197-a376-2d9088331268)
2. Choose name and save it (DB name)

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/ffd0ed9f-db02-48c2-8405-51add81edc06)
>Next one choose schema => Create schema => Choose name of schema => save it

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/9b6ec9fc-a18d-4031-8edd-9e87210e2f83)
> Schema => Find Table => Create table => Choose name of table

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/654b18c6-5627-4b5b-afe3-94d4afdca4a2)
> Columns => Create columns =>save

3. If column have String choose (text) or Integer choose Integer
![createtable](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/131f9acc-201d-4ee5-938a-df9fa5590b6f)

4. **pgAdmin (postgresql)** easy to use because it can push csv,binary or text into DB.
You don't need to use command to create tables and insert row by row (In some case).
>Table => import/Export

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/7d159de0-7795-4eaa-9d30-08933e652be2)
>Choose import => file name (location file on local) =>format csv => In options => Choose enable Header

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/9aa572c6-fd3f-429d-9d58-66027c81c077)

5.  **_Aah!_** I think it not easy at all .I have some problem .I got error of different "datestyle"

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/50152751-ed92-4e84-9e36-c370f57dd740)

6. Let me Check .CSV (This csv have different of format date)

![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/22cc17cd-fa9d-455d-b97f-bbe33be431b6)

 7. I will use Python in google colab (Jupyter notebook) to first clean data before push in Database.
> Google colab => upload file (The file that hasn't been cleaned yet)
```
# install package and import to use pd in pandas
! pip install pandas
import pandas as pd
```
8. Use function lamda (pandas) to change"-" and replace with "/" in columns that we choose in this case Join_date and Last_payment
```
#use pandas to read csv
df = pd.read_csv("/content/Userbase2.csv")
#use lamda
df["Join_Date"] = df.apply(lambda x: x["Join_Date"].replace("-","/"), axis=1)
df["Last_Payment_Date"] = df.apply(lambda x: x["Last_Payment_Date"].replace("-","/"), axis=1)
```
9. Use function lamda (pandas) to change type to datetime and errors='coerce' this agrument function if got errors that may occur during the transformation process when a conversion cannot be performed.
> Download the clean_data to local
```
#use lamda
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
df['Last_Payment_Date'] = pd.to_datetime(df['Last_Payment_Date'], errors='coerce')
#convert to csv
df.to_csv("Clean_User.csv", index=False)
```
10. Import data to postgresql again and then we got "Successfully completed".
![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/386c6e87-2959-4d3c-bdd0-fd8769c2a447)
11. Let try query this table
![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/cf9d52f3-86f4-407d-a5f9-64a37a546203)
We have prepared the database for the data pipeline :)

## 7. Google composer
We will use Google Composer with Airflow to create a DAG for writing and managing tasks in the Airflow system using Python code.
 1. Go to the [Google Cloud website](https://cloud.google.com/gcp?utm_source=google&utm_medium=cpc&utm_campaign=na-CA-all-en-dr-bkws-all-all-trial-e-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_665735450633-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt_Google%20Cloud-KWID_43700077224548586-kwd-6458750523&utm_term=KW_google%20cloud-ST_google%20cloud&gclid=Cj0KCQjw2qKmBhCfARIsAFy8buJTDdaAzub_a5_LvTWYEFgQAdcgtYCSYz1NRtQip1_QFm1UJRn_dnMaAiITEALw_wcB&gclsrc=aw.ds&hl=th).
 2. Find Google Composer in Google Cloud to create a cluster.

 ![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/4ccbd050-abd5-48d6-a1bd-396b2c8c0bf8)

  3. Wait for 15-30 minutes to create the `environment`. ( When you create a Composer environment, you will also get Google Cloud (data lake) included, so you don't need to create an extra one. )
 4. But in this case, I want to use another cloud to store all the data that is generated during the process.
 5. Let create **google cloud => buckets => create => region**  create the same region as the one where Composer is created.
 
 ![image](https://github.com/mphothanachai/Workshop-data-engineer/assets/137395742/45e371f0-a402-4ae4-bb0a-a943aa4a1b77)
 
6. Go into Composer airflow and search for `PyPI packages` to install for all tasks. In this case installs`pandas`

![image](https://github.com/mphothanachai/Workshop-data-engineer/assets/137395742/60e28075-bd52-443b-a390-b11c47607f3f)

 7. Click on the`Airflow webserver` , then click on `Admin`, and finally select `Connections`.
 ![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/e62c72e0-5ee6-48cb-8f5d-da9fe683aff0)

8. Find mysql_default and set connection (credential)

![image](https://github.com/mphothanachai/Workshop-data-engineer/assets/137395742/16655eae-d679-4c55-bf1a-9aa5adddea6e)

9. Click on the `Cloud Shell` on the right side => Editor to create dag.py for the task execution.![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/20987a1e-22a6-4b93-8c5a-c0c27b823e2f) 
 Create python file![image](https://github.com/mphothanachai/Workshop-data-engineer-/assets/137395742/5986b852-606d-4337-905e-009b04b0545b)
10. Begin the Python file by  `import`  modules that used in this task.
```
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
import pandas as pd
from datetime import datetime, timedelta
```
11. Set the  `variables`  used in this project.
```
#path and {{ ds }} = date today
raw_output_path = "gs://datalakelake/raw_data/raw_data_{{ ds }}.csv"
clean_output_path = "gs://datalakelake/clean_data/clean_data_{{ ds }}.csv"
```
12. Begin by building the first function use `pandas` to query data from `PostgreSQL`  tables and `convert`  the data into a CSV file from path
```
def  extract_DB(raw_path):
postgres = PostgresHook(postgres_conn_id='postgres_default')
df = postgres.get_pandas_df(sql="SELECT * FROM userbase")
df.to_csv(raw_path, index=False)
```
13. The next step is a bit lengthy, so I'll explain it in more detail through the following commands.
```
def  clean_data(raw_path, clean_path):
	df = pd.read_csv(raw_path)
	df['Join_Date'] = pd.to_datetime(df['Join_Date'])
	df['Last_Payment_Date'] = pd.to_datetime(df['Last_Payment_Date'])
	
	df['Subscription_period'] = (df['Last_Payment_Date'].dt.year - df['Join_Date'].dt.year) * 12 + \
	df['Last_Payment_Date'].dt.month - df['Join_Date'].dt.month
	df = df.rename(columns={'Subscription_period': 'Subscription_period_(Month)'})
	
	df["Plan_Duration"] = df["Plan_Duration"].apply(lambda  x: x.replace(" Month", "")).astype(int)
	
	df = df.rename(columns={'Plan_Duration': 'Plan_Duration_(Month)'})
	
	df['THB_Bath'] = df['Subscription_Type'].map({'Basic': 169, 'Standard': 349, 'Premium': 419})
	
	df["Revenue(Bath)"] = df["Plan_Duration_(Month)"] * df["Subscription_period_(Month)"] * df["THB_Bath"]
	df.to_csv(clean_path, index=False)
```
**Begin with  this command use pandas read csv and  use the DataFrame `df` to convert the selected column into a datetime format.**
```
df = pd.read_csv(raw_path)
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
df['Last_Payment_Date'] = pd.to_datetime(df['Last_Payment_Date'])
```
**In this command, it calculates the number of months that a customer has subscribed after converting the datetime. In the previous command, it uses `.year` to extract the year from a column and then subtracts it from another column, e.g., 2023 (latest subscription year) - 2022 (starting year), resulting in 1 year. Then, by multiplying it by 12, you get the number of months. Similarly, `.month` is used in the same way.**
```
df['Subscription_period'] = (df['Last_Payment_Date'].dt.year - df['Join_Date'].dt.year) * 12 + \
df['Last_Payment_Date'].dt.month - df['Join_Date'].dt.month

df = df.rename(columns={'Subscription_period': 'Subscription_period_(Month)'})
```
**In this function use lamda to change "Month" it is string in this column and change type to int.**
```
df["Plan_Duration"] = df["Plan_Duration"].apply(lambda  x: x.replace(" Month", "")).astype(int)
df = df.rename(columns={'Plan_Duration': 'Plan_Duration_(Month)'})
```
**Use function map to find str in dict{} and change after that multiply all column ,that is an integer.Convert to csv**
```
df['THB_Bath'] = df['Subscription_Type'].map({'Basic': 169, 'Standard': 349, 'Premium': 419})
df["Revenue(Bath)"] = df["Plan_Duration_(Month)"] * df["Subscription_period_(Month)"] * df["THB_Bath"]
df.to_csv(clean_path, index=False)
```
14. Create Default Arguments to define the **DAG's** workflow as follows
```
with DAG(
	"dag",
	schedule_interval=" 0 0 * * * ", #work on midnight(with cron)
	tags=["project"]
) as dag:
15. Create tasks to use functions and assign tasks. Use PythonOperator for use Python code and call the function (extract_postgresql). Apply kwargs (Keyword Argument) to provide the value for the raw_output_path variable t2 is same thing.

```
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
```
16. Do you remember that when creating a Composer instance, we receive a Cloud Storage bucket? We will use this bucket to connect to Snowflake. First, in task t3, the files from the "clean_data" folder will be copied to the designated folder for Snowflake integration.

17. In task t4, the files with the previous day's date in the Snowflake folder, usually named as "clean_data_2023-8-16," will be deleted. The date will keep changing, and we're removing the files from the previous day to ensure that only the latest files remain for easier data retrieval.
```
t3 = BashOperator(
	task_id="copy_to_stage_snowflake",
	bash_command="gsutil cp gs://datalakelake/clean_data/clean_data_{{ ds }}.csv gs://us-south1-airflow-c53bbfb7-bucket/data/",
)
t4 = BashOperator(
	task_id="romove_lastdate_file",
	bash_command='gsutil rm gs://us-south1-airflow-c53bbfb7-bucket/data/clean_data_$(date -d "yesterday" +%Y-%m-%d).csv',
)
```
18. Setting up Dependencies for Determine the order in which tasks should be executed.
```
t1 >> t2 >> t3 >> t4
```
19. Don't be surprised that the tasks end here. In reality, you need to proceed to work in Snowflake to pull data from GCP according to the schedule. :3
