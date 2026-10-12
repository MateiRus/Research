# Alarmă Lucrător Izolat (nume de lucru) · ILLUSTRUS S.R.L. · Business plan

**Verdict: Not yet**

- ✓ Each lucrător-lună earns $7.33 before fixed costs (61% contribution).
- ✗ Year 1 operating LOSS: $4,468.
- ✗ 4 of 30 simulated buyers buy (13%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $12.00 a lucrător-lună |
| Profit margin at plan | -1% per lucrător-lună |
| Break-even | 72 lucrător-lunăs a day |
| Year 1 operating profit | $-4,468 |
| Startup spend | $6,546 |
| Cash needed before it pays for itself | $11,013 |
| Startup money earned back | not in year 1 |
| Buyer panel | 4 buy · 26 pass |

## The idea

- What it is: un serviciu pe abonament pentru lucrătorul izolat: dispozitiv certificat cumpărat de la terți (Teltonika TMT250 / GH5200; Garmin inReach pentru zonele fără semnal) care trimite căderea, imobilitatea și butonul SOS cu locația la alarmă, plus platformă proprie (Traccar + n8n + Oracle APEX) și dispecerat externalizat la o firmă de pază din Oradea, care preia alarma, sună lucrătorul, clientul și 112.
- Who it is for: angajatori din Bihor cu oameni care lucrează singuri sau nevăzuți: întâi utilitățile locale (apă-canal, salubritate, termoficare), apoi firmele private de exploatare forestieră din zona Aleșd–Beiuș, apoi antreprenorii marilor șantiere. Decid patronul (firme mici) sau directorul general cu șeful SSM (utilități, prin SEAP); serviciul extern SSM e influențator / canal.
- What it sells, at what price: abonament pe lucrător pe lună. Ipoteza din cercetare: 20 EUR (~100 lei) cu dispozitiv inclus, sau 12 EUR (~60 lei) dacă clientul cumpără dispozitivul (~130 EUR). Pilot de 90 de zile la 30 de lucrători, cu dispozitivele cumpărate de client și trecere la 12 EUR/lucrător/lună dacă pilotul atinge țintele.
- Where and how: Bihor (Oradea și județul), vânzare directă de fondator, fizic, plus recomandări prin serviciile externe SSM (comision ~15%). Livrare: dispozitive configurate, instruire, pachet de documente SSM și GDPR, dispecerat 24/7 externalizat, raport lunar și jurnal de alarme cu oră exactă.
- Budget and constraints: ~25.000 EUR capital, 10–12 ore/săptămână la început, 0–1 angajați. Fondatorul: student anul 2 ASE, junior Oracle APEX/PL-SQL; Python, SQL, PL/SQL, APEX, n8n, LLM-uri, WordPress. Nu construiește hardware. Preferă B2B cu venit recurent. Ținta: 1.000–3.000 EUR MRR (venit lunar recurent). Obligația DR-36 (≥10.000 EUR venit din servicii web) e considerată rezolvată separat și nu se analizează aici.

## Summary

- **Ce e și pentru cine.** „Lucru izolat conform, la cheie”: alarmă de cădere, imobilitate și SOS, cu locația trimisă doar la alarmă, plus un dispecer 24/7 (firmă de pază parteneră), un jurnal cu ora exactă pentru ITM și pachetul de documente SSM/GDPR. Se vinde angajatorilor din Bihor cu oameni care lucrează singuri. Primul client e un **manager HSE de fabrică din Oradea** (mentenanță, tura de noapte).
- **Verdictul calculat: Not yet.**
  - Contribuția e de 7,33 EUR pe lucrător-lună (61%) în anul 1.
  - Anul 1 pierde 4.468 EUR pe operațiuni.
  - Doar 13% din panelul simulat cumpără, sub pragul de 25%.
  - Anul 2 trece pe plus (+2.221 EUR), dar panelul rămâne sub prag.
- **Unde au fost de acord board-ul și panelul:** încrederea, referința locală și cusătura cu dispecerul decid totul, nu prețul. **Unde nu:**
  - board-ul (Ofertă, Produs) a ales utilitatea ca prim client, iar panelul i-a dat 0/6 la prima ofertă și 1/6 la a doua;
  - Monopolul a votat PASS și propune vânzarea software-ului către firmele de pază, dar paza simulată a refuzat la ambele variante (0/12) și cere 4–7 EUR.
- **Cel mai mare risc și ce se face:** omul care răspunde la alarmă e al altei firme, iar răspunderea e reală. Se rezolvă așa: un SLA scris cu penalități și neconcurență, testul cu 50 de alarme înainte de orice client, o ofertă de RC reală și o rezervă tehnică plătită din anul 2. Fără ele nu se vinde.
- **De ce e nevoie la start:**
  - ~6.500 EUR pornire și ~8.400 EUR numerar până se autofinanțează (11.013 EUR fără taxele de pilot și marja pe dispozitive), la structura în care clientul cumpără dispozitivul. Dacă dispozitivele sunt incluse, e nevoie de ~25.400 EUR, adică tot capitalul;
  - primul test: 3 teste de semnal gratuite și un pilot plătit de 2.500 lei până în ziua 90.
- **Plafonul:** la 10–12 h/săpt, MRR-ul ajunge la 1.000 EUR în luna 15 și se oprește în jur de 2.400 EUR. 3.000 EUR MRR cere ~20 h/săpt din anul 2.
- **Lucrul de făcut săptămâna aceasta:** cere ofertă scrisă de dispecerat de la 3 firme de pază din Oradea (tarif pe persoană, minim, SLA, Legea 333/2003). Dacă nimeni nu acceptă un SLA cu penalități, oprești.
- Panelul și board-ul sunt **simulate**; cifrele sunt proiecții din estimări. Nu e consultanță financiară, juridică sau fiscală.

## What the board said

**Cum a rulat.** Trei sub-agenți separați (`claude -p`, model opus, fără unelte), câte unul pe lentilă: Ofertă, Monopol, Produs (`founder-board/lenses.md`). Fiecare a primit doar `brief.md`, care conține faptele din cercetare, fără opinia mea. Prompturile sunt în `prompt_*.md`, iar memoriile neschimbate în `offers.md`, `monopoly.md`, `product.md`. Lentilele sunt rezumate ale unor cadre publicate; membrii board-ului **nu sunt** acele persoane și nu vorbesc în numele lor.

### 1. Votul

- **Ofertă: 4/10, FUND IF.**
- **Monopol: 3/10, PASS.**
- **Produs: 5/10, FUND IF.**
- **Rezultat: 2 × FUND IF, 1 × PASS; media 4,0.** Pentru comparație, Scadențarul MM din analiza anterioară a avut 3 × FUND IF, media 5,7.

### 2. Riscurile ridicate de mai mulți membri (acestea primele)

1. **Încrederea și dovada lipsesc** (toți trei):
   - nu există dovezi că dispozitivele salvează vieți;
   - rata de alarme false e necunoscută;
   - 46–59% dintre muncitori ar refuza dispozitivul;
   - TMT250 poate fi doar 2G, iar GH5200 e „End of life”.
2. **Firma de pază este cusătura critică** (Monopol și Produs):
   - momentul în care un om răspunde nu aparține fondatorului;
   - partenerul care vede toate alarmele și procedurile e cel mai probabil să copieze serviciul.
3. **Cererea nu e formată** (Ofertă și Monopol):
   - amenzile sunt mici, CAM nu are bonus-malus, nu există licitații și nici vocabular comercial;
   - nu există un „de ce acum”;
   - durerea (dosarul penal) e rară și vine târziu.
4. **Distribuția și primii 10 clienți sunt nedovediți** (Ofertă și Monopol):
   - cicluri de 6–12 luni sau SEAP;
   - pilotul gratuit nu testează cererea.

### 3. Condițiile, unite (lista de bifat pentru restul pachetului)

- [ ] **Un pilot plătit din prima zi** (taxă de setup), nu gratuit, sau o scrisoare de intenție plătită (Ofertă; Monopol, pentru a schimba votul). Oferta v2/v3 îl conține (2.500 lei); **nu e vândut**.
- [ ] **Confirmarea rețelei TMT250 (4G/LTE-M) și a disponibilității în 2026–2029**, plus un dispozitiv de rezervă (Produs, Ofertă). Bugetul e în CFO (530 EUR pentru dispozitive alternative).
- [ ] **Test end-to-end cu 50 de alarme simulate, zi, noapte și weekend, prin operatorii reali ai pazei:** 100% să ajungă, ≥95% în sub 60 s, **înainte de orice client** (Produs). Bugetul e în CFO (300 EUR).
- [ ] **SLA scris cu firma de pază,** cu timp de preluare, penalități și **neconcurență pe segment** (Produs, Monopol).
- [ ] **Bench test de purtare cu lucrători reali,** cu rata de alarme false măsurată și pre-alarma reglată (Produs, Ofertă).
- [ ] **Ofertă reală de RC** pentru garanția de preluare (Ofertă). CFO-ul o estimează la ~150 EUR/lună; **nu există ofertă**.
- [ ] **Banii riscați plafonați la ~6.600 EUR până la prima plată** (Ofertă). La structura C, CFO-ul ajunge la 8.421 EUR în luna 5, adică **puțin peste plafon**.
- [ ] **Un singur segment în V1;** satelitul și pădurea ies (Produs). Aplicat în ofertă.
- [ ] **Scanarea concurenței regionale** (distribuitori SSM, Blackline sau Peoplesafe în Ardeal), care să confirme golul (Monopol). Făcută doar din note, fără cercetare nouă (`../competitors/`); golul de ofertă e confirmat, cel de cerere nu.

### 4. Cea mai puternică versiune pe care o vede board-ul

Membrii nu sunt de acord asupra formei, și dezacordul e util:
- **Ofertă:** **„lucru izolat conform, la cheie”**, adică setup plătit (documente, sindicat, instruire) + abonament + raport lunar + garanția de preluare în 60 s. Primul client: Compania de Apă Oradea. Pădurea vine în faza 2, pentru că acolo doborârea de unul singur e oricum interzisă.
- **Produs:** **„60 de secunde până la un om, garantat și dovedit”**, pentru echipele de utilități din cămine și stații. Trei lucruri lucrate perfect: dispozitivul, operatorul, raportul. Primul client: tot Compania de Apă.
- **Monopol (PASS pe ideea propusă):** fondatorul **nu ar trebui să devină firmă de alarme**. Ar trebui să vândă **stratul de software și conformitate firmelor de pază**, sub marca lor, cu licență pe lucrător. Amenințarea nr. 1 devine astfel canal. Primul client: firma de pază din Oradea, ca licențiat plătitor.

**Sinteza mea (judecată proprie, nu a board-ului).** Cea mai puternică versiune e un **singur motor** (ecran de dispecerat + reguli + jurnal + pachet de documente) vândut prin **două uși**:
- **ușa „la cheie”** (cu dispecerul partenerului) pentru angajatorii fără dispecerat;
- **ușa „dispeceratul vostru”**, licență pentru firmele de pază și pentru fabricile cu pază internă.

Panelul simulat a mutat apoi primul client de la utilitate (0/6 la v1) la **managerul HSE al unei fabrici mari** (2/6 → 3/6); vezi `../panel/rezultate_panel.md`. Board-ul nu a văzut panelul.

### 5. Dezacordurile, păstrate

- **Ofertă și Produs** cred că ideea se poate finanța cu condiții. **Monopolul** spune PASS: fără tehnologie proprie, fără efect de rețea, cu un stack copiabil (Teltonika + Traccar + n8n) și cu partenerul ca primul copiator.
- **Primul client:** Ofertă și Produs aleg Compania de Apă Oradea. Monopolul alege firma de pază, ca licențiat.
- **Pachetul de documente:** pentru Ofertă e nucleul valorii („reduce efortul cumpărătorului”). Produsul l-ar tăia din V1 ca să nu dilueze „lucrul unic”.

## The competition

**Cum s-a făcut.** Doar din notele existente, fără cercetare web nouă. Fiecare rând din `competitors.csv` are sursa (R = raportul; N03, N05 = notele). Pasul cu recenziile (1–3 stele) din skill **n-a putut fi făcut**: notele nu conțin recenzii de clienți pentru acești furnizori. În locul lor, mai jos sunt plângerile documentate în note (studii, afirmații ale furnizorilor) și obiecțiile din panelul simulat (marcate ca simulate în `panel/`). Câmpurile `positioning_line`, `rating` și `review_count` sunt „n/a”, pentru că notele nu le conțin.

### 1. Cine e acolo, sortat după cât de direct concurează

- **Direct, dar la distanță (nu vând în România):**
  - StaySafe (UK): aplicație + ARC (dispecerat 24/7) + satelit, listă publică de prețuri (N03 §2).
  - Peoplesafe (UK; include SoloProtect și Ok Alone): dispozitive și aplicații + ARC, 22,6 mil. GBP venit, >350.000 lucrători (N03 §2).
  - Twig (Finlanda): dispozitiv profesional om la pământ, legat prin API de centre de alarmă (R §3).
  - Blackline G7c (Canada): gaze + om la pământ + monitorizare, cel mai scump (R §3).
- **Indirect:**
  - detectoarele de gaze MSA, Dräger, Honeywell, Industrial Scientific: fără ofertă de lucrător singur cu dispecerat (R §3);
  - aplicațiile de telefon, inclusiv „Safe Alone” din Cluj, gratuită, cu SMS către un coleg (N03 §3–4);
  - firmele de pază din Oradea cu dispecerat 24/7: azi pentru obiective, nu pentru persoane (N05 §5);
  - butoanele de panică pentru vârstnici (Poșta Română, ambulanță privată Tg. Mureș) (N05 §7).
- **Substitute (cum se descurcă azi cumpărătorul):**
  - **status quo:** coleg, radio sau telefon și procedura SSM. HG 1091/2006 cere supraveghetor și mijloace de legătură, nu un dispozitiv (N05 §1; R §5). Costul în plus e zero;
  - Romsilva: GPS pe utilaje și bodycam pentru pădurari, nu alarmă personală (N03 §7).

### 2. Prețul produsului comparabil (dispozitiv sau aplicație + dispecerat, pe lucrător pe lună)

Calculul meu în EUR (1 GBP ≈ 1,17 EUR, 1 USD ≈ 0,88 EUR, cursul din R), **estimare**:
- **cel mai mic:** ~6 EUR: StaySafe la peste 7.500 de utilizatori cu ARC (3,30 + 1,85 GBP), apropiat de venitul realizat de Peoplesafe, ~6,3 EUR;
- **mediana:** ~12 EUR: StaySafe pentru 26–50 de utilizatori cu ARC, ~11,1 EUR, și pentru 0–15 utilizatori, ~13,3 EUR;
- **cu dispozitiv dedicat:** Peoplesafe MySOS ~17,5–19,3 EUR/lună plus 58–64 EUR la început (sursă terță, de verificat);
- **cel mai mare:** Blackline G7c, ~56 EUR/lună cu dispecerat, plus gaze.
- **Ancorele locale:** GPS de flotă ~50 lei (~10 EUR)/vehicul/lună; serviciu extern SSM 8–25 lei (1,6–5 EUR)/angajat/lună (N05 §3). **Media europeană:** ~10 EUR/utilizator/lună (N03 §5, estimare din Berg).

### 3. Harta de poziționare (în text)

Axele care contează pentru acest cumpărător:
- **orizontal:** cât de „la cheie” e serviciul în România (limbă, dispecerat local, documente SSM/GDPR, cineva care vine la sediu);
- **vertical:** prețul pe lucrător pe lună.

Unde stă fiecare:
- **Preț mare, puțin local:** Blackline, Twig, MSA. Sunt dispozitive excelente, fără prezență și fără dispecerat în România.
- **Preț mediu, deloc local:** StaySafe, Peoplesafe. Serviciul complet e în engleză, cu dispecerat în UK.
- **Preț zero, deloc la cheie:** Safe Alone și status quo-ul (coleg/radio).
- **Preț necunoscut, foarte local, dar pentru obiective, nu pentru oameni:** firmele de pază.
- **Cadranul gol:** preț mediu (12–20 EUR) și foarte local (dispecerat în Oradea, documente în română, instruire la sediu). Aici ar sta ILLUSTRUS.

### 4. Plângerile, ordonate (din note; recenzii de clienți nu există în note)

1. **Muncitorii nu vor să poarte / se tem de urmărire:** 46% n-ar purta purtabile biometrice, 59% n-ar folosi dispozitive de urmărire (studiu 2025, prin rezumat) (N05 §6). Personalul USACE: reticență, dar interes pentru alertele cu beneficiu direct (N05 §6). *Temă puternică* (mai multe surse).
2. **Alarmele false:** temporizatorul de imobilitate e „un instrument brut”, chiar după un furnizor (R §1). Lucrătorii din Alabama se tem că alarmele false le vor perturba munca (N05 §6). Niciun furnizor nu publică rate din teren. *Temă puternică, dar fără cifre.*
3. **Telefonul nu ajunge:** stă în buzunar, are baterie de o zi, nu e ATEX și e orb fără semnal. Chiar vânzătorii de aplicații o spun (N03 §4). *Afirmații de furnizor.*
4. **Lipsa dovezilor de eficacitate frânează angajatorii** (EU-OSHA) (R §1). *O singură sursă instituțională, dar centrală.*
5. **Costul și API-urile închise la liderii industriali:** API Blackline doar prin formular; prețurile Blackline au crescut cu ~15% în 2022, inclusiv la reînnoire (N05 §4; R §3). *Temă subțire* (sub trei surse).

### 5. Golul

- **Ce nu face nimeni bine în Bihor** (după note): un serviciu **în română, cu dispecerat local și cu pachetul de conformitate făcut pentru client**. Pachetul înseamnă:
  - notă de informare, consultarea sindicatului, DPIA (evaluarea de impact asupra datelor), retenție ≤30 de zile (Legea 190/2018 art. 5);
  - procedura de răspuns și jurnalul de alarme ca probă la ITM.
  - Serviciul e vândut la un preț de ordinul GPS-ului de flotă, nu al Blackline (N05 §2, §6; N03 §3).
- **Dovezile pentru gol:**
  - nicio ofertă locală găsită;
  - caietele de sarcini românești de pază cer deja exact capabilitățile de dispecerat (N05 §5);
  - ANSPDCP amendează improvizațiile cu GPS (N05 §6).
- **Rezerva, spusă direct:** golul de **ofertă** e documentat, cel de **cerere** nu. Nicio licitație, niciun cumpărător care caută, niciun vocabular comercial (N05 §7). Un cadran gol poate fi gol pentru că nu-l cere nimeni.

### 6. Amenințarea: cine copiază cel mai repede

1. **Firma de pază care găzduiește dispeceratul:** are operatori, autorizare, clienți și, după pilot, procedurile fondatorului (N05 §5). Cel mai rapid copiator e chiar partenerul critic. Apărarea: contract cu neconcurență pe segment, sau varianta în care pazei i se vinde software-ul (vezi board-ul, lentila Monopol).
2. **Un distribuitor Blackline/Twig sau Peoplesafe** care intră în România prin distribuitori, la clienți mari (petrol, gaze), cu prețuri de 2–3 ori mai mari (R §3; N05 §6). E puțin probabil la utilitățile mici din Bihor în primii 2 ani (**estimare**).
3. **Un serviciu extern SSM mare** care adaugă aplicații gratuite sau ieftine (estimare; niciunul nu a fost găsit).

## The buyer panel

**4 buy · 26 pass** (13% buy) out of 30 simulated buyers. Seed 2026, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Manager HSE (sănătate, securitate, mediu) la o fabrică mare din Oradea, parte dintr-un grup multinațional (1.000–2.500 de angajați; 5–15% lucrează izolat: mentenanță, tura de noapte, logistică) | 6 | 50%  (thin) |
| Șef serviciu intern SSM la o utilitate publică locală (apă-canal, salubritate sau termoficare; 400–750 de angajați; cumpără prin SEAP, are sindicat) | 6 | 17%  (thin) |
| Patron de firmă privată de exploatare forestieră din zona Aleșd–Beiuș (10–40 de angajați; decide și plătește singur) | 6 | 0%  (thin) |
| Administrator de serviciu extern SSM din Oradea (40–150 de firme-client; recomandă măsuri în evaluarea riscurilor, nu plătește el) | 6 | 0%  (thin) |
| Director de firmă de pază din Oradea (80–300 de agenți, mulți singuri pe post noaptea; are dispecerat propriu de alarme pentru obiective) | 6 | 0%  (thin) |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Marcat de un accident | 5 | 60%  (thin) |
| Deschis la tehnologie | 4 | 25%  (thin) |
| Legat de procedură | 4 | 0%  (thin) |
| Se mișcă doar la control | 6 | 0%  (thin) |
| Taie din costuri | 6 | 0%  (thin) |
| Conservator | 5 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $18,304,000 and up | 10 | 40% |
| under $2,044,000 | 10 | 0% |
| $2,044,000 to $18,304,000 | 10 | 0% |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| trust | 11 | "Nu pot semna singur nimic care mă obligă la bani. Pilotul ar trebui să treacă prin director, grup, achiziții și sindicat, iar în 3 luni nu se întâmplă asta. Testul gratuit de o zi mi-ar părea interesant, dar nu e o cumpărare." (P001) · "Nu pot semna singur nimic care să mă oblige la bani: am nevoie de aprobarea directorului, de acordul sindicatului și de procedură prin SEAP. În 3 luni nu cred că ajung la o semnătură, deși testul gratuit mă interesează." (P004) |
| need | 4 | "După accidentul din zonă mă gândesc serios la dosarul penal, dar la noi în pădure nu e semnal, iar un dispozitiv care nu merge în pădure nu mă apără de nimic. Nu semnez nimic plătit înainte să văd cu ochii mei că merge pe parcelele mele și înainte să vorbesc cu serviciul SSM cu care lucrez de ani." (P002) · "Clienții mei lucrează de obicei în echipă și au radio și telefon, așa că nu văd un risc care să justifice o cheltuială nouă. Nu aș propune la 2 clienți un abonament lunar pe lucrător când ei vor să taie costurile la SSM." (P005) |
| price | 4 | "Am deja plătit GPS, EIP și dispecerat propriu, iar 9 EUR pe agent pe lună înmulțit cu sute de agenți e un cost nou pe care nu-l pot trece în contractele cu clienții. Pilotul de 500 EUR e mic, dar nu semnez nimic plătit înainte să văd dacă agenții poartă dispozitivul." (P007) · "100 de lei pe om pe lună e mai mult decât plătesc pe tot SSM-ul, iar 70 de lei tot mi se pare mult pentru oameni în pădure. Serviciul meu SSM mă acoperă de ani buni și nu vreau încă o cheltuială lunară pe 12 luni." (P011) |
| habit | 4 | "Eu mă mișcă doar controlul: dacă ITM sau un auditor nu cere ceva scris despre lucrul izolat, nu semnez nimic. Am dispecerat propriu și agenții merg de ani de zile cu stațiile și rondele existente, așa că nu văd urgență." (P008) · "Mă mișc doar când vine ITM-ul sau un auditor și cere ceva scris. Fără o cerință clară, nu merg la 2 clienți să le propun o cheltuială nouă pe lucrător și lună, mai ales când comisionul de 15% m-ar face să par interesat." (P009) |
| timing | 3 | "Eu mă mișc doar când vine ITM-ul sau un auditor și cere ceva scris, iar acum nu am nimic de felul ăsta pe masă. Nu semnez nimic care mă costă bani doar ca să fiu mai prevăzător." (P003) · "Eu mă mișc doar când vine ITM-ul sau un auditor și cere ceva scris, iar lucrul izolat nu mi-a fost cerut până acum. Colaborez de ani de zile cu serviciul extern SSM și fără el nu pornesc nimic, iar la noi orice cheltuială trece prin SEAP și prin sindicat." (P006) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 3 | "Am văzut de aproape un accident grav și știu ce înseamnă dosarul penal pentru administrator. Testul e gratuit, iar 500 EUR pentru pilot și pachetul de documente intră ușor în bugetul meu, fără aprobări mari de la grup. Dacă testul merge, semnez pilotul." (P017) · "După accidentul pe care l-am văzut de aproape, nu mai vreau oameni singuri noaptea fără nimic care să sune dacă cad. Testul e gratuit, iar 2.500 lei pentru pilot nu trec de aprobările grupului, așa că aș semna pilotul după ce văd raportul din pasul 1, probabil în luna a doua sau a treia." (P021) |
| trust | 1 | "Testul gratuit de o zi răspunde exact la întrebarea mea, adică dacă există semnal în cămine și în zonele greu accesibile, iar pilotul de 2.500 lei e mic pentru bugetul fabricii. Dacă testul iese bine, aș semna pilotul în următoarele 3 luni, nu în prima lună." (P016) |

### What would flip a no

- Referințe de la o fabrică similară din grup sau din țară, certificări și polița de răspundere arătate în scris, plus acordul prealabil al sindicatului și al directorului pentru pilot.
- Testul gratuit să arate scris că alarma ajunge din cele mai grele parcele ale mele și ca serviciul meu SSM să spună că e bun pentru ITM.
- Un control ITM sau o cerință scrisă de auditor pentru lucrul izolat, plus testul gratuit în pădurea mea care să arate că semnalul chiar merge pe teren și că sindicatul acceptă.
- Acordul scris al sindicatului și al directorului după testul gratuit, plus dovada că răspunderea în caz de alarmă ratată e clar împărțită prin contract și acoperită de asigurare.
- Un caz concret, la un client de-al meu, în care ITM sau o evaluare de risc cere explicit măsuri pentru lucrul izolat, plus un preț sub 6 EUR pe lucrător pe lună și ieșire oricând, fără comision pentru mine.
- Un control ITM sau un audit care să ceară explicit măsuri pentru lucrul izolat, plus recomandarea serviciului meu extern SSM și acordul sindicatului după testul gratuit.
- Dacă testul gratuit arată că merge cu aparatura mea existentă (EIP/GPS) sau că agenții îl acceptă, iar prețul scade sub 4-5 EUR pe agent pe lună, fără contract lung, aș lua pilotul.
- Un control ITM sau un audit care îmi cere explicit documentația pentru lucrul izolat, plus referințe de la o firmă de pază comparabilă care folosește sistemul de câteva luni fără căderi.
- O cerință scrisă de la ITM sau de la un auditor pentru lucrul izolat, plus un caz local din Bihor documentat, cu un client care a trecut controlul având dosarul făcut de ei.
- Un control ITM sau un audit care îmi cere în scris măsuri pentru lucrul izolat, sau un accident grav în Bihor la o utilitate ca a noastră, plus un preț sub 5 EUR pe lucrător pe lună.
- Un preț sub 8 EUR pe om pe lună, fără contract de 12 luni, plus testul gratuit care arată că semnalul merge în parcelele mele, iar serviciul meu SSM să spună că ITM chiar cere asta.
- Un acord scris și semnat de sindicat pe modelul lor, plus o utilitate similară din țară care folosește deja sistemul și îmi confirmă că lucrătorii îl poartă.

Buyers say they would buy **0.2 times** in the first month on average.

30 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

Toate prețurile sunt în EUR pe lucrător pe lună, fără TVA. `van_westendorp.py` afișează „$”, dar e vorba de EUR. Răspunsurile vin de la cumpărători **simulați** (`../panel/`): ele aleg ce să testezi, nu dovedesc nimic.

### 1. Ce au spus cumpărătorii (curba Van Westendorp)

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

### 2. Ce cer concurenții (din `../competitors/competitors.md`, calculul meu în EUR)

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

### 3. Ce are nevoie afacerea (CFO, `../cfo/`)

- **C**, clientul cumpără dispozitivul (~130 EUR):
  - la 12 EUR: contribuție 6,79 EUR/lucrător-lună; prag 144 de lucrători la 200 (costuri fixe 975 EUR/lună);
  - la 10 EUR: contribuție 4,95; pragul urcă la 197 de lucrători, adică rezultatul e practic zero la 200.
- **B**, dispozitiv inclus:
  - la 14 EUR: contribuție 5,68; prag 172 de lucrători; ~17.700 EUR blocați în dispozitive la 200 de lucrători;
  - la 20 EUR: contribuție 11,20; prag 87.
- **Concluzia:** sub 12 EUR (C) sau sub ~18 EUR (B) afacerea nu are marjă la scara pe care o poate atinge fondatorul.

### 4. Decizia

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

## The offer

Metoda: `founder-offer`, cu lentila Ofertă din `founder-board/lenses.md`, aplicată ca metodă, nu ca vorbele cuiva. Materia primă:
- obiecțiile din panelul simulat (`../panel/`);
- plângerile din `../competitors/competitors.md`;
- condițiile board-ului (`../board/board.md`);
- costurile CFO-ului (`../cfo/`).

### 1. Lista problemelor (în cuvintele cumpărătorului; „P” = panel simulat, „N” = note)

**Înainte de cumpărare:**
1. „Fără o cerință ITM nu mă mișc” (P, toate segmentele).
2. „Nu pot semna singur: director, grup, sindicat, SEAP” (P, utilitate și HSE).
3. „Nu există nicio referință în Bihor” (P, serviciu extern SSM și HSE).
4. „Cine răspunde dacă alarma nu ajunge și omul moare?” (P; N02 Î10).
5. „O firmă mică din Oradea poate ține dispecerat 24/7?” (P).
6. „100 de lei pe om e mai mult decât tot SSM-ul” (P; N05 §3).
7. „Contract de 24 de luni pentru ceva netestat” (P, v1).
8. „Trebuie să cumpăr eu dispozitivele ca să fac pilotul” (P, v1).
9. „Sindicatul o să spună că-i urmărim” (P; N05 §6).
10. „Dacă recomand și nu merge, răspund eu” (P, serviciu extern SSM).
11. „Alarma ajunge la o firmă de pază concurentă” (P, pază).

**În timpul pilotului:**
12. „N-avem semnal în pădure, cămine, subsoluri, hale metalice” (P; N04 §7).
13. „Alarmele false ne încurcă munca” (P; R §1).
14. „Oamenii îl lasă în dulap după două săptămâni” (P; N05 §6).
15. „Cine face hârtiile: DPIA, nota de informare, procesul-verbal cu sindicatul?” (N02 Î11).
16. „Bateria se descarcă în tură” (R §6).
17. „Nu știu ce să facă dispecerul la o alarmă reală” (R §5 F).

**După pilot:**
18. „Dispozitivul se strică sau e scos din producție” (R §4, GH5200 End of life).
19. „Nu am ce arăta la ITM sau la audit” (R §5).
20. „Nu știu dacă a meritat banii” (N01 §6: nu există dovezi că salvează vieți).
21. „Furnizorul dispare” (risc de firmă cu un singur om; board, Produs).

### 2. Soluțiile, notate (valoare pentru cumpărător 1–5 / cost de livrare 1–5) și ce rămâne

- **Testul de semnal gratuit,** o zi, 3 dispozitive, în cele 10 locuri cele mai grele, cu raport scris. Răspunde la 12 (și parțial la 3). Notă 5/2. **PĂSTRAT**.
- **Pilot plătit mic,** 2.500 lei, cu dispozitive împrumutate. Răspunde la 7, 8 și 2 (intră în bugetul discreționar). Notă 4/2. **PĂSTRAT**.
- **Pachetul de documente făcut de noi**, care rămâne al clientului: completarea evaluării riscurilor pentru lucrul izolat (împreună cu serviciul lui SSM), nota de informare, modelul de acord cu sindicatul, DPIA, procedura de răspuns. Răspunde la 15, 9 și 19. Notă 5/2 (după primul pilot devine șablon). **PĂSTRAT**.
- **Garanția „luna gratuită”** dacă o alarmă nu e preluată în 60 de secunde. Răspunde la 4 și 5. Notă 4/2: ~3% din venit, cost modelat de CFO. **PĂSTRAT**.
- **Contract de 12 luni,** cu ieșire în primele 3 luni. Răspunde la 7. Notă 4/1. **PĂSTRAT**.
- **Polița RC arătată și răspunderea fiecăruia scrisă** (angajator, ILLUSTRUS, firma de pază). Răspunde la 4 și 10. Notă 4/3: ~150 EUR/lună, fără ofertă reală. **PĂSTRAT**, condiționat de o ofertă de asigurare.
- **„Dispeceratul vostru”:** alarmele intră în ecranul nostru la dispecerii proprii ai clientului. Răspunde la 11 (și la 5, pentru fabricile cu pază internă). Notă 4/1. **PĂSTRAT** ca treaptă separată (6 EUR).
- **Pre-alarmă de 20–30 s și reglaj în primele 2 săptămâni,** cu rata de alarme false raportată săptămânal. Răspunde la 13. Notă 4/2. **PĂSTRAT**.
- **Locația doar la alarmă, dispozitivul oprit după program, ștergere după 30 de zile, fără puls.** Răspunde la 9. Notă 5/1. **PĂSTRAT** (cerut oricum de Legea 190/2018 art. 5).
- **Sesiune de 30 de minute cu lucrătorii, la sediu,** ținută de fondator, și „aș continua?” întrebat la final. Răspunde la 14 și 9. Notă 4/2. **PĂSTRAT**.
- **Raport lunar pentru director și dosarul ITM** (alarme de test, timpi, purtare). Răspunde la 19 și 20. Notă 4/1. **PĂSTRAT**.
- **Alarmă de test săptămânală pe echipă și test zilnic automat.** Răspunde la 17, 5 și 16. Notă 4/1. **PĂSTRAT**.
- **Două dispozitive suportate** (TMT250 + o alternativă LTE). Răspunde la 18. Notă 3/3. **PĂSTRAT în spate**, nu se vinde.
- **Inginer de rezervă la apel** din anul 2. Răspunde la 21. Notă 3/3. **PĂSTRAT** ca promisiune de continuitate (escrow de cod + rezervă).
- **Comision de 15% pentru serviciul extern SSM.** Răspunde la 3. Notă 2/2: în v2 a scăzut încrederea („m-ar face să par interesat”). **SCOS din pitch-ul către angajator.** Rămâne un acord separat cu serviciul SSM, după primul client de referință.
- **Satelit Garmin pentru pădure.** Răspunde la 12 în pădure. Notă 3/4. **SCOS din v1** (Produs: un singur segment).
- **Gaze, stres termic, puls.** **SCOASE** (R §1; MDR).

### 3. Stiva finală

- **Nucleul (rezultatul, nu ingredientele):** „Dacă omul tău cade și nu se mai mișcă, un om îl sună în 60 de secunde, iar tu ai dovada cu ora exactă la dosar.”
- **Bonusuri**, fiecare omorând o obiecție:
  1. testul de semnal gratuit (obiecția 12);
  2. pachetul de documente care rămâne al clientului (15, 9, 19);
  3. sesiunea cu lucrătorii și acordul-model cu sindicatul (14, 9).
- **Garanția:** luna gratuită pentru toată echipa dacă o alarmă, de test sau reală, nu e preluată în 60 de secunde. Plus ieșirea fără penalități în primele 3 luni.
- **Urgența (adevărată):** fondatorul poate duce **doar 3 piloți în primul an** (modelul de ore CFO: ~45 h primul pilot, 20 h următorii, 48 h/lună disponibile). Prețul de 12 EUR e blocat 24 de luni pentru acești 3 clienți. Oferta de pilot e valabilă până la 30 iunie 2027.
- **Numele:** „Lucru izolat conform, la cheie”.

### 4. Ecuația valorii (1–10; înainte = pitch-ul v1 din cercetare, după = v2/v3) — judecata mea

- **Rezultatul visat:** 6 → 7. Promisiunea de 60 de secunde cu dovadă e mai clară decât „alarmă”; pachetul de documente adaugă „sunt acoperit la ITM”.
- **Probabilitatea percepută:** 3 → 5. Testul de semnal, garanția și răspunderea scrisă ajută. Lipsește referința locală, cea mai cerută „probă”, care nu se poate cumpăra: vine doar din primul pilot.
- **Timpul până la rezultat:** 4 → 6. Testul de semnal se face într-o zi, pilotul durează 60 de zile în loc de 90, iar documentele le face furnizorul.
- **Efortul și sacrificiul:** 3 → 6. Nu cumperi dispozitive în pilot, nu semnezi 24 de luni, nu scrii hârtiile.
- **Ce rămâne slab:** probabilitatea. Fără o cerință ITM și fără referință, majoritatea nu se mișcă, oricât de bună e oferta.

### 5. Retestarea pe panel (aceleași cărți, seed 2026)

- **v1:** 4/30 (13%), adică HSE 2/6 și serviciu extern SSM 2/6.
- **v2:** 4/30 (13%), adică HSE **3/6**, utilitate **1/6**, serviciu extern SSM **0/6**.
- **Ce a scăzut:** obiecția „trebuie să cumpăr dispozitivele” și obiecția „alarma ajunge la concurent” (paza: de la 6 refuzuri la 1).
- **Ce a crescut:** cererea de referințe (de la 3 la 8) și „fără ITM nu mă mișc” (de la 9 la 12).
- **Concluzia, spusă direct:** oferta a mutat **cine** cumpără (spre HSE-ul fabricilor și utilitatea marcată de un accident), dar **nu câți**. Problema e piața (cerere neformată, declanșator extern), nu oferta. Prețul nu e problema principală la HSE și utilități. La forestier și pază, prețul cerut (4–8 EUR) e sub ce poate susține modelul cu dispecer extern.
- **Varianta finală (v3, `pitch-v3.md`)** schimbă doar structura de preț, după CFO: clientul cumpără dispozitivul + 12 EUR, sau 16 EUR cu dispozitiv inclus, sau 6 EUR pe dispeceratul propriu. Scoate și comisionul SSM din text. **Nu a fost retestată pe panel**: e de testat cu cumpărători reali (12 față de 14 EUR).

### 6. Textul ofertei de pilot (de trimis după testul de semnal)

> **Către:** [Nume], manager HSE, [Fabrica], Oradea
> **Subiect:** Pilot „Lucru izolat conform” — 60 de zile, 20 de lucrători
>
> Bună ziua,
>
> Vă mulțumesc pentru ziua de test din [data]. Raportul atașat arată că alarma a ajuns la dispecer din [X] din cele 10 locuri testate, în medie în [Y] secunde. Locurile fără semnal sunt [lista], cu soluția propusă pentru fiecare.
>
> **Vă propun un pilot de 60 de zile pentru cei 20 de oameni din [mentenanță / tura de noapte / stațiile de pompare]:**
> - Fiecare poartă un dispozitiv certificat Teltonika, prins de vestă. Dacă omul cade și nu se mai mișcă 30 de secunde, sau apasă SOS, dispecerul de serviciu îl sună în sub 60 de secunde. Dacă nu răspunde, sună responsabilul pe care îl desemnați și, la nevoie, 112, după procedura pe care o stabilim împreună.
> - Locația se trimite doar în momentul alarmei. Dispozitivul se oprește după program. Datele se șterg după 30 de zile. Fără puls și fără date medicale.
> - Fiecare pas e salvat cu ora exactă. Primiți un raport săptămânal și, la final, dosarul pentru ITM și audit.
>
> **Ce primiți în pilot:**
> - 20 de dispozitive împrumutate (nu le cumpărați);
> - instruirea la sediu și o sesiune de 30 de minute cu lucrătorii;
> - documentele: completarea evaluării riscurilor pentru lucrul izolat, împreună cu serviciul dumneavoastră SSM; nota de informare; modelul de acord și procesul-verbal cu reprezentanții lucrătorilor; DPIA (evaluarea de impact asupra protecției datelor); procedura de răspuns la alarmă;
> - o alarmă de test pe săptămână pe echipă și un test automat zilnic.
>
> Documentele rămân ale dumneavoastră chiar dacă nu continuăm.
>
> **Prețul pilotului:** 2.500 lei fără TVA, o singură dată, facturat la semnare.
>
> **Ținte pe care le măsurăm împreună:**
> - 100% din alarmele de test ajung la dispecer;
> - cel puțin 95% sunt preluate în sub 60 de secunde;
> - dispozitivul e purtat și conectat în cel puțin 85% din ture;
> - sub 2 alarme false la 100 de ture-om, după primele două săptămâni de reglaj.
>
> **După pilot, doar dacă țintele sunt atinse:**
> - 12 EUR (~60 lei) pe lucrător pe lună fără TVA, cu dispozitivele cumpărate de dumneavoastră la 650 lei bucata, configurate;
> - sau 16 EUR (~80 lei) pe lună cu dispozitivul inclus;
> - contract de 12 luni, din care puteți ieși fără penalități în primele 3 luni.
> - Dacă aveți dispecerat propriu 24/7, alarmele pot intra direct la dispecerii dumneavoastră în ecranul nostru, la 6 EUR pe lucrător pe lună.
>
> **Garanția:** dacă o alarmă, de test sau reală, nu este preluată în 60 de secunde, luna respectivă e gratuită pentru toată echipa.
>
> **Răspunderea:** răspunderea SSM rămâne la angajator, conform legii. Răspunderea noastră e pentru preluarea alarmei și pașii de escaladare, este scrisă în contract și e acoperită de polița RC profesională [asigurător, nr.], pe care v-o trimit odată cu contractul.
>
> **Pe cine aveți în spate:**
> - ILLUSTRUS S.R.L., Oradea, CUI [...];
> - dispeceratul: [firma de pază], autorizată, cu dispeceri 24/7;
> - o persoană de rezervă tehnică la apel.
>
> Pot lua în pilot doar 3 clienți până la 30 iunie 2027.
>
> Cu stimă,
> [Nume], ILLUSTRUS S.R.L.

**Ce trebuie să fie adevărat înainte de a trimite textul:**
- un contract semnat cu firma de pază, cu timp de preluare și penalități;
- o ofertă reală de RC;
- testul de 50 de alarme simulate trecut;
- confirmarea că TMT250 merge pe 4G/LTE-M, nu doar pe 2G.

Altfel, garanția și răspunderea din text nu pot fi promise.

## The numbers

Unealta: `founder-cfo/unit_economics.py`, rulată pe fiecare `*.json` din acest folder. Rapoartele complete ale uneltei sunt fișierele `*_cfo.md`. Cele 36 de luni sunt calculul meu peste ieșirile uneltei (`build_model.py` → `model_36m.md`, `model_36m.json`). Unealta afișează „$”, dar toate sumele sunt **EUR fără TVA**. Intrările sunt aproape toate **estimări** (`cfo-sources.md`). Nu e consultanță financiară sau fiscală: structura, TVA-ul la vânzarea dispozitivelor și contractul cu firma de pază trebuie verificate cu un contabil și un avocat înainte să se miște bani.

### Nota CFO

- **Marja.** Un lucrător lasă puțin, iar marja depinde de dispecerat și de cine plătește dispozitivul:
  - **C (clientul cumpără dispozitivul, 12 EUR/lună):** contribuția e de **6,79 EUR** pe lucrător-lună (57%) cu comisionul de canal, și 7,33 EUR fără el;
  - **B (dispozitiv inclus, 14 EUR):** 5,68 EUR (41%). La 20 EUR, cu dispozitiv inclus: 11,20 EUR (56%);
  - pentru comparație, Scadențarul MM din analiza anterioară lăsa ~61 EUR pe client (94%).
- **Pragul (stare stabilă, vedere amortizată), la C 12 EUR:**
  - 50 de lucrători: −186 EUR/lună; pragul e la 78 de lucrători (`scale_50_C12_cfo.md`);
  - 200 de lucrători (cu 0,25 normă ajutor): +383 EUR/lună (16%); pragul e la 144 de lucrători;
  - 1.000 de lucrători (cu 2 angajați): +3.660 EUR/lună (31%); pragul e la 461 de lucrători.
- **Linia de urmărit: tariful dispecerului.** Nu există niciun tarif românesc găsit (N05 §4):
  - la 4 EUR în loc de 2,50, anul 2 trece de la +2.221 EUR la **−59 EUR** pe operațiuni (`whatif_y2_dispatch400_cfo.md`);
  - imediat după vine rampa: la −20% volum, anul 1 scade de la −4.468 la −4.834 EUR, iar efectul crește în anii următori.
- **Numerarul:**
  - C: **~8.400 EUR** necesari până se autofinanțează, cu taxele de pilot și marja pe dispozitive (cel mai adânc punct e în luna 5). Fără aceste încasări unice, unealta dă **11.013 EUR** (`base_y1_cfo.md`); cumulatul revine pe zero în **luna 21**;
  - B (14 EUR, dispozitiv inclus): **~25.400 EUR** necesari, adică tot capitalul; în 36 de luni nu revine pe zero (−11.235 EUR);
  - **concluzie:** nu finanța dispozitivele din capitalul propriu.
- **Trei pârghii, fiecare dovedită cu unealta (anul 2 al scenariului de bază, profit operațional +2.221 EUR):**
  1. **Prețul de 14 EUR în loc de 12, tot cu dispozitivul cumpărat de client:** anul 2 urcă la **+5.018 EUR** (+2.797 EUR), iar pragul coboară de la 99 la 78 de lucrători (`whatif_y2_price14_cfo.md`).
  2. **Fără minim lunar la pază și RC la 100 EUR/lună:** anul 2 urcă la **+4.621 EUR**, iar pragul ajunge la 70 de lucrători (`whatif_y2_lowfixed_cfo.md`).
  3. **Dispecerat la 1,50 EUR, negociat sau prin dispeceratul propriu al clientului/pazei:** anul 2 urcă la **+3.741 EUR**, cu pragul la 87 (`whatif_y2_dispatch150_cfo.md`).
- **Condițiile de bani ale board-ului:**
  - pilot plătit din prima zi: oferta v2 îl include (2.500 lei), dar nu e încă vândut;
  - bani riscați plafonați la ~6.600 EUR până la prima plată: pornirea C e de 6.546 EUR, iar până în luna 5 se ajunge la 8.421 EUR, adică **puțin peste plafon**;
  - oferte reale pentru RC și pentru dispecerat: **niciuna nu există încă**;
  - concluzie: **nicio condiție nu e îndeplinită**; toate devin metrici de validare (vezi planul).

### Rezultatele pe scurt

**Stare stabilă (vedere amortizată, fișierele `scale_*`):**

- **50 de lucrători** (fondator singur, costuri fixe 525 EUR/lună):
  - C 12 EUR: −186 EUR/lună; C 10 EUR: −278;
  - B 14 EUR: −241 (capital în dispozitive ~4.400 EUR); B 20 EUR: +35.
- **200 de lucrători** (costuri fixe 975 EUR/lună):
  - C 12: +383; C 10: +15;
  - B 14: +161 (capital în dispozitive ~17.700 EUR); B 20: +1.265.
- **1.000 de lucrători** (2 angajați, costuri fixe 3.130 EUR/lună):
  - C 12: +3.660; C 10: +1.820;
  - B 14: +2.550 (capital în dispozitive ~88.500 EUR); B 20: +8.070.

**Treptele din `../pricing/pricing.md`, la 200 de lucrători:**

- **B la 16 EUR** (dispozitiv inclus): contribuție 7,52 EUR, +529 EUR/lună, prag 130 de lucrători (`scale_200_B16_cfo.md`).
- **„Dispeceratul vostru” la 6 EUR** (dispecerul și SIM-ul sunt ale clientului, fără minim la pază): contribuție 5,45 EUR, +265 EUR/lună, prag 151 de lucrători (`scale_200_D6_cfo.md`).

**Pe 36 de luni (vedere numerar, `model_36m.md`):**

- **Bază (C 12 EUR, 10–12 h/săpt):**
  - clienții încep să plătească în lunile 6, 9, 12, 15 și 18, apoi orele se termină;
  - MRR (venit lunar recurent): 840 EUR în luna 12, 2.160 în luna 24, 2.400 în luna 36 (5 clienți, 200 de lucrători);
  - **1.000 EUR MRR în luna 15. 3.000 EUR MRR: niciodată** la 10–12 h/săpt (plafonul e de ~2.400 EUR);
  - anul 1, cu tot cu pornirea: −5.108 EUR; anul 2: +7.536; anul 3: +8.551;
  - numerar necesar: 8.421 EUR; cumulat la 36 de luni: +10.978 EUR.
- **B (14 EUR, dispozitiv inclus, aceeași rampă):**
  - MRR 980 / 2.520 / 2.800 EUR; 1.000 EUR MRR în luna 15; 3.000 niciodată;
  - **numerar necesar: 25.387 EUR**; cumulat la 36 de luni: −11.235 EUR.
- **Pesimist** (10 EUR, dispecerat 4 EUR, client nou la 6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20):
  - MRR 150 / 350 / 850 EUR; **1.000 EUR MRR nu vine în 36 de luni**;
  - numerar necesar: 16.017 EUR; cumulat la 36 de luni: −16.017 EUR, adică nu se recuperează nimic.
- **20 h/săpt din luna 13** (C 12 EUR, client nou la 2 luni):
  - MRR 840 / 3.240 / 5.640 EUR;
  - 1.000 EUR MRR în luna 14, **3.000 EUR MRR în luna 24**;
  - 13 clienți și 470 de lucrători în luna 36; cumulat +43.912 EUR;
  - peste ~300 de lucrători e nevoie de ajutor plătit, pe care modelul nu-l mai adaugă.
- **Costul timpului:** la 20 EUR/h, timpul fondatorului (~960 EUR/lună) depășește tot profitul cumulat din scenariul de bază (calculul meu).

## Launch plan

Toate termenele pornesc de luni, **19 octombrie 2026**, cu ~11 h/săptămână (~48 h/lună; ~140 h în 90 de zile). Țintele numerice sunt **estimări** (modelul de ore și rampa din `../cfo/`). Comparația cu Scadențarul MM și recomandarea de secvență sunt în analiza finală.

### Primele 90 de zile (19.10.2026 – 17.01.2027)

**Săptămânile 1–4: descoperire, fără cod (~40 h)**
- **10–12 conversații calificate**, în ordinea din panel:
  - 5 manageri HSE la fabrici din Oradea (Plexus, Celestica, Connect Group, Emerson; lista din N05 §1);
  - 3 utilități (Compania de Apă Oradea, RER Vest, Termoficare Oradea);
  - 2 firme de pază cu dispecerat;
  - 2 firme forestiere private (Aleșd–Beiuș).
  - **Faist Mekatronic** e evitată: e în concordat (N05 §1).
- **Întrebările** (din R §9): câți oameni lucrează izolat și unde; ce folosesc acum; cine semnează și până la ce sumă fără licitație; ce a cerut ITM-ul sau auditul ISO 45001 pe lucrul izolat; cine e reprezentantul lucrătorilor.
- **ITM Bihor:** cum aplică HG 1091/2006 și dacă un sistem de alarmă cu procedură contează ca „legătură cu exteriorul”.
- **3 oferte scrise de la firme de pază pentru dispecerat:** tarif pe persoană conectată, minim lunar, timp de preluare garantat, penalități, autorizare după Legea 333/2003, acceptarea neconcurenței pe segment.
- **Distribuitorul Teltonika:** TMT250 merge pe 2G sau pe LTE-M/4G? Ce înlocuiește GH5200? Documentația Codec 8; preț la 30 și 200 de bucăți. Se cumpără 3 TMT250 + 1 alternativă LTE.
- **2 oferte de asigurare RC** profesională, care să acopere explicit dispeceratul de alarme pentru persoane (prin broker).
- **O oră de consultanță la un avocat** (dreptul muncii + GDPR) pe răspundere, clauzele de limitare și Legea 333/2003.

**Săptămânile 5–10: lanțul minim (~70 h)**
- **Traccar** primește Codec 8 de la cele 3–4 dispozitive și trimite webhook la **n8n** (pre-alarmă de 30 s; escaladare la 60 s; SMS direct din Traccar ca a doua cale).
- **Ecranul APEX de dispecerat:** coadă cu cronometru, hartă, fișa lucrătorului, butoane pe pași cu ora salvată, ștergere automată după 30 de zile prin PL/SQL. Test automat zilnic. Fără satelit, gaze sau puls.
- **Bench test:** 3 dispozitive purtate 10 ture reale (prieteni, colegi, un client prietenos). Se notează alarmele false și bateria.
- **Testul end-to-end:** 50 de alarme simulate, zi, noapte și weekend, prin operatorii reali ai pazei alese.

**Săptămânile 9–13: primele vânzări (~30 h)**
- **3 teste de semnal gratuite** la cei mai calzi 3 prospecți. Ținta: cel puțin 2 manageri HSE.
- **Trimiterea ofertei de pilot** (`../offer/offer.md` §6) după fiecare test.
- **Metrici go / no-go în ziua 90:**
  - conversații calificate: **GO ≥10**, din care ≥5 HSE sau utilități; **NO-GO <6**;
  - oferte de dispecerat: **GO ≥2**, cu tarif ≤3 EUR/lucrător, minim ≤150 EUR/lună, preluare ≤60 s cu penalități; **NO-GO**: niciuna acceptă SLA cu penalități;
  - dispozitiv confirmat pe LTE-M/4G: **GO da**, cu un al doilea model testat; **NO-GO**: doar 2G și fără înlocuitor;
  - asigurarea RC care acoperă dispeceratul: **GO ofertă ≤2.500 EUR/an**; **NO-GO**: niciun asigurător sau >3.500 EUR/an;
  - testul de 50 de alarme: **GO** 50/50 ajung și ≥95% preluate sub 60 s; **NO-GO**: sub 100% după a doua încercare;
  - alarme false la bench test, după reglaj: **GO <2 la 100 de ture-om**; **NO-GO >5 la 100**;
  - teste de semnal acceptate: **GO ≥3**; **NO-GO ≤1**;
  - **piloți plătiți semnați (2.500 lei): GO ≥1 până în ziua 90** (sau o comandă fermă pentru ianuarie); **NO-GO: 0 după 3 teste de semnal**;
  - orele fondatorului: **GO ≤12 h/săpt**; **NO-GO >15 h/săpt, susținut**;
  - numerarul cheltuit: **GO ≤6.600 EUR**; **NO-GO >9.000 EUR fără niciun pilot plătit**.
- **Decizia din ziua 90:**
  - **GO:** toate cele de mai sus;
  - **PIVOT spre „dispeceratul vostru”:** cumpărătorii vor, dar nicio pază nu acceptă SLA-ul și nicio asigurare nu acoperă. Atunci se vinde doar software-ul (licență de 6 EUR/lucrător) unei firme de pază sau unei fabrici cu dispecerat propriu, iar răspunderea dispeceratului rămâne la ele;
  - **STOP:** oricare dintre NO-GO-urile marcate cu „STOP” de mai jos.

### Primele 12 luni (după cele 90 de zile)

- **Luna 4–5 (feb.–mar. 2027):** primul pilot de 60 de zile, la o fabrică (mentenanță sau tura de noapte, 20 de lucrători). Raport săptămânal; interviuri cu lucrătorii în ziua 55. În paralel, al doilea test de semnal.
- **Luna 6 (apr. 2027):** prima conversie, cu 20 de lucrători × 12 EUR = **240 EUR MRR**, plus vânzarea dispozitivelor (~650 lei bucata). Începe al doilea pilot. Cu acordul clientului, se scrie un **studiu de caz** (timpi de preluare, purtare, alarme false), anonimizat.
- **Luna 7–9:** a doua conversie în luna 9 (~480 EUR MRR). Abia acum, cu o referință, se semnează **acordul de recomandare cu 1–2 servicii externe SSM** (comision de 15%, cu răspunderea furnizorului scrisă). Se oferă licența „dispeceratul vostru” unei singure firme de pază.
- **Luna 10–12:** al treilea client în luna 12. **~70 de lucrători, ~840 EUR MRR** (CFO, scenariul de bază). Primul client crește spre 30 de lucrători.
  - **Decizia din luna 12:** cu ≥3 clienți plătitori și ≥700 EUR MRR, fie se trece la ~20 h/săpt (atunci 3.000 EUR MRR vine în ~luna 24, CFO `h20`), fie se plătește un ajutor part-time. Altfel, vezi condițiile de oprire.
- **Finanțare opțională, fără să depindă de ea:**
  - voucherul de inovare UEFISCDI (≤50.000 lei), cu Universitatea din Oradea, pentru validarea alarmelor false pe datele pilotului;
  - servicii gratuite EDIH (R §8; N06 §7).
- **Ce nu se face în anul 1:** pădurea și satelitul, gazele, stresul termic, pulsul, ML-ul în lanțul de alarmă (AI Act; R §5), dispeceratul propriu 24/7 (care se plătește abia peste ~2.400 de lucrători; R §7) și licitațiile SEAP mari.

### Condițiile de oprire (kill criteria)

Oprești proiectul, nu îl „mai împingi o lună”, dacă se întâmplă oricare dintre următoarele:
1. **Ziua 90:** 0 piloți plătiți după ≥10 conversații calificate și ≥3 teste de semnal. Asta înseamnă că cererea nu există la acest preț și sub această formă.
2. **Nicio firmă de pază** nu acceptă în scris preluarea în ≤60 s cu penalități, la ≤3 EUR/lucrător, **și** niciun prospect nu are dispecerat propriu. Fără acest om care răspunde, nu există produs.
3. **Nicio asigurare RC** nu acoperă dispeceratul de alarme pentru persoane, sau costă peste 3.500 EUR/an. Garanția și răspunderea din ofertă nu se pot susține.
4. **Testul end-to-end** nu ajunge la 100% alarme livrate după două iterații, sau alarmele false rămân peste 5 la 100 de ture-om după reglaj.
5. **În pilot:** purtarea scade sub 60% din ture sau alarmele de test ajung sub 95% (pragurile de oprire din R §6). Se oprește pilotul la acel client. La doi piloți eșuați la rând, se oprește proiectul.
6. **Luna 9:** niciun client plătitor de abonament. **Luna 12:** sub 2 clienți plătitori sau sub 500 EUR MRR.
7. **Timpul:** peste 15 h/săpt timp de două luni la rând, **sau** o alarmă reală (sau de test) care n-a fost preluată pentru că lanțul a depins de fondator (examen, noapte, telefon închis) și nu există încă rezervă plătită.
8. **Banii:** peste 9.000 EUR cheltuiți înainte de primul abonament încasat. Peste o treime din capital s-ar duce înainte de prima dovadă.
9. **Un incident real grav** în care lanțul a eșuat. Se oprește vânzarea până la analiza cauzei și opinia avocatului și a asigurătorului.

## Not done yet

- Marketing: run /founder-marketing
- Brand: run /founder-brand
- Operations: run /founder-ops

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
