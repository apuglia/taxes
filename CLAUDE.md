# Tax Filing Project - Alejandro Puglia

## Project Overview

This repository contains tax documentation, analysis, and tracking for filing back taxes (2023-2024) for personal returns and 4 Delaware LLCs.

## Quick Reference

### Federal Tax Status
- **2023:** ✅ FILED - Refund of **$20,436** issued 08-19-2024
- **2024:** ~$4,047 estimated refund (pending filing)

### Key Files
- `tracking/COMPLETE-SITUATION-MAP.md` - Full overview of tax situation, entities, unknowns
- `tracking/FINAL-tax-calculation.md` - Tax calculations based on IRS transcripts
- `tracking/tax-summary-2023-2024.md` - Summary of income and deductions
- `exports/monarch-transactions.csv` - Bank transaction data (5,880 transactions)

### Entities
| Entity | Type | Status | Filing Requirement |
|--------|------|--------|-------------------|
| Personal | Individual | Active | Form 1040 + NY IT-201 |
| Panamerican Group LLC | Partnership (0.99%) | Active | K-1 flows to personal return |
| CannuMate LLC | Single-member | Active | Schedule C on personal return |
| Vergincetrix LLC | Single-member | Dormant | Schedule C ($0) on personal return |
| Redi Servicios LLC | Single-member | Dormant | Schedule C ($0) on personal return |

## Outstanding Tasks

### Unknowns to Resolve
1. [ ] Get 2024 K-1 from Panamerican Group accountant
2. [ ] Check Delaware status for CannuMate, Vergincetrix, Redi Servicios
3. [x] ~~Get W-2 copies showing state withholding (boxes 15-17)~~ - Have W-2s in `IRS/Personal/2023/W2/` and `IRS/Personal/2024/`
4. [ ] Find CannuMate expense records (if any)

### Filing Tasks
1. [x] ~~File 2023 Federal (Form 1040 with K-1 loss)~~ - Filed, refund $20,436 received 08-19-2024
2. [ ] File 2023 NY State (IT-201)
3. [ ] File 2023 NJ Non-resident - **NJ withholding confirmed: $10,685.85**
4. [ ] File 2024 Federal (Form 1040)
5. [ ] File 2024 NY State (IT-201)
6. [ ] File 2024 NJ Non-resident - **NJ withholding confirmed: $1,297.20**
7. [ ] Pay Delaware franchise tax - all 4 LLCs × 2 years (~$2,400 + penalties)

## Folder Structure

```
taxes/
├── IRS/
│   └── Personal/
│       ├── 2021/      # W-2, returns, transcripts, bank statements
│       ├── 2022/      # W-2, returns, transcripts, bank statements
│       ├── 2023/      # W-2, IRS transcripts, bank statements
│       ├── 2024/      # W-2, bank statements
│       └── 2025/      # Bank statements
├── personal/
│   ├── 2023/          # Personal docs for 2023
│   └── 2024/          # Personal docs for 2024
├── panamerican-group-llc/
├── cannumate-llc/
├── vergincetrix-llc/
├── redi-servicios-llc/
├── delaware/          # Franchise tax info
├── exports/           # Bank transaction exports
├── tracking/          # Analysis and status tracking
└── tools/             # Helper scripts
```

## Key Income Sources (from IRS Documents)

### 2023 (from filed return transcript)
- W-2 (Ernst & Young): $187,311.88
- Schedule C Income (Panamerican Group): $18,940
- K-1 Loss (Panamerican Partnership): -$90,483 **(NONPASSIVE)**
- **Total Income:** $115,768
- **Taxable Income:** $101,918
- **Tax Owed:** $17,860
- **Withholding:** $38,296.09
- **Refund Received:** $20,436

### 2023 State Withholding (from W-2)
| State | Wages | Tax Withheld |
|-------|-------|--------------|
| NY | $187,311.88 | $1,006.03 |
| NJ | $189,240.56 | $10,685.85 |
| NYC (Local) | $187,311.88 | $7,434.24 |

### 2024 (from W-2)
- W-2 (Ernst & Young): $24,090.21
- Federal Tax Withheld: $4,772.62

### 2024 State Withholding (from W-2)
| State | Wages | Tax Withheld |
|-------|-------|--------------|
| NY | $24,090.21 | $190.44 |
| NJ | $24,331.86 | $1,297.20 |
| NYC (Local) | $24,090.21 | $943.88 |

## Important Notes

- **K-1 Loss:** The $90,483 partnership loss was classified as **NONPASSIVE** on the 2023 return, fully offsetting W-2 income.
- **Loss Carryforward:** $71,543 qualified business loss carryforward available for future years (from 2023 return).
- **Gift Income:** ~$210K received from family in 2024 is NOT taxable income (gifts to recipient are tax-free)
- **Delaware Franchise Tax:** $300/year per LLC regardless of activity. Likely have penalties for late payment.
- **Multi-State:** NJ non-resident returns REQUIRED for both 2023 and 2024 - NJ taxes were withheld from W-2.

## Document Locations

### IRS Folder (`IRS/Personal/`)
- `2023/W2/` - 2023 W-2 from EY
- `2023/2023_IRS_Account Transcript.pdf` - Shows 2023 return filed, refund issued
- `2023/2023_IRS_Form 1040 Tax Return Transcript.pdf` - Full return details
- `2024/2024_W2_EY_Alejandro Puglia.pdf` - 2024 W-2 from EY
- `2021/`, `2022/` - Prior year W-2s, returns, and bank statements
- Bank of America Statements (2021-2025)
- Chase Statements (2021-2022)
