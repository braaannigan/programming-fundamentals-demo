import datetime
import concurrent.futures
import time
from typing import List

import numpy as np
import pandas as pd 
import polars as pl

def generateUrl(dataset_id:str, metadata:List[str], columns:List[str], start_date:str, end_date:str):
    # Set ERDDAP server details
    s = 'https://erddap.marine.ie/erddap'
    p = 'tabledap'
    r = 'csv'
    param = ','.join(columns)
    combinedMetadata = metadata + [param]

    # Generate parameter component of URL
    plist = ''
    for item in combinedMetadata:
        plist = f"{plist}{item}%2C"
    plist = plist[0:-3]
    # Create ERDDAP url and load data for selected dates  
    url = f"{s}/{p}/{dataset_id}.{r}?{plist}&time%3E={start_date}T00:00:00Z&time%3C{end_date}T23:59:59Z"
    return url

def fetchDataFromERDDAP(dataset_id:str, metadata:List[str], columns:List[str], start_date:str, end_date:str,engine:str='c',index=None):
    try:
        url = generateUrl(dataset_id=dataset_id,metadata=metadata, columns=columns, start_date=start_date, end_date=end_date)        
        if engine == 'c':
            skiprows = [1]
        else:
            skiprows = None
        startTime = time.time()
        df= pd.read_csv(url,skiprows=skiprows,index_col=[0],parse_dates=True,engine=engine)
        if engine == 'pyarrow':
            df = df.iloc[1:]
        endTime = time.time()
        print(f"Download and parse: {round(endTime-startTime,3)} seconds")

        #Replace all NaN values with -5
        df = df.fillna(-5)

        return (df,index)
    except Exception as e:
        print(e)