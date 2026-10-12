# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · 20 h/săpt din luna 13: clientul cumpără dispozitivul + 12 EUR/lună, client nou la ≥2 luni · anul 3 · vedere numerar

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
- **Profit margin at your plan** (470 a day): **43%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 270 | $3,240 | $1,058 | $1,058 |
| 2 | 310 | $3,720 | $1,330 | $2,388 |
| 3 | 310 | $3,720 | $1,330 | $3,718 |
| 4 | 350 | $4,200 | $1,602 | $5,320 |
| 5 | 350 | $4,200 | $1,602 | $6,921 |
| 6 | 390 | $4,680 | $1,873 | $8,794 |
| 7 | 390 | $4,680 | $1,873 | $10,667 |
| 8 | 410 | $4,920 | $2,009 | $12,676 |
| 9 | 430 | $5,160 | $2,145 | $14,821 |
| 10 | 450 | $5,400 | $2,280 | $17,101 |
| 11 | 450 | $5,400 | $2,280 | $19,382 |
| 12 | 470 | $5,640 | $2,416 | $21,798 |

- **Year 1 operating profit: $21,798** on $54,960 of revenue.
- After the $0 startup spend: $21,798.
- Startup money earned back: month 1.
- Cash you need before it pays for itself: **$0**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 43% | 115 | $21,798 |
| Price -10% | 36% | 139 | $16,302 |
| Volume -20% | 39% | 115 | $15,579 |
| Unit costs +15% | 36% | 129 | $18,219 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
