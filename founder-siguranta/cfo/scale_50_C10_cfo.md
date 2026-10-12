# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 50 de lucrători · structura C · vedere amortizată

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $10.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.45 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.30 |
| Facturare și încasare (0,5%) | -$0.05 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$4.95** (50%) |

## The margin that matters

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 107 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (50 a day): **-55%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 50 | $500 | -$278 | -$4,258 |
| 2 | 50 | $500 | -$278 | -$4,535 |
| 3 | 50 | $500 | -$278 | -$4,812 |
| 4 | 50 | $500 | -$278 | -$5,090 |
| 5 | 50 | $500 | -$278 | -$5,368 |
| 6 | 50 | $500 | -$278 | -$5,645 |
| 7 | 50 | $500 | -$278 | -$5,922 |
| 8 | 50 | $500 | -$278 | -$6,200 |
| 9 | 50 | $500 | -$278 | -$6,478 |
| 10 | 50 | $500 | -$278 | -$6,755 |
| 11 | 50 | $500 | -$278 | -$7,032 |
| 12 | 50 | $500 | -$278 | -$7,310 |

- **Year 1 operating profit: -$3,330** on $6,000 of revenue.
- After the $3,980 startup spend: -$7,310.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$7,310**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -55% | 107 | -$3,330 |
| Price -10% | -73% | 133 | -$3,930 |
| Volume -20% | -82% | 107 | -$3,924 |
| Unit costs +15% | -63% | 126 | -$3,784 |

## Red flags

- Year 1 loses money on operations (-$3,330).
- The startup spend is not earned back within year 1.
