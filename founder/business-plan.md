# ILLUSTRUS — site-uri și automatizări pentru consultanți în fonduri europene · Business plan

**Verdict: Not yet**

- ✓ Each PRO contract (setup + 12 months) earns $3588.00 before fixed costs (88% contribution).
- ✓ Year 1 operating profit: $9,493.
- ✓ Break-even is 1 PRO contract (setup + 12 months)s a day against a capacity of 0.0222.
- ✗ 2 of 20 simulated buyers buy (10%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $4080.00 a PRO contract (setup + 12 months) |
| Profit margin at plan | 82% per PRO contract (setup + 12 months) |
| Break-even | 1 PRO contract (setup + 12 months)s a day |
| Year 1 operating profit | $9,493 |
| Startup spend | $300 |
| Cash needed before it pays for itself | $615 |
| Startup money earned back | month 4 |
| Buyer panel | 2 buy · 18 pass |

## The idea

- What it is: A one-person web-services firm in Romania that builds professional websites for consultants in European funds and business consultants, with two automations attached: lead qualification (form → structured request → AI pre-check of eligibility → notification → booking) and client document collection with reminders. A monitoring "radar" for funding calls is offered only as a paid 30-day pilot.
- Who it is for: Consulting firms (CAEN 7022/7020) in Bihor county (Oradea) and Bucharest, 1–15 people, that write and manage EU/national grant projects for SMEs and farmers. Decision-maker: the owner/managing consultant.
- What it sells, at what price (all excl. VAT): START = website (6–8 pages, texts written from interviews, FAQ, structured data, Google Business, lead form) at 1,200 EUR + 60 EUR/month (hosting, updates, backup, 2 h support). PRO = START + the two automations at 2,400 EUR + 140 EUR/month (4 h/month). First two clients get −20% (960 / 1,920 EUR) in exchange for a named case study and two introductions. RADAR pilot: 1,100 EUR for 30 days, one consultant, 3 official sources, 5 client profiles.
- Where and how: Founder lives in Bucharest, is from Bihor, visits Oradea 1–2 times a month. Sales by phone calls to firms, in-person meetings, events (CFO Conference Oradea, GoTech World Bucharest), referrals from the founder's own grant consultant and GAL network, and the public AFIR list of consulting firms. Delivery remote, kickoff in person when possible. No cold e-mail (Romanian law 506/2004).
- Budget and constraints: 10–12 hours per week (founder is a 2nd-year student and a junior Oracle APEX/PL/SQL developer with a day job). Skills: SQL/PLSQL/APEX, n8n, Python, HTML/CSS/JS, WordPress, LLM APIs. Infrastructure almost free (Oracle Always Free, self-hosted n8n, ~40 EUR/month). Hard objective: 10,000 EUR of recognised web-service revenue within 3 years (grant obligation), target 12–15 months. Local market context: Oradea agencies publish website prices of 100–990 EUR; national agencies 990–2,490 EUR; automation agencies 500–1,500 EUR + 50–150 EUR/month. Bihor has ~400–470 consulting firms (60–70% in Oradea); Bucharest has thousands.

## Summary

**Ce este.** ILLUSTRUS vinde consultanților în fonduri europene din Bihor și București un sistem care le aduce documentele clienților la timp („Dosar Complet”: link personal pe WhatsApp, listă de lipsuri, remindere automate), cu site-ul și pre-check-ul de eligibilitate ca add-on-uri și radarul de finanțări parcat. Cumpărătorul e proprietarul unei firme de consultanță cu 1–15 oameni.

**Verdictul calculat: Not yet.** Cele trei verificări pe cifre trec (contribuție 3.588 EUR pe contract PRO, 88%; profit operațional anul 1 ~9.500 EUR la 3 contracte; pragul de rentabilitate 0,03 contracte/lună, sub capacitate). Verificarea de cerere pică: **oferta inițială 0 din 20; oferta refăcută 2 din 20 (10%), sub bara de 25%.** Cumpărătorii sunt simulați; rata de cumpărare e o limită superioară, nu o predicție.

**Unde board-ul și panelul sunt de acord.** (1) Site-ul nu e produsul; nimeni nu l-a vrut, nici la 1.200, nici la pachet. (2) Durerea reală e colectarea documentelor; 17 din 20 au numit-o. (3) Fără un client real care poate fi sunat, nu se semnează nimic: 14 din 20 au refuzat pe „încredere”, nu pe preț, chiar la 900 EUR cu garanție și clauză de continuitate. (4) Verificarea AI a eligibilității e un risc, nu un argument. **Unde nu sunt de acord:** lentila Monopoly vrea radarul vândut devreme ca singur activ proprietar; panelul nu l-a cerut deloc, iar lentilele Offers și Product îl parchează. Panelul a mai arătat ceva ce board-ul nu a văzut: pentru firmele mici (5–15 clienți/an) problema nu e remindere, ci documente care nu există încă, deci produsul e pentru firme cu 20+ clienți activi.

**Cel mai mare risc:** fondatorul part-time fără referință. Nu se rezolvă cu preț, garanții sau clauze (le-am testat, au mutat 0% → 10%); se rezolvă doar cu **un pilot real, finalizat, la un consultant care acceptă să fie sunat**, plus o persoană de rezervă cunoscută de client înainte de semnare. Ce se face: pilotul la consultantul fondatorului, 60 de zile, măsurat (zile între cerere și dosar complet, înainte vs după), apoi vânzarea.

**Ce îi trebuie fondatorului ca să înceapă:** ~615 EUR numerar (CFO) și 20–25 h pentru pilotul de documente; nu un site, nu un radar. Primul test real: 10 apeluri telefonice la firme cu 20+ clienți (lista AFIR, filtru Bihor), cu întrebarea „câte zile trec de la cerere la dosar complet?”.

**Un singur lucru săptămâna asta:** semnezi pilotul „Dosar Complet” cu consultantul tău, cu măsurătoarea „înainte” luată acum, și pui în contract numele persoanei de rezervă.

Cifrele sunt proiecții din inputurile fondatorului; panelul e simulat. Nu e consultanță financiară, juridică sau fiscală.

## What the board said

**Vot: 3 × FUND IF. Scor mediu: 4,3 / 10** (Offers 5, Monopoly 4, Product 4).

### Riscurile ridicate de mai mulți membri (primele)

1. **Produsul plătit e o marfă.** Toate cele trei lentile: START (site 1.200 EUR) nu e distinct de un site de 389–990 EUR din Oradea în primele 5 minute ale cumpărătorului; PRO e „site + n8n” într-o piață cu 300–1.500 EUR/proiect. Nimic nu e de 10 ori mai bun; e doar mai bine scris.
2. **Zero dovadă, zero interviuri.** Offers + Monopoly + Product: cele trei dureri (cereri neeligibile, documente întârziate, apeluri aflate târziu) sunt ipoteze. Fără portofoliu, fără client, fără set de test pentru verificarea de eligibilitate.
3. **Trei produse, o persoană, 10–12 h/săptămână.** Offers + Product: 20 h/lună rămase la 5 clienți; trei promisiuni de suport diferite trec prin același calendar (sesiune, drumuri, job).
4. **Radarul concurează cu gratuitul.** Offers + Monopoly: informația e gratuită (portaluri, newslettere cu 16.000 abonați, buletine PDF); valoarea posibilă e doar potrivirea pe profil și urmărirea modificărilor, neprobate.
5. **Verificarea AI a eligibilității e cel mai riscant moment** (Product): un „neeligibil” greșit pierde un onorariu de succes și încrederea; nu există cifră de acuratețe.

### Condițiile, unite (lista pe care restul pachetului o bifează)

- [ ] 10 interviuri cu proprietari de firme de consultanță (≥ 6 în Bihor) **înainte de orice construcție**, cu o durere confirmată în ore sau onorarii pierdute. → panel + interviuri reale
- [ ] **Un singur produs principal** în primele 12 luni; lentila Product și Offers aleg automatizările (colectare documente ± pre-check), site-ul devine bonus/add-on, radarul stă parcat până îl cere un client PRO. (Monopoly ar vrea radarul vândut devreme — dezacord reținut.)
- [ ] Verificare de eligibilitate **măsurată** pe 50 de cereri reale ale unui consultant, cu cifră de acuratețe, și un traseu pentru „neeligibil” care nu pierde niciodată tăcut un prospect. → de făcut cu primul client-pilot
- [ ] O garanție legată de rezultat pe automatizare (ex. reducerea timpului de urmărit documente, altfel se returnează instalarea). → founder-offer
- [ ] Primii 2 clienți semnați și documentați ca dovadă **înainte** de a cere prețul întreg altcuiva.
- [ ] Confirmare scrisă de la finanțator pe ce venituri contează (în afara scopului evaluării de față, la cererea fondatorului).
- [ ] O „pană”: doar consultanți din Bihor 12 luni, cu țintă de cotă (ex. 10 din 450) înainte de București.
- [ ] Test de copiere: ce îi trebuie unui concurent să reproducă radarul; dacă datele de profil acumulate într-un an nu sunt activul, Monopoly votează PASS.
- [ ] Plan scris de acoperire a suportului în sesiune și în drumuri.

### Dezacorduri păstrate

- **Ce se vinde primul.** Offers și Product: automatizarea de documente (durere concretă, fără concurent local). Monopoly: radarul, singurul lucru cu șansă de a deveni proprietar. Chair-ul reține ambele ca ipoteze de testat pe panel.
- **Ce e site-ul.** Pentru toți, „ușa, nu afacerea”; dar Offers îl vede ca bonus în stivă, Product ca add-on opțional, Monopoly ca irelevant pentru poziție.

### Cea mai bună versiune a acestei afaceri, văzută de board

Nu „site-uri pentru consultanți”, ci **„sistemul care îi aduce consultantului documentele clienților la timp”**: colectarea de documente cu listă de lipsuri și remindere, vândută singură, instalată pe conturile clientului (continuitate), cu o garanție pe ore economisite, la un preț pe care un consultant îl plătește dintr-un singur onorariu. Site-ul e un add-on pentru cine îl vrea; radarul e un abonament care se adaugă abia când există 5 clienți care deja plătesc și cer „spune-mi tu când apare apelul”. Asta diferă de ce a prezentat fondatorul: site-ul iese din față.

## The buyer panel

**2 buy · 18 pass** (10% buy) out of 20 simulated buyers. Seed 7, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Established firm, 8-15 people, 50+ clients, several programmes | 3 | 67%  (thin) |
| Small consulting firm, 3-8 people, 20-50 active clients | 8 | 0% |
| Solo consultant / PFA-style firm, 1-2 people, 5-15 clients a year | 9 | 0% |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Tech-curious | 2 | 50%  (thin) |
| Drowning in admin | 4 | 25%  (thin) |
| Has a cheap site already | 4 | 0%  (thin) |
| Skeptical of newcomers | 3 | 0%  (thin) |
| Price-anchored locally | 3 | 0%  (thin) |
| Referral-only | 4 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $130,000 and up | 7 | 29%  (thin) |
| $64,000 to $130,000 | 7 | 0%  (thin) |
| under $64,000 | 6 | 0%  (thin) |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| trust | 14 | "The problem is real, my people lose whole days chasing farmers for bilant and extras CF, and 900 plus 50 a month is nothing against what we bill. But I am not putting the documents of 50 clients into a tool built nights and weekends by someone whose first client has not even finished the pilot yet." (P001) · "The problem is real, I chase farmers for CUI copies and bank statements every deadline season, and the handover and backup-person clauses are better than what the agency that vanished on me ever offered. But there is not one consultant in Romania I can phone today who has used it; the only reference exists after a pilot that has not finished, and the man building it does this on evenings next to a day job." (P002) |
| need | 3 | "I have 5 to 15 clients a year and I already chase their papers on WhatsApp myself; it is annoying, but not 900 EUR plus 600 a year annoying. For my volume this is a nice tool for a firm twice my size, not for me." (P006) · "I have ten, maybe twelve clients a year and I already chase their papers on WhatsApp myself; 900 EUR plus 50 a month to automate something I do in a few hours a month is money I would rather keep. The part that actually hurts me is not collecting files, it is that my whole pipeline is a stack of business cards from conferences like this one." (P016) |
| price | 1 | "900 EUR is what a whole website costs here in Oradea, and this is a WhatsApp link with reminders for the ten or so clients I handle a year; chasing documents is annoying but I already do it from my phone and a shared Drive folder for free. Out of 32,000 EUR revenue I am not putting 900 plus 600 a year into something I can mostly imitate by hand." (P008) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 2 | "I lose my evenings chasing balance sheets and APIA extracts from 50-odd clients, and 900 EUR plus 50 a month is less than one junior's week; with the setup refunded if the file-completion time does not drop, and no 12-month lock-in, I can afford to test it on one programme's clients." (P004) · "I spent half of today driving 120 km round trip for one missing paper, and my people spend hours every week on WhatsApp begging clients for documents; 900 plus 50 a month is less than one of those days costs me, and if the time to a complete file does not drop in 60 days I get the setup back. This is not another funding radar, which I would have ignored; it is the chasing I actually hate." (P007) |

### What would flip a no

- A phone call with the Bihor consultant after the 60-day pilot saying it worked, and the name and number of the backup person written into the contract before I sign.
- A phone call with the Bihor consultant after the 60 days, with his real before/after numbers on days-to-complete-file, and him telling me who answered when something broke.
- A phone call with the Bihor consultant after his 60 days, telling me his farmer and small-SME clients actually used the link and his time to a complete file really dropped.
- A phone call with the Bihor consultant after the pilot, with real before/after numbers from their own files, and ideally a second consultant I did not hear about from the founder.
- If the Bihor consultant tells me on the phone after the 60 days that it really cut the chasing to a fraction, and the setup comes down to around 400 EUR, I would try it for one submission season.
- Setup at around 400-500 EUR, or a per-client price instead of a flat fee, after I have called the Bihor consultant and heard that the before-and-after measurement actually held up.
- A phone call with the Bihor consultant after the 60-day pilot, where he tells me the reminders actually got documents out of his clients without him chasing, and shows me his monthly report.
- A 15-minute phone call with the Bihor consultant after his 60 days, saying the chasing actually dropped and his clients used the WhatsApp link without complaints; then I would sign the next day.
- A phone call with the Bihor grant consultant, after his pilot, telling me his farmer clients actually used the link and his chasing time dropped; then I would try it for one submission round.
- A 15-minute phone call with the Bihor consultant after his 60 days, telling me his farmers actually used the link and he stopped chasing; then I take the 720 slot the same week.
- A phone call with the Bihor consultant after his 60 days are up, with his before-and-after numbers in hand, and the name and a conversation with the backup person before I sign anything.
- A phone call with the Bihor consultant after the 60-day pilot saying the links actually worked with farmer clients and the founder picked up during deadline week; then I would try it on a batch of my own clients.

Buyers say they would buy **1.0 times** in the first month on average.

20 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

### 1. Curba Van Westendorp (20 de răspunsuri, preț de instalare, EUR fără TVA)

| punct | preț | sens |
|---|---:|---|
| PMC | ~790 | sub acest preț, prea mulți cred că e prea ieftin ca să fie bun |
| OPP | ~800 | cea mai mică rezistență |
| IPP | ~1.500 | la fel de mulți spun „chilipir” ca „scump” |
| PME | ~2.400 | peste acest preț, prea mulți nu cumpără deloc |

Interval acceptabil: **~790 – ~2.400 EUR** instalare. Mediane: prea ieftin 500, chilipir 1.000, scump 1.800, prea scump 2.500. Prețul PRO de 2.400 e **exact pe marginea de sus**; START la 1.200 e în zona confortabilă; 960 (pilot) e lângă OPP.

Nuanță din răspunsuri: firmele mari (venituri > 300k) au dat praguri de 3.500–7.000 EUR, firmele mici 2.200–2.400. Prețul nu e bariera la firmele mari; încrederea e.

### 2. Ce cere piața (din plan v2/v3, [VERIFICAT – sursă secundară])

Oradea: 389–990 EUR site; național „Business” 990–1.690 EUR; automatizări 300–1.500 EUR + 50–150 EUR/lună. Deci 2.400 EUR e justificabil doar dacă cumpărătorul vede automatizările ca produs, nu site-ul.

### 3. Ce dă marja (founder-cfo)

Contribuție pe contract PRO (4.080 EUR cu 12 luni): 3.588 EUR (88%). Costurile fixe sunt 105 EUR/lună; pragul de rentabilitate e 0,03 contracte/lună (tool-ul afișează „1 pe zi” din rotunjire). Prețul poate scădea cu 50% și afacerea rămâne profitabilă pe costuri externe; limita reală e **timpul fondatorului**, nu marja.

### 4. Decizia

1. **Prețul**: automatizarea de colectare documente **singură** la **900 EUR** instalare (în interiorul PMC–IPP, lângă „chilipir”) + **50 EUR/lună** (sub pragul de 60 EUR/lună numit repetat de cumpărători), **fără angajament de 12 luni** (lunar, preaviz 30 de zile). Pre-check-ul de eligibilitate: add-on **+400 EUR**, livrat doar ca „semnalare de date lipsă / criterii evidente”, cu verdictul final la consultant, după un test pe 20–50 de cereri reale ale clientului.
2. **Scara**: Bun = Documente (900 + 50/lună) · Mai bun = Documente + Pre-check (1.300 + 70/lună) · Cel mai bun = + site refăcut (2.400 + 140/lună, cu 4 h/lună). Motivul de urcare: fiecare treaptă elimină încă o oră pe săptămână.
3. **Oferta de lansare**: primii 2 clienți la 720 EUR (−20%), în schimbul studiului de caz și a două introduceri; termen 31 ianuarie 2027. Nu se mai dă reducere după.
4. **De testat cu cumpărători reali**: 900 vs 1.200 EUR instalare pentru Documente, pe două oferte trimise alternativ la cele 10 discuții din planul pe 30 de zile; și lunar vs 12 luni la același preț.
5. **Obiecțiile de preț, verbatim**: „4.080 EUR în primul an e aproape o zecime din venitul meu pentru un site care funcționează” (P006); „plătesc un preț de site-builder ca să primesc la pachet singurul lucru care mă doare” (P003); „140 EUR pe lună pentru totdeauna, plătind automatizări și ore pe care nu le folosesc” (P006).

Răspunsurile de preț vin de la cumpărători simulați: aleg ce testezi, nu dovedesc nimic.

### 5. După re-test (oferta „Dosar Complet”, 20 de cumpărători, același seed)

| punct | ofertă v1 (PRO 2.400) | ofertă v2 (Documente 900) |
|---|---:|---:|
| PMC (prea ieftin) | ~790 | ~300 |
| OPP | ~800 | ~300 |
| IPP | ~1.500 | ~500 |
| PME (prea scump) | ~2.400 | ~1.500 |

Mediane v2: prea ieftin 200, chilipir 500, scump 1.200, prea scump 2.000. **900 EUR e în interval, dar peste IPP**: pentru firmele mici (5–15 clienți/an) pragul „prea scump” coboară la 800–900, iar „aș încerca” apare la 400–500. Pentru firmele cu 50+ clienți, 900 e „nimic”. Concluzie: **preț pe volum**, nu preț unic: 500 EUR + 30/lună pentru ≤ 15 clienți finali, 900 EUR + 50/lună pentru ≤ 50, 1.500 EUR + 90/lună peste 50. De testat cu cumpărători reali, nu cu panelul.

## The offer

### Problemele cumpărătorului (din panel și board, în cuvintele lor)

Înainte de a cumpăra: (1) „un student cu job: cine răspunde la telefon peste un an?”; (2) „prețul de lansare pentru primii 2 = nimeni nu îl folosește”; (3) „4.000 EUR în primul an pentru un site care nu promite clienți”; (4) „12 luni blocat cu un om care lucrează 10 h pe săptămână”; (5) „arată-mi un consultant din România care îl folosește”; (6) „site-ul meu vechi funcționează”; (7) „toți clienții vin din recomandări”; (8) „plătesc automatizări și ore pe care nu le folosesc”.
În timpul folosirii: (9) „fermierii mei nu folosesc linkuri; aduc hârtii”; (10) „AI-ul spune greșit «neeligibil» și pierd un client”; (11) „se strică cu o zi înainte de termen și el e la job”; (12) „suport într-o zi lucrătoare e prea lent lângă un termen”; (13) „regulile apelurilor se schimbă; cine ține pre-check-ul la zi?”.
După: (14) „dacă dispare, portalul meu moare”; (15) „datele clienților mei pe un sistem al unui om”; (16) „ce primesc concret în fiecare lună pentru abonament?”.

### Soluții păstrate (valoare mare, cost mic)

| problemă | soluție | valoare 1–5 | cost 1–5 |
|---|---|---|---|
| 1, 4, 14, 15 | **Instalare pe conturile clientului** (domeniu, găzduire, n8n, stocare în contul lui) + **predare scrisă** + **persoană de rezervă numită** în contract; fără blocare: lunar, preaviz 30 zile | 5 | 2 |
| 3, 6, 7, 8 | **Fără site în ofertă.** Automatizarea de documente se vinde singură, se leagă de site-ul/WhatsApp-ul existent | 5 | 1 |
| 9 | Clientul final primește linkul **pe WhatsApp, în numele consultantului**, poate trimite și poze; consultantul vede lista de lipsuri; reminderele pleacă automat | 4 | 2 |
| 10, 13 | Pre-check-ul **nu dă verdicte**: semnalează date lipsă și criterii evidente (județ, CAEN, mărime); verdictul rămâne la consultant; **test pe 20–50 de cereri reale** înainte de activare | 4 | 2 |
| 11, 12 | Automatizările au **fallback manual** (dacă pică, linkul duce la un formular simplu + e-mail); suport **în aceeași zi lucrătoare până la 18** în săptămâna unui termen anunțat | 3 | 2 |
| 2, 5 | **Pilot la primul client cunoscut** (consultantul fondatorului) 60 de zile, apoi referință telefonică; prețul de lansare dispare după 2 clienți | 5 | 2 |
| 16 | Raport lunar de o pagină: documente colectate, remindere trimise, zile economisite, incidente | 3 | 1 |

Eliminate: site-ul ca produs principal; radarul din ofertă; abonamentul de 12 luni; promisiunea „verificare AI a eligibilității”.

### Stiva

- **Produsul**: „Dosarul complet la timp” — clienții consultantului primesc link și remindere, consultantul vede ce lipsește, nimeni nu mai conduce 60 km după o hârtie.
- **Bonusuri**: (a) pre-check de date lipsă pe cererile noi (+400 EUR dacă vrea verdicte structurate; semnalarea simplă e inclusă); (b) șablon de pagină „Documente necesare” pe site-ul existent; (c) predarea scrisă + persoana de rezervă.
- **Garanția**: dacă în 60 de zile timpul de urmărit documente nu scade (măsurat: zile între cerere și dosar complet, înainte vs după), instalarea se returnează. Cost la o rată de reclamații de 1 din 5: 180 EUR pe contract mediu — acoperit de contribuția de ~700 EUR.
- **Urgență reală**: 2 locuri la preț de lansare până la 31 ianuarie 2027, pentru că fondatorul nu poate livra mai mult de un client la 6 săptămâni.
- **Numele**: „Dosar Complet”.

### Scor pe ecuația valorii (1–10), înainte → după

- Rezultat dorit: 5 → 7 (de la „site” la „dosare complete la timp”)
- Probabilitate percepută: 2 → 5 (pilot cu referință, test pe cereri reale, continuitate; rămâne 5 fără un client real)
- Timp până la rezultat: 4 → 7 (7 săptămâni → 2 săptămâni)
- Efort și sacrificiu: 4 → 7 (fără site, fără 12 luni, pe conturile lui)

### Re-test

`founder/pitch-v1.md` = oferta inițială (0 din 20). `founder/pitch.md` = oferta nouă; panel „quick”, același seed (7), în `founder/panel/ (oferta v2; panelul ofertei inițiale e în founder/panel-v1/)`. Rezultatul: vezi `founder/panel/results.md` și `founder/summary.md`.

## The numbers

Every number below comes from the input file. Nothing is looked up or guessed.

### One PRO contract (setup + 12 months)

| line | per PRO contract (setup + 12 months) |
| --- | ---: |
| Price | $4,080.00 |
| Hosting 12 months (5 EUR/month) | -$60.00 |
| LLM API + automation running costs 12 months (10 EUR/month) | -$120.00 |
| Theme/plugins/domain for the client | -$80.00 |
| Travel for kickoff (one Oradea trip share) | -$40.00 |
| Launch discount reserve (20% on 2 of 5 contracts, averaged) | -$192.00 |
| **Contribution** (what each PRO contract (setup + 12 months) leaves to pay the fixed costs) | **$3,588.00** (88%) |

### The margin that matters

Fixed costs: $105 a month (VPS + n8n + tools $15, Extra bookkeeping volume $30, Phone, software, misc $20, Travel not tied to a client (prospecting trips, averaged) $40).

- **Break-even: 1 PRO contract (setup + 12 months)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (0 a day): **82%** of every sale, after every cost.
- Capacity: 0.0222 a day.

### Year 1, month by month

| month | PRO contract (setup + 12 months)s a day | revenue | profit | cumulative (after $300 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$105 | -$405 |
| 2 | 0 | $0 | -$105 | -$510 |
| 3 | 0 | $0 | -$105 | -$615 |
| 4 | 0 | $4,076 | $3,479 | $2,864 |
| 5 | 0 | $0 | -$105 | $2,759 |
| 6 | 0 | $0 | -$105 | $2,654 |
| 7 | 0 | $4,076 | $3,479 | $6,134 |
| 8 | 0 | $0 | -$105 | $6,029 |
| 9 | 0 | $0 | -$105 | $5,924 |
| 10 | 0 | $4,076 | $3,479 | $9,403 |
| 11 | 0 | $0 | -$105 | $9,298 |
| 12 | 0 | $0 | -$105 | $9,193 |

- **Year 1 operating profit: $9,493** on $12,228 of revenue.
- After the $300 startup spend: $9,193.
- Startup money earned back: month 4.
- Cash you need before it pays for itself: **$615**.

### What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 82% | 1 | $9,493 |
| Price -10% | 80% | 1 | $8,270 |
| Volume -20% | 80% | 1 | $7,343 |
| Unit costs +15% | 80% | 1 | $9,272 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.

## Not done yet

- The competition: run /founder-competitors
- Marketing: run /founder-marketing
- Brand: run /founder-brand
- Operations: run /founder-ops
- Launch plan: run /founder-launch

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
