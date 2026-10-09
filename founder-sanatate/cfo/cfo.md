# Nota CFO: A (Scadențar MM + portal) și G (Controale pierdute)

**Toate cifrele de mai jos vin din `unit_economics.py`**, rulat pe fișierele `*_numbers*.json` din acest folder. Excepție: orizontul de 36 de luni, care e calculul meu peste ieșirile uneltei (`combine_36m.py`). **Sursa fiecărei intrări** e în `cfo-sources.md`: aproape toate sunt estimările mele, nu oferte reale. Unealta afișează „$”, dar toate sumele sunt în **EUR, fără TVA**. Unitatea e **un client pe o lună**: `days_per_month = 1`, deci „per day” înseamnă „clienți activi în luna respectivă”. SMS-urile se refacturează la cost și sunt scoase și din preț, și din cost. **Nu e consultanță financiară, fiscală sau juridică.** Un contabil trebuie să verifice structura (SRL, TVA, deductibilitate) înainte să se miște bani.

## Rezumat

| Indicator | A (bază) | A („spre 3k”) | G (bază) |
|---|---:|---:|---:|
| Preț mediu / client-lună | 65 € | 65 € | 89 € |
| Contribuție / client-lună | 61 € (94%) | 61 € | 84,5 € (95%) |
| Costuri fixe / lună | 230 € | 230 € (310 € din anul 2) | 230 € |
| Prag de rentabilitate lunar | 4 clienți | 4 clienți | 3 clienți |
| Cheltuiala de pornire (numerar) | 2.980 € | 2.980 € | 3.900 € |
| Numerar necesar până se autofinanțează | **3.825 €** | 3.825 € | **5.233 €** |
| Profit operațional anul 1 | +534 € | +534 € | −1.070 € |
| MRR luna 12 / 24 / 36 | 650 / 1.430 / 1.625 € | 650 / 2.210 / 3.250 € | 356 / 890 / 1.157 € |
| **Luna cu MRR ≥ 1.000 €** | **18** | 15 | 27 |
| **Luna cu MRR ≥ 3.000 €** | **niciodată** (plafon de timp: 25 de clienți ≈ 1.625 €) | **31** | niciodată (plafon: 13 clienți ≈ 1.157 €) |
| Luna în care se recuperează pornirea | 17 | 17 | 25 |
| Luna în care profitul cumulat ajunge la 25.000 € | 36 | 30 | peste 36 |
| Profit cumulat la 36 de luni, după pornire | 22.229 € | 40.134 € | 9.790 € |

**Scenariul „spre 3k”** presupune două lucruri: fondatorul trece la ~20 h/săpt din luna 13, iar vânzarea crește la +2 clienți/lună. Ajunge la 50 de cabinete plătitoare, adică ~10% din cele 508 cabinete listate la nivel național (RSMM §3). E un risc real de saturare.

## Nota CFO

- **Marja:** A lasă 61 € pe client-lună (94%). La planul de 16 clienți, marja după toate costurile e de 72% (`A_cfo.md`). G lasă 84,5 € (95%), cu 73% la plan (`G_cfo.md`). **Marja nu e problema.** Software-ul administrativ are costuri variabile mici.
- **Ce trebuie urmărit: rampa și timpul fondatorului, nu banii.**
  - La volum −20%, anul 1 al lui A trece pe pierdere: **−125 €** (tabelul „What if” din `A_cfo.md`).
  - Plafonul real e timpul. La 10–12 h/săpt, fondatorul poate deservi ~25 de clienți A sau ~13 clienți G (estimare în `cfo-sources.md`). La prețurile acestea, **niciuna dintre idei nu ajunge singură la 3.000 € MRR**.
- **Numerarul:** A are nevoie de **~3.800 €**, G de **~5.200 €**, din 25.000 € disponibili. **Capitalul nu e constrângerea.** Restul de ~20.000 € e rezervă: asigurare, avocat la nevoie, un ajutor part-time în anul 2.
- **Trei moduri de a îmbunătăți rezultatul** (fiecare cu rularea uneltei care îl dovedește):
  1. **Prețul mediu la 79 € în loc de 65 €:** profitul din anul 1 crește de la 534 € la **1.290 €**, iar pragul scade la 3 clienți (`--price 79`). Panelul arată că firmele medii au pragul „scump” la 95–120 €.
  2. **Un canal care aduce +50% volum** (un vendor de program MM sau o asociație profesională care recomandă produsul): anul 1 urcă la **2.181 €**, cu MRR 975 € în luna 12; anul 2 urcă la **15.357 €**, cu MRR 2.145 € în luna 24 (`--volume 1.5`). Atenție: la acest volum, plafonul de 25 de clienți e atins în anul 2.
  3. **Costuri fixe mai mici** (deplasări fără cost dedicat, asigurare negociată la 30 €/lună): pragul scade de la 4 la **2 clienți**, iar anul 1 urcă la **1.734 €** (`A_numbers_lowfixed.json`).
- **SMS absorbit în loc de refacturat** (~12 €/client-lună la A, ~9 € la G): contribuția scade la 49 € (A) și 75,5 € (G). Anul 1 al lui A ajunge la **−114 €**, iar G la −1.250 € (`A_cfo_sms_absorbed.md`, `G_cfo_sms_absorbed.md`). Refacturarea trebuie scrisă în contract.
- **Costul complet** (timpul fondatorului la 20 €/h, 1 h/client-lună pentru A și 2 h pentru G): contribuția scade la 41 € pentru A și la 44,5 € pentru G. **Anul 1 al lui A trece pe pierdere: −546 €** (`A_cfo_fullcost.md`). Cu timpul inclus, A e o afacere bună abia din anul 2.
- **CAC (estimare):** ~25–40 h de vânzare pe client câștigat, plus 50–100 € deplasări. În numerar asta înseamnă ~75–150 €. Cu timpul la 20 €/h, ~600–900 €. La 61 € contribuție, **recuperarea CAC-ului complet durează ~10–15 luni**. De aceea un client care pleacă în primul an e o pierdere.
- **Orele pe client (estimare):** A are nevoie de 6–10 h de integrare și ~1 h/lună de suport. G are nevoie de 10–15 h de integrare și ~2 h/lună de suport.
- **Condițiile de bani ale board-ului** (`../board/board.md`):
  - „3 pre-vânzări plătite înainte de construcție”: **neîndeplinită**. E prima țintă a validării de 90 de zile.
  - „G: audit cu recuperări de 5× prețul”: **neîndeplinită**.
  - „Lista de ≥20 de cabinete accesibile”: **neîndeplinită**. Ea condiționează direct rampa de mai sus.

## Fișierele

- **Intrări:** `A_numbers.json`, `A_numbers_y2.json`, `A_numbers_y3.json`, `A_numbers_fullcost.json`, `A_numbers_lowfixed.json`, `A_scale_numbers*.json`, `G_numbers*.json`.
- **Rapoartele uneltei:** `A_cfo.md`, `A_cfo_y2.md`, `A_cfo_y3.md`, `A_cfo_fullcost.md`, `A_scale_cfo_y2.md`, `G_cfo.md`, `G_cfo_y2.md`, `G_cfo_y3.md`, `G_cfo_fullcost.md`. Ieșirile JSON sunt în `*.out.json`.
- **36 de luni:** `A_36m.md`, `A_scale_36m.md`, `G_36m.md` (`combine_36m.py`).
