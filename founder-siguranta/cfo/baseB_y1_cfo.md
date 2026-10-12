# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Varianta B: dispozitiv inclus, 14 EUR/lună (pitch-ul v2); aceleași ore și aceeași rampă · anul 1 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $14.00 |
| Pierderi și defecte (10%/an din valoarea dispozitivului) | -$0.74 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 0% din venit) | -$0.00 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.42 |
| Facturare și încasare (0,5%) | -$0.07 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$8.77** (63%) |

## The margin that matters

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 60 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (70 a day): **9%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $13,360 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$525 | -$13,886 |
| 2 | 0 | $0 | -$525 | -$14,410 |
| 3 | 0 | $0 | -$525 | -$14,936 |
| 4 | 0 | $0 | -$525 | -$15,460 |
| 5 | 0 | $0 | -$525 | -$15,986 |
| 6 | 20 | $280 | -$350 | -$16,335 |
| 7 | 20 | $280 | -$350 | -$16,685 |
| 8 | 20 | $280 | -$350 | -$17,034 |
| 9 | 40 | $560 | -$174 | -$17,208 |
| 10 | 40 | $560 | -$174 | -$17,383 |
| 11 | 40 | $560 | -$174 | -$17,557 |
| 12 | 70 | $980 | $89 | -$17,468 |

- **Year 1 operating profit: -$4,108** on $3,500 of revenue.
- After the $13,360 startup spend: -$17,468.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$17,557**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 9% | 60 | -$4,108 |
| Price -10% | -1% | 72 | -$4,458 |
| Volume -20% | -4% | 60 | -$4,546 |
| Unit costs +15% | 3% | 66 | -$4,304 |

## Red flags

- Year 1 loses money on operations (-$4,108).
- The startup spend is not earned back within year 1.
