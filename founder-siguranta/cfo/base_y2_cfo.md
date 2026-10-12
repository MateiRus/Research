# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători · anul 2 · vedere numerar

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

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 100 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (180 a day): **25%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | $840 | -$200 | -$200 |
| 2 | 70 | $840 | -$200 | -$399 |
| 3 | 100 | $1,200 | $4 | -$395 |
| 4 | 100 | $1,200 | $4 | -$391 |
| 5 | 100 | $1,200 | $4 | -$387 |
| 6 | 140 | $1,680 | $276 | -$112 |
| 7 | 140 | $1,680 | $276 | $164 |
| 8 | 140 | $1,680 | $276 | $439 |
| 9 | 160 | $1,920 | $411 | $851 |
| 10 | 160 | $1,920 | $411 | $1,262 |
| 11 | 160 | $1,920 | $411 | $1,674 |
| 12 | 180 | $2,160 | $547 | $2,221 |

- **Year 1 operating profit: $2,221** on $18,240 of revenue.
- After the $0 startup spend: $2,221.
- Startup money earned back: month 7.
- Cash you need before it pays for itself: **$399**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 25% | 100 | $2,221 |
| Price -10% | 17% | 121 | $397 |
| Volume -20% | 18% | 100 | $157 |
| Unit costs +15% | 19% | 113 | $1,033 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
