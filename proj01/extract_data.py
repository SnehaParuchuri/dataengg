import json
import sys

primary_key = "sql_steps"

validate_process_keys = ["sql_num", "action", "next_sql"]

file = open("D:\\training-UI\\python\\proj01\\config.json")

config_data = json.load(file)


if(primary_key not in config_data.keys()):
    print("Invalid Json")
    sys.exit(0)

for sqlData in config_data[primary_key]:
    for key in validate_process_keys:
        if(key not in sqlData.keys()):
            print(f'{key_name} is not found in the given data')
            sys.exit(0)

accepted_action = ['read|database', 'read|parquet', 'write|parquet']
acceptable_data = []

for sqlData in config_data[primary_key]: 
    if(sqlData['sql_num'] == '1' or sqlData['sql_num'] == 1):   
        sqlData['sql_num'] = int(sqlData['sql_num'])
        if(sqlData['action'] in accepted_action) :
            acceptable_data.append(sqlData)
        
    # print(sqlData)

# print(acceptable_data)

for sqlData in acceptable_data:
    for key_name in sqlData.keys():
        if(key_name not in validate_process_keys):
            print(f'Invalid key {key_name} in the given data')
            sys.exit(0)

