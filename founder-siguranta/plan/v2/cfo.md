# CFO: economia unitară pentru „Lucru izolat conform, la cheie”

Unealta: `founder-cfo/unit_economics.py`, rulată pe fiecare `*.json` din acest folder. Rapoartele complete ale uneltei sunt fișierele `*_cfo.md`. Cele 36 de luni sunt calculul meu peste ieșirile uneltei (`build_model.py` → `model_36m.md`, `model_36m.json`). Unealta afișează „$”, dar toate sumele sunt **EUR fără TVA**. Intrările sunt aproape toate **estimări** (`cfo-sources.md`). Nu e consultanță financiară sau fiscală: structura, TVA-ul la vânzarea dispozitivelor și contractul cu firma de pază trebuie verificate cu un contabil și un avocat înainte să se miște bani.

## Nota CFO

- **Marja.** Un lucrător lasă puțin, iar marja depinde de dispecerat și de cine plătește dispozitivul:
  - **C (clientul cumpără dispozitivul, 12 EUR/lună):** contribuția e de **6,79 EUR** pe lucrător-lună (57%) cu comisionul de canal, și 7,33 EUR fără el;
  - **B (dispozitiv inclus, 14 EUR):** 5,68 EUR (41%). La 20 EUR, cu dispozitiv inclus: 11,20 EUR (56%);
  - pentru comparație, Scadențarul MM din analiza anterioară lăsa ~61 EUR pe client (94%).
- **Pragul (stare stabilă, vedere amortizată), la C 12 EUR:**
  - 50 de lucrători: −186 EUR/lună; pragul e la 78 de lucrători (`scale_50_C12_cfo.md`);
  - 200 de lucrători (cu 0,25 normă ajutor): +383 EUR/lună (16%); pragul e la 144 de lucrători;
  - 1.000 de lucrători (cu 2 angajați): +3.660 EUR/lună (31%); pragul e la 461 de lucrători.
- **Linia de urmărit: tariful dispecerului.** Nu există niciun tarif românesc găsit (N05 §4):
  - la 4 EUR în loc de 2,50, anul 2 trece de la +2.221 EUR la **−59 EUR** pe operațiuni (`whatif_y2_dispatch400_cfo.md`);
  - imediat după vine rampa: la −20% volum, anul 1 scade de la −4.468 la −4.834 EUR, iar efectul crește în anii următori.
- **Numerarul:**
  - C: **~8.400 EUR** necesari până se autofinanțează, cu taxele de pilot și marja pe dispozitive (cel mai adânc punct e în luna 5). Fără aceste încasări unice, unealta dă **11.013 EUR** (`base_y1_cfo.md`); cumulatul revine pe zero în **luna 21**;
  - B (14 EUR, dispozitiv inclus): **~25.400 EUR** necesari, adică tot capitalul; în 36 de luni nu revine pe zero (−11.235 EUR);
  - **concluzie:** nu finanța dispozitivele din capitalul propriu.
- **Trei pârghii, fiecare dovedită cu unealta (anul 2 al scenariului de bază, profit operațional +2.221 EUR):**
  1. **Prețul de 14 EUR în loc de 12, tot cu dispozitivul cumpărat de client:** anul 2 urcă la **+5.018 EUR** (+2.797 EUR), iar pragul coboară de la 99 la 78 de lucrători (`whatif_y2_price14_cfo.md`).
  2. **Fără minim lunar la pază și RC la 100 EUR/lună:** anul 2 urcă la **+4.621 EUR**, iar pragul ajunge la 70 de lucrători (`whatif_y2_lowfixed_cfo.md`).
  3. **Dispecerat la 1,50 EUR, negociat sau prin dispeceratul propriu al clientului/pazei:** anul 2 urcă la **+3.741 EUR**, cu pragul la 87 (`whatif_y2_dispatch150_cfo.md`).
- **Condițiile de bani ale board-ului:**
  - pilot plătit din prima zi: oferta v2 îl include (2.500 lei), dar nu e încă vândut;
  - bani riscați plafonați la ~6.600 EUR până la prima plată: pornirea C e de 6.546 EUR, iar până în luna 5 se ajunge la 8.421 EUR, adică **puțin peste plafon**;
  - oferte reale pentru RC și pentru dispecerat: **niciuna nu există încă**;
  - concluzie: **nicio condiție nu e îndeplinită**; toate devin metrici de validare (vezi planul).

## Rezultatele pe scurt

**Stare stabilă (vedere amortizată, fișierele `scale_*`):**

- **50 de lucrători** (fondator singur, costuri fixe 525 EUR/lună):
  - C 12 EUR: −186 EUR/lună; C 10 EUR: −278;
  - B 14 EUR: −241 (capital în dispozitive ~4.400 EUR); B 20 EUR: +35.
- **200 de lucrători** (costuri fixe 975 EUR/lună):
  - C 12: +383; C 10: +15;
  - B 14: +161 (capital în dispozitive ~17.700 EUR); B 20: +1.265.
- **1.000 de lucrători** (2 angajați, costuri fixe 3.130 EUR/lună):
  - C 12: +3.660; C 10: +1.820;
  - B 14: +2.550 (capital în dispozitive ~88.500 EUR); B 20: +8.070.

**Treptele din `../pricing/pricing.md`, la 200 de lucrători:**

- **B la 16 EUR** (dispozitiv inclus): contribuție 7,52 EUR, +529 EUR/lună, prag 130 de lucrători (`scale_200_B16_cfo.md`).
- **„Dispeceratul vostru” la 6 EUR** (dispecerul și SIM-ul sunt ale clientului, fără minim la pază): contribuție 5,45 EUR, +265 EUR/lună, prag 151 de lucrători (`scale_200_D6_cfo.md`).

**Pe 36 de luni (vedere numerar, `model_36m.md`):**

- **Bază (C 12 EUR, 10–12 h/săpt):**
  - clienții încep să plătească în lunile 6, 9, 12, 15 și 18, apoi orele se termină;
  - MRR (venit lunar recurent): 840 EUR în luna 12, 2.160 în luna 24, 2.400 în luna 36 (5 clienți, 200 de lucrători);
  - **1.000 EUR MRR în luna 15. 3.000 EUR MRR: niciodată** la 10–12 h/săpt (plafonul e de ~2.400 EUR);
  - anul 1, cu tot cu pornirea: −5.108 EUR; anul 2: +7.536; anul 3: +8.551;
  - numerar necesar: 8.421 EUR; cumulat la 36 de luni: +10.978 EUR.
- **B (14 EUR, dispozitiv inclus, aceeași rampă):**
  - MRR 980 / 2.520 / 2.800 EUR; 1.000 EUR MRR în luna 15; 3.000 niciodată;
  - **numerar necesar: 25.387 EUR**; cumulat la 36 de luni: −11.235 EUR.
- **Pesimist** (10 EUR, dispecerat 4 EUR, client nou la 6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20):
  - MRR 150 / 350 / 850 EUR; **1.000 EUR MRR nu vine în 36 de luni**;
  - numerar necesar: 16.017 EUR; cumulat la 36 de luni: −16.017 EUR, adică nu se recuperează nimic.
- **20 h/săpt din luna 13** (C 12 EUR, client nou la 2 luni):
  - MRR 840 / 3.240 / 5.640 EUR;
  - 1.000 EUR MRR în luna 14, **3.000 EUR MRR în luna 24**;
  - 13 clienți și 470 de lucrători în luna 36; cumulat +43.912 EUR;
  - peste ~300 de lucrători e nevoie de ajutor plătit, pe care modelul nu-l mai adaugă.
- **Costul timpului:** la 20 EUR/h, timpul fondatorului (~960 EUR/lună) depășește tot profitul cumulat din scenariul de bază (calculul meu).
