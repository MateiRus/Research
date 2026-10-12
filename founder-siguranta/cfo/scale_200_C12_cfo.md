# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 200 de lucrători · structura C · vedere amortizată

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $12.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.54 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.36 |
| Facturare și încasare (0,5%) | -$0.06 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$6.79** (57%) |

## The margin that matters

Fixed costs: $975 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150, Ajutor part-time 0,25 normă (instalări, schimb dispozitive) $300).

- **Break-even: 144 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (200 a day): **16%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 200 | $2,400 | $383 | -$3,597 |
| 2 | 200 | $2,400 | $383 | -$3,214 |
| 3 | 200 | $2,400 | $383 | -$2,831 |
| 4 | 200 | $2,400 | $383 | -$2,448 |
| 5 | 200 | $2,400 | $383 | -$2,065 |
| 6 | 200 | $2,400 | $383 | -$1,682 |
| 7 | 200 | $2,400 | $383 | -$1,299 |
| 8 | 200 | $2,400 | $383 | -$916 |
| 9 | 200 | $2,400 | $383 | -$533 |
| 10 | 200 | $2,400 | $383 | -$150 |
| 11 | 200 | $2,400 | $383 | $233 |
| 12 | 200 | $2,400 | $383 | $616 |

- **Year 1 operating profit: $4,596** on $28,800 of revenue.
- After the $3,980 startup spend: $616.
- Startup money earned back: month 11.
- Cash you need before it pays for itself: **$3,980**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 16% | 144 | $4,596 |
| Price -10% | 7% | 175 | $1,716 |
| Volume -20% | 6% | 144 | $1,337 |
| Unit costs +15% | 9% | 163 | $2,720 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
