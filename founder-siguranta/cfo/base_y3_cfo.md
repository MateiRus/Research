# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători · anul 3 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $12.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.54 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.36 |
| Facturare și încasare (0,5%) | -$0.06 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$6.79** (57%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 100 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (200 a day): **28%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 180 | $2,160 | $547 | $547 |
| 2 | 180 | $2,160 | $547 | $1,094 |
| 3 | 190 | $2,280 | $615 | $1,710 |
| 4 | 190 | $2,280 | $615 | $2,325 |
| 5 | 190 | $2,280 | $615 | $2,940 |
| 6 | 200 | $2,400 | $683 | $3,623 |
| 7 | 200 | $2,400 | $683 | $4,306 |
| 8 | 200 | $2,400 | $683 | $4,989 |
| 9 | 200 | $2,400 | $683 | $5,672 |
| 10 | 200 | $2,400 | $683 | $6,355 |
| 11 | 200 | $2,400 | $683 | $7,038 |
| 12 | 200 | $2,400 | $683 | $7,721 |

- **Year 1 operating profit: $7,721** on $27,960 of revenue.
- After the $0 startup spend: $7,721.
- Startup money earned back: month 1.
- Cash you need before it pays for itself: **$0**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 28% | 100 | $7,721 |
| Price -10% | 21% | 121 | $4,925 |
| Volume -20% | 21% | 100 | $4,557 |
| Unit costs +15% | 22% | 113 | $5,900 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
