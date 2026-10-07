# Plan v2: aprofundarea planului „site-uri + automatizări” — 10.000 EUR cât mai repede (maximum 3 ani)

**Răspuns la „Prompt v2”.** Data: 7 octombrie 2026. Construit pe `plan-de-afaceri.md` (plan v1) și pe notele de cercetare din `research_notes/Plan v2 site-uri și automatizări/` (șase dosare: A reguli DR36, B1 concurență contabili, B2 prețuri site/AEO, C1 surse finanțări, C2 surse fiscal/SSM, E evenimente și contactare).

Legendă: **[VERIFICAT]** = sursă primară, link, dată · **[VERIFICAT – sursă secundară]** = presă, agregator sau fragment indexat al documentului oficial · **[ESTIMARE]** = judecata mea · **[DE VERIFICAT]** = nu am putut confirma.

**Limitare de metodă, spusă o singură dată:** din mediul în care am lucrat, toate domeniile `.ro` și `.gov.ro`, plus `developers.google.com`, `ec.europa.eu` și `web.archive.org`, au fost blocate de proxy. Nicio pagină oficială nu a fost citită integral. Cifrele vin din fragmentele indexate ale paginilor respective (link-urile sunt cele originale) și din cod public pe GitHub al unor proiecte care au monitorizat aceleași surse în 2025–2026. Tot ce e marcat [VERIFICAT – sursă secundară] trebuie deschis de tine în browser înainte să intre într-o ofertă sau într-o scrisoare oficială.

---

## 0. Rezumat: ce rămâne, ce se schimbă

**Rămâne din v1:** nișa 1 (consultanți fonduri europene și afaceri), pachetele START/PRO/RADAR pentru nișa 1 la 1.200/2.400/3.500 EUR + 60/140/280 EUR/lună, radarul vândut ca upgrade, demo pe o sursă înainte de primul client, prospectare fără e-mail rece, avocații evitați în anul 1.

**Se schimbă (detalii în §H):**
1. **Contabilii nu mai primesc „portal + OCR”.** Piața e ocupată și aproape gratuită (Contera 0 lei pentru contabil, SmartBill Conta S 2 EUR/CIF/lună, eConta 15 EUR + ~1 EUR/firmă/lună, Finans 39 lei/lună). Oferta pentru contabili devine **site + calendar de termene per client cu remindere + radar fiscal curat**, la 1.900 EUR + 120 EUR/lună, și contabilii sunt tratați în primul rând ca sursă de recomandări.
2. **Prețul de 3.500 EUR se vinde descompus** (2.400 site + automatizări, 1.100 configurare radar), pentru că depășește aproape toate ofertele publicate de site-uri de prezentare din România.
3. **Preț de pilot** pentru primii 2 clienți: −20% în schimbul unui studiu de caz, al unei recenzii și al a două introduceri.
4. **Calendarul pe 12 săptămâni e refăcut** pentru București + 2 drumuri în Bihor, cu 10–12 h/săptămână, 70 h de construcție (nu 110).
5. **Scenariile financiare**: 10.000 EUR în **luna 13 (rapid), 14 (echilibrat), 17 (prudent)**, nu 9/13/18. Abonamentele aduc 21–24% din sumă.
6. **Radarul are acum un registru concret de surse** (24 de finanțări + 12 fiscal/SSM), cu trei descoperiri care simplifică arhitectura: API JSON la MIPE (`oportunitati-ue.gov.ro/wp-json/wp/v2/apel`), catalog public MySMIS pe Oracle APEX/ORDS, API publică SEDIA la portalul UE. Și o constrângere nouă: site-urile `.gov.ro` resping conexiunile din centre de date, deci colectorul rulează de pe o conexiune rezidențială din România.
7. **DR36 confirmă regula de 30% din prima tranșă**, dar „facturat vs încasat”, TVA, abonamente și termenul exact rămân neclare în surse. E-mailul către GAL/OJFIR e în §A.2.

---

## A. Verificarea proiectului de finanțare (DR36 LEADER, PS 2023–2027)

### A.1 Ce spun sursele

| Regulă | Ce am găsit | Statut |
|---|---|---|
| Pragul de venituri | „Înainte de solicitarea celei de-a doua tranșe de plată, solicitantul face dovada desfășurării activităților comerciale prin producția comercializată sau prin activitățile prestate, în procent de **minimum 30% din valoarea primei tranșe de plată** (cerința va fi verificată în momentul finalizării implementării planului de afaceri)” — formulare redată din Ghidul de implementare DR36 al AFIR (Ed. I, Rev. 2, anexă la ordin MADR 2026) și preluată identic în ghidurile GAL din 2025 | [VERIFICAT – sursă secundară: fragment indexat al PDF-ului AFIR și al ghidurilor GAL Plaiurile Mehedințiului, Câmpia Transilvaniei] |
| Baza de calcul | Pragul se raportează la **prima tranșă**, nu la total. Tranșele le stabilește fiecare GAL (exemple găsite: 70/30, 75/25, 80/20, 90/10; a doua tranșă minimum 10%) | [VERIFICAT – sursă secundară] |
| Început | Implementarea planului de afaceri începe în maximum **6 luni** de la decizia de acordare a sprijinului | [VERIFICAT – sursă secundară, fișa intervenției GAL Câmpia Transilvaniei] |
| Termen | Durata de execuție a contractului pentru start-up neagricol: **3 ani** | [VERIFICAT – sursă secundară, doar site-uri de consultanță; **textul AFIR nu a fost citit**] |
| Dacă nu atingi obiectivul | „În cazul implementării necorespunzătoare a planului de afaceri, sumele plătite vor fi **recuperate proporțional** cu ponderea corespunzătoare acțiunilor/obiectivelor nerealizate, raportat la întreaga valoare a sprijinului” | [VERIFICAT – sursă secundară: fragment din Ghidul de implementare DR36] |
| Monitorizare după plată | 3 ani de la ultima plată | [VERIFICAT – sursă secundară, consultanți; neconfirmat în textul AFIR] |
| Facturat vs încasat | Formularea este „producția comercializată sau activitățile prestate”, nu „încasat”. La depunere, contabilul autorizat certifica „că nu există încasări de venituri pe codul CAEN pentru care se solicită finanțarea” | [DE VERIFICAT] — nicio sursă nu răspunde explicit |
| TVA | Solicitantul declară statutul de TVA și notifică AFIR în 10 zile orice schimbare; nu am găsit dacă pragul se calculează cu sau fără TVA | [DE VERIFICAT] |
| Doar CAEN-ul finanțat? | Certificarea de la depunere e „pe codul CAEN pentru care se solicită finanțarea” → probabil și verificarea e pe CAEN-ul finanțat, nu pe toată firma | [ESTIMARE] |
| Abonamente, avansuri | Nicio sursă | [DE VERIFICAT] |
| Documente la tranșa a doua | Lista exactă e în Manualul de procedură implementare DR36 (Ed. 1, Rev. 1), secțiunea dosarului cererii de plată; nu a putut fi citită | [DE VERIFICAT] |
| Diferența față de sM 6.2 (2014–2020) | Nucleul e identic (30% din prima tranșă, două tranșe, recuperare proporțională). Diferențe: la DR36 suma per proiect și tranșele le decide GAL-ul; sM 6.2 avea fix 70/30 și 50.000/70.000 EUR, cu termen explicit de 3 ani de la contract | [VERIFICAT – sursă secundară: Ghid sintetic sM 6.2 AFIR 2021, ghid MADR 2015] |

**Calculul tău, de făcut pe decizia de finanțare** [ESTIMARE]: dacă sprijinul e S și prima tranșă e p% din S, pragul = 0,30 × p% × S. Exemplu: S = 40.000 EUR, p = 83% → prima tranșă 33.333 EUR → prag 10.000 EUR. Cursul euro aplicabil și dacă se compară cu lei sau cu euro: de întrebat.

**Unde fiecare GAL poate avea reguli proprii** [VERIFICAT – sursă secundară]: suma forfetară per proiect (în plafonul de 70.000 EUR), procentele tranșelor, criteriile de selecție și obligațiile asumate prin ele (ex. parteneriate verificabile la tranșa a doua), ponderea fiecărui obiectiv în planul de afaceri. Pragul de 30% pare fix la nivel de cadru AFIR.

**GAL-urile din Bihor** (lista MADR 2023–2027, actualizată 10.02.2026) [VERIFICAT – sursă secundară]: GAL Bihor de pe lângă Frontiera cu Ungaria; GAL Țara Beiușului; GAL EuroCrișana; GAL Zona Aleșd – Valea Crișului Repede; GAL Crișul Negru (singurul cu ghid DR36 start-up confirmat online, 18.08.2025); GAL Câmpia Crișului; GAL ZMO Dealul Șomleu; GAL Valea Velj. Un studiu al Universității din Oradea vorbește de 16 GAL-uri cu teritoriu în Bihor; lista completă e pe afir.ro/instrumente/nomenclator/lista-gal/. Identifică-l pe al tău după comuna sediului și descarcă ghidul **din apelul în care ai depus**, nu versiunea curentă.

**Canal oficial de clarificări** [DE VERIFICAT]: nu am confirmat un e-mail AFIR pentru petiții. Trimite scrisoarea de mai jos (1) la GAL-ul tău (prima instanță pentru planul de afaceri), (2) la OJFIR Bihor (Oradea), care verifică cererile de plată, cu număr de înregistrare. Cere răspuns scris.

### A.2 Scrisoarea către GAL / OJFIR (gata de trimis)

> **Subiect:** Solicitare clarificări privind dovada veniturilor — Decizia de finanțare nr. [●] / [data], DR36 LEADER, ILLUSTRUS S.R.L., CUI [●]
>
> Stimate doamne / Stimați domni,
>
> ILLUSTRUS S.R.L., beneficiar al Deciziei de finanțare nr. [●] din [data] în cadrul intervenției DR36 LEADER (apel de selecție nr. [●], GAL [●]), cod CAEN finanțat 6310, vă rog să îmi comunicați în scris, pentru pregătirea corectă a cererii de plată pentru tranșa a doua, următoarele:
>
> 1. **Valoarea exactă a obiectivului de venituri**: confirmați că pragul este de 30% din valoarea primei tranșe (adică [●] EUR), cursul de schimb aplicabil și dacă verificarea se face în lei sau în euro.
> 2. **Natura veniturilor luate în calcul**: se verifică veniturile **facturate** (înregistrate în contul 70x) sau veniturile **încasate** (extras de cont)? Dacă ambele sunt necesare, în ce proporție?
> 3. **TVA**: pragul se compară cu valoarea fără TVA? Societatea [este / nu este] înregistrată în scopuri de TVA.
> 4. **Codul CAEN**: se iau în calcul doar veniturile din activitatea cu cod CAEN 6310 (prelucrarea datelor, administrarea paginilor web și activități conexe)? Vă rog să confirmați că următoarele servicii sunt considerate venituri din activitatea finanțată: (a) realizarea și publicarea de site-uri web pentru clienți; (b) administrarea, mentenanța și găzduirea paginilor web, facturate ca abonament lunar; (c) dezvoltarea de pagini/portaluri web alimentate automat cu date (prelucrare de date); (d) configurarea de automatizări legate de site (formulare, notificări). Dacă vreunul dintre acestea trebuie facturat sub alt cod CAEN pentru a fi recunoscut, vă rog să precizați.
> 5. **Abonamente**: veniturile lunare recurente (mentenanță, administrare, găzduire) facturate pe durata implementării se cumulează la obiectiv?
> 6. **Avansuri**: avansurile facturate înainte de finalizarea serviciului se iau în calcul la data facturării, la data încasării sau la data livrării serviciului?
> 7. **Clienți**: există restricții privind clienții (de exemplu, persoane afiliate, asociați, rude, firme cu același administrator sau consultantul care a elaborat planul de afaceri)?
> 8. **Termenul**: până la ce dată trebuie atins obiectivul și depusă cererea pentru tranșa a doua (de la semnarea deciziei sau de la prima plată)?
> 9. **Documentele justificative** cerute la tranșa a doua pentru dovada veniturilor (contracte, facturi, extrase, balanță, fișa contului, procese-verbale de recepție, capturi ale site-urilor livrate) și forma în care se prezintă.
> 10. **Versiunea ghidului**: care versiune a Ghidului de implementare DR36 și a Manualului de procedură se aplică deciziei mele și unde pot descărca exact acea versiune.
>
> Vă mulțumesc. Vă rog să îmi transmiteți răspunsul pe adresa [e-mail] și să îmi comunicați numărul de înregistrare al prezentei.
>
> Cu stimă,
> [Nume], administrator ILLUSTRUS S.R.L.
> [telefon] · [e-mail] · [sediu]

### A.3 Consultantul care ți-a scris proiectul: canal de recomandări, posibil client [ESTIMARE – nu am găsit regulă scrisă]

Nu am găsit în surse o interdicție ca el să devină client. Pentru ca relația să fie curată la verificarea proiectului:
- **Contract separat, la prețul de listă**, cu obiect clar și proces-verbal de recepție. Fără barter, fără compensare cu onorariile lui de consultanță, fără reducere „pentru recomandări”.
- **Plata prin bancă**, nu cash; factura cu descrierea exactă a serviciului.
- **Nu-l lăsa să fie primul sau singurul client.** Dacă 100% din venitul dovedit vine de la cel care ți-a scris planul, un verificator va pune întrebări chiar dacă regulile nu interzic. Ținta: el să fie maximum unul din 4–5 clienți.
- **Angajații sau membrii GAL** (care evaluează și monitorizează proiectele) nu pot fi clienți; nici firme ale lor. Întreabă explicit (întrebarea 7 din scrisoare).
- Păstrează corespondența în care el te recomandă altora; e dovada că relația e comercială normală.

---

## B. Concurența, pe fiecare pachet

### B.1 Tabel

| Pachet / nișă | Cine vinde deja ceva similar | Ce face | Cât costă | Statut |
|---|---|---|---|---|
| **START nișa 1 (site 6–8 pagini + SEO + GBP + formular)** — 1.200 EUR | Oradea: VisionFlow 389 EUR (+30 EUR/lună), RoMedia Design de la 2.000 lei (cu găzduire și administrare gratuite 12 luni), 4Us Consulting de la 199 EUR, Smart Mouse 100–160 EUR, sitela90lei.ro 90 lei/lună, NRGO ~400 EUR orientativ; agregator Necesit.ro 1.500–2.900 lei | Site WordPress pe template, responsive, SEO de bază | 100–990 EUR local | [VERIFICAT – sursă secundară] |
| | Național cu preț afișat: Cor Media 299/499/799 EUR, Design94 de la 390 EUR, WebDesignAgency.ro 990/1.690/2.490 EUR, HZone 990/1.290 EUR fără TVA, Sitto de la 450 EUR cu garanție 36 luni, Pronet Design (Sibiu) de la 2.500 EUR | | 299–2.500 EUR | [VERIFICAT – sursă secundară] |
| **PRO nișa 1 (site + calificare cereri AI + programări + colectare documente)** — 2.400 EUR + 140/lună | Automatizez.ro (Galați): Business 700 EUR + 150 EUR/lună (chatbot AI, programări, plăți, dashboard); WebsiteFirma.ro: Starter 500 EUR (1 chatbot sau 1 workflow n8n), Pro 1.500 EUR (3–5 workflow-uri, WhatsApp + e-mail + CRM, 90 zile suport), Custom 3.500 EUR+; webforge.org.ro: workflow mediu 600–1.500 EUR, complex/AI 1.500–5.000 EUR, mentenanță 50–150 EUR/lună; cosimo.dev de la 290 EUR/workflow | Automatizări generice, fără cunoașterea domeniului „fonduri” | 500–1.500 EUR + 50–150/lună | [VERIFICAT – sursă secundară] |
| **RADAR nișa 1 (apeluri + corrigenda potrivite pe profilul clienților finali, validate de om)** — 3.500 EUR + 280/lună | Agregatoare gratuite: fonduri-structurale.ro (>16.000 abonați newsletter, asistent AI), finantare.ro (2.000 newslettere trimise), startupcafe.ro; buletine PDF gratuite: ADR Nord-Vest „Catalogul surselor de finanțare” (lunar), CJ Harghita (săptămânal); calendarul MIPE 2026 (~300 apeluri). Produse plătite similare ca funcție: Sintact „Monitorizare Proiecte Legislative” de la 150 lei/lună fără TVA (juridic, nu fonduri); Licitatia.ro 70–162 lei/lună (licitații). Open-source: registru-fonduri-ue (GitHub), „Radar Finanțări Oradea” (digest automat pentru un startup local) | Știri și cataloage editoriale, fără potrivire pe client și fără alerte la modificări de ghid | Gratuit sau sub 50 EUR/lună | [VERIFICAT – sursă secundară] |
| **„Optimizare pentru AI” inclusă în abonamente** | optimizareai.online: audit de la 1.500 EUR, monitorizare LLM 800 EUR/lună; NION: 4.990 RON setup + 2.390 RON/lună (12 luni); AI Engine Optim 647–2.347 EUR/lună (6 luni); Instatic 499–2.499 EUR/lună, audit 590 EUR + TVA; Outglow 299/699/1.299 RON; DigitalSpace de la 700 RON/lună; AEOScore.eu (Sentio Digital Laboratories SRL, Vaslui): site de la 450 EUR, „AI Visibility Guard” 350–600 EUR/lună | Audit, conținut, schema, monitorizare mențiuni în ChatGPT/Gemini | 300 RON – 2.400 EUR/lună | AEOScore: [DE VERIFICAT – cifre date de tine; nu am putut deschide aeoscore.eu și nu apar în niciun rezultat indexat]; restul [VERIFICAT – sursă secundară] |
| **PRO contabili v1 (portal documente + OCR + remindere)** — 2.200 EUR + 150/lună | eConta Platformă: 15 EUR/lună + 0,75–1,25 EUR/firmă/lună + AI de la 0,01 EUR/doc; Elevio One: colectare + OCR + codare + bancă (12 bănci) + e-Factura + export SAGA/WinMentor, trepte „191–1.192 EUR” (perioadă și TVA neclare); Contera: cont contabil gratuit nelimitat, IMM 49–199 lei/lună; Finans Plus Contabil 39 lei/lună cu OCR + SAGA; SmartBill ManagerConta gratuit, Conta S 2 EUR + TVA/CIF/lună; Oblio 29 EUR/an cu export către contabil; TaxDome 800–1.200 USD/utilizator/an | Exact „portal + upload + OCR + e-Factura” | 0–2 EUR/firmă/lună | [VERIFICAT – sursă secundară] — **piață ocupată** |
| **PRO contabili v2 (site + calendar termene per client + remindere + radar fiscal curat)** — 1.900 EUR + 120/lună | Calendare fiscale gratuite (termene.ro, contabilul.manager.ro, legalit.ro, Accace); Lege5 67–167 lei/lună; Sintact Lege Assist 99 lei + TVA/lună; Rentrop & Straton PortalContabilitate 2.775 lei/an, Monitorul Contabil 595 lei/an; folositor.ro „Radar fiscal” gratuit (agregator RSS ANAF); contzilla newsletter gratuit | Conținut legislativ pentru contabil, nu alerte per client final și nu remindere automate per client | 0–300 lei/lună | [VERIFICAT – sursă secundară] — **nu am găsit produs care să vândă remindere de termene per client pentru cabinete** |
| **Site + automatizări pentru SSM / brokeri** | Aceiași furnizori generici de site-uri și automatizări | — | ca la START/PRO | [ESTIMARE] |

### B.2 Concluzie: unde e golul și unde intri într-o piață ocupată

- **Piață ocupată, nu intra:** „portal + OCR” pentru contabili; „site ieftin” (sub 1.000 EUR) în Oradea; „optimizare AI” ca serviciu separat (agențiile cer 650–2.400 EUR/lună și au portofoliu).
- **Piață ocupată, dar intri cu diferențiere:** site-ul profesional la 1.200 EUR. Pe plan național ești în banda „Business” (990–1.690 EUR) și la mediana ghidurilor 2026 (~1.000 EUR); în Oradea ești peste toate prețurile publicate. Diferențierea: conținut scris ca întrebările oamenilor, date structurate, Google Business, formular care calificează, și argumentul că nu vinzi gadgeturi (llms.txt) pe care Google le declară inutile.
- **Gol real (nimeni nu vinde așa):** (1) radar de finanțări cu potrivire pe profilul clienților finali ai consultantului, alerte la corrigenda/ordine de modificare, validare umană și acoperire locală (GAL Bihor, ADLO/CRESC Oradea, CCI Bihor); (2) calendar de termene per client cu remindere automate pentru cabinete mici, care se așază peste SAGA/SmartBill/Contera, nu le înlocuiește; (3) toate livrate local, la cheie, de cineva care vine fizic.

---

## C. Radarul

### C.1 Registrul de surse — finanțări (nișa 1)

Legendă verificare: **[S]** confirmat prin surse secundare 2025–2026 cu URL; **[C]** dedus din structura URL/CMS; **[G]** gol. Prioritate: **A** = în pachetul RADAR de la primul client; **B** = al doilea val; **C** = opțional.

| # | Sursă | URL de monitorizat | Ce publică | Format | Frecvență | RSS / API / newsletter | Restricții | Parsare | Prio | Verif. |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MIPE – Oportunități UE (punct unic) | https://oportunitati-ue.gov.ro/apeluri/ ; **API**: https://oportunitati-ue.gov.ro/wp-json/wp/v2/apel?per_page=100 ; https://oportunitati-ue.gov.ro/wp-sitemap.xml | Toate apelurile active/estimate 2021–2027 incl. PNRR, cu termen, buget, eligibilitate | HTML randat JS + **JSON** | zilnic–săptămânal | API WordPress REST (tip `apel`) confirmat de două proiecte open-source; `/feed/` neverificat; newsletter nu am găsit | Conexiunile din centre de date expiră (verificat aug. 2026 de alt proiect); IPv6 | Ușor prin JSON | A | [S] |
| 2 | MIPE – calendar apeluri | https://mfe.gov.ro/calendar-apeluri-de-proiecte/ | Calendarul estimativ anual (2026: ~300 apeluri, 6,6 mld EUR) | HTML + PDF/XLSX | anual + actualizări | WordPress → `/feed/` probabil, neverificat | ca #1 | Mediu | A | [S]/[C] |
| 3 | MIPE – anunțuri PNRR | https://mfe.gov.ro/category/anunțuri-pnrr/ ; https://mfe.gov.ro/pnrr/ | Apeluri PNRR, ghiduri, ordine de modificare (corrigenda) | HTML + PDF/ZIP | săptămânal | `…/feed/` probabil, neverificat | ca #1 | Mediu | A | [S] |
| 4 | MySMIS2021 – catalog public de finanțări | https://resurse.mysmis2021.gov.ro/ords/repo_bo/r/mysmis-2021/finantari-programe-2021-2027 | Registrul oficial al apelurilor validate, cu statut | HTML Oracle APEX (Interactive Report) | la fiecare apel | fără RSS; export CSV din UI de verificat | aplicația principală respinge boții; subdomeniul „resurse” neverificat | Mediu (APEX — avantajul tău) | A | [S] |
| 5 | MySMIS2021 – aplicație | https://mysmis2021.gov.ro/ | Depunere | SPA | — | nu | login, anti-bot | nu monitoriza | C | [S] |
| 6 | Platforma proiecte PNRR | https://proiecte.pnrr.gov.ro | Centralizare apeluri PNRR | HTML | — | nu am găsit | neverificat | de verificat | B | [G] |
| 7 | data.gov.ro (CKAN) | https://data.gov.ro/api/3/action/package_search?q=fonduri ; set `proiecte-contractate` | Proiecte contractate 2014–2020; **nu** apeluri 2021–2027 | CSV/XLSX + JSON | trimestrial | API CKAN; licență OGL-ROU-1.0 | fără | Ușor | B | [S] |
| 8 | Kohesio (CE) | https://kohesio.ec.europa.eu/api/projects?countryCode=RO | Proiecte finanțate RO | JSON | lunar | API | **403 din centre de date** | Ușor | C | [S] |
| 9 | AFIR – sesiuni | https://www.afir.ro/instrumente/sesiuni/sesiuni-primire-proiecte/ ; contor: https://depunerepspac.afir.ro/Sesiune/Lista | Sesiuni deschise, alocări (ex. DR-14, 1.09–31.10.2026) | HTML + PDF | lunar / zilnic | nu am găsit RSS/newsletter | blocat din mediul meu; HTTP 200 pentru alt proiect | Mediu | A | [S] |
| 10 | AFIR – ghiduri, comunicate, consultări | https://www.afir.ro/domenii-de-interventie/detalii-si-anexe-dr-NN/ ; https://www.afir.ro/comunicate/ ; https://www.afir.ro/info-la-zi/ ; DR36: https://www.afir.ro/domenii-de-interventie/detalii-si-anexe-dr-36/ | Versiuni consultative/finale de ghid, ordine MADR | HTML + PDF (`/api/file?…`) | săptămânal | nu am găsit | ca #9 | Mediu | A | [S] |
| 11 | AFIR – platforma GAL + lista GAL | https://gal.afir.ro/ ; https://www.afir.ro/instrumente/nomenclator/lista-gal/ | Apeluri GAL (obligatoriu pe platformă din 20.06.2025) | HTML | neregulat | nu am găsit | neverificat | de verificat | A (LEADER Bihor) | [S]/[G] |
| 12 | MADR – LEADER / PS 2023–2027 | https://www.madr.ro/ (URL secțiune neverificat) | Ghidul GAL, ordine MADR, lista GAL (PDF 10.02.2026) | HTML + PDF | lunar | nu am găsit | neverificat | de verificat | B | [G] |
| 13 | Regio Nord-Vest (AM PR NV) | https://regionordvest.ro/ | Apeluri PR NV (ex. 961 STEP, 28.08–12.10.2026), consultări, corrigenda | HTML (slug-uri WordPress) + PDF | săptămânal | `/feed/` și `/wp-json` probabile, neverificate; newsletter există (ADR NV achiziționează servicii de transmitere), pagină de abonare negăsită | blocat din proxy-uri (sept. 2026) | Mediu | A | [S] |
| 14 | ADR Nord-Vest | https://www.nord-vest.ro/ ; **API**: https://www.nord-vest.ro/en/wp-json/wp/v2/posts | Știri, corrigenda, catalog lunar surse de finanțare | HTML + PDF | săptămânal | WordPress REST expus (confirmat) | ca #13 | Ușor | A | [S] |
| 15 | ADR București-Ilfov | https://www.adrbi.ro/programe-regionale/por-bi-2021-2027/ ; documente `/media/<id>/` | Ghiduri, apeluri PR BI | HTML + PDF | lunar | nu am găsit | neverificat | Mediu (diff pe lista `/media/<id>/`, ID-uri crescătoare) | A | [S]/[C] |
| 16 | Alte ADR (model de parsare) | https://regionordest.ro/apeluri-de-proiecte/ ; https://2021-2027.adrmuntenia.ro/ ; https://www.adroltenia.ro/ ; https://www.vest.ro/ ; https://www.regiocentru.ro/ | Registre de apeluri | HTML + PDF | săptămânal | WordPress la unele | neverificat | Mediu | C | [S] |
| 17 | Ministerul Economiei (MEDAT) | https://economie.gov.ro/ | Start-Up Nation (sesiunea 2 deschisă 06.10.2026), Microindustrializare, Comerț, Femeia Antreprenor | HTML + PDF/DOCX | săptămânal în sezon | `/feed/` probabil, neverificat | blocat din proxy-uri | Mediu | A | [S] |
| 18 | Platforma MINIMIS | https://minimis.imm.gov.ro/ ; https://minimis.imm.gov.ro/sn2024/transparenta_persoane_juridice | Liste de transparență, ordinea de evaluare | HTML (tabele) | zilnic în sesiune | nu | paginile de transparență publice (HTTP 200, sept. 2026) | Ușor | A | [S] |
| 19 | Ministerul Energiei – Fondul pentru Modernizare | https://energie.gov.ro/category/fondul-pentru-modernizare/ | Apeluri FM (autoconsum, CHP), actualizări de ghid | HTML + PDF | lunar | `…/feed/` probabil, neverificat | neverificat | Mediu | B | [S] |
| 20 | Ministerul Transporturilor – FM | https://fonduri.mt.ro/transparenta/consultare-publica/fondul-pentru-modernizare/ | Consultări (e-MOVE RO) | HTML + PDF | rar | nu | neverificat | Mediu | C | [S] |
| 21 | AFM | https://www.afm.ro/ ; https://online.afm.ro/ | Rabla firme, stații de reîncărcare, ghiduri | HTML + PDF | lunar | nu am găsit | depunere cu cont | de verificat | B | [S]/[G] |
| 22 | MCID / research.gov.ro | https://www.mcid.gov.ro/ ; https://www.research.gov.ro/ | Ghiduri PNRR cercetare în dezbatere | HTML + PDF | rar | nu | neverificat | de verificat | C | [G] |
| 23 | Granturi SEE & Norvegiene / Innovation Norway | https://eeagrants.ro/ | Programul de Dezvoltare a Afacerilor (43 mil EUR), Energie (62,8 mil EUR) | HTML + PDF | 1–2 apeluri/an | nu am găsit | neverificat | de verificat | B | [S]/[G] |
| 24 | EU Funding & Tenders Portal (SEDIA) | `POST https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=***` ; bulk: https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json ; pagina API: https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/apis | Toate apelurile UE, statut (31094501 forthcoming, 31094502 open, 31094503 closed), termene | **JSON** | zilnic | API publică, fără cheie/login; trimite `languages:["en"]`; `deadlineDate` în format `2026-09-21T00:00:00.000+0000` | fără declarație oficială privind accesul automat; robots/termeni necitite | Ușor | B | [S] |

Toate: [VERIFICAT – sursă secundară]. Niciun `robots.txt` și nicio pagină de termeni nu a fost citită; completezi coloana „Restricții” la prima rulare de pe o conexiune normală și salvezi `robots.txt` în tabela `SOURCE` ca dovadă de bună-credință.

**Nucleul de 8 surse pentru primul client RADAR** [ESTIMARE]: #1 (JSON), #4 (catalog MySMIS), #2 + #3 (MIPE), #9 + #10 (AFIR), #11 (GAL), #13 + #14 (Regio NV / ADR NV), #15 (ADRBI), #17 + #18 (MEDAT + MINIMIS). Majoritatea sunt WordPress → un singur adaptor (`wp-json` + `/feed/`) acoperă 7–8 surse; AFIR, ADRBI, APEX/ORDS și SEDIA au adaptoare dedicate.

**Constrângere operațională** [VERIFICAT – sursă secundară: două proiecte independente, aug.–sept. 2026]: `oportunitati-ue.gov.ro` și `mfe.gov.ro` lasă conexiunile din centre de date (Hetzner, GitHub Actions) să expire; Kohesio răspunde 403. Soluție: colectorul Python rulează pe un mini-PC acasă în Bihor sau pe un VPS românesc cu IPv4 + IPv6, 1 cerere/zi/sursă, ≥1 s între cereri, `User-Agent` identificabil cu e-mail de contact. Nu scrapa din n8n Cloud sau din cloud străin.

### C.2 Registrul de surse — radar fiscal / SSM (nișele 2 și 3)

| # | Sursă | URL | Ce publică | Format | Frecvență | RSS / API | Restricții | Parsare | Prio |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Monitorul Oficial – e-Monitor | https://monitoruloficial.ro/e-monitor/ ; index intern folosit de un scraper: `…/ramo_customs/emonitor/get_mo.php` (cere header `Referer: https://monitoruloficial.ro/e-monitor/`) | Partea I și II, PDF per ediție, gratuit din ziua publicării (Legea 57/2021 permite expres „căutare, salvare, distribuire și tipărire”) | PDF text | zilnic | nu am găsit RSS/API; baza plătită e Expert Monitor | lanț de certificat incomplet raportat; termeni necitiți | Medie (split pe acte după sumar) | 1 |
| 2 | legislatie.just.ro | https://legislatie.just.ro/Public/DetaliiDocument/{id} ; **SOAP**: http://legislatie.just.ro/ServiciulWebLegislatie.htm (client Python open-source govro) | Text consolidat, metadate, legături | HTML + SOAP | continuu | API SOAP oficial; RSS nu am găsit | OKFN: date fără drept de autor, reutilizabile; terți: fără anti-bot | Mică–medie | 1 |
| 3 | ANAF – Noutăți legislative | https://static.anaf.ro/static/10/Anaf/Legislatie_R/noutati_legislative.htm | Buletin săptămânal cu actele fiscale din MO (nr. 25 din 20.07.2026) | HTML static | săptămânal | RSS ANAF există (folositor.ro le agregă la ≤2 h); URL-uri exacte negăsite | server static, risc mic | Mică | 1 |
| 4 | ANAF – calendar obligații | https://www.anaf.ro/ (secțiunea Asistență contribuabili; URL exact neverificat) | Termene lunare | HTML/PDF | lunar | nu | neverificat | Medie | 2 |
| 5 | ANAF – proiecte, ghiduri, SPV/e-Factura | https://static.anaf.ro/static/10/Anaf/AsistentaContribuabili_r/ | Ghiduri (e-Factura), proiecte de ordine | HTML + PDF | neregulat | RSS pe categorii (negăsite exact) | neverificat | Medie | 2 |
| 6 | Ministerul Finanțelor – transparență | https://mfinante.gov.ro/ (pagina exactă neverificată) | Proiecte OUG/HG/ordine (Cod fiscal) | HTML + PDF/DOC | săptămânal | nu am găsit | neverificat | Mare | 2 |
| 7 | Inspecția Muncii | https://www.inspectiamuncii.ro/ (documente Liferay `/documents/…/*.pdf/{uuid}`) | Comunicate săptămânale, campanii, legislație SSM | HTML + PDF | săptămânal | nu am găsit | neverificat | Medie | 2 (SSM) |
| 8 | Ministerul Muncii | https://mmuncii.ro/ (transparență; pagina exactă neverificată) | Proiecte SSM (HG 1425/2006, Legea 319/2006) | HTML + PDF | neregulat | nu am găsit | neverificat | Mare | 2 (SSM) |
| 9 | IGSU / MAI – PSI | https://www.igsu.ro/ ; https://www.mai.gov.ro/ | Legea 307/2006, OMAI 163/2007, norme | HTML + PDF | rar | nu | neverificat | Medie | 3 |
| 10 | Senat | https://www.senat.ro/Legis/Lista.aspx?cod=… ; buletin legislativ PDF | Propuneri, consultare publică; **RSS pentru consultarea publică** menționat în pliantul oficial POCA (URL negăsit) | ASP.NET + PDF | zilnic | RSS (URL de găsit) | neverificat | Medie | 3 |
| 11 | Camera Deputaților | https://www.cdep.ro/ (PL/SQL + ORDS `/ords/co/…`) | Proiecte de lege, ordine de zi | HTML | zilnic | nu am găsit | neverificat | Mare | 3 |
| 12 | SGG / consultare.gov.ro | https://sgg.gov.ro/ ; https://consultare.gov.ro/ | Proiecte centralizate, ședințe de guvern | HTML + PDF | săptămânal | nu am găsit | neverificat | Medie | 3 |

Toate: [VERIFICAT – sursă secundară]. Validare încrucișată gratuită: folositor.ro/radar-fiscal, contzilla.ro, contabilul.manager.ro.

### C.3 Cum măsori precizia înainte să vinzi [ESTIMARE]

1. **Set de test („golden set”)**: 120 de elemente etichetate manual de tine în 2 seri: 60 de apeluri/corrigenda reale din ultimele 90 de zile (surse #1, #3, #9, #13, #17) + 60 de „zgomot” (știri, comunicate fără apel, evenimente). Pentru fiecare: tip, termen limită, buget, beneficiari eligibili, regiune, CAEN-uri. Plus 10 profiluri fictive de clienți finali (IMM Bihor producție, cabinet medical București, fermă, ONG etc.) cu lista corectă de potriviri.
2. **Metrici**, calculate automat în APEX după fiecare rulare:
   - Clasificare (apel vs zgomot): precizie ≥ 90%, recall ≥ 90%.
   - Extracție câmpuri: termen limită corect ≥ 95% (câmpul critic), buget și eligibilitate ≥ 85%.
   - Potrivire pe profil: precizie ≥ 80% (din alertele propuse, cel puțin 8 din 10 relevante), recall ≥ 90% (din apelurile relevante, cel puțin 9 din 10 prinse).
   - Latență: alerta propusă în ≤ 24 h de la publicare pentru 90% din elemente.
3. **Prag de acceptare**: două săptămâni consecutive peste praguri pe date noi (nu pe setul de test) și rată de aprobare în coada de validare ≥ 70% (dacă respingi 4 din 10 alerte, extracția nu e gata).
4. **După vânzare**: fiecare „respins/corectat” din coada APEX intră automat în setul de test; raport lunar de precizie către client (e și argument de reînnoire).

### C.4 Schema de date minimă (Oracle) [ESTIMARE]

| Tabel | Câmpuri principale | Rol |
|---|---|---|
| `SOURCE` | id, name, base_url, monitor_url, access_method (wpjson/rss/html/apex/soap/sedia), format, frequency_hours, robots_txt (CLOB, data citirii), terms_url, requires_ro_ip (Y/N), rate_limit_sec, priority, active, last_run_at, last_http_status, health | registrul de surse |
| `FETCH_RUN` | id, source_id, started_at, finished_at, status, items_seen, items_new, error | jurnal de rulări |
| `RAW_DOC` | id, source_id, url, content_hash, fetched_at, content (CLOB/BLOB), content_type, http_etag, last_modified | conținut brut, dedup pe hash |
| `ITEM` | id, source_id, external_id, url, title, item_type (apel/ghid/corrigendum/lege/termen/stire), first_seen_at, last_changed_at, status (deschis/estimat/închis), confidence | elementul normalizat |
| `ITEM_VERSION` | id, item_id, raw_doc_id, version_no, extracted_json (CLOB), diff_summary, created_at | istoricul modificărilor (corrigenda = versiune nouă) |
| `ITEM_FIELD` | item_id, field_name (deadline, budget_min, budget_max, region, beneficiary_type, caen_list, program, intensity), field_value, confidence | câmpuri extrase, interogabile în SQL |
| `CLIENT` | id, name, cui, contact, plan (START/PRO/RADAR), channels (email/whatsapp), active | clientul tău (consultantul) |
| `CLIENT_PROFILE` | id, client_id, end_client_name, caen_list, county, size (micro/mica/mijlocie), legal_form, sectors, funding_types_wanted, keywords, budget_range, active | clienții finali ai consultantului (max 30/RADAR) |
| `MATCH` | id, item_id, profile_id, rule_score, semantic_score, total_score, created_at | rezultatul potrivirii |
| `ALERT` | id, match_id, client_id, status (propusă/aprobată/respinsă/corectată/trimisă), reviewer, reviewed_at, sent_at, channel, message_text, correction_note | coada de validare umană + jurnal de audit |
| `EVAL_GOLDEN` | id, item_id sau raw_doc_id, expected_type, expected_fields_json, expected_profile_ids, labeled_by, labeled_at | setul de test |
| `EVAL_RUN` | id, run_at, precision_cls, recall_cls, deadline_acc, match_precision, match_recall, notes | istoric de precizie |
| `PUBLISH_LOG` | id, client_id, item_id, site_url, published_at, status | ce a ajuns pe pagina publică a clientului |

Chei: `RAW_DOC.content_hash` unic per sursă; `ITEM.external_id` = URL canonic sau ID API. Date personale: `CLIENT_PROFILE` conține date de firmă, nu de persoane; dacă apar persoane (PFA), marchează și aplică retenție.

### C.5 Fluxurile n8n principale [ESTIMARE]

| Flux | Declanșator | Pași | Ieșire |
|---|---|---|---|
| F1 Colectare | Cron zilnic 06:00 (rulat pe mașina cu IP românesc; n8n self-hosted acolo sau n8n care apelează un script Python prin SSH/webhook) | pentru fiecare `SOURCE` activă: citește `robots.txt` (o dată/lună), fetch cu User-Agent identificabil, hash, scrie `RAW_DOC` doar dacă hash-ul e nou, `FETCH_RUN` | documente brute noi |
| F2 Extracție | `RAW_DOC` nou (webhook din DB sau poll la 15 min) | normalizare (HTML→text, PDF→text cu Python), prompt cu schemă JSON fixă, LLM prin API (fără antrenare pe date), validare JSON (termen = dată validă, buget numeric), scriere `ITEM` + `ITEM_VERSION` + `ITEM_FIELD`, diff față de versiunea anterioară | elemente structurate |
| F3 Potrivire | `ITEM` nou/modificat | apel la procedură PL/SQL: reguli (CAEN ∩ județ/regiune ∩ tip beneficiar ∩ termen > azi) + scor semantic (embedding titlu+rezumat vs profil) → `MATCH` cu scor; `ALERT` cu status „propusă” pentru scor ≥ prag | coadă de validare |
| F4 Livrare | Butonul „Aprobă” din APEX (status → aprobată) | compune mesajul (titlu, de ce e relevant pentru clientul X, termen, link la sursă, marcaj „informativ, verificați ghidul”), trimite e-mail / WhatsApp Business API, actualizează `ALERT.sent_at`; webhook către WordPress REST (`/wp-json/wp/v2/posts` sau un custom post type) pentru pagina „Apeluri deschise” → `PUBLISH_LOG` | alerte + pagină publică |
| F5 Raport lunar | Cron, ziua 1 | SQL: alerte trimise, apeluri noi, modificări, precizie din `EVAL_RUN`, vizibilitate (10 întrebări verificate manual) → PDF → e-mail client | raport |
| F6 Sănătate | Cron la 6 h | surse cu `last_http_status` ≠ 200 sau fără elemente noi de X zile → notificare ție; cost API LLM din log | alertă internă |

Costuri de operare [ESTIMARE]: Oracle Always Free (2 ADB × 20 GB, APEX inclus) 0 EUR; mini-PC/VPS românesc 5–10 EUR/lună; API LLM 5–30 EUR/lună; n8n Community Edition 0 EUR (Cloud Starter 20 EUR/lună dacă nu vrei administrare). Sub 50 EUR/lună până la 5 clienți.

---

## D. Prețuri și validarea lor

### D.1 Zece oferte reale, comparate cu pachetele tale

| # | Furnizor (oraș) | Ce include | One-off | Lunar | TVA | Link | Statut |
|---|---|---|---|---|---|---|---|
| 1 | VisionFlow (pagină Oradea/Bihor) | Site Business Pro | 389 EUR (de la 689) | 30 EUR mentenanță | nespecificat | visionflow.ro/creare-site-oradea-bihor | [VERIFICAT – sursă secundară] |
| 2 | RoMedia Design (Oradea) | Prezentare ≤10 pagini, design custom, găzduire + administrare gratuite 12 luni | de la 2.000 lei | 0 în primul an | nespecificat | romediadesign.com | [VERIFICAT – sursă secundară] |
| 3 | WebDesignAgency.ro | Start 6–8 pagini, SEO bază, 2 revizii, garanție 30 zile / Business / Premium | 990 / 1.690 / 2.490 EUR | de la 29 EUR | nespecificat | webdesignagency.ro/pachete | [VERIFICAT – sursă secundară] |
| 4 | HZone | Site prezentare / interactiv | 990 / 1.290 EUR | — | fără TVA 19% | hzone.ro/servicii/creare-site | [VERIFICAT – sursă secundară] |
| 5 | Pronet Design (Sibiu) | Site de business, calculator de preț | de la 2.500 EUR | — | parțial „+TVA” | pronetdesign.ro/pret-website | [VERIFICAT – sursă secundară] |
| 6 | Webage | Mentenanță BASIC / STANDARD; administrare | — | 59 / 149 / de la 75 EUR | nespecificat | webage.ro/mentenanta-site-web | [VERIFICAT – sursă secundară] |
| 7 | SiteSOS | Mentenanță Basic / Standard / Premium (2 h dev) | — | 500 / 1.000 / 2.000 RON | + TVA | sitesos.ro/mentenanta | [VERIFICAT – sursă secundară] |
| 8 | Automatizez.ro (Galați) | Site + hosting (Starter); + chatbot AI, programări, plăți (Business) | 300 / 700 EUR | 50 / 150 EUR | nespecificat | automatizez.ro | [VERIFICAT – sursă secundară] |
| 9 | WebsiteFirma.ro | Starter 1 chatbot sau 1 workflow n8n / Pro 3–5 workflow-uri + CRM + 90 zile suport | 500 / 1.500 EUR | — | nespecificat | websitefirma.ro/automatizari-firma | [VERIFICAT – sursă secundară] |
| 10 | NION | AEO „Full Package”: audit, conținut, schema, 20 articole, raport lunar | 4.990 RON setup | 2.390 RON (min. 12 luni) | nespecificat | nion.ro | [VERIFICAT – sursă secundară] |
| 11 | optimizareai.online | Audit AEO / monitorizare LLM | 1.500 EUR | 800 EUR | nespecificat | optimizareai.online | [VERIFICAT – sursă secundară] |
| 12 | AEOScore.eu (Vaslui) | Audit, optimizare, site; „AI Visibility Guard” | de la 450 EUR | 350–600 EUR | — | aeoscore.eu | [DE VERIFICAT – cifre din prompt; pagina nu a putut fi deschisă și nu apare indexată] |

Repere agregate 2026 [VERIFICAT – sursă secundară]: site de prezentare 500–2.500 EUR, median ~1.000 EUR; site custom în cod 2.500–6.000 EUR; mentenanță 10–20% din valoarea proiectului pe an (ghiduri cyberfolks.ro, webforge.org.ro, brig.ro); automatizări 600–1.500 EUR (mediu), 1.500–5.000 EUR (AI), mentenanță 50–150 EUR/lună freelanceri, 200–800 EUR/lună agenții.

Google [VERIFICAT – sursă secundară; pagina oficială nu a putut fi citită]: „There are no additional technical requirements to appear in AI features”; ghidul „Optimizing your website for generative AI features on Google Search” (adăugat 15 mai 2026 conform Search Engine Journal; tu indici o actualizare în iulie 2026 — [DE VERIFICAT] data din subsolul paginii) spune explicit că **nu ai nevoie de fișiere llms.txt, fișiere text pentru AI, markup special sau Markdown**, și că AEO/GEO „este tot SEO”. Argument de vânzare onest: unele agenții românești încă vând llms.txt ca livrabil.

### D.2 Verdict pe 1.200 / 2.400 / 3.500 EUR pentru un furnizor nou, fără portofoliu [ESTIMARE]

| Pachet | Verdict | Condiție |
|---|---|---|
| START 1.200 EUR + 60/lună | **Realist pe plan național, scump pentru Oradea.** Ești în banda „Business” (990–1.690 EUR) și la mediana ghidurilor; local, nimeni nu afișează peste ~990 EUR | Livrabile explicite: 6–8 pagini cu texte scrise de tine din interviul cu clientul (nu „trimiteți textele”), FAQ, date structurate, Google Business, formular cu calificare, raport la lansare. 60 EUR/lună ≈ Webage BASIC (59 EUR); include găzduire, update-uri, backup, 2 h/lună |
| PRO 2.400 EUR + 140/lună | **Realist doar cu automatizările vizibile.** ≈ „Premium” național (2.490 EUR); automatizările singure valorează 500–1.500 EUR pe piață | Vinde-l ca „site 1.200 + automatizări 1.200”; 140 EUR/lună ≈ Webage STANDARD (149) și include chatbot/calificare (50–150 EUR/lună pe piață) + 4 h/lună |
| RADAR 3.500 EUR + 280/lună | **Greu de susținut ca „site”; susținut ca „sistem”.** Depășește aproape toate ofertele publicate de site-uri; dar e sub orice ofertă AEO (650–2.400 EUR/lună) și sub automatizările „AI” (1.500–5.000 EUR) | Descompune: 2.400 (PRO) + 1.100 (configurare radar: 8 surse, 30 profiluri, pagină publică). 280 EUR/lună ≈ SiteSOS Standard–Premium; include validarea umană (4–6 h/lună), raportul de precizie, raportul de vizibilitate |
| PRO contabili 1.900 EUR + 120/lună | **Realist** ca site + calendar termene + remindere + radar fiscal; **nerealist** ca portal + OCR (concurenți la 0–2 EUR/firmă/lună) | Nu construi OCR; folosește portalul gratuit al Contera/SmartBill/Oblio pe care clientul îl are deja și adaugă ce lipsește |

**Cum compensezi lipsa portofoliului** [ESTIMARE; practicile de piață observate: preț tăiat afișat, garanții 30 zile–36 luni, 12 luni administrare gratuită — VisionFlow, Sitto, WebDesignAgency, RoMedia; nu am găsit date românești despre „pilot pricing” la agenții noi]:
1. **Preț de pilot pentru primii 2 clienți: −20%** (START 960, PRO 1.920), scris în ofertă ca „preț de lansare, valabil pentru primii 2 clienți semnați până la [dată]”, în schimbul: studiu de caz cu nume, recenzie Google (cerută tuturor, nu selectiv), 2 introduceri. Nu scădea abonamentul.
2. **Garanție de satisfacție pe START**: dacă la livrare site-ul nu respectă specificația scrisă din anexa 1, clientul nu plătește a doua tranșă până nu e corectat; 90 de zile de corectări gratuite (norma de piață e 30–90).
3. **Portofoliu înainte de primul client**: site-ul ILLUSTRUS + pagina demo „Apeluri deschise Bihor” cu date reale + un site refăcut gratuit pentru o cauză locală (ONG, asociație) — 15 h, un caz real.
4. **Pilot plătit pentru RADAR**: 30 de zile la 1.100 EUR (configurarea) cu drept de a nu continua; dacă continuă, trece la 280 EUR/lună. Reduce riscul perceput al unui produs nou.

---

## E. Clienții și vânzarea

### E.1 Lista de 50 de prospecți calificați, legal [VERIFICAT – sursă secundară pentru surse; ESTIMARE pentru metodă]

1. **Filtru**: CAEN 7022 (consultanță pentru afaceri și management), 7021, 7020 (verifică echivalența în CAEN Rev. 3), denumire conține „consulting/proiecte/fonduri/grant/europe”; județ Bihor sau București; activă; cifră de afaceri > 0; ≥ 1 angajat.
2. **Surse gratuite**: paginile termene.ro pe cod CAEN (ex. CAEN 7022; filtrarea pe județ cere abonament sau parcurgere manuală); topfirme.com pe județ + CAEN; Google Maps „consultanță fonduri europene Oradea/București”; Necesit.ro „Top 20 consultanță fonduri europene București 2026”; site-urile ADR NV / ADRBI (listele de beneficiari ale apelurilor menționează uneori consultantul); ACRAFE (59 de firme membre, >1.000 consultanți — lista de membri [DE VERIFICAT pe acrafe.ro]).
3. **Sursa contra cost, cea mai curată juridic**: ONRC/Recom „serie de firme grupate pe criterii” (CAEN + județ): tarif ~9–11 lei/firmă, −30% peste 100 de firme [VERIFICAT – sursă secundară, tarife posibil actualizate]. Obții denumire, CUI, sediu, administratori (date de registru).
4. **Calificare** (vizită pe site, 5 minute/firmă): are site? vechime? arată proiecte? e pe LinkedIn? menționează DR/PNRR/PR NV? → scor 1–5. Păstrezi 50 cu scor ≥ 3.
5. **Separă datele**: coloana „firmă” (denumire, CUI, office@, telefon fix, site — nu sunt date personale) de coloana „persoană” (nume administrator, e-mail nominal, LinkedIn — date personale: temei interes legitim art. 6(1)(f) GDPR, cu un test de echilibrare scris de o pagină și notă de informare la primul contact, art. 14).
6. **Nu**: scraping LinkedIn (încalcă termenii), liste de e-mail cumpărate, automatizări de contact.
7. **Nu există** o „listă oficială a consultanților” la MIPE sau AFIR [VERIFICAT – sursă secundară: căutările au returnat doar contracte MIPE și cazuri de conflict de interese].

### E.2 Evenimente și comunități (oct. 2026 – ian. 2027)

| Data | Eveniment | Unde | Cine vine | Cost | Statut |
|---|---|---|---|---|---|
| 21 oct. 2026 | CFO Conference Oradea (BusinessMark) | Ramada Oradea, 08:30–15:30 | CFO, antreprenori, manageri | 600 RON + TVA | [VERIFICAT – sursă secundară] |
| 22 oct. 2026 | MAGNETICO Oradea (BusinessMark) | Ramada Oradea | HR, management | neverificat | [VERIFICAT – sursă secundară] |
| 10–11 nov. 2026 | GoTech World | Romexpo București | 15.000+ participanți B2B IT & digital, inclusiv consultanți de digitalizare | bilet expo [DE VERIFICAT] | [VERIFICAT – sursă secundară] |
| 12 nov. 2026 | CFO Conference Timișoara | Timișoara | ca mai sus | 600 RON + TVA | [VERIFICAT – sursă secundară] |
| noiembrie (recurent) | Zilele Biz (Revista Biz) | București, 3 zile, 80+ speakeri | antreprenori, corporații | [DE VERIFICAT] | dată 2026 neconfirmată |
| ~24 nov. (recurent; 2025: 24 nov., Crowne Plaza) | București Business Days (BRCC) | București | lideri de piață, networking | [DE VERIFICAT] | dată 2026 neconfirmată |
| sfârșit oct. / început nov. (recurent) | Topul Firmelor: CCIB (București, ~29 oct.), CCIR (gala națională, ~6 nov.), **CCI Bihor** | București / Oradea | firmele premiate pe CAEN, inclusiv consultanță | invitație / taxă [DE VERIFICAT] | dată 2026 neconfirmată |
| recurent (2023: 25 mai, 190 participanți) | **Business Evolution Oradea** „Finanțare. Digitalizare. Sustenabilitate” (partener CCI Bihor) | Oradea | antreprenori + consultanți de fonduri — **publicul tău exact** | [DE VERIFICAT] | dată 2026 neconfirmată |
| recurent | Entrepreneurial Journey (Univ. Oradea); Be Inspired Oradea (B-Leader); EMEB/EINCO (FSE Oradea, noiembrie) | Oradea | academic + practicieni | [DE VERIFICAT] | dată 2026 neconfirmată |
| recurent | Maratonul Fondurilor Europene (Profit.ro) — temă: „cum alegi consultantul potrivit” | București / online | consultanți, IMM | gratuit de obicei | dată 2026 neconfirmată |
| continuu | Oradea Tech Hub / Make IT in Oradea (Cowork deschis în sept. 2026), Startup Grind Bucharest (819 membri), ACRAFE | Oradea / București | tech, antreprenori, consultanți | gratuit / membru | evenimente de toamnă negăsite |

Nu am găsit niciun eveniment numit „Zilele Fondurilor Europene” și nici sesiuni de informare ADR NV / MIPE în Oradea pentru toamna 2026. Recomandare: abonează-te acum la newsletterele CCI Bihor, CCIB, ACRAFE, BusinessMark, Revista Biz și urmărește paginile lor în octombrie.

### E.3 Ce e permis la contactare (Legea 506/2004 art. 12 + GDPR)

Textul art. 12 alin. (1) [VERIFICAT – sursă secundară; textul integral de la legislatie.just.ro, Document 57058, nu a putut fi deschis]: interzice comunicările comerciale „prin utilizarea unor sisteme automate de apelare și comunicare care nu necesită intervenția unui operator uman, prin fax ori prin poștă electronică sau prin orice altă metodă care folosește serviciile de comunicații electronice destinate publicului”, fără consimțământ prealabil expres; excepția „produse/servicii similare” pentru clienți existenți; amenzi 5.000–100.000 lei sau până la 2% din cifra de afaceri la firme > 5 mil. lei. Practica ANSPDCP [VERIFICAT – sursă secundară]: în 2025, 9 amenzi pe Legea 506/2004 (187.000 RON total); One United Properties 2.000 EUR (feb. 2025), Whitedecor 2.000 EUR (oct. 2025), Elefant 10.000 lei; **NN Asigurări de Viață sancționată pentru mesaje comerciale trimise prin mesageria LinkedIn** (titlu Profit.ro; detalii [DE VERIFICAT]). EDPB, Ghidul 1/2024: marketingul direct nu e automat interes legitim; testul în 3 pași e obligatoriu.

| Canal | Statut | De ce |
|---|---|---|
| Apel telefonic făcut de tine, la numărul firmei | **Permis, risc scăzut** | Art. 12(1) vizează sisteme automate fără operator uman; numărul fix al firmei nu e dată personală. Dacă numărul e mobilul personal al consultantului: dată personală → interes legitim documentat, informare la primul contact, respectă refuzul |
| Vizită, întâlnire la eveniment | **Permis** | Nu e comunicare electronică |
| E-mail după o discuție în care persoana a acceptat să primească informații | **Permis** | Consimțământ expres (notează-l: carte de vizită + dată + ce a cerut); primul e-mail face referire la discuție și are opțiune de dezabonare |
| Formular de contact de pe site-ul prospectului | **Gri spre permis** | Canal pus la dispoziție de firmă; mesaj unic, personalizat, cu identitate reală; nu există practică ANSPDCP identificată |
| Mesaj LinkedIn personalizat, după acceptarea conexiunii | **Gri, cu precedent nefavorabil (NN)** | Unu-la-unu, fără caracter de ofertă în masă, fără instrumente de automatizare |
| E-mail rece pe adresă nominală | **Interzis** | Poșta electronică e expres în art. 12(1); România nu are excepție B2B |
| E-mail rece pe office@ | **Gri, tinde spre interzis** | „Abonatul” include persoane juridice [DE VERIFICAT art. 2]; nicio sancțiune găsită pe acest scenariu, dar riscul nu e zero |
| Orice automatizare (secvențe, auto-dialer, boți) | **Interzis** | Exact ipoteza legii |

Fluxul recomandat: eveniment / vizită / apel uman la firmă → acord explicit de a trimite informații → e-mail cu referire la discuție + dezabonare + notă GDPR → follow-up LinkedIn personalizat.

### E.4 Script de telefon (60 de secunde) [ESTIMARE]

> „Bună ziua, [Nume], sunt Matei de la ILLUSTRUS, din Oradea. Lucrez cu firme de consultanță în fonduri europene. Aveți un minut? [pauză]
> Pe scurt: am construit un instrument care urmărește zilnic sursele oficiale — MIPE, AFIR, ADR Nord-Vest, GAL-urile din Bihor — și îmi spune, pe fiecare client al unui consultant, pentru ce apel nou sau ce modificare de ghid e eligibil. Alertele sunt verificate de om înainte să plece. Pe lângă asta fac site-uri care aduc cereri calificate, nu doar vizite.
> Nu vă sun să vă vând acum. Vreau 20 de minute, la birou sau online, să vă arăt pe datele reale din Bihor cum arată și să-mi spuneți dacă vi s-ar potrivi sau nu. Dacă nu, îmi spuneți ce ar trebui să facă diferit. Marți sau joi vă convine?
> [Dacă nu] Înțeleg. Pot să vă trimit un e-mail cu un link la pagina cu apelurile deschise din Bihor, fără altceva? [notează acordul] Mulțumesc, o zi bună.”

### E.5 Mesaj de follow-up după întâlnire [ESTIMARE]

> **Subiect:** Mulțumesc pentru discuția de [zi] — pagina cu apelurile și pașii următori
>
> Bună ziua, [Nume],
>
> Mulțumesc pentru cele 20 de minute de [zi]. Așa cum am convenit, vă trimit: (1) linkul la pagina „Apeluri deschise Bihor / Nord-Vest” actualizată automat: [link]; (2) exemplul de alertă pentru profilul de client despre care am vorbit ([tip firmă, județ]); (3) oferta pe o pagină pentru [pachet], cu prețul de lansare valabil până la [dată].
>
> Din ce mi-ați spus, cel mai mult v-ar ajuta [problema concretă menționată de el: ex. „să aflați de corrigenda înainte de clienți”]. Propun un pas mic: [pilot de 30 de zile / site-ul cu formularul de calificare], cu [preț], fără obligație de continuare.
>
> Dacă nu e momentul, îmi spuneți și nu insist. Dacă e, îmi ajunge un „da” ca să trimit contractul.
>
> Cu stimă, Matei [telefon]
>
> _Primiți acest mesaj pentru că ați acceptat la întâlnirea din [zi] să primiți informații de la ILLUSTRUS S.R.L. Dacă nu mai doriți, răspundeți „stop” și șterg datele dvs. de contact. Detalii: [link politică de confidențialitate]._

---

## F. Livrabile gata de folosit

### F.1 Oferta standard (o pagină), nișa 1

> **ILLUSTRUS S.R.L. — Site + automatizări + radar de finanțări pentru consultanți în fonduri europene**
> Oradea / București · [telefon] · [e-mail] · [site] · Ofertă valabilă 30 de zile · Prețuri fără TVA [sau: ILLUSTRUS nu este plătitor de TVA — de completat după verificare]
>
> | | **START** | **PRO** | **RADAR** |
> |---|---|---|---|
> | **Pentru cine** | Vreți un site care aduce cereri, nu doar vizite | Vreți să nu mai pierdeți timp cu cereri neeligibile și documente lipsă | Vreți să fiți primul care sună clientul când apare apelul |
> | **Preț instalare** | **1.200 EUR** (preț de lansare primii 2 clienți: 960) | **2.400 EUR** (lansare: 1.920) | **3.500 EUR** = PRO 2.400 + radar 1.100 |
> | **Abonament** | **60 EUR/lună** | **140 EUR/lună** | **280 EUR/lună** |
> | **Site** | 6–8 pagini: acasă, 4 servicii, despre, întrebări frecvente (15 întrebări scrise cum le caută oamenii), contact, GDPR. Texte scrise de noi din 2 interviuri cu dvs. | START + pagini detaliate de serviciu (max 8) + 3 studii de caz + blog | PRO + pagina publică „Apeluri deschise” / „Ce s-a schimbat luna asta”, actualizată automat, cu link la sursă |
> | **Vizibilitate** | SEO tehnic, date structurate (Organization, Service, FAQPage), profil Google Business, Search Console. Fără gadgeturi: Google spune că nu există cerințe speciale pentru funcțiile AI | START + plan de 10 articole (titluri + structură) | PRO + raport lunar: 10 întrebări agreate verificate în Google, Modul AI, Gemini, ChatGPT (fără promisiuni de poziție) |
> | **Automatizări** | Formular → notificare + listă de cereri | + Calificare preliminară cu AI (eligibil probabil / nu, cu motiv), programare automată, remindere, colectare documente de la clienții dvs. prin link securizat | + Radar: 8 surse oficiale (MIPE, MySMIS, AFIR, GAL, Regio NV, ADR NV, ADR BI, MEDAT), profiluri pentru max 30 de clienți ai dvs., alerte validate de om în max 24 h, e-mail/WhatsApp |
> | **Limite** | 2 runde revizii design, 1 pe texte; 2 h/lună suport | 3 runde; 4 h/lună | 3 runde; 6 h/lună; 2 modificări de profil/lună |
> | **Termen** | 4 săptămâni de la avans | 7 săptămâni | 9 săptămâni |
> | **Abonamentul include** | Găzduire, domeniu (pe numele dvs.), actualizări, backup zilnic, monitorizare, raport lunar | + Rularea automatizărilor, costuri API | + Validarea alertelor, raport de precizie, pagina publică |
>
> **Cum lucrăm:** 50% la semnare, 50% la livrare (proces-verbal). Specificația scrisă e anexa 1; dacă livrarea nu o respectă, nu plătiți a doua tranșă până nu corectăm. 90 de zile corectări gratuite. Abonament 12 luni, preaviz 30 de zile. Site-ul și conținutul sunt ale dvs. la plata integrală; motorul radar rămâne al nostru, cu licență de utilizare pe durata abonamentului.
> **Ce nu promitem:** poziții în Google sau apariție în răspunsurile AI; că radarul prinde tot (lista surselor e în contract); rezultate de business.
> **Ce facem diferit:** venim la dvs. în Bihor; alertele au link la sursă și sunt verificate de om; nu vindem llms.txt.
> **Pasul următor:** demo de 20 de minute pe datele reale din Bihor → [calendar].

### F.2 Structura contractului + anexa GDPR (clauze; **de revăzut de un avocat**)

**Contract de prestări servicii** [ESTIMARE]
1. Părți, obiect (descriere aliniată cu CAEN 6310: „realizare, publicare și administrare pagini web; prelucrare de date pentru pagina [X]; configurare automatizări legate de site”), anexa 1 = specificația (pagini, funcții, surse radar, profiluri).
2. Preț, facturare, plată: 50% avans la semnare (nerambursabil după începerea lucrului), 50% la livrare; abonament lunar facturat în avans; întârziere la plată → suspendarea abonamentului după 15 zile.
3. Termene și obligațiile clientului: furnizarea materialelor în 10 zile; feedback în 5 zile lucrătoare, altfel etapa se consideră acceptată; interviuri de conținut.
4. Revizii: numărul din pachet; revizii suplimentare la [X] EUR/oră.
5. Recepție: proces-verbal cu URL, checklist din anexa 1, capturi de ecran datate.
6. Garanție: 90 de zile corectări; excluderi (modificări făcute de client, plugin-uri terțe, schimbări la Google).
7. Proprietate intelectuală: site, texte, grafică → clientul, la plata integrală; motorul radar, scripturile, prompturile → prestatorul; licență neexclusivă, netransferabilă, pe durata abonamentului; domeniul și găzduirea pe numele clientului.
8. Abonament: 12 luni, reînnoire automată, preaviz 30 de zile; ce include (ore, găzduire, costuri API); la încetare, export complet al datelor în 30 de zile.
9. Limitarea răspunderii: alertele și paginile sunt informative, nu consultanță juridică/fiscală; prestatorul nu răspunde pentru termene ratate pe baza alertelor; răspundere plafonată la valoarea abonamentului pe 3 luni [de validat cu avocatul].
10. Confidențialitate; referințe (dreptul de a menționa clientul în portofoliu, revocabil).
11. Date cu caracter personal: trimitere la anexa 2.
12. Încetare, forță majoră, lege aplicabilă, soluționarea litigiilor (negociere → instanța de la sediul prestatorului).
13. Clauză de audit: prestatorul păstrează contractul, facturile, dovezile de plată și procesele-verbale 5 ani (pentru verificarea proiectului de finanțare).

**Anexa 2 — Acord de prelucrare a datelor (art. 28 GDPR)** [ESTIMARE]
- Roluri: clientul = operator pentru datele clienților săi finali; ILLUSTRUS = persoană împuternicită.
- Obiect, durată, natură, scop: colectarea cererilor, calificarea, programarea, colectarea documentelor, potrivirea cu apeluri.
- Categorii de persoane și date: reprezentanți ai firmelor, PFA; date de identificare și contact, date din documente încărcate; **fără date speciale**; **fără CNP în prompturile trimise la API**.
- Instrucțiuni documentate; prelucrare doar în scopul contractului.
- Confidențialitate; măsuri de securitate (criptare în tranzit și în repaus, acces pe roluri, jurnal de acces, backup, parole/2FA).
- Subîmputerniciți, cu lista nominală și dreptul de obiecție: găzduire (ex. Romarg/Hostico), Oracle Cloud (regiunea EU), furnizorul API LLM (OpenAI/Google/Anthropic — cont business, fără antrenare pe date), WhatsApp Business API / furnizor e-mail, n8n (self-hosted sau Cloud, EU).
- Transferuri în afara SEE: doar cu clauze contractuale standard; preferă regiuni EU.
- Asistență pentru drepturile persoanelor și pentru evaluările de impact; notificarea încălcărilor în 48 h.
- Retenție: ștergere/restituire la încetare (30 de zile); retenția documentelor încărcate: [X] luni, configurabilă.
- Audit: dreptul operatorului la informații și la audit cu preaviz de 15 zile.
- Jurnal al activităților de prelucrare (art. 30) ținut de ambele părți.

### F.3 Specificația demo-ului de 5 minute [ESTIMARE]

| Minut | Ecran | Date | Flux |
|---|---|---|---|
| 0:00–1:00 | Site-ul ILLUSTRUS pe telefon (pagina FAQ „Ce finanțări sunt deschise pentru IMM-uri din Bihor în 2026?”) și rezultatul Google / Modul AI pentru întrebarea respectivă | Conținut real, FAQPage schema | „Așa arată un site care răspunde la întrebările pe care le pun clienții dvs.” |
| 1:00–2:30 | Formularul de calificare (pe telefonul lor) → în 20 s primesc e-mail: „Cerere calificată: eligibil probabil pentru [program], motiv: CAEN X, județ Y” + link de programare | 3 cazuri pregătite: eligibil, neeligibil, incert | n8n: formular → LLM → e-mail + rând în APEX |
| 2:30–4:00 | Pagina publică „Apeluri deschise Bihor / Nord-Vest” (date reale din MIPE JSON + Regio NV + AFIR, cu „actualizat la [dată-oră]” și link la sursă) → APEX: profilul unui client fictiv („IMM producție mobilă, Oradea, 12 angajați”) → lista alertelor potrivite cu scor → butonul „Aprobă” → WhatsApp/e-mail primit live | ≥ 20 apeluri reale; 3 profiluri; 1 corrigendum recent evidențiat ca „modificat” | Arăți validarea umană explicit: „nimic nu pleacă fără om” |
| 4:00–5:00 | Raportul lunar (PDF, 1 pagină): alerte trimise, apeluri noi, precizie, vizibilitate | Un raport generat pe luna trecută | „Asta primiți lunar. Hai să vedem dacă vi se potrivește” → întrebările de discovery din plan v1 §7.4 |

Reguli: nu arăți cod sau n8n; totul rulează de pe telefon și laptop fără internet de birou (hotspot); ai capturi de rezervă dacă pică API-ul.

### F.4 Calendarul pe 12 săptămâni refăcut (București, 2 drumuri în Bihor + sărbătorile acasă)

Ipoteze: săptămâna 1 = 7–13 oct. 2026; drumurile București–Oradea le faci în weekend (timpul de drum nu e contabilizat; doar orele de întâlniri); sesiunea de iarnă e după săptămâna 12. Plafon: **12 h/săptămână**.

| Săpt. | Construcție (h) | Vânzare (h) | Drumuri Bihor (h întâlniri) | Admin (h) | Total | Ce se întâmplă |
|---|---|---|---|---|---|---|
| 1 (7–13 oct.) | 5: decizii stack, workspace APEX, tabela `SOURCE` cu cele 8 surse-nucleu | 2: schelet listă prospecți (termene.ro, Maps) | 0 | 3: citești decizia de finanțare, trimiți scrisoarea §A.2 la GAL + OJFIR, întrebi contabilul | 10 | |
| 2 (14–20 oct.) | 8: site-ul ILLUSTRUS (5 pagini, GBP, schema) | 2: lista ajunge la 50, calificare | 0 | 1 | 11 | programezi întâlnirile pentru drumul 1 (telefon, nu e-mail) |
| 3 (21–27 oct.) | 3: colector pentru sursa #1 (JSON MIPE) | 2: follow-up-uri | **6: Oradea** (consultantul tău + GAL + 2 discovery; opțional CFO Conference 21 oct.) | 1 | 12 | **Drumul 1** |
| 4 (28 oct.–3 nov.) | 8: extracție AI + tabel APEX + pagina „Apeluri deschise Bihor” | 2: 2 discovery online (București) | 0 | 1 | 11 | |
| 5 (4–10 nov.) | 7: coada de validare + alertă e-mail; set de test (30 elemente) | 3: pregătești GoTech, 1 discovery | 0 | 1 | 11 | |
| 6 (11–17 nov.) | 4: formular de calificare demo | 6: GoTech World 10–11 nov. (3 conversații-țintă) + follow-up | 0 | 1 | 11 | |
| 7 (18–24 nov.) | 6: ofertă PDF + contract + anexa GDPR (din §F) | 4: 2 discovery, prima ofertă scrisă | 0 | 1 | 11 | BRCC Business Days ~24 nov. dacă se confirmă |
| 8 (25 nov.–1 dec.) | 5: corecturi după feedback, demo repetat | 4: 2 oferte, negocieri | 0 | 1 | 10 | **Țintă: 1 ofertă acceptată** |
| 9 (2–8 dec.) | 8: start livrare client 1 (interviuri de conținut, structură) | 2 | 0 | 1 | 11 | **avans 480–960 EUR** |
| 10 (9–15 dec.) | 4: livrare | 2 | **5: Oradea** (kickoff fizic client 1 sau semnare; 2 discovery) | 1 | 12 | **Drumul 2** |
| 11 (16–22 dec.) | 8: livrare (pagini, formular) | 2: cer 2 introduceri | 0 | 1 | 11 | |
| 12 (23–29 dec.) | 4: livrare | 0 | 4: ești acasă de sărbători — 2 întâlniri informale (contabil, consultant) | 2: retrospectivă, ajustări §9 din v1 | 10 | |
| **Total** | **70** | **31** | **15** | **15** | **131** (10,9 h/săpt.) | |

Ce iese la săptămâna 12: site propriu live, demo pe 1–2 surse cu date reale, coadă de validare, ofertă și contract gata, ~21 de discuții, 1 contract semnat (START sau PRO), 480–960 EUR avans încasat, livrarea clientului 1 la 60%. Livrarea se termină în săptămânile 13–15 (ianuarie; atenție la sesiune: lasă 6 h/săptămână în ultimele două săptămâni de ianuarie).

---

## G. Scenariile financiare refăcute

Ipoteze comune [ESTIMARE]: venit = instalare (contabilizată în luna livrării, deși e 50/50) + abonamente (din luna următoare livrării); primele 2 contracte cu −20%; fără TVA; ore = 10 vânzare + 2 admin + construcție motor (demo 25 h în lunile 1–2; motor complet 90 h întins pe 6 luni) + livrări (START 22 h pe 2 luni, PRO 45 h pe 3 luni, RADAR 45 h pe 3 luni după ce motorul există) + abonamente (1,5 / 3 / 5 h pe client-lună). Plafon: 48 h/lună.

### RAPID — 10.000 EUR în luna 13 (probabilitate ~25%)

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 1 | — | 0 | 0 | 0 | 24 |
| 2 | — | 0 | 0 | 0 | 36 |
| 3 | START (pilot) | 960 | 0 | 960 | 38 |
| 4 | — | 0 | 60 | 1.020 | 44 |
| 5 | — | 0 | 60 | 1.080 | 44 |
| 6 | PRO (pilot) | 1.920 | 60 | 3.060 | 44 |
| 7 | — | 0 | 200 | 3.260 | 46 |
| 8 | — | 0 | 200 | 3.460 | 46 |
| 9 | RADAR | 3.500 | 200 | 7.160 | 32 |
| 10 | — | 0 | 480 | 7.640 | 32 |
| 11 | START | 1.200 | 480 | 9.320 | 48 |
| 12 | — | 0 | 540 | 9.860 | 38 |
| **13** | PRO | 2.400 | 540 | **12.800** | 38 |

Abonamente până în luna 13: 2.820 EUR (22%). Fără abonamente: 9.980 EUR în luna 13 → al șaselea contract în luna ~15.

### ECHILIBRAT — 10.000 EUR în luna 14 (probabilitate ~50%)

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 1–3 | motor demo, site propriu, ~21 discuții | 0 | 0 | 0 | 23–24 |
| 4 | START (pilot) | 960 | 0 | 960 | 36 |
| 5–6 | — | 0 | 60 | 1.080 | 41 |
| 7 | PRO (pilot) | 1.920 | 60 | 3.060 | 41 |
| 8–10 | motor complet | 0 | 200/lună | 3.660 | 29–44 |
| 11 | RADAR | 3.500 | 200 | 7.360 | 32 |
| 12–13 | — | 0 | 480/lună | 8.320 | 22–32 |
| **14** | START | 1.200 | 480 | **10.000** | 32 |
| 15 | — | 0 | 540 | 10.540 | 38 |

Abonamente până în luna 14: 2.420 EUR (24%). Fără abonamente: 7.580 EUR în luna 14 → mai e nevoie de un PRO (luna ~17) → 9.980 → și încă un START (luna ~19).

### PRUDENT — 10.000 EUR în luna 17 (probabilitate ~25%)

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 1–4 | motor demo, 0 vânzări în nișa 1 | 0 | 0 | 0 | 12–24 |
| 5 | site local (fallback) | 800 | 0 | 800 | 26 |
| 7 | site local (fallback) | 800 | 40 | 1.680 | 27 |
| 9 | START (pilot) | 960 | 80 | 2.800 | 25 |
| 12 | PRO (pilot) | 1.920 | 140 | 5.140 | 43 |
| 13–16 | motor complet | 0 | 280/lună | 6.260 | 31–46 |
| **17** | RADAR | 3.500 | 280 | **10.040** | 34 |
| 20 | START | 1.200 | 560 | 13.200 | 38 |
| 23 | PRO | 2.400 | 620 | 17.460 | 50 |

Abonamente până în luna 17: 2.060 EUR (21%). Fără abonamente: luna 23. Tot în interiorul celor 3 ani, dar fără rezervă.

### Ce se întâmplă dacă contractul nu recunoaște abonamentele sau avansurile [ESTIMARE]

| Caz | Efect | Ce faci |
|---|---|---|
| Abonamentele nu contează | Pierzi 21–24% din sumă; ai nevoie de 1–2 instalări în plus: rapid luna ~15, echilibrat ~19, prudent ~23 | Facturează abonamentul ca „administrare pagini web” (6311) și cere confirmarea scrisă (întrebarea 5 din scrisoare); dacă tot nu, mută valoarea în instalare (abonament mai mic, instalare mai mare) la clienții noi |
| Avansurile nu contează până la livrare | Nu schimbă suma, doar decalează cu ~1–2 luni; tabelele de mai sus contabilizează deja totul la livrare | Livrează în etape cu procese-verbale parțiale (ex. „site live” înainte de „automatizări”), ca să facturezi și să încasezi pe bucăți recunoscute |
| Se cere „încasat”, nu „facturat” | Decalaj egal cu termenul de plată (15–30 zile) | Termen de plată 10 zile; factura finală emisă la proces-verbal |
| Doar CAEN 6310, iar „creare site” e considerat 6201 | Risc major: instalările nu contează | Formulează obiectul contractului ca „realizare și publicare pagini web + administrare + prelucrare date” și cere în scris confirmarea (întrebarea 4); dacă răspunsul e negativ, adaugă codul CAEN cerut la ONRC înainte de primul contract și întreabă dacă veniturile pe el se recunosc |

Sensibilitate la ore: în toate scenariile luna cea mai încărcată are 44–48 h. Dacă ai sesiune într-o lună de livrare, decalezi livrarea cu 3–4 săptămâni și o spui clientului la semnare.

---

## H. Ce s-a schimbat față de plan v1, și cele 3 decizii din săptămâna asta

**Schimbări:**
1. Oferta pentru contabili: de la „portal + OCR + remindere” (2.200 + 150) la „site + calendar termene per client + remindere + radar fiscal curat” (1.900 + 120), fără OCR; contabilii = în primul rând sursă de recomandări.
2. RADAR se prezintă descompus (2.400 + 1.100) și cu pilot de 30 de zile la 1.100 EUR.
3. Preț de pilot −20% la primii 2 clienți, garanție de specificație pe START, 90 de zile corectări.
4. AEOScore (Vaslui) adăugat ca reper, marcat [DE VERIFICAT]; ghidul Google din mai 2026 (llms.txt inutil) folosit ca argument de vânzare.
5. Calendarul pe 12 săptămâni: 70 h construcție, 31 h vânzare, 15 h întâlniri în Bihor (2 drumuri + sărbători), 15 h admin; 10,9 h/săptămână.
6. Scenariile: 10.000 EUR în luna 13/14/17 (v1: 9/13–14/18–20), cu plafon de 48 h/lună respectat; abonamente 21–24%.
7. Radar: registru de 24 + 12 surse cu URL-uri reale; arhitectură pe API-uri (MIPE JSON, MySMIS APEX, SEDIA) în loc de HTML; colector pe IP românesc rezidențial; schemă de date și 6 fluxuri n8n; set de test și praguri de precizie.
8. DR36: regula de 30% din prima tranșă confirmată prin fragmente din ghidul AFIR; neclaritățile (facturat/încasat, TVA, abonamente, termen, CAEN) puse într-o scrisoare oficială; GAL-urile din Bihor listate.
9. Contactare: tabel pe canale cu precedentul ANSPDCP pentru LinkedIn (NN Asigurări); script de telefon și mesaj de follow-up.
10. Relația cu consultantul care ți-a scris proiectul: reguli de igienă (contract la preț de listă, plată prin bancă, nu primul/singurul client, GAL exclus).

**Cele 3 decizii din săptămâna asta:**
1. **Trimite scrisoarea din §A.2** la GAL și OJFIR Bihor, cu număr de înregistrare, și calculează pragul exact din decizia ta (30% × prima tranșă). Până vine răspunsul, formulează toate contractele ca „realizare și publicare pagini web + administrare + prelucrare date”.
2. **Fixează oferta din §F.1** (1.200 / 2.400 / 3.500, pilot −20% pentru primii 2) și programează prin telefon întâlnirile pentru drumul 1 în Oradea (21–23 octombrie): consultantul tău, GAL-ul, 2 discovery.
3. **Pornește colectorul pe sursa #1** (API JSON MIPE) și pagina „Apeluri deschise Bihor / Nord-Vest” de pe o conexiune din România, ca să ai la drumul 2 (decembrie) un demo cu date reale, nu slide-uri.

---

## Surse

Notele complete, cu toate link-urile și gradul de verificare, sunt în `research_notes/Plan v2 site-uri și automatizări/`. Surse-cheie citate în text:

- DR36: Ghid de implementare DR36 AFIR (Ed. I, Rev. 2) https://stportalafirprod.blob.core.windows.net/media/media/x55l55ql/ghid-implementare-dr_36_editia-i_revizia-2.pdf ; Manual de procedură DR36 Ed. 1 Rev. 1 https://stportalafirprod.blob.core.windows.net/media/media/bw0ppzxa/manual_procedura-implementare-dr-36f-editia-1-revizia-1-fara-track-changes.pdf ; pagina AFIR DR36 https://www.afir.ro/domenii-de-interventie/detalii-si-anexe-dr-36/ ; lista GAL MADR 10.02.2026 https://www.madr.ro/docs/dezvoltare-rurala/Axa_LEADER/2023-2027/2026/Lista-cu-Grupurile-de-Actiune-Locala-2023-2027-selectate-de-MADR-si-datele-de-contact-ale-acestora-actualizata-la-data-de-10.02.2026.pdf ; GAL Crișul Negru https://galcrisulnegru.ro/apeluri-de-selectie-proiecte/ ; ghiduri GAL model: https://www.galpm.ro/wp-content/uploads/2025/08/GhidSolicitant-START-UP-ACTIVITATI-NONAGRICOLE-s.pdf , https://galcampiatransilvaniei.ro/wp-content/uploads/2025/08/Fisa-interventiei.pdf ; sM 6.2 ghid sintetic AFIR 2021 https://portal.afir.info/Uploads/GHIDUL%20Solicitantului/2021_tranzitie/GS%20Sintetic/Ghid-sintetic_sM-6.2__FINAL.pdf
- Concurență contabili: https://platforma.econta.ro/ , https://elevioone.io/resurse/programe-contabilitate-romania-comparatie , https://contera.ro/ , https://finans.ro/preturi , https://www.smartbill.ro/preturi/contabilitate , https://www.oblio.eu/pret-onest , https://www.keez.ro/cabinete-contabilitate , https://taxdome.com/pricing ; monitorizare legislativă: https://lege5.ro/buy , https://demo.sintact.ro/ , https://shop.wolterskluwer.ro/produse/monitorizare-proiecte-legislative,693052.html , https://www.rs.ro/contabilitate-36/abonament-portalcontabilitatero-abonament-12-luni-1959.html ; automatizări: https://www.cosimo.dev/ro/automatizari-n8n , https://webforge.org.ro/en/blog/automatizari-n8n , https://websitefirma.ro/automatizari-firma/ ; piață: https://www.topfirme.com/judet/bihor/caen/6920/
- Prețuri site/AEO: https://visionflow.ro/creare-site-oradea-bihor , https://romediadesign.com/ , https://www.4usconsulting.ro/creare-site-oradea/ , https://www.necesit.ro/creare-site-web/oradea , https://www.cormedia.ro/preturi-realizare-site-de-prezentare/ , https://webdesignagency.ro/pachete/ , https://www.hzone.ro/servicii/creare-site , https://pronetdesign.ro/pret-website/ , https://www.sitto.ro/ , https://automatizez.ro/ , https://sitesos.ro/mentenanta/ , https://webage.ro/mentenanta-site-web/ , https://optimizareai.online/ , https://www.nion.ro/ai-ranking-optimization-aeo-ago-romania , https://aiengineoptim.ro/pachete-de-servicii-seo-geo-aeo/ , https://instatic.ro/servicii-seo , https://aeoscore.eu/ ; Google: https://developers.google.com/search/docs/appearance/ai-features , https://developers.google.com/search/docs/fundamentals/ai-optimization-guide , https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/
- Surse radar finanțări: https://oportunitati-ue.gov.ro/apeluri/ , https://mfe.gov.ro/calendar-apeluri-de-proiecte/ , https://resurse.mysmis2021.gov.ro/ords/repo_bo/r/mysmis-2021/finantari-programe-2021-2027 , https://www.afir.ro/instrumente/sesiuni/sesiuni-primire-proiecte/ , https://gal.afir.ro/ , https://regionordvest.ro/ , https://www.nord-vest.ro/ , https://www.adrbi.ro/programe-regionale/por-bi-2021-2027/ , https://economie.gov.ro/ , https://minimis.imm.gov.ro/ , https://energie.gov.ro/category/fondul-pentru-modernizare/ , https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/apis ; proiecte open-source citate: https://github.com/TudorAndrei/registru-fonduri-ue , https://github.com/florincaciur/atelierdeconsultanta , https://github.com/caba12345/oradea-news , https://github.com/aborruso/opencli
- Surse radar fiscal/SSM: https://monitoruloficial.ro/ , https://legislatie.just.ro/ , http://legislatie.just.ro/ServiciulWebLegislatie.htm , https://github.com/govro/legislatie-just-python-soap-client , https://static.anaf.ro/static/10/Anaf/Legislatie_R/noutati_legislative.htm , https://folositor.ro/radar-fiscal , https://www.inspectiamuncii.ro/ , https://www.senat.ro/pagini/poca/2023-12-21/Pliant_12_2023_web.pdf ; Legea 57/2021: https://www.fiscalitatea.ro/acces-gratuit-la-toata-legislatia-vezi-in-ce-conditii-2856/
- Evenimente și contactare: https://business-mark.ro/event/cfo-conference-oradea-2026/ , https://www.gotech.world/event-details/2026-gotech-world , https://brcconline.eu/bucuresti-business-days/ , https://spotmedia.ro/stiri/economie/190-de-antreprenori-si-manageri-din-bihor-si-din-judetele-invecinate-au-participat-la-conferinta-business-evolution-finantare-digitalizare-sustenabilitate-de-la-oradea , https://profit.ro/taxe-si-consultanta/asociatia-consultantilor-pentru-accesarea-fondurilor-europene-avanseaza-masuri-de-simplificare-a-procesului-de-gestiune-a-programelor-de-finantare-din-bani-ue-18537884 (ACRAFE) ; Legea 506/2004: https://legislatie.just.ro/Public/DetaliiDocument/57058 ; sancțiuni: https://profit.ro/legal/retrospectiva-anului-2025-din-prisma-sanctiunilor-aplicate-pentru-incalcarea-legislatiei-privind-protectia-datelor-22372249 , https://profit.ro/stiri/nn-asigurari-de-viata-liderul-de-profil-a-fost-sanctionat-pentru-trimiterea-de-mesaje-prin-mesageria-linkedin-21320206 , https://startupcafe.ro/gdpr-in-romania-dezvoltatorul-roman-de-imobiliare-one-united-properties-amenda-pentru-mesaje-nesolicitate-78901 ; EDPB Ghid 1/2024 (comentariu): https://www.morganlewis.com/blogs/sourcingatmorganlewis/2024/10/gdpr-when-can-data-controllers-rely-on-legitimate-interests-for-data-processing-new-guidelines-from-the-edpb ; ONRC tarife liste: https://www.capital.ro/registrul-comertului-comaseaza-tarife-si-scade-pretul-la-jumatate.html
