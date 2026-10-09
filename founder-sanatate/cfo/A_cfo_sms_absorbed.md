# Unit economics: A · SMS absorbit de fondator (nu refacturat) — anul 1

Every number below comes from the input file. Nothing is looked up or guessed.

## One client-lună

| line | per client-lună |
| --- | ---: |
| Price | $65.00 |
| API LLM (maparea importurilor) | -$2.00 |
| Găzduire și stocare incrementală | -$1.00 |
| E-mailuri tranzacționale | -$0.50 |
| Comisioane de plată și facturare | -$0.50 |
| SMS absorbit: ~200 SMS × 0,06 € (cabinet cu ~3.000 de angajați, ~40% consimțământ, 2 remindere) | -$12.00 |
| **Contribution** (what each client-lună leaves to pay the fixed costs) | **$49.00** (75%) |

## The margin that matters

Fixed costs: $230 a month (Găzduire UE (VM + backup + monitorizare) $45, Domeniu, e-mail tranzacțional, unelte $25, Asigurare RC profesională + cyber (600 €/an) $50, Contabilitate suplimentară $30, Deplasări de vânzare în Nord-Vest $80).

- **Break-even: 5 client-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (16 a day): **53%** of every sale, after every cost.
- Capacity: 25 a day.

## Year 1, month by month

| month | client-lunăs a day | revenue | profit | cumulative (after $2,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$230 | -$3,210 |
| 2 | 0 | $0 | -$230 | -$3,440 |
| 3 | 0 | $0 | -$230 | -$3,670 |
| 4 | 2 | $130 | -$132 | -$3,802 |
| 5 | 3 | $195 | -$83 | -$3,885 |
| 6 | 4 | $260 | -$34 | -$3,919 |
| 7 | 5 | $325 | $15 | -$3,904 |
| 8 | 6 | $390 | $64 | -$3,840 |
| 9 | 7 | $455 | $113 | -$3,727 |
| 10 | 8 | $520 | $162 | -$3,565 |
| 11 | 9 | $585 | $211 | -$3,354 |
| 12 | 10 | $650 | $260 | -$3,094 |

- **Year 1 operating profit: -$114** on $3,510 of revenue.
- After the $2,980 startup spend: -$3,094.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$3,919**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 53% | 5 | -$114 |
| Price -10% | 48% | 6 | -$465 |
| Volume -20% | 48% | 5 | -$643 |
| Unit costs +15% | 50% | 5 | -$244 |

## Red flags

- Year 1 loses money on operations (-$114).
- The startup spend is not earned back within year 1.
