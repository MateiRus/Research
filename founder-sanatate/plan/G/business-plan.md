# Controale pierdute: lista pacienților cronici care au depășit controlul stabilit de medic · Business plan

**Verdict: Not yet**

- ✓ Each client-lună earns $84.50 before fixed costs (95% contribution).
- ✗ Year 1 operating LOSS: $1,070.
- ✓ Break-even is 3 client-lunăs a day against a capacity of 13.
- ✗ 2 of 20 simulated buyers buy (10%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $89.00 a client-lună |
| Profit margin at plan | 73% per client-lună |
| Break-even | 3 client-lunăs a day |
| Year 1 operating profit | $-1,070 |
| Startup spend | $3,900 |
| Cash needed before it pays for itself | $5,233 |
| Startup money earned back | not in year 1 |
| Buyer panel | 2 buy · 18 pass |

## The idea

- Ce este: o listă săptămânală pentru clinicile de boli cronice cu pacienții la care medicul a stabilit un control și care au depășit data fără să se programeze. Asistenta primește lista de sunat. SMS-ul pleacă doar la pacienții care și-au dat consimțământul, cu un text aprobat de directorul medical și fără nicio mențiune medicală.
- Pentru cine: clinici independente multi-specialitate cu diabet, cardiologie și endocrinologie (de ex. GrandMed, NewMedics, Medena în Oradea), apoi din Cluj și Timișoara.
- Ce vinde, la ce preț: 89 €/lună pe locație, după un audit gratuit pe 6 luni de date pseudonimizate. Garanție: lunile din primele 3 în care se programează mai puțin de 15 controale nu se plătesc.
- Unde și cum: SaaS în UE. Exportul automat e configurat de fondator la sediu. Vânzarea se face prin vizite și audit.
- Buget și constrângeri: ~25.000 €, 10–12 h/săpt. Produsul rămâne administrativ: termenele sunt ale medicului, fără interpretarea rezultatelor (opinie MDR scrisă înainte de orice extindere spre rezultate de laborator).

## Summary

**Ce e și pentru cine.** O listă săptămânală pentru clinicile independente de boli cronice cu pacienții care au depășit controlul stabilit de medic fără să se programeze. Asistenta sună. SMS-ul pleacă doar cu consimțământ, fără mențiuni medicale.

**Verdictul (calculat de `compile.py`): Not yet.**
- Profitul operațional din anul 1 e de −1.070 €, din cauza rampei lente (audit, apoi integrare per clinică).
- Doar 2 din 20 de cumpărători simulați cumpără (10%, sub pragul de 25%); la oferta inițială, 0 din 20.
- Contribuția e mare (84,5 €), dar 1.000 € MRR vine abia în ~luna 27, iar plafonul de timp e ~13 clinici.

**Panel și board:**
- Board-ul o preferă ca valoare (media 6,0; lentilele Ofertă și Monopol o pun pe primul loc).
- Panelul o respinge pe încredere („date de pacienți la un SRL necunoscut”) și pe integrare („exportul nu-l știe face nimeni”).

**Ce trebuie să se schimbe:** referințe reale (după primii clienți A), 2 audituri reale care arată zeci de controale pierdute și o opinie MDR scrisă. Skill-urile care o schimbă sunt `founder-offer` (făcut, v2) și testul real.

**Lucrul de făcut:** după primii 2 clienți A, cere unei clinici cronice din Oradea un export pseudonimizat pe 6 luni pentru un audit gratuit.

## What the board said

**Cum a rulat.** Trei membri de board, fiecare un sub-agent separat (`claude -p`, model opus, fără unelte). Fiecare a primit doar `brief.md` și o singură lentilă din `founder-board/lenses.md`. Lentilele sunt rezumate ale unor cadre publicate; membrii nu vorbesc în numele autorilor. Memoriile complete sunt în `offers.md`, `monopoly.md` și `product.md` (lentila „Monopol” a răspuns în engleză, deși i s-a cerut româna; textul e păstrat neschimbat). Board-ul **nu** a văzut rezultatele panelului de cumpărători (au rulat în paralel).

### 1. Votul

| Idee | Ofertă | Monopol | Produs | Media | Voturi |
|---|---:|---:|---:|---:|---|
| **A** Scadențar MM + portal angajator (prin cabinete) | 6 FUND IF | 5 FUND IF | 6 FUND IF | **5,7** | 3 × FUND IF |
| **G** Bucle deschise (clinici cronice, laboratoare, MF) | 7 FUND IF | 6 FUND IF | 5 FUND IF | **6,0** | 3 × FUND IF |
| **B** Scadențar MM direct la HR | 4 PASS | 3 PASS | 7 FUND IF | 4,7 | 2 PASS, 1 FUND IF |
| **K** Turism dentar | 5 FUND IF | 3 PASS | 4 PASS | 4,0 | 2 PASS, 1 FUND IF |
| **H** Rechemare CNAS 40+/60+ | 3 PASS | 3 PASS | 3 PASS | 3,0 | 3 × PASS |

**Recomandarea fiecărei lentile pentru primul produs:**
- **Ofertă:** G, apoi A.
- **Monopol:** G, apoi A.
- **Produs:** B, apoi A. A e „același nucleu, cu datele venite de la cine emite fișa”.

**A e singura idee pe care toți trei o pun în primele două.**

### 2. Riscurile ridicate de mai mulți membri (primele)

1. **Piața locală e prea mică pentru ținta de MRR** (A, G, B; toți trei). În Oradea sunt ~6 cabinete MM independente, ~3 clinici cronice și 1 laborator. La 59–129 EUR, pentru 1–3k EUR MRR sunt necesari 8–50 de clienți, deci vânzare în tot Nord-Vestul sau la nivel național din primul an.
2. **Copierea în luna 6 / funcția devine o bifă** (A: toți trei; B: Ofertă și Monopol). Cele 6 programe MM existente (BizMedica importă deja Excel) și portalul MedLife pot închide golul.
3. **Lipsa dovezilor locale de plată și de durere** (A, G; toți trei). Nu există sondaj, măsurătoare sau pre-vânzare.
4. **Cusătura de date: fără API, totul depinde de exporturi** (A: Produs și Monopol; G: Ofertă și Produs). Un portal care arată „depășit” pentru cineva deja examinat distruge încrederea.
5. **Granița MDR la bucla „rezultat în afara intervalului”** (G: Monopol și Produs). Cere o opinie scrisă de reglementare înainte de a fi construită.
6. **H: cumpărătorul n-are bani și statul poate absorbi funcția** (toți trei).

### 3. Condițiile, unite într-o listă de verificat

- [ ] **A:** 3 cabinete independente semnează pre-vânzări plătite **înainte** de construcție (toți trei). → verificat parțial în panel (simulat); confirmare reală în validarea de 90 de zile.
- [ ] **A:** o listă verificată cu ≥20 de cabinete independente accesibile în Nord-Vest (Monopol). → validarea de 90 de zile.
- [ ] **A:** confirmarea că BizMedica MM, MedExam etc. **nu** au deja un portal pentru angajator (Ofertă). → nu se poate din note; de întrebat vendorii și cabinetele.
- [ ] **A:** v1 face un singur lucru: statusul în termen / depășit, actualizat cel puțin săptămânal (Produs). → integrat în oferta v2.
- [ ] **A:** oferta reformulată în jurul păstrării și câștigării angajatorilor, cu o garanție (Ofertă). → integrat în oferta v2 (garanție de 90 de zile).
- [ ] **G:** 2 audituri reale pe 6 luni de date, cu recuperări de cel puțin 5 ori prețul, și o conversie la plată (Ofertă, Monopol, Produs).
- [ ] **G:** importul demonstrat fără muncă manuală zilnică (Ofertă). → integrat în oferta v2 (export automat configurat de fondator).
- [ ] **G:** v1 tăiat la o singură buclă, „controale scadente neprogramate”, pentru un singur tip de client (Produs). → oferta v2.
- [ ] **G:** opinie de reglementare scrisă înainte de bucla de laborator (Monopol, Produs).
- [ ] **B:** cel mult canalul angajatorului pentru A, nu produs separat (Ofertă, Monopol). Dacă e testat: 5 pre-vânzări și un flux de actualizare de un clic după examen (Produs).
- [ ] **K:** volumul de pacienți străini pe clinică și 2 pre-vânzări (Ofertă). Altfel PASS.
- [ ] **H:** niciuna; PASS unanim.

### 4. Cea mai puternică versiune pe care o vede board-ul

Board-ul nu vede cinci afaceri, ci **un singur motor**: o listă de termene stabilite de un profesionist (medicul MM, medicul curant), ținută la zi din exporturile programelor existente, cu un om care acționează și un jurnal. Motorul are **două uși de intrare**:

- **Ușa A** (cabinetele MM independente, cu portal pentru angajator) e cea mai rapidă la bani. Cumpărătorul e numărabil și accesibil fizic, iar motivul de cumpărare e concret: paritatea cu portalul MedLife. Datele nu sunt clinice, iar riscul de reglementare e minim.
- **Ușa G** (controalele scadente la clinicile de boli cronice) e cea mai valoroasă strategic. Duce direct spre prevenție, iar know-how-ul de integrare cu programe fără API devine o barieră. Dar golul e nedemonstrat în România, iar oferta inițială n-a convins pe nimeni din panel.

B nu e o afacere separată, ci partea de angajator a lui A. K și H nu trec.

**Dezacordul real:** lentilele Ofertă și Monopol ar începe cu G pentru valoare și secret. Lentila Produs ar începe cu forma cea mai simplă (B, apoi A). Panelul de cumpărători (§C3 în `analiza_founder.md`) înclină balanța spre A ca prim produs. Și varianta propusă aici diferă de ce a fost propus: nu „un produs de medicina muncii” și nici „un produs de rechemare”, ci un motor comun, cu A ca primă ușă și G ca a doua, deschisă doar după un audit real.

## The competition

**Limita acestui pas.** Skill-ul `founder-competitors` cere surse publice citite acum, cu link, inclusiv recenziile clienților. Sarcina interzice cercetarea web nouă, așa că **toate rândurile vin din notele de cercetare** (coloana `note_source` din `competitors.csv`), cu link-urile citate acolo. **Pasul 3 (recenziile, 1–3 stele) nu s-a putut face:** notele nu conțin recenzii pentru niciunul dintre acești concurenți. În locul lor folosesc obiecțiile din panelul de cumpărători, marcate ca simulate. Nu am inventat niciun concurent, preț sau rating.

### 1. Tabelul, după cât de direct concurează

#### A · Scadențar MM + portal angajator (prin cabinete independente)

| Concurent | Tip | Preț comparabil | Ce vinde | Sursa |
|---|---|---|---|---|
| BizMedica MM (Setrio) | direct | nepublicat (versiunea pentru medicina de familie: 159–199 RON/lună, preț vechi) | fișa de aptitudine, dosarul, **import Excel** al angajaților | RSMM §1; RO §2 |
| MedExam (DMV Consult) | direct | nepublicat | cabinet MM fără hârtie, rapoarte | RSMM §1 |
| Qmedical | direct | nepublicat | firmele-client, posturile pe risc, rapoarte | RSMM §1 |
| Charisma (modul MM) | direct | nepublicat | fișa, evoluția angajatului | RSMM §1 |
| MedSoft (modul MM) | direct | ofertă la cerere | modul MM | RSMM §1 |
| **MedLife Self-Service + MM Express** | indirect (rețea) | inclus | **portal angajator** cu statusul MM în timp real; fișa în 24h | RSMM §1 |
| Regina Maria MM Oradea | indirect (rețea) | nepublicat | MM cu programare online | RSMM §5 |
| Urmărirea scadențelor ca serviciu (One Medicina Muncii, HARDMED, M Hospital) | indirect | inclus în 80–110 lei/angajat/an | evidență digitală, urmărirea scadențelor | RO §5 |
| Excel + telefonul asistentei | substitut | 0 € | — | panel A |

#### G · Bucle deschise (clinici cronice)

| Concurent | Tip | Preț comparabil | Ce vinde | Sursa |
|---|---|---|---|---|
| MediNote | indirect | 50 lei/utilizator/lună, cu SMS inclus | program de clinică cu remindere | RO §2 |
| icMED + icMED.Mobile | indirect | nepublicat | program de clinică cu aplicație pentru pacient | RSMM §1 |
| Zarina CRM Medical | indirect | 2.990 € + TVA, licență unică (licența CRM generală) | CRM cu WhatsApp/SMS și automatizări | RSMM §1 |
| VAstoma, DentAIM, AI Frontdesk | indirect | nepublicat (agenți vocali români ~299–499 €/lună) | remindere WhatsApp și apeluri AI | EMG §L, Q3 |
| Callio | indirect | 139/189/299 €/lună | agent vocal la recepție | RO §2 |
| receptie-clinica.ai | indirect | 1.200 € setup + 150 €/lună | recepționist AI | RO §2 |
| Asistentul AI MedLife, Synevo Decoder, aplicația Regina Maria | indirect (rețele, nu se vând independenților) | inclus | interpretarea rezultatelor, la inițiativa pacientului | RSMM §2 |
| e-SănătateaMea | substitut (stat) | gratuit | programări obligatorii pentru furnizorii CNAS din T4 2026 | RO §4; RSMM §6 |
| Lighthouse 360 (SUA) | doar ancoră de preț | 329 $/lună + 299 $ setup | rechemare dentară legată de PMS | B2B Q4 |
| Asistenta cu telefonul / pacientul revine singur | substitut | 0 € | — | panel G |

#### B · Scadențar MM direct la HR

| Concurent | Tip | Preț | Sursa |
|---|---|---|---|
| Excel + furnizorul MM care anunță scadențele | substitut | 0 € | panel B; RO §5 |
| MedLife Self-Service (pentru clienții MedLife) | indirect | inclus | RSMM §1 |
| Platforme HR/salarizare cu evidența fișelor | indirect | **neverificat**: notele nu le documentează | — |

### 2. Intervalul de preț pentru produsul comparabil

- **A:** **niciun preț publicat pentru software de medicina muncii** (RSMM §1, Gaps). Cele mai apropiate ancore sunt programele de clinică:
  - MediNote, ~10 €/utilizator/lună (50 lei);
  - BizMedica pentru medicina de familie, ~31–39 €/lună (preț vechi);
  - Zarina, 2.990 € licență unică, adică ~83 €/lună pe 3 ani (calculul meu).
  - **Cel mai mic ~10 €, median ~35 €, cel mai mare necunoscut.**
- **G:** de la ~10 € (reminder inclus în MediNote) la 24–59 € (AllAI; RO §2), 139–299 € (Callio), 150 € plus setup (receptie-clinica.ai) și 299–499 € (agenți vocali; EMG Q3). **Mediana ancorelor românești e ~150 €/lună**, dar acestea sunt agenți vocali la recepție, nu liste de rechemare.
- **B:** 0 € (Excel, serviciul inclus de furnizorul MM).

### 3. Harta de poziționare (în text)

**A:** axa X = cine deține relația cu angajatorul (rețea ↔ cabinet independent); axa Y = ce vede angajatorul (doar fișa pe hârtie sau PDF ↔ portal de status la zi).
- **Sus-stânga:** MedLife (rețea, cu portal).
- **Jos-dreapta:** cabinetele independente cu BizMedica MM, MedExam, Qmedical, Charisma sau MedSoft. Notele nu documentează un portal pentru angajator la niciunul dintre aceste programe; **trebuie verificat** la vendori.
- **Mijloc:** furnizorii care vând urmărirea scadențelor ca serviciu.
- **Golul:** sus-dreapta, adică un cabinet independent cu portal pentru angajator.

**G:** axa X = reactiv (reminder la o programare care există deja) ↔ proactiv (găsește pacientul care n-a programat nimic); axa Y = integrat în programul clinicii ↔ separat.
- MediNote și icMED: integrat, reactiv.
- VAstoma, DentAIM, Callio, AI Frontdesk: separat, reactiv (recepție, apeluri).
- Rețelele: proactiv, dar doar pentru pacienții lor și la inițiativa pacientului.
- **Golul:** proactiv, pentru clinici independente, pe termene stabilite de medic.

### 4. Plângerile (în locul recenziilor)

Notele n-au recenzii pentru acești concurenți. Obiecțiile din panelurile simulate (`panels/*/results.md`) sunt cel mai apropiat substitut. **Nu sunt recenzii reale.** Ordonate după frecvență:
- **A:** „programul MM/Excel-ul îmi arată deja scadențele” (6/13 refuzuri); încrederea în date și teama de amenzi ANSPDCP (4/13); prețul și „nu aduce bani imediat” (2/13).
- **G:** încrederea în date și teama de amenzi GDPR (7/20); „programul trimite deja SMS” (6/20); prețul față de capitație la medicii de familie (3/20); exportul zilnic pe care nimeni nu știe să-l facă (2/20).
- **B:** „Excel și furnizorul MM ne anunță” (10/18); „nu e o problemă reală” (5/18).

### 5. Golul

- **A:** un **portal pentru angajator cu marca cabinetului independent**, alimentat din programul MM existent. E legat de dovezi: MedLife vinde exact asta (RSMM §1), iar cabinetele independente concurează fără echivalent (RSMM §3, Inferences). **Condiție:** să fie confirmat că BizMedica MM, MedExam și ceilalți nu-l au deja. Altfel golul nu există.
- **G:** **găsirea pacienților care n-au mai programat controlul** stabilit de medic. N-a fost documentat niciun produs românesc (RSMM §2, Inferences). Golul există ca produs, dar **cererea pentru el nu e demonstrată**: în panelul v1, 0/20.
- **B:** **nu există un gol vizibil**. Substitutul gratuit (Excel plus furnizorul MM) e suficient pentru 18 din 20 de cumpărători simulați.

### 6. Cine ar copia cel mai repede

- **A:** **Setrio (BizMedica MM)** și **DMV Consult (MedExam)**. Au deja datele și clienții. Un portal de status e pentru ei o funcție, nu un produs. Apărarea fondatorului e viteza de onboarding, relația locală și un parteneriat cu un vendor (vânzarea prin el), nu tehnologia.
- **G:** **MediNote sau icMED** pot adăuga un raport „controale scadente” peste datele pe care le au deja. Vendorii de recepție AI (Callio, VAstoma) pot adăuga apeluri de rechemare.

## The buyer panel

**2 buy · 18 pass** (10% buy) out of 20 simulated buyers. Seed 2026, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Clinică independentă multi-specialitate (diabet, cardiologie, endocrinologie), cu contract CAS, 5-20 de medici | 9 | 22% |
| Cabinet de medicină de familie cu contract CNAS, 1-2 medici, listă de 1.500-3.000 de pacienți | 7 | 0%  (thin) |
| Laborator independent de analize medicale, cu contract CAS și 2-6 puncte de recoltare proprii | 4 | 0%  (thin) |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Prudent cu datele | 3 | 33%  (thin) |
| Orientat pe venit | 3 | 33%  (thin) |
| Mulțumit de programul de cabinet | 4 | 0%  (thin) |
| Copleșit de CNAS | 3 | 0%  (thin) |
| Interesat de calitate | 2 | 0%  (thin) |
| Asistenta sună | 4 | 0%  (thin) |
| Sceptic față de startup-uri | 1 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $890,000 and up | 7 | 29%  (thin) |
| $173,000 to $890,000 | 7 | 0%  (thin) |
| under $173,000 | 6 | 0%  (thin) |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 11 | "Programul nostru trimite deja SMS-uri de reminder și nu am o problemă mare cu controalele pierdute, laboratorul nostru nu e clinică de cronici. Nu am chef să leg încă un furnizor de datele pacienților." (P007) · "Asistentele sună oricum pacienții când au timp, iar la noi nimeni nu măsoară cine a revenit, așa că nu simt o durere care să mă facă să plătesc. Nu vreau încă o integrare cu programul și cu datele pacienților pentru o listă pe care nu știu dacă cineva o să o folosească." (P008) |
| trust | 4 | "Prețul nu mă sperie, dar nu dau acces la datele pacienților unui SRL mic pe care nu îl cunosc, nici măcar pseudonimizate. O amendă GDPR m-ar costa mult mai mult decât câștigă lista asta. Iar exportul din programul nostru e o problemă, nimeni nu știe să-l facă." (P001) · "Programul nostru trimite deja SMS de reminder și nu vreau să mai dau date de pacienți unui furnizor nou. Văd în presă amenzi GDPR și nu am consimțământ pentru SMS de la pacienții vechi, deci riscul îmi pare mai mare decât câștigul." (P002) |
| habit | 3 | "Programul nostru de gestiune trimite deja SMS-uri și avem deja destule de făcut cu raportările CNAS și e-Sănătatea. Nu vreau încă un furnizor, încă un export și încă o listă pe care să o verifice cineva." (P004) · "Programul nostru trimite deja SMS-uri, iar asistenta știe cine trebuie sunat la control. Nu simt nevoia unui serviciu în plus, mai ales de la un SRL pe care nu îl cunosc, când am deja bătaie de cap cu GDPR." (P005) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 2 | "Pacienții cronici care nu mai revin la control sunt o problemă reală la noi, iar 69 €/lună pe locație e puțin față de ce pierdem. Auditul e gratuit pe date fără nume, iar garanția mă protejează, așa că risc foarte puțin. Pornesc doar dacă auditul arată un număr clar de controale pierdute." (P003) · "Un control uitat înseamnă o consultație pierdută, iar la 69 € pe lună, cu garanția de 15 controale, riscul e mic. Fac întâi auditul gratuit și, dacă îmi arată pacienți reali neprogramați, plătesc." (P006) |

### What would flip a no

- Să văd pe un export real al clinicii mele, făcut de ei fără ca personalul meu să piardă timp, că găsesc multe controale pierdute. În plus, să am avizul scris al juristului sau al responsabilului GDPR și referințe de la o altă clinică din Oradea sau Cluj care lucrează deja cu ei.
- Un aviz scris de la un jurist sau de la responsabilul meu GDPR că procesul e conform fără consimțământ nou, plus o clinică similară din zonă care îl folosește de un an și confirmă că nu a avut probleme.
- Dacă furnizorul programului meu ar integra lista direct, fără export separat și fără alt contract, sau dacă un coleg de la o clinică similară mi-ar arăta că a recuperat pacienți fără bătaie de cap.
- Dacă auditul gratuit ar arăta un număr mare de controale pierdute pe care programul meu nu le prinde, iar firma mi-ar da referințe de la alte cabinete și ar confirma în scris că funcționează cu programul meu de gestiune.
- Dacă producătorul programului meu ar include lista asta ca funcție în programul actual, fără export către terți, sau dacă auditul gratuit ar arăta zeci de controale pierdute pe lună, la mine, în cifre clare.
- Un audit gratuit care îmi arată o cifră mare de controale pierdute la pacienții mei, plus un medic coordonator dintr-o clinică din Cluj sau Timișoara care confirmă că asistentele chiar folosesc lista și că au apărut programări reale, fără nicio problemă cu pacienții sau cu protecția datelor.
- Dacă aș vedea în auditul gratuit, pe datele mele, un număr mare de pacienți cronici reali neprogramați, și dacă mi-ar confirma în scris un jurist sau CNAS că apelurile nu mă expun la nicio răspundere.
- Dacă auditul gratuit ar arăta un număr mare de controale pierdute la pacienții mei cu risc (diabet decompensat, cardiologie), iar furnizorul ar dovedi la o clinică similară că lista se integrează în program fără muncă în plus pentru personal.
- Auditul gratuit pe export pseudonimizat să arate un număr mare de controale pierdute, iar furnizorul să-mi confirme în scris că știe programul nostru și că exportul nu atinge baza de date. Aș vrea și o clinică din Oradea sau Cluj care să-l folosească deja și să-mi spună că merge.
- Să văd că există un tip de listă utilă pentru un laborator, cum ar fi pacienți cronici care nu mai revin la analizele periodice. Și să mi se demonstreze pe programul meu, fără nicio muncă de la mine, că exportul funcționează.
- Dacă aș vedea în audit, pe datele mele, o sută de pacienți pierduți care ar aduce analize plătite de CAS, și dacă lista ar fi trimisă automat, fără ca asistenta să facă ceva.
- Dacă auditul gratuit îmi arată în cifre clare sute de controale pierdute la lista mea, cu valoarea lor în consultații și analize decontate, și prețul ar fi sub 30 € pe lună, fără contract pe termen lung.

Buyers say they would buy **1.0 times** in the first month on average.

20 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

**Sursele prețului:** (1) răspunsurile la cele patru întrebări de preț din panelurile **simulate** (`van_westendorp.py`; tabelele `*-curve.md` din acest folder; unealta afișează „$”, dar toate răspunsurile sunt în **EUR pe lună, fără TVA**); (2) prețurile concurenților din `../competitors.md`; (3) marjele din unealta CFO (`../cfo/`). Răspunsurile simulate aleg ce să testezi. Nu dovedesc ce se va plăti.

### A · Scadențar MM + portal angajator (prin cabinete)

**1. Ce au spus cumpărătorii** (20 simulați; v1 = primul pitch, v2 = oferta refăcută):

| Panel | PMC | OPP | IPP | PME | Interval acceptabil |
|---|---:|---:|---:|---:|---|
| v1 (59/99 €) | 24 € | 25 € | 59 € | 120 € | 24–120 € |
| v2 (35/69/129 €) | 15 € | 30 € | 40 € | 99 € | 15–99 € |

Mediana pragului „începe să fie scump”, pe segment (v1/v2): **cabinet mic 60/40 €, firmă medie 120/95 €, furnizor regional 250/250 €.** Cei care cumpără au în v1 o mediană de 130 € la „scump” și 250 € la „prea scump”.

**2. Ce cer concurenții:** niciun preț publicat pentru software de medicina muncii. Ancore apropiate: MediNote ~10 €/utilizator/lună; BizMedica pentru medicina de familie ~31–39 €/lună (preț vechi) (RO §2).

**3. Ce cere afacerea** (`unit_economics.py --price`, rampa de bază din anul 1):

| Preț mediu | Contribuție/client | Prag de rentabilitate (clienți) | Profit operațional anul 1 |
|---:|---:|---:|---:|
| 39 € | 35 € | 7 | −870 € |
| 49 € | 45 € | 6 | −330 € |
| **65 €** | **61 €** | **4** | **+534 €** |
| 79 € | 75 € | 4 | +1.290 € |
| 99 € | 95 € | 3 | +2.370 € |

**4. Decizia:**
- **Prețul: o scară pe trei trepte, cu o medie țintă de ~65 €/client-lună.** Media e calculul meu, la un mix estimat de 50% cabinete mici, 40% firme medii, 10% furnizori regionali.
  - **Mic: 39 €/lună** (până la 1.500 de angajați urmăriți). Stă sub pragul „scump” al cabinetelor mici (40–60 €).
  - **Standard: 79 €/lună** (până la 6.000). Firmele medii sunt segmentul care a cumpărat cel mai mult (50% în v1), iar pragul lor „scump” e 95–120 €.
  - **Regional: 149 €/lună** (nelimitat, mai multe locații). Pragul lor „scump” e 250 €.
  - SMS-urile se refacturează la cost, separat.
- **De ce nu 25–30 € (OPP):** OPP e prețul cu cea mai mică rezistență, dar la 39 € sau mai puțin primul an e pe pierdere (tabelul de mai sus), iar la plafonul de timp al fondatorului (~25 de clienți) MRR-ul maxim ar fi sub 1.000 €.
- **Oferta de lansare:** „pilot fondator” pentru primele 5 cabinete:
  - preț blocat 24 de luni;
  - configurarea inițială făcută de fondator la sediu;
  - garanție de 90 de zile cu returnarea banilor.
  - **Fără reduceri procentuale**, ca să nu-i înveți pe cumpărători să aștepte promoții. Raritatea e reală: la 10–12 h/săpt fondatorul poate integra ~1 client pe lună.
- **Ce se testează cu cumpărători reali:**
  - Standard la **69 € față de 89 €** (pre-vânzare la firmele medii);
  - Mic la **35 € față de 49 €**;
  - întrebarea „ați refactura portalul angajatorilor?”.
- **Obiecțiile de preț, citate din panel (simulat):**
  1. „Costul de 59–99 € pe lună îl iau din marjă, iar clientul nu-mi dă un leu în plus pentru portal sau remindere.” (A/P015)
  2. „Încă un abonament lunar pe care îl plătesc eu, iar clienții nu vor plăti în plus pentru el.” (A/P001)
  3. „Cu 3.000–10.000 de angajați aș ajunge pe treapta de 69 sau 129 € pe lună, bani scoși din marja mea.” (A2/P007)
  - **Răspunsul de marketing:** argumentul nu e „portal”. E „asistenta nu mai sună angajatorii” plus „nu mai pierzi clientul la renegociere”. Testul A/B simulat sugerează că economia de timp (reminderele) convinge mai mult decât portalul.

### G · Controale pierdute (clinici de boli cronice)

**1. Ce au spus cumpărătorii:**

| Panel | PMC | OPP | IPP | PME | Interval |
|---|---:|---:|---:|---:|---|
| v1 (129 €) | 30 € | 30 € | 69 € | 130 € | 30–130 € |
| v2 (69 €) | 15 € | 15 € | 40 € | 120 € | 15–120 € |

Pragul „scump” pe segment (v1/v2): **clinici cronice 150/120 €**, laboratoare 110/80 €, medici de familie 70/59 €.

**2. Ce cer concurenții:** de la ~10 € (reminder inclus în MediNote) la 139–299 € (Callio) și 299–499 € (agenți vocali; EMG Q3).

**3. Ce cere afacerea:**

| Preț | Contribuție | Prag de rentabilitate (clienți) | Profit operațional anul 1 |
|---:|---:|---:|---:|
| 49 € | 44,5 € | 6 | −1.870 € |
| 69 € | 64,5 € | 4 | −1.470 € |
| **89 €** | **84,5 €** | **3** | **−1.070 €** |
| 119 € | 114,5 € | 2 | −470 € |

Anul 1 e pe pierdere la orice preț. Motivul e rampa lentă: audit, integrare per clinică, prima plată abia în luna 5.

**4. Decizia:**
- **Prețul: 89 €/lună pe locație, doar pentru clinicile de boli cronice**, după un audit gratuit.
- **Nu se vinde medicilor de familie** (0 cumpărători din 7 în ambele paneluri; „sunt plătită pe listă, nu pe consultație”, G/P017) și **nici laboratoarelor** în v1.
- **Garanția** „în lunile din primele 3 cu mai puțin de 15 controale programate din listă, nu plătiți” costă cel mult 3 × 89 € pe client. Se acordă doar dacă auditul arată cel puțin 30 de controale depășite.
- **Ce se testează:** 69 € față de 99 €, la primele 4–6 clinici auditate.
- **Obiecțiile de preț (simulate):**
  1. „Plătesc 129 € pe lună, adică aproape 1.550 € pe an, și nu am nicio garanție că vin pacienți în plus.” (G/P014)
  2. „Nu sunt convinsă că ar aduce suficiente consultații în plus cât să acopere 129 € pe lună.” (G/P016)
  3. „69 € pe lună plus TVA pentru o listă pe care asistenta o poate scoate și din programul actual.” (G2/P016)

### B · Scadențar MM direct la HR

**1. Ce au spus cumpărătorii:** PMC 10 €, OPP 10 €, IPP 25 €, PME 60 €. Intervalul acceptabil e 10–60 €. Pragul „scump” median e 37–57 €, după mărimea angajatorului.

**2. Ce cer concurenții:** 0 € (Excel, furnizorul MM).

**3. Ce cere afacerea:** la ~25 € (IPP), 1.000 € MRR cere ~40 de angajatori, fiecare cu vânzare separată. La 10–12 h/săpt e nefezabil ca produs separat (calculul meu; CFO nu a rulat pentru B, care nu e în primele 2).

**4. Decizia:** **niciun preț separat pentru B ca produs.** Partea de angajator intră în A, prin portalul cabinetului. Singura excepție testabilă: un nivel de autoservire la **19 €/lună** pentru angajatorii „speriați de ITM” (singurul segment care a cumpărat, 2 din 3). Rolul lui e de **sursă de clienți pentru cabinete**, nu de linie de venit.
- **Obiecțiile de preț (simulate):**
  1. „Ar trebui să primesc scadențarul de la furnizorul de medicina muncii, în prețul pe care îl plătesc deja.” (B/P017)
  2. „39 € pe lună mi se pare mult pentru un tabel cu date.” (B/P007)
  3. „39 € pe lună plus SMS-uri pentru ceva ce fac gratis nu mi se pare justificat.” (B/P020)

## The offer

### Problemele (din panelul G, simulat, și din board)
1. „Datele pacienților diabetici și cardiaci la un SRL necunoscut.”
2. „Programul trimite deja SMS.”
3. „Exportul zilnic: nimeni nu știe să-l facă.”
4. „Un mesaj despre un rezultat anormal sperie pacientul și mă face răspunzător.”
5. „129 € pentru câteva programări.”
6. „Nu am consimțământ de la pacienții vechi.”
7. „Pacientul e responsabil să revină.”
8. „La capitație nu câștig nimic din consultații în plus.” (medici de familie)
9. „Laboratorul n-are controale.”
10. „Cine răspunde dacă un mesaj nu pleacă?”
11. Board, lentila Produs: „Prea multe lucruri; cusături peste tot.”
12. Board, lentilele Monopol și Produs: „Granița MDR la bucla de rezultate.”

### Ce s-a schimbat de la v1 la v2
- **O singură buclă** (controale stabilite de medic), **un singur cumpărător** (clinici cronice). Răspunde la 4, 8, 9, 11, 12.
- **Audit gratuit pe export pseudonimizat, înainte de orice plată.** Răspunde la 1, 5, 7.
- **Export automat configurat de fondator.** Răspunde la 3.
- **Implicit, doar lista de sunat; SMS numai cu consimțământ, cu text aprobat de directorul medical, fără mențiuni medicale.** Răspunde la 4, 6.
- **Fără CNP, fără diagnostice; DPA.** Răspunde la 1.
- **Preț 69 € și garanția „sub 15 controale programate → nu plătiți”.** Răspunde la 5, 10.

### Retestarea (aceleași cărți)
- **v1: 0/20. v2: 2/20 (10%).** Ambii cumpărători sunt clinici cronice (2 din 9 în acel segment). Medicii de familie (0/7) și laboratoarele (0/4) rămân la zero.
- **Ce a mișcat ceva:** auditul înainte de plată și garanția.
- **Ce n-a mișcat:** încrederea într-un SRL necunoscut cu date de pacienți. Asta se rezolvă doar cu referințe reale, adică după A.
- **Concluzie:** problema lui G e mai degrabă piața și încrederea decât prețul. Oferta merge doar în nișa clinicilor cronice și doar cu un audit care arată pacienți pierduți reali.

## The numbers

**Toate cifrele de mai jos vin din `unit_economics.py`**, rulat pe fișierele `*_numbers*.json` din acest folder. Excepție: orizontul de 36 de luni, care e calculul meu peste ieșirile uneltei (`combine_36m.py`). **Sursa fiecărei intrări** e în `cfo-sources.md`: aproape toate sunt estimările mele, nu oferte reale. Unealta afișează „$”, dar toate sumele sunt în **EUR, fără TVA**. Unitatea e **un client pe o lună**: `days_per_month = 1`, deci „per day” înseamnă „clienți activi în luna respectivă”. SMS-urile se refacturează la cost și sunt scoase și din preț, și din cost. **Nu e consultanță financiară, fiscală sau juridică.** Un contabil trebuie să verifice structura (SRL, TVA, deductibilitate) înainte să se miște bani.

### Rezumat

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

### Nota CFO

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

### Fișierele

- **Intrări:** `A_numbers.json`, `A_numbers_y2.json`, `A_numbers_y3.json`, `A_numbers_fullcost.json`, `A_numbers_lowfixed.json`, `A_scale_numbers*.json`, `G_numbers*.json`.
- **Rapoartele uneltei:** `A_cfo.md`, `A_cfo_y2.md`, `A_cfo_y3.md`, `A_cfo_fullcost.md`, `A_scale_cfo_y2.md`, `G_cfo.md`, `G_cfo_y2.md`, `G_cfo_y3.md`, `G_cfo_fullcost.md`. Ieșirile JSON sunt în `*.out.json`.
- **36 de luni:** `A_36m.md`, `A_scale_36m.md`, `G_36m.md` (`combine_36m.py`).

## Not done yet

- Marketing: run /founder-marketing
- Brand: run /founder-brand
- Operations: run /founder-ops
- Launch plan: run /founder-launch

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
