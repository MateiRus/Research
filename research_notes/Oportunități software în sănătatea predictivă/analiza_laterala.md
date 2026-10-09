# Analiză laterală: oportunități software în trecerea de la îngrijire reactivă la sănătate predictivă și preventivă

**Data:** 9 octombrie 2026
**Statut:** **ideație și inferență, nu dovezi.** Tot ce urmează sunt idei generate cu tehnici de gândire laterală. Faptele pe care se sprijină vin din notele de cercetare din acest dosar și sunt citate ca atare. Nu am făcut cercetare web nouă.

---

## 0. Cum să citești documentul

**Ce conține.** Patru tehnici de gândire laterală aplicate pe notele de cercetare:
- **A. Concept fan** (de Bono): urcăm de la soluția obișnuită la scopul pe care îl servește, apoi coborâm la alte soluții.
- **B. Inversarea presupunerilor**: răsturnăm presupunerile „playbook-ului” standard și căutăm unde răsturnarea e deja adevărată.
- **C. Analogia forțată**: mutăm mecanisme din domenii îndepărtate (biologic, operațional, social).
- **D. Random stimulus** (lot scurt de control): verificăm dacă primele trei tehnici au convers pentru că ideea e bună sau pentru că am intrat într-un făgaș.
- **E.** Lista de 25 de oportunități concrete.
- **F.** Meta-tiparul comun și clasamentul preliminar (top 10, supraviețuitorii slabi, fundăturile).

**Despre rutare.** Routerul `lateral` recomandă o singură tehnică pe trecere. Cererea a fost explicit pentru trei tehnici plus una opțională, așa că le-am rulat ca treceri separate. Fiecare are pașii și mecanismele ei de onestitate (ramuri tăiate, inversări moarte, analogii abandonate, stimuli abandonați) și propriul meta-tipar. Meta-tiparul comun e la final, în secțiunea F.

**Cum citez.** Formatul este `(fișier §secțiune ← sursa citată acolo)`. Abrevieri:

| Abreviere | Fișier |
|---|---|
| ȘTI | `stiinta_predictie_preventie.md` |
| MON | `monitorizare_date_coordonare.md` |
| RO | `romania_piata.md` |
| REG | `reglementare_ue_ro.md` |
| EMG | `emergente_si_platitori.md` |
| B2B | `competitori_b2b_infrastructura.md` |
| CONS | `competitori_consumer.md` |
| CEE | `cee_nordice.md` |
| L3, L4 | `lateral/03-random-stimulus.md`, `lateral/04-industrii-hot-servicii.md` |
| REC | `reports/Recepționist AI telefonic București.md` |

**Atenție la calitatea surselor.** Notele spun singure că aproape toate faptele vin din rezumate ale motorului de căutare (snippet), nu din pagini citite integral, iar o parte vin din cunoștințele de fond ale cercetătorului (marcate BK sau PK). Citările de aici moștenesc aceeași limită. Unde fac un calcul propriu, scriu „calculul meu”.

**Fondatorul (constrângerile folosite peste tot).**
- SRL în Bihor, rețele în Oradea și București.
- Python, SQL, PL/SQL, Oracle APEX, backend web, arhitectură de date, AI/ML, API-uri LLM, agenți AI, n8n.
- ~25.000 EUR capital și 10–12 ore pe săptămână la început.
- Poate merge fizic la clienți. Preferă B2B SaaS cu venit recurent.
- Acces inițial limitat la medici, dosare și seturi de date. E dispus să facă parteneriate cu organizații medicale, dacă există un motiv comercial.
- Vrea un prim produs îngust care aduce bani și poate crește credibil spre o platformă predictivă/preventivă, fără să construiască sau să valideze clinic un model fundațional propriu.

**Categoriile de reglementare** folosite în lista de oportunități (după REG §8):
1. **Administrativ / flux de lucru**: programare, rechemare pe date stabilite de om, raportare, comunicare. Povară mică.
2. **Wellness**: stil de viață, fără revendicări medicale. Povară mică spre medie.
3. **Suport decizional clinic, partea care nu e dispozitiv**: căutare simplă, afișare fără interpretare, tablouri la nivel de populație. REG §8 avertizează că în UE această categorie „se prăbușește” aproape mereu în categoria 4.
4. **Dispozitiv medical reglementat** (MDSW, de regulă clasa IIa sau mai sus după Regula 11): orice informație despre un pacient anume folosită pentru decizii de diagnostic sau tratament, scoruri de risc individuale, alerte RPM, triaj. REG §2 estimează 32.000–110.000 EUR și 9–18 luni pentru clasa IIa, fără investigații clinice (estimare de pe blogul unui furnizor).

---

## Pe scurt (ce a ieșit)

- **Toate cele patru tehnici au ajuns la același loc:** valoarea rară nu e predicția, ci **un proprietar plătit al „buclei deschise”**: drumul de la un semnal care există deja (rezultat, recomandare, notificare, invitație) până la o acțiune făcută și confirmată. Proprietarul stă pe un contact care există deja și e plătit din bugetul cuiva care are deja o obligație. Dovezile din note susțin direcția:
  - doar 49,6% dintre pacienții semnalați de AI-ECG au făcut ecografia (EAGLE);
  - finalizarea examenului a urcat de la 22% la 100% când testul s-a făcut în aceeași vizită (ACCESS);
  - stratificarea riscului fără acțiune a crescut internările (PRISMATIC);
  - telemonitorizarea a mers doar cu un centru dotat cu oameni (TIM-HF2 față de Tele-HF/BEAT-HF).
- **În primul produs, „predicția” e calendarul:** reguli deterministe stabilite de medic sau de program (termene, intervale, eligibilitate pe vârstă). Asta ține produsul în categoria 1 (administrativ). Predicția cu ML vine în etapa a doua, pe o țintă operațională: cine nu-și va închide bucla.
- **Cel mai bine plasat plătitor pentru fondator** e unul care are deja o obligație legală sau un buget: furnizorul de medicina muncii (examene periodice obligatorii), proiectul de screening finanțat UE (ROCCAS 4 Nord-Vest, inclusiv Bihor, 2025–2029), angajatorul (plafonul de 400 EUR pe an), vendorul de software care trebuie să devină conform EHDS (2029/2031). Pacientul și spitalul public sunt cei mai slabi plătitori.
- **Axa nouă, venită din random stimulus:** *dez-implementarea*. Un produs care scoate testele fără valoare din pachetele de check-up, plătit de cine plătește daunele (asigurătorii au avut daune +~30% în T1 2025).
- **Primele trei din clasamentul preliminar:** (1) registrul recomandărilor deschise după examenul de medicina muncii, (2) navigatorul „FIT pozitiv → colonoscopie făcută” pentru ROCCAS 4 NV, (3) „ziua de prevenție” la locul de muncă, ca a doua treaptă a primului.
- **Fundăturile au un motiv comun:** cer fie un plătitor nou (consumatorul român, CNAS pentru digital), fie o revendicare clinică certificată (MDR IIa+).

---

## A. Concept fan

### Pasul 1. Ținta

Soluția curentă, adică playbook-ul standard: **„un startup de sănătate predictivă construiește sau licențiază un model care prezice riscul individual de boală din date (analize, wearables, dosar) și îl vinde ca aplicație pentru pacient sau ca instrument clinic pentru spital.”** E o țintă validă: există ceva concret de pe care să urcăm.

### Pasul 2. Urcarea

**Urcarea 1: „Un model de risc individual e un mod de a face… ce?”**
E un mod de a **transforma un semnal timpuriu despre o persoană într-o acțiune făcută la timp**: un test de confirmare, o consultație, o schimbare de tratament. Predicția acoperă doar jumătatea „semnal”. Notele spun că beneficiul apare numai când predicția e legată de (a) o acțiune specifică și eficientă, (b) un flux cu oameni care acționează și (c) finalizarea urmăririi (ȘTI KQ1, Inferences).
→ Direcția de nivel 1: **a închide bucla semnal → acțiune → confirmare.**

**Urcarea 2: „A închide bucla semnal → acțiune e un mod de a face… ce?”**
E un mod de a **muta efortul și banii de la evenimente târzii și scumpe** (internare, cancer în stadiu avansat, inaptitudine de muncă) **la acțiuni timpurii și ieftine**, într-un fel pe care cineva acceptă să-l plătească.
→ Direcția de nivel 2: **a muta cheltuiala de la târziu la devreme, pe banii cuiva care are deja motiv să plătească.**

Mă opresc aici. O a treia urcare ar da „oameni mai sănătoși” sau „costuri mai mici pentru sistem”, adică nimic din care să se mai poată coborî la ceva concret.

### Pasul 3. Evantaiul

**Nivelul 1: alte moduri de a închide bucla semnal → acțiune**

- **A1. A deține urmărirea (follow-through).** Nu un semnal mai bun, ci garanția că semnalul existent ajunge la acțiune. În EAGLE, chiar cu alertă, doar 49,6% dintre pacienții pozitivi la AI-ECG au făcut ecografia (ȘTI KQ2 ← TCTMD). În TREWS, beneficiul a depins de confirmarea alertei în 3 ore (ȘTI KQ1 ← Scientific American).
- **A2. A muta testul unde omul e deja (punctul de contact).** În ACCESS, finalizarea examenului de retină a fost 100% când testul s-a făcut în aceeași vizită, față de 22% cu trimitere. Urmarea după un rezultat anormal a fost 64% față de 22% (ȘTI KQ1 ← UW Ophthalmology). Unde nu există predare între actori, bucla nu are pe unde să se rupă.
- **A3. A filtra zgomotul ca omul să mai acționeze.** Praguri, eliminarea dublurilor, un buget de alerte, o echipă desemnată. TIM-HF2, cu centru 24/7 cu medici și asistente, a redus mortalitatea (HR ~0,70), iar Tele-HF și BEAT-HF, fără bucla aceasta de răspuns, n-au avut efect (MON §2 ← Koehler, Lancet 2018; Chaudhry, NEJM 2010; Ong, JAMA IM 2016). Oboseala de alerte reduce escaladarea (MON §2 ← BMC Nursing 2026).
- **A4. Un model mai precis.** **Tăiată.** E soluția originală cu altă haină. Chiar și în dovezi, precizia în plus aduce puțin: scorul poligenic adaugă ~0,02 la statistica C, iar cu QRISK2 AUROC-ul a fost 0,635 față de 0,623 (ȘTI KQ1 ← JAMA 2020; Brunel).

**Nivelul 2: alte moduri de a muta cheltuiala de la târziu la devreme, pe banii cuiva care are deja motiv**

- **B1. A călări o obligație care există deja** (lege, contract, termen):
  - examenele periodice de medicina muncii (Legea 319/2006, HG 355/2007) (RO §5);
  - folosirea e-SănătateaMea pentru programări, obligatorie din T4 2026 pentru furnizorii cu contract CNAS (RO §4);
  - EHDS, cu termene în 2029 și 2031 (MON §5);
  - proiectele de screening finanțate UE (RO §5).
- **B2. A lipi prevenția de o relație recurentă deja plătită:**
  - abonamentul corporate, cu plafon fiscal de 400 EUR pe an (EMG Q2);
  - rechemarea stomatologică la 6 luni (L4);
  - scanarea anuală cu programare la plecare: ~75% dintre membrii Neko își plătesc anticipat scanarea următoare (CONS KQ1 ← Pulse2).
- **B3. A face vizibil în bani evenimentul târziu pentru cel care îl plătește:**
  - pentru clinică, venitul pierdut din recomandări neurmate;
  - pentru angajator, inaptitudinea și absența;
  - pentru asigurător, daunele, care au crescut cu ~30% în T1 2025 față de prime cu +12–13% (EMG Q2 ← ZF; Financial Intelligence).
- **B4. Aplicație de educație și coaching pentru consumatori.** **Evidentă și slabă.** E ce ar spune oricine. Istoria PHR-urilor (Google Health, HealthVault), lipsa plății directe de la consumatori în afara „membrilor captivi” (EMG Q2 ← Accenture/Nextgov) și cele mai slabe competențe digitale de bază din UE (31,8%, RO §8) o fac fragilă. Nu e tăiată ca variantă cosmetică, pentru că are alt mecanism, dar nu e randamentul tehnicii.

### Pasul 4. Coborârea la produse

**A1. A deține urmărirea:**
- navigator „FIT pozitiv → colonoscopie făcută” pentru ROCCAS 4 Nord-Vest (→ O1);
- registrul recomandărilor deschise din fișele de aptitudine de medicina muncii (→ O2);
- inbox de urmărire pentru rezultatele în afara intervalului de referință la laboratoarele independente (→ O3).

**A2. Punctul de contact:**
- „ziua de prevenție” la locul de muncă, cu toți actorii în același loc și aceeași zi (→ O9);
- confirmarea ECG/Holter/MAPA în aceeași vizită pentru cine vine cu o notificare de la ceas (→ O4);
- verificarea eligibilității pentru pachetul CNAS 40+ la vizita de medicina muncii, cu scrisoare către medicul de familie (→ O8, O9).

**B1. A călări o obligație:**
- componente EHDS (FHIR, rezumat IPS, jurnal de acces) pentru vendorii locali de software medical (→ O15);
- puntea e-SănătateaMea pentru furnizori mici cu contract CNAS (→ O14);
- arhiva de expunere profesională pe 40 de ani (→ O17).

**B3. Banii vizibili:**
- auditul „bani expuși” al buclelor deschise dintr-o clinică (→ O24);
- raportul de finalizare a prevenției pentru abonamentele corporate (→ O10).

### Pasul 5. Ramurile evidente

- **A3 (filtrarea zgomotului)** e pe jumătate evidentă. Apare deja în note ca „review-queue / triage workbench” pentru RPM (MON §2, Inferences). În plus, nu are plătitor în România, pentru că RPM nu e rambursat (MON §2, Gaps).
- **B2 (lipirea de o relație recurentă)** e evidentă în contextul acestui proiect: sesiunea L4 a găsit deja rechemarea stomatologică.
- **Randamentul tehnicii** e A2 (bucla mutată acolo unde omul e deja, ceea ce șterge predările) și combinația **A1 × B1**: un proprietar al urmăririi, așezat pe un contact obligatoriu care există deja.

### Pasul 6. Meta-tiparul

Fiecare ramură puternică mută valoarea **de pe semnal pe cine deține acțiunea și pe cine plătește deja**. Soluția originală (modelul mai bun) a fost cea mai slabă la ambele niveluri, iar notele o confirmă: precizia în plus aduce puțin (scorurile poligenice), iar stratificarea fără acțiune poate crește utilizarea (PRISMATIC: +~1% internări de urgență, +~3% prezentări la urgențe, +~5% vizite ambulatorii; ȘTI KQ1 ← PMC6820297).

A doua observație: în ramurile puternice, „predicția” devine **deterministă**. Ea înseamnă date și reguli: intervale stabilite de program sau de medic, termene pe fiecare recomandare. **Calendarul e cel mai ieftin predictor validat.** Asta ține produsul în categoria 1. REG §8 spune explicit că „îi amintește pacientului data de control stabilită de medic” e administrativ, iar „identifică pacienții cu risc mare care trebuie văzuți mai devreme” e dispozitiv.

### Pasul 7. Clasament onest al ramurilor

1. **A1 × B1**: proprietarul urmăririi pe un contact obligatoriu. Cea mai puternică, pentru că satisface ambele niveluri deodată.
2. **A2**: punctul de contact. Puternică, are cea mai bună dovadă (ACCESS), dar depinde de parteneri care să fie fizic în același loc.
3. **B3**: banii vizibili. E mai degrabă o unealtă de vânzare decât un produs.

Slabe: A3 (fără plătitor pentru timpul de revizie în România) și B4 (evidentă și fragilă). Evantaiul nu a eșuat: ambele urcări au dat direcții din care s-a putut coborî la concret.

---
## B. Inversarea presupunerilor

**Ținta:** playbook-ul standard al unui startup de sănătate predictivă.

**De ce funcționează tehnica.** Fiecare presupunere de mai jos pare un fapt, nu o alegere. Răsturnarea e doar un truc de dezbatere până la întrebarea care contează: **unde e opusul deja adevărat, și cine câștigă din el azi?** Răsturnările care au un răspuns cinstit la întrebarea asta arată direcțiile pe care planul obișnuit nu le-a văzut. Cele fără răspuns rămân pe hartă, marcate moarte.

### 1. Valoarea: „Valoarea e în modelul de predicție.”

→ **Răsturnare:** valoarea e în ce se întâmplă **după** semnal. Predicția e ieftină sau există deja.

→ **Unde e deja adevărat:**
- **EAGLE:** după un AI-ECG pozitiv, doar 49,6% au făcut ecografia (ȘTI KQ2 ← TCTMD).
- **ACCESS:** efectul a venit din închiderea golului de îngrijire, nu din acuratețe (ȘTI KQ1 ← UW Ophthalmology).
- **TREWS:** beneficiul e legat de confirmarea alertei în 3 ore (ȘTI KQ1 ← Scientific American).
- **TIM-HF2** a mers, Tele-HF și BEAT-HF nu (MON §2).
- **PRISMATIC:** stratificarea riscului singură a crescut utilizarea (ȘTI KQ1 ← PMC6820297).

Cine câștigă azi din opus:
- Lifen, cu rutarea documentelor: profitabil la peste 20 mil. EUR ARR (B2B ← FrenchWeb);
- Accurx, cu mesaje: 98% dintre cabinetele din Anglia (B2B ← G-Cloud);
- Lighthouse 360 și Solutionreach, cu rechemări: 199–329 USD pe locație pe lună (B2B Q4 ← Spendbase, SoftwarePundit).

În România, startup-urile noi vând front-office (MedOcean, Callio), nu predicție (RO §6).

**Supraviețuiește puternic.**

### 2. Cumpărătorul: „Plătește pacientul sau spitalul.”

→ **Răsturnare:** plătește cine are **deja o obligație sau un buget** pentru acea persoană: angajatorul și furnizorul lui de medicina muncii, clinica ce vinde abonamente corporate, proiectul de screening finanțat UE, vendorul de software care trebuie să devină conform.

→ **Unde e deja adevărat:**
- **Medicina muncii** e obligatorie și se plătește per angajat: 80 lei pe an, 110 lei pentru șoferi (RO §5 ← Medworks). Medexpert din Cluj declară peste 15.000 de angajați evaluați pe an și peste 500 de firme (RO §5 ← Medexpert).
- **Abonamentele corporate** au plafon fiscal de 400 EUR pe an. Cifra de 2,2 milioane de beneficiari vine dintr-o sursă slabă, un advertorial (EMG Q2 ← Romania Insider; Bursa).
- **ROCCAS 4 NV** are un buget de 35,6 mil. lei (RO §5 ← ARPS).
- **În Finlanda**, obligația de conectare la Kanta a creat o piață de intermediari („joint connection”) (CEE Q4 ← Kanta).
- **Docplanner** vinde medicilor, nu pacienților (CEE Q1).

Contra pacientului ca plătitor:
- doar ~10% dintre români își fac programări online sau își accesează dosarul (RO §8 ← OECD 2025);
- PHR-urile au eșuat (MON §5);
- Aware a intrat în insolvență în iunie 2026 (CONS ← Apotheke Adhoc).

Contra spitalului:
- achiziții publice lente, iar Comarch și-a vândut partea de HIS (CEE Q1 ← ITwiz);
- atacul ransomware asupra Hipocrate (RO §2 ← DNSC).

**Supraviețuiește puternic.**

### 3. Datele: „Datele trebuie colectate din nou (senzori noi, aplicații noi).”

→ **Răsturnare:** datele **există deja, dar zac nefolosite**: PDF-uri de analize, fișe de aptitudine, liste de pacienți ai medicului de familie, rezultate FIT, planuri de tratament.

→ **Unde e deja adevărat:**
- Levels oferă „încărcări nelimitate ale analizelor vechi” (CONS KQ3 ← Levels support).
- Aeon a cumpărat de la Aware tocmai integrările cu laboratoarele și rețeaua de recoltare (CONS ← IT Brief UK).
- Stiva transversală din ȘTI KQ4 pornește de la ingestia și maparea datelor existente.

→ **Frecarea:**
- La date ajungi doar ca persoană împuternicită (processor) a unei clinici, câte o clinică pe rând (REG §1).
- Vendorii locali de software de cabinet nu au API-uri publice (RO §2).
- e-SănătateaMea nu are un API public pentru terți (RO §4).
- Consultațiile private plătite din buzunar nu ajung în dosarul național (RO §4, Inferences).

**Supraviețuiește, cu frecare.** Datele există, dar le citești din CSV și PDF, prin clinică.

### 4. Reglementarea: „Reglementarea e bariera principală.”

→ **Răsturnare:** reglementarea e **motorul cererii**. Termenele creează cumpărători.

→ **Unde e deja adevărat:**
- **Finlanda:** obligația de conectare plus lanțul de certificare a creat piață pentru vendori și intermediari (CEE Q4).
- **EHDS:** termene datate pentru „sistemele EHR”, cu autocertificare, componentă de interoperabilitate și componentă de jurnalizare. Grupa 1 (rezumat pacient, rețete) pe 26.03.2029, grupa 2 (analize, imagini, externări) pe 26.03.2031 (MON §5; REG §4).
- **e-SănătateaMea** e obligatoriu pentru programări din T4 2026 (RO §4 ← medic24).
- **NIS2** impune clinicilor cerințe de securitate pentru furnizori (REG §5).
- **AI Act Art. 50** se aplică din 2 august 2026 (REG §3).
- **Noua directivă de răspundere pentru produse (PLD)** se aplică din 9 decembrie 2026 (REG §7).

→ **Unde e fals:** pentru tot ce e clinic. Regula 11 MDR împinge software-ul de decizie în clasa IIa, cu 32.000–110.000 EUR și 9–18 luni (REG §2 ← meddeviceguide). Platform24 a fost pus sub supraveghere pentru că nu era înregistrat ca dispozitiv (CEE Q3 ← SVT).

**Supraviețuiește pe jumătate.** Răsturnarea taie spațiul în două: motor pentru partea administrativă și de interoperabilitate, barieră reală pentru partea clinică.

### 5. Produsul: „Produsul trebuie să fie clinic (să diagnosticheze, să recomande).”

→ **Răsturnare:** produsul vandabil e **administrativ**, iar partea „preventivă” se livrează prin logistică: calendar, invitație, urmărire, raport.

→ **Unde e deja adevărat:**
- Povara administrativului e mică, iar suportul decizional se prăbușește în IIa (REG §8).
- Remindere simple cresc prezența la programări (RR ~1,14; MON §6 ← Cochrane 2013).
- ACCESS e un efect de logistică, nu de diagnostic.
- În România, startup-urile se strâng pe front-office (RO §6).
- Tandem a intrat în IIa abia când a crescut spre codare și suport decizional (B2B ← TheNextWeb).

**Supraviețuiește puternic.**

### 6. Canalul: „Pacientul folosește o aplicație.”

→ **Răsturnare:** canalul e **telefonul, WhatsApp-ul și un om**. Aplicația e opțională.

→ **Unde e deja adevărat:**
- ~10% online și 31,8% competențe digitale de bază (RO §8).
- Organizațiile de pacienți cer păstrarea programării telefonice (RO §4).
- 39,6% dintre cei care sună pentru o programare nouă închid fără ea. Rata de programare e 83,8% cu operatori empatici, față de 21,9% cu operatori reci (RO §3 ← AGERPRES/MedOcean).

**Supraviețuiește, dar nu e nouă.** Raportul REC și sesiunea L4 au găsit-o deja. O păstrez ca să fie harta completă.

### 7. Secvența: „Întâi construiești platforma sau modelul, apoi vinzi.”

→ **Răsturnare:** întâi faci bucla **manual, ca serviciu, pentru un plătitor**, apoi o automatizezi. Modelul vine ultimul, din datele adunate cu consimțământ.

→ **Unde e deja adevărat:**
- **TIM-HF2** și centrele germane de telemedicină (TMZ) sunt centre cu oameni; serviciul e rambursat prin coduri EBM în afara bugetului cabinetului (MON §2 ← KBV).
- **Withings Cardio Check-Up** e o revizie umană ambalată: 4 revizii de cardiolog în 24 de ore, incluse în 99,95 EUR pe an (CONS ← Withings PR).
- **Cera** e un serviciu cu software, nu SaaS pur (B2B).
- **REG §8** descrie exact secvența: produs administrativ acum, consimțământ și parteneriate clinice acumulate, produs predictiv cronometrat pentru 2028–2029.

**Supraviețuiește.**

### 8. „Un scor de risc individual folosit de medic e dispozitiv medical reglementat.”

→ **Răsturnare:** un scor publicat și transparent (SCORE2, FINDRISC) poate fi pus în fluxul medicului fără certificare.

→ **Unde e adevărat:** în SUA, prin excepția pentru suportul decizional clinic transparent (520(o)(1)(E)), menționată în REG §2. **În UE nu există echivalent.** „E doar o formulă publicată” nu e o excepție recunoscută, iar un scor validat cere tot evaluare clinică (REG §2 tabel; REG §8 ← MDCG 2020-1).

**Moartă (în UE).** Presupunerea originală trece neatinsă prin inversare și e aproape lege. Concluzia: primul produs nu trebuie să cheltuiască efort aici.

### Dezvoltarea supraviețuitorilor

- **1 + 5 + 2 → „operatorul buclei deschise pe un contact obligatoriu”.** Un produs care deține recomandările rămase deschise după un contact care are loc oricum (examen periodic, screening, analize). Termenele le stabilește medicul sau programul; produsul doar le urmărește și escaladează. → O1, O2, O8, O9.
- **3 → „cititorul de hârtii existente”.** Produse care transformă PDF-urile și CSV-urile aflate deja la clinică într-o listă de lucru, fără senzori noi. → O3, O17, O21.
- **4 (jumătatea vie) → „instalații cu termen”.** EHDS, e-SănătateaMea, drepturile de acces. → O14, O15, O16.
- **7 → „întâi serviciul”.** Primele 2–3 luni la fiecare client merg ca serviciu: apeluri făcute de om, foaie de lucru, n8n. Prețul se pune însă de la început ca abonament, ca trecerea la SaaS să nu ceară renegociere.

### Meta-tiparul inversării

Aproape toate presupunerile care au căzut se sprijineau pe aceeași credință ascunsă: **că resursa rară în sănătatea predictivă e informația.** Inversările arată că informația e din belșug. Notele au chiar o expresie pentru asta: „date fără beneficiu” (MON §7). Rare sunt **responsabilitatea** (cine răspunde de acțiune) și **un buget care există deja**.

Singura inversare moartă (8) e cea în care legea pune resursa rară: certificarea. De aceea ea e granița dură. Strategia care decurge de aici: construiești pe belșugul de informație și pe lipsa de proprietari, și stai departe de granița certificării până ai venit și un partener clinic.

### Clasament onest

1. **1 + 5 (urmărirea, administrativ):** cea mai puternică direcție de produs.
2. **2 (plătitorul cu obligație):** cea mai puternică direcție comercială.
3. **7 (întâi serviciul):** direcție operațională, potrivită cu 10–12 ore pe săptămână.
4. **3 (hârtiile existente):** utilă, dar frânată de accesul la date.

Pe jumătate: **4**. Adevărată, dar nu nouă: **6**. Moartă și lăsată vizibilă: **8**.

---
## C. Analogia forțată (transplant structural)

### Pasul 1. Ținta

Structura „semnalele există, dar nimeni nu deține bucla de răspuns”. E o problemă de reproiectare a unui sistem, nu o analiză, deci ținta e validă.

### Pasul 2. Structura într-o frază, fără vocabular medical

> **Semnale slabe despre o problemă viitoare apar în multe locuri. Fiecare ajunge la cineva care nu poate acționa. Cel care ar putea acționa nu le vede, n-are timp sau nu e plătit să le adune. Cele mai multe semnale expiră fără răspuns.**

- **Actori:** emițătorii; cei care pot acționa; purtătorii, care lipsesc.
- **Flux:** semnalul.
- **Blocaj:** nu există un proprietar plătit al drumului dintre semnal și acțiune.

### Pasul 3. Domeniile

Am ales cinci domenii, din familii diferite:
- 🧬 **sistemul imunitar**, prin prezentarea antigenului (biologic);
- 🐜 **colonia de furnici** (biologic);
- ✈️ **managementul continuității navigabilității în aviație, CAMO** (operațional);
- ⚡ **dispeceratul rețelei electrice** (sisteme);
- 🏚 **claca**, adică ridicarea unui hambar de către tot satul (social).

Două precizări:
- **Triajul de la urgențe** l-am exclus din start ca analogie de suprafață. Împarte vocabularul cu ținta, nu structura.
- **Sistemul imunitar** a apărut și în L4, unde a fost abandonat: acolo s-a folosit *memoria* imună, care cerea un al doilea rol forțat. Aici folosesc altă proprietate, *prezentarea* antigenului, și o testez de la zero.
- **CAMO** nu e în lista de domenii a skill-ului. L-am ales pentru că proprietatea lui structurală se potrivește exact cu fraza de la Pasul 2: un rol separat de mecanic, care deține defectele rămase deschise și termenele lor. Faptele despre aviație sunt cunoștințe generale, nu vin din note.

### Pasul 4. Transplanturile

#### 🧬 Sistemul imunitar: prezentarea antigenului

**Rolurile:**
- **țesutul unde apare semnalul** = laboratorul, examenul de medicina muncii, ceasul;
- **celula dendritică** = purtătorul care ia semnalul din țesut și îl duce la ganglion;
- **ganglionul limfatic** = locul unde cei care pot acționa sunt deja adunați: lista zilnică a medicului de familie, programul specialistului;
- **limfocitul T** = medicul cu autoritate de decizie;
- **MHC** = formatul standard, minimal, în care e prezentat semnalul;
- **co-stimularea** = al doilea semnal, necesar înainte de un răspuns complet;
- **limfocitele T reglatoare** = toleranța, adică suprimarea care previne reacția exagerată.

Maparea cere un singur salt metaforic: purtătorul, un rol care azi nu există și care e chiar produsul.

**Ce face domeniul și noi nu:**
- **(a) Prezentare, nu transmitere.** Purtătorul nu trimite semnalul brut. Îl convertește într-un pachet minim, standard și acționabil: ce s-a găsit, de cine, ce se cere, până când. Apoi îl **duce acolo unde lucrează deja cel care poate acționa**, nu într-un portal nou. Lifen a crescut exact așa, integrând documentele direct în dosarul electronic al spitalului, iar Accurx pornind „de pe desktopul medicului de familie” (B2B Q2). Formatul IPS e echivalentul MHC (MON §5).
  → O3, O5, plus pachetul de ieșire din O2 și O9.
- **(b) Co-stimulare.** Se escaladează doar când două semnale independente spun același lucru, după reguli stabilite de medic. Exemplu din note: notificarea de hipertensiune de la Apple îi cere chiar utilizatorului 7 zile de măsurători cu manșeta (MON §1 ← AAFP).
  → O4.
- **(c) Toleranță.** Reguli explicite de suprimare și un buget de alerte pe fiecare om care revizuiește. Alertele de sepsis Epic au urcat de la 9% la 21% dintre pacienți pe zi când s-a schimbat mixul de cazuri, iar modelul a fost oprit (ȘTI KQ2 ← Healthcare IT News). Oboseala de alerte scade escaladarea (MON §2 ← BMC Nursing 2026).
  → principiu de design pentru O1, O4 și O18.

**Rezultat: aterizează.**

#### 🐜 Colonia de furnici (abandonată)

**Rolurile:** furnicile cercetaș = emițătorii; feromonul = semnalul; furnicile recrutate = cei care răspund.

**Ce face domeniul:** nu există proprietar. Fiecare agent urmează o regulă locală, iar traseele se întăresc prin folosire.

**Transferul încercat:** fiecare punct de contact (recepția, laboratorul, medicul de familie, farmacistul) aplică regula locală „dacă vezi o buclă deschisă, împinge-o mai departe”.

**Testul de potrivire:** furnicile sunt interschimbabile, orice furnică poate căra orice firimitură. În sănătate, doar laboratorul cunoaște rezultatul și doar medicul de familie poate da trimiterea. Ca analogia să meargă, laboratorul ar trebui să fie și cel care trimite: **al doilea rol forțat.** Mai mult, „fiecare e puțin responsabil” e exact starea de azi, care produce golul.

**Abandonată.** Mecanismul coloniei descrie boala, nu leacul.

#### ✈️ CAMO: managementul continuității navigabilității

**Rolurile:**
- **avionul** = omul, de exemplu angajatul;
- **mecanicul** = medicul care face examenul;
- **programul de întreținere** = periodicitatea examenelor;
- **directivele de navigabilitate** = programe sau reguli noi care se aplică întregii „flote” (de exemplu, pachetul CNAS 40+, gratuit din februarie 2026 și pentru neasigurații înscriși la un medic de familie; RO §5);
- **defectele amânate** = recomandările nefăcute încă: „consult ORL”, „reevaluare la 6 luni”, „analize”;
- **certificatul de navigabilitate** = fișa de aptitudine;
- **CAMO** = o organizație separată, plătită de operator, care deține starea și termenele, dar nu repară nimic.

**Ce face domeniul și noi nu** (din cunoștințe generale despre aviație):
- **(a) Un rol de continuitate, separat de cel care face munca, și plătit.**
  → un serviciu sau produs pentru furnizorii de medicina muncii, care deține recomandările deschise (O2).
- **(b) Defectele amânate au categorii cu termene fixe** (de exemplu 3, 10 sau 120 de zile) **și escaladare automată.** Fiecare recomandare primește o clasă de termen pusă de medic. Ceasul e al medicului, nu al software-ului, deci produsul rămâne administrativ.
- **(c) Poarta existentă:** avionul nu zboară cu termene depășite. Expirarea fișei de aptitudine e deja o poartă, pentru că examenele periodice sunt obligatorii (RO §5). Poarta asta devine forța care împinge bucla.
- **(d) Directiva către toată flota:** când apare un program nou, se generează lista celor din „flotă” cărora li se aplică, după vârstă, sex și regula programului.
  → O9. Atenție: „cine e restant la screening după ghid” e o zonă de graniță între categoria 1 și categoria 4 (REG §8).

**Rezultat: aterizează. E cea mai densă potrivire a lotului,** pentru că se potrivește pe două trăsături independente: un proprietar separat și clase de termen.

#### ⚡ Dispeceratul rețelei electrice

**Rolurile:**
- **producția** = invitațiile și alertele generate;
- **capacitatea de transport și consumul** = capacitatea din aval: sloturi de colonoscopie, consultații de cardiologie, minute de revizie;
- **căderea de tensiune** = listele de așteptare și alertele ignorate;
- **dispecerul** = cel care potrivește ce se eliberează cu capacitatea.

**Ce face domeniul și noi nu:**
- **(a) Eliberare în valuri, pe măsura capacității.** ROCCAS 4 NV are ca țintă 24.156 de teste FIT și 1.328 de colonoscopii (RO §5 ← ARPS; Digenio). **Calculul meu:** dacă pozitivitatea din Nord-Vest e ca în Sud-Vest Oltenia (6,68%; RO §5 ← Gazeta de Sud), rezultă ~1.614 pozitivi, adică ~285 (≈21%) peste ținta de colonoscopii. Fără dispecerat, pozitivii așteaptă, iar urmarea scade. **Ipoteze:** pozitivitatea se transferă de la o regiune la alta, iar ținta FIT înseamnă teste efectuate, nu kituri distribuite. Dacă înseamnă kituri distribuite, numărul de pozitivi scade.
- **(b) Răspuns la cerere:** când se eliberează un slot prin anulare, e tras primul din coada de pozitivi. Notele au deja mecanismul de umplere a listei de așteptare (EMG L).
- **(c) Lecția PRISMATIC:** cererea generată fără capacitate a crescut utilizarea (ȘTI KQ1).

**Rezultat: aterizează.** Ca modul al O1 (→ O18) și ca principiu pentru orice campanie (O8, O9).

#### 🏚 Claca: ridicarea hambarului de către tot satul

**Rolurile:**
- **familia** = un singur furnizor;
- **hambarul** = o buclă preventivă completă (examen, probă, rezultat, trimitere), prea mare pentru un singur furnizor când e vorba de o întreagă forță de muncă;
- **comunitatea** = angajatorul, furnizorul de medicina muncii, laboratorul și, opțional, un program de screening;
- **plata** = reciprocitatea: angajatorul dă timp plătit și spațiu, programul primește indicatori, clinica primește volum.

**Ce face domeniul și noi nu:**
- **(a) Toată bucla, într-o singură zi și într-un singur loc, cu toți actorii de față.** Predările dispar. Dovada cea mai apropiată e ACCESS: testul în aceeași vizită a urcat finalizarea de la 22% la 100% (ȘTI KQ1 ← UW Ophthalmology).
- **(b) Lista organizatorului** („cine aduce ce”) e chiar produsul: sloturi, kituri, consimțământ, reprogramarea absenților.
- **(c) Registrul reciprocității:** cine a dat ce și ce a primit înapoi.

**Rezultat: aterizează,** dar depinde de parteneri. → O9.

### Pasul 5. Meta-tiparul analogiei

Fiecare domeniu care a funcționat are un **purtător sau proprietar desemnat, distinct și de emițător, și de cel care face acțiunea finală**. Același proprietar **limitează fluxul la capacitate**:

| Domeniu | Proprietarul | Cum limitează fluxul |
|---|---|---|
| Sistemul imunitar | celula prezentatoare | toleranța |
| CAMO | organizația de continuitate | ceasul pe categorii |
| Rețeaua electrică | dispecerul | capacitatea din aval |
| Claca | organizatorul | programul zilei |

Colonia de furnici a eșuat exact din motivul invers: **distribuie proprietatea**, iar asta e chiar modul în care sistemul eșuează azi.

Concluzia structurală: produsul nu e „un semnal mai deștept”, ci **un proprietar plătit al buclelor deschise, cu un buget de capacitate.**

### Pasul 6. Clasament onest

1. **CAMO:** potrivire densă și un produs direct (O2).
2. **Rețeaua electrică:** dă cifre concrete pentru ROCCAS și un modul diferențiator.
3. **Sistemul imunitar:** dă principii de design (prezentare, co-stimulare, toleranță), mai puțin un produs de sine stătător.
4. **Claca:** bună, dar dependentă de parteneri.

Abandonată: **colonia de furnici**. Exclus din start: **triajul de la urgențe**, ca analogie de suprafață.

---

## D. Random stimulus: lot scurt de control

### De ce l-am rulat

Primele trei tehnici au ajuns repede la același răspuns: „proprietarul buclei”. Lotul acesta testează dacă convergența e reală sau doar un făgaș.

**De ce funcționează tehnica.** Când rămâi în spațiul problemei, asocierile trec mereu prin aceleași rute („urmărire”, „rechemare”, „buclă”). Un obiect din afară are o proprietate structurală pe care ținta n-o are încă, iar nepotrivirea forțează un drum nou prin aceeași țintă. Testul de redundanță e strict: **dacă ideea se putea obține și fără stimul, stimulul e abandonat.**

**Lotul:** 8 stimuli din 8 categorii distincte, 5 concreți și 3 abstracți, fără două din aceeași categorie unul după altul. Am evitat stimulii folosiți în L3 (sextantul, albina, marginalia, trimestrul fiscal, sala de așteptare, kintsugi, interpretul, umbra ploii, salvarea din joc, cheia de sub preș, ecolocația, calendarul de Advent).

### 📮 Biroul scrisorilor nelivrate — Curiosities & Edge Cases [concrete]

**Proprietăți:** aici ajung scrisorile care nu pot fi nici livrate, nici returnate. Funcționarii le deschid ca să caute orice indiciu. E locul unde lucrurile imposibil de livrat sunt în sfârșit tratate.

- **Prima încercare:** un serviciu separat pentru „restul de 10%”, rezultatele sau recomandările al căror destinatar nu poate fi găsit (telefon greșit, niciun răspuns după 3 încercări), escaladate la un om. Se putea obține din țintă: escaladarea eșecurilor face parte din orice urmărire de buclă.
- **A doua încercare:** problema reală e calitatea datelor de contact și de identitate → curățarea lor. Notele au deja unelte pentru calitatea datelor (ȘTI KQ4). Tot redundantă.

**Abandonat.**

### 🍞 Maiaua de pâine — Food & Cooking [concrete]

**Proprietăți:** o cultură vie, ținută în viață prin hrănire regulată. Se dă de la o casă la alta. Fiecare pâine are nevoie de puțină maia. Neglijată, moare. Cu vârsta devine mai puternică.

- **Prima încercare:** fiecare tranzacție a produsului „hrănește” un set longitudinal de date, cu consimțământ explicit. Redundantă: REG §8 numește deja „seiful de date cu consimțământ granular” cea mai directă rută legală spre un set de antrenare.
- **A doua încercare:** pacientul își duce „maiaua” (dosarul) de la o clinică la alta. Asta e modelul PHR, care a eșuat (MON §5), plus „pachetul de prezentare” de la sistemul imunitar.

**Abandonat.**

### 🎰 Automatul de vânzare — Tools & Machines [concrete]

**Proprietăți:** autoservire. Meniu fix, preț fix pe produs. Funcționează 24/7 fără personal. Un operator de traseu umple pe rând multe automate.

→ **Ideea:** un **meniu fix de prevenție bazată pe dovezi, cu preț fix, din care angajatul alege singur**, în bugetul de beneficii al angajatorului (plafonul de 400 EUR pe an; EMG Q2). Meniul e definit de un medic partener pe vârstă și sex, nu pe riscul fiecărui om. Comanda merge la laboratorul sau clinica parteneră, iar finalizarea e urmărită.

**Redundanța:** din țintă ajungeam la „tablou de prevenție pentru angajator”, nu la „meniu fix cu autoservire într-un buget plafonat fiscal”. Curatoriatul meniului (doar ce are dovezi, fără RMN de corp întreg și fără panouri largi) e o idee nouă.

→ **A doua potrivire:** **operatorul de traseu.** Fondatorul ține back-office-ul comun pentru 20 de cabinete mici, fiecare fiind un „automat”. E un model de afaceri pentru O2.

**Păstrat.** → O11.

### 🎼 Pauza (tăcerea ca parte din muzică) — Music & Performance [abstract]

**Proprietăți:** absența deliberată a sunetului. Pauza dă structură și înțeles notelor. E notată precis, cu durată.

→ **Ideea:** un **audit „pauza”**, care scoate din pachetele de check-up testele fără valoare dovedită. Clientul e cel care plătește daunele: asigurătorul de sănătate sau angajatorul care plătește pe test. „Pauza e notată”: fiecare test scos are o justificare scrisă.

**Pe ce se sprijină:**
- Controalele generale de sănătate n-au efect asupra mortalității (RR 1,00; ȘTI KQ1 ← AAFP/Cochrane).
- La RMN-ul de corp întreg, 94% au o anomalie, până la 30% ajung la investigații suplimentare și doar 1,1–1,6% au un cancer confirmat (ȘTI KQ1 ← CFPC TFP 410).
- Daunele plătite au crescut cu ~30% în T1 2025 față de prime cu +12–13% (EMG Q2 ← ZF; Financial Intelligence).

**Redundanța:** toată ținta spune „fă mai mult, mai devreme”. Pauza spune „fă mai puțin, deliberat”. Fără stimul nu ajungeam aici.

**Păstrat, surpriza lotului.** → O12.

### 🗳 Cvorumul — Abstractions & Concepts [abstract]

**Proprietăți:** decizia se ia doar când destui agenți sunt de acord. Un prag declanșează angajamentul.

- **Prima încercare:** escaladezi doar când mai multe semnale coincid. E co-stimularea de la sistemul imunitar, deci redundantă.
- **A doua încercare:** un mic consiliu asincron de medici pentru cazurile la limită. E clinic (categoria 4) și nu e nou.

**Abandonat.**

### ⚓ Botezul unei nave — Rituals & Ceremonies [concrete]

**Proprietăți:** ceremonia marchează intrarea navei în serviciu. Numele se înregistrează, se numește o „nașă” legată de navă pe viață, iar din acel moment nava are jurnal de bord.

→ **Ideea:** **examenul la angajare e „botezul”.** El deschide un jurnal de sănătate ocupațională pe toată durata carierei: un nivel de bază, expunerile, recomandările. Jurnalul poate fi purtat, cu consimțământul angajatului, de la un furnizor de medicina muncii la altul. Pentru expunerea la cancerigeni, REG §6 menționează păstrarea evidențelor 40 de ani (← Directiva 2004/37/CE, BK).

**Redundanța:** arhiva ocupațională se putea obține și din țintă, dar ideea de bază fixată la angajare și purtabilă între furnizori e nouă.

**Lovitură pe jumătate.** Se contopește cu O17.

### ⛴ Luntrașul (Charon) — People & Roles [concrete]

**Proprietăți:** îi trece pe oameni peste o graniță. E plătit cu o monedă. Granița desparte două lumi.

→ **Ideea:** buclele se rup la **treceri**. Pensionarea e ieșirea din singurul contact preventiv sistematic (medicina muncii) exact la vârsta când riscul crește. Un pachet de predare către medicul de familie, plus invitația la pachetul CNAS 60+ (RO §5), ar acoperi trecerea. **Problema:** nu se vede cine plătește.

→ **A doua încercare:** predarea la externare. Lifen o face deja, deci e redundantă.

**Lovitură slabă, păstrată pentru hartă.** → O23.

### 🌟 Lumina unei stele moarte — Cosmos & Scale [abstract]

**Proprietăți:** ce vezi e vechi. Sursa s-ar putea să se fi schimbat între timp.

- **Prima încercare:** prospețimea datelor, adică derapajul modelelor. Redundantă (ȘTI KQ2).
- **A doua încercare:** consultațiile private lipsesc din dosarul național, deci produsul ar reconcilia dosarul public cu cel privat. Asta e iar PHR-ul.

**Abandonat.**

### Meta-tiparul lotului

**Loviturile** (automatul, pauza, botezul, luntrașul) au schimbat toate **direcția valorii**:
- de la „mai multe semnale și mai multă urmărire” la **curatoriat: ce merită făcut** (pauza, automatul);
- la **unde, în viața unui om, se rupe bucla** (botezul, luntrașul).

**Abandonările** (scrisorile nelivrate, maiaua, cvorumul, steaua moartă) au murit toate la fel: au repetat un mecanism găsit deja de primele trei tehnici (urmărirea, setul de date cu consimțământ, co-stimularea, derapajul).

Patru abandonări din opt e mult, dar nu peste jumătate. Spun ceva util: **convergența e reală**, iar spațiul din jurul „proprietarului buclei” e saturat. Singura axă nouă cu plătitor e **dez-implementarea**: mai puțină prevenție fără valoare, plătită de cine plătește daunele.

### Clasament onest

1. **Pauza:** auditul de dez-implementare.
2. **Automatul:** meniul fix în bugetul plafonat.
3. **Botezul:** variantă a arhivei ocupaționale.

Slab: **luntrașul**, fără plătitor. Abandonate: scrisorile nelivrate, maiaua, cvorumul, steaua moartă.

---
## E. Lista de oportunități (26)

**Cum se citește fiecare intrare:**
- **Origine:** tehnica din care a ieșit ideea (CF = concept fan, INV = inversare, AN = analogie, RS = random stimulus).
- **Cine plătește:** clientul precis.
- **Fluxul de azi** și **durerea**.
- **Produsul.**
- **Date și cum se obțin.**
- **Distribuție.**
- **Reglementare:** prima ghicire, după cele 4 categorii de la §0.
- **Pro** și **contra:** dovezile care susțin și cele care slăbesc ideea, cu citare.

Toate prețurile sunt **ipoteze de testat**. Toate „durerile” sunt **inferențe**, dacă nu e citată o sursă. Pentru orice produs care atinge date de sănătate, fondatorul lucrează ca **persoană împuternicită** (Art. 28 GDPR), cu contract de prelucrare, listă de sub-procesatori și găzduire în UE (REG §1).

### Familia 1. Operatorul buclei deschise (urmărirea)

#### O1. Navigator „FIT pozitiv → colonoscopie făcută” pentru ROCCAS 4 Nord-Vest, cu dispecerat de capacitate

*Origine:* CF A1; INV 1 și 2; AN rețeaua electrică.

- **Cine plătește:** partenerul din consorțiul ROCCAS 4 NV care răspunde de partea din Bihor (spital, universitate sau ONG; rolul ARPS e neverificat), ca subcontractare din bugetul proiectului: ~35,6 mil. lei, 1 septembrie 2025 – 1 septembrie 2029. Extinderi posibile: proiectele surori (SE, SVO, Vest) și IRO Iași (COLONPREV, DARIA, CLARA).
- **Fluxul de azi:** informare → consiliere → FIT → evaluarea riscului → investigație de specialitate → trimitere, plus raportarea indicatorilor (RO §5 ← Digenio; ARPS).
- **Durerea:**
  - pozitivii se pierd între rezultat și colonoscopie, ca în EAGLE și ACCESS;
  - capacitatea de colonoscopii e fixă: la pozitivitatea din SVO, ~1.614 pozitivi față de 1.328 colonoscopii țintă (calculul meu, cu ipotezele de la §C);
  - indicatorii trebuie raportați autorității de management.
- **Produsul:**
  - listă de lucru pe caz: stare, termen, cine sună;
  - scenarii de mesaj SMS/WhatsApp și de apel pentru consilieri și mediatori;
  - programare în valuri după sloturile de colonoscopie;
  - umplerea anulărilor din coada de pozitivi;
  - export de indicatori;
  - o variantă offline pentru mediatorii din zone vulnerabile.
- **Date și cum se obțin:** lista participanților, rezultatul FIT de la laborator, programarea și finalizarea colonoscopiei. Vin de la proiect, fondatorul fiind persoană împuternicită. La început, introducere manuală sau CSV.
- **Distribuție:**
  - rețeaua din Oradea: Spitalul Clinic Județean de Urgență Bihor găzduiește deja programări pentru screeningul cervical (RO §7), iar Bihor e în ROCCAS 4 NV;
  - apoi aceleași module, vândute celorlalte proiecte regionale.
- **Reglementare:** (1) administrativ. Termenele și eligibilitatea le stabilește protocolul proiectului, nu software-ul. Atenție la orice „cine e eligibil după ghid” calculat de software: e zonă de graniță (REG §8).
- **Pro:**
  - RO §5 (ROCCAS 4 NV: cifrele și calendarul ← Digenio, ARPS; pozitivitate 6,68% în SVO ← Gazeta de Sud);
  - ȘTI KQ2 și KQ4 (golul de urmare ← TCTMD, UW Ophthalmology);
  - ȘTI KQ1 (PRISMATIC ← PMC6820297);
  - EMG Q1-C (motoare de invitare și rechemare pentru screening).
- **Contra:**
  - bugetele au fost fixate în 2025, cu reguli de achiziție UE, iar intrarea realistă e doar ca subcontractor (RO §5, Inferences);
  - nu știm ce software are deja consorțiul;
  - un singur client mare;
  - proiectul acoperă 6 județe, deci partea Bihorului e o fracțiune;
  - identitatea partenerilor e neverificată (RO §5, Gaps).

#### O2. Registrul recomandărilor deschise după examenul de medicina muncii („CAMO pentru oameni”)

*Origine:* AN CAMO; INV 2 și 5; CF A1 × B1.

- **Cine plătește:** furnizorul independent de medicina muncii (cabinet sau firmă) din Bihor.
  - **Ipoteză de preț:** abonament fix pe cabinet, de ordinul zecilor de euro pe lună (ancore: MediNote 50 lei/utilizator/lună, BizMedica 159–199 lei/lună; RO §2) sau câțiva lei pe angajat activ pe an.
  - Furnizorul îl poate revinde angajatorului ca „raport de conformitate”.
- **Fluxul de azi:** examen la angajare, periodic sau la reluarea muncii → fișa de aptitudine (apt / apt condiționat / inapt temporar) → recomandări (consult de specialitate, reevaluare, analize). Recomandările rămân pe hârtie, iar următorul contact e peste 6–12 luni.
- **Durerea:**
  - nimeni nu știe dacă recomandările s-au făcut;
  - furnizorul concurează doar pe preț (80 lei/angajat/an; RO §5 ← Medworks);
  - urmărirea scadențelor e vândută ca trăsătură de serviciu, nu ca produs (RO §5 ← One Medicina Muncii, HARDMED, M Hospital).
- **Produsul:**
  - fiecare recomandare e un element cu clasă de termen pusă de medic;
  - remindere către angajat, pe bază de consimțământ;
  - încărcarea dovezii (scrisoarea medicală);
  - escaladare la medic;
  - o vedere pentru angajator care arată doar „în termen / depășit / închis”, **fără diagnostic**;
  - calendarul de expirare a fișelor pe fiecare angajator și raport lunar.
  - **Etapa 2:** back-office comun pentru mai multe cabinete mici („operatorul de traseu”, de la RS).
- **Date și cum se obțin:** evidențele furnizorului (persoană împuternicită; baza furnizorului e Art. 9(2)(h), medicina muncii; REG §1), importate din Excel sau din programul lui. Telefoanele angajaților vin din lista angajatorului.
- **Distribuție:** vizite pe jos la cabinetele din Oradea și rețeaua de angajatori a fondatorului. Apoi furnizori mai mari, de tip Medexpert (Cluj: 15.000 de angajați pe an, peste 500 de firme; RO §5).
- **Reglementare:** (1) administrativ. Angajatorul nu trebuie să vadă diagnostice; practica „angajatorul primește doar concluzia de aptitudine” e BK și trebuie verificată (REG §6, Gaps).
- **Pro:**
  - RO §5 (Legea 319/2006, HG 355/2007, prețuri, volume);
  - EMG Q3 (nivelul 1, punctul 4);
  - REG §8 (punctul de intrare 3, „logistica medicinei muncii”);
  - MON §6 (urmărirea trimiterilor).
- **Contra:**
  - marje mici;
  - n-am identificat vendorii de software pentru medicina muncii (RO §2, Gaps) și nici firmele independente din Bihor (RO §7, Gaps);
  - nu știm dacă furnizorii simt durerea sau dacă angajatorii plătesc în plus.
  - Diferă de ideea din L4 („Rămân”, retenția muncitorilor străini): aici jobul e închiderea recomandărilor după un examen obligatoriu.

#### O3. Inbox de urmărire pentru rezultatele în afara intervalului de referință (laboratoare independente și clinici cu laborator propriu)

*Origine:* CF A1; AN sistemul imunitar (prezentarea); INV 3.

- **Cine plătește:** un laborator independent din Oradea sau din Bihor (nu unul dintr-o rețea), lunar, după volum; sau o clinică cu laborator propriu.
- **Fluxul de azi:** pacientul, adesea venit fără trimitere și plătind din buzunar, primește un PDF cu valorile marcate față de intervalele laboratorului. Niciun medic nu e atașat și nimeni nu verifică ce urmează.
- **Durerea:**
  - urmarea lipsește pentru cei veniți fără trimitere;
  - au existat amenzi GDPR pentru rezultate trimise pe WhatsApp sau e-mail (RO §3 ← e-juridic);
  - laboratorul pierde repetările de test și consultațiile.
- **Produsul:**
  - livrare conformă (link cu cod unic);
  - un mesaj neutru, scris de om, folosind **doar marcajele laboratorului** („rezultatul are valori în afara intervalului de referință al laboratorului; discutați cu un medic”);
  - link de programare la un medic partener;
  - urmărirea faptului că pacientul s-a programat;
  - reminder de repetare la intervalul stabilit de medicul de laborator.
- **Date și cum se obțin:** exportul din programul laboratorului (HL7 sau PDF), plus contactul și consimțământul pacientului.
- **Distribuție:** laboratoare independente și puncte de recoltare; mai târziu, un parteneriat cu vendorul programului de laborator.
- **Reglementare:** (1) comunicare. Devine (4), posibil sub IVDR, dacă adaugă marcaje noi, tendințe sau predicții (REG §2, tabel).
- **Pro:**
  - REG §2 (tabelul: rutarea rezultatelor nu e dispozitiv);
  - B2B (Lifen ← FrenchWeb);
  - ȘTI KQ4 (tabel, aria 3: fluxul de urmare după rezultat anormal);
  - CONS KQ3 (Neko urmărește trimiterile ← Neko Year Two).
- **Contra:**
  - laboratoarele din Oradea sunt mai ales în rețele, cu IT centralizat; Bioclinica e neverificată (RO §7);
  - nu există date românești despre cum anunță laboratoarele valorile anormale (RO §3, Gaps);
  - 32% dintre români s-ar simți trădați dacă explicațiile analizelor ar fi scrise de AI (RO §6 ← StartupCafe/MKOR), deci mesajul trebuie să fie uman și neutru.

#### O4. Navigator „am primit o notificare de la ceas” pentru clinici private de cardiologie

*Origine:* CF A2; AN sistemul imunitar (co-stimularea).

- **Cine plătește:** o clinică privată de cardiologie din Oradea sau București, din venitul pe ECG, Holter și MAPA.
- **Fluxul de azi:** oamenii vin cu notificări de fibrilație atrială, hipertensiune sau apnee în somn. Diagnosticul cere confirmare pe ECG, pentru că o alertă PPG nu e diagnostic (MON §1 ← ESC 2024). Notificarea de hipertensiune de la Apple îi cere chiar utilizatorului 7 zile de măsurători cu manșeta.
- **Durerea:** alertele neconfirmate se pierd, pacienții sună îngrijorați, programarea e greoaie.
- **Produsul:**
  - pagină de intrare dedicată, cu formular structurat (ce notificare, de când, captură de ecran);
  - programarea testului de confirmare după protocolul clinicii;
  - jurnal de 7 zile de tensiune introdus de pacient și afișat fidel;
  - remindere.
  - Medicul decide.
- **Date și cum se obțin:** de la pacient. La început, fără integrare cu dispozitivul.
- **Distribuție:** clinici de cardiologie din Oradea, prin site-ul clinicii.
- **Reglementare:** (1) dacă doar colectează, afișează și programează. (4) dacă interpretează notificarea sau semnalează praguri (REG §2: un tablou RPM cu praguri și alerte e IIa).
- **Pro:**
  - MON §1: PPV al notificărilor de 0,84 și ~0,98 (← Perez, NEJM 2019; Lubitz, Circulation 2022); sensibilitatea notificării Apple de hipertensiune 41,2% și cele 7 zile cu manșeta (← AAFP);
  - MON §6 (închiderea buclei după o alertă de wearable).
- **Contra:**
  - penetrarea wearable-urilor în România e necunoscută (EMG, Gaps);
  - statutul CE al funcțiilor Apple e neverificat (MON §1, Gaps);
  - volumul poate fi prea mic pentru un produs separat; probabil e un modul.

#### O5. Urmărirea biletelor de trimitere pentru cabinetele de medicină de familie („biletul a fost folosit?”)

*Origine:* CF A1; MON §6.

- **Cine plătește:** cabinetul de medicină de familie (abonament mic) sau vendorul programului de cabinet, ca modul în plus (Setrio/BizMedica).
- **Fluxul de azi:** medicul dă bilet către specialist sau laborator, dar nu află dacă pacientul a ajuns acolo.
- **Durerea:** trimiteri neînchise, inclusiv după consultația de prevenție.
- **Produsul:**
  - lista biletelor emise, din exportul programului de cabinet;
  - mesaj automat către pacient la ziua X („ați reușit să vă programați?”), cu răspunsul înregistrat;
  - lista celor fără răspuns, pentru telefonul asistentei.
- **Date și cum se obțin:** exportul cabinetului și răspunsurile pacienților.
- **Distribuție:** asociații de medici de familie; vendorii de software de cabinet.
- **Reglementare:** (1).
- **Pro:** MON §6 (urmărirea trimiterilor ca piesă de coordonare); RO §4 (e-SănătateaMea arată trimiterile pacientului).
- **Contra:**
  - nu știm dacă medicii de familie plătesc;
  - asistența primară primește doar 10% din cheltuiala de sănătate (RO §5 ← State of Health in the EU 2025);
  - programele de cabinet n-au API (RO §2).
  - Slabă spre medie.

#### O6. Check-in administrativ după chirurgia de zi (oftalmologie, ortopedie)

*Origine:* MON §6.

- **Cine plătește:** o clinică privată de chirurgie de zi (de exemplu cataractă).
- **Fluxul de azi:** controale la ziua 1, 7 și 30; pacienții le ratează; întrebările vin pe telefon.
- **Produsul:** mesaje sau apeluri vocale programate, **doar cu întrebări administrative** („ați primit rețeta?”, „știți ora controlului?”). Orice cuvânt despre simptome duce imediat la o asistentă. Software-ul nu face triaj.
- **Date și cum se obțin:** programul clinicii.
- **Distribuție:** clinicile de chirurgie de zi.
- **Reglementare:** (1) numai fără evaluarea simptomelor. Dacă pune întrebări clinice ca să decidă ceva, trece la (4): Tucuvi e poziționat ca dispozitiv CE, iar Platform24 e lecția de evitat (MON §6; CEE Q3).
- **Pro:** MON §6 (Ufonia la controlul după cataractă; Tucuvi; BK); REC (româna merge pentru sarcini vocale scurte); MON §6 (remindere ← Cochrane).
- **Contra:**
  - e la granița triajului;
  - răspunderea pentru semnale de alarmă ratate (MON §6, Barriers);
  - PLD din decembrie 2026 (REG §7).
  - **Slabă.**

#### O7. Urmărirea la distanță a pacienților străini și din diaspora ai clinicilor dentare de turism medical (Oradea)

*Origine:* extinde L4; RS luntrașul (trecerea graniței); CF A1.

- **Cine plătește:** clinica dentară de turism medical. Din note sunt cunoscute ca existente, nu drept clienți: Dental-Art, MaxiloMED, LifeDent, Estetical Dentis, German Dental (RO §7).
- **Fluxul de azi:** faza 1 de implant → pacientul pleacă acasă → faza 2 peste câteva luni, plus controale; complicațiile apar în străinătate.
- **Durerea:** urmarea se pierde, complicațiile sunt tratate de alții, apar recenzii proaste, faza 2 e ratată.
- **Produsul:**
  - programarea protocolului de după tratament;
  - check-in-uri în DE, IT, HU, EN (fotografii și chestionar trimise stomatologului, fără evaluare automată);
  - planificarea ferestrei de călătorie pentru faza 2.
- **Date și cum se obțin:** planurile de tratament ale clinicii și fotografiile trimise de pacient (date de sănătate, deci contract de prelucrare și găzduire în UE).
- **Distribuție:** clinicile de turism dentar din Oradea, din aceeași rețea ca ideea din L4.
- **Reglementare:** (1) dacă doar transmite. (4) dacă evaluează automat.
- **Pro:** RO §7 (clinicile își declară pacienți din IT, UK, AT, DE; peste 30.000 de turiști medicali ← Economica; comparația de prețuri cu Ungaria ← Stomatologo); L4 (rechemarea dentară); CONS KQ3 (urmărirea ca pârghie economică).
- **Contra:**
  - volumul turismului dentar în Bihor e necunoscut (RO §7, Gaps);
  - e același cumpărător ca în L4, nu un segment nou;
  - nu e cu adevărat „predictiv”.
  - Medie.

### Familia 2. Pe obligații și bugete care există deja

#### O8. Rechemare pentru pachetul CNAS de prevenție 40+ (și 60+) la cabinetele de medicină de familie

*Origine:* INV 2; CF B1.

- **Cine plătește:** cabinetul de medicină de familie, o asociație de cabinete sau vendorul de software, ca modul.
- **Fluxul de azi:** din februarie 2026, serviciile de prevenție sunt gratuite pentru oricine e înscris la un medic de familie. Pentru 40+, pachetul are până la 3 consultații în 6 luni (evaluare, intervenție, monitorizare). Analizele vin prin trimiterea medicului și adesea trebuie cerute explicit. La 60+ se adaugă evaluarea pentru osteoporoză, incontinență și demență (RO §5 ← Capital, MS, PS News).
- **Durerea:** nimeni nu invită, secvența de 3 vizite se rupe, iar pacienții nu știu de pachet (RO §5 ← Doctorul Zilei, titlu).
- **Produsul:**
  - listă de eligibili din lista cabinetului, doar după vârstă și data ultimei prevenții, nu după risc clinic;
  - invitații prin SMS, telefon sau scrisoare;
  - programare;
  - urmărirea celor 3 pași;
  - ajutor la raportare.
- **Date și cum se obțin:** exportul programului de cabinet, cu cabinetul ca operator.
- **Distribuție:** medicii de familie din Bihor; vendorii de software (Setrio).
- **Reglementare:** (1). Eligibilitatea după vârstă și dată, conform pachetului CNAS, e o regulă de calendar. Devine zonă de graniță dacă începe să prioritizeze după risc clinic (REG §8).
- **Pro:**
  - RO §5 (pachetul CNAS 2026);
  - EMG Q3 (nivelul 1, punctul 2);
  - EMG Q2 (stimulente pentru prevenție în asistența primară ← WHO/Observatory 2026).
- **Contra:**
  - nu știm cât plătește CNAS medicului per serviciu de prevenție, deci nici dacă medicul are motiv să cumpere (lipsește din note);
  - sursele se contrazic despre frecvența la 18–39 de ani;
  - programele de cabinet n-au API;
  - apelurile automate cer consimțământ (Legea 506/2004; RO §3).

#### O9. „Ziua de prevenție” la locul de muncă (organizatorul de clacă)

*Origine:* AN claca; CF A2; RS botezul navei.

- **Cine plătește:** furnizorul de medicina muncii sau clinica privată care vinde angajatorului. Angajatorul plătește din contractul de medicina muncii sau din bugetul de beneficii (plafonul de 400 EUR; EMG Q2).
- **Fluxul de azi:** examenele periodice se fac separat de orice altă prevenție; angajații nu merg singuri la controale.
- **Durerea:**
  - 3 din 10 români n-au făcut niciun control de rutină în 2025 (CONS G ← Agerpres/Regina Maria);
  - logistica e grea;
  - predările pierd oameni.
- **Produsul:**
  - planificator de eveniment: sloturi pe secții și ture;
  - consimțământ;
  - urmărirea kiturilor și a probelor;
  - check-in în ziua respectivă;
  - reprogramarea absenților;
  - rutarea rezultatelor către medic;
  - închiderea buclelor după eveniment, legată de O2.
- **Date și cum se obțin:** lista de la HR (nume, anul nașterii, sex, tura; nimic medical) și datele de examen ale furnizorului.
- **Distribuție:** furnizorii de medicina muncii; angajatorii din parcurile industriale din Oradea (prin rețeaua fondatorului).
- **Reglementare:** (1). Listele de eligibilitate se fac după regulile definite de partener sau de program.
- **Pro:** ȘTI KQ1 (ACCESS ← UW Ophthalmology); CONS G (Agerpres); RO §5 (examene periodice, abonamente).
- **Contra:**
  - apetitul angajatorilor pentru suplimente e neverificat (EMG Q2, Gaps);
  - depinde de parteneri (laborator, program);
  - venitul e pe proiect dacă nu e legat de O2.

#### O10. Raportul de „finalizare a prevenției” pentru abonamentele corporate (vândut clinicilor care vând abonamente)

*Origine:* CF B2 și B3; INV 2.

- **Cine plătește:** o clinică independentă sau o rețea medie care vinde abonamente corporate (nu cele trei mari). E un raport cu marca clinicii pentru clienții ei de HR.
- **Fluxul de azi:** angajatorul plătește abonamentul. La reînnoire, HR-ul întreabă ce a primit, iar clinica raportează utilizarea, nu prevenția.
- **Durerea:** argument slab la reînnoire; prevenția e puțin folosită.
- **Produsul:**
  - tablou anonimizat (grupuri de minimum 10): procentul care au făcut controlul anual, procentul recomandărilor închise, campaniile trimise;
  - plus contactarea celor care n-au făcut controlul.
- **Date și cum se obțin:** datele de vizită ale clinicii, agregate, plus numărul de angajați de la HR.
- **Distribuție:** prin clinici.
- **Reglementare:** (1) sau (3, fără dispozitiv): tablou de calitate la nivel de populație (REG §8).
- **Pro:**
  - EMG Q2 (400 EUR ← Romania Insider; ~750.000 de abonamente Regina Maria ← BestJobs; ~1 milion de angajați la MedLife ← Forbes RO);
  - EMG Q2, Inferences (software-ul trebuie să coste 0,5–2 EUR pe membru pe lună, prin clinică);
  - ȘTI KQ2, Inferences (tablourile au valoare doar legate de o acțiune).
- **Contra:**
  - rețelele mari își fac singure software-ul (RO §1; CEE Q2);
  - cererea angajatorilor pentru analiză n-a fost găsită (EMG Q2, Gaps);
  - plafonul de 400 EUR e neschimbat din 2016 (RO §5).

#### O11. Meniul fix de prevenție bazată pe dovezi („automatul”) în bugetul de beneficii

*Origine:* RS automatul de vânzare.

- **Cine plătește:** angajatorul, din beneficiul plafonat la 400 EUR. Cumpărarea se face prin clinica sau laboratorul partener, iar platforma ia o taxă pe comandă sau pe angajat pe lună.
- **Fluxul de azi:** angajatorii cumpără pachete largi, angajații nu aleg, iar testele fără dovezi stau amestecate cu cele utile.
- **Durerea:** banii de beneficii se risipesc, iar folosirea e mică.
- **Produsul:**
  - meniu fix pe vârstă și sex, definit și semnat de un medic partener (de exemplu: tensiune; profil lipidic și glicemie de la 40 de ani; FIT la 50–74 de ani; Babeș-Papanicolau/HPV la intervalul stabilit);
  - angajatul comandă singur, în limita bugetului;
  - comanda merge la partener și finalizarea e urmărită;
  - **fără recomandări pe riscul fiecărui om.**
- **Date și cum se obțin:** eligibilitatea de la HR (vârstă, sex), comenzile și finalizarea de la laborator.
- **Distribuție:** angajatori prin clinici partenere; furnizori de medicina muncii.
- **Reglementare:** (1), comercial. Dacă meniul ajunge să se personalizeze după date de sănătate, devine profilare (Legea 190/2018 art. 3) și posibil (4).
- **Pro:**
  - EMG Q2 (400 EUR; scutirea pentru abonamente sportive, inclusiv pachete cu servicii medicale ← PwC, Legea 34/2023);
  - ȘTI KQ1, aria 3 (controalele generale au RR 1,00 ← AAFP/Cochrane; RMN de corp întreg ← CFPC);
  - CONS (prețurile abonamentelor de analize din SUA scad repede).
- **Contra:**
  - e nevoie de un laborator partener și de un medic care semnează meniul;
  - angajatorii pot prefera abonamentele marilor rețele;
  - tratamentul fiscal trebuie verificat (EMG Q2, Gaps).

#### O12. Auditul „pauza”: scoaterea testelor fără valoare din pachetele de check-up plătite de asigurători și angajatori

*Origine:* RS pauza (surpriza lotului).

- **Cine plătește:** asigurătorul privat de sănătate care oferă pachete de analize (exemplul din note: NN, la Regina Maria; CONS G) sau un angajator mare care plătește pe test. Ori o clinică ce vrea un pachet ușor de apărat.
- **Fluxul de azi:** pachete de check-up plătite pe test, cu daune în creștere.
- **Durerea:**
  - daunele plătite au crescut cu ~30% față de prime cu +12–13% în T1 2025 (EMG Q2 ← ZF; Financial Intelligence);
  - testele fără valoare declanșează cascade: alte teste, anxietate (ȘTI KQ2).
- **Produsul:**
  - audit trimestrial al pachetelor: fiecare test e pus față în față cu dovezile (recomandat de ghid sau nu);
  - estimarea costului cascadelor (investigațiile de după descoperiri întâmplătoare);
  - propunere de pachet refăcut;
  - monitorizarea utilizării.
  - **Fără decizii pe pacienți individuali.**
- **Date și cum se obțin:** date agregate și anonimizate despre daune sau pachete, de la asigurător, plus ghiduri publice.
- **Distribuție:** greu fără rețea în asigurări. Poate merge prin clinica parteneră care vinde pachete asigurătorului.
- **Reglementare:** (3, fără dispozitiv), analiză la nivel de populație.
- **Pro:**
  - EMG Q2 (daunele);
  - RO §1 (prime de 756 mil. lei în S1 2026, +10% ← 1asig);
  - ȘTI KQ1 aria 3 și KQ2 (Cochrane, CFPC, meta-analiza din JMRI despre RMN-ul de corp întreg);
  - CONS (ACR recomandă împotriva scanărilor de corp întreg).
- **Contra:**
  - fondatorul n-are acces la asigurători, iar programele lor de prevenție n-au fost cercetate (RO §1, Gaps; EMG Q2, Gaps);
  - e nevoie de un partener clinic pentru revizia dovezilor, deci seamănă cu consultanța;
  - piața de asigurări e mică (~1,2–1,5 mld. lei pe an);
  - „mai puține teste” poate intra în conflict cu venitul clinicilor partenere.

#### O13. Platformă de operare pentru programe de prevenție a diabetului (tip DPP), plătite de angajatori

*Origine:* ȘTI KQ4, tabel, aria 4(a); CF B2.

- **Cine plătește:** o clinică de nutriție sau un furnizor de medicina muncii care rulează programe de grup. Angajatorul plătește per participant.
- **Fluxul și produsul:** înscriere, prezență, cântăriri, mesaje de coaching scrise de LLM și supravegheate de om, raport de rezultate. Prediabetul îl identifică laboratorul clinicii.
- **Date și cum se obțin:** participanții, cu consimțământ, plus cântăriri introduse manual sau prin cântar Bluetooth.
- **Reglementare:** (2) wellness, fără revendicări de boală. „Previne diabetul” l-ar muta în (4) (REG §2, tabel).
- **Pro:** ȘTI KQ1, aria 4 (DPP −58% ← Knowler, NEJM 2002; varianta cu AI non-inferioară, 31,7% față de 31,9%, cu inițiere 93,4% față de 82,7% ← Patient Care).
- **Contra:**
  - n-am găsit niciun program sau plătitor DPP în România;
  - apetitul angajatorilor e neverificat;
  - efectul scade în timp (DPPOS: −27% la 15 ani).
  - **Slabă.**

### Familia 3. Instalații cu termen legal

#### O14. Puntea e-SănătateaMea pentru furnizori mici cu contract CNAS (T4 2026)

*Origine:* INV 4; CEE Q4 și Q5 (tiparul 1, analogul conectării comune finlandeze).

- **Cine plătește:** clinici de specialitate și laboratoare mici cu contract CNAS din Bihor, lunar.
- **Fluxul de azi:** din T4 2026, programările trebuie să treacă prin e-SănătateaMea, dar furnizorii își țin în continuare propriul calendar.
- **Durerea:** două calendare, conformitate, instruirea personalului.
- **Produsul:** sincronizarea și reconcilierea sloturilor, tablou de stare, listă de verificare.
- **Date și cum se obțin:** calendarul propriu și portalul, dacă are API.
- **Reglementare:** (1).
- **Pro:** RO §4 (obligația ← medic24; Digi24); CEE Q4 (Kanta).
- **Contra:**
  - n-am găsit niciun API public pentru terți (RO §4);
  - programarea națională nu funcționa la lansare;
  - raportările se contrazic (2.500 de programări în prima lună, sursă neclară);
  - portalul poate face marfă din uneltele de programare.
  - **Slabă până se verifică API-ul.**

#### O15. Componentele EHDS (fațadă FHIR R4, rezumat IPS, jurnal de acces) pentru vendorii locali de software medical

*Origine:* INV 4; MON §5 (implicații pentru software).

- **Cine plătește:** vendorii români de software pentru clinici, laboratoare și spitale (din note: MediNote, BizMedica/Setrio, iStoma, icMED, iClinic; ca HIS, Hipocrate/RSC și InfoWorld). Licență plus taxă de integrare.
- **Fluxul de azi:** sistemele EHR puse pe piață trebuie să se autocertifice față de cerințele esențiale, cu componentele armonizate de interoperabilitate și de jurnalizare. Termenele: grupa 1 pe 26.03.2029, grupa 2 pe 26.03.2031 (MON §5; REG §4).
- **Durerea:** vendorii mici n-au expertiză FHIR sau IPS și au baze vechi Oracle/PL-SQL (MON §5, Inferences).
- **Produsul:**
  - fațadă FHIR peste Oracle/PL-SQL;
  - generator de rezumat IPS;
  - tabele de mapare LOINC/ATC;
  - componenta de jurnalizare;
  - evaluare de pregătire.
- **Date și cum se obțin:** nu e nevoie de date de pacient pentru dezvoltare (date sintetice); schemele vin de la vendori.
- **Distribuție:** direct către ~10–20 de vendori, prin rețeaua din București.
- **Reglementare:** fondatorul livrează o componentă a unui „sistem EHR”, pe care vendorul îl autocertifică. Nu e MDR.
- **Pro:**
  - MON §5 (← EUR-Lex 2025/327, BK; Xt-EHR; HL7 Europe);
  - REG §4 (← Heuking, noze, PLMJ);
  - EMG Q1-D;
  - RO §2 (vendori fragmentați, fără API public).
- **Contra:**
  - datele EHDS sunt în conflict între surse: Noze dă 2027/2028 (EMG Q1-D);
  - regulile românești de aplicare nu există încă;
  - cumpărătorii vor amâna până în 2027–2028 (EMG Q1-D, Inferences);
  - concurență open-source (HAPI, Medplum; B2B nr. 19);
  - România poate întârzia (MON §5).

#### O16. Jurnal de acces vizibil pacientului și gestiunea cererilor de acces la dosar (clinici private)

*Origine:* INV 4; CEE Q4 (jurnalul de acces vizibil pacientului, din Estonia).

- **Cine plătește:** clinica privată (stomatologie, specialități), lunar.
- **Fluxul de azi:** pacienții cer copii ale dosarului, iar personalul le trimite pe WhatsApp sau e-mail. Jurnalele de acces sunt interne sau lipsesc.
- **Durerea:**
  - o clinică dentară a fost amendată pentru că i-a refuzat unui pacient accesul la propriul dosar, iar alte clinici pentru că au trimis date pe WhatsApp sau e-mail (RO §3 ← e-juridic);
  - EHDS va da pacientului dreptul să vadă cine i-a accesat datele (REG §4; MON §5);
  - clinicile primesc cerințe de securitate prin NIS2 (REG §5).
- **Produsul:**
  - primirea cererii, cu ceas de 30 de zile;
  - livrare prin link securizat;
  - jurnal de acces vizibil pacientului („cine mi-a deschis dosarul”);
  - mai târziu, export în format standard (IPS).
- **Date și cum se obțin:** jurnalele programului clinicii, dacă există, sau depozitul de documente al produsului.
- **Reglementare:** (1). Poate deveni parte a unui „sistem EHR” dacă stochează date din categoriile prioritare (2029/2031), cu autocertificare.
- **Pro:** RO §3 (amenzile); CEE Q4 (← TEHIK/Linna); REG §4.
- **Contra:**
  - clinicile plătesc pentru conformitate, de obicei, abia după o amendă (inferență);
  - integrarea cu programele de cabinet lipsește;
  - valoarea pe client e mică.
  - Medie.

#### O17. Arhiva longitudinală de expunere profesională („jurnalul de bord” deschis la angajare)

*Origine:* RS botezul navei; REG §6; CF B1.

- **Cine plătește:** furnizorul de medicina muncii cu angajați expuși (zgomot, praf, substanțe chimice, cancerigeni) sau un angajator mare.
- **Fluxul de azi:** supravegherea specială produce audiograme, spirometrii și monitorizare biologică. Pentru cancerigeni, evidențele se păstrează 40 de ani (REG §6 ← Directiva 2004/37/CE, BK). Când angajatorul schimbă furnizorul, istoricul se rupe.
- **Durerea:** istoric pierdut, nivel de bază absent, obligație de arhivare.
- **Produsul:**
  - depozit longitudinal pe fiecare lucrător, cu afișarea fidelă a valorilor în timp (fără interpretare);
  - nivelul de bază fixat la angajare;
  - gestiunea termenului de păstrare;
  - pachet de predare către furnizorul următor, cu consimțământ.
- **Date și cum se obțin:** evidențele furnizorului; exporturile PDF din audiometre și spirometre, structurate cu LLM.
- **Reglementare:** (1) evidențe. (4) dacă semnalează automat deteriorarea. Posibil „sistem EHR” pentru rezultatele de laborator (grupa 2, 2031).
- **Pro:** REG §6; RO §5 (supravegherea specială printre tipurile de examen); CONS KQ3 (structurarea rezultatelor).
- **Contra:**
  - numărul de lucrători expuși din Bihor e necunoscut;
  - vendorii existenți sunt necunoscuți;
  - referința la directivă e BK, nereverificată.
  - **Strategic, însă:** e cel mai plauzibil activ de date pentru o predicție viitoare, cu bază legală clară (Art. 9(2)(h)).

### Familia 4. Capacitate, zgomot, monitorizare

#### O18. Dispecerat de capacitate pentru campanii de invitații

*Origine:* AN rețeaua electrică.

- **Cine plătește:** o clinică privată de gastroenterologie, endoscopie sau imagistică ce rulează campanii (pentru angajatori sau pachete de asigurător); ca modul, un program de screening (O1).
- **Fluxul de azi:** invitațiile pleacă în bloc → vârf de cerere → listă de așteptare, iar anulările rămân neumplute.
- **Produsul:** planificator de valuri după capacitate, umplerea anulărilor din coadă, măsurarea absențelor.
- **Date și cum se obțin:** capacitatea din calendar și lista de invitați.
- **Reglementare:** (1).
- **Pro:** EMG L (umplerea listei de așteptare; absențe); ȘTI KQ1 (PRISMATIC); RO §5 (cifrele ROCCAS).
- **Contra:** ca produs separat e mic, merge mai bine ca modul.
- Medie, ca modul.

#### O19. Atelier administrativ pentru un program privat de hipertensiune cu ajustarea tratamentului de către medic

*Origine:* CF A3; INV 7; MON §2.

- **Cine plătește:** o clinică privată de medicină internă sau cardiologie care vinde un „program de tensiune de 6 luni”, plătit din buzunar sau prin abonamente corporate.
- **Fluxul de azi:** pacientul măsoară acasă cu un tensiometru validat, asistenta revizuiește, iar medicul ajustează tratamentul după protocol.
- **Produsul:** înscriere, remindere pentru măsurători, afișarea fidelă a valorilor, programarea vizitelor de ajustare, jurnal de timp. **Alertarea** stă într-o aplicație parteneră marcată CE sau lipsește.
- **Date și cum se obțin:** introduse de pacient sau exportate din aplicația dispozitivului.
- **Reglementare:** (4) dacă există praguri sau alerte (REG §2: tablou RPM → IIa). (1) doar pentru logistica din jur.
- **Pro:** MON §2: TASMINH4 −3,5/−4,7 mmHg (← McManus, Lancet 2018); HOME BP (← BMJ 2021); PHTI: monitorizarea singură aduce efect marginal, gestionarea medicației aduce efect relevant (← PHTI 2024); modelul TMZ german rambursat (← KBV).
- **Contra:**
  - nu există rambursare în România (MON §2, Gaps);
  - MDR;
  - disponibilitatea pacienților de a plăti din buzunar e necunoscută.
  - Slabă spre medie. **Etapă ulterioară, cu partener.**

#### O20. Monitor local de performanță pentru AI-ul marcat CE cumpărat de rețele de imagistică sau programe de screening

*Origine:* ȘTI KQ2 și KQ4; INV 1.

- **Cine plătește:** rețeaua de imagistică sau programul de screening care folosește un AI marcat CE (de exemplu pentru mamografie). Din 2 august 2028 se aplică obligațiile utilizatorului (deployer) din AI Act, Art. 26: monitorizare și jurnale pentru AI cu risc ridicat (REG §3).
- **Produsul:**
  - tablou de audit: rata de rechemare, PPV, cancerele de interval, derapajul pe subgrupuri, volumul de alerte;
  - pachet de dovezi pentru supravegherea post-piață a vendorului.
- **Date și cum se obțin:** rezultate agregate și pseudonimizate, de la program sau din sistemul de radiologie.
- **Reglementare:** (1) sau (3): analiză de calitate la nivel de populație.
- **Pro:** ȘTI KQ2: modelul Epic de sepsis a avut AUC 0,63 la validarea externă față de 0,76–0,83 intern (← JAMA IM 2021); alertele au urcat de la 9% la 21% (← Healthcare IT News); NICE a recomandat DERM doar condiționat, pe 3 ani (← PharmaTimes).
- **Contra:**
  - n-am găsit utilizări românești ale unui astfel de AI;
  - nu există dovezi că cineva plătește pentru unelte de audit (ȘTI KQ4, Gaps);
  - fondatorul n-are acces la radiologie.
  - **Slabă acum; opțiune pentru 2028+.**

#### O21. Pregătirea vizitei de check-up: din PDF-urile vechi ale pacientului, un tabel de valori pentru medic (afișare fidelă)

*Origine:* INV 3; CONS KQ3 (punctul 1).

- **Cine plătește:** o clinică independentă care vinde pachete de check-up, per check-up sau lunar.
- **Fluxul de azi:** pacientul aduce analize vechi, în PDF-uri sau poze diferite, iar medicul răsfoiește.
- **Produsul:** pacientul încarcă documentele înainte de vizită (cu consimțământ). LLM-ul extrage valorile într-un tabel, cu unitatea de măsură și pagina sursă. Medicul verifică. Nu se adaugă interpretări și nici marcaje în afara celor ale laboratorului.
- **Date și cum se obțin:** încărcările pacientului.
- **Reglementare:** (1) dacă afișarea e fidelă. (4), posibil IVDR, dacă interpretează sau face predicții de tendință (REG §2).
- **Pro:** CONS KQ3 (← Levels support; Aeon/Aware); EMG Q1-B; ȘTI KQ4 (cronologia longitudinală a pacientului).
- **Contra:**
  - erorile de extracție ale LLM-ului atrag răspundere strictă din 9 decembrie 2026 (REG §7);
  - încrederea pacienților (MKOR, 32%);
  - medicii s-ar putea să nu plătească.
  - Medie spre slabă.

#### O22. Jurnal de evenimente și escaladare pentru cămine de bătrâni și îngrijire la domiciliu

*Origine:* MON §3; AN sistemul imunitar (toleranța față de alarmele false).

- **Cine plătește:** un cămin privat sau o agenție de îngrijire la domiciliu din Bihor, pe pat sau pe client pe lună.
- **Produsul:** jurnal de incidente, arbore de escaladare, informări pentru familie, planificarea vizitelor. Mai târziu, evenimente de la senzori obișnuiți, cu reguli de suprimare.
- **Date și cum se obțin:** introduse de personal.
- **Reglementare:** (1). Revendicări de genul „prevenim căderile” ar muta produsul în (4).
- **Pro:**
  - MON §3: 98,5% dintre studiile de detecție a căderilor folosesc căderi simulate (← recenzia de la Catania); 84 de alarme false la o cădere reală (← Chaudhuri 2015); teleasistența n-a redus utilizarea serviciilor (← Steventon 2013). Concluzia: se vinde pe timp de personal și documentare, nu pe rezultate clinice.
  - EMG G: îngrijirea pe termen lung e 5,6% din cheltuiala curentă de sănătate (← INSSE); populația 65+ urcă de la 19,7% la 30,6% până în 2050.
- **Contra:** căminele din Oradea n-au fost verificate (RO §7, Gaps); bugete mici; piață fragmentată (EMG G). **Slabă.**

### Familia 5. Uneltă de vânzare, treceri și etapa a doua

#### O23. Predarea la pensionare: ultimul examen de medicina muncii → medicul de familie

*Origine:* RS luntrașul.

- **Cine plătește:** neclar. Poate angajatorul, ca beneficiu de final de carieră, sau furnizorul de medicina muncii, ca serviciu.
- **Produsul:** pachet de predare plus invitația la pachetul CNAS 60+ la medicul de familie (RO §5).
- **Reglementare:** (1).
- **Contra:** n-are plătitor identificat. **Slabă, păstrată pentru hartă.**

#### O24. Auditul „bani expuși” al buclelor deschise (raport gratuit care deschide ușa)

*Origine:* CF B3; L3 (meta-tiparul „banii expuși”).

- **Cine plătește:** la început nimeni, e unealtă de vânzare. Apoi se transformă în O2, O3, O7 sau O8.
- **Produsul:** raport unic în APEX: numărul de recomandări deschise, controale neprogramate, lei nerealizați estimați, pacienți la risc de a pierde urmarea.
- **Date și cum se obțin:** export de la clinică (ca persoană împuternicită) și lista de prețuri.
- **Reglementare:** (1), analiză operațională, fără profilarea persoanelor (Legea 190/2018 art. 3).
- **Pro:** L3; B2B (argumentul ROI de la Lighthouse și Weave); RO §3, Gaps (nu există date românești, deci auditul produce primul număr local).
- **Contra:** datele pot fi prea nestructurate ca să se poată calcula ceva. Nu e o afacere de sine stătătoare.

#### O25. Predicția operațională a buclelor care nu se vor închide (etapa a doua, nu produs de start)

*Origine:* meta-tiparul tuturor tehnicilor; EMG L.

- **Cine plătește:** clienții O1, O2 și O8, ca modul în plus.
- **Fluxul:** apelurile făcute de oameni sunt puține. Întrebarea e pe cine suni primul.
- **Produsul:**
  - model care ordonează buclele deschise după probabilitatea de a nu se închide fără un apel;
  - **grup de control încorporat**, ca să se vadă dacă bate „reminder pentru toți”.
- **Date și cum se obțin:** istoricul buclelor (timpul de la recomandare, contactele încercate, răspunsul pe canal).
  - **Atenție:** dacă vendorul antrenează pe datele clinicii pentru scopurile lui, devine operator (REG §1).
  - Rute posibile: un model pe fiecare client, comandat de clinică (baza 9(2)(h) e contestată), sau consimțământ explicit.
  - Legea 190/2018 art. 3 cere consimțământ explicit sau o bază legală expresă pentru profilarea cu date de sănătate (REG §1).
- **Reglementare:** (1) după MDR, pentru că e o predicție operațională fără scop medical individual (REG §8). Dar e **profilare** după GDPR și legea română.
- **Pro:** EMG L: 33% față de 36% absențe (← PMC10150669); 19,3% → 15,9% (← Healthcare Finance News).
- **Contra:**
  - recenzia JAMIA spune că nu e clar dacă țintirea bate reminderul pentru toți (← Glasgow eprints);
  - baza legală e dificilă.
  - **Trebuie dovedită pe datele proprii, cu grup de control.**

#### O26. Coordonator pentru părinții din România ai familiilor din diaspora

*Origine:* RS luntrașul (trecerea graniței); MON §3, Inferences (familiile din diaspora).

- **Cine plătește:** copilul adult din străinătate, cu abonament B2C.
- **Produsul:** un coordonator (om plus software) care urmărește programările și rețetele părintelui, inclusiv pachetul CNAS 60+, și trimite noutăți familiei.
- **Reglementare:** (1). E nevoie de consimțământul părintelui și de confidențialitate (Legea 46/2003).
- **Contra:**
  - e B2C, iar fondatorul preferă B2B;
  - consumatorii plătesc greu, în afara „membrilor captivi” (EMG Q2);
  - consumă mult timp de om.
  - **Slabă.**

### Tabel de sinteză

| # | Oportunitate (scurt) | Cine plătește | Categ. reglem. | Tehnica | Încadrare preliminară |
|---|---|---|---|---|---|
| O1 | Navigator FIT+ → colonoscopie (ROCCAS 4 NV) | partener din consorțiu (subcontract) | 1 | CF, INV, AN | top 10 (#2) |
| O2 | Registrul recomandărilor de medicina muncii | furnizor de medicina muncii | 1 | AN, INV, CF | top 10 (#1) |
| O3 | Inbox pentru rezultate în afara intervalului | laborator independent | 1 (→4 dacă interpretează) | CF, AN, INV | top 10 (#4) |
| O4 | Navigator după notificarea de la ceas | clinică de cardiologie | 1 (→4) | CF, AN | top 10 (#10) |
| O5 | Urmărirea biletelor de trimitere | cabinet de medicină de familie | 1 | CF | slabă–medie |
| O6 | Check-in administrativ post-operator | clinică de chirurgie de zi | 1 (graniță 4) | MON | slabă |
| O7 | Urmărirea pacienților de turism dentar | clinică dentară | 1 | L4+, RS | medie |
| O8 | Rechemare pentru pachetul CNAS 40+/60+ | cabinet de medicină de familie | 1 (graniță) | INV, CF | top 10 (#5) |
| O9 | Ziua de prevenție la locul de muncă | furnizor de medicina muncii / angajator | 1 | AN, CF, RS | top 10 (#3) |
| O10 | Raport de finalizare pentru abonamente corporate | clinică cu abonamente | 1/3 | CF, INV | medie |
| O11 | Meniul fix de prevenție („automatul”) | angajator (400 EUR) | 1 | RS | top 10 (#8) |
| O12 | Auditul „pauza” (dez-implementare) | asigurător / angajator | 3 | RS | top 10 (#7) |
| O13 | Platformă de operare DPP | clinică de nutriție / angajator | 2 | ȘTI | slabă |
| O14 | Puntea e-SănătateaMea | furnizor mic cu contract CNAS | 1 | INV, CEE | slabă (API?) |
| O15 | Componente EHDS pentru vendori | vendor de software medical | EHDS (fără MDR) | INV | top 10 (#6) |
| O16 | Jurnal de acces și cereri de acces la dosar | clinică privată | 1 | INV, CEE | top 10 (#9) |
| O17 | Arhiva de expunere profesională | furnizor de medicina muncii | 1 (→4) | RS, CF | medie (strategică) |
| O18 | Dispecerat de capacitate | clinică endoscopie/imagistică; program | 1 | AN | medie (modul) |
| O19 | Atelier pentru program de hipertensiune | clinică de cardiologie | 4 pentru alerte / 1 logistic | CF, INV | etapă ulterioară |
| O20 | Monitor local de performanță AI | rețea de imagistică | 1/3 | ȘTI, INV | slabă acum (2028+) |
| O21 | PDF-uri vechi → tabel pentru medic | clinică cu check-up | 1 (→4) | INV | medie–slabă |
| O22 | Jurnal de evenimente pentru cămine | cămin / agenție de îngrijire | 1 | MON, AN | slabă |
| O23 | Predarea la pensionare | neclar | 1 | RS | slabă (fără plătitor) |
| O24 | Auditul „bani expuși” | — (unealtă de vânzare) | 1 | CF, L3 | instrument |
| O25 | Predicția buclelor care nu se închid | clienții O1, O2, O8 | 1 MDR / profilare GDPR | toate | etapa 2 |
| O26 | Coordonator pentru familiile din diaspora | familia (B2C) | 1 | RS, MON | slabă |

---
## F. Meta-tiparul comun și clasamentul preliminar

### F1. Meta-tiparul peste toate tehnicile

**1. Toate cele patru tehnici au ajuns la același loc, pe drumuri diferite.**

| Tehnica | Unde a ajuns la „proprietarul buclei” |
|---|---|
| Concept fan | ramura A1 × B1 |
| Inversarea | răsturnările 1, 2, 5 și 7 |
| Analogia | celula prezentatoare, CAMO, dispecerul, organizatorul de clacă; colonia de furnici a eșuat tocmai pentru că distribuie proprietatea |
| Random stimulus | toate abandonările au murit repetând același mecanism |

Formulat o dată, rezultatul comun e:

> **Valoarea rară nu e predicția, ci un proprietar plătit al buclei deschise (semnal → acțiune → confirmare). El stă pe un contact care are loc oricum și e plătit din bugetul cuiva care are deja o obligație.**

Dovezile din note care o susțin direct:
- EAGLE: 49,6% (ȘTI KQ2);
- ACCESS: 22% → 100% (ȘTI KQ1);
- TREWS: 3 ore (ȘTI KQ1);
- TIM-HF2 față de Tele-HF/BEAT-HF (MON §2);
- PRISMATIC (ȘTI KQ1);
- regula de sinteză din MON §7: beneficiul crește cu riscul de bază × cât de acționabil e semnalul × cât de sigur e răspunsul. Scoate oricare factor și rămân „date fără beneficiu”.

**2. În primul produs, „predicția” e calendarul.** Reguli deterministe stabilite de medic sau de program: termene, intervale, eligibilitate după vârstă și dată. Asta ține produsul în categoria 1 (REG §8) și îl scoate de sub Regula 11.

Predicția cu ML vine abia în etapa a doua (O25), pe o țintă **operațională** (cine nu-și va închide bucla), cu trei condiții:
- consimțământ explicit sau bază legală (Legea 190/2018 art. 3);
- grup de control;
- să bată reminderul pentru toți, lucru încă nedovedit (EMG L ← JAMIA).

**3. Activul care face credibil drumul spre platformă e istoricul buclelor.** Ce s-a recomandat, cine a închis bucla, când, după câte contacte. Inferența mea: acest istoric nu există azi nicăieri în România într-o formă structurată. El servește la trei lucruri:
- **(a)** predicția operațională (O25);
- **(b)** stratul de urmărire de care vendorii de AI clinic marcat CE vor avea nevoie ca să arate beneficiu, nu doar acuratețe (lecția EAGLE; ȘTI KQ4);
- **(c)** pregătirea pentru folosirea secundară a datelor prin EHDS, prin organismele de acces la date (HDAB), de la ~2029 (REG §4).

**4. Axa nouă de la random stimulus e dez-implementarea.** Mai puțină prevenție fără valoare, plătită de cine plătește daunele (O12), și un meniu curat de prevenție cu dovezi în bugetul plafonat al angajatorului (O11). E singura direcție care nu trece prin „mai multă urmărire”.

**5. Fundăturile au un motiv comun.** Cer fie **un plătitor nou** (consumatorul român, CNAS pentru digital, care nu are rută de rambursare; EMG Q2), fie **o revendicare clinică certificată** (MDR IIa+, AI Act cu risc ridicat din 2 august 2028; REG §2, §3).

**6. Unde se leagă de sesiunile anterioare** (pentru că L3 și L4 nu trebuiau repetate):
- „banii expuși” din L3 revine ca unealtă de vânzare (O24);
- rechemarea dentară din L4 se extinde doar spre urmarea pacienților de turism dentar (O7);
- ideea „Rămân” din L4 (muncitorii străini) nu e repetată. Medicina muncii apare aici cu alt job: închiderea recomandărilor după un examen obligatoriu (O2).
- Recepționistul vocal din REC poate fi un canal (apeluri de reminder), nu un produs separat aici.

### F2. Clasament preliminar, top 10

**Criteriile:**
- cât de clar e plătitorul;
- dacă fondatorul poate ajunge la el fizic, prin rețeaua din Oradea;
- categoria de reglementare;
- dacă accesul la date e posibil ca persoană împuternicită;
- venitul recurent;
- încadrarea în 10–12 ore pe săptămână;
- forța dovezilor;
- concurența;
- drumul spre o platformă predictivă.

Clasamentul e **preliminar**: niciun cumpărător n-a fost întrebat încă.

**1. O2 — Registrul recomandărilor deschise după examenul de medicina muncii.**
- **De ce:**
  - obligație legală, recurentă, cu plătitor existent (RO §5);
  - cabinetele pot fi vizitate pe jos în Oradea;
  - categoria 1, cu bază legală clară pentru furnizor (Art. 9(2)(h));
  - „predicția” e ceasul pus de medic;
  - se extinde natural spre O9, O17, O11 și O25;
  - construiește istoricul de bucle (§F1.3).
- **Risc:** valoarea per angajat e mică (80 lei pe an, deci produsul trebuie să coste puțin), vendorii existenți sunt necunoscuți, iar durerea nu e confirmată.

**2. O1 — Navigatorul FIT+ → colonoscopie pentru ROCCAS 4 NV.**
- **De ce:**
  - cea mai puternică dovadă pentru efectul urmăririi;
  - program finanțat până în 2029, care include Bihorul;
  - cifrele arată presiune de capacitate (calculul meu: ~285 de pozitivi peste ținta de colonoscopii);
  - dă credibilitate „preventivă” și o referință publică;
  - se poate replica la celelalte programe regionale.
- **Risc:** subcontractare în regim de proiect UE, un singur cumpărător, software existent necunoscut, identitatea partenerilor neverificată.

**3. O9 — „Ziua de prevenție” la locul de muncă**, ca a doua treaptă a O2.
- **De ce:** dovada din ACCESS (testul în aceeași vizită); același cumpărător ca O2; venit mai mare per angajator.
- **Risc:** depinde de parteneri (laborator, program), iar apetitul angajatorilor e neverificat.

**4. O3 — Inbox pentru rezultatele în afara intervalului, la laboratoarele independente.**
- **De ce:** gol clar de urmărire, presiune GDPR (amenzi pentru WhatsApp și e-mail), drum spre un activ longitudinal de date de laborator.
- **Risc:** laboratoarele din Oradea sunt mai ales în rețele; nu există date românești despre gol; încrederea în mesajele scrise de AI e scăzută (MKOR).

**5. O8 — Rechemarea pentru pachetul CNAS 40+/60+ la medicii de familie.**
- **De ce:** pachet gratuit din 2026, o bază uriașă de eligibili, bani publici de prevenție care trec prin medicul de familie.
- **Risc:** nu știm dacă medicul are un motiv financiar să cumpere; programele de cabinet n-au API.

**6. O15 — Componentele EHDS pentru vendorii locali.**
- **De ce:** termene legale datate (2029/2031); avantajul real al fondatorului pe PL/SQL și Oracle; B2B2B, cu puțini clienți mari.
- **Risc:** vânzarea vine abia în 2027–2028; datele EHDS sunt în conflict între surse; concurență open-source; regulile românești lipsesc.

**7. O12 — Auditul „pauza” (dez-implementare).**
- **De ce:** axă nouă, singura care nu e „mai multă urmărire”; plătitorul are un motiv (daune +~30% față de prime +12–13%); categoria 3, la nivel de populație.
- **Risc:** fondatorul n-are acces la asigurători; e nevoie de partener clinic; seamănă cu consultanța.

**8. O11 — Meniul fix de prevenție („automatul”).**
- **De ce:** folosește un buget existent și plafonat fiscal; e bazat pe dovezi; e simplu de explicat.
- **Risc:** e nevoie de laborator și medic partener; regulile fiscale trebuie verificate; concurența abonamentelor marilor rețele.

**9. O16 — Jurnalul de acces și cererile de acces la dosar.**
- **De ce:** amenzi ANSPDCP reale; dreptul de a vedea cine ți-a accesat datele vine prin EHDS; reglementare ușoară; se vinde ca protecție.
- **Risc:** valoare mică pe client; clinicile cumpără conformitate abia după o amendă.

**10. O4 — Navigatorul după notificarea de la ceas.**
- **De ce:** wearable-urile generează cerere, clinica are venit din testul de confirmare, iar povestea „predictivă” e bună.
- **Risc:** volumul e necunoscut; probabil e un modul, nu un produs.

**În afara clasamentului, dar utile:**
- **O24** (auditul „bani expuși”) e unealta de vânzare pentru O2, O3, O7 și O8.
- **O25** (predicția buclelor care nu se închid) e etapa a doua a oricăruia din top 5.
- **O18** (dispeceratul) e modulul diferențiator al O1.

### F3. Cei mai slabi supraviețuitori (păstrați, dar numiți)

| # | De ce e slab |
|---|---|
| O6 | la granița triajului; risc de răspundere pentru semnale ratate |
| O13 | niciun plătitor DPP în România |
| O14 | depinde complet de un API e-SănătateaMea care n-a fost găsit |
| O19 | alertarea e MDR IIa; nu există rambursare în România |
| O20 | n-am găsit cumpărători români; opțiune pentru 2028+ |
| O22 | bugete mici, piață fragmentată, cămine neverificate |
| O23 | n-are plătitor |
| O26 | B2C, cu mult timp de om |
| O5 | nu știm dacă medicii de familie plătesc |
| O21 | răspunderea pentru erorile de extracție; încredere scăzută |

**De mijloc:** O7 (aceeași familie de cumpărător ca L4), O10 (marile rețele își fac singure software-ul), O17 (strategică, dar cu piață necunoscută), O18 (mai bun ca modul).

### F4. Fundături (lăsate vizibile)

| Fundătura | De ce moare | Unde e dovada |
|---|---|---|
| Model propriu de risc / model fundațional | doar acuratețe retrospectivă, acces la date grele, MDR IIa | ȘTI KQ1 aria 2 (Delphi-2M, Foresight); REG §2 |
| Calculator SCORE2/QRISK în fluxul medicului | IIa; în UE nu există excepție ca în SUA (inversarea 8, moartă) | REG §2 (tabel), §8 |
| Chatbot de triaj sau verificator de simptome pentru pacient | IIa+; Anexa III din AI Act pentru triajul de urgență; Platform24 pus sub supraveghere | REG §2, §3; CEE Q3 ← SVT |
| RPM de sine stătător, cu alerte automate | MDSW IIa/IIb; nicio rambursare găsită în România | REG §2; MON §2 (Gaps) |
| PHR sau portofel de sănătate pentru consumator | eșecurile Google Health și HealthVault; plătesc doar „membrii captivi” | MON §5; EMG Q2 |
| Abonament de analize direct către consumator, ca Function, în România | laboratoarele sunt chiar mărcile de consum; Aware a intrat în insolvență | CONS KQ2, KQ4 |
| Clinică de scanare de corp întreg, tip Neko | capital (peste 960 mil. USD în rundele B și C); ACR recomandă împotrivă | CONS; ȘTI KQ1 aria 3 |
| Tablouri de stratificare a riscului vândute ca „reduc internările” | PRISMATIC a crescut utilizarea; Camden n-a avut efect | ȘTI KQ1 aria 6 |
| Scrib AI general în română | concurenți foarte finanțați (Tandem 160 mil. USD, Heidi ~340 mil. USD); funcțiile avansate alunecă în IIa | EMG Q1-F; B2B |
| Export prin DiGA/PECAN | marcaj CE plus RCT; plătitorul tăie prețuri | EMG Q2; CEE Q1 |
| Software pentru centrele germane de telemonitorizare (TMZ), ca export | piața rambursată există (EBM, GOP 40909), dar alertarea RPM e MDSW IIa; limbă germană; reguli KV de asigurarea calității; nicio dovadă de gol de software. **Moartă pentru acest fondator.** | MON §2 ← KBV; REG §2 |
| Platformă de federated learning | o problemă de guvernanță, nu de cod | EMG Q1-E ← Univ. Turku |
| Analiza poverii de alerte pentru spitalele românești | n-am găsit AI cu alerte instalat; achiziții publice; ieșirea Comarch | ȘTI KQ4; CEE Q1 |

**Abandonate în tehnici:**
- concept fan: A4 (model mai precis) tăiată; B4 marcată evidentă și slabă;
- analogie: colonia de furnici; triajul de la urgențe, exclus din start ca analogie de suprafață;
- random stimulus: scrisorile nelivrate, maiaua, cvorumul, steaua moartă;
- inversare: răsturnarea 8, moartă.

### F5. Ce ar schimba clasamentul

Acestea nu sunt un plan. Sunt necunoscutele care, aflate, ar muta pozițiile cel mai mult:
1. **O2:** există în Bihor cabinete independente de medicina muncii care țin recomandările și ar plăti pentru un registru? Ce program folosesc azi? (RO §7, Gaps; RO §2, Gaps)
2. **O1:** cine răspunde de Bihor în ROCCAS 4 NV, ce software folosește consorțiul și dacă pozitivii FIT chiar așteaptă colonoscopia. Cât e pozitivitatea reală în NV?
3. **O3:** există laboratoare independente în Oradea, cu program propriu? (RO §7, Gaps)
4. **O8:** cât plătește CNAS medicului de familie per serviciu de prevenție? Lipsește din note.
5. **O15:** când apar regulile românești de aplicare a EHDS și dacă vendorii locali au bugetat ceva (EMG Q1-D).
6. **O14:** are e-SănătateaMea un API pentru terți? (RO §4)
7. **Peste tot:** cât plătesc clinicile românești pentru unelte de rechemare. N-am găsit niciun preț de referință european specific pentru rechemare (B2B Q4, Gaps).

### F6. Cum ar putea crește spre o platformă predictivă (inferență, nu plan)

- **Etapa 1 (primul an):** un registru de bucle deschise în categoria 1, cu reguli deterministe puse de medic sau de program (O2 sau O1). Fondatorul e persoană împuternicită. Primele luni la fiecare client merg ca serviciu (inversarea 7). Se strânge istoricul buclelor cu consimțământ granular, explicit, pentru dezvoltarea viitoare a produsului (REG §8, punctul de intrare 4).
- **Etapa 2 (anul 2–3):**
  - același nucleu, cu mai mulți clienți (O9, O8, O3);
  - predicție operațională cu grup de control (O25);
  - componentele EHDS (O15), când apar regulile românești.
- **Etapa 3 (2028–2031):**
  - „stratul de buclă” devine locul unde se conectează modele de risc ale unor vendori marcați CE: vendorul poartă MDR, fondatorul poartă urmărirea;
  - folosirea secundară a datelor prin EHDS, când România are un organism de acces la date (~2029+, REG §4).
- **De urmărit pe drum:**
  - reforma MDR, care ar putea muta mai mult software în clasa I (votul în comisia SANT pe 3 decembrie 2026, posibil până în 2028; REG §2);
  - AI Act Anexa I, pe 2 august 2028 (REG §3);
  - PLD, pe 9 decembrie 2026: din acel moment software-ul e produs cu răspundere strictă (REG §7).

### F7. Mișcări următoare (alegerea e a fondatorului)

- **Un al doilea lot de random stimulus**, tras doar pe axa „dez-implementare / buget curat” (O11, O12), singura axă nouă.
- **Un nou concept fan, pornit de la O2** ca soluție curentă, ca să vedem ce alte joburi are furnizorul de medicina muncii.
- **Six hats pe alegerea dintre O2 și O1**, dacă decizia pare luată prea repede.
- **Stop aici.** Clasamentul de mai sus e o hartă, nu o recomandare de angajament.
