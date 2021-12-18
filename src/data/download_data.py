#Scripts to download data 

import pandas as pd

def download_positives(urls: list, dir_save: list):
    #Read csv files and then save them as json
    for i in range(len(urls)):
        pd.read_csv(urls[0]).to_json(dir_save[i], orient='records')