# Unit economics: G · Controale pierdute (clinici independente de boli cronice) — anul 3

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

| month | client-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 11 | $979 | $700 | $700 |
| 2 | 11 | $979 | $700 | $1,399 |
| 3 | 12 | $1,068 | $784 | $2,183 |
| 4 | 12 | $1,068 | $784 | $2,967 |
| 5 | 13 | $1,157 | $868 | $3,836 |
| 6 | 13 | $1,157 | $868 | $4,704 |
| 7 | 13 | $1,157 | $868 | $5,572 |
| 8 | 13 | $1,157 | $868 | $6,441 |
| 9 | 13 | $1,157 | $868 | $7,310 |
| 10 | 13 | $1,157 | $868 | $8,178 |
| 11 | 13 | $1,157 | $868 | $9,046 |
| 12 | 13 | $1,157 | $868 | $9,915 |

- **Year 1 operating profit: $9,915** on $13,350 of revenue.
- After the $0 startup spend: $9,915.
- Startup money earned back: month 1.
- Cash you need before it pays for itself: **$0**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 73% | 3 | $9,915 |
| Price -10% | 70% | 4 | $8,580 |
| Volume -20% | 68% | 3 | $7,380 |
| Unit costs +15% | 73% | 3 | $9,814 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
