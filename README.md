# ETL Process
In industry, a data person will often be dealing with large or much data. The purpose of this task is you can extract, transform, and load it into one file from a combination of several files in a folder (in this repository, the data is in the data folder). 

## Process
- Extract: Reading a file.
- Transform: Take some of the fields as needed (in this case, there are 10 fields) and take genres & languages field as needed.
- Load: From combined all files then the files are merged and saved in output_file.json

## Output
You can download output file <a href = "https://drive.google.com/drive/folders/1uIpGUDo1oI41DPztmhDoykRGXKzAmoT5?usp=sharing"> here <a>
There are 3 output files:
- logfile: Showing log from each process
- error_rpt: Showing error report when process running
- output_data: Result from this ETL process

## Installation
Use git to clone this repository
```
git clone https://github.com/fdhanh/self-learning-blank-space.git
```
## How To Use
1. Make sure you have .json file or you can download here <a href="https://drive.google.com/file/d/15Py0Z-lrKdR7K6sz3l8usgCfRGD0jE6_/view?usp=sharing">here</a> and place it into folder ```data```
2. Type this on your command prompt: ```python main.py```
