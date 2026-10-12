# Evaluarea planului PREVENT-NV (v1) și ce se schimbă în v2

**Ce am evaluat:** `proiect-STEP-PREVENT-NV-plan.md` (branch `claude/trusting-planck-3jm893`, commit `745f2f4`, 12 oct. 2026), împreună cu `proiect-STEP-sanatate-predictiva.md`, `evaluare-research-STEP.md` și raportul `reports/Oportunități software în sănătatea predictivă.md`.
**Metoda (skill-urile din repo, aplicate aici):** trei lentile adversariale în stilul „bulletproof” (evaluator ETF al ADR Nord-Vest; cofinanțator/CFO; expert MDR împreună cu un clinician), fiecare obiecție cu o **probabilitate de respingere dacă rămâne nerezolvată**; apoi un control lateral (planul respectă meta-tiparele pe care repo-ul le-a găsit de patru ori?) și un control CFO pe durabilitate. Fără cercetare web nouă în afară de trei verificări (PRRC extern, termenele AI Act după Digital Omnibus, decontarea telemonitorizării de CNAS). Planul v2 e în `proiect-STEP-PREVENT-NV-plan-v2.md`.
**Data:** 12 octombrie 2026.

---

## Verdictul pe scurt

Planul v1 e **bine construit ca dosar** (criteriile sunt mapate pe roluri, bugetul e pe linii de ajutor, checklist-ul e complet) și **greșit construit ca proiect**: pune într-un singur proiect de 30 de luni și 6 oameni **patru lucruri grele** (o platformă clinică, un dispozitiv medical software clasa IIa, un produs hardware cu linie de asamblare și un centru de monitorizare 24/7 cu pilot pe 200–300 de pacienți) și alege exact direcția pe care **propriul research din repo o pune pe lista „de evitat”**: RPM cu alerte automate, modele de risc proprii, scoruri în fluxul medicului, fără plătitor în România (raport, §3 și „Răspunsuri directe” b). Cea mai bună întrebare de cercetare din plan, „pe cine suni primul” (WP5), e tratată ca anexă, deși e singura cu noutate reală și singura care se leagă de dovezile din repo (ACCESS, EAGLE, PRISMATIC, TIM-HF2).

**Ce păstrez din v1:** echipa de 6 ENI justificată pe criterii; separarea rolurilor cerută de IEC 62304; pilotul cu partener clinic; FHIR/IPS și EHDS ca schelet de date; extragerea din PDF-uri RO/HU; checklist-ul de depunere; cele patru întrebări pentru ADR NV.
**Ce schimb în v2:** un singur produs clinic (modulul de prioritizare și risc, clasa IIa, cu plan B de investigație clinică), **fără hub hardware** (cumperi dispozitive certificate), investiția pe art. 14 mutată pe **unități mobile de prevenție + centru de coordonare + mediu securizat de date** (legate de plătitorul real: angajatorul, prin medicina muncii), WP5 devine nucleul de cercetare, calendar cu porți și criterii de oprire, buget cu TVA și decalaj de rambursare, indicatori conservatori.

---

## Lentila 1: evaluatorul ETF (ADR Nord-Vest)

### O1. Patru proiecte într-unul: criteriile 5.7 și 5.4 cad
- **Probabilitate de respingere dacă rămâne: 75%**
- **Logica:** 5.7 cere activități „susținute de resurse umane, financiare și materiale suficiente”. Șase oameni, din care doi sunt manager și responsabil de calitate, trebuie să livreze platforma, patru pachete de cercetare, un hardware cu teste CE și serie mică, un centru de monitorizare și un pilot clinic. Evaluatorul nu trebuie să demonstreze că nu se poate; trebuie doar să nu fie convins că se poate. La 5.4, „costuri rezonabile” se verifică pe oferte: 1,4 mil. EUR „centru de date securizat” pentru 300 de pacienți nu trece de un evaluator care a văzut oferte de colocare.
- **Dovezi din plan:** WP1–WP8 în paralel pe 30 de luni; hub cu „matrițe și stoc inițial”; buget art. 14 de 4,6 mil. EUR cu linii rotunde.
- **Ce rezolvă:** un singur produs clinic; hardware cumpărat, nu produs; art. 14 pe active a căror valoare e evidentă (vehicule echipate, un centru amenajat, servere la dimensiunea pilotului).

### O2. Încadrarea „tehnologie critică” e fragilă pentru „AI aplicat în sănătate”
- **Probabilitate: 70%**
- **Logica:** 5.1 și 5.2 au 0 = respingere. STEP finanțează tehnologii critice, nu aplicații ale lor. „O platformă cu modele de risc” poate fi citită drept aplicație. Încadrarea la biotehnologie e slabă pentru software (planul o spune singur în `proiect-STEP-sanatate-predictiva.md`). Nota de ghidare folosită e C/2024/3209; există a doua notă, din 22.12.2025 (`evaluare-research-STEP.md`, problema 2), necitită.
- **Ce rezolvă:** raportul CTT trebuie să numească tehnologia critică, nu domeniul: **infrastructură suverană de date de sănătate conformă EHDS, învățare federată și extragere verificabilă din documente în limbi cu resurse puține (RO/HU)**; sănătatea e domeniul de aplicare. Întrebarea 1 către ADR NV se pune exact așa.

### O3. Investiția pe art. 14 e umflată ca să atingă minimul de 3 mil. EUR
- **Probabilitate: 60%**
- **Logica:** evaluatorul recunoaște un buget construit de la prag în jos. Hubul există în plan ca să existe „producție”; centrul de date e supradimensionat; „licențe și know-how 0,9 mil.” fără furnizor numit. `evaluare-research-STEP.md` (problema 3) a semnalat deja contradicția dintre „software ca activ necorporal nu merge” și „4,5 mil. pe servere”.
- **Ce rezolvă:** active cu utilitate evidentă în producția serviciului: **unități mobile de prevenție** (vehicul + ECG 12 derivații, spirometru, audiometru, analizor point-of-care, tensiometre validate; ~350–450 k EUR fiecare [ESTIMARE, de confirmat cu oferte]), **centrul de coordonare** (spațiu, stații, telefonie, sistem), **mediul securizat de date** la dimensiunea reală, **licențe numite** (algoritm certificat CE pentru fibrilație, terminologii, QMS). Confirmarea în scris de la ADR NV rămâne prima acțiune.

### O4. Directorul de proiect nu e „în domeniul proiectului”
- **Probabilitate: 50%**
- **Logica:** 2.1.a cere director cu 5 ani „în domeniul proiectului (cercetare sau operațional)”. Managerul cu experiență UE acoperă 2.1.e, nu 2.1.a. Fondatorul nu are 5 ani. Planul lasă cele 4 puncte în aer.
- **Ce rezolvă:** directorul de proiect e **responsabilul de calitate și reglementare** (5+ ani în dispozitive medicale) sau **medicul coordonator** detașat de partener, cu contract; managerul rămâne manager.

### O5. Indicatorii de venit nu au plătitor numit
- **Probabilitate: 40%**
- **Logica:** 150 / 350 / 600 k EUR în durabilitate, din „clinici, asigurători, angajatori”. Research-ul din repo spune: CNAS nu plătește telemonitorizare și nici aplicații; rețelele mari își fac IT-ul în casă; asigurările private sunt mici (756 mil. lei prime brute în S1 2026); plătitorul accesibil e **angajatorul** (raport, §5). Căutarea de azi nu a găsit nicio decontare CNAS pentru telemonitorizare în 2026 [căutare 12.10.2026, absență].
- **Ce rezolvă:** plătitor principal angajatorul, prin cabinetele de medicina muncii și pachetele de prevenție la locul de muncă; venituri în durabilitate setate la ce acoperă salariile menținute; asigurătorii și clinicile ca al doilea val.

## Lentila 2: cofinanțatorul / CFO

### O6. Nevoia reală de numerar e dublă față de cofinanțare
- **Probabilitate: 65%**
- **Logica:** cofinanțarea de 2,26 mil. EUR e doar o parte. TVA pe cheltuielile eligibile (~19% din 7,5 mil. ≈ 1,4 mil. EUR) se plătește furnizorilor și se recuperează cu întârziere. Rambursările vin la 3–6 luni după plată. Prefinanțarea de până la 40% cere garanție bancară, deci garanții reale. Vârful de numerar poate ajunge la **3,5–4,5 mil. EUR** [ESTIMARE]. Planul nu are un tabel de flux de numerar pe trimestre.
- **Ce rezolvă:** flux de numerar trimestrial în planul de afaceri; linie de credit pentru TVA; etapizarea achizițiilor mari (unitățile mobile în două valuri); prefinanțare cerută din luna 1.

### O7. Modelul de afaceri contrazice research-ul propriu
- **Probabilitate: 55%**
- **Logica:** `reports/Oportunități software în sănătatea predictivă.md`, „Răspunsuri directe” b: „Evită: RPM-ul cu alerte automate (IIa/IIb, nicio rambursare în România); un model predictiv propriu; calculatoarele SCORE2 în fluxul medicului.” Planul v1 face toate trei. Un cofinanțator care citește repo-ul întreabă de ce finanțează ceea ce fondatorul însuși a scris că trebuie evitat.
- **Ce rezolvă:** proiectul STEP e exact instrumentul care face „evitabilul” finanțabil (grant pentru certificare, partener clinic, bani pentru dovezi), **dar numai dacă nucleul rămâne ce research-ul a găsit valoros**: bucla închisă, măsurarea, capacitatea, interoperabilitatea. Predicția intră ca un singur modul clinic, nu ca identitate.

### O8. Hardware-ul e capcana cunoscută
- **Probabilitate: 45%**
- **Logica:** raportul §4.4: Forward a închis după 400+ mil. USD, lecția „nu construi hardware și nici clinici”. Hubul cere design, EMC/radio, serie mică, stoc, suport, înlocuiri; dispozitive certificate cu API există deja. În plus, criteriul 5.5 cere ca dotările să fie „necesare” și justificate.
- **Ce rezolvă:** hubul iese. Datele vin din dispozitive certificate cu SDK/API și din aplicația de telefon a pacientului; unde nu există telefon, un gateway cumpărat.

## Lentila 3: expertul MDR și clinicianul

### O9. Certificarea clasa IIa în 30 de luni, de la zero, cu model nou de ML, e optimistă
- **Probabilitate: 60%**
- **Logica:** QMS ISO 13485 de la zero (6–12 luni), IEC 62304, ISO 14971, evaluare clinică; un model de risc **nou** cere dovezi clinice proprii, nu doar literatură; organismele notificate au cozi; AI-ul din dispozitive clasa IIa+ devine „risc ridicat” din 2.08.2028 după Digital Omnibus (Reg. (UE) 2026/1744, JO 24.07.2026 ([Pure Global](https://www.pureglobal.com/news/eu-ai-act-omnibus-high-risk-dates-2028)) [sursă secundară, de verificat pe EUR-Lex]), deci dosarul tehnic se evaluează pe ambele cadre. Estimarea din repo (32–110 k EUR, 9–18 luni) e **fără investigații clinice**.
- **Ce rezolvă:** modulul certificat folosește **scoruri validate (SCORE2, CHA2DS2-VASc) cu calibrare locală și prioritizare**, nu un model fundamental nou; modelele ML noi rămân în cercetare (WP) și intră în dispozitiv doar după dovezi. Pilotul rulează ca **investigație clinică** (MDR art. 62) sau cu produsul în regim de cercetare, iar certificarea are plan B explicit: finalizare în durabilitate, din venituri și art. 28. PRRC poate fi extern pentru microîntreprinderi și întreprinderi mici (MDR art. 15(2)) ([Freyr](https://www.freyrsolutions.com/who-is-a-prrc)) [VERIFICAT, sursă secundară], deci rolul nu cere neapărat un angajat dedicat.

### O10. Datele pentru „calibrarea pe populația din România” nu există la îndemână
- **Probabilitate: 55%**
- **Logica:** raportul §5: niciun vendor românesc de software clinic nu are API public; e-SănătateaMea și SIUI nu dau date terților; spitalele au dosare „închise”. Un model calibrat cere mii de pacienți cu rezultate la 1–3 ani. Legea 190/2018 art. 3 cere consimțământ explicit sau temei legal expres pentru profilare pe date de sănătate. Planul spune „profil de risc din dosarul medical” fără a numi sursa.
- **Ce rezolvă:** sursele de date se numesc în dosar: exporturile partenerului clinic (CSV/PDF), fișele de medicina muncii ale cabinetelor partenere, laboratorul partener, dispozitivele din pilot; temei: art. 9(2)(j) GDPR cu partener academic și comisie de etică pentru cercetare, consimțământ explicit în pilot, DPIA; nicio promisiune de acces la date naționale.

### O11. Centrul de monitorizare 24/7 nu are cine să-l plătească după proiect
- **Probabilitate: 40%**
- **Logica:** TIM-HF2 a funcționat cu medic și asistentă 24/7; Tele-HF și BEAT-HF fără răspuns clinic puternic nu au avut efect (raport §2). Dar personalul centrului e cost operațional permanent, iar în durabilitate nu e grant. Oboseala de alerte și „nimeni nu deține alerta” sunt două din cele șase puncte unde se pierde beneficiul.
- **Ce rezolvă:** centrul e **centru de coordonare în orar de lucru**, operat de partenerul clinic sub contract, cu protocol de escaladare spre 112 în afara orelor; alertele trec prin triaj cu proprietar numit și termen; dimensiunea se decide din pilot.

## Controlul lateral: respectă planul ce a găsit repo-ul?

| Meta-tipar din repo (găsit independent de 3–4 tehnici) | v1 | v2 |
|---|---|---|
| Valoarea rară e **proprietarul plătit al buclei deschise**, nu predicția | predicția e identitatea proiectului | bucla închisă e identitatea; predicția e un modul |
| **Nu deține și nu opera** ce poate fi al altcuiva | hub propriu, centru 24/7 propriu | dispozitive cumpărate; centrul operat de partener |
| **Banii expuși lângă un risc** se vând altfel decât remindere | plătitorul nevăzut | angajatorul plătește prevenția și pierde bani la absenteism și la amenzi MM |
| **Mută încrederea pe cine o are deja** | fondatorul e lider tehnic, partenerii sunt listați | partenerul clinic și universitatea sunt în guvernanță, directorul e din domeniu |
| Cinci din șase puncte unde se pierde beneficiul sunt **probleme de software și operațiuni** (raport §2) | planul construiește modelul | planul construiește stratul care duce semnalul la acțiune și îl măsoară |

## Controlul CFO pe durabilitate (3 ani după proiect)

| | v1 | v2 |
|---|---|---|
| Salarii menținute (RCR01, 6 ENI) | ~24.500 EUR/lună → ~880 k EUR / 3 ani | la fel, dar 2 posturi pot trece la partener/contract în durabilitate (de verificat dacă e permis fără pierderea indicatorului) |
| Venituri promise | 150 / 350 / 600 k EUR = 1,1 mil. | plătitor numit (angajatori prin MM, 80–110 lei/angajat/an pe examen; pachet de prevenție 25–60 lei/angajat/lună [ESTIMARE]); ținta setată la ce acoperă salariile: 250 / 400 / 550 k EUR, cu scenariu pesimist scris |
| Costuri operaționale centru + flotă | nebugetate | combustibil, întreținere, personal medical contractat, hosting: ~120–180 k EUR/an [ESTIMARE] |
| Concluzie | durabilitatea nu se închide fără finanțare nouă | se închide la ~35–45 de angajatori cu 300+ salariați sau echivalent; e un număr care se poate verifica în Bihor (187,3 k salariați, INS) |

## Ce se schimbă în v2, pe scurt

1. **Un singur produs clinic**, clasa IIa, bazat pe scoruri validate + prioritizare; modelele noi rămân în cercetare până au dovezi.
2. **Fără hardware propriu.** Dispozitive certificate cu API, cumpărate pentru pilot și pentru unitățile mobile.
3. **Investiția art. 14** pe unități mobile de prevenție, centru de coordonare și mediu securizat de date, la dimensiuni justificabile cu oferte.
4. **WP „pe cine suni primul” devine nucleul**, cu design de studiu controlat (randomizare pe angajatori sau în trepte), partener academic și comisie de etică.
5. **Plătitor numit:** angajatorul, prin cabinetele de medicina muncii și pachetul de prevenție la locul de muncă; clinici și asigurători în valul 2; Ungaria pentru 4.3.
6. **Director de proiect din domeniu**; fondatorul e arhitect și lider tehnic; PRRC poate fi extern.
7. **Porți și criterii de oprire** la lunile 6, 12, 18, 24; plan B pentru certificare.
8. **Flux de numerar** cu TVA și decalaj de rambursare; achiziții în două valuri.
9. **Indicatori conservatori**, cu scenariu pesimist scris în planul de afaceri.
10. **Întrebările pentru ADR NV și GAL/OJFIR** (încadrare, art. 14, MDR eligibil, fereastră viitoare, cumul de minimis cu DR-36) înainte de orice buget detaliat.

Cifrele din acest document sunt estimări sau provin din notele de research (rezumate de căutare, surse secundare), nu din ghidul consolidat. Totul ce ține de apel se reverifică pe GS 961 după Corrigendum nr. 2.
