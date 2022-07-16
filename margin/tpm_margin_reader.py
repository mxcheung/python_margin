# This is a sample Python script.

# tpm_margin_reader
# Purpose read raw data
import pandas as pd


def get_margin_records_from_file():
    input_df = pd.read_csv('student.csv')
    return input_df
