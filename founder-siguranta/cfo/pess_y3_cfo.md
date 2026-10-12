# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Pesimist: 10 EUR/lună, dispecerat 4 EUR, client nou la ≥6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20 · anul 3 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $10.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$4.00 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.45 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.30 |
| Facturare și încasare (0,5%) | -$0.05 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$3.45** (34%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 196 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (85 a day): **-45%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 35 | $350 | -$554 | -$554 |
| 2 | 60 | $600 | -$468 | -$1,022 |
| 3 | 60 | $600 | -$468 | -$1,490 |
| 4 | 60 | $600 | -$468 | -$1,958 |
| 5 | 60 | $600 | -$468 | -$2,426 |
| 6 | 60 | $600 | -$468 | -$2,894 |
| 7 | 60 | $600 | -$468 | -$3,362 |
| 8 | 85 | $850 | -$382 | -$3,744 |
| 9 | 85 | $850 | -$382 | -$4,126 |
| 10 | 85 | $850 | -$382 | -$4,508 |
| 11 | 85 | $850 | -$382 | -$4,889 |
| 12 | 85 | $850 | -$382 | -$5,271 |

- **Year 1 operating profit: -$5,271** on $8,200 of revenue.
- After the $0 startup spend: -$5,271.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$5,271**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -45% | 196 | -$5,271 |
| Price -10% | -61% | 276 | -$6,091 |
| Volume -20% | -65% | 196 | -$5,837 |
| Unit costs +15% | -55% | 274 | -$6,077 |

## Red flags

- Year 1 loses money on operations (-$5,271).
- The startup spend is not earned back within year 1.
