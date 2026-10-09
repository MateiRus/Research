# Ideea de proiect STEP: pașaport digital, telemetrie și a doua viață pentru baterii, produse în Bihor

**Data:** 9 octombrie 2026. **Cerința:** o idee concretă de proiect pentru apelul STEP al Programului Regional Nord-Vest (PRNV/2026/961/1 sau o fereastră STEP ulterioară), presupunând că eligibilitatea este rezolvată, cu presupunerile scrise explicit. Repo-ul a fost folosit doar ca context (competențe, canale, lecții), nu ca plan.

---

## 0. Ce presupun (și ce se întâmplă dacă presupunerea cade)

| # | Presupunere | Dacă nu e adevărată |
|---|---|---|
| P1 | ILLUSTRUS (sau un vehicul nou cu sediul în Nord-Vest) îndeplinește ESO1–ESO6: an fiscal închis cu profit din exploatare, salariat mediu ≥ 1, fără excludere, drept de folosință asupra halei. | Vehicul nou cu un partener industrial ca acționar majoritar; ILLUSTRUS rămâne furnizorul de software. |
| P2 | Cofinanțare de **~3–3,5 mil. EUR** [ESTIMARE] disponibilă (bancă, investitor, partener industrial), plus capital de lucru pentru prefinanțarea TVA și a tranșelor. | Varianta „lean” de mai jos (grant ~5,2 mil.) cu cofinanțare ~2 mil.; sub asta, proiectul nu atinge minimul de 5 mil. grant. |
| P3 | O echipă nominală există: director de proiect cu ≥ 5 ani în baterii/energie/electronică, un inginer de putere/BMS, un inginer software; tu ești lead pe date, AI și platformă. | Pierzi 6–10 puncte din criteriul 2.1; proiectul rămâne peste pragul de 65, dar nu peste 85. |
| P4 | Un centru de transfer tehnologic (Universitatea din Oradea CNCG-CTT, UTCN, INCDTIM Cluj) sau un cercetător științific gradul I semnează raportul pentru criteriile 1.2 / 5.1 / 5.2. | Fără raport, criteriile 5.1 și 5.2 pot fi notate 0 și proiectul e respins; e pe drumul critic. |
| P5 | Fereastra de depunere: fie 961 până la **02.11.2026 ora 10:00** (după Corrigendum nr. 2) cu un consultant deja contractat, fie o fereastră STEP ulterioară în PR Nord-Vest (dacă alocarea de 20,95 mil. nu se consumă) — apelurile STEP din alte regiuni cer sediul acolo. | Dacă nu există a doua fereastră în NV, ideea se construiește fără grant (secțiunea 9) și se depune la POCIDIF/alte scheme când apar. |
| P6 | Reguli presupuse din notele de research (toate din rezumate de căutare, de citit pe original): fiecare proiect trebuie să conțină cel puțin o activitate de producție pe art. 14 (minim 3 mil. grant); intensitate regională Nord-Vest 40% bază [ESTIMARE, HG 311/2022] + 20 pp întreprindere mică + 10 pp STEP (SA.115647 / HG 248/2025) [de verificat] → până la 70%; art. 25: 80% cercetare industrială, 60% dezvoltare experimentală; art. 28: 100% până la 220.000 EUR; minimis 300.000 EUR; implementare până la 31.12.2029. | Dacă intensitățile sunt mai mici, cofinanțarea crește cu 0,5–1 mil. EUR; structura ideii nu se schimbă. |
| P7 | Faptele de piață de mai jos (termenul pașaportului, registrul UE, Casa Verde Baterii) sunt corecte conform surselor citate; textul Reg. (UE) 2023/1542 art. 77 și Anexa XIII nu a fost citit pe EUR-Lex (proxy blocat). | Dacă termenul de 18.02.2027 se amână, piața pașaportului se mută cu 1–2 ani; telemetria și a doua viață rămân. |

---

## 1. Ideea într-un paragraf

**Un nod regional pentru bateriile staționare și industriale: platforma de pașaport digital al bateriei (DPP) găzduită în UE, un modul de telemetrie independent de producătorul BMS fabricat în Bihor, și o linie de diagnoză și „a doua viață” care gradează bateriile uzate cu modele AI de stare de sănătate (SoH) și le reasamblează în stocare staționară.** Din 18 februarie 2027, orice baterie industrială peste 2 kWh, orice baterie de vehicul electric și de mobilitate ușoară pusă pe piața UE trebuie să aibă pașaport digital, accesibil prin QR și înregistrat în registrul UE, care e activ din 20 iulie 2026 ([Codibly](https://codibly.com/blog/articles/eu-battery-regulation-passport-bess-operators); [Scantrust](https://www.scantrust.com/eu-battery-regulation-eu-battery-passport-requirements/); [Elevenes](https://elevenes.com/news/the-eu-battery-passport-what-it-requires-who-benefits-who-pays/)) [VERIFICAT din surse de furnizori; de citit art. 77 și Anexa XIII pe EUR-Lex]. Obligația cade pe cine pune bateria pe piață: producătorul UE sau **importatorul**. În Nord-Vest există un producător de baterii (Rombat, Bistrița: 618,7 mil. RON venituri 2025, 694 angajați [VERIFICAT, Termene via căutare]), un val de ~27.000 de baterii rezidențiale de minimum 10 kWh prin Casa Verde Baterii (400 mil. lei, Ordin 1.904/2026, lansare anunțată pentru octombrie 2026 ([Economedia](https://economedia.ro/prosumatorii-cer-sa-fie-consultati-inainte-de-lansarea-programului-casa-verde-baterii-2026.html); [Alba24](https://alba24.ro/casa-verde-baterii-2026-program-de-400-de-milioane-de-lei-prosumatorii-cer-reguli-clare-inainte-de-lansare-1152388.html)) [VERIFICAT], aproape toate importate, și peste 250.000 de prosumatori. Nu am găsit nicio firmă din România care să facă pașaport digital, telemetrie neutră sau diagnoză SoH pentru a doua viață [căutare 9.10.2026; absența nu e dovadă].

## 2. De ce intră în STEP (argumentul pentru raportul CTT)

- **Sector:** tehnologii curate și eficiente din punctul de vedere al resurselor (lanțul valoric al bateriilor și stocării, tehnologie net-zero conform NZIA) **și** tehnologii digitale (IoT, spații de date, AI pentru estimarea stării de sănătate). Dubla încadrare contează la 5.1 și la RCO125/126.
- **Condiția (b), dependențe strategice:** bateriile și sistemele de management (BMS) sunt dependența-manual a UE față de Asia; un modul de telemetrie și o platformă de date europene, neutre față de producătorul BMS, și recondiționarea bateriilor în UE reduc dependența de celule noi și de date închise ale furnizorilor. Formulează exact așa în 5.2.
- **Condiția (a), element inovator cu potențial economic:** modele de SoH/RUL (durată rămasă) antrenate pe date de exploatare reală din stocare staționară, folosite pentru gradare la a doua viață; literatura arată că lipsa istoricului bateriei e problema centrală a reutilizării ([TUM](https://mediatum.ub.tum.de/doc/1319473/1319473.pdf); [Batteries 2024](https://hal-hprints.archives-ouvertes.fr/ENTPE/hal-04564165v1)) [VERIFICAT, surse academice via căutare]. Asta e „inovație de proces” (1.2.c) și „tehnologie emergentă” (1.2.d); nu pretinde „ruptură” (1.2.a).
- **Piața:** rapoartele comerciale estimează piața pașaportului de la 0,15 mld. USD (2025) la 2,35 mld. USD (2035) ([MarketsandMarkets](https://www.marketsandmarkets.com/ResearchInsight/battery-passport-market.asp)) [ESTIMARE comercială]; jucători: Circulor, Minespider, Spherity, Siemens, AVL, Optel [VERIFICAT că există; poziționarea lor pe stocare staționară nu a fost găsită].

## 3. Ce se construiește (trei straturi, două variante de buget)

| Strat | Ce este | Linia de ajutor | Rolul tău |
|---|---|---|---|
| **S1. Platforma DPP** | Software găzduit în UE: emitere pașaport per baterie (identitate, amprentă de carbon, conținut reciclat, performanță, due diligence, Anexa XIII), QR, integrare cu registrul UE, API pentru producători/importatori, portal pentru proprietar, actualizare automată din telemetrie | art. 25 (dezvoltare experimentală) + art. 28 (consultanță inovare, brevete/mărci, baze de date) | Arhitectura de date, APEX/ORDS pentru portal și API, n8n pentru fluxuri cu furnizorii, LLM pentru extragerea datelor din fișele tehnice și declarațiile furnizorilor |
| **S2. Modulul de telemetrie** | Gateway hardware neutru față de BMS (CAN/Modbus/RS485 → LTE/Wi-Fi), carcasă, firmware, linie de asamblare, programare și testare în Bihor; SMT subcontractat la un EMS din Oradea | art. 14 (hală, linie de asamblare/test, echipamente) + art. 25 (firmware, algoritmi la margine) | Specificație de date, pipeline, calibrare; inginerul hardware conduce designul |
| **S3. Linia de diagnoză și a doua viață** | Bancuri de test (ciclatoare, camere climatice, impedanță), gradare cu modelele SoH, reasamblare în module de stocare staționară, pașaport actualizat „second-life” | art. 14 (echipamente, hală) + art. 25 (modele SoH/RUL, validare) + art. 41 opțional (instalație PV + stocare proprie pentru teste și consum) | Modelele AI și trasabilitatea; partener industrial pentru procesul fizic |

**Varianta completă (S1+S2+S3):** grant ~7–8 mil. EUR, 8–10 locuri de muncă. **Varianta lean (S1+S2, cu S3 doar ca laborator de validare):** grant ~5,2–5,5 mil. EUR, 5–6 locuri de muncă. Recomand **lean pentru prima depunere**: minimul de 5 mil. e atins, art. 14 e acoperit de linia de module și servere, iar a doua viață rămâne ca etapă 2 finanțabilă separat.

## 4. Cine cumpără și de unde vin scrisorile de intenție

| Cumpărător | Ce cumpără | De ce acum | Rol în dosar |
|---|---|---|---|
| **Rombat** (Bistrița, NV) | Pașapoarte pentru bateriile industriale > 2 kWh (tracțiune, staționare), telemetrie pentru flote | Obligație din 18.02.2027; producător regional fără soluție publică [absență în căutare] | Scrisoare de intenție; potențial partener/acționar în vehicul |
| **Importatori și distribuitori de baterii rezidențiale** (NV și național) | Pașaport „as a service” per baterie + telemetrie pentru garanție | Importatorul poartă obligația; valul Casa Verde Baterii de ~27.000 unități ≥ 10 kWh [VERIFICAT, estimare APCE/minister] | 3–5 scrisori; cel mai rapid venit |
| **Instalatori validați AFM** (Bihor, Cluj, Arad) | Telemetrie + portal pentru clienți, dovezi pentru garanție | Legea 160/2026 face bateria mai valoroasă; instalatorii nu au date după punere în funcțiune | Scrisori; canal spre proprietari |
| **Renovatio Solar** (Cluj, EPC; Borzești 918 MWh cu CATL ([Actual de Cluj](https://actualdecluj.ro/?p=293505))) | Monitorizare neutră și pașaport pentru parcuri de stocare | Operatorii BESS trebuie să aibă pașaport pentru bateriile puse în funcțiune după 2027 | Scrisoare de intenție pentru 4.3 (scalare) |
| **Prime Batteries** (Cernica, Ilfov; 2,5 → 8,5 GWh ([Energynomics](https://www.energynomics.ro/en/prime-batteries-technology-expands-battery-production-capacity-to-8-5-gwh))) | DPP pentru producție proprie, telemetrie pentru clienți | Nu am găsit soluție DPP anunțată [absență în căutare] | Client național, nu regional |
| **Piețe externe** (HU, PL, BG, DE) | Aceeași obligație UE; distribuitori CEE fără furnizor local | Regulamentul e identic în toată UE | 1–2 scrisori pentru 4.3; parteneriat cu un distribuitor maghiar |

## 5. Schiță de buget (varianta lean) [ESTIMARE, de refăcut cu oferte]

| Linie | Cheltuieli eligibile | Intensitate (P6) | Grant | Cofinanțare |
|---|---|---|---|---|
| Art. 14 regional: hală (închiriere/amenajare), linie asamblare și test module, servere și echipamente de laborator | 5.000.000 | 60–70% | 3.000.000–3.500.000 | 1.500.000–2.000.000 |
| Art. 25 CD: cercetare industrială (modele SoH/RUL, date) | 900.000 | 80% | 720.000 | 180.000 |
| Art. 25 CD: dezvoltare experimentală (platformă DPP, firmware, pilot) | 1.200.000 | 60% | 720.000 | 480.000 |
| Art. 28 inovare IMM: raport CTT, studiu de piață, consultanță inovare, protecție IP | 220.000 | 100% | 220.000 | 0 |
| Minimis: consultanță scriere/implementare, proiectare, publicitate (15.000 lei fără TVA) | 300.000 | 100% | 300.000 | 0 |
| **Total** | **~7.600.000** | | **~5.000.000–5.500.000** | **~2.200.000–2.700.000** |

Grantul e între 5 și 7 mil., deci criteriul 1.1 cere **> 4 locuri de muncă** pentru 6 puncte: planifică 6 ENI (2 ingineri, 2 operatori linie/test, 1 vânzări/conformitate, 1 date). TVA e eligibilă doar dacă e nedeductibilă; cu ILLUSTRUS plătitor de TVA, bugetează TVA ca neeligibil și prefinanțează-l.

## 6. Cum ar puncta pe grila din transcriere [ESTIMARE; grila a fost modificată prin Corrigendum 2]

| Criteriu | Puncte posibile | Estimare | De ce |
|---|---|---|---|
| 1.1 locuri de muncă | 6 | 6 | 6 ENI asumate, justificate în planul de afaceri |
| 1.2 inovație | 5 | 3 | b (produs), c (proces), d (emergentă); fără a și, probabil, fără e |
| 2.1 echipă | 12 | 6–8 | P3: director 5 ani (4), un membru 3 ani (2), management operațional (2) de la partener; experiența UE (2) doar dacă aduci un consultant/membru cu 2 proiecte |
| 2.2 solvabilitate | 4 | 2–4 | depinde de bilanțul vehiculului |
| 2.3 cash-flow | 4 | 4 | planul financiar trebuie să arate flux cumulat pozitiv |
| 3 maturizare ≥ 10% | 8 | **0** | ILLUSTRUS nu are 500.000 EUR de investiții anterioare; acceptă pierderea, nu o inventa |
| 4.3 scalare internațională | 3 | 3 | scrisori din CEE + strategie de distribuție |
| 4.1, 4.2, 4.4 | necunoscute | ? | lipsesc din transcriere; probabil ~20 p; spillover-ul e bun (standard DPP, date deschise) |
| Secțiunea II | 11 | 11 | obligatorii; raportul CTT și bugetul corelat sunt condiții |
| **Total orientativ** | 100 | **~70–80** | peste pragurile de 65/75 din ultimele ferestre; sub 85/90 |

Regula „punctaj ETF cu peste 5 puncte sub autoevaluare = respingere” (din transcriere, de verificat după Corrigendum 2) spune: **autoevaluează conservator**, nu optimist.

## 7. Calendar realist

- **Dacă ținta e 961 (până la 02.11.2026):** trei săptămâni pentru vehicul, echipă, raport CTT, studiu de piață, plan de afaceri, machetă, 3 oferte per echipament, scrisori de intenție. Se poate doar dacă un consultant și un partener industrial intră săptămâna aceasta [PRESUPUNERE P5]. Altfel, nu forța: un dosar incomplet pierde puncte de secțiune II și e respins.
- **Dacă ținta e o fereastră ulterioară:** contract T2–T3 2027, hală și linie 2027–2028, producție 2028, pilot a doua viață 2029, durabilitate 2030–2032.
- **Independent de grant:** obligația de pașaport începe pe 18.02.2027. Stratul S1 (software) poate porni acum, fără grant, și devine dovada de „maturizare a ideii” pentru criteriul 3 la o depunere ulterioară (cheltuielile proprii pe S1 în 2026–2027 contează, cu raport de expert contabil).

## 8. Ce poate ucide ideea (spune-o înainte s-o spună evaluatorul)

1. **Furnizorii mari de DPP** (Circulor, Siemens, Minespider, Spherity) iau producătorii mari; tu rămâi cu importatorii mici și regionali, care plătesc puțin per baterie. Răspuns: preț per pașaport + telemetrie + garanție, nu platformă enterprise.
2. **Producătorii de invertoare/BMS** (Huawei, SolarEdge, BYD, Deye) includ monitorizarea în propriul cloud; telemetria neutră se vinde doar unde proprietarul vrea independență (operatori BESS, flote, second-life). Răspuns: ținta e stocarea industrială și a doua viață, nu doar rezidențialul.
3. **Standardele DPP** (CEN/CENELEC JTC 24, actele delegate) încă se finalizează; ce construiești în 2027 poate cere refacere în 2028. Răspuns: arhitectură pe standard deschis, nu pe format propriu.
4. **Nu știi baterii.** Fără inginer de putere și partener industrial (Rombat, un instalator mare, UTCN), raportul CTT nu se semnează. E presupunerea P3 și e cea mai fragilă.
5. **A doua viață** are reglementare și răspundere neclare (siguranță, garanție, cine e „producător” al bateriei reasamblate); literatura avertizează împotriva folosirii în aplicații critice pentru rețea. Răspuns: de aceea S3 e etapa 2.
6. **Cofinanțarea.** 2–3 mil. EUR nu vin dintr-un SRL cu un angajat; vin de la un partener. Dacă partenerul e majoritar, proiectul e al lui, iar tu ești CTO cu părți sociale. E un rezultat bun, nu o înfrângere.

## 9. Versiunea fără grant, care începe luna aceasta (și plătește obligația DR-36)

- **Produs:** „Pașaport + telemetrie pentru bateriile instalate de tine”, vândut instalatorilor validați AFM și importatorilor, ca portal web (CAEN 6310 e fix „portaluri web și prelucrare de date”): generezi pașaportul din fișa tehnică (extragere cu LLM, validare umană), QR pe baterie, pagină publică per baterie, actualizare lunară din datele invertorului acolo unde există API. Preț de test: 15–25 EUR/baterie/an [ESTIMARE, fără ancoră în RO].
- **De ce acum:** sesiunea Casa Verde Baterii se deschide în octombrie–noiembrie 2026; importatorii află despre obligația din februarie 2027 abia când distribuitorii lor din Vest le cer pașaportul. Canalul fără e-mail rece: telefon la instalatorii validați AFM (listă publică) și vizite la 3 importatori din Cluj/Oradea; se leagă direct de ideea „Bateria” din sesiunea laterală 4 din repo.
- **Ce produce pentru STEP:** date reale de exploatare (materia primă a modelelor SoH), 3–5 clienți pentru scrisori de intenție, cheltuieli de maturizare pentru criteriul 3, și dovada că piața există înainte de a cere 5 milioane.

## 10. Alternativele pe care le-am cântărit și de ce sunt a doua, a treia

| Idee | Încadrare STEP | De ce e mai jos |
|---|---|---|
| **B. Inspecție optică cu AI (AOI) la margine pentru EMS-urile din Oradea** (Plexus ~1.850 angajați ([ZF](https://www.zf.ro/te-inspira/oradea-poarta-catre-vest/oradea-poarta-catre-vest-proiect-zf-sustinut-banca-transilvania-22818536)), Celestica, Connectronics): producție de capete de inspecție cu modele antrenate on-prem | Digital (AI, robotică), lanțul valoric al semiconductorilor | Echipamentele AOI vin de la Koh Young/Omron/Orbotech cu decenii de avans; EMS-urile cumpără la nivel de grup; fără obligație legală care să creeze cerere; nevoie de expertiză în viziune și optică pe care nu o ai |
| **C. Nod regional de calcul AI suveran** (GPU edge-cloud la Oradea, modele RO/HU pentru industrie și sănătate) | Digital (AI, cloud/edge, HPC) | Capex și energie mari, GPU-urile sunt non-UE (argumentul de dependență se întoarce împotriva ta), Cloud Regional Nord-Vest (60,3 mil. EUR, public) ocupă spațiul public, cererea privată on-prem e neclară; locuri de muncă puține |
| **D. Software medical predictiv (MDSW clasa IIa)** din notele de sănătate din repo | Biotech/digital, incert | Certificare MDR 9–18 luni și 32–110 k EUR înainte de orice venit; art. 14 greu de justificat la 3 mil.; încadrarea „biotehnologie” e incertă pentru software |

Bateriile câștigă pentru că au **o obligație legală cu dată, un producător și un val de instalări în regiune, dublă încadrare STEP, date ca materie primă pentru AI, și un drum fără grant care începe acum**.

## 11. Următoarele 10 zile, dacă mergi pe idee

1. Citește pe EUR-Lex Reg. (UE) 2023/1542 art. 77, Anexa XIII și actele delegate publicate; notează ce câmpuri se cer de la importator (2 h).
2. Trei telefoane: responsabilul de conformitate de la Rombat („cine vă face pașaportul din februarie?”), un importator de baterii rezidențiale din Cluj/Oradea, un instalator validat AFM din Bihor (3 h).
3. O vizită la Universitatea din Oradea, CNCG-CTT: întrebarea e dacă semnează raportul tehnico-științific pentru încadrarea STEP și cu ce echipă de energetică (2 h).
4. O discuție cu biroul din Oradea al unui consultant care are pagină pentru 961 (Goodwill) sau cu Neotrust: „e fezabil un dosar până la 2.11 sau pregătim următoarea fereastră?” (1 h).
5. Construiește demo-ul S1: pașaport generat din fișa tehnică a unei baterii reale, cu QR și pagină publică, în APEX (8–10 h). Cu demo-ul în mână, întrebările 2–4 primesc răspunsuri reale.
6. Cere ADR Nord-Vest, în scris, dacă există intenția unei a doua ferestre STEP în 2027 dacă alocarea nu se consumă (30 min).

Dacă două din cele trei telefoane de la punctul 2 se termină cu „da, cât costă?”, ideea trece de la ipoteză la plan. Dacă niciunul, pivotezi pe alternativa B cu aceleași reguli de test.
