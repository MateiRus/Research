# Analiza founder: alarma pentru lucrătorul izolat (ILLUSTRUS S.R.L., Oradea)

**Data:** 12 octombrie 2026
**Statut:** analiză comercială peste cercetarea din acest dosar, cu uneltele pachetului `founder-skill`: board, competitors, consumer, pricing, offer, cfo, plan. **Nu am făcut cercetare web nouă.**
- Fiecare fapt trimite la fișierul și secțiunea din care vine.
- Tot ce e calcul sau judecată proprie e marcat **„estimare”**.
- **Board-ul și panelul de cumpărători sunt simulate:** sunt sub-agenți, iar niciun om real n-a fost întrebat.

**Artefacte:** `/home/user/Research/founder-siguranta/` (subfolderele board, competitors, panel, pricing, cfo, offer, plan).

**Prescurtări pentru citări:**
- **R §n** = raportul `reports/Dispozitiv purtabil siguranță în muncă.md`, secțiunea n.
- **N01–N06** = notele din acest dosar:
  - N01 problema și costurile;
  - N02 cadrul legal (citat pe „Întrebări”, Î);
  - N03 piața și concurenții;
  - N04 hardware și conectivitate;
  - N05 clienți, preț, canale, riscuri;
  - N06 finanțare.
- **FS/…** = un fișier din `founder-siguranta/` (de exemplu `FS/cfo/cfo.md`).
- **AF-MM** = analiza anterioară, `research_notes/Oportunități software în sănătatea predictivă/analiza_founder.md` (Scadențarul MM).

**Prescurtările din text:**
- SSM = securitate și sănătate în muncă;
- HSE = sănătate, securitate, mediu (funcția din fabrici);
- ITM = inspectoratul teritorial de muncă;
- MRR = venit lunar recurent;
- RC = asigurare de răspundere civilă;
- SLA = nivel de serviciu garantat prin contract;
- DPIA = evaluarea de impact asupra protecției datelor;
- SEAP = sistemul electronic de achiziții publice;
- EUR = euro, fără TVA dacă nu se spune altfel.

**Limita surselor (moștenită).** Toată cercetarea a fost scrisă din rezumatele motorului de căutare. Tarifele românești de dispecerat, de SIM-uri IoT și de asigurare RC **nu au fost găsite** (R, „Limita metodei”; N05 §4 Gaps). De aceea aproape toate costurile din CFO sunt estimări.

**Obligația DR-36** (≥10.000 EUR din servicii web) e considerată rezolvată separat, cum s-a cerut. Presupun că cele 10–12 h/săpt merg integral la acest produs.

---

## Pe scurt

- **Verdictul: merită ca afacere doar în forma îngustă de mai jos și doar după un test real. Nu e un prim produs bun pentru tine acum. Scadențarul MM rămâne mai bun ca prim produs** (vezi §9). Verdictul calculat de `compile.py` e **„Not yet”** (FS/plan/v2/business-plan.md):
  - fiecare lucrător lasă bani: 7,33 EUR pe lună în anul 1;
  - **anul 1 pierde 4.468 EUR** pe operațiuni;
  - **doar 13% din panelul simulat cumpără**, sub pragul de 25%;
  - anul 2 trece pe plus (+2.221 EUR, FS/plan/v2_an2), dar panelul rămâne sub prag.
- **Ce produs, exact: „Lucru izolat conform, la cheie”.**
  - Dispozitiv certificat Teltonika: cădere și imobilitate, SOS, locația doar la alarmă.
  - Un dispecer al unei firme de pază partenere sună lucrătorul în sub 60 de secunde, apoi responsabilul clientului, apoi 112.
  - Jurnal cu ora exactă pentru dosarul ITM.
  - **Pachetul de documente făcut pentru client:** evaluarea riscurilor pentru lucrul izolat, nota de informare, acordul cu sindicatul, DPIA, procedura de răspuns.
  - **Fără** pădure, satelit, gaze, puls sau stres termic în anul 1.
  - **Prețul** (estimare, §4): 12 EUR/lucrător/lună cu dispozitivul cumpărat de client (~650 lei), sau 16 EUR cu dispozitiv inclus, sau 6 EUR dacă alarma intră la dispeceratul propriu al clientului. Pilot plătit de 2.500 lei.
- **Primul client: managerul HSE al unei fabrici mari din Oradea**, pentru cei 20 de oameni din mentenanță sau din tura de noapte. Nu utilitatea pe care o propunea cercetarea:
  - în panelul simulat, HSE-ul de fabrică a cumpărat de 2 ori din 6 la prima ofertă și de 3 ori din 6 la oferta refăcută;
  - utilitatea locală a cumpărat de 0 ori din 6, apoi o dată din 6, blocată de director, sindicat și SEAP (FS/panel/rezultate_panel.md);
  - utilitatea rămâne clientul nr. 2, după o referință.
- **Banii, la 10–12 h/săpt** (estimare, FS/cfo/model_36m.md):
  - ~6.500 EUR pornire și ~8.400 EUR numerar până se autofinanțează;
  - **1.000 EUR MRR în luna 15**;
  - **3.000 EUR MRR nu vine**: plafonul e de ~2.400 EUR, la 5 clienți și ~200 de lucrători, pentru că se termină orele;
  - cu ~20 h/săpt din anul 2, 3.000 EUR MRR vine în luna 24;
  - **dacă dispozitivele sunt incluse și le cumperi tu, îți trebuie ~25.400 EUR, adică tot capitalul.**
- **Riscul care decide totul:** omul care răspunde la alarmă e al altei firme. Răspunderea, în schimb, e reală. Fără un SLA scris cu penalități, o ofertă de RC și un test de 50 de alarme reușit, **nu vinzi**. Prima acțiune, săptămâna aceasta: cere ofertă scrisă de dispecerat de la 3 firme de pază din Oradea.

---

## 1. Board-ul (simulat)

**Cum a rulat:**
- trei sub-agenți separați (`claude -p`, model opus, fără unelte), câte unul pe lentilă: Ofertă, Monopol, Produs;
- fiecare a primit doar brieful cu faptele (FS/board/brief.md);
- lentilele sunt rezumate ale unor cadre publicate; membrii nu sunt acele persoane (FS/board/board.md).

**Voturile:**
- **Ofertă: 4/10, FUND IF.** Ce e puternic: cumpărătorii pot fi găsiți după nume, iar documentele și jurnalul se potrivesc cu competențele fondatorului. Ce ar ucide ideea: „piața nu simte durerea” (amenzi mici, CAM fix, fără licitații), lipsa dovezilor că funcționează și un pilot gratuit care nu testează cererea (FS/board/offers.md).
- **Monopol: 3/10, PASS.** Firma de pază care găzduiește dispeceratul vede toate alarmele și clienții, deci poate copia serviciul în luna șase. Stack-ul e copiabil (Teltonika + Traccar + n8n). Nu există avantaj de 10x și nici un „de ce acum” (FS/board/monopoly.md).
- **Produs: 5/10, FUND IF.** Tăierile sunt bune, iar promisiunea încape într-o propoziție. Dar lanțul are multe predări: tracker → SIM → Traccar → n8n → APEX → operatorul de pază → 112. Momentul critic nu e al fondatorului. Iar dispozitivul ales poate să dispară: TMT250 poate fi doar 2G, iar GH5200 e „End of life” (FS/board/product.md; faptele din R §4).
- **Media: 4,0** (2 × FUND IF, 1 × PASS). Scadențarul MM a avut 3 × FUND IF, media 5,7 (AF-MM §C1).

**Riscurile ridicate de mai mulți membri:**
1. lipsesc dovada și încrederea: alarmele false sunt necunoscute, iar 46–59% dintre muncitori ar refuza dispozitivul (N05 §6);
2. firma de pază e și cusătura critică, și primul copiator;
3. cererea nu e formată: nu există licitații și nici vocabular comercial (N05 §7);
4. distribuția e nedovedită.

**Condițiile unite** (de bifat; niciuna nu e îndeplinită azi):
- un pilot plătit din prima zi;
- dispozitiv confirmat pe 4G/LTE-M, plus o rezervă;
- testul cu 50 de alarme simulate, zi, noapte și weekend, prin operatorii reali, **înainte de orice client**;
- SLA cu paza, cu penalități și neconcurență;
- bench test de purtare cu lucrători reali;
- ofertă reală de RC;
- banii riscați ≤ ~6.600 EUR până la prima plată;
- un singur segment în V1.

**Dezacordurile, păstrate:**
- **Primul client:** Ofertă și Produs aleg **Compania de Apă Oradea**. Monopolul alege **firma de pază ca licențiat**: îi vinzi software-ul sub marca ei, ca amenințarea să devină canal.
- **Pachetul de documente:** pentru Ofertă e nucleul valorii, iar Produsul l-ar tăia din V1.
- **Ce a schimbat panelul** (pe care board-ul nu l-a văzut): utilitatea a fost refuzată, iar paza simulată a respins și licența (0/12, cere 4–7 EUR). Rămâne totuși ideea Monopolului ca treaptă: „dispeceratul vostru”, la 6 EUR.

---

## 2. Concurența și poziționarea

Sursa: FS/competitors/competitors.csv (12 rânduri) și competitors.md, din note. **Pasul cu recenziile (1–3 stele) nu s-a putut face:** notele nu conțin recenzii de clienți.

**Cine e acolo:**
- **Direct, dar la distanță (niciunul nu vinde în România):**
  - StaySafe (UK): aplicație 9,50 → 3,30 GBP/utilizator/lună, dispecerat +1,85 GBP (N03 §2);
  - Peoplesafe (UK): 22,6 mil. GBP venit și >350.000 de lucrători; dispozitivul MySOS la 14,99–16,49 GBP/lună, sursă terță (N03 §2; N05 §4);
  - Twig One: 793 EUR (R §3);
  - Blackline G7c: ~56 EUR/lună cu dispecerat (R §3, estimare din prețul public).
- **Indirect:**
  - detectoarele de gaze MSA, Dräger, Honeywell, fără ofertă de lucrător singur (R §3);
  - aplicația gratuită „Safe Alone” din Cluj, cu SMS către un coleg (N03 §3);
  - firmele de pază cu dispecerat, azi pentru obiective (N05 §5);
  - butoanele de panică pentru vârstnici (N05 §7).
- **Substitutul principal:** status quo-ul (coleg, radio, telefon, procedura SSM) la cost suplimentar zero, plus GPS pe utilaje și bodycam la Romsilva (N03 §7; R §5).

**Prețul comparabil** (dispozitiv sau aplicație + dispecerat, pe lucrător pe lună; calculul meu în EUR, estimare):
- cel mai mic: ~6 EUR (StaySafe la scară);
- mediana: ~12 EUR (StaySafe pentru 26–50 de utilizatori, cu dispecerat);
- cu dispozitiv dedicat: ~17,5–19 EUR (Peoplesafe);
- maximul: ~56 EUR (Blackline);
- ancore locale: GPS de flotă ~10 EUR/vehicul, serviciu extern SSM 1,6–5 EUR/angajat (N05 §3).

**Harta (în text), pe două axe:**
- **Axele:** cât de „la cheie” e serviciul în România (limbă, dispecerat local, documente, cineva la sediu) și prețul.
  - Liderii (Blackline, Twig) sunt scumpi și absenți din România.
  - Britanicii au preț mediu și sunt absenți din România.
  - Aplicațiile și status quo-ul sunt gratuite, dar nu sunt „la cheie”.
- **Cadranul gol:** preț mediu (12–16 EUR) și foarte local. Aici stă oferta.

**Plângerile documentate** (din note, nu recenzii):
1. muncitorii nu vor să poarte și se tem de urmărire (N05 §6);
2. alarmele false („un instrument brut”, chiar după un furnizor; R §1);
3. telefonul nu ajunge (buzunar, baterie, semnal; N03 §4);
4. lipsa dovezilor de eficacitate frânează angajatorii (EU-OSHA; R §1).

**Golul:**
- **Ce există:** un gol de **ofertă** documentat. Nimeni nu vinde în Bihor un serviciu în română, cu dispecer local și pachetul de conformitate de la Legea 190/2018 art. 5 (N05 §2, §6; N03 §3).
- **Ce nu există:** un gol de **cerere** documentat. Nu există licitații, nici bloguri SSM, nici căutări (N05 §7). Un cadran gol poate fi gol pentru că nu-l cere nimeni.

**Cine copiază cel mai repede:**
1. firma de pază parteneră (N05 §5, estimare);
2. un distribuitor Blackline, Twig sau Peoplesafe, la clienții mari (N03 §3);
3. un serviciu extern SSM mare (estimare).

---

## 3. Panelul de cumpărători B2B (simulat)

**Cum a rulat:**
- **unealta:** `panel.py`, 30 de cumpărători (câte 6 pe fiecare dintre cele 5 tipuri cerute), seed 2026, aceleași cărți la ambele oferte;
- **cumpărătorii:** fiecare e un **sub-agent separat** (`claude -p`, model sonnet, fără unelte), cu un sufix identic pentru toți (FS/panel/uniform_suffix.txt);
- **definiția lui „cumpără”:** semnează ceva care îl obligă la bani în 3 luni; la serviciul extern SSM: semnează un acord de recomandare și îl propune activ la 2 clienți;
- **controlul:** 60 de răspunsuri, toate valide, salvate cu `panel.py save`. N-am răspuns în locul niciunui cumpărător;
- **limitele:**
  - modelele de limbaj tind să fie de acord, deci rata e o **limită superioară**;
  - răspunsurile sunt corelate (același model);
  - n=6 pe segment e „subțire”;
  - citatele sunt simulate, nu mărturii.

**Rezultatul:**
- **Oferta v1** (cea din cercetare: 20 EUR, contract de 24 de luni, pilot gratuit cu dispozitivele cumpărate de client):
  - **4/30 (13%)**: HSE fabrică 2/6, serviciu extern SSM 2/6;
  - utilitate 0/6, forestier 0/6, pază 0/6 (FS/panel/v1/results.md).
- **Oferta v2** (test de semnal gratuit, pilot plătit cu dispozitive împrumutate și documente incluse, 14 EUR, 12 luni cu ieșire, garanție):
  - **4/30 (13%)**, aceeași rată, alți cumpărători;
  - **HSE fabrică 3/6**, utilitate 1/6 (cel „marcat de un accident”), serviciu extern SSM 0/6, forestier 0/6, pază 0/6 (FS/panel/v2/results.md).
- **Cine cumpără:** la ambele variante, doar cei „marcați de un accident” și cei „deschiși la tehnologie”. Cei care „se mișcă doar la control”, „taie din costuri” sau sunt „conservatori” nu cumpără niciodată.

**Obiecțiile reale** (citate simulate):
- **„Nu pot semna singur”**, 10–11 refuzuri pe „încredere”: „trebuie aprobarea directorului, discuția cu sindicatul și o procedură prin SEAP” (v1/P004, utilitate).
- **„Fără ITM nu mă mișc”:** „Eu mă mișc la SSM doar când vine ITM-ul sau un auditor și cere ceva scris” (v1/P003, forestier). ITM-ul apare în ce-ar schimba decizia la 9 din 26 de refuzuri în v1 și la 12 din 26 în v2.
- **Prețul pe cap de om:** „100 de lei pe om pe lună e mai mult decât plătesc pe tot serviciul SSM” (v1/P011, forestier).
- **Paza nu dă alarmele unui concurent:** „Nu dau alarmele agenților mei pe mâna unei alte firme de pază” (v1/P008).
- **Răspunderea:** „Dacă omul meu cade la 3 noaptea și nimeni nu sună în 60 de secunde, dosarul penal e al nostru, nu al lor” (v1/P021, HSE).
- **Semnalul** în pădure, cămine, subsoluri și hale metalice (v1/P002, P016, P017).

**Ce i-ar face să semneze:**
1. o cerință scrisă a ITM sau a auditorului (cel mai repetat);
2. **o referință locală** cu jurnal real de alarme (de la 3 la 8 cereri explicite în v2);
3. **testul de semnal gratuit**: în v2, 23 din 30 îl pomenesc și majoritatea l-ar accepta, dar spun că „nu e o cumpărare”;
4. acordul sindicatului și al grupului înaintea pilotului;
5. răspunderea scrisă, cu poliță arătată;
6. la forestier și pază, un preț de 4–8 EUR.

**Ce înseamnă, spus direct** (estimare):
- oferta refăcută a mutat **cine** cumpără, nu **câți**;
- problema principală nu e prețul, ci **declanșatorul** (ITM, un accident, o referință);
- **forestierul**, al doilea segment al cercetării, a refuzat la ambele oferte, pe semnal, preț și obișnuință;
- **paza** vrea alarma la ea și un preț pe care modelul cu dispecer extern nu-l susține.

---

## 4. Prețul

Fișierele: FS/pricing/pricing.md și curbele `v1-curve.md`, `v2-curve.md`, `v2-hse-utilitati-curve.md`. Toate sumele sunt în EUR pe lucrător pe lună (unealta afișează „$”).

**Curba (Van Westendorp, pe răspunsuri simulate):**
- **v1:** interval acceptabil **6–20 EUR**; IPP (punctul de indiferență) **11 EUR**; mediane: prea ieftin 5, chilipir 8, scump 15, prea scump 25. **20 EUR e chiar peste marginea de sus** (19,97).
- **v2:** interval **4–16 EUR**; IPP **8 EUR**. Menționarea prețului de 9 EUR pentru „dispeceratul vostru” a tras ancorele în jos (estimare).
- **Doar HSE și utilități:** interval **4–20 EUR**; pragul „scump” median e de 16 EUR.
- **Pragul „scump” pe segment** (v1 / v2):
  - HSE: 21 / 17;
  - serviciu extern SSM: 17 / 15;
  - forestier: 16,5 / 13;
  - utilitate: 14,5 / 15;
  - pază: 14 / 9.

**Ancorele:**
- StaySafe cu dispecerat ~11–13 EUR la echipe mici; Peoplesafe cu dispozitiv ~17,5–19 EUR (N03 §2; N05 §4);
- media europeană ~10 EUR (N03 §5);
- GPS de flotă ~10 EUR/vehicul (N05 §3).

**Ce cere marja** (unealta CFO, la 200 de lucrători):
- **structura C** (clientul cumpără dispozitivul): la 12 EUR, contribuție 6,79 EUR și prag 144 de lucrători; la 10 EUR, prag 197, adică zero profit;
- **structura B** (dispozitiv inclus): la 14 EUR, 5,68 EUR contribuție și 17.700 EUR blocați în dispozitive; la 16 EUR, 7,52 EUR; la 20 EUR, 11,20 EUR (FS/cfo/scale_200_*_cfo.md).

**Recomandarea:**
- **Implicit:** clientul cumpără dispozitivul (~650 lei, configurat), iar abonamentul e de **12 EUR (~60 lei)**, numai pentru lucrătorii expuși, cu contract de 12 luni. E în interval, peste IPP și sub pragul „scump” al HSE și al utilităților. E la nivelul StaySafe pentru echipe mici, cu dispecer local și documente în plus.
- **Scara:**
  - **„Dispeceratul vostru”, 6 EUR** (pentru pază și fabricile cu dispecerat propriu; contribuție 5,45 EUR);
  - **„Standard”, 12 EUR**;
  - **„Standard cu dispozitiv”, 16 EUR**, plafonat la ~60 de dispozitive finanțate de tine;
  - satelitul abia după ce lanțul a fost dovedit.
- **Oferta de deschidere:** test de semnal gratuit + pilot plătit de 2.500 lei, cu prețul de 12 EUR blocat 24 de luni pentru primii 3 clienți, până la 30 iunie 2027. Fără „preț vechi” tăiat.
- **De testat cu cumpărători reali:** 12 față de 14 EUR la primii 6 HSE și utilități calificați. Prețul de 14 EUR ar adăuga ~2.800 EUR în anul 2 (FS/cfo/whatif_y2_price14_cfo.md).

---

## 5. CFO: economia unitară

**Cum s-a calculat:**
- **unealta:** `unit_economics.py`, rulată pe fiecare JSON din FS/cfo/, generat de `build_model.py`;
- **unitatea:** un lucrător echipat pe o lună (`days_per_month = 1`);
- **cele 36 de luni** sunt calculul meu peste ieșirile uneltei, cu o rampă limitată de **orele fondatorului** (48 h/lună);
- **intrările**, aproape toate estimări, sunt în FS/cfo/cfo-sources.md;
- nu e consultanță financiară sau fiscală.

**Intrările-cheie** (estimări):
- **dispozitivul:** TMT250 la 88,50 EUR, preț real (R §4), vândut cu 130 EUR;
- **costurile variabile:** SIM 1,50 EUR, dispecer extern 2,50 EUR (ancorat pe StaySafe; N05 §4), garanția 3% din venit, comisionul SSM de 15% pe 30% din venit din anul 2;
- **costurile fixe (fondator singur), 525 EUR/lună:** găzduire 60, gateway SMS 20, **RC 150 (fără ofertă reală)**, **minim la pază 150**, contabilitate 30, deplasări 100, SIM-uri de test 15;
- **pornirea, 6.546 EUR:** avocat 2.500, consultant SSM 500, parc de pilot 23 × 88,50 EUR, 3 dispozitive LTE alternative, testul cu paza, găzduire, materiale, deplasări;
- **orele:** primul pilot 45 h, următorii 20 h; suport 3 h/client/lună + 0,05 h/lucrător.

**Unit economics la 50 / 200 / 1.000 de lucrători** (stare stabilă, vedere amortizată, structura C la 12 EUR; FS/cfo/scale_*_C12_cfo.md):
- **contribuția:** 6,79 EUR pe lucrător-lună (57%). Scadențarul MM lăsa ~61 EUR pe client (AF-MM §D2);
- **50 de lucrători** (fondator singur, costuri fixe 525 EUR/lună): **−186 EUR/lună**; pragul e la **78 de lucrători**;
- **200 de lucrători** (cu 0,25 normă ajutor, costuri fixe 975 EUR): **+383 EUR/lună** (16% marjă); pragul e la **144**;
- **1.000 de lucrători** (2 angajați, costuri fixe 3.130 EUR): **+3.660 EUR/lună** (31%); pragul e la **461**;
- **dispozitiv inclus la 14 EUR**: −241 / +161 / +2.550 EUR pe lună, cu **4.400 / 17.700 / 88.500 EUR** blocați în dispozitive;
- **la 20 EUR cu dispozitiv inclus** (prețul de listă al cercetării): +35 / +1.265 / +8.070 EUR, dar 20 EUR e peste intervalul acceptat de panel;
- **dispecerat propriu 24/7:** se plătește abia peste ~2.400 de lucrători (R §7). Nu e o opțiune în orizontul analizat.

**Numerarul necesar:**
- **structura C:** ~**8.400 EUR** până se autofinanțează, cu taxele de pilot și marja pe dispozitive. Fără ele, unealta dă **11.013 EUR** (FS/cfo/base_y1_cfo.md). Cel mai adânc punct e în luna 5, iar cumulatul revine pe zero în **luna 21**;
- **structura B (dispozitiv inclus):** **~25.400 EUR**, adică tot capitalul, și cumulatul e încă −11.235 EUR în luna 36. **Nu finanța dispozitivele din capitalul propriu.**

**Anul 1, bază** (structura C, 10–12 h/săpt):
- clienții încep să plătească în lunile 6, 9 și 12;
- 70 de lucrători și **840 EUR MRR** în luna 12;
- profit operațional **−4.468 EUR**; cu pornirea și încasările unice, **−5.108 EUR**;
- anul 2: **+7.536 EUR**; anul 3: **+8.551 EUR** (FS/cfo/model_36m.md).

**Cât până la 1.000–3.000 EUR MRR, la 10–12 h/săpt:**
- **1.000 EUR MRR în luna 15** (4 clienți, 100 de lucrători);
- **3.000 EUR MRR nu vine.** La 5 clienți și ~200 de lucrători orele se termină (~43–45 h din 48), iar MRR-ul se oprește la **~2.400 EUR** (luna 30–36);
- cu **~20 h/săpt din luna 13**: 3.000 EUR MRR în **luna 24**, 13 clienți și ~5.600 EUR MRR în luna 36. Peste ~300 de lucrători e nevoie de ajutor plătit, pe care modelul nu-l mai adaugă.

**Scenariul pesimist** (10 EUR/lună, dispecer la 4 EUR, client nou la 6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20):
- MRR 150 / 350 / 850 EUR în lunile 12 / 24 / 36;
- **1.000 EUR MRR nu vine în 36 de luni**;
- se pierd ~16.000 EUR și nu se recuperează nimic (FS/cfo/pess_y*_cfo.md).

**Linia de urmărit: tariful dispecerului.** La 4 EUR în loc de 2,50, anul 2 trece de la +2.221 EUR la **−59 EUR** pe operațiuni (FS/cfo/whatif_y2_dispatch400_cfo.md).

**Trei pârghii, fiecare dovedită cu unealta** (pe anul 2):
1. prețul de 14 EUR în loc de 12: **+5.018 EUR** în loc de +2.221;
2. fără minim la pază și RC la 100 EUR/lună: **+4.621 EUR**;
3. dispecer la 1,50 EUR: **+3.741 EUR**.

**Timpul tău:** la 20 EUR/h, cele ~48 h/lună valorează ~960 EUR/lună, adică mai mult decât tot profitul cumulat în 36 de luni în scenariul de bază (+10.978 EUR față de ~34.560 EUR; estimare).

---

## 6. Oferta de pilot (text concret)

Construcția ofertei, notarea soluțiilor și ecuația valorii sunt în FS/offer/offer.md. Pitch-ul final e în `pitch-v3.md`: structura de preț după CFO, **neretestată pe panel**, de testat cu oameni reali. Textul de mai jos se trimite **după** testul de semnal gratuit.

> **Către:** [Nume], manager HSE, [Fabrica], Oradea
> **Subiect:** Pilot „Lucru izolat conform” — 60 de zile, 20 de lucrători
>
> Bună ziua,
>
> Vă mulțumesc pentru ziua de test din [data]. Raportul atașat arată că alarma a ajuns la dispecer din [X] din cele 10 locuri testate, în medie în [Y] secunde. Locurile fără semnal sunt [lista], cu soluția propusă pentru fiecare.
>
> **Vă propun un pilot de 60 de zile pentru cei 20 de oameni din [mentenanță / tura de noapte]:**
> - Fiecare poartă un dispozitiv certificat Teltonika, prins de vestă. Dacă omul cade și nu se mai mișcă 30 de secunde, sau apasă SOS, dispecerul de serviciu îl sună în sub 60 de secunde. Dacă nu răspunde, sună responsabilul pe care îl desemnați și, la nevoie, 112, după procedura pe care o stabilim împreună.
> - Locația se trimite doar în momentul alarmei. Dispozitivul se oprește după program. Datele se șterg după 30 de zile. Fără puls și fără date medicale.
> - Fiecare pas e salvat cu ora exactă. Primiți un raport săptămânal și, la final, dosarul pentru ITM și audit.
>
> **Ce primiți în pilot:**
> - 20 de dispozitive împrumutate (nu le cumpărați);
> - instruirea la sediu și o sesiune de 30 de minute cu lucrătorii;
> - documentele: completarea evaluării riscurilor pentru lucrul izolat, împreună cu serviciul dumneavoastră SSM; nota de informare; modelul de acord și procesul-verbal cu reprezentanții lucrătorilor; DPIA; procedura de răspuns la alarmă;
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
> - sau 16 EUR (~80 lei) cu dispozitivul inclus;
> - contract de 12 luni, din care puteți ieși fără penalități în primele 3 luni.
> - Dacă aveți dispecerat propriu 24/7, alarmele pot intra direct la dispecerii dumneavoastră în ecranul nostru, la 6 EUR pe lucrător pe lună.
>
> **Garanția:** dacă o alarmă, de test sau reală, nu este preluată în 60 de secunde, luna respectivă e gratuită pentru toată echipa.
>
> **Răspunderea:** răspunderea SSM rămâne la angajator, conform legii. Răspunderea noastră e pentru preluarea alarmei și pașii de escaladare, e scrisă în contract și acoperită de polița RC profesională [asigurător, nr.], pe care v-o trimit odată cu contractul.
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

**Ce trebuie să fie adevărat înainte să trimiți textul:**
- contract semnat cu firma de pază, cu timp de preluare și penalități;
- o ofertă reală de RC;
- testul cu 50 de alarme trecut;
- TMT250 confirmat pe 4G/LTE-M.

Altfel, garanția și răspunderea din text nu pot fi promise. **Limita de 3 piloți e adevărată:** în modelul de ore nu încap mai mulți în primul an (FS/cfo/model_36m.md).

**Ecuația valorii** (1–10, judecata mea; v1 → v3):
- rezultatul: 6 → 7;
- **probabilitatea: 3 → 5**. Rămâne cea mai slabă, pentru că referința locală nu se poate cumpăra;
- timpul: 4 → 6;
- efortul: 3 → 6.

---

## 7. Planul

Detaliile sunt în FS/plan/plan_90z_12l.md. Pornește pe 19.10.2026, cu ~11 h/săpt.

**Primele 90 de zile (până la 17.01.2027):**
- **Săptămânile 1–4, fără cod (~40 h):**
  - 10–12 conversații calificate: 5 HSE de fabrică (Plexus, Celestica, Connect Group, Emerson; N05 §1), 3 utilități, 2 firme de pază, 2 forestieri. **Faist Mekatronic e evitată**, pentru că e în concordat (N05 §1);
  - o întrebare la ITM Bihor despre HG 1091/2006;
  - **3 oferte scrise de dispecerat** (tarif, minim, SLA, Legea 333/2003, neconcurență);
  - distribuitorul Teltonika: TMT250 merge pe 2G sau pe LTE? Ce înlocuiește GH5200? (R §9);
  - 2 oferte de RC;
  - o oră de consultanță la un avocat.
- **Săptămânile 5–10 (~70 h):**
  - lanțul minim: Traccar → n8n (pre-alarmă de 30 s, escaladare la 60 s, SMS direct ca a doua cale) → ecranul APEX de dispecerat, cu ștergere după 30 de zile și test zilnic (R §6);
  - bench test cu 3 dispozitive în 10 ture;
  - **testul cu 50 de alarme** prin dispecerii reali.
- **Săptămânile 9–13 (~30 h):**
  - 3 teste de semnal gratuite la cei mai calzi prospecți (cel puțin 2 HSE);
  - trimiterea ofertei de pilot.
- **Metricile go / no-go din ziua 90:**
  - **GO** dacă:
    - ≥10 conversații calificate;
    - ≥2 oferte de dispecerat la ≤3 EUR/lucrător, cu minim ≤150 EUR și SLA ≤60 s cu penalități;
    - dispozitivul e confirmat pe LTE-M/4G;
    - există o ofertă de RC ≤2.500 EUR/an;
    - testul cu 50 de alarme iese 50/50, cu ≥95% preluate sub 60 s;
    - alarmele false sunt <2 la 100 de ture-om;
    - ≥3 teste de semnal acceptate;
    - **≥1 pilot plătit semnat**;
    - orele ≤12 h/săpt și cheltuielile ≤6.600 EUR.
  - **PIVOT** spre „dispeceratul vostru” (licență de 6 EUR la o fabrică sau la o pază cu dispecerat propriu, cu răspunderea dispeceratului la ele): cumpărătorii vor, dar nicio pază nu semnează SLA-ul sau nicio asigurare nu acoperă riscul.
  - **STOP:** vezi §8.

**Primele 12 luni:**
- **Lunile 4–5:** primul pilot de 60 de zile la o fabrică; al doilea test de semnal.
- **Luna 6:** prima conversie (20 de lucrători × 12 EUR = 240 EUR MRR, plus vânzarea dispozitivelor). Începe al doilea pilot. Un studiu de caz anonimizat, cu acordul clientului.
- **Lunile 7–9:** a doua conversie (~480 EUR MRR). Abia acum, cu o referință, vine acordul de recomandare cu 1–2 servicii externe SSM. În v2, comisionul arătat direct angajatorului a scăzut încrederea. Se oferă licența „dispeceratul vostru” unei singure paze.
- **Lunile 10–12:** al treilea client; **~70 de lucrători și ~840 EUR MRR**.
  - **Decizia din luna 12:** fie ~20 h/săpt (atunci 3.000 EUR MRR vine în ~luna 24), fie ajutor part-time, fie oprire.
- **Finanțare opțională:** voucherul UEFISCDI (≤50.000 lei), cu Universitatea din Oradea, pentru validarea alarmelor false; servicii gratuite EDIH (R §8; N06 §7). Pilotul nu depinde de ele.
- **Ce nu faci în anul 1:**
  - pădurea și satelitul, gazele, pulsul, stresul termic;
  - ML în lanțul de alarmă (AI Act; R §5);
  - dispecerat propriu 24/7;
  - licitații SEAP mari.

---

## 8. Condițiile de oprire (kill criteria)

Oprești, nu „mai împingi o lună”, dacă se întâmplă oricare dintre următoarele:
1. **Ziua 90:** 0 piloți plătiți după ≥10 conversații calificate și ≥3 teste de semnal.
2. **Nicio firmă de pază** nu acceptă în scris preluarea în ≤60 s cu penalități, la ≤3 EUR/lucrător, **și** niciun prospect nu are dispecerat propriu.
3. **Nicio asigurare RC** nu acoperă dispeceratul de alarme pentru persoane, sau costă peste 3.500 EUR/an.
4. **Testul end-to-end** nu ajunge la 100% alarme livrate după două iterații, sau alarmele false rămân peste 5 la 100 de ture-om după reglaj.
5. **În pilot**, purtarea scade sub 60% din ture sau alarmele de test ajung sub 95% (pragurile din R §6). Se oprește la acel client, iar după doi piloți eșuați la rând se oprește tot.
6. **Luna 9:** niciun abonament plătit. **Luna 12:** sub 2 clienți plătitori sau sub 500 EUR MRR.
7. **Timpul:** peste 15 h/săpt două luni la rând, **sau** o alarmă (reală sau de test) nepreluată pentru că lanțul a depins de tine (examen, noapte, telefon închis) înainte să existe o rezervă plătită.
8. **Banii:** peste 9.000 EUR cheltuiți înainte de primul abonament încasat.
9. **Un incident real grav** în care lanțul a eșuat. Se oprește vânzarea până la analiza cauzei, cu avocatul și asigurătorul.

---

## 9. Comparația cu „Scadențar MM” (analiza anterioară)

**Pe aceleași unelte** (AF-MM §C–E pentru Scadențar; restul din acest document):
- **Board:**
  - Scadențar: 3 × FUND IF, media 5,7;
  - alarmă: 2 × FUND IF + 1 × PASS, media 4,0.
- **Panel simulat:**
  - Scadențar: 35% la prima ofertă, 15% la a doua;
  - alarmă: 13% la ambele.
- **Verdictul calculat:**
  - Scadențar: „Profitable” (fragil: +534 EUR în anul 1);
  - alarmă: „Not yet” (−4.468 EUR în anul 1).
- **Bani pe client:**
  - Scadențar: ~61 EUR contribuție pe client-lună (94%);
  - alarmă: 6,79–7,33 EUR pe lucrător-lună (57–61%), adică ~150–290 EUR pe client-lună la 20–40 de lucrători. **Pe client, alarma aduce mai mult.**
- **Numerar necesar:**
  - Scadențar: ~3.800 EUR;
  - alarmă: ~8.400 EUR (C) sau ~25.400 EUR (B).
- **MRR la 10–12 h/săpt:**
  - Scadențar: 1.000 EUR în ~luna 18, plafon ~1.600 EUR;
  - alarmă: 1.000 EUR în luna 15, plafon ~2.400 EUR. **Alarma ajunge puțin mai repede și mai sus.**
  - **3.000 EUR:** niciunul nu ajunge la 10–12 h/săpt. La ~20 h/săpt: Scadențar ~luna 31, alarmă ~luna 24.
- **Cumulat la 36 de luni:** Scadențar ~+22.200 EUR, alarmă ~+11.000 EUR.
- **Riscul:**
  - Scadențarul e software administrativ: fără 24/7, fără hardware, fără risc de viață și moarte, nu e dispozitiv medical (AF-MM §E2);
  - alarma cere răspuns non-stop prin alt operator, dispozitive, sindicat și DPIA la fiecare client, cu răspundere reală la vătămare (N02 Î10; R §5).

**Care e mai bun ca prim produs:** **Scadențarul MM.** Alarma are un MRR mai mare pe client și un plafon puțin mai înalt. Dar are:
- o contribuție pe oră de suport comparabilă (~35–65 EUR pe oră de suport la alarmă față de ~61 EUR la Scadențar, estimare), dar mult mai multe ore de pilot și de vânzare pe fiecare client câștigat;
- un an 1 pe pierdere;
- de 2 ori mai mult numerar;
- un risc pe care un student cu 10–12 h/săpt nu-l poate ține singur noaptea;
- dovezi mai slabe la board și în panel.

**Se combină? Da, dar în secvență, nu în paralel** (estimare):
1. **Anul 1: Scadențarul MM.** Același stack (APEX, PL/SQL, n8n) și aceleași modele GDPR (contract art. 28, DPA, retenție).
2. **În paralel, doar cu cost aproape zero**, adaugi în conversațiile Scadențarului 3 întrebări despre lucrul izolat. Cabinetele de medicina muncii văd anual toți angajații și știu cine lucrează în ture sau izolat (N05 §5). Ceri și cele 3 oferte de dispecerat, care sunt ieftine și decid totul.
3. **Portalul angajatorului din Scadențar** poate avea un câmp „post cu lucru izolat (HG 1091/2006)”. Asta devine lista de prospecți pentru alarmă și canalul ei, prin cabinet sau serviciul SSM, cu comision.
4. **Alarma pornește ca produs în anul 2:** când există ≥2 clienți Scadențar ca referință de încredere, ≥3 manageri HSE care cer pilotul și un SLA de dispecerat semnat. Începe întâi cu „dispeceratul vostru” la fabricile cu pază internă, unde răspunderea dispeceratului rămâne la client.

**Ce ar răsturna comparația** (estimare):
- dacă ≥2 programe MM au deja portal pentru angajator, Scadențarul pierde golul (AF-MM §E5);
- dacă un manager HSE real semnează pilotul de 2.500 lei în primele 60 de zile **și** o pază semnează SLA-ul, alarma devine competitivă ca prim produs;
- dacă ITM Bihor începe să ceară explicit măsuri pentru lucrul izolat, declanșatorul pe care panelul îl tot cere apare de la sine.

---

## Anexă: unde sunt artefactele (`/home/user/Research/founder-siguranta/`)

- `idea.md`: ideea.
- **`board/`:** `brief.md`, `prompt_*.md`, cele trei memorii (`offers.md`, `monopoly.md`, `product.md`) și `board.md`, cu rezumatul și condițiile.
- **`competitors/`:** `competitors.csv` și `competitors.md`.
- **`panel/`:**
  - intrările: `customer.json`, `pitch-v1.md`, `pitch-v2.md`, `uniform_suffix.txt`, `run_panel.sh`;
  - rulările `v1/` și `v2/` (cărți, brief-uri, răspunsuri, răspunsurile brute, `results.md`, `results.json`);
  - `rezultate_panel.md`.
- **`pricing/`:** curbele `v1-curve.md`, `v2-curve.md`, `v2-hse-utilitati-curve.md` (plus CSV-ul) și `pricing.md`.
- **`cfo/`:**
  - `build_model.py`;
  - toate intrările `*.json` și ieșirile uneltei `*_cfo.md`: stare stabilă `scale_*`, ani `base_*`, `baseB_*`, `pess_*`, `h20_*`, what-if-uri `whatif_*`;
  - `model_36m.md` / `.json`, `cfo-sources.md`, `cfo.md`.
- **`offer/`:** `offer.md` (lista problemelor, stiva, ecuația valorii, retestarea, textul de pilot) și `pitch-v1/v2/v3.md`.
- **`plan/`:**
  - `plan_90z_12l.md`;
  - planurile compilate cu `compile.py`: `v1/`, `v2/` (cu `summary.md`, `one-pager.md`, `business-plan.md`) și `v2_an2/` (cifrele din anul 2). Toate trei au verdictul „Not yet”.
- `bulletproof/` **nu e făcut de mine.** A apărut în același folder în timpul lucrului, dintr-o sesiune paralelă. Ideea lui centrală (alarma merge la dispeceratul non-stop al clientului) se potrivește cu treapta „dispeceratul vostru” de aici. Nu l-am folosit ca sursă.

_Board-ul și panelul sunt simulate. Cifrele sunt proiecții din estimări. Confirmă cererea cu cumpărători reali și costurile cu oferte reale înainte să cheltuiești. Nu e consultanță financiară, juridică sau fiscală._
