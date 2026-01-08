import csv

with open('monarch-transactions.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    transactions = list(reader)

print("="*80)
print("LARGE TRANSACTIONS (>$5,000) - 2023 & 2024")
print("="*80)

for year in [2023, 2024]:
    print(f"\n{'='*40}")
    print(f"{year}")
    print(f"{'='*40}")
    
    txns = [t for t in transactions if t['Date'].startswith(str(year))]
    large = [t for t in txns if abs(float(t['Amount'] or 0)) >= 5000]
    large.sort(key=lambda x: float(x['Amount'] or 0), reverse=True)
    
    print("\n--- INCOMING (>$5K) ---")
    for t in large:
        amt = float(t['Amount'] or 0)
        if amt > 0:
            print(f"{t['Date']} | ${amt:>12,.2f} | {t['Account'][:30]} | {t['Merchant'][:25]} | {t['Original Statement'][:50]}")
    
    print("\n--- OUTGOING (>$5K) ---")
    for t in large:
        amt = float(t['Amount'] or 0)
        if amt < 0:
            print(f"{t['Date']} | ${amt:>12,.2f} | {t['Account'][:30]} | {t['Merchant'][:25]} | {t['Original Statement'][:50]}")

print(f"\n{'='*80}")
print("WHO IS PAYING YOU? - Income sources analysis")
print("="*80)

# Find all unique payers (Zelle from, Wire from, etc.)
payers = {}
for t in transactions:
    if not t['Date'].startswith('2023') and not t['Date'].startswith('2024'):
        continue
    amt = float(t['Amount'] or 0)
    if amt <= 0:
        continue
    
    statement = t['Original Statement'] or ''
    merchant = t['Merchant'] or ''
    
    # Try to extract payer name
    if 'from' in statement.lower():
        parts = statement.lower().split('from')
        if len(parts) > 1:
            payer = parts[1][:40].strip().upper()
            if payer not in payers:
                payers[payer] = 0
            payers[payer] += amt
    elif 'WIRE' in statement.upper():
        if payer not in payers:
            payers['WIRE TRANSFERS'] = 0
        payers['WIRE TRANSFERS'] += amt

print("\nTop sources of incoming money:")
for payer, total in sorted(payers.items(), key=lambda x: -x[1])[:15]:
    print(f"  ${total:>12,.2f} | {payer[:60]}")
