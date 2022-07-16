# This is a sample Python script.

# tpm_margin_writer
# Purpose write margin records in TPM CSV format.


TPM_CSV = ['sequenceNumber', 'messageType', 'version', 'siteCode', 'originator', 'valueDate',
           'level', 'clientType', 'clientNumber', 'accountNumber', 'subaccountNumber',
           'marginExchangeCode', 'externalMember', 'oppositePartyCode', 'marginCalculationMethod',
           'currencyCode', 'marginAmount', 'marginAmountDC']


def create_margin_file(df):
    return df[TPM_CSV]
