import json
from src.transaction.transaction import Transaction


class TaxService:
    @classmethod
    def calculate_taxes(cls, transactions: list[Transaction]) -> list[dict]:
        taxes = []
        losses, stocks_amount, stocks_value = 0, 0, 0

        for transaction in transactions:
            transaction_tax = 0
            if transaction.type == Transaction.BUY:
                stocks_amount += transaction.quantity
                stocks_value += transaction.cost * transaction.quantity

            if transaction.type == Transaction.SELL:
                average = stocks_value / stocks_amount
                balance = abs((average - transaction.cost) * transaction.quantity)

                if transaction.cost < average:
                    losses = balance

                elif transaction.cost > average:
                    if transaction.quantity * transaction.cost > 20000:
                        if losses > balance:
                            losses -= balance
                            balance = 0
                        else:
                            balance -= losses
                            losses = 0

                        transaction_tax = balance * 0.2

            taxes.append(transaction_tax)

        return cls.__format_taxes(taxes)

    def __format_taxes(taxes: list[float]) -> list[dict]:
        return [json.loads(json.dumps({"tax": tax})) for tax in taxes]
