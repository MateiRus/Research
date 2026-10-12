# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 200 de lucrători · structura B · vedere amortizată

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

Fixed costs: $975 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150, Ajutor part-time 0,25 normă (instalări, schimb dispozitive) $300).

- **Break-even: 172 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (200 a day): **6%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 200 | $2,800 | $161 | -$3,819 |
| 2 | 200 | $2,800 | $161 | -$3,658 |
| 3 | 200 | $2,800 | $161 | -$3,497 |
| 4 | 200 | $2,800 | $161 | -$3,336 |
| 5 | 200 | $2,800 | $161 | -$3,175 |
| 6 | 200 | $2,800 | $161 | -$3,014 |
| 7 | 200 | $2,800 | $161 | -$2,853 |
| 8 | 200 | $2,800 | $161 | -$2,692 |
| 9 | 200 | $2,800 | $161 | -$2,531 |
| 10 | 200 | $2,800 | $161 | -$2,370 |
| 11 | 200 | $2,800 | $161 | -$2,209 |
| 12 | 200 | $2,800 | $161 | -$2,048 |

- **Year 1 operating profit: $1,932** on $33,600 of revenue.
- After the $3,980 startup spend: -$2,048.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$3,980**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 6% | 172 | $1,932 |
| Price -10% | -5% | 228 | -$1,428 |
| Volume -20% | -3% | 172 | -$794 |
| Unit costs +15% | -3% | 220 | -$1,063 |

## Red flags

- The startup spend is not earned back within year 1.
