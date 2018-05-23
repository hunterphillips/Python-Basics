stockDict = {'GM': 'General Motors',
             'CAT': 'Caterpillar', 'EK': 'Eastman Kodak', 'GE': 'General Electric'}

purchases = [('GE', 100, '10-sep-2001', 48.74),
             ('CAT', 100, '1-apr-1999', 24.25),
             ('GM', 300, '1-oct-1998', 56.01),
             ('EK', 75, '21-jul-1998', 56.01),
             ('GE', 200, '2-jul-1998', 56.01),
             ('GM', 150, '3-jun-1998', 56.01)
             ]


# Create report showing full purchase price (shares times dollars) for each stock
def makePurchaseHistory(stocks, buys):
    purchaseHistory = []
    for buy in buys:  # Match purchase ticker with stock name, compute total price
        purchaseHistory.append(
            {'Company': stocks[buy[0]], 'Ticker': buy[0],
             'Purchase Total': buy[1]*buy[3]})
    return purchaseHistory


purchaseHistroy = makePurchaseHistory(stockDict, purchases)
print('history', purchaseHistroy)

# Create a report that accumulates total investment by ticker symbol.
purchaseSummary = {}
for record in purchaseHistroy:
    if record['Ticker'] in purchaseSummary:  # if key exists, add to total
        purchaseSummary[record['Ticker']] += record['Purchase Total']
    else:
        purchaseSummary[record['Ticker']] = record['Purchase Total']
print('\nsummary', purchaseSummary)
