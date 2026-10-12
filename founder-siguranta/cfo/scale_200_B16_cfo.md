# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 200 de lucrători · structura B la 16 EUR · vedere amortizată

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $16.00 |
| Dispozitiv 88.50 EUR amortizat pe 36 de luni | -$2.46 |
| Pierderi și defecte (10%/an din valoarea dispozitivului) | -$0.74 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.72 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.48 |
| Facturare și încasare (0,5%) | -$0.08 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$7.52** (47%) |

## The margin that matters

Fixed costs: $975 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150, Ajutor part-time 0,25 normă (instalări, schimb dispozitive) $300).

- **Break-even: 130 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (200 a day): **17%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 200 | $3,200 | $529 | -$3,451 |
| 2 | 200 | $3,200 | $529 | -$2,922 |
| 3 | 200 | $3,200 | $529 | -$2,393 |
| 4 | 200 | $3,200 | $529 | -$1,864 |
| 5 | 200 | $3,200 | $529 | -$1,335 |
| 6 | 200 | $3,200 | $529 | -$806 |
| 7 | 200 | $3,200 | $529 | -$277 |
| 8 | 200 | $3,200 | $529 | $252 |
| 9 | 200 | $3,200 | $529 | $781 |
| 10 | 200 | $3,200 | $529 | $1,310 |
| 11 | 200 | $3,200 | $529 | $1,839 |
| 12 | 200 | $3,200 | $529 | $2,368 |

- **Year 1 operating profit: $6,348** on $38,400 of revenue.
- After the $3,980 startup spend: $2,368.
- Startup money earned back: month 8.
- Cash you need before it pays for itself: **$3,980**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 17% | 130 | $6,348 |
| Price -10% | 7% | 165 | $2,508 |
| Volume -20% | 9% | 130 | $2,738 |
| Unit costs +15% | 9% | 157 | $3,295 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
