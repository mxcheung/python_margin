# tpm_margin_processor
# Purpose process raw date.

from margin import tpm_margin_mapper
import pandas as pd


def process(input_df):
    data = []
    for row_number, row in input_df.iterrows():
        client = get_client(row)
        row = tpm_margin_mapper.map_row(row, client)
        row['sequenceNumber'] = row_number
        data.append(row)
    return pd.DataFrame(data)


##########################################
# Dataframe mappings here

#  postcode
#  if gender is female return 008 if female
#  otherwise return 007
def postcode(df):
    df['postcode'] = '2035'
    return df


#  version
#  if gender is female return 008 if female
#  otherwise return 007
def version(row):
    if row['gender'] == 'female':
        return '008'
    else:
        return '007'


def get_client(row):
    client_1 = {'clientType': 'ABC', 'clientNumber': '1115', 'accountNumber': '1', 'subaccountNumber': '4'}
    client_2 = {'clientType': 'MM', 'clientNumber': '9784', 'accountNumber': '1', 'subaccountNumber': '1'}
    if row['gender'] == 'female':
        return client_1
    else:
        return client_2
