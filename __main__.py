import json
from src.taxes.tax_service import TaxService
from src.transaction.transaction import Transaction
from src.utils.parser import Parser

if __name__ == "__main__":
    json_input = json.loads(input())
    transactions = Parser.parse_json(json_input)

    taxes = TaxService.calculate_taxes(transactions)

    print(taxes)
