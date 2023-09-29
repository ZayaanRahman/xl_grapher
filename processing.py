# get data from Excel file and remove NaN values
import sys
import pandas as pd


# get data from Excel file "file_name", if file exists in directory
def get_data(file_name):
    try:
        data = pd.read_excel(file_name)  # TODO: Convert excel to csv, pd parses csv faster
        print("data loaded successfully.")
    except FileNotFoundError:
        print("file does not exist.")
        sys.exit()

    clean_data()
    return data


# remove NaN values from dataframe
def clean_data():
    
    
    return
