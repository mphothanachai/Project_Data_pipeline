# Project_Data_pipeline
Data pipeline with (postgresql to googlecloud to snowflek) base on airfow

# Postgre Database (Prepare)

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

## pgAdmin (postgresql)
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

5.  **_Aah!_** I have some problem .I got error of different "datestyle"

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
