# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Varianta B: dispozitiv inclus, 14 EUR/lună (pitch-ul v2); aceleași ore și aceeași rampă · anul 2 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $14.00 |
| Pierderi și defecte (10%/an din valoarea dispozitivului) | -$0.74 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.63 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.42 |
| Facturare și încasare (0,5%) | -$0.07 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$8.14** (58%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 83 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (180 a day): **31%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $10,708 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | $980 | -$105 | -$10,814 |
| 2 | 70 | $980 | -$105 | -$10,919 |
| 3 | 100 | $1,400 | $139 | -$10,780 |
| 4 | 100 | $1,400 | $139 | -$10,641 |
| 5 | 100 | $1,400 | $139 | -$10,502 |
| 6 | 140 | $1,960 | $465 | -$10,037 |
| 7 | 140 | $1,960 | $465 | -$9,573 |
| 8 | 140 | $1,960 | $465 | -$9,108 |
| 9 | 160 | $2,240 | $627 | -$8,481 |
| 10 | 160 | $2,240 | $627 | -$7,853 |
| 11 | 160 | $2,240 | $627 | -$7,226 |
| 12 | 180 | $2,520 | $790 | -$6,436 |

- **Year 1 operating profit: $4,273** on $21,280 of revenue.
- After the $10,708 startup spend: -$6,436.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$10,919**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 31% | 83 | $4,273 |
| Price -10% | 24% | 101 | $2,145 |
| Volume -20% | 25% | 83 | $1,798 |
| Unit costs +15% | 25% | 93 | $2,937 |

## Red flags

- The startup spend is not earned back within year 1.
