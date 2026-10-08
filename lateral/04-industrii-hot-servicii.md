# Sesiunea laterală 4: industrii fierbinți → servicii (cercetare + analogie forțată)

**Cererea fondatorului:** vrea să vândă **servicii**, nu un produs software și nu „site-uri” ca atare. Site-ul poate veni în pachet, pentru că se face repede cu AI. Metoda cerută: întâi caută industriile fierbinți din România, apoi gândește ce poate face el pentru ele.

**Constrângeri păstrate:** 10–12 h/săptămână; Oracle APEX / PL/SQL, n8n, Python, WordPress, LLM; Bihor (Oradea); fără e-mail rece (telefon și vizite da); minimum 10.000 EUR venituri în 12–15 luni.

**Tehnica laterală folosită:** analogie forțată (Synectics, Gordon 1961), pe care n-am mai rulat-o în sesiunile 1–3. Am ales-o pentru că acum avem industriile concrete și căutăm *mecanisme* de serviciu care funcționează în alte domenii și se pot muta aici.

---

## Pasul 1. Ce industrii sunt fierbinți (ce am găsit)

| Industrie | Semnal | Sursă |
|---|---|---|
| Firme noi, total | 153.425 înmatriculări în 2025, +22,8% față de 2024 | Capital, date ONRC |
| Top domenii la firme noi 2025 | 1 construcții (6.545), 2 transport cu șofer la comandă (3.955), 3 transport marfă (3.712), 4 retail nealimentar, 5 software, 6 comerț online (3.174), 7 consultanță, 8 restaurante (2.706), 10 service auto (2.422) | StartupCafe, estimări identitate.ro |
| Cele mai dinamice în ultimii ani | construcții, IT, servicii medicale; piața medicală privată > 15 mld. lei în 2025 | ZF, Economedia |
| Stomatologie | piață privată > 7 mld. lei în 2025; **732 de firme în Bihor, 72% în Oradea (~527)**; ~30.000 de pacienți străini în 2024; diaspora vine acasă vara și de Crăciun (Life Group: +20% programări în decembrie) | Termene.ro, Romania Insider, Business Forum |
| Medicină estetică | venituri > 130 mil. EUR în 2025, dublu față de 2018 (sursa nu e numită, de verificat); Skinmed: +30% clienți noi | Capital, Revista Biz |
| Fotovoltaice / prosumatori | ~248.000 de prosumatori (iulie 2025), +10.000/lună; 87% din sistemele noi E.ON au baterie. **Casa Verde Baterii 2026**: Ordinul 1.904/2026 (MO 14.09.2026), 400 mil. lei, până la 15.000 lei per prosumator existent, lansare anunțată pentru octombrie 2026, selecție după punctaj (contribuție proprie + capacitate), apoi beneficiarul are 90 de zile să-și aleagă instalatorul validat. **Legea 160/2026**: decontare lunară sub 27 kW, deci surplusul nu se mai reportează 24 de luni și bateria devine mai valoroasă | ANRE prin Economica, Forbes, Financiarul, Economedia, Agerpres |
| Muncitori străini | 148.000 de non-UE cu permis la final de 2025 (+48%); contingent de 90.000 pentru 2026; **~1/3 pleacă înainte de finalul contractului** spre Vest; 28% spun că limba e cea mai mare problemă; ~1.700 de agenții, OUG 32/2026 cu garanție de 75.000 EUR; platforma WorkinRomania funcționează din august 2026 (acoperă actele, nu comunicarea) | Antena 3, Profit, TVR Info, Economedia, Romania Insider |
| Cazare Oradea / Felix | Oradea: −6% turiști în 2025, dar număr **record** de apartamente în regim hotelier pe platforme, deci supraofertă; Booking a eliminat clauzele de paritate (DMA), așa că prețul direct poate fi mai mic | Visit Oradea, Economedia |
| Service auto | 15.000–23.000 de firme, peste 90% micro; reparațiile +22,6% în mai 2025 față de mai 2024; 42% din vizite sunt pentru revizie și 35% pentru ITP | Sierra Quadrant prin StartupCafe, Puterea |
| Context general | România e ultima în UE la folosirea AI în firme: 5,2% față de 20% media UE (2025) | Eurostat prin Business Forum |

### Industrii eliminate, pe scurt

- **Transport cu șofer (Uber/Bolt):** ANAF a blocat plățile către 100 de flote, DNA face percheziții, iar șoferii trec pe PFA. Cumpărătorii sunt instabili și sectorul e în zonă gri. Eliminat.
- **Construcții:** cele mai multe firme noi, dar 62% se așteaptă la mai puține lucrări în 2026, iar lead-urile pentru constructori sunt o piață de agenții deja aglomerată. Slab.
- **Cabinete contabile:** durerea e reală (e-Factura, SAF-T, documente întârziate), dar piața e plină de software (SmartBill, Keez, TaxDome), iar contabilii sunt conservatori. Slab.
- **Accesibilitate pentru magazine online (Legea 232/2022, din 28.06.2025):** obligație reală, dar microîntreprinderile sunt exceptate, nu am găsit cine controlează și ce amenzi sunt, iar munca cere specializare. Slab pentru acum.

---

## Pasul 2. Structura problemei, fără vocabularul industriei

> Un profesionist ocupat cu munca de bază pierde bani în **momentele dintre**: între ofertă și decizie, între două vizite, între sosire și plecare. Nimeni nu are sarcina să le urmărească. În plus, banii vin în **valuri** (sezon, sesiune de finanțare, diaspora acasă), iar firma le prinde nepregătită.

---

## Pasul 3–4. Domeniile analogiei și ce mutăm înapoi

### 🍽 Expeditorul de la pass, într-o bucătărie de restaurant (operațional)

- **Roluri:** bonul = planul de tratament / oferta / dosarul; lampa de încălzire = perioada în care oferta așteaptă; expeditorul = eu.
- **Ce face domeniul și noi nu:** expeditorul are tabla cu toate bonurile deschise și ora fiecăruia. Nimic nu stă sub lampă fără să fie strigat înapoi, și nimic nu iese incomplet.
- **Mecanism mutat:** un serviciu care **deține lista ofertelor deschise** ale firmei și le urmărește până la „da” sau „nu”:
  - la stomatologi, planurile de tratament prezentate și neprogramate;
  - la instalatori, clienții vechi eligibili pentru baterie.
  Software-ul are deja datele (de exemplu, Zarina CRM are planuri de tratament, Dentware are SMS-uri), dar **nimeni nu face munca de urmărire**.
- **Rezultat: păstrat, cea mai puternică analogie.**

### 🍄 Rețeaua de micorize, ciupercile din rădăcini (biologic)

- **Roluri:** firma = planta; eu = ciuperca; apa și sărurile din afara rădăcinii = clienții sau oamenii pe care firma nu-i poate atinge (altă limbă, departe); zahărul = plata.
- **Ce face domeniul și noi nu:** ciuperca extinde raza rădăcinii de zeci de ori și e plătită **proporțional cu ce aduce**.
- **Mecanism mutat:**
  1. extinderea razei peste bariera de limbă, pe care AI o face ieftină: pagini și mesaje în limba pacientului din diaspora sau din străinătate, ori în limba muncitorului nepalez, vietnamez sau indian;
  2. preț legat de rezultat: plătești pentru ce s-a programat sau pentru cine a rămas.
- **Rezultat: păstrat.**

### 🛫 Sloturile din controlul traficului aerian (operațional)

- **Roluri:** fereastra care se deschide și se închide = sesiunea de finanțare / sezonul; avioanele = dosarele.
- **Ce face domeniul și noi nu:** totul e aliniat pe pista de rulare **înainte** de deschiderea slotului, iar ordinea e decisă dinainte.
- **Mecanism mutat:** pregătirea dosarelor **înainte** să se deschidă sesiunea Casa Verde Baterii:
  - liste de clienți calificați;
  - acte strânse și verificate;
  - punctajul simulat.
  Când se deschide, clienții instalatorului depun primii, cu dosar complet.
- **Rezultat: păstrat.**

### 🚐 Microbuzul de colete al diasporei (social / cultural)

- **Roluri:** românii din Italia și Spania vin acasă în valuri (vara, Crăciunul); transportatorul anunță cursele cu săptămâni înainte în grupuri și prin telefon.
- **Ce face domeniul și noi nu:** lucrează **pe calendarul altcuiva** și rezervă capacitatea înainte ca oamenii să ajungă.
- **Mecanism mutat:** campania „vii acasă de Crăciun? programează-te acum”, pentru clinici și service-uri: dentistul și revizia înainte de drumul înapoi.
- **Rezultat: păstrat ca modul în pachet, nu ca serviciu separat**, pentru că e sezonier.

### 🦠 Celulele de memorie ale sistemului imunitar (biologic)

- **Roluri:** clienții vechi = antigenii memorați…
- Pentru ca analogia să funcționeze, clientul ar trebui să fie și amenințarea, și prietenul. Asta e un al doilea rol forțat. Singurul transfer rămas e „ține minte clienții vechi”, adică un CRM, pe care îl aveam deja.
- **Rezultat: abandonat, analogie de suprafață.**

---

## Pasul 5. Meta-tiparul

Toate transferurile care au mers vând **proprietatea asupra unui moment care există deja, dar nu are stăpân**:

- planul de tratament după consultație;
- săptămânile dinaintea unei sesiuni de finanțare;
- bariera de limbă;
- calendarul diasporei.

**Site-ul nu e niciodată produsul. E ghișeul unde aterizează momentul.** De asta poate fi „inclus”: costă puțin și nu e motivul pentru care se plătește.

Pentru că momentul se poate număra (programat, depus, rămas), toate trei se pot vinde **cu plată legată de rezultat**. Asta le face „prea bune ca să le refuzi”. Analogia abandonată a murit tocmai pentru că „memoria” fără un stăpân al momentului e doar o bază de date.

Tiparul confirmă și sesiunea 3 („banii expuși”), dar acum în formă de **serviciu**, nu de produs software.

---

## Pasul 6. Clasament onest: pachetele de servicii

### 1. „Planuri recuperate”: pentru clinici stomatologice și de estetică (Oradea)

**Ce vinzi, într-o frază:** „Recuperez pacienții care au primit plan de tratament și nu s-au mai programat, plus pe cei care au sărit controlul de 6 luni. Site-ul e inclus.”

**De ce acum:**
- piață de peste 7 mld. lei, cu ~527 de firme dentare doar în Oradea, deci poți merge pe jos de la una la alta;
- în benchmark-urile internaționale (cifre de furnizori, deci optimiste), 30–60% din tratamentele prezentate nu se programează niciodată, iar urmărirea recuperează 20–30%;
- absențele la programări sunt de 15–20%.

**Ce faci concret:**
1. În fiecare săptămână iei din programul clinicii lista planurilor neprogramate și a pacienților fără control de peste 6 luni.
2. Mesaje WhatsApp/SMS scrise cu AI, în numele clinicii, personalizate pe tratament, plus un scenariu scurt pentru recepție pentru cine nu răspunde.
3. Reminder înainte de programare și cerere de recenzie Google după vizită.
4. Campanie pentru diaspora în noiembrie și iunie.
5. Raport lunar: câți s-au programat și câți lei înseamnă.

**Site-ul din pachet:** refacere sau site nou, cu o pagină pe tratament, programare online și pagini RO/EN/HU/DE pentru diaspora și pacienții străini.

**Demo la prima vizită:** „Câte planuri ați prezentat anul ăsta care nu s-au început? Înmulțim cu valoarea medie.” Numărul se scoate din programul lor în 5 minute.

**Preț de testat:**
- 400 EUR setup, cu site inclus, plus 175 EUR/lună;
- garanție: dacă în primele 60 de zile se programează mai puțin de 5 pacienți din listă, a doua lună e gratuită.

**Calcul spre 10.000 EUR:**
- se semnează câte o clinică pe lună, din luna 2, până la 5 clinici;
- 45 de luni-client × 175 = 7.875 EUR, plus 5 × 400 = 2.000 EUR, deci ≈ **9.900 EUR în primele 12 luni** și peste 10.000 în luna 13;
- timp: ~3 h/lună per clinică după setup (~10 h), deci 15 h/lună la 5 clinici.

**Riscuri:**
- date de sănătate: lucrezi ca persoană împuternicită de clinică, cu contract de prelucrare, și mesajele pleacă în numele clinicii;
- fiecare clinică are alt program de gestiune;
- unele recepții sună deja pacienții;
- există agenții de marketing dentar, dar ele vând reclame (pacienți noi), nu urmărirea planurilor existente.

### 2. „Bateria”: pentru instalatorii de fotovoltaice (val în octombrie 2026)

**Ce vinzi, într-o frază:** „Clienții tăi vechi pot lua până la 15.000 lei pentru baterie. Eu îi găsesc, le simulez punctajul, le strâng actele și ți-i aduc gata de semnat.”

**De ce acum:**
- programul Casa Verde Baterii (400 mil. lei) are lansarea anunțată pentru octombrie 2026;
- Legea 160/2026 face surplusul mai puțin util fără baterie;
- fiecare instalator are sute de clienți vechi, toți prosumatori, deci eligibili.

**Ce faci concret:**
1. Landing page cu **simulator de punctaj**: 50 de puncte pentru contribuția proprie și 50 pentru capacitate. Simulatorul arată „cu 15 kWh în loc de 10 urci în clasament”, ceea ce e și upsell pentru instalator.
2. Iei lista clienților vechi și le trimiți mesaje în numele instalatorului.
3. Bot de colectare a actelor, cu verificare AI de completitudine.
4. Tablou de stare per client: eligibil → acte complete → depus → selectat → contract.

**Preț de testat:** 300 EUR setup plus 75 EUR per contract semnat din campanie.

**Calcul:**
- bugetul de 400 mil. lei / 15.000 lei înseamnă ~26.700 de granturi la ~300.000 de prosumatori;
- per instalator cu 300 de clienți: ~60 de cereri, ~16 selectate, deci ~1.500 EUR;
- **~7 instalatori pentru 10.000 EUR.**
- Listă de contact: instalatorii validați AFM sunt publici și îi poți suna.

**Riscuri:**
- programele AFM se amână des (Casa Verde Fotovoltaice a fost suspendată în iulie 2025);
- e un val, nu un abonament;
- instalatorii aglomerați pot zice „nu am nevoie de clienți”. Atunci vinzi doar partea de acte și dosare.

### 3. „Rămân”: pentru angajatorii de muncitori străini (Bihor)

**Ce vinzi, într-o frază:** „Un asistent pe WhatsApp care le răspunde muncitorilor în limba lor și un puls lunar care îți spune cine vrea să plece, înainte să plece.”

**De ce acum:**
- 148.000 de muncitori (+48% într-un an), ~1/3 pleacă înainte de finalul contractului;
- limba e problema nr. 1 pentru 28% dintre ei;
- WorkinRomania acoperă actele, **nu** comunicarea;
- nu am găsit un serviciu românesc care să facă asta.

**Ce faci concret:**
1. Întrebările frecvente (fluturaș de salariu, cazare, medic, acte, ture) traduse în nepaleză, hindi, bengali, vietnameză și puse într-un asistent AI pe WhatsApp.
2. Sondaj anonim lunar de 3 întrebări în limba lor, cu alertă către HR când scorul scade.
3. Pachet de bun venit tradus.
4. **Site:** pagini în limba lor plus o pagină „lucrează la noi” pentru recrutare.

**Preț de testat:** 400 EUR setup plus 4 EUR/muncitor/lună, minimum 120 EUR/lună.
- Exemplu: un angajator cu 40 de muncitori plătește 160 EUR/lună.
- Dacă ține 2 oameni în plus pe an, serviciul se plătește singur. Costul de înlocuire a unui muncitor e o **estimare a mea**, de verificat cu angajatorii.

**Riscuri:**
- mulți pleacă pentru salariu, iar comunicarea nu repară diferența de salariu;
- legislația se mișcă (OUG 32/2026, modificată de Senat);
- angajatorii mari au HR propriu, deci ținta sunt firmele de 20–150 de angajați: hoteluri din Felix, construcții, alimentar, curierat.

### 4. „Rezervări directe”: pentru cazări din Oradea și Felix (mai slab)

- **Ce vinzi:** site cu motor de rezervări, Google Hotels (linkuri gratuite), mesaje automate pentru oaspeți și program pentru oaspeții care revin; plătești 5% din rezervările directe în loc de 15–18% la Booking.
- **Pentru:** supraofertă, gazdele simt durerea acum, iar paritatea a dispărut, deci prețul direct poate fi mai mic.
- **Contra:** bugete mici, multe motoare de rezervări existente, rezultatele vin încet.

### 5. „Sezonul de anvelope”: pentru service-uri auto (cel mai slab)

- **Ce vinzi:** remindere pentru ITP, revizie și schimbul de anvelope din aprilie și noiembrie, plus programare online și recenzii.
- **Contra:** 90% sunt micro și plătesc puțin; RevMy face deja programări.

---

## Cum alegi în 2 săptămâni (test, nu plan)

1. **Clinici:** 10 vizite în Oradea, pe jos. Întrebarea-cheie: „Câte planuri prezentate anul ăsta nu s-au început?” Semnal bun: 3 din 10 nu știu numărul și vor să-l afle.
2. **Instalatori:** 10 telefoane la instalatori validați din Bihor, Cluj și Arad. Întrebarea: „Câți clienți vechi aveți și cine îi anunță de Casa Verde Baterii?” Semnal bun: 2 vor campania.
3. **Muncitori străini:** 5 discuții cu angajatori (hoteluri din Felix, construcții). Întrebarea: „Câți din muncitorii aduși anul trecut au plecat înainte de termen?” Semnal bun: răspunsul e peste 20% și le pasă.

Alegi industria unde iese primul „da, cât costă?”. Pilot plătit: setup redus la jumătate, cu garanția de mai sus.

**Ce rămâne din sesiunile anterioare:** experiența din proiectul ILLUSTRUS și Busola nu se pierd. Tabloul de stare din APEX și fluxurile n8n sunt aceleași piese, folosite acum ca unelte interne ale serviciului, nu ca produs vândut.

---

## Surse

- Capital, înmatriculări 2025: https://www.capital.ro/inmatricularile-de-firme-au-crescut-cu-aproape-23-in-2025-peste-153-000-de-noi-entitati-majoritatea-srl-uri.html
- StartupCafe, radiografia firmelor (top domenii): https://startupcafe.ro/radiografia-firmelor-din-romania-peste-1-milion-activeaza-in-prezent-104239
- ZF, sectoarele care au condus creșterea: https://www.zf.ro/analiza-de-luni/analiza-luni-au-sectoarele-au-condus-cresterea-economiei-ultimii-ani-23163755
- Romania Insider, stomatologie și turism dentar: https://romania-insider.com/dental-tourism-and-increasing-domestic-demand-to-fuel-growth-for-romanian-dental-services
- Business Forum, Life Group +20% în decembrie: https://www.businessforum.ro/industry/20260108/life-group-sees-20-surge-in-dental-visits-in-december-2724
- Evenimentul Zilei, turism dentar: https://evz.ro/calitate-europeana-costuri-mai-mici-romania-pe-harta-turismului-dentar.html
- Henry Schein One, tratamente neprogramate: https://www.henryscheinone.com/insights/blogs/average-providers-are-losing-hundreds-of-thousands-in-unscheduled-treatment/
- Jarvis Analytics, unscheduled treatment: https://www.jarvisanalytics.com/blog/unscheduled-treatment
- Zarina CRM, soft cabinet stomatologic: https://www.zarinacrm.ro/soft-crm-pentru-cabinet-stomatologic/
- Forbes, medicină estetică: https://www.forbes.ro/medicina-estetica-salt-de-proportii-496800
- Revista Biz, Skinmed 2025: https://www.revistabiz.ro/skinmed-clinic-inchide-anul-2025-cu-o-crestere-a-cifrei-de-afaceri-de-20-si-ajunge-la-2-2-mil-euro/
- Economica, prosumatori record: https://www.economica.net/?p=876723
- Financiarul, Casa Verde Baterii 400 mil. lei: https://financiarul.ro/economie/programul-casa-verde-baterii-are-buget-de-400-de-milioane-de-lei/
- Economedia, Casa Verde Baterii 2026: https://economedia.ro/prosumatorii-cer-sa-fie-consultati-inainte-de-lansarea-programului-casa-verde-baterii-2026.html
- Economica, noua lege a prosumatorilor: https://www.economica.net/noua-lege-a-prosumatorilor-a-fost-promulgata-care-sunt-schimbarile_962072.html
- Agerpres, compensarea până în 2030: https://agerpres.ro/ots/compensarea-energiei-pentru-prosumatori-se-modifica-ce-urmeaza-pana-in-2030--660492
- Antena 3, contingent 2026: https://www.antena3.ro/actualitate/guvernul-a-aprobat-contingentul-de-muncitori-straini-cati-vin-in-romania-in-2026-si-pentru-ce-meserii-candideaza-771864
- TVR Info, o treime pleacă înainte de termen: https://tvrinfo.ro/muncitorii-din-asia-in-calculele-de-baza-ale-patronilor-romani-pentru-afacerile-de-anul-acesta-caracterul-sezonier-al-slujbelor-din-turism-o-problema/
- Economedia, profilul muncitorilor străini: https://economedia.ro/profilul-muncitorilor-straini-care-lucreaza-in-romania-varsta-medie-este-de-27-de-ani-majoritatea-vin-din-india-vietnam-si-bangladesh-doar-7-planuiesc-sa-se-stabileasca-definitiv-in-tara-noastra.html
- Romania Insider, WorkinRomania funcțional: https://www.romania-insider.com/platform-foreign-workers-coming-romania-and-running-aug-2026
- Spotmedia, garanția de 75.000 EUR: https://spotmedia.ro/stiri/social/schimbare-majora-pentru-firmele-care-aduc-muncitori-straini-garantia-de-75-000-de-euro-ar-putea-elimina-majoritatea-agentiilor
- Visit Oradea, sinteza 2025: https://www.visitoradea.com/files/shares/Sinteza_raport_de_activitate_2025_-_conf_presa_17_02_26.pdf
- Economedia, Booking și hotelurile din România: https://economedia.ro/circa-110-operatori-din-romania-s-au-inscris-in-procesul-colectiv-la-nivel-european-portalului-de-turism-pentru-a-solicita-despagubiri-pentru-ani-de-fixare-fortata-a-preturilorimpotriva-booking.html
- StartupCafe, service-uri auto: https://startupcafe.ro/service-auto-reglementare-htm-14578
- Profit.ro, plăți Uber/Bolt blocate: https://profit.ro/taxe-si-consultanta/plati-uber-si-bolt-blocate-reactie-rapida-a-soferilor-trec-de-la-firme-pe-pfa-dupa-anuntul-profit-ro-22194381
- StartupCafe, construcții 2026: https://startupcafe.ro/piata-constructiilor-incetineste-62-dintre-firme-vad-scaderi-ale-lucrarilor-iar-lipsa-personalului-devine-principala-problema-din-industrie-studiu-97945
- Business Forum, AI în firme (Eurostat): https://businessforum.ro/industry/20251211/romanian-companies-fall-behind-on-ai-usage-says-eurostat-2662
- Permis de antreprenor, EAA pentru e-commerce: https://permisdeantreprenor.ro/european-accessibility-act-eaa-pentru-site-uri-e-commerce/
