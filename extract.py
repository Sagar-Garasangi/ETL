import pandas as pd
from datetime import datetime
import requests 
import json
import pyarrow
import time
link= "https://dummyjson.com/users"
def extract(url,record):
    response_data=[]
    skip=0
    limit=100
    while True:
        try:
            temp=requests.get(url,params={"skip":skip,"limit":limit},timeout=25)
            status=temp.status_code
            if(status==429):
                time.sleep(10)
                continue
            temp.raise_for_status()
            temp_data=temp.json()
            temp_data=temp_data[record]
            if(not temp_data):
                break
            response_data.extend(temp_data)
            skip+=limit
           
        except requests.RequestException as e:
            print(f"error{e}")
            break
    latest=datetime.now()
    return response_data
df=extract(link,"users")
df=pd.json_normalize(df)
print(df.info())
df.to_parquet("users.parquet")
latest=datetime.now()
print("Extraction Successfull")