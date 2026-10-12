# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători · anul 2 · vedere numerar · what-if dispecerat 1,50 EUR

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $12.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$1.50 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.54 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.36 |
| Facturare și încasare (0,5%) | -$0.06 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$7.79** (65%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 87 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (180 a day): **34%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | $840 | -$130 | -$130 |
| 2 | 70 | $840 | -$130 | -$259 |
| 3 | 100 | $1,200 | $104 | -$155 |
| 4 | 100 | $1,200 | $104 | -$51 |
| 5 | 100 | $1,200 | $104 | $53 |
| 6 | 140 | $1,680 | $416 | $468 |
| 7 | 140 | $1,680 | $416 | $884 |
| 8 | 140 | $1,680 | $416 | $1,299 |
| 9 | 160 | $1,920 | $571 | $1,871 |
| 10 | 160 | $1,920 | $571 | $2,442 |
| 11 | 160 | $1,920 | $571 | $3,014 |
| 12 | 180 | $2,160 | $727 | $3,741 |

- **Year 1 operating profit: $3,741** on $18,240 of revenue.
- After the $0 startup spend: $3,741.
- Startup money earned back: month 5.
- Cash you need before it pays for itself: **$259**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 34% | 87 | $3,741 |
| Price -10% | 26% | 103 | $1,917 |
| Volume -20% | 26% | 87 | $1,373 |
| Unit costs +15% | 28% | 95 | $2,781 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
