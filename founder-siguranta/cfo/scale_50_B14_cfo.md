# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 50 de lucrători · structura B · vedere amortizată

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $14.00 |
| Dispozitiv 88.50 EUR amortizat pe 36 de luni | -$2.46 |
| Pierderi și defecte (10%/an din valoarea dispozitivului) | -$0.74 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.63 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.42 |
| Facturare și încasare (0,5%) | -$0.07 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$5.68** (41%) |

## The margin that matters

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 93 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (50 a day): **-34%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 50 | $700 | -$241 | -$4,221 |
| 2 | 50 | $700 | -$241 | -$4,462 |
| 3 | 50 | $700 | -$241 | -$4,703 |
| 4 | 50 | $700 | -$241 | -$4,944 |
| 5 | 50 | $700 | -$241 | -$5,185 |
| 6 | 50 | $700 | -$241 | -$5,426 |
| 7 | 50 | $700 | -$241 | -$5,667 |
| 8 | 50 | $700 | -$241 | -$5,908 |
| 9 | 50 | $700 | -$241 | -$6,149 |
| 10 | 50 | $700 | -$241 | -$6,390 |
| 11 | 50 | $700 | -$241 | -$6,631 |
| 12 | 50 | $700 | -$241 | -$6,872 |

- **Year 1 operating profit: -$2,892** on $8,400 of revenue.
- After the $3,980 startup spend: -$6,872.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$6,872**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -34% | 93 | -$2,892 |
| Price -10% | -49% | 123 | -$3,732 |
| Volume -20% | -53% | 93 | -$3,574 |
| Unit costs +15% | -43% | 119 | -$3,641 |

## Red flags

- Year 1 loses money on operations (-$2,892).
- The startup spend is not earned back within year 1.
