# Prețul: „Lucru izolat conform, la cheie”

Toate prețurile sunt în EUR pe lucrător pe lună, fără TVA. `van_westendorp.py` afișează „$”, dar e vorba de EUR. Răspunsurile vin de la cumpărători **simulați** (`../panel/`): ele aleg ce să testezi, nu dovedesc nimic.

## 1. Ce au spus cumpărătorii (curba Van Westendorp)

- **v1** (`v1-curve.md`, 30 de răspunsuri, pitch cu 20 EUR):
  - interval acceptabil **6,02–19,97 EUR**; OPP (prețul cu cea mai mică rezistență) 6,10; IPP (punctul de indiferență) **11,00**;
  - mediane: prea ieftin 5, chilipir 8, începe să fie scump 15, prea scump 25;
  - **20 EUR e chiar peste marginea de sus** (PME, pragul de la care prea mulți spun „prea scump”: 19,97).
- **v2** (`v2-curve.md`, pitch cu 14 EUR și 9 EUR la „dispeceratul vostru”):
  - interval **4,04–15,98 EUR**; IPP **8,01**;
  - mediane: 3 / 7 / 15 / 25;
  - 14 EUR e în interval, aproape de margine. Menționarea prețului de 9 EUR a tras ancorele în jos (judecata mea).
- **Doar HSE și utilități** (`v2-hse-utilitati-curve.md`, 12 răspunsuri):
  - interval **4,05–19,99 EUR**; mediane 4 / 8 / 16 / 28.
- **Pragul „scump” pe segment** (mediana „începe să fie scump” în v1 / v2, calculul meu din răspunsuri):
  - HSE fabrică: 21 / 17;
  - serviciu extern SSM: 17 / 15;
  - forestier: 16,5 / 13;
  - utilitate: 14,5 / 15;
  - pază: 14 / 9.

## 2. Ce cer concurenții (din `../competitors/competitors.md`, calculul meu în EUR)

- **StaySafe (UK), aplicație + ARC:**
  - ~11–13 EUR la 0–50 de utilizatori (listă publică G-Cloud);
  - ~6 EUR la peste 7.500 de utilizatori (N03 §2).
- **Peoplesafe MySOS**, dispozitiv dedicat: ~17,5–19 EUR/lună plus ~60 EUR la început (sursă terță).
- **Venitul realizat, ca reper:**
  - Peoplesafe: ~6,3 EUR (N03 §2, estimare);
  - media europeană: ~10 EUR (N03 §5).
- **Blackline G7c**, cu gaze: ~56 EUR (R §3).
- **Ancorele locale:**
  - GPS de flotă: ~50 lei (~10 EUR)/vehicul;
  - serviciu extern SSM: 8–25 lei (1,6–5 EUR)/angajat (N05 §3).
- **Comparația corectă** e cu serviciul complet (dispozitiv + om care răspunde), nu cu aplicația gratuită: 11–19 EUR în UK.

## 3. Ce are nevoie afacerea (CFO, `../cfo/`)

- **C**, clientul cumpără dispozitivul (~130 EUR):
  - la 12 EUR: contribuție 6,79 EUR/lucrător-lună; prag 144 de lucrători la 200 (costuri fixe 975 EUR/lună);
  - la 10 EUR: contribuție 4,95; pragul urcă la 197 de lucrători, adică rezultatul e practic zero la 200.
- **B**, dispozitiv inclus:
  - la 14 EUR: contribuție 5,68; prag 172 de lucrători; ~17.700 EUR blocați în dispozitive la 200 de lucrători;
  - la 20 EUR: contribuție 11,20; prag 87.
- **Concluzia:** sub 12 EUR (C) sau sub ~18 EUR (B) afacerea nu are marjă la scara pe care o poate atinge fondatorul.

## 4. Decizia

1. **Prețul.** Implicit e structura **C**: dispozitivul îl cumpără clientul cu **~650 lei (130 EUR)**, configurat, iar abonamentul e de **12 EUR (~60 lei) pe lucrător pe lună**, numai pentru lucrătorii expuși, cu contract de 12 luni.
   - 12 EUR stă în intervalul acceptabil al ambelor variante. E puțin peste IPP (8–11) și sub pragul „scump” al HSE și al utilităților (15–21).
   - E la nivelul StaySafe pentru echipe mici, fără să fie mai ieftin decât o aplicație din UK. Diferența o fac limba română, dispeceratul local și documentele.
   - Pentru clientul care nu vrea să cumpere dispozitive există **varianta B: 16 EUR (~80 lei) cu dispozitiv inclus**, plafonată la ~60 de dispozitive finanțate de ILLUSTRUS. Peste plafon, prin leasing sau prin distribuitor.
2. **Scara** (good / better / best):
   - **„Dispeceratul vostru”, 6 EUR:** pentru firmele de pază și pentru fabricile cu dispecerat propriu 24/7. Ecranul APEX, regulile, jurnalul și pachetul de documente; fără dispecer ILLUSTRUS și fără SIM inclus. Panelul de pază cere 4–7 EUR.
   - **„Standard”, 12 EUR:** dispozitiv al clientului + dispecer extern 24/7 + raport lunar.
   - **„Standard cu dispozitiv”, 16 EUR.**
   - **Satelit** pentru șefii de echipă din pădure: costul Garmin plus 15%. Abia după ce lanțul a fost dovedit la oraș.
3. **Oferta de deschidere:**
   - testul de semnal gratuit;
   - pilotul plătit de 2.500 lei (~500 EUR), cu dispozitive împrumutate și documentele incluse, valabil pentru **primii 3 clienți până la 30 iunie 2027**;
   - prețul de 12 EUR blocat 24 de luni pentru acești 3 clienți.
   - Nu există un preț „vechi” tăiat și nu se face reducere la abonament, ca să nu înveți piața să aștepte reduceri.
4. **Ce se testează cu cumpărători reali:**
   - **12 EUR față de 14 EUR** pe structura C, la primii 6 cumpărători calificați (HSE și utilități), cu aceeași ofertă scrisă și doar prețul schimbat. Se măsoară câți semnează pilotul plătit;
   - separat, **6 EUR față de 8 EUR** pentru „dispeceratul vostru”, la 3 firme de pază.
   - Prețul de 14 EUR adaugă ~2.800 EUR în anul 2 (CFO, `whatif_y2_price14_cfo.md`).
5. **Cele mai repetate trei obiecții de preț** (simulate, pentru marketing):
   - „100 de lei pe om pe lună e mai mult decât plătesc pe tot serviciul SSM” (v1/P011);
   - „Cu 200 de agenți ar însemna 48.000 EUR pe an, iar clienții nu mi-l plătesc în plus” (v1/P007);
   - „70 de lei tot mi se pare mult pentru oameni în pădure” (v2/P011).
   - **Răspunsul:** prețul se plătește doar pe lucrătorii expuși (5–15% din personal la o fabrică), nu pe tot personalul. La o fabrică, 30 de lucrători × 12 EUR = 360 EUR pe lună.
