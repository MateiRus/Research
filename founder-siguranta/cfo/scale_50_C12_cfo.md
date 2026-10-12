# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 50 de lucrători · structura C · vedere amortizată

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

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 78 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (50 a day): **-31%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 50 | $600 | -$186 | -$4,166 |
| 2 | 50 | $600 | -$186 | -$4,351 |
| 3 | 50 | $600 | -$186 | -$4,536 |
| 4 | 50 | $600 | -$186 | -$4,722 |
| 5 | 50 | $600 | -$186 | -$4,908 |
| 6 | 50 | $600 | -$186 | -$5,093 |
| 7 | 50 | $600 | -$186 | -$5,278 |
| 8 | 50 | $600 | -$186 | -$5,464 |
| 9 | 50 | $600 | -$186 | -$5,650 |
| 10 | 50 | $600 | -$186 | -$5,835 |
| 11 | 50 | $600 | -$186 | -$6,020 |
| 12 | 50 | $600 | -$186 | -$6,206 |

- **Year 1 operating profit: -$2,226** on $7,200 of revenue.
- After the $3,980 startup spend: -$6,206.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$6,206**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -31% | 78 | -$2,226 |
| Price -10% | -45% | 94 | -$2,946 |
| Volume -20% | -53% | 78 | -$3,041 |
| Unit costs +15% | -37% | 88 | -$2,695 |

## Red flags

- Year 1 loses money on operations (-$2,226).
- The startup spend is not earned back within year 1.
