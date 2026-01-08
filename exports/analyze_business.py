import csv

with open('monarch-transactions.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    transactions = list(reader)

# Look for LLC-related transactions
keywords = ['PANAMERICAN', 'CANNUMATE', 'VERGINCETRIX', 'REDI SERVICIOS', 'WHITE HAT', 
            'MERCURY', 'LLC', 'CONSULTING', 'PROMACECA']

print("="*80)
print("BUSINESS/LLC RELATED TRANSACTIONS (2023-2024)")
print("="*80)

for year in [2023, 2024]:
    print(f"\n--- {year} ---")
    txns = [t for t in transactions if t['Date'].startswith(str(year))]
    
    business_txns = []
    for t in txns:
        statement = (t['Original Statement'] or '').upper()
        merchant = (t['Merchant'] or '').upper()
        account = (t['Account'] or '').upper()
        
        if any(kw in statement or kw in merchant or kw in account for kw in keywords):
            business_txns.append(t)
    
    # Sort by amount
    business_txns.sort(key=lambda x: -abs(float(x['Amount'] or 0)))
    
    total_in = sum(float(t['Amount']) for t in business_txns if float(t['Amount'] or 0) > 0)
    total_out = sum(abs(float(t['Amount'])) for t in business_txns if float(t['Amount'] or 0) < 0)
    
    print(f"Total incoming: ${total_in:,.2f}")
    print(f"Total outgoing: ${total_out:,.2f}")
    print(f"\nTransactions:")
    
    for t in business_txns[:20]:
        amt = float(t['Amount'] or 0)
        direction = "IN " if amt > 0 else "OUT"
        print(f"  {t['Date']} | {direction} ${abs(amt):>10,.2f} | {t['Account'][:35]} | {t['Merchant'][:25]} | {t['Original Statement'][:40]}")

# Check Mercury account specifically (business account)
print(f"\n{'='*80}")
print("MERCURY CHECKING ACCOUNT (Business Account)")
print("="*80)

mercury = [t for t in transactions if 'MERCURY' in (t['Account'] or '').upper() or 'MERCURY' in (t['Original Statement'] or '').upper()]

for year in [2023, 2024]:
    year_txns = [t for t in mercury if t['Date'].startswith(str(year))]
    if year_txns:
        income = sum(float(t['Amount']) for t in year_txns if float(t['Amount'] or 0) > 0)
        expenses = sum(abs(float(t['Amount'])) for t in year_txns if float(t['Amount'] or 0) < 0)
        print(f"\n{year}: Income ${income:,.2f} | Expenses ${expenses:,.2f}")
        for t in sorted(year_txns, key=lambda x: -abs(float(x['Amount'] or 0)))[:10]:
            amt = float(t['Amount'] or 0)
            print(f"  {t['Date']} | ${amt:>12,.2f} | {t['Merchant'][:30]} | {t['Original Statement'][:50]}")
