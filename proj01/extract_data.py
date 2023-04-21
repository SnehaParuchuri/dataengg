import json
import sys
import csv
import logging

logging.basicConfig(filename = "proj01\\logfiles\\log.txt", level = logging.INFO,
    format = f"%(asctime)s %(levelname)s %(lineno)s %(message)s")
log = logging.getLogger('sample logger')
log.setLevel(logging.INFO)
csv_r_file = None
def performAction(sqlData):
    log.info(f"processing {sqlData['sql_num']}")
    if(sqlData['action'].startswith('read')):
        readFunc(sqlData, config_data[primary_key])
    elif (sqlData['action'].startswith('write')):
        writeFunc(sqlData, config_data[primary_key])
    return

def readFunc(sqlData, config_data):
    try:   
        if('location' not in sqlData.keys()):
            log.info("There's no location to read the file from")
            sys.exit(0)

        file_type = sqlData['action'].split('|')[1]
        # print(sqlData)
        match file_type:
            case 'csv':
                readCsv(sqlData['location'])

        
        log.info(csv_r_file)
        for data in config_data:
            if(data['sql_num'] == sqlData['next_sql']):
                performAction(data)
    except:
        log.info("Encountered an exception in read function")
    return

def writeFunc(sqlData, config_data):
    try:
        if('location' not in sqlData.keys()):
            log.info("There's no location to write the file into")
            sys.exit(0)
        if(csv_r_file == None):
            log.info("There's no file to read")
            sys.exit(0)
        writeCsv(sqlData['location'])
        for data in config_data:
            if(data['sql_num'] == sqlData['next_sql']):
                performAction(data)
    except:
        log.info("Encountered an exception in write function")
    return

def readCsv(location):
    global csv_r_file
    log.info(location)
    csv_r_file = csv.reader(open(location, 'r'))
    return

def writeCsv(location):
    writer = csv.writer(open(location, 'w'))
    for row in csv_r_file:
        writer.writerow(row)

primary_key = "sql_steps"

validate_process_keys = ["sql_num", "action", "next_sql"]

file = open("D:\\training-UI\\python\\proj01\\config.json")

config_data = json.load(file)



if(primary_key not in config_data.keys()):
    log.info("Invalid Json")
    sys.exit(0)

for sqlData in config_data[primary_key]:
    for key in validate_process_keys:
        if(key not in sqlData.keys()):
            log.info(f'{key_name} is not found in the given data')
            sys.exit(0)

accepted_action = ['read', 'read', 'write']
acceptable_data = []

for sqlData in config_data[primary_key]:
    sqlData['sql_num'] = int(sqlData['sql_num'])
    sqlData['next_sql'] = int(sqlData['next_sql'])
    # print(sqlData['sql_num'])
    if(sqlData['sql_num'] == 1):        
        for act in accepted_action:
            if(sqlData['action'].startswith(act)):
                acceptable_data.append(sqlData)
                break
        
    # print(sqlData)

log.info(acceptable_data)

if(len(acceptable_data) <= 0):
    log.info('Could not find step 1 to start with')
    sys.exit(0)

performAction(acceptable_data[0])


