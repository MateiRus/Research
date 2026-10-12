# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători · anul 2 · vedere numerar · what-if dispecerat 4 EUR

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $12.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$4.00 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.54 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.36 |
| Facturare și încasare (0,5%) | -$0.06 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$5.29** (44%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 128 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (180 a day): **13%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | $840 | -$305 | -$305 |
| 2 | 70 | $840 | -$305 | -$609 |
| 3 | 100 | $1,200 | -$146 | -$755 |
| 4 | 100 | $1,200 | -$146 | -$901 |
| 5 | 100 | $1,200 | -$146 | -$1,047 |
| 6 | 140 | $1,680 | $66 | -$982 |
| 7 | 140 | $1,680 | $66 | -$916 |
| 8 | 140 | $1,680 | $66 | -$851 |
| 9 | 160 | $1,920 | $171 | -$679 |
| 10 | 160 | $1,920 | $171 | -$508 |
| 11 | 160 | $1,920 | $171 | -$336 |
| 12 | 180 | $2,160 | $277 | -$59 |

- **Year 1 operating profit: -$59** on $18,240 of revenue.
- After the $0 startup spend: -$59.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$1,047**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 13% | 128 | -$59 |
| Price -10% | 3% | 166 | -$1,883 |
| Volume -20% | 5% | 128 | -$1,667 |
| Unit costs +15% | 4% | 158 | -$1,589 |

## Red flags

- Year 1 loses money on operations (-$59).
- The startup spend is not earned back within year 1.
