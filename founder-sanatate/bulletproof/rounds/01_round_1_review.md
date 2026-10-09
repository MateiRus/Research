# Runda 1: review-ul investitorului pentru „Scadențar MM” (planul din runda 0)

**Investitorul (persona):** partener la un fond european de seed / Series A pe digital health, cu portofoliu în CEE. Cunoaște piața privată din România: MedLife (care a cumpărat Medicris Oradea), Regina Maria (acum a finlandezilor de la Mehiläinen), Medicover (Synevo, Spitalul Pelican) și vendorii de software de medicina muncii (BizMedica/Setrio, MedExam/DMV Consult, Qmedical, Charisma, MedSoft). E sceptic din principiu: a văzut multe „portaluri” care au devenit o bifă în produsul altcuiva.

**Ce evaluează:** dacă ar pune bani acum (pre-seed) sau ce ar trebui să vadă ca să revină. Pentru fiecare obiecție dă o **probabilitate de respingere dacă obiecția rămâne nerezolvată**. Probabilitatea nu e statistică: e cât de mult cântărește obiecția în decizia lui.

**Sursele:** fără cercetare web nouă. Faptele vin din notele de cercetare (abrevierile din `00_original_plan.md`). Ce e calcul sau judecată proprie e marcat.

---

## Verdictul pe scurt

**Nu investesc în forma asta.** Planul e cinstit despre limitele lui, iar asta îmi place. Dar tot ce susține „FUND IF” e simulat, golul de produs nu e verificat, modelul financiar nu are churn, iar „drumul spre predictiv” e o listă de speranțe, nu un plan cu porți. Pentru un fond de digital health, întrebarea nu e „poate aduce 1.600 € MRR?”, ci „de ce e asta începutul unei companii de prevenție și nu o funcție în programul altcuiva?”.

**Ce e puternic, ca să fie clar:**
- Fluxul e obligatoriu, recurent, plătit de angajator și datat (HG 355/2007 art. 20; Legea 319/2006 art. 39(4); RSMM §3).
- Concurența e documentată: MedLife vinde exact stratul pentru angajator (RSMM §1), deci cererea pentru el există cel puțin la rețele.
- Produsul e administrativ (REG §8, „logistica medicinei muncii”), deci evită MDR la start.
- Capitalul nu e problema: ~3,8k € din 25k € (`cfo/A_cfo.md`).
- Fondatorul poate ajunge fizic la cumpărători numărabili (RSMM §5).

---

## Obiecțiile (în ordinea gravității)

### 1. Nu există nicio dovadă reală de cerere, iar semnalul simulat e fragil
- **Probabilitatea de respingere dacă rămâne nerezolvată: 85%**
- **Logica:** Tot ce împinge A pe primul loc e produs de modele de limbaj: board-ul (3 sub-agenți) și panelul (20 de sub-agenți, același model, răspunsuri corelate). Planul o spune singur. Mai grav: aceeași idee, reformulată, a căzut de la 7/20 la 3/20. Un semnal care se înjumătățește când schimbi un paragraf nu e un semnal de cerere, e un semnal de formulare. Verdictul „Profitable” se răstoarnă la −20% volum.
- **Dovezi:**
  - panelul v1: 35%; panelul v2: 15%; diferența poate fi zgomot la n=20 (AF §C0, §C3; `panels/A2/results.md`);
  - „Lipsesc: orice dovadă că un cabinet independent plătește pentru asta și orice sondaj despre durerea angajatorilor” (AF §B #1; RSMM §3, Gaps);
  - verdictul `compile.py`: „Profitable” cu +534 € în anul 1; −125 € la −20% volum (AF §E1);
  - nicio condiție de bani a board-ului nu e îndeplinită (AF §D3).
- **Ce m-ar face să schimb votul:** pre-vânzări plătite de la cabinete reale, plus o măsurătoare făcută pe exportul lor: câte fișe sunt azi expirate sau aproape de expirare și câte ore pe săptămână pierde asistenta cu telefoanele.

### 2. Golul s-ar putea să nu existe, iar dacă există, e o funcție pe care incumbenții o copiază
- **Probabilitatea de respingere dacă rămâne nerezolvată: 80%**
- **Logica:** Cel puțin șase programe românești emit deja fișa de aptitudine și țin firmele-client. Unul importă deja listele angajaților din Excel. Un portal de status peste datele pe care ei le au deja e, pentru ei, o funcție de câteva săptămâni, nu un produs. Planul nu știe dacă vreunul îl are deja. Toți trei membrii board-ului au pus „copiat în luna 6” printre riscurile principale. Nu văd nimic 10× mai bun, doar „ceva ce lipsește poate”.
- **Dovezi:**
  - BizMedica MM (Setrio) „importă lista angajaților firmei-client din Excel”; Qmedical „gestionează firmele-client cu posturi pe risc și produce rapoarte complexe”; MedExam „monitorizează activitatea asistentei” (RSMM §1);
  - „Nu s-a găsit preț, API sau număr de clienți” pentru niciunul dintre ele (RSMM §1, Gaps), deci nici funcțiile lor reale nu sunt cunoscute;
  - furnizorii își fac deja reclamă cu urmărirea scadențelor ca serviciu: One Medicina Muncii, HARDMED, M Hospital (RO §5);
  - board: risc „ridicat de toți trei” (`board/board.md`, §2 punctul 2); lentila Monopol: „Nothing here is 10x better” (`board/monopoly.md`).
- **Ce m-ar face să schimb votul:** o verificare directă (demo sau discuție) a celor 5–6 programe, făcută înainte de orice linie de cod, și un răspuns clar la „ce rămâne al tău dacă BizMedica adaugă portalul”.

### 3. Piața adresabilă e prea mică și nenumărată; planul își calculează singur plafonul
- **Probabilitatea de respingere dacă rămâne nerezolvată: 80%** (pentru un fond; pentru o afacere de nișă, mai puțin)
- **Logica:** Modelul se oprește la ~25 de clienți și ~1.625 € MRR, iar 3.000 € MRR cere 50 de cabinete, adică ~10% din toate cele listate în țară. În Oradea sunt ~6 cabinete independente identificate, cu proprietatea neverificată. Consolidarea merge în direcția greșită pentru acest cumpărător: rețelele cumpără independenții.
- **Dovezi:**
  - 508 cabinete MM listate de Romedic la nivel național, „director, nu recensământ” (RSMM §3);
  - ~6 cabinete aparent independente în Oradea, proprietatea neverificată (RSMM §5, Gaps);
  - Medicris (22.000+ abonați) a fost cumpărat de MedLife; rețelele au centre MM proprii în Oradea: MedLife Ronald Reagan, Regina Maria, Pelican/Medicover (RSMM §5; RO §7);
  - plafonul: ~25 de clienți la 10–12 h/săpt; 50 de cabinete pentru 3k € (AF §D2).
- **Calculul meu:**
  - la prețul din plan, chiar dacă **toate** cele 508 cabinete listate ar cumpăra: 508 × 65 € × 12 ≈ **396.000 €/an**. Asta e plafonul teoretic al stratului, nu o țintă;
  - dacă stratul s-ar plăti per angajat, cu 2–4 lei/angajat/an (ținta din AF §B #1) pentru toți cei 5,76 mil. de salariați: ~11,5–23 mil. lei/an ≈ **2,3–4,5 mil. €/an**. Dar rețelele nu cumpără (își fac singure software-ul; RO §1), deci partea accesibilă e o fracțiune necunoscută;
  - Bihorul are ~3,3% din salariații țării (187,3k din 5,76 mil.; RSMM §3). Dacă cabinetele listate ar urma aceeași proporție: ~16–17 cabinete listate în Bihor, de orice proprietar. Estimare grosieră.
- **Ce m-ar face să schimb votul:** o listă nominală de ≥20 de cabinete independente accesibile, cu programul folosit, și o explicație credibilă a pieței mai mari în care A e doar ușa de intrare.

### 4. „Drumul spre predictiv” e o poveste, nu un plan
- **Probabilitatea de respingere dacă rămâne nerezolvată: 70%**
- **Logica:** Pentru un fond de digital health, asta e întrebarea centrală. Planul spune singur că drumul e „inferență, nu plan”. Problemele:
  - **datele nu sunt ale tale.** Ca persoană împuternicită, nu poți folosi datele cabinetelor pentru propriile modele. Dacă o faci, devii operator și ai nevoie de o bază legală proprie (REG §1, Art. 28(10));
  - **datele MM sunt subțiri:** o categorie de aptitudine, o dată și un termen. Nu sunt valori clinice structurate;
  - **medicul MM nu deține urmarea:** rolul lui e aptitudinea; tratamentul aparține medicului de familie (RSMM §3, Inferences, „Against”);
  - **profilarea cu date de sănătate** cere consimțământ explicit sau o bază legală expresă (Legea 190/2018 art. 3; REG §1);
  - nu există porți: ce trebuie construit, validat, licențiat sau obținut prin parteneriat la fiecare etapă și când te oprești.
- **Dovezi:** AF §E2 (marcat „inferență, nu plan”); REG §1, §8 (punctul de intrare 4: datele cu consimțământ granular sunt singura rută directă spre un set de antrenare controlat de fondator); RSMM §3 („the OH doctor does not own the referral loop”); LAT §F1.2 (predicția ML abia în etapa 2, cu trei condiții).
- **Ce m-ar face să schimb votul:** un drum pe etape, fiecare cu: activul de date construit, baza legală pentru el, ce se validează, ce partener e necesar, ce costă și condiția de oprire.

### 5. Plătitorul e greșit, iar „paritatea cu MedLife” nu e paritate
- **Probabilitatea de respingere dacă rămâne nerezolvată: 70%**
- **Logica:** Plătește cabinetul, din marjă, dar valoarea o vede angajatorul. Cabinetele independente concurează pe preț la 80–110 lei/angajat/an. Mai important: rețelele nu câștigă clienți pentru că au un portal. Câștigă pentru că vând **pachetul**: abonament medical plus medicina muncii ca intrare obligatorie. Un portal nu-i dă independentului pachetul. Pitch-ul „paritate cu rețelele” a convins doar cabinetele care pierduseră deja clienți.
- **Dovezi:**
  - prețul MM: 80 lei/angajat/an, 110 lei pentru șoferi (RO §5 ← Medworks); „marja mică lasă buget mic” (AF §B #1);
  - ROMATSA: abonament + MM ≈ 1.800 lei/angajat/an; „banii stau în pachetul de abonament, cu MM ca intrare obligatorie” (RSMM §3, Inferences);
  - MedLife ~800.000 de angajați abonați, Regina Maria 780.000–850.000 de abonamente de la ~10.000–12.000 de companii (RSMM §4);
  - panel: „Costul de 59–99 € îl iau din marjă, iar clientul nu-mi dă un leu în plus” (`panels/A`, P015); la pitch-ul „paritate”, au cumpărat doar cei 3 „sub presiunea rețelelor” (`panels/A2/results.md`);
  - lentila Ofertă: „Durerea e slabă la cumpărător” (`board/offers.md`).
- **Ce m-ar face să schimb votul:** dovada că produsul îi aduce cabinetului bani sau timp măsurabil (ore de asistentă, clienți păstrați), nu doar o imagine mai modernă.

### 6. Modelul financiar e optimist în trei locuri care contează
- **Probabilitatea de respingere dacă rămâne nerezolvată: 65%**
- **Logica:**
  - **(a) Fără churn.** În 36 de luni, niciun cabinet nu pleacă (`cfo/A_36m.md`). Garanția de 90 de zile, pe care chiar oferta o estimează la „1 din 5 cer banii înapoi”, nu e în model (`plan/A/offer.md`).
  - **(b) Timpul nu încape.** CAC-ul e de 25–40 h de vânzare per client câștigat (`cfo/cfo-sources.md`). Capacitatea e ~52 h/lună. La 10 clienți: 25–40 h vânzare + ~10 h suport + 6–10 h onboarding = **41–60 h/lună** (calculul meu). Deci rampa de +1 client/lună nu ține după ~10 clienți fără să se oprească dezvoltarea.
  - **(c) Costul complet e negativ în anul 1:** −546 € cu timpul fondatorului la 20 €/h (AF §D2).
- **Calculul meu** (`bulletproof/model_36m.py`, aceleași intrări ca CFO, plus churn 1,5%/lună și 20% retururi la garanție):
  - anul 1: **−198 €** în loc de +534 €;
  - 1.000 € MRR în **luna 24** în loc de 18;
  - dacă și rampa încetinește la 0,6 clienți/lună după luna 12 (limita de timp de la punctul b): **1.000 € MRR nu vine în 36 de luni** (984 € în luna 36).
- **Ce m-ar face să schimb votul:** un model cu churn, retururi și un buget de ore pe lună care încape în 10–12 h/săpt, plus o metrică de CAC în ore măsurată pe primii clienți.

### 7. Încrederea și datele: un SRL necunoscut cu datele a mii de angajați
- **Probabilitatea de respingere dacă rămâne nerezolvată: 60%**
- **Logica:** Încrederea a fost al doilea motiv de refuz în v1 și primul în v2. Pe lângă teama de amenzi, există o întrebare juridică nerezolvată: **ce are voie să vadă angajatorul**. Practica „angajatorul primește doar concluzia” nu e verificată, iar o listă de „recomandări apt condiționat deschise” poate dezvălui indirect date de sănătate. Datele care dezvăluie indirect starea de sănătate sunt tot date de categorie specială (REG §1, Inferences, ← CJUE C-184/20, C-21/23).
- **Dovezi:**
  - trust: 4/13 refuzuri în v1, 7/17 în v2 (`panels/A`, `panels/A2/results.md`);
  - amenzi ANSPDCP în sectorul medical, inclusiv pentru date trimise pe WhatsApp sau e-mail (RO §3);
  - „angajatorul primește doar concluzia de aptitudine” e BK și trebuie verificat (REG §6, Gaps); fișa are un exemplar pentru angajator (RSMM §3 ← HG 355/2007, anexa 5);
  - CNP-ul pe interes legitim cere garanții specifice (Legea 190/2018 art. 4; REG §1);
  - confidențialitatea (Legea 46/2003 art. 21–22; REG §1).
- **Ce m-ar face să schimb votul:** un model de date minim scris (ce câmpuri, cine vede ce), o opinie juridică pe „ce vede angajatorul” înainte de a construi portalul, și dovezi de securitate pe care un cabinet mic le poate înțelege.

### 8. Cusătura de date: fără API, portalul e cât de actual e ultimul export
- **Probabilitatea de respingere dacă rămâne nerezolvată: 55%**
- **Logica:** Un portal care arată „depășit” pentru un angajat deja examinat strică încrederea angajatorului **în cabinet**, nu doar în produs. Fiecare cabinet are alt program, alt export și altă disciplină. Onboarding-ul de 6–10 h e o estimare. „Integrare directă, fără import manual” e prima condiție care ar întoarce un „nu” în panel.
- **Dovezi:** niciun API public la programele MM (RSMM §1, Takeaway, Gaps); lentila Produs: „cusătura import–export” e riscul nr. 1 (`board/product.md`); panel: integrarea directă apare de 5 ori în „ce ar întoarce un nu” (`panels/A/results.md`).
- **Ce m-ar face să schimb votul:** două exporturi reale obținute în <30 de minute, timpul real de curățare măsurat la primul pilot și o regulă de produs pentru datele învechite.

### 9. Un fondator la 10–12 ore pe săptămână nu poate opera un serviciu B2B pe care îl văd și clienții clientului
- **Probabilitatea de respingere dacă rămâne nerezolvată: 50%**
- **Logica:** Produsul are doi clienți: cabinetul și angajatorii lui. Un import ratat într-o săptămână de concediu e vizibil pentru zeci de HR-uri. Nu există plan de suport, de continuitate sau de angajare. Pentru 3k € MRR planul cere ~20 h/săpt din anul 2, dar nu spune dacă fondatorul le are.
- **Dovezi:** „Timpul fondatorului, nu capitalul, e constrângerea” (AF, „Pe scurt”); scenariul „spre 3k” cere ~20 h/săpt din luna 13 (AF §D2); panel: „Ce fac dacă firma dispare?” (`plan/A/offer.md`, problema 7); lentila Produs: „doi clienți, două experiențe” (`board/product.md`).
- **Ce m-ar face să schimb votul:** un buget de ore pe lună, o regulă de suport scrisă, documentație pentru continuitate și un prag clar la care se angajează ajutor.

### 10. Răspunderea și granița de reglementare la etapele următoare
- **Probabilitatea de respingere dacă rămâne nerezolvată: 30%**
- **Logica:** Etapa 1 e curată. Dar drumul promis (urmarea constatărilor anormale, predicție) se apropie de MDR, iar orice versiune lansată după 9.12.2026 e „produs” cu răspundere strictă. Formularea din marketing poate schimba singură clasificarea.
- **Dovezi:**
  - PLD: software-ul e produs din 9.12.2026; răspunderea față de persoana vătămată nu se poate exclude prin contract (REG §7);
  - scopul declarat, inclusiv în materialele de vânzare, decide calificarea MDR (REG §2, Art. 2(12));
  - „Evidențiază valori anormale și prezice deteriorarea” e categoria 4, posibil IVDR (REG §8);
  - SMS-urile automate cer consimțământ (Legea 506/2004; RO §3).
- **Ce m-ar face să schimb votul:** o declarație de scop scrisă, o listă de cuvinte interzise în marketing și o regulă: nimic din etapele 2–4 nu se lansează fără opinie scrisă.

---

## Tabelul obiecțiilor

| # | Obiecția | Probabilitate de respingere |
|---:|---|---:|
| 1 | Nicio dovadă reală de cerere; semnal simulat fragil | 85% |
| 2 | Golul neverificat; funcție copiabilă de incumbenți | 80% |
| 3 | Piață mică, nenumărată; plafon ~1,6k € MRR | 80% |
| 4 | Drumul spre predictiv e poveste, fără porți | 70% |
| 5 | Plătitor greșit; rețelele câștigă prin pachet, nu prin portal | 70% |
| 6 | Model financiar fără churn și fără limită de timp | 65% |
| 7 | Încredere, date, „ce vede angajatorul” | 60% |
| 8 | Cusătura exporturilor fără API | 55% |
| 9 | Fondator solo la 10–12 h/săpt, fără plan de operare | 50% |
| 10 | Răspundere și granița MDR la etapele următoare | 30% |

**Ce cer înainte de o a doua discuție:** dovezi de cerere reale, o verificare a vendorilor, un model cu churn și timp, și un drum spre predictiv cu porți și condiții de oprire.
