# C2 – Surse oficiale pentru „radar legislativ” fiscal-contabil și SSM/PSI (România, octombrie 2026)

> **Notă metodologică importantă (citiți înainte de a folosi tabelul).** În această sesiune, proxy-ul de rețea a blocat accesul direct la TOATE domeniile `.ro` (monitoruloficial.ro, legislatie.just.ro, anaf.ro, static.anaf.ro, mfinante.gov.ro, inspectiamuncii.ro, mmuncii.ro, igsu.ro, cdep.ro, senat.ro, lege5.ro, legis.ro, shop.wolterskluwer.ro, avocatnet.ro, contzilla.ro etc.) și la web.archive.org. Prin urmare **nu am putut citi niciun `robots.txt`, nicio pagină „Termeni și condiții” și niciun flux RSS direct**. Tot ce urmează provine din (a) rezultate de căutare (titluri/URL-uri/fragmente indexate), (b) pagini de pe domenii ne-românești accesibile (github.com), (c) articole secundare citate în rezultate. Fiecare URL este marcat astfel:
> - **[V]** = URL-ul a apărut ca atare într-un rezultat de căutare (există, dar conținutul nu a fost citit integral);
> - **[N]** = URL „din memorie”/dedus din structura site-ului, **neverificat** în această sesiune – trebuie confirmat manual înainte de a fi pus în producție;
> - **nu am găsit** = nicio sursă.
> Recomand ca prima iterație a radarului să includă un script simplu care descarcă `robots.txt` + pagina de termeni pentru fiecare domeniu din tabel și le arhivează (dovadă de bună-credință).

---

## Întrebarea 1: Tabelul surselor de monitorizat (8–12 surse)

### Takeaway
Pentru un radar fiscal + SSM/PSI există două „coloane vertebrale” gratuite și re-utilizabile legal: **Monitorul Oficial (e-Monitor, PDF gratuit din ziua publicării, Legea 57/2021)** și **legislatie.just.ro (HTML + serviciu web SOAP, date fără drept de autor)**. În jurul lor, ANAF (buletin „Noutăți legislative” + fluxuri RSS), Parlamentul (cdep.ro/senat.ro, cu flux RSS la Senat pentru consultare publică) și paginile de transparență ale ministerelor (MF, MMSS, MAI/IGSU) acoperă „ce urmează”. Accesul automat nu a putut fi verificat la nivel de robots.txt/termeni – aceasta rămâne principala necunoscută.

### Tabel

| # | Sursă / URL de monitorizat | Ce publică | Format | Frecvență | RSS / API / newsletter oficial | Restricții acces (robots.txt, CAPTCHA, termeni) | Dificultate parsare | Prioritate |
|---|---|---|---|---|---|---|---|---|
| 1 | **Monitorul Oficial – e-Monitor** – `https://monitoruloficial.ro/` [V, domeniu] ; secțiunea e-Monitor: `https://monitoruloficial.ro/e-monitor/` [N] | Partea I (legi, OUG, HG, ordine ANAF/MF/MMSS/MAI etc.) și Partea II, în ziua publicării; PDF per ediție (număr de MO), fără filigran | PDF (căutabil), site WordPress (vezi `https://monitoruloficial.ro/wp-content/uploads/2025/03/raaaip2024.pdf` [V] – confirmă CMS WordPress) | Zilnic, în zilele lucrătoare; mai multe ediții/zi posibile | **nu am găsit** RSS/API oficial; baza de date plătită „Expert Monitor”: `http://www.expert-monitor.ro/expert-monitor/` [V] | robots.txt / termeni: **neverificat** (blocat). Legea 57/2021 permite expres căutarea, salvarea, distribuirea și tipărirea formatului electronic gratuit (vezi Î2) | Medie: PDF per ediție (nu per act) ⇒ trebuie split pe acte după sumar; OCR nu e necesar (PDF text) | **1 (critică)** – sursa de adevăr pentru „a intrat în vigoare / a fost publicat” |
| 2 | **Portal Legislativ (Ministerul Justiției)** – `https://legislatie.just.ro/` [V]; act: `https://legislatie.just.ro/Public/DetaliiDocument/{id}` [V]; afișare: `https://legislatie.just.ro/Public/DetaliiDocumentAfis/{id}` [V, ex. 136599] | Text consolidat al actelor normative, metadate (tip, număr, dată, MO), legături între acte | HTML + **serviciu web SOAP** (`http://legislatie.just.ro/ServiciulWebLegislatie.htm` [V]) | Actualizat continuu după publicarea în MO (de regulă aceeași zi/ziua următoare – de verificat) | **API SOAP oficial** (vezi Î3); client Python: `https://github.com/govro/legislatie-just-python-soap-client` [V]; RSS: **nu am găsit** | robots.txt / termeni: **neverificat**. Index OKFN 2015 + scraper Apify afirmă: fără autentificare, fără anti-bot, date fără drept de autor (vezi Î3) | Mică–medie: ID numeric incremental + SOAP cu căutare pe an/cuvânt; HTML-ul articolelor e structurat | **1 (critică)** – pentru text consolidat și diff între versiuni |
| 3 | **ANAF – Buletin „Noutăți legislative”** – `https://static.anaf.ro/static/10/Anaf/Legislatie_R/noutati_legislative.htm` [V] ; arhivă: `https://static.anaf.ro/static/10/Anaf/legislatie/arhiva2019_noutati_legislative.htm` [V] | Buletin săptămânal cu actele cu incidență fiscală publicate în MO (ex. „buletin nr. 25 din 20 iulie 2026”) | HTML static (`static.anaf.ro`) cu link-uri (PDF/HTML) | Săptămânal (numerotat: nr. 25 la 20 iulie 2026 ⇒ ~1/săpt.) | Fluxuri RSS ANAF există (confirmate indirect de folositor.ro, vezi Î4); index RSS: `https://www.anaf.ro/anaf/internet/ANAF/rss` [N]; exemplu flux pe static: `https://static.anaf.ro/static/10/Anaf/Informatii_R/rss_valorif_bunuri.htm` [V] | robots.txt: **neverificat**. Server static, fără login | Mică (HTML static, structură repetitivă) | **1** – rezumatul oficial al săptămânii fiscale |
| 4 | **ANAF – Calendar obligații fiscale** – `https://www.anaf.ro/anaf/internet/ANAF/asistenta_contribuabili/calendar_obligatii_fiscale` [N] ; portal: `https://www.anaf.ro/` [V] | Termene lunare de declarare/plată | HTML (portal Liferay-like) / PDF lunar | Lunar | nu am găsit RSS dedicat | **neverificat** | Medie (portal dinamic) | 2 |
| 5 | **ANAF – Proiecte de acte normative (transparență) + Ghiduri + e-Factura/SPV** – `https://www.anaf.ro/anaf/internet/ANAF/despre_anaf/transparenta_decizionala/proiecte_acte_normative` [N]; ghiduri: `https://static.anaf.ro/static/10/Anaf/AsistentaContribuabili_r/` [V, ex. `Ghid_e_factura_2024.pdf`] | Proiecte de ordine ANAF, ghiduri, comunicate, informări SPV/e-Factura | HTML + PDF pe `static.anaf.ro` | Neregulat (zilnic–săptămânal) | RSS „comunicate de presă / ghiduri / acte administrative / noutăți” – confirmate de folositor.ro (URL-uri exacte **nu am găsit**) | **neverificat** | Medie | 2 |
| 6 | **Ministerul Finanțelor – Transparență decizională** – `https://mfinante.gov.ro/` [V, domeniu]; pagina: `https://mfinante.gov.ro/ro/transparenta-decizionala` [N] | Proiecte de OUG/HG/ordine MF (Cod fiscal, Cod procedură fiscală, contabilitate), note de fundamentare | HTML + PDF/DOC | Neregulat (săptămânal) | **nu am găsit** RSS/API | **neverificat** | Medie–mare (documente DOC/PDF, denumiri neuniforme) | 2 – „early warning” fiscal |
| 7 | **Inspecția Muncii** – `https://www.inspectiamuncii.ro/` [V]; documente: `https://www.inspectiamuncii.ro/documents/{groupId}/{folderId}/{nume}.pdf/{uuid}` [V, structură Liferay, ex. „Comunicat rezultate saptamanale 18-22 mai 2026”]; legislație SSM: `https://www.inspectiamuncii.ro/legislatie` [N] | Comunicate săptămânale, campanii de control, legislație SSM/relații de muncă, rapoarte anuale | Liferay (HTML) + PDF | Săptămânal (comunicate) | **nu am găsit** RSS | **neverificat** | Medie (URL-uri Liferay cu UUID, greu de enumerat; util pentru text, nu pentru listare) | 2 (SSM) |
| 8 | **Ministerul Muncii (MMSS)** – `https://mmuncii.ro/` [V, domeniu]; transparență: `https://mmuncii.ro/j33/index.php/ro/transparenta/proiecte-in-dezbatere` [N] | Proiecte HG/ordine SSM (modificări HG 1425/2006, Legea 319/2006), legislație muncii | HTML (Joomla) + PDF | Neregulat | **nu am găsit** RSS | **neverificat** | Medie–mare | 2 (SSM) |
| 9 | **IGSU / MAI – PSI** – `https://www.igsu.ro/` [V, domeniu]; legislație: `https://www.igsu.ro/Resources/Legislatie` [N]; transparență MAI: `https://www.mai.gov.ro/transparenta-decizionala/` [N] | Legea 307/2006, OMAI 163/2007 și modificări, norme tehnice, proiecte MAI | HTML + PDF | Rar (lunar–trimestrial) | **nu am găsit** RSS | **neverificat** | Medie | 3 (PSI) |
| 10 | **Camera Deputaților** – `https://www.cdep.ro/` [V]; căutare proiecte: `https://www.cdep.ro/pls/proiecte/upl_pck2015.home` [N]; ordinea de zi (Oracle ORDS): `https://www.cdep.ro/ords/co/sedinte.ordinezi?ids=13483` [V] | Proiecte de lege, fișe, stadiu, ordinea de zi | HTML (Oracle PL/SQL + ORDS) + PDF | Zilnic în sesiune | RSS/XML open data: **nu am găsit** (site-ul vechi avea pagini PL/SQL; există endpoint ORDS, deci API intern probabil, nedocumentat) | **neverificat** | Mare (parametri Oracle, HTML tabelar vechi) | 3 |
| 11 | **Senat** – `https://www.senat.ro/` [V]; fișă proiect: `https://www.senat.ro/Legis/Lista.aspx?cod=27496` [V]; PDF-uri proiecte: `https://senat.ro/legis/PDF/2021/21L412FS.pdf` [V] | Propuneri legislative, proiecte în consultare publică, buletin legislativ pe sesiune (PDF, ex. `https://www.senat.ro/UploadFisiere\03db55c6-7e90-43cc-97f5-b9907c26bbd7\Buletin legislativ sesiunea II 2025.pdf` [V]) | ASP.NET (HTML) + PDF | Zilnic în sesiune | **Flux RSS „pentru consultarea publică a inițiativelor legislative”** – menționat în pliantul oficial POCA `https://www.senat.ro/pagini/poca/2023-12-21/Pliant_12_2023_web.pdf` [V]; URL-ul fluxului **nu am găsit** | **neverificat** | Medie (ASP.NET, cod numeric `cod=`) | 3 |
| 12 | **SGG – consultare.gov.ro / ședințe de guvern** – `https://sgg.gov.ro/` [V, domeniu]; `https://consultare.gov.ro/` [N, menționat ca angajament OGP: `https://www.opengovpartnership.org/fr/members/romania/commitments/RO0035/` [V]) | Proiecte de acte normative ale ministerelor centralizate; ordinea de zi a ședințelor de guvern | HTML + PDF | Săptămânal (ședințe) | **nu am găsit** | **neverificat** | Medie | 3 |

**Surse secundare utile (nu oficiale, dar gratuite) pentru validare încrucișată:** `https://folositor.ro/radar-fiscal` [V] (agregator RSS ANAF, vezi Î4), `https://www.contzilla.ro/` [V] (newsletter zilnic gratuit, >20.000 abonați), `https://contabilul.manager.ro/` [V] și `https://www.fiscalitatea.ro/` [V] (portaluri editoriale, aparent din grupul Rentrop & Straton – neconfirmat oficial).

### Cited Findings
- Legea nr. 57/2021 a modificat art. 18 din Legea nr. 202/1998: formatul electronic al Monitorului Oficial, Partea I și Partea a II-a, este disponibil gratuit și permanent, „în format portabil, fără filigran sau înscrisuri suplimentare”, accesibil tuturor „în aceeași zi cu publicarea, inclusiv pentru căutare, salvare, distribuire și tipărire”; legea a fost publicată în MO nr. 337 din 2 aprilie 2021 — [contabilul.manager.ro](https://contabilul.manager.ro/a/25772/actele-normative-publicate-in-monitorul-oficial-vor-putea-fi-descarcate-gratuit.html); [economica.net](https://www.economica.net/monitorul-oficial-devine-gratuit-la-publicare-copiere-reproducere_502513.html); [e-juridic.manager.ro](https://e-juridic.manager.ro/articole/monitorul-oficial-e-monitor-va-fi-gratuit-27297.html); [profit.ro](https://profit.ro/stiri/politic/monitorul-oficial-obligat-sa-publice-gratuit-legile-si-alte-acte-oficiale-in-format-pdf-19468428)
- Serviciul gratuit se numește **e-Monitor**; directorul RA Monitorul Oficial (Liviu Moraru) a declarat că toate legile vor putea fi citite „în format PDF portabil, gratuit, de pe site” — [bzi.ro](https://www.bzi.ro/monitorul-oficial-va-fi-disponibil-gratuit-in-format-pdf-liviu-moraru-directorul-mo-toate-legile-vor-putea-fi-citite-pe-calculatorul-dumneavoastra-4159726); [alba24.ro](https://alba24.ro/monitorul-oficial-va-fi-accesibil-gratuit-integral-online-noul-format-va-permite-inclusiv-cautarea-in-interiorul-documentelor-831032.html)
- Baza de date comercială a RA MO este „Expert Monitor” (`http://www.expert-monitor.ro/expert-monitor/`), distinctă de e-Monitor — [Publications Office EU, forum Romania OJ](https://op.europa.eu/en/web/forum/romania-oj)
- RA „Monitorul Oficial” funcționează din 28 iulie 2018 sub autoritatea Camerei Deputaților — [avocatnet.ro](https://www.avocatnet.ro/articol_29476/Monitorul-Oficial-se-afla-de-sambata-sub-autoritatea-Guvernului.html) (articol mai vechi despre trecerea la Guvern; schimbarea din 2018 apare în rezultate [data.gov.ro search])
- ANAF publică buletinul „Noutăți legislative” numerotat (ex. „buletin nr. 25 din 20 iulie 2026”) la `static.anaf.ro/static/10/Anaf/Legislatie_R/noutati_legislative.htm` — [ANAF (titlu indexat)](https://static.anaf.ro/static/10/Anaf/Legislatie_R/noutati_legislative.htm)
- Pe site-ul ANAF, secțiunea „Asistență contribuabili” include calendarul obligațiilor fiscale lunare — [ANAF Ploiești, servicii_anaf.pdf](https://static.anaf.ro/static/10/Ploiesti/servicii_anaf.pdf)
- Ghidul e-Factura este publicat ca PDF pe `static.anaf.ro` — [Ghid_e_factura_2024.pdf](https://static.anaf.ro/static/10/Anaf/AsistentaContribuabili_r/Ghid_e_factura_2024.pdf)
- Inspecția Muncii publică comunicate săptămânale ca PDF în structură Liferay `/documents/{id}/{id}/{nume}.pdf/{uuid}` — [inspectiamuncii.ro, comunicat 18–22 mai 2026](https://www.inspectiamuncii.ro/documents/66402/268210/Comunicat+rezultate+saptamanale+18-22+mai+2026.pdf/a9180589-f386-4759-bd5e-0c2890dadda8)
- Camera Deputaților expune pagini Oracle ORDS (`/ords/co/sedinte.ordinezi?ids=…`) — [cdep.ro](https://www.cdep.ro/ords/co/sedinte.ordinezi?ids=13483); presa a semnalat probleme la noul site (contract 4 mil. lei) — [cotidianul.ro](https://www.cotidianul.ro/upgradare-cu-bucluc-la-camera-deputatilor-4-milioane-de-lei-pentru-un-site-care-da-rateuri-in-cascada/)
- Senatul: fișe de proiect `Legis/Lista.aspx?cod=…`, PDF-uri în `/legis/PDF/{an}/…` și „Buletin legislativ” pe sesiune în PDF — [senat.ro Lista.aspx](https://www.senat.ro/Legis/Lista.aspx?cod=27496); [Buletin legislativ sesiunea II 2025](https://www.senat.ro/UploadFisiere\03db55c6-7e90-43cc-97f5-b9907c26bbd7\Buletin legislativ sesiunea II 2025.pdf)
- Senatul oferă un „Flux pentru consultarea publică a inițiativelor legislative” (RSS), parte a proiectului de digitalizare POCA — [Pliant POCA senat.ro](https://www.senat.ro/pagini/poca/2023-12-21/Pliant_12_2023_web.pdf)
- România și-a asumat (OGP) publicarea centralizată a proiectelor de acte normative pe portalul unic Consultare.Gov.Ro — [opengovpartnership.org](https://www.opengovpartnership.org/fr/members/romania/commitments/RO0035/)
- Cadrul legal SSM/PSI de urmărit: Legea 319/2006 (MMSS elaborează proiectele, Inspecția Muncii controlează) și Legea 307/2006 + Normele generale din 28.02.2007 (OMAI 163/2007) — [rubinian.com](https://www.rubinian.com/legea-319-2006-a-securitatii-si-sanatatii-in-munca-capitolul-10); [e-juridic.manager.ro](https://e-juridic.manager.ro/articole/respectarea-normelor-psi-obligatii-legale-si-consecinte-30271.html); punct focal EU-OSHA România: [osha.europa.eu](https://osha.europa.eu/ro/about-eu-osha/national-focal-points/romania)

### Inferences
- Pentru „ce a intrat în vigoare” combinația **MO (PDF ediție) → legislatie.just.ro (ID act, text consolidat)** este suficientă și legal curată; ANAF „Noutăți legislative” este un filtru fiscal gata făcut (săptămânal) care reduce zgomotul.
- Pentru „ce urmează” (proiecte), paginile de transparență ale MF/MMSS/MAI nu au RSS și au structuri eterogene ⇒ monitorizare prin hash-uri de pagină + diff, cu o toleranță la fals-pozitive; Senatul este singura instituție parlamentară cu RSS confirmat.
- Site-urile folosesc CMS-uri diferite (WordPress la MO, Liferay la Inspecția Muncii, Oracle PL/SQL+ORDS la CDEP, ASP.NET la Senat, server static la ANAF) ⇒ fiecare adaptor va fi separat; cele statice (static.anaf.ro) sunt cele mai stabile.

### Gaps
- **robots.txt și termenii de utilizare** pentru toate cele 12 domenii: imposibil de citit (acces blocat). Trebuie verificate manual: `https://monitoruloficial.ro/robots.txt`, `https://legislatie.just.ro/robots.txt`, `https://www.anaf.ro/robots.txt`, `https://static.anaf.ro/robots.txt`, `https://mfinante.gov.ro/robots.txt`, `https://www.inspectiamuncii.ro/robots.txt`, `https://mmuncii.ro/robots.txt`, `https://www.igsu.ro/robots.txt`, `https://www.cdep.ro/robots.txt`, `https://www.senat.ro/robots.txt`.
- URL-ul exact al secțiunii e-Monitor și dacă există o pagină-index pe zi / pe număr de MO: nu am găsit (doar confirmarea că PDF-urile sunt per ediție, fără filigran).
- URL-urile exacte ale fluxurilor RSS ANAF: nu am găsit (există, conform folositor.ro).
- Paginile exacte MF transparență, MMSS proiecte, IGSU legislație: nu am găsit URL-uri în rezultate; cele marcate [N] sunt deduse.

---

## Întrebarea 2: Monitorul Oficial – ce este gratuit și „machine-readable” după Legea 57/2021; termeni privind descărcarea automată

### Takeaway
Din 2021, Partea I și a II-a sunt gratuite, permanente, PDF fără filigran, din ziua publicării, cu drept explicit de căutare/salvare/distribuire/tipărire. Nu am găsit nicio prevedere publică care să interzică descărcarea automată, dar nici termeni de utilizare citiți direct; nu există API/RSS oficial cunoscut.

### Cited Findings
- Textul legal (Legea 57/2021, art. 18 L.202/1998 modificat): format electronic „gratuit și deschis permanent… în format portabil, fără filigran sau înscrisuri suplimentare… accesibil tuturor utilizatorilor în aceeași zi cu publicarea, inclusiv pentru căutare, salvare, distribuire și tipărire” — [fiscalitatea.ro](https://www.fiscalitatea.ro/acces-gratuit-la-toata-legislatia-vezi-in-ce-conditii-2856/); [e-juridic.manager.ro](https://e-juridic.manager.ro/articole/monitorul-oficial-e-monitor-va-fi-gratuit-27297.html)
- Expunerea de motive / fișa proiectului (L534/2020) este pe senat.ro — [20L534EM.pdf](https://senat.ro/legis/PDF\2020\20L534EM.pdf); [20L534LG.pdf](https://senat.ro/legis/PDF\2020\20L534LG.pdf)
- Economica: legea promulgată – „Monitorul Oficial în format electronic – disponibil gratuit permanent” — [economica.net](https://www.economica.net/lege-promulgata-monitorul-oficial-in-format-electronic-disponibil-gratuit-permanent_501962.html)
- Monitorul Oficial publică rapoarte anuale ca PDF pe WordPress (`/wp-content/uploads/…`) — [raaaip2024.pdf](https://monitoruloficial.ro/wp-content/uploads/2025/03/raaaip2024.pdf)
- Tarifele și procedura de publicare (pentru cei care publică, nu pentru cititori) — [e-juridic.manager.ro](https://e-juridic.manager.ro/articole/monitorul-oficial-al-romaniei-procedura-si-tarife-de-publicare-30444.html)

### Inferences
- „Distribuire” explicit permisă de lege ⇒ re-publicarea PDF-ului/extraselor în radar este în litera legii; totuși e prudent să se citeze sursa și numărul MO.
- Lipsa API ⇒ monitorizarea se face prin pagina de listare a edițiilor (de identificat) + descărcare PDF; dimensiunea zilnică este mică (câteva PDF-uri/zi).

### Gaps
- Termenii de utilizare ai monitoruloficial.ro (dacă există o clauză anti-scraping sau de „uz personal”): **nu am putut citi**.
- Dacă există un index JSON/HTML pe zi (ex. listare ediții din data X): **nu am găsit**.

---

## Întrebarea 3: legislatie.just.ro – structură URL, API, RSS, termeni

### Takeaway
Portalul MJ (lansat 12 nov. 2014) are URL-uri cu ID numeric (`/Public/DetaliiDocument/{id}`) și un serviciu web SOAP documentat la `ServiciulWebLegislatie.htm`, folosit de un client Python open-source pentru descărcare în masă; surse terțe afirmă că datele nu sunt protejate de drept de autor și că nu există anti-bot. RSS/„ultimele acte”: nu am găsit.

### Cited Findings
- Portalul a fost lansat de Ministerul Justiției pe 12 noiembrie 2014, cu acces gratuit la toată legislația, „prin interfața web sau prin API”; „prin lege, datele nu sunt protejate de drept de autor și pot fi reutilizate fără restricții” — [Open Knowledge Index 2015, Romania/Legislation](https://2015.index.okfn.org/place/romania/legislation/); [discuss.okfn.org](https://discuss.okfn.org/t/entry-for-national-laws-romania/4218)
- Instrucțiuni de descărcare în masă: `http://legislatie.just.ro/ServiciulWebLegislatie.htm`; client SOAP Python (suds, MIT), cu exemple de căutare după an și cuvânt în titlu și descărcare paralelă a întregii baze — [github.com/govro/legislatie-just-python-soap-client](https://github.com/govro/legislatie-just-python-soap-client)
- Structura URL `https://legislatie.just.ro/Public/DetaliiDocument/{id}` (ex. 171282) și câmpuri extrase: id, title, docType, number, date, publishedIn, articleCount, articles[] — [Apify „Romanian Legislation Scraper”](https://apify.com/ponderable_hydrometer/romanian-legislation-scraper); pagina de afișare `DetaliiDocumentAfis/136599` — [legislatie.just.ro](https://legislatie.just.ro/Public/DetaliiDocumentAfis/136599)
- Un server MCP terț („romanian-law-mcp”, Ansvar Systems) afirmă că portalul nu cere autentificare și nu are restricții anti-bot — [playbooks.com](https://playbooks.com/mcp/ansvar-systems/romanian-law-mcp); [glama.ai](https://glama.ai/mcp/servers/epjge9se19) (afirmații ale terților, neverificate pe site)

### Inferences
- Pentru radar: interogare SOAP periodică „acte publicate în intervalul [ieri, azi]” (dacă metoda există – clientul arată căutare pe an + cuvânt; filtrarea pe dată trebuie testată), fallback: crawl incremental pe ID-uri noi.
- Art. 9 lit. b) din Legea 8/1996 (textele oficiale de natură legislativă nu beneficiază de protecția dreptului de autor) este baza afirmației OKFN; nu am citit textul în această sesiune ⇒ de citat din legislatie.just.ro la implementare.

### Gaps
- robots.txt, termeni, limite de rată, disponibilitatea actuală (2026) a serviciului SOAP: **neverificate**.
- Pagină „ultimele acte”/RSS: **nu am găsit**.

---

## Întrebarea 4: ANAF – pagini și RSS

### Takeaway
ANAF are buletin săptămânal „Noutăți legislative” pe `static.anaf.ro` (HTML static) și fluxuri RSS oficiale pe categorii (comunicate, ghiduri, acte administrative, noutăți) – confirmate indirect printr-un agregator terț (folositor.ro „Radar fiscal”) care le consumă la fiecare 2 ore; URL-urile RSS exacte nu au putut fi extrase.

### Cited Findings
- Buletin „Noutăți legislative” nr. 25 din 20 iulie 2026 și seria din 2026 (începând cu 14 ianuarie 2026) — [static.anaf.ro noutati_legislative.htm](https://static.anaf.ro/static/10/Anaf/Legislatie_R/noutati_legislative.htm); arhivă 2019 — [arhiva2019_noutati_legislative.htm](https://static.anaf.ro/static/10/Anaf/legislatie/arhiva2019_noutati_legislative.htm)
- Buletinele ANAF sunt republicate de presa de specialitate (ex. „Buletin ANAF: noutăți legislative cu incidență fiscală în perioada…”) — [contabilul.manager.ro](https://contabilul.manager.ro/a/19849/buletin-anaf-noutati-legislative-cu-incidenta-fiscala-in-perioada-5-11-decembrie-2016.html)
- folositor.ro „Radar fiscal”: agregă „exclusiv din fluxurile RSS oficiale ale ANAF (anaf.ro)” comunicate de presă, ghiduri fiscale, acte administrative și noutăți generale, „actualizare automată la maximum 2 ore”, afișând titlul oficial și linkul, fără interpretare — [folositor.ro/radar-fiscal](https://folositor.ro/radar-fiscal)
- Exemplu de pagină RSS ANAF pe serverul static (valorificare bunuri) — [rss_valorif_bunuri.htm](https://static.anaf.ro/static/10/Anaf/Informatii_R/rss_valorif_bunuri.htm)
- Biblioteci terțe pentru API-urile e-Factura/SPV (nu pentru știri): [anafpy](https://anafpy.readthedocs.io/en/latest/library/efactura/), [AnafIntegration (NuGet)](https://www.nuget.org/packages/AnafIntegration), [ediconnect.ro – SPV](https://www.ediconnect.ro/en/e-invoice/anaf-spv)

### Inferences
- Există deja un concurent gratuit minimal (folositor.ro) care face exact „agregare RSS ANAF” ⇒ radarul trebuie să adauge valoare peste simpla agregare (clasificare pe tip de client, termene, impact SSM/fiscal, diff pe text).
- `static.anaf.ro` fiind un server static, riscul de CAPTCHA/WAF este mic; `www.anaf.ro` (portal) e mai probabil protejat.

### Gaps
- Lista URL-urilor RSS ANAF (pagina index): **nu am găsit** în rezultate; `https://www.anaf.ro/anaf/internet/ANAF/rss` este [N].
- Pagina „Proiecte de acte normative” ANAF și pagina de știri SPV/e-Factura: URL exact **nu am găsit**.

---

## Întrebarea 5: Ministerul Finanțelor, Inspecția Muncii, Ministerul Muncii, IGSU – pagini și format

### Takeaway
Nu am reușit să confirm URL-urile exacte ale paginilor de transparență/legislație ale MF, MMSS și IGSU (blocate și neindexate în rezultate); Inspecția Muncii publică PDF-uri în structură Liferay. Nicio sursă RSS găsită pentru aceste instituții.

### Cited Findings
- MF este menționat ca sursă oficială pentru e-Factura alături de anaf.ro — [fiscal-requirements.com](https://www.fiscal-requirements.com/news/1254-romanian-anaf-launches-the-mobile-application-and-introduces-new-electronic-services-in-spv-for-taxpayers)
- Inspecția Muncii: raport anual 2019 și comunicate săptămânale 2026 ca PDF Liferay — [rapanual2019.pdf](https://www.inspectiamuncii.ro/documents/825609/23820040/rapanual2019.pdf/817c8a99-9793-4972-a8ff-f4ccdfcc34aa); [comunicat mai 2026](https://www.inspectiamuncii.ro/documents/66402/268210/Comunicat+rezultate+saptamanale+18-22+mai+2026.pdf/a9180589-f386-4759-bd5e-0c2890dadda8)
- Rolurile instituționale SSM: MMSS elaborează proiecte, Inspecția Muncii controlează — [rubinian.com, L.319/2006 cap. X](https://www.rubinian.com/legea-319-2006-a-securitatii-si-sanatatii-in-munca-capitolul-10)
- Alte ministere publică rapoarte anuale de transparență (L.52/2003) ca PDF (exemplu de format) — [mmediu.ro](https://mmediu.ro/storage/2025/07/RAPORT-ANUAL-PRIVIND-TRANSPARENTA-DECIZIONALA-MMAP-2024.pdf); [edu.ro](https://edu.ro/sites/default/files/_fi%C8%99iere/Minister/2023/Transparenta/rapoarte_diverse/Raport_ME_2022_L52_2003_v1.pdf)

### Inferences
- Legea 52/2003 obligă toate ministerele să afișeze proiectele în secțiunea de transparență decizională ⇒ paginile există, dar au nume/URL-uri diferite; se recomandă identificare manuală + monitorizare prin diff.

### Gaps
- URL-uri exacte MF/MMSS/IGSU/MAI transparență: **nu am găsit**.
- Pentru PSI, sursa primară rămâne MO + legislatie.just.ro (OMAI); igsu.ro pare a avea doar pagini informative, neconfirmat.

---

## Întrebarea 6: Parlament (cdep.ro, senat.ro) – urmărirea proiectelor, RSS/open data

### Takeaway
cdep.ro are pagini PL/SQL vechi și un nou strat Oracle ORDS, fără RSS/open data documentat găsit; senat.ro are fișe `Lista.aspx?cod=`, PDF-uri, buletine legislative și un flux RSS pentru consultare publică (menționat oficial, URL negăsit).

### Cited Findings
- cdep.ro ORDS: `https://www.cdep.ro/ords/co/sedinte.ordinezi?ids=13483` — [cdep.ro](https://www.cdep.ro/ords/co/sedinte.ordinezi?ids=13483)
- senat.ro: `Legis/Lista.aspx?cod=27496`, PDF-uri `/legis/PDF/{an}/{cod}{tip}.pdf` (ex. 21L412FS/FG), buletine legislative pe sesiune — [senat.ro](https://www.senat.ro/Legis/Lista.aspx?cod=27496); [21L412FS.pdf](https://senat.ro/legis/PDF/2021/21L412FS.pdf); [Buletin legislativ sesiunea I 2023](https://new.senat.ro/UploadFisiere\03db55c6-7e90-43cc-97f5-b9907c26bbd7\Buletin legislativ sesiunea I 2023.pdf)
- Flux RSS Senat pentru consultarea publică a inițiativelor — [Pliant POCA 2023](https://www.senat.ro/pagini/poca/2023-12-21/Pliant_12_2023_web.pdf)
- Senatul publică „Opiniile persoanelor interesate asupra propunerilor legislative aflate în consultare publică” pe fișa fiecărui proiect — [senat.ro Lista.aspx](https://www.senat.ro/Legis/Lista.aspx?cod=27496)

### Inferences
- Pentru radar, Parlamentul este prioritate 3: proiectele relevante fiscal ajung oricum în MO; valoarea e în „alertă timpurie” pentru clienți mari.

### Gaps
- RSS/XML cdep.ro: **nu am găsit**. URL flux RSS senat.ro: **nu am găsit**.

---

## Întrebarea 7: Servicii plătite de monitorizare legislativă – ce oferă și cât costă

### Takeaway
Piața are trei baze de date juridice mari (Lege5/Indaco, Sintact/Wolters Kluwer, Legis/CTCE) cu prețuri de la ~67 lei/lună (Lege5 legislație, 1 cont) până la ~300 lei/lună fără TVA (Sintact Expert Plus/Lege), plus un produs dedicat „Monitorizare Proiecte Legislative” (Sintact, de la 150 lei/lună fără TVA); editorii (Rentrop & Straton, avocatnet, contzilla) vând newslettere/abonamente editoriale de 150–600 lei/an sau gratuite. Niciunul nu este poziționat specific pe „fiscal + SSM pentru cabinete mici” cu alertă pe impact.

### Cited Findings
**Lege5 (Indaco Systems)**
- Lege5 Online: 1 cont – 67 lei/lună (doar legislație), 104 lei (jurisprudență), 167 lei (pachet complet); reduceri 15–30% la 2–3 conturi; plata pe 12 luni în avans: 10% reducere + 2 luni bonus — [infojurist.ro, ofertă Lege5 Online (PDF, 2019)](https://infojurist.ro/wp-content/uploads/2019/01/Lege5-ONLINE.pdf) (date din 2019 – pot fi depășite)
- Pagini de comandă: [lege5.ro/Buy/Documentare](https://lege5.ro/Buy/Documentare), [lege5.ro/Buy/Dockets](https://lege5.ro/Buy/Dockets); conținut gratuit limitat: [lege5.ro/Gratuit/…](https://lege5.ro/Gratuit/g43donzvgi/impozite-si-taxe-locale-codul-fiscal?dp=hazdimzzgmztg)
- Achiziții publice: „Lege5 Online Legislație+Jurisprudență+Comentarii+Dosare+Hotărâri – 5 conturi – 12 luni” (Primăria Oradea) — [oradea.ro](https://oradea.ro/primaria-oradea/achizitii/cumparari-directe/da30913918/); pachet 10 conturi ≈ 424,08 lei/lună; Lege5 Desktop PREMIUM rețea 8 licențe ≈ 11.245,36 lei (Tribunalul București) — [tribunalulbucuresti.ro PACHET_LEGE5.pdf](https://www.tribunalulbucuresti.ro/images/documente/Achizitii_publice/PACHET_LEGE5.pdf); [licitatie-publica.ro (SRR)](https://www.licitatie-publica.ro/dv/773c057a-3fea-4238-a93e-bdf81d4836ef) – sumele din fragmente de căutare, de reconfirmat în documente

**Sintact (Wolters Kluwer România)** – prețuri listate pe shop (fără TVA/lună):
- Sintact AI Expert Plus – de la 299,25 lei — [shop.wolterskluwer.ro](https://shop.wolterskluwer.ro/produse/sintact-ai-expert-plus,695278.html)
- Sintact Lege – de la 300 lei; Sintact.ro Lege Assist – de la 99 lei; Sintact AI Jurisprudență – de la 219 lei — [shop.wolterskluwer.ro/produse](https://shop.wolterskluwer.ro/produse); [jurisprudență](https://shop.wolterskluwer.ro/produse/sintact-ai-jurisprudenta,693721.html)
- **„Sintact.ro Monitorizare Proiecte Legislative” – de la 150 lei fără TVA/lună** (produs dedicat alertelor pe proiecte) — [shop.wolterskluwer.ro](https://shop.wolterskluwer.ro/produse/monitorizare-proiecte-legislative,693052.html)
- Sintact AI Reviste – de la 289 lei; Biblioteca WK – de la 50 lei; contractare anuală/trimestrială/lunară, reînnoire automată, trial 14 zile menționat — [shop.wolterskluwer.ro](https://shop.wolterskluwer.ro/produse/sintact-ai-reviste,695260.html); [biblioteca](https://shop.wolterskluwer.ro/produse/biblioteca-wolters-kluwer,734257.html)
- Pachet „JustAll” (Sintact Expert Plus + laptop + Windows) de la 79 EUR/lună; versiune „Sintact AI” lansată iunie 2023; ofertă pentru Baroul București — [wolterskluwer.com JustAll](https://www.wolterskluwer.com/ro-ro/news/justall-solutie-completa-pentru-profesionisti); [Sintact AI](https://www.wolterskluwer.com/ro-ro/news/noua-versiune-sintact-ai); [baroul-bucuresti.ro](https://www.baroul-bucuresti.ro/stire/oferta-de-colaborare-din-partea-wolters-kluwer-romania-in-baza-protocolului-incheiat-cu-baroul-bucuresti-din-data-de-22-februarie)

**Legis (CTCE Piatra Neamț)**
- Disponibil monopost, rețea, online (`www.legisplus.ro`) și intranet; „aceeași bază de date folosită de instanțe”, actualizări zilnice; variantă „Legis Plus Fiscalitate” pentru contabili — [fiscalitatea.ro](https://www.fiscalitatea.ro/legis-plus-fiscalitate-unicul-soft-legislativ-care-ofera-acces-contabililor-la-toate-actele-normative-20339/); [contabilul.manager.ro](https://contabilul.manager.ro/a/13333/toata-legislatia-din-romania-toate-monitoarele-oficiale-toate-codurile-consolidate-si-actualizate.html); aplicație „Legis Mobile” — [App Store](https://apps.apple.com/app/id6444888569); produs iLegis — [ilegis.ro](https://www.ilegis.ro/application/noacces/modul/spete-act/parametri/eyJpZCI6IjEyMTQzOSJ9)
- Prețuri publice Legis: **nu am găsit** (doar oferte la cerere / achiziții publice)

**Rentrop & Straton**
- „Monitorul Contabil”: 6 luni (12 ediții) 287,76 lei TVA inclus; 12 luni (52 ediții săptămânale, miercurea) 595,14 lei (~11 lei/ediție), cu 2 rapoarte speciale și acces gratuit la „Alerta Contabilă” — [infotva.manager.ro](https://infotva.manager.ro/articole/legislatie/monitorul-contabil-au-aparut-ultimele-modificari-contabile-21333.html); [e-juridic.manager.ro](https://e-juridic.manager.ro/articole/monitorul-contabil-stiai-ca-exista-28513.html)
- „Consilier Taxe și Impozite” (30 de ani de apariție) — [fiscalitatea.ro](https://www.fiscalitatea.ro/rentrop-straton-implineste-30-de-ani-consilier-taxe-si-impozite-implineste-30-de-ani-24123/)

**avocatnet.ro**
- Abonament „Content Practic” (istoric, 2007): 12,50 lei/lună sau 150 lei/an, cu bază legislativă IntraLegis-CTCE (85.000 acte) — [avocatnet.ro](https://www.avocatnet.ro/articol_9960/Am-relansat-Abonamentul-Content-Practic.html); secțiunea Premium oferă alerte legislative (forum) — [avocatnet.ro forum](https://www.avocatnet.ro/forum/discutie_596150/Probleme-accesare-avocatnet-premium.html); termeni: [avocatnet.ro/Termeni-și-condiții](https://avocatnet.ro/Termeni-%C8%99i-condi%C8%9Bii*1.html). Preț Premium 2025–2026: **nu am găsit**.

**contzilla.ro** – informație contabilă gratuită, newsletter zilnic cu >20.000 abonați, >18.000 articole — [contzilla.ro/about](https://www.contzilla.ro/about/)

**folositor.ro „Radar fiscal”** – agregator gratuit RSS ANAF, actualizare ≤2 h — [folositor.ro](https://folositor.ro/radar-fiscal)

### Inferences
- Poziționare onestă: bazele de date (Lege5/Sintact/Legis) vând *conținut consolidat + jurisprudență* la 70–300 lei/lună/utilizator; un „radar” nu le înlocuiește, ci le precede (alertă + triere + impact). Singurul produs comparabil ca funcție este Sintact „Monitorizare Proiecte Legislative” (150 lei/lună fără TVA), orientat juridic, nu fiscal/SSM.
- Spațiul neacoperit: alertă combinată fiscal + SSM/PSI, pe profil de client (ex. microîntreprindere, HoReCa), cu termene și checklist – și la un preț sub 100 lei/lună.

### Gaps
- Prețuri curente (2026) Lege5 și Legis, preț avocatnet Premium, prețurile „Monitorul Fiscal”/alertelor R&S: **nu am găsit** în surse accesibile; cifrele Lege5 sunt din 2019 și din achiziții publice.

---

## Întrebarea 8: Există ghiduri ANSPDCP sau termeni care interzic scraping-ul site-urilor publice?

### Takeaway
Nu am găsit niciun ghid ANSPDCP sau altă poziție oficială românească despre scraping-ul site-urilor instituțiilor publice; nu am putut citi termenii site-urilor oficiale. Cadrul legal relevant indică mai degrabă libertate de reutilizare (texte oficiale fără drept de autor; Legea 57/2021 permite distribuirea MO), cu atenție la date personale eventual conținute în acte (ex. decizii nominale).

### Cited Findings
- Datele legislatie.just.ro „nu sunt protejate de drept de autor și pot fi reutilizate fără restricții” — [OKFN Index 2015](https://2015.index.okfn.org/place/romania/legislation/)
- Legea 57/2021 permite expres „căutare, salvare, distribuire și tipărire” a formatului electronic al MO — [fiscalitatea.ro](https://www.fiscalitatea.ro/acces-gratuit-la-toata-legislatia-vezi-in-ce-conditii-2856/)
- Modificările Legii 8/1996 (dreptul de autor) prin L.15/2019, L.8/2020, L.39/2022, L.69/2022 — [legeaz.net L.69/2022](https://legeaz.net/monitorul-oficial-321-2022/lege-69-2022) (pentru verificarea art. 9 – excluderea textelor oficiale)
- Căutarea „ANSPDCP web scraping date publice” a returnat doar articole comerciale generice (Energent, Monolith Law – Japonia), niciun document ANSPDCP — [monolith.law/ro](https://monolith.law/ro/general-corporate/scraping-datacollection-law)

### Inferences
- Riscul legal principal nu este dreptul de autor pe acte, ci (1) eventuale clauze din termenii site-urilor (necitite) și (2) GDPR dacă radarul stochează acte cu date personale (ex. ordine nominale în MO Partea I) – de filtrat/anonimizat.
- Bune practici recomandate: respectarea robots.txt, User-Agent identificabil cu contact, rată ≤1 cerere/secundă, cache ETag/Last-Modified, descărcare doar diferențe, păstrarea link-ului către sursă.

### Gaps
- Ghid ANSPDCP sau poziție oficială privind scraping: **nu am găsit**.
- Termenii de utilizare ai site-urilor oficiale (MO, MJ, ANAF, Parlament): **nu am putut citi** (acces blocat); trebuie verificați manual.
