# PREVENT-NV: planul complet al proiectului STEP (echipă de 6 oameni)

**Ce e documentul:** planul de proiect pentru apelul STEP PR Nord-Vest. Ideea: o platformă de prevenție cardiovasculară predictivă, cu senzori certificați cumpărați, profil de risc din dosarul medical, centru de monitorizare și un hub de casă asamblat în Bihor.
**Ipoteze de lucru** (cerute de tine):
- cofinanțarea nu e o problemă;
- există un partener clinic și unul de cercetare;
- platforma și datele le construiești tu, cu AI.

**Atenție:** regulile vin din notele din repo (transcrierea ghidului, rezumate de căutare). Corrigendum nr. 2 (8.10.2026) a schimbat grila, valorile min/max și pragul de calitate. **Toate cifrele de mai jos trebuie verificate în ghidul consolidat**, iar sumele sunt estimări.
**Data:** 12 octombrie 2026.

---

## 1. Câți oameni îți trebuie ca să îndeplinești criteriile

| Criteriu | Ce cere (din transcriere, de verificat) | Ce facem |
|---|---|---|
| ESO4: eligibilitate | ≥1 salariat mediu în anul dinaintea depunerii | Firma solicitant are deja cel puțin 1 angajat înainte de depunere |
| 1.1 Locuri de muncă (6 p) | Grant 5–7 mil. EUR: **peste 4 locuri noi** pentru punctaj maxim (praguri mai mari la grant > 7 mil. EUR) | **6 ENI noi**, cu marjă de 1–2 peste prag |
| Indicator RCR01 | Locurile create se mențin 3 ani după proiect (IMM) | Bugetăm salariile și în durabilitate, din venituri |
| 2.1 Echipa (12 p) | Director ≥5 ani experiență; membri cu 5 și 3 ani; management operațional 5 ani; experiență în ≥2 proiecte UE (≥100.000 EUR) | Managerul de proiect cu experiență UE + responsabilul de calitate + partenerul clinic acoperă cerințele de vechime. Tu ești lider tehnic, nu director de proiect. |
| Cercetare „cu personal propriu” | Cercetătorii angajați la beneficiar | 2 cercetători angajați + tu, plus cercetare contractată pentru o parte |
| MDR / ISO 13485 | Roluri separate (dezvoltare, verificare, aprobare) + PRRC (persoana responsabilă cu conformitatea) | Dezvoltatorul face verificarea, responsabilul de calitate e PRRC |

**Concluzie: 6 angajați** (5 cu normă întreagă de la început + 1 din anul 2), cu un total de **6 ENI**. Ești peste prag cu marjă, iar fiecare rol e justificat de o cerință.

## 2. Echipa

| # | Rol | Normă | Ce face | Profil | Cost lunar estimat (angajator) |
|---|---|---|---|---|---:|
| 1 | **Lider tehnic / arhitect (tu)** | 1,0 | Arhitectura, platforma, integrarea dispozitivelor, datele, cu AI (inclusiv Fable) | Tu, cu normă întreagă pe proiect | 4.500 € |
| 2 | **Dezvoltator software** | 1,0 | Dezvoltare, teste, verificare independentă (cerută de IEC 62304), întreținere | 3+ ani experiență | 3.500 € |
| 3 | **Cercetător AI / date medicale** | 1,0 | Modele de risc, predicția agravării, calibrarea pe populația din România | Doctorat sau doctorand în ML / informatică medicală | 4.500 € |
| 4 | **Cercetător AI / semnal biomedical** | 1,0 | Fibrilația atrială din ECG, triajul alertelor, calitatea datelor de la senzori | ML + procesare de semnal | 4.500 € |
| 5 | **Responsabil calitate și reglementare (PRRC)** | 1,0 | Sistemul ISO 13485, dosarul tehnic MDR, GDPR, AI Act, relația cu organismul notificat | 5+ ani în dispozitive medicale | 4.000 € |
| 6 | **Manager de proiect** | 1,0 (din luna 1) sau 0,5 + 0,5 coordonator pilot | Implementare, achiziții, cereri de rambursare, raportări, coordonarea pilotului și a dispozitivelor | 5+ ani, ≥2 proiecte UE implementate | 3.500 € |
| **Total** | | **6 ENI** | | | **~24.500 €/lună** |

**De la parteneri (nu sunt angajații tăi):**
- medic coordonator (cardiolog);
- asistente și medici pentru centrul de monitorizare;
- echipa de studiu clinic;
- cercetători universitari pentru cercetarea contractată;
- fabrica de electronice pentru asamblarea hubului;
- laboratorul de teste pentru compatibilitate electromagnetică și siguranță.

## 3. Ce construiește proiectul

1. **Platforma PREVENT-NV:**
   - dosarul longitudinal al pacientului (FHIR/IPS, compatibil EHDS);
   - integrarea senzorilor certificați (tensiometre, ECG, brățări);
   - extragerea datelor din PDF-uri medicale (RO/HU).
2. **Profilul de risc:** risc cardiovascular și de AVC, din dosar + date continue (SCORE2/CHA2DS2-VASc + modele ML calibrate local).
3. **Motorul de alerte și triaj** + **predicția „pe cine suni primul”**.
4. **Centrul de monitorizare** (la partenerul clinic sau într-un spațiu propriu), cu tabloul de bord și protocol de escaladare. Modelul e TIM-HF2.
5. **Hubul de casă PREVENT-NV:** adună datele de la senzorii certificați și le trimite securizat. Se asamblează în Bihor.
6. **Modulul software certificat MDR**, clasa IIa: profilul de risc + alertele.

## 4. Pachetele de lucru

| WP | Ce | Responsabil | Luni | Tip ajutor |
|---|---|---|---|---|
| WP0 | Management, achiziții, raportări, vizibilitate | Manager de proiect | 1–30 | de minimis |
| WP1 | Platforma și dosarul FHIR/EHDS, integrarea dispozitivelor | Tu + dezvoltator | 1–18 | dezvoltare experimentală |
| WP2 | Extragerea datelor din documente medicale RO/HU | Tu + cercetător 1 | 3–15 | cercetare industrială |
| WP3 | Modele de risc din date combinate + calibrare pe populația din România | Cercetător 1 + universitate | 3–24 | cercetare industrială |
| WP4 | Detectarea fibrilației, predicția agravării, triajul alertelor | Cercetător 2 | 4–24 | cercetare industrială |
| WP5 | „Pe cine suni primul” (comparat cu reminder pentru toți) | Cercetător 1 + clinic | 12–27 | cercetare industrială |
| WP6 | Hubul de casă: specificație, prototip, teste CE, serie mică | Tu + fabrică + laborator | 4–20 | investiție (art. 14) |
| WP7 | Centrul de monitorizare și studiul pilot (≥200–300 pacienți) | Partener clinic + manager | 12–30 | dezvoltare experimentală |
| WP8 | Sistemul de calitate ISO 13485 + dosarul MDR + certificare | Responsabil calitate | 1–30 | art. 28 + dezvoltare experimentală |

## 5. Calendar (implementarea se termină obligatoriu la 31.12.2029)

| Perioadă | Ce se întâmplă |
|---|---|
| **Acum → depunere** | Prototip făcut de tine cu AI. Partener clinic și de cercetare. E-mail la ADR NV. Raport CTT, raport expert contabil, scrisori de intenție, oferte. |
| **Contractare** | Pentru 961: contract realist în T2–T3 2027. Pentru o fereastră ulterioară, totul se decalează. |
| **Lunile 1–6** | Angajări. Sistemul de calitate pornit. Platforma v1. Contracte cu producătorii de dispozitive. Aviz de etică. Cererea de prefinanțare. |
| **Lunile 7–12** | Modelele de risc v1. Prototipul hubului. Centrul de monitorizare amenajat. Primul organism notificat contactat. |
| **Lunile 13–20** | Pilotul începe (primii pacienți). Seria mică de huburi. Testele CE pentru hub. Dosarul tehnic MDR. |
| **Lunile 21–27** | Rezultatele pilotului. „Pe cine suni primul” testat. Auditul organismului notificat. |
| **Lunile 28–30** | Certificarea (țintă), raportul final, primii clienți plătitori, cererea finală de rambursare. |
| **2030–2032** | Durabilitate: 6 locuri de muncă menținute, venituri din abonamente, raport anual. |

**Risc de calendar:** certificarea MDR poate depăși termenul. Pornește-o din luna 1. Planul B: pilot cu marcajul de cercetare (investigație clinică), iar certificarea se termină din venituri după proiect.

## 6. Bugetul (estimare, de refăcut cu oferte)

| Linie | Ce include | Eligibil | Intensitate | Grant | Cofinanțare |
|---|---|---:|---:|---:|---:|
| **Cercetare industrială (art. 25)** | Salarii: cercetători + tu, pe WP2–WP5 (~60% din timp); cercetare contractată cu universitatea (~350k); calcul și date | 1.400.000 | 80% | 1.120.000 | 280.000 |
| **Dezvoltare experimentală (art. 25)** | Salarii pe WP1, WP7, WP8 (dezvoltator, calitate, parte din tine); studiul pilot la partenerul clinic (~400k); dispozitive pentru pilot (~150k) | 950.000 | 60% | 570.000 | 380.000 |
| **Investiție (art. 14)** | Centru de date securizat (~1,4 mil.); centrul de monitorizare (~0,8 mil.); linia de asamblare și testare a hubului + matrițe + stoc inițial (~1,0 mil.); licențe și know-how (algoritm certificat pentru fibrilație, terminologii, ~0,9 mil.); dispozitive pentru extindere (~0,5 mil.) | 4.600.000 | ~65% (de verificat) | ~3.000.000 | ~1.600.000 |
| **Inovare (art. 28)** | Consultanță MDR și organismul notificat, studiu de piață, protecția mărcii / IP | 220.000 | 100% | 220.000 | 0 |
| **De minimis** | Consultanță la scriere și implementare; publicitate (max. 15.000 lei) | 300.000 | 100% | 300.000 | 0 |
| **Total** | | **~7.470.000** | | **~5.210.000** | **~2.260.000** |

- Salariile celor 6 pe 30 de luni ≈ 735.000 EUR. Sunt împărțite între cele două linii de cercetare, cu pontaj pe pachete de lucru.
- TVA-ul se plătește separat și se recuperează (neeligibil dacă e deductibil).
- Grantul rămâne între 5 și 7 mil. EUR, deci se aplică pragul „> 4 locuri de muncă”. Avem 6.
- Partea de investiție e cea mai incertă: trebuie confirmat în scris de ADR NV că centrul de date, centrul de monitorizare, linia hubului și licențele sunt acceptate ca „investiție inițială”.

## 7. Indicatorii pe care îi promiți (conservator)

| Indicator | Țintă |
|---|---|
| Întreprinderi sprijinite (RCO01/02, STEP RCO125) | 1 |
| Locuri de muncă create (RCR01) | **6 ENI**, menținute 3 ani |
| Produs nou introdus pe piață | Platforma + modulul certificat + hubul |
| Venituri din activitatea sprijinită, primii 3 ani de durabilitate [ESTIMARE, de setat conservator] | Anul 1: ~150.000 EUR; anul 2: ~350.000 EUR; anul 3: ~600.000 EUR. Sursele: abonament per pacient pentru clinici, asigurători, angajatori + huburi vândute |
| Pacienți monitorizați în pilot | ≥200–300 |
| Spillover | Profil FHIR românesc publicat + benchmark deschis de documente medicale RO/HU |

**Regulă:** setează veniturile la ce poți atinge sigur. Neîndeplinirea aduce recuperare proporțională.

## 8. Cum faci bani după proiect (pentru planul de afaceri)

- **Abonament per pacient monitorizat:** 15–40 EUR/lună [ESTIMARE], plătit de clinici private, asigurători sau angajatori (pachete de prevenție). Hubul e inclus sau vândut.
- **Licență pentru platformă:** pentru clinici, laboratoare și cabinete de medicina muncii (profilul de risc + rechemare).
- **Servicii de date și AI:** pentru alte proiecte (de exemplu, ca furnizor pe linia de inovare pentru alți beneficiari STEP).
- **Extindere:** Ungaria și restul CEE (scrisori de intenție pentru criteriul 4.3).

## 9. Partenerii și ce semnezi cu ei

| Partener | Ce aduce | Document |
|---|---|---|
| Spital sau clinică de cardiologie (NV) | Pacienții din pilot, centrul de monitorizare, medicul coordonator, studiul | Acord de parteneriat / contract de servicii + acord de date + protocol de studiu |
| Universitate (UO, UMF Cluj, UTCN) | Cercetare contractată, raportul CTT / CS I | Contract de cercetare + raportul |
| Producători de dispozitive (2–3) | Senzori certificați + acces la date (API/SDK) | Ofertă + contract de livrare + DPA (prelucrarea datelor) |
| Fabrică de electronice (Oradea) | Asamblarea hubului | Ofertă + contract de producție |
| Laborator acreditat | Teste de compatibilitate electromagnetică, siguranță, radio | Ofertă |
| Organism notificat | Certificarea MDR | Ofertă / acord de evaluare |
| Consultant | Scrierea dosarului + implementarea | Contract (fără conflict de interese cu furnizorii) |
| Clienți viitori (clinici, asigurători, angajatori, 1–2 din UE) | Dovada pieței | Scrisori de intenție |

## 10. Dosarul de depunere: checklist

- [ ] Firma solicitant:
  - sediu în Nord-Vest;
  - an fiscal închis cu profit din exploatare > 0;
  - ≥1 salariat mediu;
  - fără excludere;
  - drept de folosință asupra spațiului.
- [ ] Dovada capacității de cofinanțare (~2,3 mil. EUR + TVA + rezervă de cash).
- [ ] Cererea de finanțare în MySMIS2021+ (cont, semnătură electronică calificată).
- [ ] Planul de afaceri, cu indicatorii de mai sus.
- [ ] Studiul de piață.
- [ ] Macheta financiară (Anexa III.5, versiunea corectată).
- [ ] Raportul CTT sau al unui cercetător științific gradul I (inovație, TRL, încadrarea STEP).
- [ ] Raportul expertului contabil CECCAR.
- [ ] CV-uri și dovezi de experiență (inclusiv cele 2 proiecte UE).
- [ ] Scrisori de intenție (NV + internaționale).
- [ ] Câte 3 oferte de preț per echipament / serviciu + centralizatorul de costuri.
- [ ] Deviz general HG 907/2016, dacă amenajezi spații.
- [ ] Declarația Unică (Anexa III.1, versiunea nouă) + declarațiile de ajutor de stat / de minimis.
- [ ] Autoevaluare **conservatoare**: punctajul evaluatorilor nu trebuie să scadă cu mai mult de câteva puncte față de el.

## 11. Ce faci în următoarele 4 săptămâni

1. **E-mail la regio@nord-vest.ro cu 4 întrebări:**
   - Proiectul se încadrează la „tehnologii digitale critice”?
   - Centrul de date, centrul de monitorizare, linia hubului și licențele sunt investiție inițială pe art. 14?
   - Certificarea MDR e eligibilă?
   - Există o fereastră STEP după 961?
2. **Consultantul:** decizie împreună. Fie 961 până pe 02.11.2026 (foarte strâns), fie următoarea fereastră.
3. **Partenerul clinic:** discuție cu un cardiolog sau spital din NV despre pilot și centrul de monitorizare.
4. **Universitatea:** cine semnează raportul CTT și cine intră în cercetarea contractată.
5. **Prototipul tău cu AI (2–3 săptămâni):**
   - un tensiometru și un ECG certificat conectate;
   - un dosar FHIR de test;
   - un profil de risc simplu;
   - un tablou de bord cu alerte.

   Îl arăți tuturor celor de mai sus.
6. **Managerul de proiect și responsabilul de calitate:** găsește-i acum. CV-urile lor intră în dosar.
7. **Ofertele:** cere de la 2–3 producători de dispozitive, de la o fabrică din Oradea și de la un organism notificat.
