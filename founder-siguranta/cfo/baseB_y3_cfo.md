# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Varianta B: dispozitiv inclus, 14 EUR/lună (pitch-ul v2); aceleași ore și aceeași rampă · anul 3 · vedere numerar

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
- **Profit margin at your plan** (200 a day): **34%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $1,947 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 180 | $2,520 | $790 | -$1,157 |
| 2 | 180 | $2,520 | $790 | -$367 |
| 3 | 190 | $2,660 | $872 | $505 |
| 4 | 190 | $2,660 | $872 | $1,377 |
| 5 | 190 | $2,660 | $872 | $2,248 |
| 6 | 200 | $2,800 | $953 | $3,201 |
| 7 | 200 | $2,800 | $953 | $4,154 |
| 8 | 200 | $2,800 | $953 | $5,107 |
| 9 | 200 | $2,800 | $953 | $6,060 |
| 10 | 200 | $2,800 | $953 | $7,013 |
| 11 | 200 | $2,800 | $953 | $7,966 |
| 12 | 200 | $2,800 | $953 | $8,919 |

- **Year 1 operating profit: $10,866** on $32,620 of revenue.
- After the $1,947 startup spend: $8,919.
- Startup money earned back: month 3.
- Cash you need before it pays for itself: **$1,947**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 34% | 83 | $10,866 |
| Price -10% | 27% | 101 | $7,604 |
| Volume -20% | 28% | 83 | $7,073 |
| Unit costs +15% | 28% | 93 | $8,818 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
