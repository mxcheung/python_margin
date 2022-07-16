# tpm_margin_processor
# Purpose process raw date.


def map_row(row, client):
    row['messageType'] = message_type(row)
    row['version'] = '003'
    row['siteCode'] = 'MG'
    row['originator'] = 'EXCHANGE'
    row['valueDate'] = '20220716'
    row['level'] = 'CLIENT'
    row['clientType'] = client['clientType']
    row['clientNumber'] = client['clientNumber']
    row['accountNumber'] = client['accountNumber']
    row['subaccountNumber'] = client['subaccountNumber']
    row['marginExchangeCode'] = 'XTFF'
    row['externalMember'] = '9111'
    row['oppositePartyCode'] = 'DEFCFD'
    row['marginCalculationMethod'] = ''
    row['currencyCode'] = 'JPY'
    row['marginAmount'] = '212698.00'
    row['marginAmountDC'] = 'D'
    return row

# Row mappings here

#  message_type
#  return MAR
def message_type(row):
    return 'MAR'

