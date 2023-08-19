# create intergration for connect external source or cloud service
CREATE STORAGE INTEGRATION new_gcp
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'GCS'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('gcs://location_bucket/data/')

# this command will show detail of intergration(service account)
DESC STORAGE INTEGRATION new_gcp;

# To create table and cloumns
CREATE OR REPLACE TABLE User_Subscriptions (
  User_ID INT,
  Subscription_Type STRING,
  Join_Date DATE,
  Last_Payment_Date DATE,
  Country STRING,
  Age INT,
  Gender STRING,
  Device STRING,
  Plan_Duration_Month INT,
  Subscription_period_Month INT,
  THB_Bath INT,
  Revenue_Bath INT
);

# create task
create or replace task DATA_WAREHOUSE.USERDATA.RUN_EVERYLUNCH
	warehouse=COMPUTE_WH
	schedule='USING CRON 0 12 * * * UTC' #this cron mean everyday in 12:00am
	as 
sql command

#copy to command use to copy csv to table that create
COPY INTO "DATA_WAREHOUSE"."USERDATA"."USER_SUBSCRIPTIONS"
FROM '@"DATA_WAREHOUSE"."USERDATA"."NEW_GCP_STAGE"'
PATTERN='.*.'# all csv
FILE_FORMAT = (
    TYPE=CSV,
    SKIP_HEADER=1,
    FIELD_DELIMITER=',',
    TRIM_SPACE=FALSE,
    FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
    DATE_FORMAT=AUTO,
    TIME_FORMAT=AUTO,
    TIMESTAMP_FORMAT=AUTO
)
ON_ERROR=ABORT_STATEMENT;