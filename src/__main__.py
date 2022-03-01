import json
from transaction import Transaction

transactions = json.loads(input())
transaction = input()
ans = []
losses, stocks_amount, stocks_value = 0, 0, 0

for transaction in transactions:
    print(transaction)
    transaction = Transaction(
        transaction["operation"], transaction["unit-cost"], transaction["quantity"]
    )
    print("this is", transaction)
    if transaction.type == Transaction.BUY:
        stocks_amount += transaction.quantity
        stocks_value += transaction.cost * transaction.quantity
        ans.append(json.dumps({"tax": 0}))
    if transaction.type == Transaction.SELL:
        average = (stocks_value) / stocks_amount
        balance = abs((average - transaction.cost) * transaction.quantity)
        if transaction.cost == average:
            print("nothing", balance, transaction.cost, average, stocks_amount, stocks_value)
            ans.append(json.dumps({"tax": 0}))
        
        if transaction.cost < average:
            print("LOSS", balance, transaction.cost, average, stocks_amount, stocks_value)
            losses = balance
            ans.append(json.dumps({"tax": 0}))

        if transaction.cost > average:
            if transaction.quantity * transaction.cost < 20000:
                ans.append(json.dumps({"tax": 0}))
                continue
            print("PROFIT", balance, f'losses: {losses}')
            if losses > balance:
                losses -= balance
                balance = 0
            else:
                balance -= losses
                losses = 0

            taxes = balance * 0.2
            print("taxes:", taxes, 'balance', balance, 'losses', losses)
            ans.append(json.dumps({"tax": taxes}))

        print(
            losses,
            average,
            transaction.cost,
            f"loss: {balance}" if balance > 0 else f"profit: {balance}",
        )
print(ans)
