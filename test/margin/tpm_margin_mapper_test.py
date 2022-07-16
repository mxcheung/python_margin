# tpm_margin_processor
# Purpose process raw date.

import unittest
from margin import tpm_margin_mapper


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_map_row(self):
        client = self.client()
        row = self.data_row()
        expected = self.expected_row()
        actual = tpm_margin_mapper.map_row(row, client)
        self.assertEqual(expected, actual)

    @staticmethod
    def data_row():
        return {'accountNumber': '1',
                'clientNumber': '1234',
                'clientType': 'ABC',
                'currencyCode': 'JPY',
                'externalMember': '9111',
                'level': 'CLIENT',
                'marginAmount': '212698.00',
                'marginAmountDC': 'D',
                'marginCalculationMethod': '',
                'marginExchangeCode': 'XTFF',
                'messageType': 'MAR',
                'oppositePartyCode': 'DEFCFD',
                'originator': 'EXCHANGE',
                'siteCode': 'MG'}

    @staticmethod
    def client():
        return {'clientType': 'ABC', 'clientNumber': '1115', 'accountNumber': '1', 'subaccountNumber': '4'}

    @staticmethod
    def expected_row():
        return {'accountNumber': '1',
                'clientNumber': '1115',
                'clientType': 'ABC',
                'currencyCode': 'JPY',
                'externalMember': '9111',
                'level': 'CLIENT',
                'marginAmount': '212698.00',
                'marginAmountDC': 'D',
                'marginCalculationMethod': '',
                'marginExchangeCode': 'XTFF',
                'messageType': 'MAR',
                'oppositePartyCode': 'DEFCFD',
                'originator': 'EXCHANGE',
                'siteCode': 'MG',
                'subaccountNumber': '4',
                'valueDate': '20220716',
                'version': '003'}


if __name__ == '__main__':
    unittest.main()
