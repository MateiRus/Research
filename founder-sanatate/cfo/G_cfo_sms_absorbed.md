# Unit economics: G · SMS absorbit de fondator (nu refacturat) — anul 1

Every number below comes from the input file. Nothing is looked up or guessed.

## One client-lună

| line | per client-lună |
| --- | ---: |
| Price | $89.00 |
| API LLM (maparea exporturilor) | -$2.00 |
| Găzduire și stocare incrementală | -$1.50 |
| E-mailuri tranzacționale | -$0.50 |
| Comisioane de plată și facturare | -$0.50 |
| SMS absorbit: ~150 SMS × 0,06 € (clinică, controale depășite, doar cu consimțământ) | -$9.00 |
| **Contribution** (what each client-lună leaves to pay the fixed costs) | **$75.50** (85%) |

## The margin that matters

Fixed costs: $230 a month (Găzduire UE (VM + backup + monitorizare) $45, Domeniu, e-mail tranzacțional, unelte $25, Asigurare RC profesională + cyber (600 €/an) $50, Contabilitate suplimentară $30, Deplasări de vânzare în Nord-Vest $80).

- **Break-even: 4 client-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (12 a day): **63%** of every sale, after every cost.
- Capacity: 13 a day.

## Year 1, month by month

| month | client-lunăs a day | revenue | profit | cumulative (after $3,900 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$230 | -$4,130 |
| 2 | 0 | $0 | -$230 | -$4,360 |
| 3 | 0 | $0 | -$230 | -$4,590 |
| 4 | 0 | $0 | -$230 | -$4,820 |
| 5 | 1 | $89 | -$154 | -$4,974 |
| 6 | 1 | $89 | -$154 | -$5,129 |
| 7 | 2 | $178 | -$79 | -$5,208 |
| 8 | 2 | $178 | -$79 | -$5,287 |
| 9 | 3 | $267 | -$4 | -$5,290 |
| 10 | 3 | $267 | -$4 | -$5,294 |
| 11 | 4 | $356 | $72 | -$5,222 |
| 12 | 4 | $356 | $72 | -$5,150 |

- **Year 1 operating profit: -$1,250** on $1,780 of revenue.
- After the $3,900 startup spend: -$5,150.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$5,294**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 63% | 4 | -$1,250 |
| Price -10% | 59% | 4 | -$1,428 |
| Volume -20% | 58% | 4 | -$1,552 |
| Unit costs +15% | 61% | 4 | -$1,290 |

## Red flags

- Year 1 loses money on operations (-$1,250).
- The startup spend is not earned back within year 1.
