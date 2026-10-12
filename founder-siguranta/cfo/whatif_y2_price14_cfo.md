# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători · anul 2 · vedere numerar · what-if preț 14 EUR

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $14.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.63 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.42 |
| Facturare și încasare (0,5%) | -$0.07 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$8.63** (62%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 79 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (180 a day): **35%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | $980 | -$71 | -$71 |
| 2 | 70 | $980 | -$71 | -$142 |
| 3 | 100 | $1,400 | $188 | $46 |
| 4 | 100 | $1,400 | $188 | $234 |
| 5 | 100 | $1,400 | $188 | $422 |
| 6 | 140 | $1,960 | $533 | $955 |
| 7 | 140 | $1,960 | $533 | $1,489 |
| 8 | 140 | $1,960 | $533 | $2,022 |
| 9 | 160 | $2,240 | $706 | $2,728 |
| 10 | 160 | $2,240 | $706 | $3,433 |
| 11 | 160 | $2,240 | $706 | $4,139 |
| 12 | 180 | $2,520 | $878 | $5,018 |

- **Year 1 operating profit: $5,018** on $21,280 of revenue.
- After the $0 startup spend: $5,018.
- Startup money earned back: month 3.
- Cash you need before it pays for itself: **$142**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 35% | 79 | $5,018 |
| Price -10% | 28% | 94 | $2,890 |
| Volume -20% | 28% | 79 | $2,394 |
| Unit costs +15% | 29% | 87 | $3,793 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
