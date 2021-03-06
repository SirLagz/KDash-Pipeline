#!/usr/bin/python3
import mod_trimsndata
import mod_getsndata

parser = argparse.ArgumentParser(description="Gets a ServiceNow table and returns the JSON")
parser.add_argument("--instance","-i", help="ServiceNow Instance name to access", required=True)
parser.add_argument("--user","-u", help="ServiceNow User", required=True)
parser.add_argument("--password","-p", help="Password for ServiceNow User", required=True)
parser.add_argument("--table","-t",help="ServiceNow Table to retrieve", required=True, choices=['incident','u_request','change_request'])
parser.add_argument("--format","-f",help="Export format - Defaults to JSON",default="JSONv2", choices=['JSONv2','XML'])
parser.add_argument("--query","-q",help="URL Query to run against the table - Default is updated",default="updated",choices=['updated','created','closed','resolved','completed','startdate'])
parser.add_argument("--time","-d",help="Time period for Query to be run against - Default is ThisMonth",default="ThisMonth",choices=['ThisMonth','LastMonth','Last6Months','Last12Months'])

args = parser.parse_args()

fields = ["assigned_to","assignment_group","category","contact_type","description","number","opened_at","opened_by","priority","short_description","state","sys_class_name","sys_created_on","sys_id","sys_updated_on","u_req_priority","u_requestor","u_affected_contact","u_business_service","u_resolution_code","u_resolution_reason","u_sla_progress"]

data = mod_getsndata.get_sn_table_data(args.instance, args.user, args.password, args.table, args.query, args.time, args.format)

newdata = mod_trimsndata.trim_sn_data(data,fields)

print(newdata)
