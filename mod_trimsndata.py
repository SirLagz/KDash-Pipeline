#!/usr/bin/python

def trim_sn_data(jsondata,fields,id='_id'):
    import json
    field = set(fields)

    data = json.loads(jsondata)

    newdata = {}

    for record in data['records']:
        tr = {}
        for key in record:
            if key in field:
                tr[key] = record[key]
        tr[id] = tr['sys_id']
        newdata[tr['sys_id']] = tr

    return newdata
