# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · 20 h/săpt din luna 13: clientul cumpără dispozitivul + 12 EUR/lună, client nou la ≥2 luni · anul 2 · vedere numerar

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

Fixed costs: $775 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150, Deplasări suplimentare (ritm dublu de vânzare) $100).

- **Break-even: 115 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (270 a day): **33%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | $840 | -$300 | -$300 |
| 2 | 90 | $1,080 | -$164 | -$464 |
| 3 | 100 | $1,200 | -$96 | -$560 |
| 4 | 120 | $1,440 | $40 | -$520 |
| 5 | 120 | $1,440 | $40 | -$480 |
| 6 | 160 | $1,920 | $311 | -$169 |
| 7 | 160 | $1,920 | $311 | $143 |
| 8 | 190 | $2,280 | $515 | $658 |
| 9 | 200 | $2,400 | $583 | $1,241 |
| 10 | 230 | $2,760 | $787 | $2,028 |
| 11 | 230 | $2,760 | $787 | $2,814 |
| 12 | 270 | $3,240 | $1,058 | $3,873 |

- **Year 1 operating profit: $3,873** on $23,280 of revenue.
- After the $0 startup spend: $3,873.
- Startup money earned back: month 7.
- Cash you need before it pays for itself: **$560**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 33% | 115 | $3,873 |
| Price -10% | 25% | 139 | $1,545 |
| Volume -20% | 27% | 115 | $1,238 |
| Unit costs +15% | 26% | 129 | $2,356 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
