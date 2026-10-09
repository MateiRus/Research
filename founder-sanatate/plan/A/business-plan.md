# Scadențar MM: portal pentru angajator, vândut cabinetelor independente de medicina muncii · Business plan

**Verdict: Profitable**

- ✓ Each client-lună earns $61.00 before fixed costs (94% contribution).
- ✓ Year 1 operating profit: $534.
- ✓ Break-even is 4 client-lunăs a day against a capacity of 25.
- ✓ 7 of 20 simulated buyers buy (35%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $65.00 a client-lună |
| Profit margin at plan | 72% per client-lună |
| Break-even | 4 client-lunăs a day |
| Year 1 operating profit | $534 |
| Startup spend | $2,980 |
| Cash needed before it pays for itself | $3,825 |
| Startup money earned back | not in year 1 |
| Buyer panel | 7 buy · 13 pass |

## The idea

- Ce este: un add-on pentru cabinetele independente de medicina muncii. Ține scadențele fișelor de aptitudine ale tuturor angajaților fiecărui client, trimite remindere în locul asistentei și îi arată fiecărui angajator un portal cu marca cabinetului: cine e în termen, cine expiră, cine a depășit, ce recomandări „apt condiționat” sunt deschise. Nu conține diagnostice.
- Pentru cine: cabinete și firme independente de medicina muncii (1–5 medici, 1.000–10.000 de angajați urmăriți) din Oradea, apoi din Nord-Vest. Primii vizați: cele care au pierdut clienți în fața rețelelor (MedLife a cumpărat Medicris în 2022).
- Ce vinde, la ce preț: abonament lunar pe trei trepte: 39 € (până la 1.500 de angajați), 79 € (până la 6.000), 149 € (nelimitat). SMS-urile se facturează la cost. Configurarea e inclusă, cu garanție de 90 de zile.
- Unde și cum: SaaS găzduit în UE (Oracle APEX/PL-SQL, n8n). Datele vin din exportul programului MM existent sau din Excel. Vânzarea se face prin vizite la sediu, mai întâi în Oradea, apoi în Cluj, Satu Mare și Arad.
- Buget și constrângeri: ~25.000 € capital, 10–12 h/săptămână, un singur fondator. Produsul e administrativ (nu e dispozitiv medical); fondatorul e persoană împuternicită GDPR.

## Summary

**Ce e și pentru cine.** Un add-on administrativ pentru cabinetele independente de medicina muncii. Ține scadențele fișelor de aptitudine, trimite remindere în locul asistentei și dă fiecărui angajator-client un portal cu marca cabinetului (status, fără diagnostice). E răspunsul independenților la portalul self-service MedLife.

**Verdictul (calculat de `compile.py`): Profitable, dar fragil.** Cele trei numere din spatele lui (estimări, `cfo/`):
- contribuție de 61 €/client-lună (94%);
- prag de rentabilitate la 4 clienți;
- profit operațional în anul 1 de doar +534 €.

Verdictul devine „Not yet” dacă e calculat cu panelul v2 (15% cumpără, sub pragul de 25%) sau la un volum cu 20% mai mic (anul 1: −125 €). **1.000 € MRR vine în ~luna 18. 3.000 € MRR nu vine la 10–12 h/săpt** (plafon ~1.600 €).

**Unde au fost de acord panelul și board-ul:** A e singura idee pusă de toate trei lentilele în primele două, iar în panel are cea mai mare rată (35% în v1, limită superioară). Cumpără firmele medii și cabinetele care au pierdut clienți în fața rețelelor. **Unde nu au fost de acord:** board-ul preferă G ca valoare strategică, dar panelul a respins G (0% → 10%).

**Cel mai mare risc:** cabinetele consideră că programul MM sau Excel-ul „face deja asta”, iar un vendor MM (Setrio, DMV Consult) adaugă portalul. **Ce se face:**
- 15 conversații de descoperire;
- verificarea a ce face deja fiecare program MM;
- 3 pre-vânzări plătite **înainte** de construcție.

**Ce îi trebuie fondatorului:** ~3.800 € în numerar (din 25.000 €) și ~120–160 h pentru MVP. Primul test sunt 3 pre-vânzări la cabinete din Oradea și Nord-Vest.

**Lucrul de făcut săptămâna aceasta:** sună sau mergi la Medimun, Carimed și Endodigest. Întreabă trei lucruri: ce program MM folosesc, cum țin azi scadențele și dacă ar plăti 79 €/lună ca asistenta să nu mai sune angajatorii. Notează răspunsurile exact.

_Panelul e simulat, iar cifrele sunt proiecții din estimări. Nu e consultanță financiară, juridică sau fiscală._

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

**7 buy · 13 pass** (35% buy) out of 20 simulated buyers. Seed 2026, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Firmă MM medie: 2-5 medici, echipă mobilă care face examene la sediul angajatorilor, 3.000-10.000 de angajați urmăriți | 8 | 50% |
| Furnizor MM regional independent mare: peste 10.000 de angajați pe an și peste 300 de firme-client | 3 | 33%  (thin) |
| Cabinet MM mic: 1 medic de medicina muncii și 1 asistentă, aprox. 800-2.500 de angajați urmăriți, clienți IMM-uri locale | 9 | 22% |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Sub presiunea rețelelor | 3 | 100%  (thin) |
| Caută noutăți | 1 | 100%  (thin) |
| Excel și hârtie | 4 | 50%  (thin) |
| Medic ocupat care delegă | 3 | 33%  (thin) |
| Foarte atent la costuri | 3 | 0%  (thin) |
| Mulțumit de programul MM actual | 4 | 0%  (thin) |
| Prudent cu datele | 2 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $380,000 and up | 7 | 43%  (thin) |
| under $112,000 | 6 | 33%  (thin) |
| $112,000 to $380,000 | 7 | 29%  (thin) |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| habit | 6 | "Folosesc deja programul MM care emite fișa de aptitudine, iar asistenta ține scadențele într-un Excel care merge. Nu simt nevoia să mai plătesc pentru încă o unealtă și încă un import de date." (P002) · "Asistenta mea ține deja tabelul Excel cu toate firmele și merge. Angajatorii nu plătesc în plus, deja mă negociază la 80 de lei pe angajat, așa că nu văd de unde îmi revine banii, iar pentru mine ar fi încă o platformă de învățat." (P004) |
| trust | 4 | "Nu vreau să încarc pe o platformă externă lista a mii de angajați ai clienților mei, după ce am citit despre amenzile ANSPDCP. Pe deasupra, asistenta mea își face treaba în Excel, iar angajatorii nu plătesc în plus, că deja mă negociază la 80 de lei pe angajat." (P005) · "Programul meu de medicina muncii îmi arată deja când expiră fișele, iar eu nu vreau să dau lista angajaților clienților mei unei platforme externe. Am citit despre amenzile ANSPDCP și nu risc pentru un add-on." (P010) |
| price | 2 | "Nu văd cum aduce bani imediat un abonament de 59 €/lună. Țin deja evidența scadențelor în Excel și în program, iar pe clienți îi țin cu prețul mic pe angajat, nu cu portaluri." (P001) · "Angajatorii nu plătesc în plus pentru așa ceva, iar eu concurez deja pe 80 de lei pe angajat. Tai abonamentele care nu aduc bani imediat, iar remindere pot face și cu Excel-ul și programul pe care le am." (P015) |
| need | 1 | "Nu văd ce câștig concret: nu-mi aduce clienți noi, doar mai multă muncă cu importuri și remindere. Scadențele le țin deja sub control, iar 59 € pe lună plus SMS-uri înseamnă un abonament în plus, într-un business unde concurez pe preț." (P003) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 6 | "Am pierdut clienți în fața rețelelor mari și un portal cu marca cabinetului, cu scadențe și remindere, e ceva ce le pot arăta angajatorilor. Importul îl fac ei, prima lună e gratuită și nu am contract, deci riscul e mic." (P006) · "Scadențele le țin în Excel și pe hârtie, iar asistenta sună angajatorii când își amintește, deci pierd controale de reînnoire. Pentru 59 € pe lună, cu import făcut de ei și fără contract, merită încercat o lună." (P008) |
| convenience | 1 | "Importul îl fac ei, prima lună e gratis și nu am contract pe termen lung, deci nu pierd nimic dacă asistenta spune că nu merge. Dacă HR-urile clienților primesc remindere fără să mă mai sune pe mine, 99 € pe lună la cifra mea de afaceri nu mă doare." (P012) |

### What would flip a no

- Dacă l-aș putea refactura clienților ca serviciu separat și aș vedea că îmi aduce clienți noi sau reduce munca asistentei, într-un test real pe un singur client, cu un preț în jur de 25-30 €/lună.
- Dacă s-ar integra direct cu programul meu MM, fără import manual, și dacă mi-ar da un model gata făcut de consimțământ și un acord de împuternicit clar, aș testa luna gratuită.
- Dacă aș vedea că angajatorii mari îl cer sau că mă ajută să țin sau să câștig contracte la renegocierea anuală, iar prețul ar fi în jur de 30-35 € pe lună, cu SMS-urile incluse.
- Dacă asistenta mea ar încerca luna gratuită și ar spune că îi scade munca cu telefoanele și cu urmărirea scadențelor, iar eu aș putea cere angajatorilor un mic plus pentru portal sau l-aș folosi ca să nu pierd clienți.
- Dacă l-aș vedea funcționând la un cabinet de medicina muncii pe care îl cunosc, cu un audit de securitate sau o certificare verificabilă, și dacă s-ar putea rula doar cu date minime (fără CNP), cu import din Excel și fără portal pentru clienți. Aș mai fi convins dacă angajatorii ar accepta să plătească ei portalul.
- Dacă s-ar integra direct cu programul meu MM, fără import manual din Excel, și dacă aș putea să le cer clienților un abonament separat pentru portal, astfel încât să nu-l plătesc eu.
- Dacă mi-ar arăta că se conectează direct la programul meu actual, fără să încarc eu fișiere Excel, și dacă aș avea un audit de securitate independent sau referințe de la alte cabinete din zonă. Aș vrea și o analiză de impact GDPR deja făcută, cu clauze clare despre răspundere.
- Să văd la un alt cabinet din zonă, cu care pot vorbi, că funcționează de câteva luni, și să-mi facă importul pe datele mele reale în perioada gratuită, ca să văd rezultatul înainte să decid.
- Să-mi arate pe datele mele reale, fără efort din partea mea, că se leagă direct de exportul programului meu și trimite singur remindere la HR-urile clienților, astfel încât asistenta să nu mai sune. Ar ajuta și o referință de la un alt cabinet independent din zonă.
- Dacă mi-ar demonstra cu cifre, pe cabinete ca al meu, că remindere automate aduc mai multe examene reprogramate și facturate la timp, sau dacă angajatorii ar accepta să plătească portalul separat.
- Integrare directă cu programul meu MM, fără import manual din Excel, plus garanția scrisă că pot exporta toate datele oricând, plus referințe de la un cabinet de dimensiunea mea.
- Să fie testat și recomandat de asistenta sau contabila mea, cu preț clar pentru peste 6.000 de angajați. Și un angajament scris că îmi dau tot exportul de date oricând și la închiderea firmei, plus o referință de la un cabinet comparabil cu mine.

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

Metoda e lentila „Ofertă” din `founder-board/lenses.md`: un rezumat al unui cadru publicat, nu cuvintele autorului. Problemele vin din obiecțiile panelului simulat (`panels/A/results.md`, `panels/A2/results.md`) și din riscurile ridicate de board.

### Problemele, în cuvintele cumpărătorului (din panel și board)
1. „Programul meu MM îmi arată deja scadențele.”
2. „Asistenta ține un Excel care merge.”
3. „Angajatorii nu plătesc în plus; mă negociază la 80 de lei.”
4. „Îl plătesc din marjă.”
5. „Nu am timp să importăm și să curățăm datele.”
6. „Datele angajaților la un SRL necunoscut? Amenzi ANSPDCP.”
7. „Ce fac dacă firma dispare?”
8. „Angajatorul nu are voie să vadă nimic medical.”
9. „SMS-urile cer consimțământ.”
10. „Cine răspunde dacă scapă o scadență?”
11. „Nu-mi aduce clienți noi.”
12. „Vreau să-l văd la un cabinet pe care îl cunosc.”
13. „Vreau integrare directă, nu Excel.”
14. „Portalul arată «depășit» pentru cineva deja examinat?” (board, lentila Produs)
15. „Copiază BizMedica funcția în 6 luni.” (board, lentila Monopol)
16. „Nu-i convinge pe angajatorii mici, care nu cer portal.”

### Soluțiile (valoare pentru cumpărător / cost de livrare, 1–5)

| Soluție | Răspunde la | Valoare | Cost | Păstrată |
|---|---|---:|---:|---|
| Remindere automate către HR-ul clienților: asistenta nu mai sună | 2, 5, 11 | 5 | 1 | ✔ nucleu |
| Configurare la sediu, din exportul programului MM existent; actualizare săptămânală | 1, 5, 13, 14 | 5 | 3 | ✔ |
| Portal cu marca cabinetului: status în termen / expiră / depășit | 3, 11 | 4 | 2 | ✔ |
| Raport lunar de scadențe pe angajator (argument la renegociere) | 3, 11 | 4 | 1 | ✔ |
| Fără CNP, fără diagnostice; DPA și model de consimțământ gata făcute | 6, 8, 9 | 4 | 1 | ✔ într-o frază |
| Export complet oricând; date returnate la închidere | 7 | 3 | 1 | ✔ |
| Jurnal „cine a văzut ce”; marcarea manuală „examinat azi” | 10, 14 | 3 | 2 | ✔ |
| Garanție de 90 de zile cu returnarea banilor | 4, 12 | 4 | 2 | ✔ |
| Refacturarea portalului către angajatori (opțional) | 3, 4 | 3 | 1 | ✔ ca opțiune |
| Integrare API cu fiecare program MM | 13 | 5 | 5 | ✘ (nu există API; doar parteneriat ulterior) |
| Audit de securitate certificat | 6 | 3 | 5 | ✘ deocamdată (aliniere la controale, certificare mai târziu; REG §5) |

### Pachetul recomandat (v3, de testat cu oameni reali)
- **Nucleul (rezultatul, nu ingredientele):** „Asistenta dumneavoastră nu mai sună angajatorii: fiecare client își vede singur scadențele, cu marca cabinetului, și primește remindere la timp.”
- **Bonusuri:**
  - (1) configurarea la sediu, din exportul existent;
  - (2) raportul lunar pentru renegocierea anuală;
  - (3) modelele de DPA și consimțământ, gata făcute.
- **Garanția:** 90 de zile, cu returnarea banilor. Costul la o rată estimată de 1 din 5 clienți care cer banii înapoi e de ~3 × 65 € / 5 ≈ 39 € pe client. Acceptabil la o contribuție de 61 €/lună (calculul meu, pe cifrele din `cfo/`).
- **Urgența (reală):** doar 5 cabinete pilot în primul semestru, pentru că fondatorul poate integra ~1 cabinet pe lună. Pilotii păstrează prețul 24 de luni.
- **Numele:** „Scadențar MM”, cu „portal pentru angajatori” ca subtitlu.
- **Prețul:** 39 / 79 / 149 € (`pricing/pricing.md`).

### Ecuația valorii (1–10, estimarea mea): v1 → v3
- **Rezultatul dorit:** 6 → 7, prin raportul pentru renegociere și portalul cu marca proprie.
- **Probabilitatea percepută:** 4 → 6, prin garanție și configurarea la sediu. Va urca la 8 doar cu o referință reală.
- **Timpul până la rezultat:** 6 → 8, prin configurarea făcută de fondator.
- **Efortul cerut:** 5 → 8. Asistenta nu mai exportă și nu mai sună.

### Retestarea (panel simulat, aceleași cărți, seed 2026)
- **v1** (remindere + portal, 59/99 €): **7/20 (35%)**.
- **v2** (paritate cu rețelele, paragraf lung despre date, 35/69/129 €, garanție): **3/20 (15%)**. Au plecat 2 dintre cei cu „Excel și hârtie”, medicul ocupat și cel care caută noutăți, mai ales pe încredere.
- **Lecția:** reminderele care economisesc timpul asistentei vând mai bine decât portalul. Datele se spun într-o frază sigură, nu într-un paragraf care sperie. **v3 combină nucleul din v1 cu configurarea și garanția din v2.** N-a fost retestată în panel, pentru că următorul test trebuie făcut cu cabinete reale.

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
