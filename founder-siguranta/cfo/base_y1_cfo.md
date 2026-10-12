# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători · anul 1 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $12.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 0% din venit) | -$0.00 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.36 |
| Facturare și încasare (0,5%) | -$0.06 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$7.33** (61%) |

## The margin that matters

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 72 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (70 a day): **-1%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $6,546 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$525 | -$7,071 |
| 2 | 0 | $0 | -$525 | -$7,596 |
| 3 | 0 | $0 | -$525 | -$8,121 |
| 4 | 0 | $0 | -$525 | -$8,646 |
| 5 | 0 | $0 | -$525 | -$9,171 |
| 6 | 20 | $240 | -$378 | -$9,549 |
| 7 | 20 | $240 | -$378 | -$9,928 |
| 8 | 20 | $240 | -$378 | -$10,306 |
| 9 | 40 | $480 | -$232 | -$10,538 |
| 10 | 40 | $480 | -$232 | -$10,770 |
| 11 | 40 | $480 | -$232 | -$11,002 |
| 12 | 70 | $840 | -$12 | -$11,013 |

- **Year 1 operating profit: -$4,468** on $3,000 of revenue.
- After the $6,546 startup spend: -$11,014.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$11,013**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -1% | 72 | -$4,468 |
| Price -10% | -13% | 86 | -$4,768 |
| Volume -20% | -17% | 72 | -$4,834 |
| Unit costs +15% | -7% | 80 | -$4,643 |

## Red flags

- Year 1 loses money on operations (-$4,468).
- The startup spend is not earned back within year 1.
