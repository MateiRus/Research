# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Pesimist: 10 EUR/lună, dispecerat 4 EUR, client nou la ≥6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20 · anul 2 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $10.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$4.00 |
| Comision serviciu extern SSM (15% x 30% din venit) | -$0.45 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.30 |
| Facturare și încasare (0,5%) | -$0.05 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$3.45** (34%) |

## The margin that matters

Fixed costs: $675 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15, Inginer de rezervă la apel pentru platformă (retainer) $150).

- **Break-even: 196 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (35 a day): **-158%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 15 | $150 | -$623 | -$623 |
| 2 | 35 | $350 | -$554 | -$1,178 |
| 3 | 35 | $350 | -$554 | -$1,732 |
| 4 | 35 | $350 | -$554 | -$2,286 |
| 5 | 35 | $350 | -$554 | -$2,840 |
| 6 | 35 | $350 | -$554 | -$3,394 |
| 7 | 35 | $350 | -$554 | -$3,949 |
| 8 | 35 | $350 | -$554 | -$4,503 |
| 9 | 35 | $350 | -$554 | -$5,057 |
| 10 | 35 | $350 | -$554 | -$5,612 |
| 11 | 35 | $350 | -$554 | -$6,166 |
| 12 | 35 | $350 | -$554 | -$6,720 |

- **Year 1 operating profit: -$6,720** on $4,000 of revenue.
- After the $0 startup spend: -$6,720.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$6,720**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -158% | 196 | -$6,720 |
| Price -10% | -187% | 276 | -$7,120 |
| Volume -20% | -207% | 196 | -$6,996 |
| Unit costs +15% | -168% | 274 | -$7,113 |

## Red flags

- Year 1 loses money on operations (-$6,720).
- The startup spend is not earned back within year 1.
