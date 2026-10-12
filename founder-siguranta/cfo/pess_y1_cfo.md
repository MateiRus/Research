# Unit economics: Lucru izolat conform, la cheie (ILLUSTRUS) · Pesimist: 10 EUR/lună, dispecerat 4 EUR, client nou la ≥6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20 · anul 1 · vedere numerar

Every number below comes from the input file. Nothing is looked up or guessed.

## One lucrător-lună

| line | per lucrător-lună |
| --- | ---: |
| Price | $10.00 |
| Logistică garanție și schimb (dispozitivul e al clientului) | -$0.25 |
| SIM IoT multi-rețea | -$1.50 |
| Dispecerat externalizat (firmă de pază), pe lucrător | -$4.00 |
| Comision serviciu extern SSM (15% x 0% din venit) | -$0.00 |
| Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit) | -$0.30 |
| Facturare și încasare (0,5%) | -$0.05 |
| **Contribution** (what each lucrător-lună leaves to pay the fixed costs) | **$3.90** (39%) |

## The margin that matters

Fixed costs: $525 a month (Găzduire UE: VM + bază de date + backup + monitorizare $60, Gateway SMS/voce pentru escaladare și test zilnic $20, Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală) $150, Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător $150, Contabilitate suplimentară $30, Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive) $100, SIM-uri de test și de rezervă $15).

- **Break-even: 135 lucrător-lunăs a day.** Below that you lose money every month.
- **Profit margin at your plan** (15 a day): **-311%** of every sale, after every cost.

## Year 1, month by month

| month | lucrător-lunăs a day | revenue | profit | cumulative (after $6,546 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$525 | -$7,071 |
| 2 | 0 | $0 | -$525 | -$7,596 |
| 3 | 0 | $0 | -$525 | -$8,121 |
| 4 | 0 | $0 | -$525 | -$8,646 |
| 5 | 0 | $0 | -$525 | -$9,171 |
| 6 | 0 | $0 | -$525 | -$9,696 |
| 7 | 0 | $0 | -$525 | -$10,221 |
| 8 | 15 | $150 | -$466 | -$10,688 |
| 9 | 15 | $150 | -$466 | -$11,154 |
| 10 | 15 | $150 | -$466 | -$11,620 |
| 11 | 15 | $150 | -$466 | -$12,087 |
| 12 | 15 | $150 | -$466 | -$12,554 |

- **Year 1 operating profit: -$6,008** on $750 of revenue.
- After the $6,546 startup spend: -$12,554.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$12,554**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -311% | 135 | -$6,008 |
| Price -10% | -357% | 182 | -$6,082 |
| Volume -20% | -399% | 135 | -$6,066 |
| Unit costs +15% | -320% | 176 | -$6,076 |

## Red flags

- Year 1 loses money on operations (-$6,008).
- The startup spend is not earned back within year 1.
