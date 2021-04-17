import json
from .banyakfile import *
from glob import glob

def startETL():
    log("ETL Job Started")
    log("Extract and transform phase Started")
    n_file = 0
    jfiles = []
    files = glob("data/movies/movies/*.json")
    print(len(files))
    for jfile in files:
        try:
            with open(jfile, encoding="utf8") as f:
                jfiles.append(getColumn(json.load(f)))
        except ValueError as e:
            error_rpt(e, jfile)
            log(f"Error found at file {jfile.split('/')[-1]}")
        print(f"extract processed {n_file} of {len(files)}")
        n_file+=1
        
    log("Extract and transform phase Ended")
    log("Load phase Started")
    with open('output/output_data.json', 'w', encoding="utf8") as outfile:
        json.dump(jfiles, outfile)
    log("Load phase Ended")
    log("ETL Job Ended")
