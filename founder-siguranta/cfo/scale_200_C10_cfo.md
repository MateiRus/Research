# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la 200 de lucrători · structura C · vedere amortizată

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $10.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$2.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.45 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.30 |
| Facturare și încasare (0,5%) | -$0.05 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$4.95** (50%) |

## The margin that matters

Fixed costs: $975 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150, Ajutor part-time 0,25 normă (instalări, schimb dispozitive) $300).

- **Break-even: 197 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (200 a day): **1%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $3,980 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 200 | $2,000 | $15 | -$3,965 |
| 2 | 200 | $2,000 | $15 | -$3,950 |
| 3 | 200 | $2,000 | $15 | -$3,935 |
| 4 | 200 | $2,000 | $15 | -$3,920 |
| 5 | 200 | $2,000 | $15 | -$3,905 |
| 6 | 200 | $2,000 | $15 | -$3,890 |
| 7 | 200 | $2,000 | $15 | -$3,875 |
| 8 | 200 | $2,000 | $15 | -$3,860 |
| 9 | 200 | $2,000 | $15 | -$3,845 |
| 10 | 200 | $2,000 | $15 | -$3,830 |
| 11 | 200 | $2,000 | $15 | -$3,815 |
| 12 | 200 | $2,000 | $15 | -$3,800 |

- **Year 1 operating profit: $180** on $24,000 of revenue.
- After the $3,980 startup spend: -$3,800.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$3,980**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 1% | 197 | $180 |
| Price -10% | -10% | 247 | -$2,220 |
| Volume -20% | -11% | 197 | -$2,196 |
| Unit costs +15% | -7% | 233 | -$1,638 |

## Red flags

- The startup spend is not earned back within year 1.
