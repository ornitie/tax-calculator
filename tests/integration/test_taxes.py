import json
import unittest

from src.utils.parser import Parser
from src.taxes.tax_service import TaxService


class TaxesTestCase(unittest.TestCase):

    f = open("./tests/integration/data_case_scenarios.json")
    data = json.load(f)

    def test_case_1(self):
        input = Parser.parse_json(self.data[0]["input"])
        expected = self.data[0]["output"]

        actual = TaxService.calculate_taxes(input)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        input = Parser.parse_json(self.data[1]["input"])
        expected = self.data[1]["output"]

        actual = TaxService.calculate_taxes(input)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        input = Parser.parse_json(self.data[2]["input"])
        expected = self.data[2]["output"]

        actual = TaxService.calculate_taxes(input)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        input = Parser.parse_json(self.data[3]["input"])
        expected = self.data[3]["output"]

        actual = TaxService.calculate_taxes(input)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        input = Parser.parse_json(self.data[4]["input"])
        expected = self.data[4]["output"]

        actual = TaxService.calculate_taxes(input)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        input = Parser.parse_json(self.data[5]["input"])
        expected = self.data[5]["output"]

        actual = TaxService.calculate_taxes(input)

        self.assertEqual(expected, actual)
