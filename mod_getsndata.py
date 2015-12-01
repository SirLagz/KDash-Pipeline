def get_sn_table_data(instance, user, password, table, format, querytype, querytime ):
    import requests

    types = {
        "updated":"sys_updated_on",
        "created":"sys_created_on",
        "closed":"closed_at",
        "resolved":"u_resolved",
        "completed":"u_completed",
        "startdate":"start_date"
    }

    queries = {
        "ThisMonth": "This%20month%40javascript%3Ags.beginningOfThisMonth()%40javascript%3Ags.endOfThisMonth()",
        "LastMonth": "Last%20month%40javascript%3Ags.beginningOfLastMonth()%40javascript%3Ags.endOfLastMonth()",
        "Last6Months": "Last%206%20months%40javascript%3Ags.monthsAgoStart(6)%40javascript%3Ags.endOfThisMonth()",
        "Last12Months": "Last%2012%20months%40javascript%3Ags.monthsAgoStart(12)%40javascript%3Ags.endOfThisMonth()"
    }

    qtype = types.get(querytype)
    qtime = queries.get(querytime)
    query = "sysparm_query="+qtype+"ON"+qtime



    urlBase = "https://"+instance+".service-now.com"
    urlTable = urlBase+"/"+table+".do?"+format
    urlQuery = urlTable+"&"+query

    jsonData = requests.get(urlQuery,auth=(user,password))

    return jsonData.text
