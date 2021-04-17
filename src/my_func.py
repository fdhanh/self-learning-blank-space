from datetime import datetime

def getValue(jfile, column):
    value = []
    for entity in jfile[column]:
        value.append(entity['name'])
    if len(value) == 0:
        return None
    return ', '.join(value)

def getColumn(jfile):
    columns_req = ['original_title', 'budget', 'genres', 
                'popularity', 'release_date', 'revenue', 
                'runtime', 'vote_average', 'vote_count', 
                'spoken_languages']
    temp_dict = {}
    for col in columns_req:
        if col in ['genres', 'spoken_languages']:
            temp_dict[col] = getValue(jfile, col)            
        else:
            temp_dict[col] = jfile[col]
    return temp_dict

def error_rpt(error_msg, file_name):
    with open("output/error_rpt.txt", "a") as f:
        f.write(f"Error on file: {file_name.split('/')[-1]} \nError message: {error_msg} \n\n")

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("output/logfile.txt","a") as f:
        f.write(f"{timestamp}, {message}\n")
