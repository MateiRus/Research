# Sesiune laterală 3: Random Stimulus (de Bono, *Lateral Thinking*, 1970)

**Ruta `lateral`:** simptomul e „ideile ies toate la fel” — de trei ori la rând, orice variantă s-a întors la „site + ceva”. Fondatorul vrea un **produs**, nu servicii de site, atât de bun încât să poată aborda firme direct. Tehnica: **random-stimulus**.

**Ținta:** un produs livrat ca aplicație web, construibil de o persoană cu Oracle APEX / PL/SQL / n8n / Python / LLM în 30–40 de ore, pe care o firmă din Bihor sau București îl cumpără la prima demonstrație. Constrângeri: 10–12 h/săptămână, fără e-mail rece, demonstrabil pe datele clientului, încredere minimă cerută (testul cu consultanți a arătat că „un part-time cu dosarele mele” e refuzat de 14 din 20), preț 300–1.500 EUR sau abonament mic.

**De ce funcționează tehnica:** în spațiul problemei, asocierile trec mereu prin aceleași rute („site”, „formular”, „reminder”). Un obiect din afară are o proprietate structurală pe care ținta nu o are încă — măsoară poziția, repară vizibil, traduce în timp real — și nepotrivirea aceea forțează o traiectorie nouă prin aceeași țintă. Primele stimule sunt de obicei slabe; de aceea se trage un lot, nu unul singur.

**Lotul** (12 stimule, 12 categorii distincte, 7 concrete, 5 abstracte, fără două din aceeași categorie alăturate).

---

### 🧭 Sextantul — Tools & Machines [concrete]
Proprietăți: măsoară poziția fără GPS; folosește un reper fix (o stea); răspunde la „unde sunt față de unde trebuia să fiu”; precizia vine din repetarea măsurătorii.
→ Un produs care spune unui beneficiar de grant **unde se află față de planul de afaceri aprobat**. Planul are repere fixe: venituri de minimum 30% din prima tranșă până la cererea tranșei a doua, locuri de muncă, termene. Lunar, produsul citește facturile emise de beneficiar direct din SPV / e-Factura (API ANAF cu OAuth, acces doar de citire, revocabil oricând din SPV) și calculează: „ești la 12% din prag; la ritmul ultimelor 3 luni atingi 30% în luna 19, termenul e luna 14; îți lipsesc 7.400 EUR facturați”. Alertă către beneficiar și consultant când traiectoria ratează ținta.
Testul de redundanță: știam de pragul de 30%, dar „poziție față de plan, calculată automat din facturi, cu dată estimată de atingere” nu apăruse în nicio sesiune. **Păstrat — cea mai puternică lovitură a lotului.**

### 🐝 Albina cercetaș care se întoarce — Insects & Microbes [concrete]
Proprietăți: caută departe, se întoarce, dansează direcția și distanța; doar sursele bune primesc multe albine.
→ Un cercetaș de *clienți*, nu de apeluri: firme nou-înființate în Bihor, cu CAEN și vechime eligibile pentru un apel deschis, livrate consultantului ca listă. → A doua încercare: dansul = dovada — nimic nou.
**Slab, păstrat cu rezerve.** Consultanții din test au spus „nu am nevoie de mai mulți clienți, am nevoie de mai puțini proști”; în plus, contactarea lor intră sub regulile de prospectare.

### 📚 Marginalia — Stories & Books [concrete]
Proprietăți: note pe marginea unui text; se acumulează de la cititor la cititor; textul rămâne, comentariul crește.
→ **Ghidul adnotat și „ce s-a schimbat”**: ghidurile au 100+ pagini și apar în versiuni (Rev. 2, Rev. 3, corrigenda). Produsul compară automat două versiuni ale aceluiași ghid la nivel de paragraf, evidențiază ce s-a schimbat și leagă de fiecare paragraf notele firmei („la apelul trecut, evaluatorul a cerut aici X”).
Redundanță: „radarul” urmărea apariția modificărilor, nu conținutul lor. **Păstrat, mediu** — există comparatoare generice de PDF, dar nu pe structura ghidurilor și cu memoria firmei.

### ⏳ Trimestrul fiscal — Time & Cycles [abstract]
Proprietăți: ritm periodic; totul se resetează; raportare obligatorie.
→ Rapoarte periodice generate pentru beneficiari — repetă Sextantul. → A doua încercare: plată pe trimestru — e preț, nu produs.
**Abandonat.** Ambele încercări au repetat ținta sau o idee deja găsită.

### 🏛 Sala de așteptare a spitalului — Buildings & Spaces [concrete]
Proprietăți: triaj după urgență; bilet cu număr; ecran care arată cine urmează; oamenii întreabă mereu „cât mai durează?”.
→ Prima încercare: triajul cererilor — avem deja calificarea cererilor. Redundant. → A doua: **ecranul „unde e dosarul meu”** — o pagină de urmărire pentru clientul consultantului, ca la curier: depus → în evaluare → selectat → contract → cerere de plată 1 → … , cu pasul următor și ce mai lipsește. Clienții nu mai sună „ce mai face proiectul meu?”, consultantul arată profesionist, iar produsul nu ține documente, doar stări.
**Păstrat** — ușor de construit, încredere minimă cerută, demonstrabil în 2 minute.

### 🎨 Kintsugi — Art & Craft [concrete]
Proprietăți: repari vasul spart cu aur; ruptura devine partea cea mai vizibilă; reparația adaugă valoare.
→ Proiectele pierd puncte la evaluare din motive previzibile. **Simulatorul de punctaj**: grila de punctaj a fiecărui apel e publică și în mare parte deterministă (praguri ca 80/40 de puncte la DR-14). Consultantul introduce datele proiectului și vede scorul estimat, criteriile unde pierde puncte și ce ar trebui schimbat pentru a le recupera — „reparația vizibilă” înainte de depunere. Criteriile se extrag din ghid cu LLM și se validează de om, apoi rulează ca reguli PL/SQL.
Redundanță: verificarea eligibilității cu AI a fost respinsă ca riscantă; punctajul pe reguli publice e alt lucru. **Păstrat** — dar fiecare apel are grila lui, deci întreținere per apel.

### 👤 Interpretul simultan — People & Roles [concrete]
Proprietăți: traduce în timp real între două părți care nu vorbesc aceeași limbă; nimeni nu observă interpretul când e bun.
→ Prima încercare: scrisorile AFIR traduse pe înțelesul fermierului — util, dar mic. → A doua: **traducerea dintre limba contabilității și limba grantului**: din facturile beneficiarului (tot SPV/e-Factura) produsul asociază fiecare factură cu o linie din bugetul proiectului și generează anexa cererii de plată și verificările ei (cheltuieli eligibile, plafoane, TVA). Consultantul pierde azi ore la fiecare cerere de plată.
**Păstrat — al doilea ca forță.** Mai greu de construit decât Sextantul (machete diferite pe program), dar folosește aceeași sursă de date.

### 🌊 Umbra ploii — Water & Weather [abstract]
Proprietăți: muntele oprește ploaia; o parte e verde, cealaltă uscată; bariera, nu lipsa apei, face seceta.
→ Banii nu ajung în comunele unde nu ajunge niciun consultant. Cumpărătorul nu e consultantul, ci **GAL-ul**: are obligația să anime teritoriul și să-și raporteze indicatorii strategiei, iar costurile de funcționare și animare sunt finanțate. Produs: harta firmelor din teritoriu, pe CAEN eligibile pentru fiecare intervenție, plus tabloul indicatorilor proiectelor în implementare (combinat cu Sextantul, la nivel de portofoliu GAL).
Redundanță: GAL-ul ca *client* nu apăruse niciodată, doar ca *canal*. **Păstrat, de verificat** — platforma gal.afir.ro acoperă deja o parte din fluxul GAL-urilor.

### 🎲 Punctul de salvare din joc — Games & Sports [abstract]
Proprietăți: progresul se salvează; reiei de unde ai rămas; nu refaci nivelul.
→ Dosarul permanent al clientului: datele și documentele se refolosesc la apelul următor, iar documentele cu valabilitate (certificat constatator, certificat fiscal) au data de expirare urmărită.
Redundanță: e Dosar Complet cu un câmp de expirare. **Variantă, nu idee nouă** — se adaugă la kitul de documente.

### 🛏 Cheia de sub preș — Household Objects [concrete]
Proprietăți: acces ascuns pentru cei de încredere; comod și nesigur.
→ Consultanții țin parolele și certificatele clienților pentru SPV, MySMIS, AFIR. Un seif de acces? → A doua încercare: acces de urgență — același lucru.
**Abandonat.** E un manager de parole, care există, și aduce răspundere de securitate pe care o persoană part-time nu o poate purta.

### 🐾 Ecolocația liliacului — Animals & Creatures [abstract]
Proprietăți: trimite un semnal, ascultă ecoul, își face harta în întuneric.
→ Ping-uri lunare automate pe WhatsApp către beneficiarii în implementare („Ai emis facturi luna asta? Ai angajat? Ai primit vreo notificare de la AFIR?”); răspunsurile alimentează un tablou de risc pe portofoliul consultantului.
Redundanță: e Sextantul cu altă sursă de date. **Variantă** — devine modul de pornire al Sextantului pentru beneficiarii care nu dau acces la SPV.

### 🎭 Calendarul de Advent — Rituals & Ceremonies [concrete]
Proprietăți: o fereastră pe zi; numărătoare inversă; o mică recompensă.
→ Calendarul obligațiilor proiectului, câte o fereastră pe lună — e calendarul de termene, deja respins ca marfă. → A doua: „un lucru pe zi” pentru beneficiarii noi — curs, nu produs.
**Abandonat.**

---

## Meta-tiparul

**Loviturile.** Toate cele puternice — Sextantul, Interpretul, Sala de așteptare, Ecolocația, Umbra ploii — s-au mutat din faza de **depunere** a proiectului, unde concurează toți consultanții și unde consultantul își vinde expertiza, în faza de **implementare de după contract**, care durează 3–5 ani. Acolo lucrul se repetă lunar, datele sunt obiective (facturi, angajări, termene) și pierderea e mare și numărabilă: tranșa a doua neplătită sau sprijinul recuperat. Schemele din jur arată același mecanism: tinerii fermieri cu prag de 20% din prima tranșă și recuperare integrală la neîndeplinire, Diaspora ReSTART cu 30%, sM 6.2 cu 30%, Start-Up Nation cu recuperare plus dobândă [VERIFICAT – sursă secundară, vezi mai jos].

**Abandonările.** Toate trei (trimestrul, preșul, calendarul de Advent) au murit în același fel: au retrasat axa „calendar / reminder / acces”. Axa aceasta e epuizată și e marfă. Axa care lipsea din țintă era **banii expuși**: un produs care pune o sumă în euro lângă un risc („7.400 EUR lipsă, 14 luni rămase”) se vinde altfel decât un produs care trimite remindere.

**A doua observație.** Fondatorul e el însuși beneficiar în implementare, cu exact pragul de 30%. Sextantul îl poate construi întâi pentru propriul proiect. Asta răspunde direct obiecției dominante din teste („nimeni nu îl folosește încă”): îl folosește el, pe banii lui.

## Clasament onest

1. **Sextantul — monitorul de implementare față de planul de afaceri.** Cea mai mare pierdere evitată, date obiective, acces doar de citire și revocabil, demonstrabil pe proiectul propriu și apoi pe un client real al consultantului. Slăbiciune: pragurile și reperele diferă pe program și pe GAL, deci fiecare proiect se configurează din contract.
2. **Interpretul — cererea de plată din facturi.** Valoare mare și repetată, aceeași sursă de date ca Sextantul; mai greu de construit și de întreținut pe programe diferite. Natural ca a doua treaptă a aceluiași produs.
3. **Sala de așteptare — „unde e dosarul meu”.** Cel mai ușor de construit și de vândut, încredere aproape zero, dar valoare mai mică; bun ca modul gratuit sau ieftin care deschide ușa.
4. **Kintsugi — simulatorul de punctaj.** Puternic înainte de depunere, dar întreținere per apel și concurență din calculatoarele consultanților și platforme ca 47Funds.
5. **Umbra ploii — GAL-ul ca client.** Cumpărător nou, cu buget de funcționare; neverificat.

Slabe: albina cercetaș (lead-uri pe care consultanții nu le vor). Variante: punctul de salvare (în Dosar Complet), ecolocația (în Sextant). Abandonate, vizibil: trimestrul fiscal, cheia de sub preș, calendarul de Advent.

Mișcări următoare, la alegerea fondatorului: un al doilea lot de stimule, coborâre pe Sextant, schimbarea tehnicii, sau oprire.

## Surse folosite pentru verificări
- Praguri și recuperare în scheme apropiate (tineri fermieri 20% și recuperare, Diaspora ReSTART 30%, sM 6.2): [bzi.ro](https://www.bzi.ro/tinerii-fermieri-din-iasi-care-vor-fonduri-europene-de-maximum-50-000-de-euro-returneaza-banii-primiti-daca-nu-respecta-obiectivele-planului-de-afaceri-3993246), [fiscalitatea.ro](https://www.fiscalitatea.ro/finanteaza-ti-start-up-ul-in-cadrul-proiectului-diaspora-restart-18093/), [economica.net](https://www.economica.net/afir-finanteaza-1-893-de-proiecte-pentru-infiintarea-de-activitati-neagricole-in-zone-rurale-cu-o-valoare-de-111-3-milioane-de-euro_183740.html/amp); Start-Up Nation, recuperare cu dobândă: [alba24.ro](https://alba24.ro/start-up-nation-romania-intri-in-insolventa-statul-iti-ia-ajutorul-pe-care-ti-l-a-acordat-in-program-567404.html)
- API e-Factura / SPV cu OAuth, token 90 de zile, listarea facturilor trimise, autorizare prin firmă sau contabil: [anafpy – OAuth](https://anafpy.readthedocs.io/en/latest/anaf-reference/oauth/authentication/), [anafpy – e-Factura API](https://anafpy.readthedocs.io/en/latest/anaf-reference/efactura/api/), [ebriza – autorizare](https://intercom.help/ebriza/ro/articles/8981890-autorizare-ebriza-e-factura)
- Concurență găsită: eMIP, management de proiect pentru echipe POSDRU/POCU [alba24.ro (P)](https://alba24.ro/emip-solutie-completa-de-gestionare-si-monitorizare-a-proiectelor-si-a-planurilor-de-afaceri-finantate-prin-fonduri-europene-p-906891.html); 47Funds, analiză automată de eligibilitate [the47network](https://app.dynamics.the47network.com/); grile de punctaj publice [startupcafe.ro](https://startupcafe.ro/fonduri-europene-grile-punctaj-afaceri-neagricole-tineri-fermieri-procesare-htm-16415)
