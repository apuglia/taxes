import csv
from collections import defaultdict
from datetime import datetime

# Read data
with open('monarch-transactions.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    transactions = list(reader)

# Filter by year
def filter_year(txns, year):
    return [t for t in txns if t['Date'].startswith(str(year))]

# Summarize
def summarize(txns, year):
    income = 0
    expenses = 0
    by_category = defaultdict(float)
    by_account = defaultdict(lambda: {'income': 0, 'expenses': 0})
    
    for t in txns:
        try:
            amt = float(t['Amount'])
        except:
            continue
        
        cat = t['Category'] or 'Uncategorized'
        acct = t['Account'] or 'Unknown'
        
        if amt > 0:
            income += amt
            by_account[acct]['income'] += amt
        else:
            expenses += abs(amt)
            by_category[cat] += abs(amt)
            by_account[acct]['expenses'] += abs(amt)
    
    print(f"\n{'='*60}")
    print(f"TAX YEAR {year}")
    print(f"{'='*60}")
    print(f"\nTransactions: {len(txns)}")
    print(f"\nTOTAL INCOME:   ${income:,.2f}")
    print(f"TOTAL EXPENSES: ${expenses:,.2f}")
    print(f"NET:            ${income - expenses:,.2f}")
    
    print(f"\n--- Income by Account ---")
    for acct, vals in sorted(by_account.items(), key=lambda x: -x[1]['income']):
        if vals['income'] > 0:
            print(f"  {acct[:45]:45} ${vals['income']:>12,.2f}")
    
    print(f"\n--- Top Expense Categories ---")
    for cat, amt in sorted(by_category.items(), key=lambda x: -x[1])[:15]:
        print(f"  {cat:30} ${amt:>12,.2f}")
    
    return income, expenses

# Analyze 2023 and 2024
txns_2023 = filter_year(transactions, 2023)
txns_2024 = filter_year(transactions, 2024)

inc_23, exp_23 = summarize(txns_2023, 2023)
inc_24, exp_24 = summarize(txns_2024, 2024)

print(f"\n{'='*60}")
print("SUMMARY FOR TAX FILING")
print(f"{'='*60}")
print(f"\n2023: Income ${inc_23:,.2f} | Expenses ${exp_23:,.2f}")
print(f"2024: Income ${inc_24:,.2f} | Expenses ${exp_24:,.2f}")
