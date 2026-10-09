# Analiza founder: ce oportunitate software din sănătatea preventivă merită construită întâi

**Data:** 9 octombrie 2026
**Statut:** analiză comercială peste notele de cercetare din acest dosar, cu uneltele din pachetul `founder-skill` (board, competitors, consumer, pricing, cfo, offer, plan). **Nu am făcut cercetare web nouă.** Fiecare fapt trimite la o notă (fișier § secțiune ← sursa citată acolo). Tot ce e calcul sau judecată proprie e marcat **„estimare”** sau **„calculul meu”**.
**Artefacte:** `/home/user/Research/founder-sanatate/` (scoring, board, panels, pricing, cfo, plan).

---

## 0. Cum să citești documentul

**Fondatorul.** SRL în Bihor (Oradea), rețele în Oradea și București. Python, SQL, PL/SQL, Oracle APEX, backend, arhitectură de date, AI/ML, API-uri LLM, agenți, n8n. ~25.000 EUR, 10–12 ore pe săptămână la început. Poate merge fizic la clienți. Preferă B2B SaaS cu venit recurent. Acces inițial limitat la medici, dosare și seturi de date; deschis la parteneriate. Vrea un prim produs îngust care aduce **1.000–3.000 EUR MRR** înainte de a avea nevoie de echipă și care poate crește credibil spre sănătate preventivă/predictivă **fără** un model medical propriu de validat.

**Abrevieri pentru citări** (toate fișierele sunt în acest dosar):

| Abreviere | Fișier |
|---|---|
| LAT | `analiza_laterala.md` |
| RO | `romania_piata.md` |
| RSMM | `romania_software_medicina_muncii.md` |
| FUR | `follow_up_recall_dovezi.md` |
| REG | `reglementare_ue_ro.md` |
| B2B | `competitori_b2b_infrastructura.md` |
| EMG | `emergente_si_platitori.md` |
| ȘTI | `stiinta_predictie_preventie.md` |
| MON | `monitorizare_date_coordonare.md` |
| CONS | `competitori_consumer.md` |
| CEE | `cee_nordice.md` |

**Limita surselor (moștenită).** Notele spun singure că aproape toate faptele vin din rezumate ale motorului de căutare, nu din pagini citite integral (RO, metoda; RSMM, metoda; FUR, „Source access”). Prețurile românești de software sunt puține și vechi. Niciun cumpărător real nu a fost întrebat. Panelurile de cumpărători și board-ul de mai jos sunt **simulate** (vezi §C0); ele aleg ce să testezi, nu dovedesc cererea.

**Ordinea sarcinilor:** A (scorare) → B (fișele top 10) → C (board, concurență, preț, panel) → D (CFO) → E (verdict).

---

## Pe scurt

- **Primul produs recomandat: A · „Scadențar MM”.** Un add-on pentru **cabinetele independente de medicina muncii** care:
  - ține scadențele fișelor de aptitudine din exportul programului MM existent;
  - trimite remindere în locul asistentei;
  - dă fiecărui angajator-client un portal cu marca cabinetului (status, fără diagnostice).
  - **Preț:** 39 / 79 / 149 €/lună, plus SMS la cost.
  - Răspunde direct la portalul angajatorilor de la MedLife (RSMM §1), pe un serviciu obligatoriu, plătit de angajator și recurent (RSMM §3). E software administrativ, deci nu e dispozitiv medical (REG §8).
- **De ce A:**
  - **Scorare:** locul 1 din 29 (73,4/100), locul 1–2 la toate cele 4 seturi de ponderi.
  - **Board:** singura idee pusă în primele două de toate trei lentilele (3 × FUND IF).
  - **Panel:** cea mai mare rată simulată, 35% (limită superioară).
  - **Bani:** cel mai mic numerar necesar (~3,8k €) și primul an pe plus (+534 €). Verdictul calculat e „Profitable”, **dar fragil**.
- **Plafonul, spus direct:**
  - 1.000 € MRR vine în **~luna 18**;
  - **3.000 € MRR nu vine la 10–12 h/săpt** (plafon ~1.600 €);
  - pentru 3.000 € e nevoie de ~20 h/săpt din anul 2 (~luna 31, ~50 de cabinete) sau de un canal (un vendor de program MM care revinde).
  - **Timpul fondatorului, nu capitalul, e constrângerea.**
- **Locul 2: G · „Controale pierdute”** la clinicile independente de boli cronice, **condiționat**.
  - E cea mai bună strategic și e preferata board-ului (media 6,0).
  - Dar panelul a respins-o: **0/20 la prima ofertă, 2/20 după refacere**, pe încredere și integrare. Anul 1 e pe pierdere.
  - Se deschide doar după 2 clienți A ca referință și 2 audituri cu ≥30 de controale depășite fiecare.
- **B** (scadențarul vândut direct HR-ului) nu e un produs separat: 10% în panel, 2 PASS în board. Devine partea de angajator a lui A.
- **De evitat:**
  - H (rechemarea CNAS), K (turism dentar), E (FIT/ROCCAS ca prim produs);
  - orice scor de risc individual, RPM cu alerte sau model propriu (MDR IIa);
  - predicția ML ca prim produs; EHDS ca prim produs;
  - reminderele generice; orice B2C.
  - Lista completă e în §E4.
- **Validarea de 90 de zile:**
  - **GO** dacă există ≥3 pre-vânzări plătite până în ziua 60, ≥2 exporturi funcționale și confirmarea că programele MM n-au deja portal pentru angajator;
  - **NO-GO** dacă după ≥15 conversații există <2 pre-vânzări, sau dacă ≥2 programe MM au deja portalul (§E6).
- **Onestitate:** board-ul și panelul sunt **simulate**: sub-agenți separați, niciun om real întrebat. Prețurile, rampele și costurile sunt **estimări**. Faptele vin din note care, la rândul lor, se sprijină mai ales pe rezumate de căutare.

---

## A. Scorarea ponderată

### A1. Ce am verificat la reluare și ce am schimbat

Rularea anterioară lăsase un script de scorare (`scoring/scoring.py`) cu 22 de oportunități. L-am verificat față de cerință și față de note:

- **Criteriile:** toate cele 17 cerute sunt prezente (tabelul A2). Ponderile însumează 100. ✔
- **Scara:** 1–5, mereu orientată „5 = bine pentru fondator” (la criteriile negative, 5 = puțin/ușor). Scorul = Σ(pondere × notă) / 5, deci 20–100. ✔
- **Flagul de dependență fatală:** prezent, cu motiv scris pentru fiecare. ✔
- **Acoperirea:** 22 de rânduri ≥ 15 cerute. ✔ Am **adăugat 7 rânduri** (O6, O13, O18, O20, O22, O23, O26), ca tabelul să acopere toate cele 26 de oportunități din LAT §E, plus 4 variante noi (B, G, L, V). Singura neevaluată e **O24** (auditul „bani expuși”): e unealtă de vânzare, nu afacere (LAT §E, O24), și o folosesc ca atare în §B.
- **Notele:** am recitit sursele pentru fiecare dintre primele 10 și n-am găsit note care să contrazică notele de cercetare. Rândurile adăugate **nu schimbă top 10** (cea mai bună dintre ele, O18, iese pe locul 11).
- Am adăugat coloana „Origine” în tabel, ca fiecare rând să poată fi urmărit înapoi în LAT.

### A2. Criteriile și ponderile

Ponderile reflectă obiectivul declarat: **bani recurenți repede, cu 10–12 ore pe săptămână**, și abia apoi drumul strategic. De aceea „cine plătește”, „cât de urgent” și „cât costă să ajungi la client” cântăresc cel mai mult.

| Cod | Criteriu (5 = favorabil) | Pondere | De ce această pondere |
|---|---|---:|---|
| U | Urgența reală la client | 10 | Fără o durere urgentă, clientul nu cumpără în 90 de zile, iar ținta e 1.000–3.000 EUR MRR. |
| P | Capacitatea și disponibilitatea de plată | 10 | România are cea mai mică cheltuială de sănătate pe locuitor din UE, iar partea privată e aproape toată din buzunar (RO §5 ← State of Health in the EU 2025). Fundăturile din LAT au toate același motiv: cer un plătitor nou (LAT §F1, punctul 5). |
| A | Achiziția clienților (5 = ușoară) | 10 | Distribuția e jumătate din afacere (lentila „Monopol”, `founder-board/lenses.md`). La 10–12 ore pe săptămână, un canal scump omoară produsul. |
| D | Accesul la datele necesare | 8 | Cel mai frecvent ucigaș în sănătate. Fondatorul poate lucra doar ca persoană împuternicită (REG §1), iar programele românești de clinică n-au API public (RSMM §1). |
| V | Potențialul de venit recurent | 8 | Preferința explicită a fondatorului (B2B SaaS). |
| ST | Relevanța strategică pentru sănătatea predictivă | 8 | Al doilea obiectiv al fondatorului. Contează, dar după „bani acum”. |
| RO | Oportunitatea în România / Bihor | 6 | Primii clienți trebuie să fie la o distanță de mers cu mașina. |
| R | Complexitatea de reglementare (5 = mică) | 6 | Clasa IIa costă ~32–110k EUR și 9–18 luni (REG §2, estimare de pe blogul unui furnizor), deci peste buget. Cazurile extreme le prinde și flagul. |
| S | Fezabil ca dezvoltator solo | 6 | Fondatorul e singur, cu timp limitat. |
| DF | Forța diferențierii | 6 | Fără diferențiere, concurezi pe preț cu produse incluse gratuit în programele de cabinet (FUR §4). |
| C | Concurența existentă (5 = puțină) | 5 | Contează, dar o piață goală poate însemna lipsă de cerere, nu ocazie (RO §7, Inferences: „gap ≠ demand”). |
| CL | Nevoia de parteneriate clinice (5 = deloc) | 4 | Fondatorul are acces limitat la medici; un partener clinic obligatoriu încetinește tot. |
| M | Efortul pentru MVP (5 = mic) | 4 | MVP-ul trebuie să încapă în ~2–3 luni la 10–12 h/săpt. |
| PT | Dependența de platforme terțe (5 = mică) | 3 | Exporturile din programele de cabinet și WhatsApp sunt riscuri reale, dar ocolibile (CSV, SMS, e-mail). |
| INT | Potențialul internațional | 2 | O întrebare de anul 3+; primul produs trebuie să meargă în România. |
| T | Dificultatea tehnică (5 = ușor) | 2 | Fondatorul e puternic tehnic; la software administrativ, tehnica rar e factorul limitativ. |
| K | Capitalul de pornire (5 = mic) | 2 | 25k EUR ajung pentru un MVP administrativ. Capitalul devine limitativ doar la MDR, iar asta e prins deja de R și de flag. |
| | **Total** | **100** | |

**Notele 1–5 sunt estimările mele**, sprijinite pe note. Justificarea notelor-cheie pentru primele 10 e în §B (rubricile „dovezi” și „de ce ar eșua”).

### A3. Flagul de dependență fatală

- **⛔ (X) fatal ca prim produs**, exclus din top 10 oricât de mare ar fi scorul, când există cel puțin una dintre:
  - **D**: datele nu sunt accesibile fondatorului;
  - **V**: e nevoie de validare sau certificare (MDR IIa+) inaccesibilă ca bani și timp;
  - **P**: nu există plătitor;
  - **I**: depinde de o integrare/API care nu există;
  - **C**: un singur cumpărător sau un canal blocat de un singur actor.
- **⚠ (W) avertisment**: o condiție care trebuie verificată în validarea de 90 de zile. Dacă testul iese negativ, avertismentul devine fatal.
- **— nimic** de semnalat dincolo de riscurile comerciale obișnuite.

### A4. Tabelul complet

Fișiere: `founder-sanatate/scoring/scoring_table.md`, `scoring.csv` (toate coloanele, plus scorurile alternative), `weights.json`. Se regenerează cu `python3 -I scoring.py`.

| Loc | Cod | Origine | Oportunitate | U | P | C | RO | INT | T | D | R | CL | S | M | K | V | A | DF | PT | ST | **Scor /100** | Flag | Motivul flagului |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| | | | **Pondere** | 10 | 10 | 5 | 6 | 2 | 2 | 8 | 6 | 4 | 6 | 4 | 2 | 8 | 10 | 6 | 3 | 8 | 100 | | |
| 1 | A | O2 + RSMM §3 | Scadențar MM + portal angajator + registrul recomandărilor (cabinete MM independente) | 3 | 3 | 3 | 4 | 2 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 3 | 4 | 4 | **73.4** | ⚠ | P/D: plata cabinetelor și exportul din softul MM existent sunt neverificate |
| 2 | G | nouă (FUR §2-3, RSMM §5) | Bucle deschise în clinici independente de boli cronice: control scadent, rezultat anormal fără programare, trimitere neînchisă | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 4 | **68.4** | ⚠ | D: export din PMS fără API; consimțământ pentru SMS (Legea 506/2004) |
| 3 | B | variantă nouă (RSMM §3) | Scadențar MM vândut direct angajatorilor (HR), indiferent de furnizor | 3 | 2 | 3 | 3 | 2 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 2 | 2 | 5 | 2 | **67.2** | ⚠ | P: plata HR-ului nedovedită; substitut gratuit (Excel) |
| 4 | K | O7 (L4) | Urmărirea pacienților de turism dentar (Oradea) | 3 | 3 | 2 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 | **64.6** | ⚠ | volum: turismul dentar din Bihor necunoscut |
| 5 | H | O8 | Rechemarea pentru pachetul CNAS de prevenție 40+/60+ (medici de familie) | 2 | 2 | 3 | 4 | 2 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 4 | 2 | 3 | 3 | 4 | **63.2** | ⚠ | P: cât plătește CNAS per serviciu de prevenție lipsește din note; dacă e ~0, devine fatal |
| 6 | J | O4 | Navigator după notificarea de la ceas (clinici de cardiologie) | 2 | 3 | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 2 | 3 | 3 | 4 | 4 | **63.2** | ⚠ | volum: penetrarea wearable-urilor în România necunoscută |
| 7 | Q | O15 | Componente EHDS (fațadă FHIR, IPS, jurnalizare) pentru vendori locali | 2 | 3 | 3 | 3 | 4 | 2 | 5 | 3 | 5 | 3 | 2 | 4 | 3 | 2 | 4 | 3 | 4 | **63.2** | ⚠ | timp: venit realist abia 2027-2028; reguli românești de aplicare lipsă |
| 8 | L | nouă (EMG §L, FUR §3) | Remindere și reducerea absențelor, cu grup de control (clinici private, stomatologie) | 3 | 3 | 1 | 3 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 2 | **62.8** | — | — |
| 9 | R | O16 | Jurnal de acces și cereri de acces la dosar (clinici private) | 2 | 2 | 3 | 3 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 5 | 4 | 2 | 3 | 3 | 2 | **60.0** | — | — |
| 10 | D | O17 + CONS KQ3 | Arhiva longitudinală de expunere profesională (+ structurarea PDF-urilor de audiometrie/spirometrie) | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 2 | 4 | 4 | 5 | **59.8** | ⚠ | piață: numărul lucrătorilor expuși din Bihor necunoscut |
| 11 | Z | O18 | Dispecerat de capacitate pentru campanii de invitații (endoscopie, imagistică), ca produs separat | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | **59.2** | ⚠ | volum: campaniile sunt rare; merge mai bine ca modul (în E sau G) |
| 12 | C | O9 | Ziua de prevenție la locul de muncă (treapta 2 a lui A) | 2 | 3 | 3 | 3 | 2 | 4 | 3 | 4 | 2 | 2 | 3 | 4 | 2 | 3 | 4 | 3 | 4 | **58.8** | ⚠ | P + parteneri: apetitul angajatorilor neverificat; laborator partener necesar |
| 13 | M | O10 | Raport de finalizare a prevenției pentru abonamente corporate (clinici medii) | 2 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 4 | 2 | 3 | 4 | 3 | **58.8** | ⚠ | P: cererea angajatorilor pentru analiză nu a fost găsită |
| 14 | F | O3 | Inbox de urmărire a rezultatelor în afara intervalului (laboratoare independente) | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 4 | 2 | 3 | 3 | 5 | **58.4** | ⚠ | D: un singur laborator independent găsit în Bihor; LIS necunoscut |
| 15 | S | O21 | PDF-uri vechi -> tabel de valori pentru medic (check-up) | 2 | 2 | 3 | 3 | 3 | 3 | 4 | 2 | 3 | 4 | 4 | 5 | 3 | 2 | 2 | 3 | 4 | **57.6** | ⚠ | răspundere: erorile de extracție intră sub PLD din 9.12.2026 |
| excl. | E | O1 (+O18) | Navigator FIT pozitiv -> colonoscopie pentru ROCCAS 4 NV, cu dispecerat de capacitate | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 4 | 1 | 3 | 3 | 4 | 2 | 1 | 4 | 2 | 5 | **57.0** | ⛔ | C/D: un singur cumpărător, achiziții UE; date doar prin contract cu consorțiul |
| 16 | AB | O22 | Jurnal de evenimente și escaladare pentru cămine și îngrijire la domiciliu | 2 | 1 | 3 | 2 | 2 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 2 | 2 | 4 | 2 | **57.0** | ⚠ | piață: căminele din Bihor neverificate; bugete mici, piață fragmentată |
| 17 | N | O11 | Meniu fix de prevenție bazată pe dovezi în bugetul de 400 EUR | 2 | 3 | 2 | 3 | 2 | 4 | 4 | 3 | 2 | 3 | 3 | 4 | 3 | 2 | 4 | 2 | 3 | **56.8** | ⚠ | parteneri: laborator + medic care semnează meniul; tratament fiscal de verificat |
| 18 | I | O5 | Urmărirea biletelor de trimitere (medici de familie) | 2 | 2 | 3 | 3 | 2 | 4 | 2 | 4 | 4 | 4 | 4 | 5 | 3 | 2 | 2 | 2 | 3 | **55.4** | ⚠ | P: nu știm dacă medicii de familie plătesc |
| excl. | U | O25 | Predicția buclelor care nu se vor închide, ca PRIM produs | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 2 | 3 | 3 | 2 | 4 | 4 | 2 | 4 | 4 | 5 | **54.2** | ⛔ | D: istoricul buclelor nu există încă; profilare cu date de sănătate = consimțământ explicit |
| 19 | W | O6 | Check-in administrativ după chirurgia de zi (oftalmologie, ortopedie) | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | **52.0** | ⚠ | R: la granița triajului; răspundere pentru semnale ratate (PLD din 9.12.2026) |
| excl. | O | O12 | Auditul „pauza” (dez-implementare) pentru asigurători | 3 | 3 | 4 | 2 | 3 | 4 | 1 | 4 | 1 | 2 | 3 | 4 | 2 | 1 | 4 | 3 | 3 | **51.4** | ⛔ | D: fără acces la datele de daune ale asigurătorilor și fără rețea în asigurări |
| excl. | AC | O23 | Predarea la pensionare: ultimul examen MM → medicul de familie | 1 | 1 | 4 | 2 | 2 | 5 | 3 | 4 | 3 | 4 | 4 | 5 | 2 | 1 | 3 | 4 | 3 | **51.2** | ⛔ | P: niciun plătitor identificat |
| excl. | AA | O20 | Monitor local de performanță pentru AI marcat CE (imagistică, screening) | 1 | 2 | 4 | 1 | 4 | 3 | 1 | 4 | 2 | 3 | 3 | 4 | 4 | 1 | 4 | 3 | 4 | **51.0** | ⛔ | D/P: niciun utilizator român de AI marcat CE găsit; fără acces la radiologie; obligațiile Art. 26 abia din 2028 |
| excl. | Y | O13 | Platformă de operare pentru programe de prevenție a diabetului (tip DPP), plătite de angajatori | 2 | 1 | 3 | 1 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 1 | 3 | 3 | 4 | **50.8** | ⛔ | P: niciun program sau plătitor DPP găsit în România |
| 20 | AD | O26 | Coordonator pentru părinții din România ai familiilor din diaspora (B2C) | 2 | 2 | 3 | 3 | 3 | 4 | 2 | 4 | 3 | 1 | 4 | 4 | 4 | 1 | 3 | 3 | 2 | **50.8** | ⚠ | P/S: B2C (consumatorii plătesc doar ca „membri captivi”); serviciu cu om, nu scalează solo |
| excl. | P | O14 | Puntea e-SănătateaMea pentru furnizori mici cu contract CNAS | 3 | 2 | 2 | 3 | 1 | 3 | 1 | 3 | 4 | 3 | 2 | 4 | 4 | 2 | 2 | 1 | 2 | **49.0** | ⛔ | I: niciun API public pentru terți găsit |
| excl. | T | O19 / MON §2 | Atelier RPM pentru un program privat de hipertensiune (cu alerte) | 2 | 1 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 1 | 3 | 2 | 5 | **45.4** | ⛔ | V+P: alertele = MDSW IIa (32-110k EUR, 9-18 luni); nicio rambursare RPM în România |
| excl. | V | F4 fundături | Scor de risc individual în fluxul medicului (SCORE2/FINDRISC) sau model propriu | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 3 | 5 | **45.4** | ⛔ | V: MDSW clasa IIa, fără excepție CDS în UE; validare clinică inaccesibilă |

**Legendă coloane:** U urgență · P plată · C concurență · RO România · INT internațional · T tehnic · D date · R reglementare · CL parteneri clinici · S solo · M efort MVP · K capital · V recurent · A achiziție · DF diferențiere · PT platforme terțe · ST strategic. „Loc” numără doar oportunitățile eligibile (fără ⛔).

**Notele-cheie ale primelor 10** (ce le ridică, ce le coboară):

| Cod | Ce o ridică | Ce o coboară | Sprijin în note |
|---|---|---|---|
| A | V=5 (examen periodic obligatoriu, de regulă anual), T=5, K=5, RO=4 (cabinete independente în Oradea) | U, P, A, DF doar 3: durerea și plata cabinetelor sunt neverificate; softul MM există deja | RSMM §3 (Legea 319/2006, HG 355/2007, amenzi 4.000–8.000 lei), RSMM §1 (6 produse MM), RSMM §5 (Medimun, Carimed) |
| G | U, P, A = 3; S, M = 4; V = 4; ST = 4 (cel mai aproape de „preventiv” dintre cele fezabile) | D=3 (export din programul clinicii, fără API), PT=3 | FUR §1–2 (golul de urmare, 7–62% la analize), RSMM §5 (GrandMed, NewMedics), RSMM §1 (fără API) |
| B | D=5, CL=5, S=5, M=5, PT=5: nu cere nimic de la nimeni | P=2 (HR-ul plătește?), A=2, DF=2 (Excel e substitutul gratuit), ST=2 | RSMM §3 (obligația și amenzile sunt ale angajatorului) |
| K | INT=4 (pacienți străini), U, P, A = 3 | C=2 (rechemarea dentară e deja vândută), ST=2 | RO §7 (clinicile își declară pacienți din IT, UK, AT, DE), EMG §L (VAstoma, DentAIM) |
| H | RO=4 (pachet național 2026), V=4 | P=2 (nu știm cât plătește CNAS medicului per serviciu), A=2 | RO §5 (pachetul 40+/60+), LAT O8 (contra) |
| J | C=4 (nimeni nu face asta), D=4 (datele vin de la pacient) | V=2, U=2 (volum necunoscut; probabil modul) | MON §1 (PPV 0,84–0,98; sensibilitate 41,2%), LAT O4 |
| Q | D=5 (date sintetice), CL=5, INT=4, DF=4 | U=2, A=2, M=2: cumpărătorii amână până în 2027–2028 | REG §4, FUR §5 (2029/2031), EMG Q1-D |
| L | CL=5, V=4 | C=1 (piață aglomerată), DF=2, ST=2 | FUR §3 (efecte SMS), EMG §L și Q3 (VAstoma, DentAIM, AI Frontdesk) |
| R | CL=5, R=4 | P=2, A=2 (clinicile cumpără conformitate abia după o amendă) | RO §3 (amenzi ANSPDCP), REG §4 |
| D | ST=5 (singurul activ de date longitudinal cu bază legală clară), DF=4 | U, P, A, RO = 2 (numărul de lucrători expuși din Bihor e necunoscut) | REG §6 (40 de ani, BK), LAT O17 |

### A5. Cât de robust e clasamentul

Am refăcut scorul cu trei seturi alternative de ponderi (fișierul `scoring/sensitivity.md`):
- **egale** (toate 17 criteriile la fel);
- **fezabilitate-întâi** (date, reglementare, solo, MVP cântăresc mai mult);
- **strategic-întâi** (relevanța strategică 15, internaționalul 5).

| Cod | Bază | Egale | Fezabilitate-întâi | Strategic-întâi |
|---|---:|---:|---:|---:|
| A | 1 | 1 | 2 | 1 |
| G | 2 | 3 | 3 | 2 |
| B | 3 | 2 | **1** | **7** |
| K | 4 | 4 | 4 | 8 |
| H | 5 | 5 | 6 | 6 |
| J | 6 | 6 | 9 | 4 |
| Q | 7 | 9 | 12 | **3** |
| L | 8 | 7 | 5 | 11 |
| R | 9 | 8 | 7 | 14 |
| D | 10 | 13 | 16 | 5 |

**Ce înseamnă:**
- **A și G sunt robuste**: rămân în primele 3 la orice set de ponderi.
- **B** e prima când contează doar fezabilitatea și a 7-a când contează strategia. E o variantă de canal a lui A, nu un produs strategic separat.
- **Q și D** urcă mult când strategia cântărește mai mult. Sunt opțiuni de anul 2, nu de start.
- Locurile 5–7 (H, J, Q) sunt la egalitate (63,2). Ordinea dintre ele nu e informativă.

### A6. Diferențe față de clasamentul preliminar din analiza laterală

LAT §F2 a pus pe primul plan forța dovezilor și drumul spre platformă. Scorarea de aici pune pe primul plan plătitorul, achiziția și accesul la date, pentru că ținta e 1–3k EUR MRR.

| LAT §F2 | Aici | Ce s-a întâmplat |
|---|---|---|
| #1 O2 (registrul MM) | **#1 (A)** | Confirmat. Am extins produsul cu scadențarul și portalul angajatorului, pentru că RSMM §3 arată că golul e pe partea angajatorului (MedLife are deja portal). |
| #2 O1 (FIT+ → colonoscopie, ROCCAS 4 NV) | **⛔ exclus (E)** | Un singur cumpărător, buget fixat în 2025 cu reguli de achiziție UE; intrare doar ca subcontractor; partenerii neverificați (RO §5, Inferences și Gaps). Chiar fără flag, scorul (57,0) l-ar pune pe ~16. Rămâne un pariu oportunist, nu un prim produs. |
| #3 O9 (ziua de prevenție) | #12 (C) | Depinde de laborator și program partener; apetitul angajatorilor e neverificat (EMG Q2, Gaps). E treapta a doua a lui A. |
| #4 O3 (inbox rezultate) | #14 (F) | În Bihor s-a găsit un singur laborator independent, Humanamed (RSMM §5). |
| #5 O8 (CNAS 40+) | #5 (H) | Confirmat, cu ⚠ pe plata CNAS. |
| #6 O15 (EHDS) | #7 (Q) | Confirmat ca opțiune de anul 2. |
| #7 O12 (auditul „pauza”) | **⛔ exclus (O)** | Fără acces la datele de daune și fără rețea în asigurări (LAT O12, contra). |
| #8 O11 (meniul fix) | #17 (N) | Partener laborator + medic semnatar; concurența abonamentelor marilor rețele. |
| #9 O16 (jurnal de acces) | #9 (R) | Confirmat. |
| #10 O4 (notificarea de la ceas) | #6 (J) | Urcă din cauza fezabilității, dar rămâne probabil un modul al lui G. |
| — | **noi în top 10: G, B, K, L, D** | G combină golul de urmare (FUR §1–2) cu clinicile-pilot din Oradea (RSMM §5). B e A vândut direct HR-ului. L e varianta „cea mai imediat realistă” din EMG Q3. |


---

## B. Top 10: fișe compacte

**Despre cifre.** Orele, costurile și prețurile de mai jos sunt **estimările mele**, dacă nu e citată o sursă. Ancorele de preț vin din: MediNote 50 lei/utilizator/lună; BizMedica 159–199 RON/lună, preț vechi (RO §2); Callio 139/189/299 EUR/lună (RO §2); agenți vocali românești ~299–499 EUR/lună (EMG Q3); unelte de rechemare dentară din SUA 199–329 USD/locație/lună (B2B Q4); extrapolarea din FUR §4: 20–60 EUR/locație/lună plus SMS la cost. SMS spre România: ~0,06–0,074 USD/mesaj prin API-uri internaționale (FUR §4 ← Sent.dm). Tariful agregatorilor locali nu e cunoscut.

**Nucleul tehnic comun** (îl refolosesc toate fișele; estimare):
- **Oracle APEX + PL/SQL** pe o instanță în UE. Model de date multi-client (fiecare cabinet sau clinică e un „tenant”), cu filtrare pe client la nivel de bază de date și **jurnal de audit pe fiecare acțiune**. Jurnalul e în același timp cerință GDPR și apărare sub noua directivă de răspundere pentru produse (PLD, din 9.12.2026; FUR §5, REG §7).
- **n8n** (găzduit în UE) pentru importuri programate (e-mail, folder, SFTP), trimiterea SMS/e-mail, escaladări și rapoarte lunare.
- **Python** pentru citirea fișierelor Excel/CSV/PDF și normalizare.
- **API-uri LLM** (regiune UE, fără retenție; REG §1, Inferences) **doar** pentru maparea coloanelor din fișiere dezordonate și extragerea din PDF cu verificare umană. **Niciodată** pentru interpretare clinică.
- **Statutul juridic:** fondatorul e persoană împuternicită (Art. 28 GDPR). Clientul e operatorul, pe baza Art. 9(2)(h). Kitul minim: contract de prelucrare, listă de sub-procesatori, găzduire în UE, ajutor la DPIA (REG §1, Inferences).

---

### #1 · A. Scadențar MM + portal pentru angajator + registrul recomandărilor (cabinete independente de medicina muncii)

- **Conceptul:** cabinetul de medicina muncii (MM) primește un instrument care urmărește scadențele examenelor (angajare, periodic, reluare) pentru fiecare angajator-client. Fiecare angajator primește un **portal cu marca cabinetului**: „în termen / expiră / depășit” și recomandările „apt condiționat” deschise sau închise, **fără diagnostice**. Pe scurt, cabinetul independent primește echivalentul portalului self-service MedLife.
- **Primul client plătitor:** un cabinet sau o firmă MM independentă din Oradea, cu 1–5 medici, care face examene la sediul angajatorilor (Medimun, Carimed; RSMM §5, Inferences) și pierde sau apără contracte în fața rețelelor (Medicris e la MedLife din 2022; RSMM §5).
- **MVP:**
  - import din Excel (lista angajaților pe angajator, post și grupă de risc, data ultimei fișe, rezultatul);
  - calendarul scadențelor la 30/60/90 de zile, plus regula examenului de reluare (după 90 de zile de absență medicală sau 6 luni din alt motiv, în 7 zile; RSMM §3);
  - remindere prin e-mail către HR și SMS către angajat (cu consimțământ);
  - portalul angajatorului (doar status) și raport lunar PDF;
  - lista recomandărilor cu termen pus de medic, plus încărcarea dovezii;
  - jurnal de audit.
- **Arhitectura:** nucleul comun. Portalul angajatorului e o aplicație APEX separată, cu acces doar la status. Python citește exporturile Excel ale programelor MM (BizMedica MM importă deja liste din Excel; RSMM §1).
- **Datele și integrarea:** evidențele cabinetului (Excel sau export din programul MM) și lista angajaților de la HR. Niciun API (RSMM §1, Gaps). Baza legală a cabinetului e Art. 9(2)(h) (medicina muncii; REG §1).
- **Concurenți și substitute:**
  - programe MM care emit fișa: BizMedica MM, MedExam, Qmedical, Charisma, MedSoft (RSMM §1);
  - portalul MedLife (RSMM §1);
  - Excel și urmărirea scadențelor vândută ca serviciu (One Medicina Muncii, HARDMED, M Hospital; RO §5).
  - Detaliile sunt în §C2.
- **Prețul:** abonament pe cabinet, pe trepte după numărul de angajați urmăriți (ex. 49–149 EUR/lună), plus SMS la cost. Cabinetul îl poate refactura angajatorului. Ținta e ~2–4 lei/angajat/an, adică ~2,5–5% din prețul MM de 80–110 lei (RSMM §3). Testul de preț e în §C3.
- **Reglementare:**
  - categoria 1, administrativ: „logistica medicinei muncii” (REG §8);
  - angajatorul nu trebuie să vadă diagnostice. Practica „doar concluzia de aptitudine” e BK și trebuie verificată (REG §6, Gaps). Fișa de aptitudine are însă un exemplar pentru angajator (RSMM §3 ← HG 355/2007, anexa 5);
  - SMS-urile către angajați cer consimțământ (Legea 506/2004; RO §3);
  - PLD pentru versiunile lansate după 9.12.2026.
- **Ruta spre primii 3 clienți:** vizite fizice la Medimun, Carimed și Endodigest, cu un „audit de scadențe” gratuit pe exportul lor (O24 ca unealtă de vânzare; LAT §E). În paralel, 2–3 angajatori din rețeaua fondatorului sunt întrebați dacă ar folosi portalul. Un angajator interesat e argumentul de vânzare către cabinet.
- **Costuri și efort (estimare):**
  - MVP 120–160 h, adică ~3–4 luni la 10–12 h/săpt;
  - numerar ~1.500–3.000 EUR (avocat pentru DPA și politici, găzduire, credit SMS, asigurare);
  - operare ~40–80 EUR/lună plus SMS;
  - onboarding 6–10 h pe client, suport 1–2 h/lună.
- **Dovezi de cerere:**
  - obligație legală recurentă, cu amenzi de 4.000–8.000 lei pe abatere (RSMM §3 ← Legea 319/2006 art. 39(4); suma trebuie reverificată pentru 2026);
  - ITM găsește frecvent muncă fără examen sau fișe lipsă (RSMM §3 ← rezumat ITM / Alba24);
  - MedLife vinde exact acest strat angajatorilor (RSMM §1 ← medlife.ro/self-service);
  - furnizorii își fac reclamă cu urmărirea scadențelor (RO §5).
  - **Lipsesc:** orice dovadă că un cabinet independent plătește pentru asta și orice sondaj despre durerea angajatorilor (RSMM §3, Gaps).
- **De ce ar eșua:**
  - cabinetele consideră că programul MM „arată deja scadențele” și nu plătesc în plus;
  - marja mică (80 lei/angajat/an) lasă buget mic;
  - în Bihor sunt doar ~6 cabinete independente identificate (RSMM §5), deci plafonul local e mic: la ~90 EUR/lună, toate 6 ar da ~540 EUR MRR (calculul meu);
  - un vendor MM (Setrio, DMV Consult) adaugă un portal și închide golul.

### #2 · G. Bucle deschise în clinici independente de boli cronice

- **Conceptul:** o listă de lucru zilnică pentru clinică, cu trei tipuri de „bucle deschise”:
  - (1) **control scadent** stabilit de medic și neprogramat;
  - (2) **rezultat marcat de laborator** în afara intervalului, fără consultație programată;
  - (3) **trimitere emisă** fără răspuns.
  Pacientul primește un mesaj neutru cu link de programare, asistenta vede pe cine sună, iar închiderea buclei se jurnalizează. Clinica primește un raport lunar cu „buclele închise → consultații și analize facturate”.
- **Primul client plătitor:** o clinică independentă multi-specialitate cu diabet, cardiologie și endocrinologie, cu laborator propriu sau partener (GrandMed, NewMedics; RSMM §5, Inferences). Plătitorul e proprietarul sau managerul, din venitul recuperat.
- **MVP:**
  - import zilnic CSV/Excel din programul clinicii (vizite, data controlului fixată de medic, rezultate cu marcajul laboratorului);
  - reguli deterministe (fără scor de risc);
  - lista de lucru pe asistentă;
  - SMS/e-mail cu consimțământ și link de programare;
  - registrul de consimțământ;
  - raport lunar;
  - grup de control opțional (o parte din bucle nu primesc mesaj), ca să se vadă efectul.
- **Arhitectura:** nucleul comun, cu reguli în PL/SQL. n8n face importul și trimiterea. Python mapează exporturile (fiecare program de clinică arată altfel). LLM doar pentru maparea coloanelor, cu confirmare umană.
- **Datele și integrarea:** exportul programului clinicii. Programele românești (icMED, MediNote, Zarina etc.) n-au API public (RSMM §1). Rezultatele de laborator vin des ca PDF sau e-mail (RSMM §2, Inferences), deci la început se citesc doar marcajele laboratorului.
- **Concurenți și substitute:**
  - remindere incluse în programele de cabinet (MediNote include SMS; RO §2);
  - agenți vocali și WhatsApp (VAstoma, DentAIM, AI Frontdesk; EMG §L);
  - asistenta cu telefonul;
  - rețelele interpretează rezultatele în propriile aplicații (asistentul AI MedLife, Synevo Decoder; RSMM §2), dar nu vând clinicilor independente.
- **Prețul:** pe locație, ~79–199 EUR/lună, plus SMS la cost. Auditul inițial e gratuit (O24). Ancore: unelte de rechemare din SUA la 199–329 USD/lună (B2B Q4); extrapolarea românească de 20–60 EUR (FUR §4). Testul e în §C3.
- **Reglementare:**
  - categoria 1 numai dacă termenele sunt ale medicului și marcajele ale laboratorului. „Evidențiază valori anormale și prezice deteriorarea” ar face produsul dispozitiv, posibil sub IVDR (REG §2, tabel; REG §8);
  - consimțământ pentru mesaje (Legea 506/2004);
  - datele despre vizite la o clinică de specialitate sunt date de sănătate indirecte (REG §1, Inferences);
  - din 2031 poate deveni „sistem EHR” sub EHDS, dacă tratează rezultate de laborator (FUR §5).
- **Ruta spre primii 3 clienți:** GrandMed și NewMedics în Oradea, apoi Medena (RSMM §5; RO §7). Prima întâlnire se încheie cu oferta unui audit gratuit pe 6 luni de date: „câte bucle sunt deschise acum”. Apoi clinici independente din Cluj și Timișoara, prin rețea.
- **Costuri și efort (estimare):**
  - MVP 140–180 h;
  - numerar ~2.000–3.500 EUR;
  - operare ~50–100 EUR/lună plus SMS;
  - onboarding 10–15 h pe client (maparea exportului), suport 2–3 h/lună.
- **Dovezi de cerere:**
  - neurmarea rezultatelor de laborator e de 6,8–62% în studii (FUR §1 ← Callen et al., JGIM);
  - alertele pasive nu ajung: 18,1% neconfirmate (FUR §1 ← Singh 2009);
  - urmărirea cu om care acționează funcționează: 73,4% față de 52,2% evaluați (FUR §2 ← Murphy/Singh RCT);
  - în România n-a fost găsit niciun proces „laborator → medic → rechemare”; urmarea e lăsată pe seama pacientului (RSMM §2, Inferences).
  - **Lipsesc:** orice măsurătoare românească a golului și orice preț plătit de clinici românești pentru rechemare (FUR §1 și §4, Gaps).
- **De ce ar eșua:**
  - exporturile sunt prea dezordonate și fiecare clinică devine un proiect de integrare;
  - clinica nu vrea să „hărțuiască” pacienții;
  - consimțământul pentru SMS lipsește din fișele vechi;
  - venitul recuperat e prea mic ca să justifice 100+ EUR/lună;
  - mandatul de programare prin e-SănătateaMea din T4 2026 pentru furnizorii cu contract CNAS schimbă fluxul (RSMM §6, Inferences, speculativ).

### #3 · B. Scadențar MM vândut direct angajatorilor (HR)

- **Conceptul:** același nucleu ca A, cumpărat de angajator, indiferent ce furnizor MM are. Urmărește scadențele fișelor, trimite remindere angajaților și șefilor de tură, ține istoricul pentru un control ITM.
- **Primul client plătitor:** un angajator cu 100–300 de angajați din Bihor, cu ture și grupe de risc (producție, logistică), cu un singur om de HR și furnizorul MM la cabinet extern. Plătitorul e HR-ul sau directorul general.
- **MVP:** import Excel; calendarul scadențelor; remindere; exportul listei „de trimis la MM luna aceasta” către furnizor; raport lunar; istoric. **Fără date medicale:** doar datele scadențelor și concluzia de pe fișă, pe care angajatorul o primește oricum (RSMM §3 ← HG 355/2007, anexa 5).
- **Arhitectura:** nucleul comun, varianta simplă: fără integrare cu furnizorul, autoservire.
- **Datele și integrarea:** doar de la angajator. Nu e nevoie de cabinet sau de medic.
- **Concurenți și substitute:** Excel, modulele HR/salarizare (neverificat în note), furnizorul MM care urmărește scadențele ca serviciu (RO §5), portalul MedLife pentru clienții MedLife (RSMM §1).
- **Prețul:** pe angajator, pe trepte (ex. 29–79 EUR/lună după numărul de angajați). Testul e în §C3.
- **Reglementare:** categoria 1. Angajatorul e operator pentru datele de HR. Concluzia de aptitudine e totuși dată legată de sănătate, deci se folosesc minimizarea datelor și contract de prelucrare. SMS doar cu consimțământ.
- **Ruta spre primii 3 clienți:** rețeaua de angajatori a fondatorului din Oradea (parcurile industriale; LAT O9, distribuție). Mesajul de vânzare: „o amendă ITM costă cât 5–10 ani de abonament” (calculul meu, pe baza amenzilor din RSMM §3).
- **Costuri și efort (estimare):** MVP 80–110 h; numerar ~1.000–2.000 EUR; onboarding 2–4 h; suport sub 1 h/lună.
- **Dovezi de cerere:** obligația și amenzile sunt ale angajatorului (RSMM §3 ← Legea 319/2006 art. 13 lit. j și art. 39(4)). Amenzile sunt de ~40–100 de ori prețul MM pe angajat (RSMM §3, Inferences). **Lipsesc:** orice sondaj despre cum își programează angajatorii examenele (RSMM §3, Gaps).
- **De ce ar eșua:**
  - Excel-ul e „suficient” și gratuit;
  - furnizorul MM face oricum urmărirea;
  - HR-ul nu are buget de software pentru o obligație pe care o consideră rezolvată;
  - prețul unitar e mic, deci e nevoie de mulți clienți (fiecare cu vânzare separată);
  - produsul e slab strategic (ST=2).

### #4 · K. Urmărirea pacienților de turism dentar (Oradea)

- **Conceptul:** după faza 1 a unui implant, pacientul pleacă acasă. Instrumentul programează protocolul de după tratament, face check-in-uri în DE/IT/EN/HU (fotografii și chestionar trimise medicului, **fără evaluare automată**) și planifică fereastra de călătorie pentru faza 2.
- **Primul client plătitor:** o clinică dentară din Oradea care își face reclamă la pacienți străini (Dental-Art, MaxiloMED, LifeDent, Estetical Dentis, German Dental; RO §7).
- **MVP:** planul post-tratament pe pacient; mesaje programate multilingve; încărcarea fotografiilor în UE; tabloul medicului; reminderul pentru faza 2.
- **Arhitectura:** nucleul comun, plus stocare de fișiere în UE. LLM doar pentru traducerea șabloanelor, verificată de om.
- **Datele și integrarea:** planul de tratament din programul clinicii (iStoma, icMED și altele, fără API; RSMM §1) și fotografiile pacientului (date de sănătate: contract de prelucrare, găzduire în UE).
- **Concurenți și substitute:** reminderele dentare existente (VAstoma, DentAIM; EMG §L), iStoma (5.300 de medici declarați; RSMM §1), WhatsApp-ul coordonatorului clinicii.
- **Prețul:** 99–249 EUR/lună pe clinică (ancoră: Callio 139–299 EUR; RO §2).
- **Reglementare:** categoria 1 dacă doar transmite. Devine dispozitiv dacă evaluează automat fotografiile (LAT O7). Pacienți din alte state UE: GDPR identic, dar limba și jurisdicția reclamațiilor contează.
- **Ruta spre primii 3 clienți:** vizite la clinicile de turism dentar din Oradea, prin rețeaua locală.
- **Costuri și efort (estimare):** MVP 120–160 h; numerar ~2.000–3.000 EUR (traduceri, stocare).
- **Dovezi de cerere:** clinicile declară pacienți din IT, UK, AT, DE (RO §7 ← Dental-Art); peste 30.000 de turiști medicali în România într-un an (RO §7 ← Economica.net); implanturi la 400–450 EUR față de 560–600 EUR în Ungaria (RO §7 ← Stomatologo). **Lipsesc:** volumul pentru Bihor (RO §7, Gaps).
- **De ce ar eșua:** volum prea mic pe clinică; coordonatorul clinicii face asta pe WhatsApp gratuit; produsul nu duce spre predictiv (ST=2); același cumpărător ca rechemarea dentară deja analizată (L4).

### #5 · H. Rechemarea pentru pachetul CNAS de prevenție 40+/60+ (medici de familie)

- **Conceptul:** din lista cabinetului, cine e eligibil după **vârstă și data ultimei prevenții** (nu după risc). Invitații prin SMS, telefon sau scrisoare, programare, urmărirea celor 3 pași ai pachetului 40+ și ajutor la raportare.
- **Primul client plătitor:** un cabinet de medicină de familie cu contract CNAS și listă mare, cu asistentă, din Oradea, care vrea să folosească pachetul de prevenție.
- **MVP:** import din exportul programului de cabinet; lista eligibililor; invitații; programare; urmărirea pașilor; export pentru raportare.
- **Arhitectura:** nucleul comun.
- **Datele și integrarea:** exportul programului de cabinet. Programele de cabinet n-au API (RO §2).
- **Concurenți și substitute:** vendorii de program de cabinet (BizMedica/Setrio); e-SănătateaMea (programări obligatorii pentru furnizorii CNAS din T4 2026; RSMM §6); asistenta cu telefonul.
- **Prețul:** 15–30 EUR/lună pe cabinet, sau un modul vândut prin vendor cu împărțirea venitului (ancore: BizMedica 159–199 RON/lună; RO §2).
- **Reglementare:** categoria 1 cât timp eligibilitatea e regula de calendar a CNAS. Devine zonă de graniță dacă prioritizează după risc clinic (REG §8). Apelurile automate cer consimțământ (RO §3).
- **Ruta spre primii 3 clienți:** medicii de familie din rețeaua fondatorului, apoi asociația județeană a medicilor de familie.
- **Costuri și efort (estimare):** MVP 100–140 h; numerar ~1.500–2.500 EUR.
- **Dovezi de cerere:** pachetul de prevenție e gratuit din februarie 2026 pentru oricine e înscris la un medic de familie (RO §5 ← Capital, MS); titlu de presă: „90% din români nu știu” de pachet (RO §5 ← Doctorul Zilei). **Lipsesc:** cât plătește CNAS medicului per serviciu de prevenție (LAT O8, contra). Asistența primară primește doar 10% din cheltuiala de sănătate (RO §5).
- **De ce ar eșua:** medicul n-are un motiv financiar să invite mai mulți pacienți; nu are timp pentru 3 vizite în plus; vendorul de program adaugă funcția gratuit; e-SănătateaMea devine canalul de programare.

### #6 · J. Navigator după notificarea de la ceas (clinici de cardiologie)

- **Conceptul:** o pagină dedicată pe site-ul clinicii („am primit o notificare de la ceas”), cu un formular structurat, programarea testului de confirmare (ECG, Holter, MAPA) după protocolul clinicii, un jurnal de tensiune de 7 zile afișat fidel și remindere. **Medicul decide.**
- **Primul client plătitor:** o clinică privată de cardiologie din Oradea sau București.
- **MVP:** formular, programare, jurnal de 7 zile, remindere. 60–90 h, ca modul.
- **Arhitectura:** nucleul comun, plus o pagină publică APEX.
- **Datele și integrarea:** de la pacient. Fără integrare cu dispozitivul.
- **Concurenți și substitute:** formularul de programare al clinicii, telefonul.
- **Prețul:** modul de 39–79 EUR/lună sau o taxă pe pacient confirmat (estimare).
- **Reglementare:** categoria 1 doar dacă colectează, afișează și programează. Dacă interpretează sau semnalează praguri, devine dispozitiv IIa (REG §2, tabel).
- **Ruta spre primii 3 clienți:** clinicile cu cardiologie din Oradea (GrandMed, Medena; RSMM §5).
- **Costuri (estimare):** numerar ~1.000–1.500 EUR.
- **Dovezi de cerere:** notificările de fibrilație atrială sunt confirmate pe ECG în 84–98% din cazuri (MON §1 ← Perez NEJM 2019; Lubitz 2022). Notificarea de hipertensiune Apple are 41,2% sensibilitate și cere 7 zile de măsurători cu manșeta (MON §1 ← AAFP). **Lipsesc:** penetrarea wearable-urilor în România (EMG, Gaps).
- **De ce ar eșua:** volum prea mic (devine un modul al lui G, nu un produs); pacienții sună direct; tentația de a „interpreta” notificarea împinge produsul în MDR.

### #7 · Q. Componente EHDS pentru vendorii locali de software medical

- **Conceptul:** o fațadă FHIR R4 peste baze vechi Oracle/PL-SQL, un generator de rezumat IPS, tabele de mapare LOINC/ATC, componenta de jurnalizare și o evaluare de pregătire.
- **Primul client plătitor:** un vendor român de software pentru clinici sau laboratoare, cu bază Oracle și fără echipă FHIR (din note: MediNote, BizMedica/Setrio, icMED, iStoma; ca HIS: Hipocrate/RSC, InfoWorld; RO §2, RSMM §1).
- **MVP:** fațada FHIR pentru 5–8 resurse (Patient, Observation, DiagnosticReport, Composition), IPS pe date sintetice, jurnal de acces.
- **Arhitectura:** PL/SQL plus ORDS (REST), sau o fațadă Python. HAPI/Medplum ca referință (B2B nr. 19).
- **Datele și integrarea:** pentru dezvoltare nu e nevoie de date de pacient (date sintetice). Schemele vin de la vendor.
- **Concurenți și substitute:** open-source (HAPI, Medplum); integratori; echipa internă a vendorului.
- **Prețul:** licență plus integrare, de ordinul 5.000–15.000 EUR per vendor, plus mentenanță anuală (estimare fără ancoră în note).
- **Reglementare:** vendorul își autocertifică sistemul EHR. Fondatorul livrează o componentă. Nu e MDR (LAT O15).
- **Ruta spre primii 3 clienți:** rețeaua din București; contact direct cu ~10–20 de vendori.
- **Costuri și efort (estimare):** 250–400 h (inclusiv învățarea FHIR/IPS); numerar ~2.000–5.000 EUR.
- **Dovezi de cerere:** termene legale (sisteme EHR conforme pentru categoria 1 din 26.03.2029, rezultate de laborator din 26.03.2031; FUR §5); vendorii sunt fragmentați și fără API (RSMM §1). **Contra:** cumpărătorii vor amâna până în 2027–2028 (EMG Q1-D, Inferences), iar regulile românești de aplicare lipsesc.
- **De ce ar eșua:** nimeni nu cumpără înainte de 2028; open-source-ul e „suficient”; România întârzie aplicarea. Venitul nu vine în fereastra de 90 de zile.

### #8 · L. Remindere și reducerea absențelor, cu grup de control (clinici private, stomatologie)

- **Conceptul:** remindere SMS/e-mail cu confirmare în două sensuri, umplerea anulărilor din lista de așteptare și **un grup de control încorporat**, ca clinica să vadă efectul măsurat, nu promis.
- **Primul client plătitor:** o clinică stomatologică sau de specialitate independentă din Oradea, cu rată de absențe vizibilă.
- **MVP:** import sau sincronizare a calendarului; remindere; confirmare; listă de așteptare; raport cu grup de control. 80–120 h.
- **Arhitectura:** nucleul comun.
- **Datele și integrarea:** calendarul clinicii (Zarina sincronizează calendare Google/Microsoft; RSMM §1).
- **Concurenți și substitute:** reminderele incluse în programele de cabinet (MediNote; RO §2), VAstoma, DentAIM, AI Frontdesk (EMG §L), Callio, AllAI la 24–59 EUR (RO §2).
- **Prețul:** 49–99 EUR/lună pe locație, plus SMS.
- **Reglementare:** categoria 1. Consimțământul pentru apeluri automate trebuie cerut la programare (EMG §L ← Legea 506/2004). Predicția absențelor e profilare cu date de sănătate (REG §8, Legea 190/2018 art. 3).
- **Ruta spre primii 3 clienți:** clinicile dentare din Oradea (~527 de firme; RO §7, notă anterioară).
- **Costuri (estimare):** numerar ~1.500–3.000 EUR.
- **Dovezi de cerere:**
  - reminderele SMS cresc prezența (RR 1,06–1,23; FUR §3 ← Cochrane, Free 2013, Robotham 2016);
  - 39,6% dintre cei care sună pentru o programare nouă închid fără ea (RO §3 ← MedOcean, date de vendor);
  - **dar** țintirea predictivă n-a fost dovedită superioară reminderului pentru toți (FUR §3 ← JAMIA 2022).
- **De ce ar eșua:** produsul e marfă (FUR §3, Inferences: „commodity”); concurenții sunt deja pe piață; prețul scade spre zero.

### #9 · R. Jurnal de acces și cereri de acces la dosar (clinici private)

- **Conceptul:** primirea cererilor de acces la dosar, cu ceas de 30 de zile; livrare prin link securizat (nu WhatsApp sau e-mail); un jurnal „cine mi-a deschis dosarul” vizibil pacientului; mai târziu, export IPS.
- **Primul client plătitor:** o clinică stomatologică sau de specialitate care s-a speriat de o amendă ANSPDCP din presă.
- **MVP:** 80–110 h.
- **Arhitectura:** nucleul comun.
- **Datele și integrarea:** jurnalele programului clinicii, dacă există, sau un depozit de documente propriu.
- **Concurenți și substitute:** e-mail, WhatsApp, programul de cabinet.
- **Prețul:** 19–49 EUR/lună.
- **Reglementare:** categoria 1. Poate deveni parte a unui sistem EHR (2029/2031).
- **Ruta spre primii 3 clienți:** clinicile din Oradea, plus parteneriate cu consultanți GDPR.
- **Costuri (estimare):** numerar ~1.000–2.000 EUR.
- **Dovezi de cerere:** o clinică dentară amendată pentru refuzul accesului la dosar și centre medicale amendate pentru date trimise pe WhatsApp sau e-mail (RO §3 ← e-juridic); EHDS dă dreptul de a vedea cine a accesat datele (REG §4; MON §5).
- **De ce ar eșua:** clinicile cumpără conformitate abia după o amendă; valoarea pe client e mică; produsul e ușor de copiat de vendorii de programe.

### #10 · D. Arhiva longitudinală de expunere profesională

- **Conceptul:** un depozit pe fiecare lucrător expus (zgomot, praf, substanțe chimice, cancerigeni), cu afișarea fidelă a audiogramelor, spirometriilor și a monitorizării biologice în timp, nivelul de bază fixat la angajare, gestiunea termenului de păstrare și un pachet de predare către furnizorul următor.
- **Primul client plătitor:** un furnizor MM cu angajatori industriali (supraveghere specială) sau un angajator mare cu expuneri.
- **MVP:** depozitul; extragerea din PDF-urile audiometrelor și spirometrelor cu LLM, **verificată de om**; graficul în timp, fără interpretare; termenele de păstrare. 160–220 h.
- **Arhitectura:** nucleul comun, plus un pipeline Python și LLM pentru PDF.
- **Datele și integrarea:** evidențele furnizorului și exporturile PDF ale aparatelor.
- **Concurenți și substitute:** programele MM (RSMM §1), arhivele pe hârtie.
- **Prețul:** pe lucrător expus pe an (ex. 10–20 lei), sau 99–199 EUR/lună pe furnizor.
- **Reglementare:** categoria 1 ca evidență. Devine dispozitiv dacă semnalează automat deteriorarea. Erorile de extracție intră sub PLD (REG §7).
- **Ruta spre primii 3 clienți:** **ca a doua treaptă a lui A**, la aceiași clienți.
- **Costuri (estimare):** numerar ~2.000–4.000 EUR.
- **Dovezi de cerere:**
  - evidențele expunerii la cancerigeni se păstrează 40 de ani (REG §6 ← Directiva 2004/37/CE, BK);
  - grupa de risc 3 adaugă audiometrie, ECG și spirometrie (RSMM §3 ← caiet de sarcini ONRC);
  - supravegherea specială e printre tipurile de examen (RSMM §3 ← HG 355/2007 art. 8).
  - **Lipsesc:** numărul de lucrători expuși din Bihor (LAT O17).
- **De ce ar eșua:** piața locală e prea mică; furnizorii nu simt obligația de arhivare ca durere; extragerea din PDF greșește și creează răspundere.

**Ce leagă primele 10.** A, B, D și C (locul 12) sunt același cumpărător sau același flux (medicina muncii). G, J, L și H sunt același motor („listă de bucle + mesaj + jurnal”) vândut altor cumpărători. Motorul se poate construi o singură dată.

---

## C. Board, concurență, preț și panelul de cumpărători

### C0. Cum au rulat (de citit înainte de cifre)

- **Board-ul** (`founder-board`): **trei sub-agenți separați** (`claude -p`, model opus, fără unelte), câte unul pe lentilă: Ofertă, Monopol, Produs (`lenses.md`). Fiecare a primit doar brieful (`founder-sanatate/board/brief.md`): faptele din note, fără opinia mea. Board-ul a evaluat ideile de pe locurile 1–5 (A, G, B, K, H). Lentila Monopol a răspuns în engleză; memoriul e păstrat neschimbat.
- **Panelurile de cumpărători** (`founder-consumer/panel.py`):
  - **câte 20 de cumpărători** (varianta `--quick`), seed 2026, deci aceleași cărți la fiecare rulare;
  - fiecare cumpărător e un **sub-agent separat** (`claude -p`, model sonnet, fără unelte);
  - fiecare a primit brieful scris de `panel.py`, plus un **sufix identic pentru toți** (`panels/uniform_suffix.txt`): e român, cifra anuală de pe card e **cifra de afaceri a organizației** în EUR, prețurile sunt în EUR/lună fără TVA, răspunde în română, iar JSON-ul se tipărește pentru că sesiunea n-are unelte de scris fișiere;
  - răspunsul **propriu** al fiecărui cumpărător a fost salvat cu `panel.py save`, calea de rezervă din SKILL.md. N-am scris niciun răspuns în locul unui cumpărător;
  - **101 apeluri**, toate valide (unul a fost refăcut după un JSON incomplet).
  - Nu a fost nevoie să simulez eu panelul: CLI-ul `claude` era disponibil în sesiune. **N-a fost întrebat niciun om real.**
- **Personaje de cumpărător:**
  - panelul A: proprietari de cabinete MM independente (mici, medii, regionale);
  - panelul G: clinici cronice, **manageri de laboratoare independente** și **medici de familie cu contract CNAS**;
  - panelul B: **HR-ul unui angajator cu 150–300 de angajați din Bihor**, al unui IMM și al unui angajator cu mai multe locații.
  - **Managerul de prevenție de la un asigurător privat n-a fost pus în panel**, pentru că niciuna dintre primele trei idei nu-l are ca plătitor. Ideea în care e plătitor (O12, auditul „pauza”) e exclusă pentru lipsa accesului la date (§A). Un „nu” de la el la un pitch care nu i se adresează n-ar fi spus nimic.
- **Limitele, spuse o dată:**
  - modelele de limbaj tind să fie de acord, deci **ratele de cumpărare sunt o limită superioară**;
  - toți cumpărătorii sunt același model, deci răspunsurile sunt corelate;
  - la n=20, o diferență de 7 față de 3 cumpărători nu e semnificativă statistic (estimarea mea: p≈0,14).
  - Panelul arată obiecțiile și segmentele. **Nu prezice conversia.** Citatele nu sunt mărturii de clienți.
- **Concurența** (`founder-competitors`): doar din note (fără cercetare web nouă), cu link-urile citate acolo. Pasul cu recenziile n-a putut fi făcut (vezi C2).

### C1. Board-ul (locurile 1–5)

Fișiere: `board/offers.md`, `board/monopoly.md`, `board/product.md`, rezumatul în `board/board.md`.

| Idee | Ofertă | Monopol | Produs | Media | Voturi |
|---|---:|---:|---:|---:|---|
| A Scadențar MM + portal (cabinete) | 6 | 5 | 6 | 5,7 | 3 × FUND IF |
| G Bucle deschise | 7 | 6 | 5 | **6,0** | 3 × FUND IF |
| B Scadențar direct la HR | 4 PASS | 3 PASS | 7 | 4,7 | 2 PASS, 1 FUND IF |
| K Turism dentar | 5 | 3 PASS | 4 PASS | 4,0 | 2 PASS, 1 FUND IF |
| H Rechemare CNAS 40+ | 3 PASS | 3 PASS | 3 PASS | 3,0 | 3 × PASS |

- **Ce recomandă fiecare lentilă:**
  - **Ofertă:** G, apoi A. G are cel mai bun mecanism de dovadă: auditul gratuit.
  - **Monopol:** G, apoi A. G e singura idee cu ceva apropiat de un „secret”: un gol nerezolvat de nimeni pentru clinicile independente. Know-how-ul de integrare fără API devine o barieră.
  - **Produs:** B, apoi A. B e singura idee în care fondatorul deține toată experiența, într-o propoziție.
  - **A e singura idee pe care toți trei o pun în primele două.**
- **Riscuri ridicate de mai mulți membri:**
  1. **Piața locală e prea mică** pentru 1–3k MRR (toți trei);
  2. **funcția poate fi copiată în luna 6** de cele 6 programe MM existente sau de MedLife (A; toți trei);
  3. **lipsesc dovezile locale** de plată și de durere;
  4. **„cusătura” exporturilor fără API** (un portal neactualizat distruge încrederea);
  5. **granița MDR** la bucla „rezultat în afara intervalului” din G.
- **Condițiile, unite** (lista completă în `board/board.md`):
  - A: 3 pre-vânzări plătite **înainte** de construcție; ≥20 de cabinete independente accesibile; confirmarea că programele MM nu au deja portal pentru angajator; v1 = doar status, actualizat săptămânal.
  - G: 2 audituri reale cu recuperări de cel puțin 5× prețul și o conversie la plată; import fără muncă zilnică; o singură buclă în v1; opinie MDR scrisă.
  - B: doar ca parte de angajator a lui A.
- **Cea mai puternică versiune pe care o vede board-ul:** **un singur motor** (termene puse de profesionist, ținute la zi din exporturi, cu un om care acționează și jurnal) cu **două uși**. A e ușa rapidă la bani. G e ușa strategică, deschisă doar după audit.

### C2. Concurența (pe scurt)

Fișiere: `founder-sanatate/competitors.csv` (24 de rânduri, fiecare cu sursa în note) și `founder-sanatate/competitors.md`.

- **A:**
  - **6 programe MM emit deja fișa** (BizMedica MM, MedExam, Qmedical, Charisma, MedSoft, Tempomed; RSMM §1). BizMedica importă deja liste din Excel.
  - **MedLife** vinde exact „portalul pentru angajator” (RSMM §1).
  - **Niciun preț publicat** pentru software MM.
  - **Golul:** un portal pentru angajator cu marca **cabinetului independent**. E valabil doar dacă cele 6 programe nu-l au deja, ceea ce **trebuie verificat**: notele nu spun.
  - **Cine copiază primul:** Setrio și DMV Consult, pentru că au deja datele și clienții.
- **G:**
  - remindere incluse în programele de cabinet (MediNote 50 lei/utilizator/lună cu SMS);
  - agenți vocali și WhatsApp (Callio 139–299 €, receptie-clinica.ai 150 € plus setup, alții la 299–499 €);
  - rețelele interpretează rezultatele doar pentru pacienții lor;
  - e-SănătateaMea preia programările furnizorilor CNAS din T4 2026.
  - **Golul:** găsirea proactivă a pacienților care n-au mai programat controlul stabilit de medic. **Niciun produs românesc documentat.** Golul de produs există; cererea pentru el n-a fost demonstrată (C3).
- **B:** concurentul real e **Excel + furnizorul MM** (0 €). **Nu există gol vizibil.**
- **Recenzii:** notele nu conțin recenzii pentru acești concurenți, deci pasul 3 din skill (citirea recenziilor de 1–3 stele) **n-a fost făcut**. În locul lor folosesc obiecțiile din panel, marcate ca simulate.

### C3. Panelul de cumpărători (top 3) și retestarea ofertei

**Rezultatele** (fișierele `panels/<X>/results.md`):

| Panel | Pitch | Cumpără | Rata (limită superioară) | Cine cumpără |
|---|---|---:|---:|---|
| **A** cabinete MM independente | v1: remindere + portal, 59/99 € | **7 / 20** | **35%** | firme medii 4/8 (50%); „sub presiunea rețelelor” 3/3; „Excel și hârtie” 2/4 |
| A2 (aceleași cărți) | v2: „paritate cu rețelele”, configurare la sediu, fără CNP, 35/69/129 €, garanție 90 de zile | 3 / 20 | 15% | doar cei 3 „sub presiunea rețelelor” |
| **G** clinici cronice, laboratoare, MF | v1: trei bucle, export zilnic, 129 € | **0 / 20** | **0%** | nimeni |
| G2 (aceleași cărți) | v2: o singură buclă (controale), audit pseudonimizat, export automat, fără mențiuni medicale, 69 €, garanție | 2 / 20 | 10% | 2 din 9 clinici cronice; 0 din 7 MF; 0 din 4 laboratoare |
| **B** HR din Bihor | 39/79 € | **2 / 20** | **10%** | 2 din 3 „speriați de ITM”; 0 din 17 ceilalți |

**De ce refuză (cu citate, simulate):**
- **A:**
  - **Obișnuința** (6/13): „Folosesc deja programul MM care emite fișa de aptitudine, iar asistenta ține scadențele într-un Excel care merge.” (A/P002)
  - **Încrederea în date** (4/13): „Nu vreau să încarc pe o platformă externă lista a mii de angajați ai clienților mei, după ce am citit despre amenzile ANSPDCP.” (A/P005)
  - **Prețul din marjă** (2/13): „Costul de 59–99 € pe lună îl iau din marjă, iar clientul nu-mi dă un leu în plus.” (A/P015)
- **G:**
  - **Încrederea și GDPR** (7/20): „Nu-mi permit să dau date de pacienți diabetici și cardiaci unui SRL necunoscut.” (G/P001)
  - **„Programul trimite deja SMS”** (6/20).
  - **Plata pe capitație la medicii de familie** (3/20): „Eu sunt plătită pe listă, nu pe consultație.” (G/P017)
  - **Exportul zilnic** (2/20): „La noi nimeni nu știe să-l facă.” (G/P011)
- **B:**
  - **„Excel-ul și furnizorul MM ne anunță”** (10/18).
  - **„Nu e o problemă reală: n-am luat niciodată amendă”** (5/18).

**Ce ar schimba un „nu”** (cele mai repetate răspunsuri):
- **A:**
  - **integrare directă** cu programul MM, fără import manual;
  - **o referință** de la un cabinet din zonă;
  - **angajatorii să plătească ei portalul** sau să-l ceară explicit;
  - DPA, audit de securitate și export garantat al datelor;
  - preț în jur de 25–35 € pentru cabinetele mici.
- **G:**
  - **integrare fără export manual**;
  - **un audit pe datele lor** care arată zeci de pacienți pierduți, nu câțiva;
  - DPA și opinie juridică;
  - **referințe de la 2–3 clinici cu contract CAS**;
  - sub 50 €/lună pentru medicii de familie.
- **B:** o amendă ITM; integrarea cu platforma HR/salarizare; un preț sub 15–20 €.

**Retestarea ofertei** (`founder-offer`, aceleași cărți; pitch-urile vechi sunt păstrate ca `pitch-v1.md`):
- **G a urcat de la 0 la 2 din 20.** Ambii cumpărători sunt clinici de boli cronice (2/9 în acel segment). Ce i-a convins: auditul înainte de plată, garanția de 15 controale și prețul de 69 €. Medicii de familie și laboratoarele au rămas la 0. **Concluzie:** G are o ofertă care poate funcționa doar pentru clinicile cronice, și doar dacă auditul arată pacienți pierduți reali.
- **A a scăzut de la 7 la 3 din 20.** I-a pierdut pe 2 dintre cei cu „Excel și hârtie”, pe medicul ocupat și pe cel care caută noutăți, în principal pe **încredere**. Două interpretări (ale mele):
  - paragraful mai lung despre date (CNP, DPIA, consimțământ) a pus riscul în prim-plan;
  - v2 a scos din text **reminderele care economisesc telefoanele asistentei** și a pus accent pe „paritatea cu rețelele”, care contează doar pentru cei care au pierdut deja clienți.
  - Diferența poate fi și zgomot (n=20).
  - **Concluzie de ofertă:** motivul principal de cumpărare e **timpul asistentei, plus clientul păstrat la renegociere**. Partea de date se spune într-o singură frază sigură, nu într-un paragraf.

### C4. Prețul (Van Westendorp)

Fișiere: `pricing/*-curve.md` (ieșirile uneltei) și decizia în `pricing/pricing.md`. Prețurile sunt în EUR/lună, fără TVA.

| Idee (panel) | Interval acceptabil (PMC–PME) | OPP | IPP | Pragul „scump” pe segment |
|---|---|---:|---:|---|
| A (v1) | 24–120 € | 25 € | 59 € | mic 60 €, mediu 120 €, regional 250 € |
| A (v2) | 15–99 € | 30 € | 40 € | mic 40 €, mediu 95 €, regional 250 € |
| G (v1) | 30–130 € | 30 € | 69 € | clinici 150 €, laboratoare 110 €, MF 70 € |
| G (v2) | 15–120 € | 15 € | 40 € | clinici 120 €, laboratoare 80 €, MF 59 € |
| B | 10–60 € | 10 € | 25 € | 37–57 € |

**Deciziile de preț** (motivarea completă, cu marjele CFO, e în `pricing/pricing.md`):
- **A:** o scară **39 € / 79 € / 149 €** (mic / standard / regional), cu o medie țintă de ~65 €. **La 49 € sau mai puțin în medie, anul 1 e pe pierdere** (unealta CFO: −330 € la 49 €, −870 € la 39 €). Ofertă de lansare: „pilot fondator” pentru primele 5 cabinete, cu preț blocat 24 de luni, configurare inclusă și garanție de 90 de zile. Se testează 69 € față de 89 € pe treapta standard.
- **G:** **89 €/locație**, doar pentru clinicile cronice, după un audit gratuit, cu garanția de 15 controale programate. Se testează 69 € față de 99 €. Nu se vinde medicilor de familie.
- **B:** fără preț separat. Cel mult un nivel de autoservire la 19 € pentru angajatorii „speriați de ITM”, ca sursă de clienți pentru cabinete.

### C5. Ce schimbă secțiunea C față de scorare

- **A rămâne pe locul 1.** E singura idee pe care toate trei lentilele o pun în primele două și are cea mai mare rată în panel (35% în v1). Plafonul ei e însă mic, iar apărarea împotriva copierii e slabă.
- **G coboară de pe locul 2 al scorării în „a doua ușă, condiționată”.** Board-ul o preferă ca valoare, dar panelul arată 0% la oferta inițială și 10% la cea refăcută. Încrederea și integrarea sunt obstacole mai mari decât prețul. Se deschide doar după 2 audituri reale.
- **B dispare ca produs separat** (2 PASS în board și 10% în panel) și devine partea de angajator a lui A.
- **K și H ies** (PASS majoritar în board).

---

## D. CFO: economia unitară pentru A și G

**Cum s-a calculat.**
- **Unealta:** `founder-cfo/unit_economics.py`, rulată pe `founder-sanatate/cfo/*_numbers*.json`.
- **Unitatea:** un client pe o lună. `days_per_month = 1`, deci „per day” înseamnă clienți activi în luna respectivă.
- **Cele 36 de luni** sunt calculul meu peste ieșirile uneltei (`cfo/combine_36m.py`).
- **Intrările** sunt aproape toate **estimări**, fiecare cu sursa și raționamentul în `cfo/cfo-sources.md`.
- **SMS-urile** se refacturează la cost, deci sunt scoase și din preț, și din cost.
- **Nota completă:** `cfo/cfo.md`.
- Nu e consultanță financiară sau fiscală; structura trebuie verificată cu un contabil.

### D1. Intrările-cheie (estimări)

| Intrare | A | G |
|---|---:|---:|
| Preț (medie) | 65 €/client-lună (scara 39/79/149 €) | 89 €/locație-lună |
| COGS / client-lună: LLM, găzduire incrementală, e-mail, comisioane | 4 € | 4,5 € |
| SMS | refacturat la cost (~0,06–0,074 USD/SMS; FUR §4). Volum estimat: ~200 SMS/lună la un cabinet cu ~3.000 de angajați (~12 €) | ~150 SMS/lună pe clinică (~9 €), doar cu consimțământ |
| Costuri fixe / lună: găzduire UE 45 €, unelte 25 €, asigurare 50 €, contabilitate 30 €, deplasări 80 € | 230 € | 230 € |
| Pornire în numerar: avocat, revizie de securitate, materiale, găzduire în timpul construcției, deplasări, SMS; plus opinia MDR la G | 2.980 € | 3.900 € |
| Ore de integrare / client | 6–10 h | 10–15 h |
| Ore de suport / client-lună | ~1 h | ~2 h |
| Capacitatea la 10–12 h/săpt | ~25 de clienți | ~13 clienți |
| CAC | ~25–40 h de vânzare + 50–100 € deplasări (~75–150 € numerar; ~600–900 € cu timpul la 20 €/h) | asemănător, plus auditul (~8–10 h) |
| Rampa | +1 client/lună din luna 4 (după 3 pre-vânzări) | primul client în luna 5, apoi ~0,5/lună |
| Ore pentru MVP | 120–160 h | 140–180 h |

Rampa e calibrată pe panel: ratele simulate de 35%/15% (A) și 0%/10% (G) sunt tratate ca limită superioară, deci conversia reală estimată din vizite calificate e de ~10–15%. Raționamentul complet e în `cfo-sources.md`.

### D2. Rezultatele

| Indicator | A (bază) | A („spre 3k”) | G (bază) |
|---|---:|---:|---:|
| Contribuție / client-lună | **61 €** (94%) | 61 € | **84,5 €** (95%) |
| Prag de rentabilitate lunar | **4 clienți** | 4 | **3 clienți** |
| Numerar necesar până se autofinanțează | **3.825 €** | 3.825 € | **5.233 €** |
| Profit operațional anul 1 | **+534 €** | +534 € | **−1.070 €** |
| MRR la luna 12 / 24 / 36 | 650 / 1.430 / 1.625 € | 650 / 2.210 / 3.250 € | 356 / 890 / 1.157 € |
| **Luni până la 1.000 € MRR** | **18** | 15 | **27** |
| **Luni până la 3.000 € MRR** | **niciodată** în 36 de luni (plafon ~25 de clienți ≈ 1.625 €) | **31** | **niciodată** (plafon ~13 clienți ≈ 1.157 €) |
| Pornirea recuperată în luna | 17 | 17 | 25 |
| Profitul cumulat ajunge la 25.000 € în luna | 36 | 30 | peste 36 |
| Profit cumulat la 36 de luni, după pornire | 22.229 € | 40.134 € | 9.790 € |
| Anul 1 cu timpul fondatorului la 20 €/h | −546 € | — | (mai slab) |

**Scenariul „spre 3k”** (doar pentru A) presupune ~20 h/săpt din luna 13 și +2 clienți/lună. Ajunge la 50 de cabinete, adică ~10% din cele 508 listate național (RSMM §3). E un risc real de saturare a pieței.

### D3. Nota CFO

- **Marja nu e problema.** Contribuția e de 94–95%. Software-ul administrativ are costuri variabile mici.
- **Banii nu sunt constrângerea.** A cere ~3,8k € și G ~5,2k € din cei 25k €.
- **Constrângerea e timpul fondatorului plus rampa.**
  - La volum −20%, anul 1 al lui A trece pe pierdere: **−125 €**.
  - La 10–12 h/săpt, **nicio idee nu ajunge singură la 3.000 € MRR**. A se oprește în jur de 1.600 €, G în jur de 1.150 €.
  - **1.000 € MRR e realist pentru A în ~18 luni.**
- **Trei pârghii, cu rularea uneltei care le dovedește:**
  1. **Prețul mediu la 79 € în loc de 65 €:** anul 1 urcă de la 534 € la **1.290 €**.
  2. **Un canal care aduce +50% volum** (un vendor de program MM sau o asociație): anul 1 ajunge la **2.181 €**, iar MRR-ul la 975 € în luna 12 și la 2.145 € în luna 24.
  3. **Costuri fixe mai mici** (fără deplasări plătite, asigurare la 30 €): pragul scade de la 4 la **2 clienți**, iar anul 1 urcă la **1.734 €**.
- **Dacă SMS-ul nu se poate refactura** și fondatorul îl absoarbe (~12 €/client-lună la A, ~9 € la G): contribuția scade la 49 € (A) și 75,5 € (G). **Anul 1 al lui A trece pe pierdere: −114 €**; G ajunge la −1.250 € (`cfo/A_cfo_sms_absorbed.md`, `G_cfo_sms_absorbed.md`). De aceea refacturarea SMS la cost trebuie scrisă în contract, nu doar promisă.
- **CAC-ul complet** (~600–900 € cu timpul fondatorului) se recuperează în **~10–15 luni** la 61 € contribuție. **Churn-ul din primul an e scump.** De aceea pilotul cu garanție trebuie făcut doar la cabinete calificate (cu export funcțional și cu cel puțin un angajator care vrea portalul).
- **G pierde bani în anul 1 la orice preț testat** (−1.870 € la 49 €, −470 € la 119 €), din cauza rampei: audit, apoi integrare per clinică. E o a doua ușă bună, finanțată din venitul lui A, nu un start.
- **Condițiile de bani ale board-ului** (pre-vânzări, audituri reale, lista de ≥20 de cabinete): **niciuna nu e îndeplinită încă**. Ele sunt chiar metricile validării de 90 de zile (§E4).

---

## E. Verdictul final (founder-plan)

### E1. Verdictul calculat (`compile.py`, nu scris de mână)

Fișiere: `founder-sanatate/plan/A/business-plan.md` și `plan/G/business-plan.md`, cu `summary.md`, `one-pager.md` (doar A) și `offer.md`.

| Variantă | Contribuție > 0 | Profit în anul 1 | Pragul de rentabilitate încape în capacitate | Panel ≥ 25% | **Verdict** |
|---|---|---|---|---|---|
| A, cu panelul v1 | ✓ 61 € | ✓ +534 € | ✓ 4 din 25 | ✓ 35% | **Profitable** |
| A, cu panelul v2 | ✓ | ✓ | ✓ | ✗ 15% | Not yet |
| A, volum −20% (what-if CFO) | ✓ | ✗ −125 € | ✓ | — | (ar pica) |
| A, SMS absorbit în loc de refacturat (what-if CFO) | ✓ 49 € | ✗ −114 € | ✓ | — | (ar pica) |
| G, cu panelul v2 | ✓ 84,5 € | ✗ −1.070 € | ✓ 3 din 13 | ✗ 10% | **Not yet** |
| G, cu panelul v1 | ✓ | ✗ | ✓ | ✗ 0% | Not yet |

**Cum se citește.** „Profitable” la A înseamnă un profit operațional pozitiv în anul 1. Profitul există, dar e mic: **+534 €**. Verdictul se răstoarnă la −20% volum, cu SMS-ul absorbit sau cu panelul v2. Concluzia: **A trece la limită, iar G nu trece.**

### E2. Cea mai puternică oportunitate inițială: **A · „Scadențar MM”**

**Ce e, exact.** Un add-on administrativ pentru **cabinetele și firmele independente de medicina muncii**. Ce face:
- ține scadențele fișelor de aptitudine pentru toți angajații fiecărui client, alimentat din exportul programului MM existent;
- trimite remindere către HR-ul clienților, ca asistenta să nu mai sune;
- dă fiecărui angajator un **portal cu marca cabinetului**: în termen / expiră / depășit, plus recomandările „apt condiționat” deschise. **Fără diagnostice și fără CNP;**
- trimite un raport lunar, folosit la renegocierea anuală.
- **Preț:** 39 / 79 / 149 €/lună, plus SMS la cost. Garanție de 90 de zile, primele 5 cabinete la preț de fondator.
- **B (direct la HR) nu e produs separat:** e partea de angajator a lui A.

**De ce A:**
- **Scorare:** locul 1 (73,4/100) și locul 1–2 la orice set de ponderi (§A5).
- **Board:** singura idee pusă de **toate trei** lentilele în primele două (3 × FUND IF; §C1).
- **Panel:** cea mai mare rată simulată (35% la v1). Cumpără firmele medii și cabinetele care au pierdut clienți în fața rețelelor (§C3).
- **Piața și plătitorul:**
  - categoria 1, administrativ (REG §8, punctul de intrare 3);
  - plătitor existent: angajatorul plătește obligatoriu, iar cabinetul încasează (RSMM §3);
  - cumpărători numărabili, la care fondatorul poate merge fizic (RSMM §5).
- **Banii:** cel mai mic numerar necesar (~3,8k €) și primul an pe plus (§D).

**De ce nu e o victorie ușoară (spus direct):**
- plafonul la 10–12 h/săpt e de ~1.600 € MRR;
- 1.000 € MRR vine abia în ~luna 18;
- **3.000 € MRR cere fie ~20 h/săpt din anul 2 (≈ luna 31, ~50 de cabinete), fie un canal** (un vendor de program MM care revinde);
- copierea de către Setrio sau DMV Consult e reală;
- golul există doar dacă programele MM n-au deja portal pentru angajator, iar notele nu pot confirma asta.

**Cum crește spre preventiv/predictiv fără model propriu** (inferență, nu plan):
1. **Anul 1, A:** fiecare examen și fiecare recomandare „apt condiționat” e o **buclă cu termen**. Se adună istoricul buclelor (cine, când, după câte contacte). LAT §F1.3 arată că acest istoric nu există azi structurat nicăieri în România.
2. **Anii 1–2, același cumpărător:**
   - **D**, arhiva de expunere: audiograme și spirometrii afișate fidel în timp;
   - **C**, ziua de prevenție la locul de muncă, cu un laborator partener. E testul în aceeași vizită, cu dovada cea mai bună din note (ȘTI KQ1 ← ACCESS: 22% → 100%).
3. **Anul 2, același motor, altă ușă:** **G**, controalele pierdute la clinicile cronice, deschisă după referințele de la A.
4. **Anii 2–3:**
   - **predicție operațională** „cine nu-și va închide bucla” (O25), cu **grup de control încorporat** și consimțământ explicit (Legea 190/2018 art. 3; REG §1). Trebuie să bată reminderul pentru toți, lucru nedovedit încă (FUR §3 ← JAMIA);
   - fără scoruri clinice individuale.
5. **2028–2031:**
   - stratul de buclă devine locul unde se conectează **modele de risc ale unor vendori cu marcaj CE**: vendorul poartă MDR-ul, fondatorul poartă urmărirea;
   - componentele EHDS (Q) când apar regulile românești;
   - folosirea secundară a datelor prin EHDS, după ~2029 (REG §4).

### E3. Locul 2: **G · „Controale pierdute”** (clinici independente de boli cronice), condiționat

- **De ce e a doua:**
  - e cea mai bună strategic: duce direct spre prevenție, iar know-how-ul de integrare fără API devine o barieră;
  - e preferata board-ului (media 6,0; lentilele Ofertă și Monopol o pun prima);
  - dovezile internaționale ale golului sunt solide (FUR §1–2).
- **De ce nu e prima:**
  - **panelul a respins-o** (0/20 la v1, 2/20 la v2), în principal pe încredere și integrare;
  - **anul 1 e pe pierdere** la orice preț testat;
  - 1.000 € MRR vine abia în ~luna 27.
- **Condițiile de deschidere (toate):**
  1. ≥2 clienți A plătitori, ca referințe și dovadă de încredere;
  2. 2 audituri pe export pseudonimizat, fiecare cu **≥30 de controale depășite**;
  3. o opinie MDR scrisă;
  4. ≥1 clinică care plătește ≥69 €/lună după audit.
- **Ce nu se face fără opinie MDR:** bucla „rezultat în afara intervalului” și orice prioritizare după risc. Ele mută produsul în categoria de dispozitiv medical (REG §2, §8).

### E4. De evitat

| Ce | De ce | Sursa |
|---|---|---|
| **H**, rechemarea CNAS 40+/60+ | Cumpărătorul n-are bani (asistența primară primește 10% din cheltuială), plata pe serviciu e necunoscută, statul poate absorbi funcția. Board: 3 × PASS. | RO §5; LAT O8; §C1 |
| **K**, turism dentar | Volum necunoscut, piață aglomerată, nu duce spre predictiv. Board: 2 PASS. | RO §7; §C1 |
| **B** ca produs separat | Excel-ul gratuit e suficient (18/20 refuză). Board: 2 PASS. | §C3 |
| **E**, navigatorul FIT ca prim produs | Un singur cumpărător, buget și achiziție UE, parteneri neverificați. Cel mult subcontractare oportunistă. | RO §5 |
| **O**, auditul „pauza” pentru asigurători | Fără date de daune, fără rețea în asigurări. | LAT O12 |
| **P**, puntea e-SănătateaMea | Niciun API public pentru terți. | RSMM §6 |
| **T**, RPM cu alerte; **V**, scoruri de risc individuale; **orice model propriu** | MDR clasa IIa (~32–110k €, 9–18 luni); AI Act cu risc ridicat din 2.08.2028; nicio rambursare RPM în România. | REG §2, §3; MON §2 |
| **U**, predicția buclelor ca prim produs | Istoricul nu există încă; profilarea cu date de sănătate cere consimțământ explicit. | REG §1; LAT O25 |
| **Q**, componentele EHDS ca prim produs | Venit realist abia în 2027–2028; regulile românești lipsesc. | EMG Q1-D; FUR §5 |
| **L**, remindere generice | Marfă, piață aglomerată, prețul scade spre zero. | FUR §3; EMG §L |
| B2C: coordonator diaspora (AD), DPP (Y), PHR, abonamente de analize direct la consumator | Consumatorii plătesc doar ca „membri captivi”. Fundături. | EMG Q2; LAT §F4 |
| Scrib AI general în română | Concurenți cu sute de milioane strânse; alunecare spre clasa IIa. | EMG Q1-F; B2B Q4 |

### E5. Ipotezele care ar schimba verdictul

1. **≥2 dintre programele MM folosite de cabinete au deja un portal sau remindere pentru angajator.** Golul lui A dispare. Se trece la vânzarea prin vendor sau la G.
2. **În Nord-Vest sunt sub ~20 de cabinete independente accesibile.** Plafonul lui A devine prea mic și singurul drum e un canal (vendor sau asociație).
3. **Un vendor de program MM acceptă să revândă sau să integreze.** A devine mult mai puternic: +50% volum înseamnă ~2.100 € MRR în luna 24 (§D3).
4. **Auditurile G arată ≥30–50 de controale depășite pe clinică, iar clinicile plătesc.** G urcă la egalitate sau pe primul loc: bilet mai mare, valoare strategică mai mare.
5. **Fondatorul poate da ~20 h/săpt din anul 2.** 3.000 € MRR devine posibil în ~luna 31 cu A.
6. **Amenda art. 39 pentru 2026 e mult mai mică sau ITM controlează rar în Bihor.** Argumentul angajatorului slăbește (A, B).
7. **Regula „angajatorul vede doar concluzia” e mai strictă decât se presupune** (de ex. recomandările „apt condiționat” nu pot fi arătate). Portalul se reduce la status. A rămâne viabil, dar mai slab.
8. **CNAS plătește medicului de familie o sumă semnificativă pe serviciu de prevenție.** H reintră în discuție.
9. **Reforma MDR (2027–2028) mută mai mult software în clasa I.** Etapa predictivă devine mai ieftină mai devreme.
10. **Testele reale arată rate mult sub panel** (de ex. 0 pre-vânzări din 15). Verdictul A cade.

### E6. Validarea de 90 de zile: metrici go / no-go

**Zilele 1–30, descoperire (fără cod):**
- 15 conversații calificate cu cabinete MM independente: Oradea (Medimun, Carimed, Endodigest, Alfa Medica, Gecoprosana, Neoklinik), apoi Cluj, Satu Mare, Arad. Plus 5 angajatori din rețeaua fondatorului.
- Se verifică pentru fiecare: proprietarul (ONRC/Termene), programul MM folosit, cum țin scadențele, dacă programul are portal pentru angajator.
- Se întreabă direct Setrio și DMV Consult.
- Partea juridică:
  - suma amenzii din art. 39 pentru 2026;
  - regula „ce vede angajatorul”;
  - consimțământul pentru SMS;
  - DPA-ul.

**Zilele 31–60, pre-vânzare:**
- machetă APEX clicabilă, pe date sintetice;
- oferta „pilot fondator”;
- scrisori de intenție plus o plată (avans sau prima lună).

**Zilele 61–90:** MVP minim (import, calendar, reminder e-mail, portal de status) la 1–3 piloți, pe exporturi reale. În paralel, un singur audit G, dacă o clinică acceptă.

| Metrică | GO | NO-GO |
|---|---|---|
| Cabinete independente accesibile găsite (Oradea + Nord-Vest) | ≥20 | <10 |
| Conversații calificate | ≥15, dintre care ≥8 în afara Oradei | — |
| Cabinete care confirmă durerea (timpul asistentei sau clienți pierduți în fața rețelelor) | ≥6 din 15 | ≤3 din 15 |
| Programe MM care au deja portal pentru angajator | 0–1 | ≥2 (golul nu există) |
| **Pre-vânzări plătite la ≥39 €/lună** | **≥3 până în ziua 60** | **≤1 până în ziua 75** |
| Export funcțional (angajat, angajator, data examenului, concluzie, scadență) obținut în <30 min | ≥2 cabinete | 0 |
| Timpul de curățare a datelor la primul pilot | ≤10 h | >20 h |
| Angajatori care spun că ar folosi portalul | ≥3 | 0 |
| Orele fondatorului | ≤12 h/săpt | >15 h/săpt, susținut |
| G (opțional): controale depășite în auditul pseudonimizat | ≥30 pe clinică | <10 pe clinică |

**Decizia din ziua 90:**
- **GO pe A:** ≥3 pre-vânzări plătite **și** ≥2 exporturi funcționale **și** golul confirmat.
- **PIVOT:** golul există, dar cabinetele nu plătesc. Se încearcă fie un parteneriat cu un vendor de program MM (revânzare), fie nivelul de autoservire pentru angajatorii „speriați de ITM”, ca sursă de clienți.
- **NO-GO pe A:** <2 pre-vânzări după ≥15 conversații, **sau** ≥2 programe MM au deja portalul. Atunci G trece în față doar dacă auditul G e puternic. Altfel, scorarea se reface cu datele reale.

---

## Anexă: unde sunt artefactele

Toate sunt sub `/home/user/Research/founder-sanatate/`:
- `scoring/`: `scoring.py` (sursa notelor), `scoring.csv`, `scoring_table.md`, `sensitivity.md`, `weights.json`.
- `board/`: `brief.md`, `prompt_*.md` (exact ce a primit fiecare membru), `offers.md`, `monopoly.md`, `product.md`, `board.md` (rezumatul).
- `competitors.csv`, `competitors.md`.
- `panels/A`, `G`, `B` (prima ofertă) și `panels/A2`, `G2` (oferta refăcută, aceleași cărți): `customer.json`, `pitch.md` (și `pitch-v1.md`), `personas.json`, `briefs/`, `answers/`, `raw/`, `results.md`, `results.json`. Plus `run_panel.sh` și `uniform_suffix.txt`.
- `pricing/`: `*-curve.md` (ieșirile Van Westendorp), `pricing.md`.
- `cfo/`: `*_numbers*.json`, `*_cfo*.md`, `*.out.json`, `combine_36m.py`, `*_36m.md`, `cfo.md`, `cfo-sources.md`.
- `plan/A`, `plan/G`: `idea.md`, `offer.md`, `summary.md`, `business-plan.md` (generat de `compile.py`) și `one-pager.md` (doar A). `plan/A_panel_v2` și `plan/G_panel_v1` sunt verificările de robustețe ale verdictului.
