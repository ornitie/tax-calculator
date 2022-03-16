import json
from src.transaction.transaction import Transaction


class TaxService:
    @classmethod
    def calculate_taxes(cls, transactions: list[Transaction]) -> list[dict]:
        taxes = []
        losses = 0
        stocks_amount_mapper, stocks_value_mapper = {}, {}

        for transaction in transactions:
            if (
                transaction.ticker not in stocks_amount_mapper
                or transaction.ticker not in stocks_value_mapper
            ):
                (
                    stocks_amount_mapper[transaction.ticker],
                    stocks_value_mapper[transaction.ticker],
                ) = (0, 0)

            transaction_tax = 0
            if transaction.type == Transaction.BUY:
                stocks_amount_mapper[transaction.ticker] += transaction.quantity
                stocks_value_mapper[transaction.ticker] += (
                    transaction.cost * transaction.quantity
                )

            stocks_amount, stocks_value = (
                stocks_amount_mapper[transaction.ticker],
                stocks_value_mapper[transaction.ticker],
            )

            if transaction.type == Transaction.SELL:
                if transaction.quantity > stocks_amount:
                    taxes.append(
                        json.dumps({"error": "Can't sell more stocks than you have"})
                    )
                    continue

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

            taxes.append(json.dumps({"tax": transaction_tax}))

        return cls.__format_taxes(taxes)

    def __format_taxes(taxes: list[float]) -> list[dict]:
        return [json.loads(tax) for tax in taxes]
