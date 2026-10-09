# Unit economics: G · Controale pierdute (clinici independente de boli cronice) — anul 1

Every number below comes from the input file. Nothing is looked up or guessed.

## One client-lună

| line | per client-lună |
| --- | ---: |
| Price | $89.00 |
| API LLM (maparea exporturilor) | -$2.00 |
| Găzduire și stocare incrementală | -$1.50 |
| E-mailuri tranzacționale | -$0.50 |
| Comisioane de plată și facturare | -$0.50 |
| **Contribution** (what each client-lună leaves to pay the fixed costs) | **$84.50** (95%) |

## The margin that matters

Fixed costs: $230 a month (Găzduire UE (VM + backup + monitorizare) $45, Domeniu, e-mail tranzacțional, unelte $25, Asigurare RC profesională + cyber (600 €/an) $50, Contabilitate suplimentară $30, Deplasări de vânzare în Nord-Vest $80).

- **Break-even: 3 client-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (12 a day): **73%** of every sale, after every cost.
- Capacity: 13 a day.

## Year 1, month by month

| month | client-lunăs a day | revenue | profit | cumulative (after $3,900 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$230 | -$4,130 |
| 2 | 0 | $0 | -$230 | -$4,360 |
| 3 | 0 | $0 | -$230 | -$4,590 |
| 4 | 0 | $0 | -$230 | -$4,820 |
| 5 | 1 | $89 | -$146 | -$4,966 |
| 6 | 1 | $89 | -$146 | -$5,111 |
| 7 | 2 | $178 | -$61 | -$5,172 |
| 8 | 2 | $178 | -$61 | -$5,233 |
| 9 | 3 | $267 | $24 | -$5,210 |
| 10 | 3 | $267 | $24 | -$5,186 |
| 11 | 4 | $356 | $108 | -$5,078 |
| 12 | 4 | $356 | $108 | -$4,970 |

- **Year 1 operating profit: -$1,070** on $1,780 of revenue.
- After the $3,900 startup spend: -$4,970.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$5,233**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 73% | 3 | -$1,070 |
| Price -10% | 70% | 4 | -$1,248 |
| Volume -20% | 68% | 3 | -$1,408 |
| Unit costs +15% | 73% | 3 | -$1,084 |

## Red flags

- Year 1 loses money on operations (-$1,070).
- The startup spend is not earned back within year 1.
