# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 200 de lucrători · structura B · vedere amortizată

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

Fixed costs: $975 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150, Ajutor part-time 0,25 normă (instalări, schimb dispozitive) $300).

- **Break-even: 88 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (200 a day): **32%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 200 | $4,000 | $1,265 | -$2,715 |
| 2 | 200 | $4,000 | $1,265 | -$1,450 |
| 3 | 200 | $4,000 | $1,265 | -$185 |
| 4 | 200 | $4,000 | $1,265 | $1,080 |
| 5 | 200 | $4,000 | $1,265 | $2,345 |
| 6 | 200 | $4,000 | $1,265 | $3,610 |
| 7 | 200 | $4,000 | $1,265 | $4,875 |
| 8 | 200 | $4,000 | $1,265 | $6,140 |
| 9 | 200 | $4,000 | $1,265 | $7,405 |
| 10 | 200 | $4,000 | $1,265 | $8,670 |
| 11 | 200 | $4,000 | $1,265 | $9,935 |
| 12 | 200 | $4,000 | $1,265 | $11,200 |

- **Year 1 operating profit: $15,180** on $48,000 of revenue.
- After the $3,980 startup spend: $11,200.
- Startup money earned back: month 4.
- Cash you need before it pays for itself: **$3,980**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 32% | 88 | $15,180 |
| Price -10% | 24% | 106 | $10,380 |
| Volume -20% | 26% | 88 | $9,804 |
| Unit costs +15% | 25% | 99 | $12,012 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
