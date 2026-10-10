# Proiect STEP: sănătate predictivă (cercetare + inovare)

**Ce e documentul:** ideile de sănătate predictivă din repo, rearanjate ca proiect pentru apelul STEP PR Nord-Vest (PRNV/2026/961/1 sau o fereastră STEP ulterioară), cu lista a tot ce îți trebuie ca să depui. **Nu judecă dacă e realist pentru tine**, așa cum ai cerut.
**Surse din repo:**
- `research_notes/Oportunități software în sănătatea predictivă/` (analiza laterală O1–O26, analiza founder, notele de știință și reglementare);
- `reports/Oportunități software în sănătatea predictivă.md`;
- regulile apelului din `research_notes/Apel STEP Nord Vest oportunități/` (branch `claude/amazing-turing-nucje7`).

Regulile apelului vin din rezumate de căutare și din transcrierea ta, iar Corrigendum nr. 2 (8.10.2026) le-a modificat. **Totul trebuie recitit în Ghidul consolidat** înainte de depunere.
**Data:** 10 octombrie 2026.

---

## 1. Cum intră sănătatea predictivă în STEP

- **Sectorul STEP:** tehnologii **digitale și deep tech** (AI, date, cloud securizat), aplicate în sănătate. Încadrarea la biotehnologie e mai slabă pentru software, așa că încadrarea principală rămâne cea digitală.
- **Condiția (a), element inovator cu potențial economic:** modele predictive pe date longitudinale românești, plus **bucla închisă**: semnalul ajunge la o acțiune măsurată. Dovezile spun că exact asta lipsește. În EAGLE, doar 49,6% dintre pacienții semnalați de AI au făcut ecografia. În ACCESS, testul în aceeași vizită a dus finalizarea de la 22% la 100%. În PRISMATIC, stratificarea fără acțiune a crescut internările.
- **Condiția (b), reducerea dependențelor strategice:** date de sănătate procesate în UE, în mediu securizat, compatibile EHDS (FHIR/IPS), fără să depindă de platforme și API-uri din afara UE.
- **Liniile de ajutor și ce acoperă fiecare:**

| Linia | Ce plătește | Intensitate |
|---|---|---|
| Art. 25: cercetare-dezvoltare | personal de cercetare propriu, cercetare contractată (spital, universitate), date, calcul | cercetare industrială 80%, dezvoltare experimentală 60%, studii de fezabilitate 70% |
| Art. 14: investiție regională | infrastructura de producție a serviciului: centru de date securizat, echipamente, licențe, software ca activ | ~40% bază în NV + bonusuri, ~60–70% (de verificat) |
| Art. 28: inovare IMM | consultanță de inovare, certificare, studiu de piață, brevete/mărci | 100% până la 220.000 EUR (brevetele 50%) |
| De minimis | consultanță la scriere/implementare, proiectare, publicitate | 100%, max. 300.000 EUR; publicitate max. 15.000 lei fără TVA |

---

## 2. Trei concepte de proiect

### Conceptul A (recomandat ca nucleu): **PREVENT-NV, platformă regională de prevenție predictivă cu buclă închisă**

**Ce e:** o platformă care adună într-un dosar longitudinal semnalele de prevenție care există deja și le duce până la o acțiune făcută. Semnalele sunt:
- rezultatele de laborator în afara intervalului (O3);
- examenele periodice de medicina muncii (O2, O17, O23);
- invitațiile de screening (O1, colorectal ROCCAS 4 NV; O18);
- consultațiile CNAS de prevenție 40+/60+ (O8);
- notificările de la dispozitive purtabile (O4).

Peste dosar rulează modele predictive pentru două întrebări:
1. Cine are risc crescut (modele clinice validate și modele ML noi).
2. Cine nu va închide bucla fără intervenție (O25).

Modulul clinic se certifică MDR clasa IIa în proiect.

**Pachetele de cercetare (art. 25):**

| WP | Întrebarea | TRL | Linia |
|---|---|---|---|
| WP1 · Dosarul longitudinal | Cum construiești un dosar FHIR/IPS (EHDS) din surse eterogene românești (exporturi de laborator, PDF-uri, fișe MM, SIUI), cu calitatea datelor măsurată? | 3→7 | cercetare industrială |
| WP2 · Extragere verificabilă | Extragerea valorilor și recomandărilor din PDF-uri medicale în română și maghiară, cu sursa citată și validare umană (O21) | 3→7 | cercetare industrială |
| WP3 · Risc predictiv | Modele de risc cardiometabolic și pentru cancer colorectal pe date longitudinale românești, comparate cu scorurile validate (SCORE2, FINDRISC), cu calibrare locală | 3→6 | cercetare industrială |
| WP4 · Predicția închiderii buclei | Pe cine suni primul? Model testat contra „reminder pentru toți” într-un studiu controlat (nedovedit în literatură, deci cercetare reală) | 3→7 | cercetare industrială |
| WP5 · Monitorizarea performanței AI | Monitor local de drift și performanță pentru AI-ul marcat CE folosit de rețelele de imagistică și screening (O20) | 4→7 | dezvoltare experimentală |
| WP6 · Pilot și certificare | Pilot în 2–3 clinici, laboratoare și cabinete MM din NV, plus dosarul tehnic MDR clasa IIa pentru modulul WP3 | 5→8 | dezvoltare experimentală + art. 28 (certificare) |

**Investiția (art. 14):**
- mediu securizat de procesare a datelor de sănătate în Nord-Vest (servere, stocare criptată, HSM, redundanță, sală de servere sau colocare);
- licențe și know-how (terminologii clinice, de exemplu LOINC/SNOMED, unde e cazul; instrumente de calitate), cumpărate de la terți nelegați la preț de piață;
- opțional: **unități mobile de prevenție** pentru „ziua de prevenție” la locul de muncă (O9). Fiecare are ECG, spirometru, audiometru și analizor point-of-care. Asta dă proiectului o componentă fizică clară de „producție” a serviciului.

**Rezultate și indicatori:**
- produs: platforma, modulul certificat, monitorul AI;
- locuri de muncă: 6–8 ENI;
- venituri din activitatea sprijinită în primii 3 ani de durabilitate (abonamente de la clinici, laboratoare, cabinete MM, angajatori, asigurători);
- spillover: benchmark deschis de documente medicale RO/HU și profil FHIR românesc publicat.

**Schiță de buget (estimare, de refăcut cu oferte):**

| Linie | Eligibil | Grant | Cofinanțare |
|---|---:|---:|---:|
| Art. 25 cercetare industrială (WP1–WP4) | 2.600.000 | 2.080.000 | 520.000 |
| Art. 25 dezvoltare experimentală (WP5–WP6) | 1.400.000 | 840.000 | 560.000 |
| Art. 14 infrastructură date + unități mobile + licențe | 4.600.000 | ~3.000.000 | ~1.600.000 |
| Art. 28 certificare MDR, consultanță inovare, studiu de piață, IP | 220.000 | 220.000 | 0 |
| De minimis: consultanță, publicitate | 300.000 | 300.000 | 0 |
| **Total** | **~9.100.000** | **~6.400.000** | **~2.700.000** |

### Conceptul B: **Prevenție predictivă la locul de muncă** (axa medicina muncii)

- **Ce e:** arhiva longitudinală de expunere profesională (O17) și examenele periodice MM (O2) devin o bază de date care prezice riscul de boală profesională și de afecțiuni cronice pe grupe de expunere (zgomot, pulberi, ture de noapte). E legată de o „zi de prevenție” cu teste făcute pe loc (O9, O11) și de predarea la medicul de familie (O23).
- **Cercetare:** modele de risc pe expunere + rezultate de examen; extragerea din fișe și documente; studiul efectului (închiderea recomandărilor la 90 de zile).
- **Investiție (art. 14):** flotă de unități mobile de medicina muncii și prevenție, plus centrul de date.
- **Plătitorii și scrisorile:** angajatorii mari din NV (fabrici din Oradea, Cluj, Satu Mare), cabinetele MM, asigurătorii privați.
- **Diferența față de A:** mai îngust, mai ușor de explicat, cu plătitor clar (angajatorul). Predicția e mai puțin „de vârf”.

### Conceptul C: **Centru regional de telemonitorizare cardiovasculară**

- **Ce e:** model TIM-HF2 (centru cu medic și asistentă 24/7). Insuficiența cardiacă și fibrilația atrială sunt urmărite de la distanță cu dispozitive CE cumpărate, cu protocol de escaladare și modele predictive de decompensare. Include navigatorul pentru alertele de la ceas (O4).
- **Cercetare:** predicția decompensării din date de acasă (greutate, tensiune, ritm); triajul alertelor; un studiu pilot cu un spital județean.
- **Investiție (art. 14):** centrul de telemonitorizare (spațiu, stații, sistem, dispozitive pentru pacienți în pilot).
- **Diferența:** cea mai puternică dovadă clinică dintre cele trei (TIM-HF2: mortalitate HR ~0,70). Cere însă un partener spital sau cardiologie și personal medical în proiect.

---

## 3. De ce ai nevoie: lista completă

### 3.1 Solicitantul (criteriile ESO)
- [ ] **Societate pe Legea 31/1990, cu sediul social în Nord-Vest** cel târziu la prima plată (ESO1).
- [ ] **Cel puțin un an fiscal încheiat, cu profit din exploatare > 0** în unul dintre ultimii doi ani și fără suspendare în anul depunerii (ESO2).
- [ ] **Cel puțin 1 salariat mediu** în anul anterior (ESO4).
- [ ] **Capacitate de cofinanțare dovedită** (ESO3): ~2,5–3 mil. EUR la conceptul A, plus bani pentru TVA și pentru perioada până vin rambursările. Prefinanțarea e de până la 40%, cu garanție bancară.
- [ ] **Fără situații de excludere** (ESO5); **drept de folosință asupra spațiului** unde se face investiția (ESO6).
- [ ] **Verificarea cumulului de ajutoare.** Ajutorul DR-36 primit de ILLUSTRUS intră la plafonul de minimis de 300.000 EUR pe 3 ani? Ai voie, prin planul DR-36, să fii solicitant sau partener (întrebare la GAL/OJFIR)?
- Dacă ILLUSTRUS nu îndeplinește criteriile: **vehicul nou sau partener solicitant** (clinică, rețea, firmă IT cu bilanț), iar ILLUSTRUS intră ca furnizor sau acționar.

### 3.2 Echipa (criteriul 2.1, 12 puncte)
- [ ] **Director de proiect** cu ≥5 ani experiență.
- [ ] **Membri** cu experiență de 5 și 3 ani.
- [ ] **Management operațional** cu 5 ani experiență.
- [ ] **Cineva care a implementat ≥2 proiecte UE** cu granturi cumulate de cel puțin 100.000 EUR (2 puncte).
- [ ] **Personal de cercetare propriu**, cerut de ghid: 3–4 cercetători sau ingineri ML, 2 dezvoltatori, 1 specialist date clinice și FHIR, 1 responsabil de reglementare (MDR/QMS).
- [ ] **Medic coordonator științific**: medic de familie, medicina muncii sau cardiolog, după concept.
- [ ] CV-uri și dovezi de experiență pentru toți.

### 3.3 Parteneri și acorduri
- [ ] **Partener clinic** pentru date și pilot: spital județean, clinică privată, laborator independent (de exemplu Humanamed Oradea), cabinete MM (Medimun, Carimed). La conceptul C, un spital cu cardiologie.
- [ ] **Partener de cercetare** pentru cercetarea contractată și raport: Universitatea din Oradea (Facultatea de Medicină + CNCG-CTT), UMF Cluj, UTCN, UBB.
- [ ] **Acorduri de acces la date** (DPA, acord de cercetare), **avizul comisiei de etică** pentru studiile WP3/WP4/WP6 și **DPIA** (evaluare de impact GDPR).
- [ ] Pentru WP4 și orice profilare pe date de sănătate: **consimțământ explicit sau bază legală expresă** (Legea 190/2018 art. 3).

### 3.4 Documentele dosarului
- [ ] **Cererea de finanțare** în MySMIS2021+ (cont, semnătură electronică calificată).
- [ ] **Planul de afaceri**, cu indicatori cantitativi și angajament de diseminare.
- [ ] **Studiul de piață**: clinici, laboratoare, cabinete MM, angajatori și asigurători din NV și din UE.
- [ ] **Macheta financiară** (Anexa III.5, versiunea corectată după Corrigendum 2).
- [ ] **Raportul unui centru de transfer tehnologic sau al unui cercetător științific gradul I** despre inovație, TRL și încadrarea STEP (criteriile 1.2, 5.1, 5.2). Fără el, 5.1/5.2 pot fi 0, adică respingere.
- [ ] **Raportul unui expert contabil CECCAR** (capacitate financiară, maturizarea ideii pentru criteriul 3).
- [ ] **Scrisori de intenție**:
  - 3–5 clienți din NV;
  - 1–2 parteneri din alte țări UE (Ungaria, Polonia) pentru criteriul 4.3 (scalare internațională).
- [ ] **Oferte de preț** pentru fiecare echipament și licență (de regulă 3) și centralizatorul de costuri.
- [ ] **Deviz general HG 907/2016**, dacă ai lucrări (amenajare sală de servere sau spațiu de telemonitorizare).
- [ ] **Declarația Unică** (Anexa III.1, versiunea nouă).
- [ ] **Declarațiile de ajutor de stat / de minimis** primite anterior.

### 3.5 Reglementare (de planificat în proiect, nu înainte de depunere)
- [ ] **MDR:** modulul care dă risc individual pacientului = dispozitiv medical, foarte probabil clasa IIa (Regula 11). Îți trebuie:
  - QMS ISO 13485;
  - ciclu de viață software IEC 62304;
  - management de risc ISO 14971;
  - evaluare clinică;
  - organism notificat.
  
  Repo-ul estimează ~32–110 mii EUR și 9–18 luni; intră pe art. 28 și art. 25.
- [ ] **AI Act:** AI-ul din dispozitive medicale e cu risc ridicat din 2 august 2028 (după Digital Omnibus). Planifică documentația tehnică și supravegherea umană.
- [ ] **EHDS:** dacă platforma e „sistem EHR”, se aplică cerințe din 2029 (rezumatul pacientului) și 2031 (analize de laborator).
- [ ] **NIS2 / securitate:** ISO 27001 sau echivalent pentru infrastructura de date (bugetat în art. 14 sau art. 28).
- [ ] **GDPR:** date de sănătate (art. 9), transferuri doar în UE, DPO.

### 3.6 Calendar
- **Fereastra actuală:** 961 se închide pe **02.11.2026, ora 10:00**. Ai nevoie de solicitant, echipă, raport CTT, raport contabil, machetă, oferte și scrisori în 3 săptămâni.
- **Alternativa:** o fereastră STEP ulterioară în Nord-Vest. Întreabă ADR NV la regio@nord-vest.ro.
- **Implementare** până la 31.12.2029, apoi 3 ani de durabilitate (IMM) cu raport anual.

### 3.7 Întrebări de pus în scris la ADR Nord-Vest înainte de orice
1. O platformă de prevenție predictivă cu AI pe date de sănătate se încadrează la „tehnologii digitale critice” STEP?
2. Mediul securizat de procesare a datelor (servere, licențe, software) și unitățile mobile de prevenție sunt acceptate ca investiție inițială pe art. 14?
3. Costurile de certificare MDR sunt eligibile pe art. 28 sau art. 25?
4. Există o fereastră STEP ulterioară în 2027?

---

## 4. Ce aș alege dintre cele trei

- **Conceptul A** are cea mai bună poveste STEP: AI + date + EHDS + reducerea dependenței. Folosește cele mai multe idei din repo și e cel mai aproape de competențele tale (date, FHIR, extragere, platformă).
- **Conceptul B** e mai ușor de explicat și are plătitorul cel mai clar.
- **Conceptul C** are cea mai puternică dovadă clinică, dar depinde de un spital.

Variantă combinată: **A, cu B ca prim domeniu de pilot** (medicina muncii + laboratoare din Bihor). Domeniul e îngust, datele sunt accesibile prin cabinetele MM, iar platforma rămâne generală pentru extinderea ulterioară.
