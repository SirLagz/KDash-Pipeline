#!/usr/bin/python3
import os
import mod_trimsndata
import mod_getsndata
import mod_loadsndata
import time
import subprocess

instance = os.environ['SNINSTANCE']
username = os.environ['SNUSERNAME']
password = os.environ['SNPASSWORD']
table = os.environ['SNTABLE']
query = "updated"
timeframe = "Last6Months"
database = "KDash"

fields = ["assigned_to","assignment_group","category","contact_type","description","number","opened_at","opened_by","priority","short_description","state","sys_class_name","sys_created_on","sys_id","sys_updated_on","u_req_priority","u_requestor","u_affected_contact","u_business_service","u_resolution_code","u_resolution_reason","u_sla_progress"]

test = subprocess.Popen(["/etc/init.d/mongodb","start"])

mongorunning = 0

while mongorunning == 0:
    print("Checking for mongo connection")
    mongorunning = mod_loadsndata.check_connection()
    if mongorunning == 0:
        print("Mongo not running. Trying again in 120 seconds")
        time.sleep(120)
    else:
        print("Mongo is running. Continuing")

data = mod_getsndata.get_sn_table_data(instance, username, password, table, query, timeframe)

records = mod_trimsndata.trim_sn_data(data,fields)

for record in records:
    mongoid = mod_loadsndata.update_mongo_collection(database,table,records[record])
    print("Upserted "+str(mongoid))


while True:
    time.sleep(1800)
    data = mod_getsndata.get_sn_table_data(instance, username, password, table)
    records = mod_trimsndata.trim_sn_data(data,fields)
    mongoid = mod_loadsndata.update_mongo_collection(database,table,records[record])
    print("Upserted "+str(mongoid))
