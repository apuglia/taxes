# Tax Project Plan

**Goal:** Get to the end feeling good about taxes - everything filed, documented, and backed up.

**Last Updated:** 2026-01-07

---

## Status Overview

| Item | Status | Est. Refund/Owed |
|------|--------|------------------|
| 2023 Federal | ✅ DONE | $20,436 received |
| 2023 NY State | ⏳ Pending | ~refund likely |
| 2023 NJ Non-resident | ⏳ Pending | ~$10,685 refund |
| 2024 Federal | ⏳ Pending | ~$4,047 refund |
| 2024 NY State | ⏳ Pending | ~small refund |
| 2024 NJ Non-resident | ⏳ Pending | ~$1,297 refund |
| Delaware Franchise Tax | ⏳ Pending | ~$2,400 + penalties |

**Estimated total refunds owed to you: ~$16,000+**

---

## Phase 1: Resolve Blockers

- [ ] **Get 2024 K-1** from Panamerican Group accountant
- [ ] **Check Delaware LLC status** for all 4 entities (CannuMate, Vergincetrix, Redi Servicios, Panamerican Group)
- [ ] **Check CannuMate expenses** - any 2023-2024 business expenses?

**Why:** Without the 2024 K-1, cannot file 2024 Federal. Delaware status determines penalties.

---

## Phase 2: File 2023 State Returns

- [ ] **NY IT-201 (2023)** - All data available from W-2
- [ ] **NJ Non-Resident (2023)** - $10,685.85 withheld, most/all refundable

**Data needed (all available):**
- W-2: `IRS/Personal/2023/W2/`
- Federal return info: `IRS/Personal/2023/2023_IRS_Form 1040 Tax Return Transcript.pdf`

---

## Phase 3: File 2024 Federal

- [ ] **Form 1040 (2024)** - Requires 2024 K-1

**Data needed:**
- W-2: `IRS/Personal/2024/2024_W2_EY_Alejandro Puglia.pdf`
- 2024 K-1: ⚠️ NEED FROM ACCOUNTANT
- Loss carryforward: $71,543 available from 2023

---

## Phase 4: File 2024 State Returns

- [ ] **NY IT-201 (2024)**
- [ ] **NJ Non-Resident (2024)** - $1,297.20 withheld

---

## Phase 5: Delaware Cleanup

- [ ] **Pay franchise tax** for all 4 LLCs × 2 years (2023 + 2024)
- [ ] **Pay late penalties** (if any)
- [ ] **Decide:** Keep dormant LLCs active or dissolve?

**LLCs:**
| Entity | Activity | Action |
|--------|----------|--------|
| Panamerican Group LLC | Active (0.99% partner) | Keep |
| CannuMate LLC | Active | Keep |
| Vergincetrix LLC | Dormant | Keep or Dissolve? |
| Redi Servicios LLC | Dormant | Keep or Dissolve? |

---

## Phase 6: Organize Final Archive

- [ ] Create `FILED/` folder with all filed returns
- [ ] Organize source documents
- [ ] Create permanent summary document

**Target structure:**
```
taxes/
├── FILED/
│   ├── 2023-federal-1040.pdf     ✅
│   ├── 2023-ny-it201.pdf
│   ├── 2023-nj-nonres.pdf
│   ├── 2024-federal-1040.pdf
│   ├── 2024-ny-it201.pdf
│   └── 2024-nj-nonres.pdf
├── SOURCE-DOCS/
│   ├── W2s/
│   ├── K1s/
│   ├── Bank-Statements/
│   └── IRS-Transcripts/
└── FINAL-SUMMARY.md
```

---

## Key Numbers Reference

### 2023 Income & Withholding
- W-2 Wages: $187,311.88
- K-1 Loss: -$90,483 (nonpassive)
- Federal Withheld: $38,296.09
- NY Withheld: $1,006.03
- NJ Withheld: $10,685.85
- NYC Withheld: $7,434.24

### 2024 Income & Withholding
- W-2 Wages: $24,090.21
- Federal Withheld: $4,772.62
- NY Withheld: $190.44
- NJ Withheld: $1,297.20
- NYC Withheld: $943.88

### Carryforward
- Qualified Business Loss: $71,543 (from 2023, available for future years)

---

## Filing Options

**DIY:**
- FreeTaxUSA (~$15-30/state)
- TurboTax
- H&R Block

**Professional:**
- CPA/Tax preparer ($200-500 total for state returns)

---

## Notes

- Gift income (~$210K in 2024) is NOT taxable to recipient
- Delaware franchise tax is $300/year per LLC regardless of activity
- NJ non-resident returns are REQUIRED - taxes were withheld from W-2
