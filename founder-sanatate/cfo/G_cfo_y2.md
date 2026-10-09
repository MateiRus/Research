# Unit economics: G · Controale pierdute (clinici independente de boli cronice) — anul 2

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
| 1 | 5 | $445 | $192 | $192 |
| 2 | 5 | $445 | $192 | $385 |
| 3 | 6 | $534 | $277 | $662 |
| 4 | 6 | $534 | $277 | $939 |
| 5 | 7 | $623 | $362 | $1,300 |
| 6 | 7 | $623 | $362 | $1,662 |
| 7 | 8 | $712 | $446 | $2,108 |
| 8 | 8 | $712 | $446 | $2,554 |
| 9 | 9 | $801 | $530 | $3,084 |
| 10 | 9 | $801 | $530 | $3,615 |
| 11 | 10 | $890 | $615 | $4,230 |
| 12 | 10 | $890 | $615 | $4,845 |

- **Year 1 operating profit: $4,845** on $8,010 of revenue.
- After the $0 startup spend: $4,845.
- Startup money earned back: month 1.
- Cash you need before it pays for itself: **$0**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 73% | 3 | $4,845 |
| Price -10% | 70% | 4 | $4,044 |
| Volume -20% | 68% | 3 | $3,324 |
| Unit costs +15% | 73% | 3 | $4,784 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
