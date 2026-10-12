# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 50 de lucrători · structura B · vedere amortizată

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $20.00 |
| Dispozitiv 88.50 EUR amortizat pe 36 de luni | -$2.46 |
| Pierderi și defecte (10%/an din valoarea dispozitivului) | -$0.74 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.90 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.60 |
| Facturare și încasare (0,5%) | -$0.10 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$11.20** (56%) |

## The margin that matters

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 47 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (50 a day): **4%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 50 | $1,000 | $35 | -$3,945 |
| 2 | 50 | $1,000 | $35 | -$3,910 |
| 3 | 50 | $1,000 | $35 | -$3,875 |
| 4 | 50 | $1,000 | $35 | -$3,840 |
| 5 | 50 | $1,000 | $35 | -$3,805 |
| 6 | 50 | $1,000 | $35 | -$3,770 |
| 7 | 50 | $1,000 | $35 | -$3,735 |
| 8 | 50 | $1,000 | $35 | -$3,700 |
| 9 | 50 | $1,000 | $35 | -$3,665 |
| 10 | 50 | $1,000 | $35 | -$3,630 |
| 11 | 50 | $1,000 | $35 | -$3,595 |
| 12 | 50 | $1,000 | $35 | -$3,560 |

- **Year 1 operating profit: $420** on $12,000 of revenue.
- After the $3,980 startup spend: -$3,560.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$3,980**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 4% | 47 | $420 |
| Price -10% | -7% | 58 | -$780 |
| Volume -20% | -10% | 47 | -$924 |
| Unit costs +15% | -3% | 54 | -$372 |

## Red flags

- The startup spend is not earned back within year 1.
