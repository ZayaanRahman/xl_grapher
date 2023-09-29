import sys
import pandas as pd


# get data from Excel file "file_name", if file exists in directory
def get_data(file_name):
    try:
        # TODO: Convert excel to csv, pd parses csv faster
        data = pd.read_excel(file_name)
        print("data loaded successfully.")
    except FileNotFoundError:
        print("file does not exist.")
        sys.exit()

    clean_data(data)
    return data


# remove NaN values from dataframe
# also removed 0s and values after space in col?
def clean_data(data):
    data.dropna(inplace=True)
