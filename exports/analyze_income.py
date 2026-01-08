import csv
from collections import defaultdict

with open('monarch-transactions.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    transactions = list(reader)

def analyze_income(year):
    txns = [t for t in transactions if t['Date'].startswith(str(year))]
    
    print(f"\n{'='*70}")
    print(f"INCOME ANALYSIS - {year}")
    print(f"{'='*70}")
    
    # Categorize income
    real_income = []
    transfers = []
    cc_payments = []
    refunds = []
    other = []
    
    for t in txns:
        try:
            amt = float(t['Amount'])
        except:
            continue
        
        if amt <= 0:  # Not income
            continue
            
        cat = t['Category'] or ''
        merchant = t['Merchant'] or ''
        statement = t['Original Statement'] or ''
        
        # Classify
        if 'Transfer' in cat or 'TRANSFER' in statement.upper():
            transfers.append(t)
        elif 'Credit Card Payment' in cat or 'PAYMENT' in statement.upper():
            cc_payments.append(t)
        elif 'Interest' in cat:
            real_income.append(t)
        elif any(x in statement.upper() for x in ['WIRE', 'PAYROLL', 'DIRECT DEP', 'SALARY']):
            real_income.append(t)
        elif any(x in merchant.upper() for x in ['REFUND', 'RETURN', 'REBATE']):
            refunds.append(t)
        elif 'Zelle' in merchant and amt > 0:
            real_income.append(t)
        else:
            other.append(t)
    
    def sum_txns(txn_list):
        return sum(float(t['Amount']) for t in txn_list)
    
    def print_top(txn_list, label, n=10):
        total = sum_txns(txn_list)
        print(f"\n{label}: ${total:,.2f} ({len(txn_list)} transactions)")
        sorted_list = sorted(txn_list, key=lambda x: -float(x['Amount']))[:n]
        for t in sorted_list:
            print(f"  {t['Date']} | ${float(t['Amount']):>10,.2f} | {t['Merchant'][:30]} | {t['Original Statement'][:40]}")
    
    print_top(real_income, "LIKELY REAL INCOME (taxable)")
    print_top(transfers, "TRANSFERS (between your accounts - not income)")
    print_top(cc_payments, "CC PAYMENTS/REFUNDS (not income)")
    print_top(other, "OTHER/UNCLEAR")
    
    print(f"\n--- SUMMARY ---")
    print(f"Likely taxable income: ${sum_txns(real_income):,.2f}")
    print(f"Internal transfers:    ${sum_txns(transfers):,.2f}")
    print(f"CC payments/refunds:   ${sum_txns(cc_payments):,.2f}")
    print(f"Other unclear:         ${sum_txns(other):,.2f}")

analyze_income(2023)
analyze_income(2024)
