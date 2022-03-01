from src.transaction.transaction import Transaction


class Parser:
    def parse_json(json_input):
        transactions = []
        for transaction in json_input:
            transactions.append(
                Transaction(
                    transaction["operation"],
                    transaction["unit-cost"],
                    transaction["quantity"],
                )
            )

        return transactions
