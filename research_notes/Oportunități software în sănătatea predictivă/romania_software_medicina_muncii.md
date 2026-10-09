# Romanian clinic, lab and occupational-health software, integration options, and the occupational-medicine ("medicina muncii") market, with Oradea/Bihor pilot candidates (as of 9 Oct 2026)

> **Method note (9 Oct 2026).** This note fills the gaps left by `romania_piata.md` and does not repeat what that file already holds: MediNote and BizMedica family-medicine prices, Docbook figures, Callio, MedOcean, the Medworks price anchor, the Pelican/Medicover facts, and the e-SănătateaMea launch basics.
>
> **How the facts were gathered.** The egress proxy blocked every direct page fetch I tried: istoma.ro, setrio.ro, dmvconsult.ro, romedic.ro, oradeni.ro, oradea.ro. **Almost all facts below therefore come from search-engine result snippets and summaries, not full pages.** Treat them as "seen in a snippet" and re-check them before quoting. Vendor claims are marked "(vendor claim)".
>
> **Evidence labels:**
> - **[Established]**: several independent or primary sources agree.
> - **[Strong emerging]**: credible but single-source, vendor-reported or dated.
> - **[Plausible]**: an inference with partial support.
> - **[Speculative]**: a hypothesis.

## 1. Clinic, dental, lab and occupational-health software in use in Romania: what it does, prices, APIs and exports, partners, customer counts

### Takeaway
The Romanian market is made of many small local vendors. **No general clinic or dental practice-management system with a publicly documented API was found.** The only exceptions are Medicai (imaging, which advertises a REST API and SDK) and the big networks' own closed employer portals. What vendors do expose is "compliance plumbing" (CNAS/SIUI, e-prescription, ANAF e-Factura), Excel imports, SMS/WhatsApp and accounting connectors.

Occupational health is **not greenfield**. At least six Romanian products generate the *fișa de aptitudine* (fitness certificate) and the medical file:
- BizMedica MM (Setrio)
- MedExam (DMV Consult)
- Qmedical
- the Charisma Medical OH module
- the MedSoft OH module
- Tempomed (listed only)

MedLife already offers employers an online status portal **[Established for product existence; APIs: none found]**.

### Cited Findings

**Dental and clinic practice management**
- **iStoma (iDava Solutions)** (vendor claim, via ZF) **[Strong emerging]**:
  - a Romanian dental-clinic digitisation suite, on the market since 2012
  - claims **5,300 dentists** in Romania, Moldova, Ireland, Italy and Spain
  - now expanding abroad
  - no public API documentation or price found
  - Source: [ZF IT Generation – Ionuț Botorogeanu, iDava](https://www.zf.ro/zf-it-generation/zf-it-generation-ionut-botorogeanu-fondator-ceo-idava-solutions-22322427)
  - Note: "iStom" API connectors on apix-drive belong to a **different, Russian** dental CRM. Do not confuse the two — [apix-drive iStom](https://apix-drive.com/pt/istom-api); [crmindex.ru iStom](https://crmindex.ru/products/istom)
- **icMED (Syonic)**: "100% web" modular platform for clinics, practices and dentistry (vendor claim). Advertised integrations:
  - CAS/SIUI reporting servers, including sending e-prescriptions to SIUI
  - ANAF e-Factura XML export
  - cash-register receipt printing
  - medical-equipment integration
  - a patient app, **icMED.Mobile**, for patients of providers that use icMED
  - support line 0256.256.256 (Timiș area code)
  - **No developer API reference found** **[Strong emerging]**
  - Sources: [icmed.ro (EN)](https://icmed.ro/indexen.html); [icMED dentistry](https://icmed.ro/dentistry.html); [icMED cabinets](https://icmed.ro/cabinets.html); [icMED patient app](https://icmed.ro/patient.html)
- **iClinic**: I could not confirm a Romanian product of this name or its developer. An iCLINIC practice-management app listing shows calendar and room booking but does not name the developer. The earlier note's only Romanian mention is as an integration target of receptie-clinica.ai — [mwm.ai iCLINIC listing](https://mwm.ai/apps/iclinic/1529086699) **[unverified]**
- **Zarina CRM Medical** (vendor claim) **[Strong emerging]**:
  - covers patient files, scheduling, online booking, invoicing, e-Factura and automations
  - pricing: **one-time licence of €2,990 + VAT ("lifetime", no per-user fees)**, from the vendor's general CRM blog; no separate medical-edition price was found
  - listed native integrations: SmartBill, FGO, Oblio, WooCommerce, Shopify, PrestaShop, Stripe, PayPal, Google and Microsoft calendars, **WhatsApp, SMS**, ANAF e-Factura
  - Sources: [Zarina CRM – cabinet medical functionalities](https://www.zarinacrm.ro/crm-cabinet-medical/functionalitati/); [Zarina blog – best CRM 2026](https://www.zarinacrm.ro/cel-mai-bun-crm-2026/); [Antena3 paid content](https://www.antena3.ro/continut-platit/zarina-crm-softul-romanesc-care-simplifica-digitalizarea-companiilor-din-romania-764158.html)
- **MediNote**: searches for "MediNote API / webhook / export" returned only foreign products (MediRecords, Metriport). **No MediNote API documentation found** **[gap confirmed]**.
- **Docbook**: an older Wall-Street.ro piece quotes founder Cristian Barbu with about 80 clinics and about 2,000 doctors in Bucharest and 11 other cities. The prior note has a newer claim of 8,500+ doctors. **No public API or PMS-sync documentation found** — [Wall-Street.ro](https://www.wall-street.ro/articol/Companii/230187/docbook-aplicatia-cu-care-te-programezi-in-mai-putin-de-un-minut-la-doctor.html) **[Strong emerging, dated]**
- **Heymedica**: a Romanian-founded (Alba Iulia) pan-European provider-search and booking platform covering hospitals, clinics, labs, pharmacies and dentists.
  - Co-founder and CEO Horea Timiș is a physician and former public-health director.
  - It claims "almost 500,000 provider indexings in Europe", 10 languages, and AI symptom-to-specialty routing.
  - Launched Dec 2022. Funding is reported as €500k (Profit.ro) vs $59k (CB Insights). Founding year is 2019 or 2020 depending on the source **[Strong emerging; data conflict]**.
  - Sources: [Profit.ro video interview](https://profit.ro/profit-live/video-profit-live-horea-timis-co-fondator-heymedica-avem-aproape-500-000-de-indexari-de-provideri-la-nivelul-europei-ne-indreptam-spre-o-platforma-sociala-21017173); [Alba24](https://alba24.ro/heymedica-cea-mai-complexa-platforma-medicala-din-europa-pornita-de-la-alba-iulia-horea-timis-un-booking-medical-960265.html); [Dealroom](https://app.dealroom.co/companies/heymedica); [CB Insights](https://www.cbinsights.com/company/heymedica)
- **Medicai** (Cluj, imaging):
  - cloud and on-prem medical-imaging storage
  - interoperable "via the Medicai API and an SDK set"; advanced plans include API access and integration with medical systems (Oct 2025 interview)
  - a third-party profile calls the API RESTful
  - for clinics that already have an imaging server, Medicai adds a "smart layer" on top
  - pricing depends on number of doctors, storage and integration level
  - raised €500k (older article)
  - **[Strong emerging; the only Romanian vendor found that advertises an API]**
  - Sources: [Revista Biz – Andrei Blaj, Medicai](https://www.revistabiz.ro/andrei-blaj-medicai-imagistica-la-puterea-ai/); [parse.gl profile](https://www.parse.gl/brands/medicai-io); [Romania Insider](https://www.romania-insider.com/medical-imaginery-medicai-funding); [StartupCafe](https://startupcafe.ro/mediaci-finantare-investitie-rocax-htm-11820)
- **Setrio** is also profiled as a Romanian provider of IT for health — [Newsweek România](https://newsweek.ro/sanatate/video-setrio-soft-solutii-it-romanesti-pentru-sanatate-si-pacientii-romani)

**Occupational-health ("soft medicina muncii") products**

All are vendor claims from search snippets; pages could not be fetched **[Strong emerging]**:
- **BizMedica – Medicina Muncii module (Setrio)**:
  - auto-generates the *fișa de aptitudine* and the medical file for hiring and periodic exams
  - fast entry of occupational history using **COR nomenclatures, workstation and workspace definitions**
  - **imports a client firm's employee list from Excel**
  - Source: [Setrio – Medicina Muncii](https://setrio.ro/medicina-muncii/)
- **MedExam (DMV Consult)**:
  - platform for OH cabinets with digital medical files, examinations, fitness certificates and reports, usable on any device
  - examinations are completed in the app ("fără hârtie", paperless)
  - lets the cabinet monitor nurse activity
  - Source: [DMV Consult – MedExam](https://dmvconsult.ro/medicina-muncii)
- **Qmedical**:
  - software for clinics offering OH
  - manages the client firms under OH contract, with jobs defined by risk, and produces "complex reports"
  - no local install needed
  - the page looks old
  - Source: [qmedical.ro](http://qmedical.ro/)
- **Charisma Medical – Medicina Muncii module** (part of an ERP suite): records visits, analyses and results, issues the aptitude certificate, tracks employee evolution — [Charisma](https://www.charisma.ro/sisteme-software/charisma-nivel-2/charisma-software-medical/medical-clinica/medicina-muncii)
- **MedSoft** (med-soft.ro): clinic-management software with an optional OH module; custom quote for organisations with more than 20 users — [MedSoft](https://www.med-soft.ro/)
- **Tempomed** and **NEW EVMEDICA MM** appeared in OH-software results, but their content could not be read. A follow-up search found nothing on Tempomed — [tempomed.ro](https://tempomed.ro/); [newevmedicamm.ro](https://newevmedicamm.ro/medicina-muncii)
- An old "free OH software" listing (originally built for Italian doctors) is expired — [Romedic](https://www.romedic.ro/software-medicina-muncii-gratuit-0A7750)

**Big-network OH digital services**
- **MedLife "MM Express"** (launched 2021): the fitness certificate for new hires is issued **online within at most 24h** after the required investigations. The employer receives it **through MedLife's client platform** — [MedLife MM Express](https://www.medlife.ro/medicina-muncii-express); [MedLife press release](https://www.medlife.ro/comunicat-de-presa/medlife-lanseaza-programul-mm-express-fisa-de-aptitudini-disponibila-24-de-ore) **[Established]**
- **MedLife Self-Service portal**: employers see the **status of OH exams in real time** and upload the documents the exam needs. Employees self-book at MedLife locations — [MedLife self-service](https://www.medlife.ro/self-service) **[Strong emerging]**

**Laboratory information systems (LIS)**
- **No Romanian LIS vendor was identified.** Searches returned only Moldovan public tenders. They are useful as specification comparators:
  - required functions: electronic orders and results, sample traceability, technical and medical validation, **automatic transmission of results to external systems**, audit trails, analyser integration (ASTM E1394 / HL7 v2.5 / LIS2-A2)
  - one bid offered REST/JSON with **HL7 FHIR R4**
  - products named: TerraLab LIMS 3.0 (Ukraine), SilverlabNet (BeHIT), Atomate (Chișinău; ASTM, HL7, FHIR R4, REST/JSON)
  - Sources: [MTender doc 1](https://storage.mtender.gov.md/get/21096c6e-a1a7-45a4-a76a-bd61980ffc43-1782370226273); [MTender LIS spec](https://storage.mtender.gov.md/get/c0256e49-7ac1-4b91-b72a-7fe6e8a96fb6-1782370223860) **[Strong emerging for Moldova; Romania unknown]**
- **Romanian reference integration spec (2026)**: a technical annex from Institutul Clinic Fundeni sets three ways for labs to send results to a screening platform:
  - **(A) CSV file**
  - **(B) manual entry in the web interface**
  - **(C) automatic transmission via API over HTTPS (TLS 1.2+)**, with automatic matching of each result to its patient and request
  - corrections after validation must keep their history and a stated reason
  - the system must show who entered and who validated each result
  - Source: [ICF Fundeni – Anexa 2 Transmiterea datelor (Apr 2026)](https://icfundeni.ro/wp-content/uploads/2026/04/Anexa-nr.-2_Transmiterea-datelor_signed.pdf) **[Established, primary document]**

**Summary table (integration surface found publicly)**

| Vendor / product | Segment | Price found | Public API / webhooks | Exports / connectors found | Claimed scale |
|---|---|---|---|---|---|
| iStoma (iDava) | dental | none | none found | — | 5,300 dentists, 5 countries |
| icMED (Syonic) | clinics, dental | none | none found | SIUI, e-prescription, e-Factura XML, cash register, equipment; patient app | none found |
| MediNote | clinics, labs | 50 lei/user/month (prior note) | none found | SIUI, SMS, e-Factura (prior note) | none found |
| BizMedica (Setrio) | GP, OH | 159–199 RON/month GP (prior note, old) | none found | SIUI; **Excel import of employees** (OH) | none found |
| Zarina CRM Medical | clinics, dental | €2,990 + VAT one-time (general licence) | none found | SmartBill/FGO/Oblio, Stripe, calendars, **WhatsApp, SMS**, e-Factura | none found |
| MedExam (DMV Consult) | OH | none | none found | reports | none found |
| Qmedical | OH | none | none found | "complex reports" | none found |
| Charisma Medical | clinics, OH | none | none found | ERP suite | none found |
| MedSoft | clinics, OH | quote for >20 users | none found | — | none found |
| Medicai | imaging | depends on size | **REST API + SDK (advertised)** | PACS layer | none found |
| Docbook | marketplace | free for patients | none found | — | 8,500+ doctors (prior note) |
| Heymedica | marketplace | none | none found | — | ~500k provider indexings (EU) |
| MedLife portal | network OH | bundled | closed | employer status portal, online fitness certificate | ~800k subscribed employees (see Q4) |

### Inferences
- **Integrating with Romanian PMS vendors will mostly mean partnering vendor by vendor, or working through files and messages, not plugging into public APIs** **[Plausible]**. The cheapest technical paths are:
  - CSV/Excel import and export (BizMedica already imports employee lists from Excel)
  - PDF and e-mail ingestion
  - calendar sync (Zarina syncs Google/Microsoft calendars)
  - a WhatsApp/SMS layer
- AI-receptionist startups claim integrations with iStoma, icMED and iClinic (prior note). That suggests these vendors grant partner access on request, even though none publishes an API **[Plausible]**.
- **OH software already exists**, so "a program that prints the *fișa de aptitudine*" is a commodity. The gap is on the **employer side**: knowing who is due, chasing staff, collecting the employer-signed risk-factor form (anexa 3), and following up abnormal findings. MedLife's self-service portal shows the networks are already selling exactly this employer coordination layer. **Independent OH cabinets compete against it without an equivalent** **[Plausible]**.
- The Fundeni annex shows the Romanian public sector accepts **CSV + manual + API** options for lab-result exchange. An add-on that supports all three would match how real Romanian projects are specified **[Plausible]**.

### Gaps
- No price, API or customer count found for: iStoma, icMED, Qmedical, MedExam, Charisma, MedSoft, Tempomed.
- No API documentation for MediNote, Docbook, iClinic or Zarina.
- iClinic's developer and its Romanian presence are unverified.
- No Romanian LIS vendor identified, so it is unknown which LIS independent Romanian labs use. Hospital HIS vendors (Hipocrate/RSC, InfoWorld, Softeh) may bundle LIS modules; that was not verified.
- No market-share data on which OH software Bihor cabinets actually use.

## 2. Do Synevo, Bioclinica, MedLife, Regina Maria and Medicover deliver results online, do independent clinics receive results electronically, and how are abnormal results followed up?

### Takeaway
All the large lab networks give **patients** online access to results (apps or portals). Synevo has long had a platform for **doctors and patients**. Each network runs its own separate account, often activated at reception. I found **no public evidence of HL7/FHIR feeds to independent clinics**, and **no documented process in which a lab or network pushes abnormal results to the referring doctor or recalls the patient**. Interpretation is offered as a patient-initiated service: Synevo Decoder tele-consults, Regina Maria's analysis dictionary, MedLife's AI assistant **[Established for patient access; doctor-side delivery and abnormal-result follow-up undocumented]**.

### Cited Findings
- **Synevo (Medicover group)**:
  - It describes itself as the first local company to launch an online results platform "for both doctors and patients" (company publication, 2020) — [Synevo – Sănătatea în focus, Mar 2020](https://www.synevo.ro/wp-content/uploads/2020/03/Sanatatea-in-focus__martie-2020_2.pdf); [Forbes.ro – digitalizare în sănătate](https://www.forbes.ro/digitalizare-in-sanatate-347369) **[Strong emerging, dated]**
  - **MySynevo app**: result history, **graphs of values over time**, children's results in the same account, online booking. Extended access needs activation at a Synevo reception — [App Store – MySynevo](https://apps.apple.com/ro/app/mysynevo/id6478497666) **[Established]**
  - **Synevo Decoder**: virtual consultations with Synevo lab physicians to interpret results, booked online. An older article cites a team of 14 lab-medicine, pathology and genetics doctors. Synevo frames it as "guidance on what to do with the result", not a medical consultation — [Synevo Decoder](https://synevo.hilio.com/) **[Strong emerging]**
  - Synevo said it works with 68% of the country's ~40,000 doctors, and that ~70% of its patients come referred by a doctor. These are company statements, about 2020–2021, from search snippets — [Synevo PDF 2020](https://www.synevo.ro/wp-content/uploads/2020/03/Sanatatea-in-focus__martie-2020_2.pdf); [Wall-Street.ro – Laurențiu Luca, Synevo](https://www.wall-street.ro/articol/Companii/246923/laurentiu-luca-synevo-romania-finantarea-companiilor-din-domeniul-analizelor-medicale-ar-trebui-sa-urmeze-dorinta-pacientului-nu.html)
- **Medicover**: its app allows booking and **checking lab results**, with the account activated by a form at a Medicover reception. MySynevo and Medicover run **separate apps and accounts**, and no source confirms that Synevo results flow into the Medicover app — [App Store – Medicover Romania](https://apps.apple.com/app/1384631429); [App Store – Medicover OnLine](https://apps.apple.com/app/id1557230744) **[Strong emerging]**
- **MedLife**:
  - The app shows analysis history and the evolution of results. Non-account holders can check results with **sample code + CNP**. A notifications section exists for MedLife patients, with content unspecified — [Capital – analize MedLife](https://www.capital.ro/analize-medicale-in-cadrul-medlife-vezi-ce-optiuni-ai-si-cum-te-programezi.html)
  - MedLife launched an **in-app AI assistant**. It summarises clinical history from the last 2 years and lab bulletins from the last 6 months, then recommends which specialty to see. It does not diagnose or prescribe — [MedLife press release](https://www.medlife.ro/comunicat-de-presa/medlife-lanseaza-primul-asistent-ai-care-ofera-ghidaj-medical-personalizat); [Economedia](https://economedia.ro/medlife-lanseaza-primul-asistent-ai-care-ofera-ghidaj-medical-personalizat-direct-in-aplicatie.html) **[Established]**
  - The Oradea lab, **MedLife Genesys**, is RENAR-accredited to ISO 15189 and offers online results — [MedLife Genesys Oradea](https://www.medlife.ro/laborator-medlife-genesys-oradea)
- **Regina Maria**:
  - The app holds a digital medical file with **10+ years of history** (results, appointments, consultations, recommendations) and an analysis dictionary — [App Store – Regina Maria](https://apps.apple.com/ro/app/regina-maria/id833535888)
  - The lab uses **AI auto-verification of results**, which is a quality-control step. A Forbes piece on its "smart labs" says the system detects abnormal values and estimates future risks. It is **unclear whether these alerts reach patients or doctors** — [Forbes.ro](https://www.forbes.ro/?p=462526) **[Strong emerging]**
- **Bioclinica**:
  - Founded 1992 in Timișoara as Biomedica, renamed in 1998.
  - Network size conflicts: 12 labs, 76 own collection points and 86 partners (directory snippet, undated) vs 15 central labs and 175+ collection points (unofficial InfoContact guide).
  - Bulletins can be downloaded online; the platform name and any doctor portal are unverified.
  - Turnover passed 150m lei in 2019.
  - Sources: [InfoContact – Bioclinica](https://www.infocontact.ro/contact-bioclinica-suport/); [Bioclinica contact](https://bioclinica.ro/contact); [ZF English 2019](https://www.zfenglish.com/companies/medical-laboratory-chain-bioclinica-overshoots-ron150m-turnover-mark-19431767) **[Strong emerging; size conflict]**
- **Electronic delivery to independent clinics:**
  - The only Romanian primary specification found is the Fundeni screening annex (CSV / manual / API; see Q1).
  - No HL7/FHIR interface from Synevo, Bioclinica, MedLife or Regina Maria to third-party clinics was documented in search results.
  - The prior note documented GDPR fines for clinics sending patient data over WhatsApp and e-mail. That suggests informal channels are in real use — see `romania_piata.md` §3.

### Inferences
- Patients receive results in **network-specific silos** (MySynevo, Medicover, MedLife and Regina Maria apps). An independent clinic or family doctor that refers to several labs likely gets results by PDF, e-mail, the patient's printout or a lab web portal, not by structured feeds **[Plausible, not measured]**.
- **Abnormal-result follow-up looks patient-initiated.** The patient reads the result, then optionally books Decoder or asks the AI assistant. I found no closed-loop "lab → doctor alert → recall" process. That is the most direct opening for a result-routing / follow-up add-on. The caveat: the big networks are visibly building AI interpretation in-house (MedLife assistant, Regina Maria smart labs), so they are competitors there, not customers **[Plausible]**.
- A follow-up product for independents probably has to **ingest PDFs and e-mails and do the structuring itself** (OCR/LLM extraction from lab bulletins) rather than wait for HL7 feeds **[Plausible]**.

### Gaps
- How Synevo, Bioclinica and MedLife deliver results to referring **external doctors** (portal login, e-mail, HL7). Not found.
- Critical-value notification policies of Romanian labs (phone call to doctor or patient) are not published.
- Which LIS each network uses, and whether any offers integration to small clinics, is unknown.
- No Romanian data on the share of abnormal results that get follow-up.

## 3. Occupational medicine market in Romania: legal basis, frequency, documents, providers, prices, scheduling, digitisation, pain points and fines, market size

### Takeaway
Occupational medicine is a **legally mandated, employer-paid, recurring** service:
- The legal basis is Law 319/2006 and HG 355/2007.
- Every worker must have a periodic exam. Its frequency is set by the risk-based forms in Annex 1 and in practice is usually **annual**.
- Missing hiring or periodic exams are fined at **4,000–8,000 lei per offence** (Law 319/2006 art. 39(4)).

With **5.76m employees nationally** (Dec 2025) and **187.3k in Bihor** (June 2025), periodic exams alone at 80–110 lei per employee give a **theoretical** spend of about **460–630m lei a year nationally and about 15–21m lei a year in Bihor**. No official market-size figure exists. The largest Bihor OH provider (Medicris) was bought by MedLife in 2022, but several independent OH cabinets still operate in Oradea **[Established for the law and fines; market size is my inference]**.

### Cited Findings

**Legal basis and process (HG 355/2007, amended notably by HG 1169/2011)** **[Established]**
- **Art. 8:** the preventive services are exams at hiring, adaptation, periodic, return to work, special surveillance, and workplace health promotion. They follow **Annex 1**. Exams are based on the **risk-factor identification form (Annex 3)**, which the **employer must complete in full and sign**.
- **Art. 20:** the periodic exam is **mandatory for all workers**.
- **Art. 21:** its frequency is set in the Annex 1 forms and can be changed only on the OH physician's proposal, with the employer informed.
- **Fitness certificate (Annex 5):** filled in 2 copies, one for the employer and one for the worker. Outcomes are *apt*, *apt condiționat*, *inapt temporar* or *inapt permanent* (art. 10–12).
- Employers fund all preventive services, and workers bear no cost.
- Sources: [avocatnet – HG 355/2007 text](https://www.avocatnet.ro/articol_8477/Hotarare-nr-355-2007-privind-supravegherea-sanatatii-lucratorilor.html); [Rubinian – HG 355/2007](https://www.rubinian.com/hg-355-2007-privind-supravegherea-sanatatii-lucratorilor_63_0_0.php); [avocatnet – HG 355 consolidated](https://www.avocatnet.ro/articol_12872)

**Frequency in practice**
- A legal forum says the periodic control "de regulă" (as a rule) happens **annually** for common jobs. This is not an official text **[Strong emerging]** — [avocatnet forum](https://www.avocatnet.ro/forum/discutie_214357/vizita-medicala-pentru-angajati.html)
- Do not confuse this with **Moldovan** drafts that move to 24/36-month intervals. Those do not apply to Romania — [Monitorul Fiscal MD](https://monitorul.fisc.md/examenul-medical-periodic-al-angajatilor-ce-modificari-se-propun/)

**Exam sets by risk group** (from public tenders, not the HG itself)
- Group 1 (office, computer, public-facing work): general clinical, ophthalmological and psychological exams.
- Group 3 (drivers, archive, copiers): adds **audiometry, glucose, EKG and spirometry**.
- Group 5 (work at height): adds balance tests.
- Source: [ONRC tender spec 2020](https://www.onrc.ro/documente/achizitii/2020/05.06.2020/Format%20editabil%20-%20caiet%20de%20sarcini%20si%20formulare.doc) **[Strong emerging]**

**Return-to-work exam**
- Due after an interruption of **at least 90 days for medical reasons, or 6 months for any other reason**, and must happen **within 7 days** of resuming work (per county tender specs) — [CJ Timiș spec 2021](https://www.cjtimis.ro/wp-content/uploads/2020/07/Caiet-de-sarcini-privind-achizitia-de-servicii-de-medicina-muncii-2021_1.pdf); [CJ Timiș spec 2024](https://www.cjtimis.ro/wp-content/uploads/2024/02/Caiet-de-sarcini-mm-2024.pdf); [CJ Timiș spec 2026](https://www.cjtimis.ro/wp-content/uploads/2020/07/Caiet-de-sarcini-MM-2026.pdf)

**Employer obligation and fines**
- **Law 319/2006 art. 13 lit. j):** the employer must hire only people fit for the job and ensure periodic medical control.
- **Art. 39(4):** failure to ensure the hiring, return-to-work, job-change or periodic exams is fined **4,000–8,000 lei**, according to an Inspecția Muncii communiqué and avocatnet. These amounts come from texts dated 2006–2010. **Re-check the consolidated law for 2026** **[Established, verify current amount]**.
- Sources: [Inspecția Muncii – comunicat examen medical](https://www.inspectiamuncii.ro/documents/547298/82715837/comunicat-examen+medical.doc/eeaa2a89-0633-4c02-b070-c7901ad81a43); [avocatnet – obligations and fines](https://www.avocatnet.ro/articol_68935)
- Common ITM findings, as summarised in search, are work done **without the hiring or periodic exam** and **missing fișe de aptitudine**. Separate press reports show ITM Alba levying SSM fines of 10,000 lei — [Alba24 – ITM Alba](https://alba24.ro/itm-alba-angajatori-sanctionati-cu-amenzi-si-avertismente-controale-la-zeci-de-firme-din-judet-755837.html); [Alba24 – ITM Alba 10,000 lei](https://alba24.ro/itm-alba-amenda-de-10-000-de-lei-si-sase-avertismente-pentru-angajatori-care-nu-au-respectat-legislatia-muncii-676613.html) **[Strong emerging]**
- An April 2026 legal article stresses that all OH costs fall on the employer. "Pay first, we reimburse later" schemes are not allowed, and an employee's refusal to attend can be disciplined — [avocatnet](https://www.avocatnet.ro/articol_68935)
- A national Inspecția Muncii undeclared-work campaign (2–22 June 2026) issued fines of over 23.3m lei. That is not OH-specific, but it shows enforcement intensity — [Contzilla – ITM tag](https://www.contzilla.ro/tag/itm/) **[Strong emerging]**

**Prices and contract values**
- **Medworks (Bucharest):** 80 lei per employee per year, or 110 lei for drivers and machine operators (prior note) **[Strong emerging]**.
- **No 2026 published price list was found** in searches for "tarif medicina muncii 2026".
- **ROMATSA tender (subscription + OH, about 1,100 employees, 4 years):**
  - estimated at 10.6m lei; bidders were MedLife, Gral Medical and Centrul Medical Unirea
  - **awarded to MedLife for 7.98m lei excl. VAT**
  - the previous contract was 3.32m lei
  - a later procedure was signed at **12.1m lei** against a 12.55m lei estimate
  - **[Established, dates 2016–2021]**
  - Sources: [Profit.ro – three bidders](https://profit.ro/stiri/trei-companii-se-bat-sa-furnizeze-servicii-medicale-angajatilor-romatsa-contractul-este-estimat-la-10-6-milioane-de-lei-16933335); [Profit.ro – MedLife 8m lei](https://profit.ro/stiri/medlife-va-avea-grija-de-sanatatea-angajatilor-romatsa-pentru-8-milioane-de-lei-17192878); [Profit.ro – 12.1m lei](https://www.profit.ro/stiri/medlife-se-va-ocupa-de-sanatatea-salariatilor-romatsa-pentru-8-milioane-de-lei-20385060)

**Scale indicators**
- **5.76m employees** in Romania on 31 Dec 2025 (INS) — [Profit.ro](https://profit.ro/taxe-si-consultanta/romania-avea-anul-trecut-5-76-milioane-salariati-botosani-si-teleorman-cele-mai-mici-salarii-la-polul-opus-bucuresti-22784743) **[Established]**
- **Bihor: 187.3k employees** (end of June 2025), +1.3% y/y; average net earnings 4,670 lei. Bihor is the second-largest county in the North-West after Cluj (about 290.7k) — [INS Bistrița-Năsăud, Forța de muncă June 2025](https://bistrita.insse.ro/wp-content/uploads/2025/09/28_Forta-de-munca_iunie_25.pdf) **[Established]**
- Provider counts:
  - The Romedic directory lists **508 "cabinete de medicina muncii"** nationally. This is a directory count, not a census — [Romedic](https://www.romedic.ro/cabinete/medicina-muncii/4) **[Strong emerging, a lower bound]**
  - **No official count of OH physicians** was found. General doctor-shortage sources do not break out this specialty.
- Provider scale examples:
  - Medexpert Cluj: 15,000+ employees a year and 500+ firms (prior note)
  - **Medicris Oradea: 22,000+ subscribers** (2022; see Q5)

**How employers schedule exams and how digital the process is**
- Evidence is indirect:
  - BizMedica imports **client employee lists from Excel**
  - MedLife's portal lets employers **upload documents and track exam status**
  - Oradea cabinets such as Carimed **travel to employer premises by appointment**, and Medimun requires appointments (see Q5)
- **No survey of employer scheduling practice** (Excel, e-mail, phone) was found.
- Sources: [Setrio](https://setrio.ro/medicina-muncii/); [MedLife self-service](https://www.medlife.ro/self-service); [Carimed – despre noi](https://carimedcenter.ro/despre-noi/)

### Inferences
- **Theoretical market size**: 5.76m employees × 80–110 lei ≈ **460–630m lei a year (≈ €90–125m)** for periodic exams alone, assuming full annual compliance. Hiring exams on labour turnover, and paraclinical extras for risk groups, would add to that. **Bihor**: 187.3k × 80–110 lei ≈ **15–21m lei a year (≈ €3–4m)**. These are my calculations, not published figures **[Plausible]**.
- **ROMATSA implies about 1,800 lei per employee per year** for subscription + OH (7.98m lei / 4 years / 1,100). That is close to the €400 tax-free ceiling (Q4). It shows the money in employer health sits in the **subscription bundle**, with OH as the mandatory entry point **[Plausible]**.
- **Fines (4,000–8,000 lei per offence) are about 40–100 times the per-employee OH price.** That makes "never miss a due date" a credible value proposition for employers. Whether employers perceive the risk depends on ITM inspection frequency, which I did not find for Bihor **[Plausible]**.
- **Viability as a first B2B market** **[Plausible]**:
  - **For:** a mandated, recurring, date-driven workflow; employer-paid; a reachable cluster of independent Oradea OH cabinets; employer-side coordination is visibly a product (MedLife portal); exam outputs (glucose, EKG, BP, spirometry, audiometry) are natural **prevention triggers** for follow-up.
  - **Against:** low unit prices (80–110 lei), existing OH software (Q1), MedLife's consolidation in Bihor (Medicris), and OH physicians' role being limited to fitness. Treatment follow-up belongs to family doctors, so a follow-up product needs a referral loop the OH doctor does not own.
- A wedge that fits: sell to **independent OH cabinets** a white-label "employer portal + due-date reminders + abnormal-finding follow-up" that lets them match MedLife's self-service. Charge per employee per year (e.g., a few lei) or per cabinet **[Speculative]**.

### Gaps
- The exact Annex 1 periodicity table (12 months vs other intervals per risk factor) was not read. The legislatie.just.ro text needs checking.
- The current (2026) amount in art. 39 of Law 319/2006, and whether the Feb 2026 Senate amendments to Law 319/2006 (violence/harassment) passed, are not confirmed.
- No ITM Bihor statistics on OH-related fines.
- No official count of OH providers or physicians, and no revenue for the OH segment.
- No survey of employer pain points (expired certificates, scheduling method).

## 4. Employer health subscriptions ("abonamente medicale"): tax treatment, subscriber numbers, providers

### Takeaway
Under the current Fiscal Code (**art. 76(4^1) lit. f)**), employer-paid medical subscriptions and voluntary health insurance for **the employer's own employees** are **non-taxable and outside the CAS/CASS/CAM base up to €400 per person per year**. They also fall under the overall 33%-of-base-salary cap for such benefits. Family members are not covered by the exemption, and an employee who pays the subscription personally gets a €400 deduction instead.

Industry sources claim **over 2–2.2m Romanian employees** hold employer subscriptions in a market of **over €250m**. MedLife (~800k) and Regina Maria (780–850k) dominate **[Established for the tax rule; subscriber numbers Strong emerging and vendor-sourced]**.

### Cited Findings

**Tax treatment**
- **Employer-paid** (July 2026 article) **[Established, re-check legislatie.just.ro]**:
  - non-taxable up to €400 per person per year
  - also within the **33% of base salary** limit
  - only the excess is a taxable benefit
  - excluded from CAS, CASS and CAM within those limits
- **Own employees only**: the €400 does not extend to family members.
- **Employee-paid**: a deduction from the salary-tax base, up to €400.
- Sources: [Fiscalitatea.ro (Jul 2026)](https://www.fiscalitatea.ro/abonamentul-medical-incheiat-direct-de-salariat-cu-centrul-medical-cum-il-poate-deconta-angajatorul-si-ce-taxe-se-aplica-24930/); [Contabilul.manager.ro – family members](https://contabilul.manager.ro/a/30196/abonamentul-de-servicii-medicale-pentru-salariat-si-membrii-de-familie-care-este-tratamentul-fiscal.html); [Capital – deductible up to €400](https://www.capital.ro/abonamentele-medicale-sunt-deductibile-in-limita-a-400-de-euro-an.html)
- **Accounting**: OH services are booked as an ordinary third-party service expense (account 628). The tax-exempt subscription is booked as a salary benefit (account 6241). OH is the employer's legal obligation, not an employee benefit (search summary) — [Portal Contabilitate](https://www.portalcontabilitate.ro/servicii-medicale-suportate-de-angajator-pentru-salariati-abonamente-medicale-si-servicii-de-medicina-muncii-tratament-fiscal-222709.htm) **[Strong emerging]**
- Whether psychologist sessions paid by the employer fall under the €400 cap was raised but not resolved in the snippets — [e-juridic](https://e-juridic.manager.ro/articole/sedinte-la-psiholog-suportate-de-angajator-se-incadreaza-in-plafonul-de-400-euro-pentru-abonamente-medicale-29772.html)

**Subscriber numbers and providers**
- **Over 2.2m Romanians** have employer-provided subscriptions and the market is **over €250m**. Seven in ten large companies include subscriptions. The source is a provider advertorial (Enayati Medical City, Oct 2025) citing "PwC estimates and industry data", with no methodology — [Wall-Street.ro advertorial](https://www.wall-street.ro/articol/sanatate/enayati-medical-city-lanseaza-abonamentele-aniversare-corporate.html); [Bursa advertorial](https://www.bursa.ro/advertorial-enayati-medical-city-lanseaza-abonamentele-aniversare-corporate-27561751) **[Strong emerging, vendor-sourced]**
- **Regina Maria**: 780,000+ subscriptions from about 10,000 companies (older material), and 850,000+ subscriptions from nearly 12,000 companies (later material). Both are sponsored content and undated in the snippets — [HotNews 1](https://hotnews.ro/?p=71164); [HotNews 2](https://hotnews.ro/?p=1749464) **[Strong emerging]**
- **MedLife**: calls itself the subscription leader, with about 800,000 employees from 8,000 companies. A 2022 MedLife release cites PALMED: about 1 in 3 of 4.23m private-sector employees used services via a MedLife subscription — [MedLife article](https://www.medlife.ro/articole-medicale/sanatatea-angajatilor-vitala-pentru-continuitatea-unui-business); [MedLife release](https://www.medlife.ro/comunicat-de-presa/1-din-3-angajati-romani-avut-grija-de-sanatatea-sa-cu-ajutorul-abonamentului) **[Strong emerging]**
- MedLife's corporate subscription bundles OH with labs, check-ups and specialist consultations. MedLife also launched "LevelUp", a subscription with gym access — [MedLife MM Express](https://www.medlife.ro/medicina-muncii-express); [Economedia – LevelUp](https://economedia.ro/?p=242357)
- A 2026 piece discusses whether **small companies** can offer packages comparable to corporates — [Economedia](https://economedia.ro/?p=369592)
- Other providers seen: Enayati Medical City (Bucharest), Gral Medical, and Centrul Medical Unirea (a ROMATSA bidder; it is Regina Maria's operating company per my background knowledge, not verified this session).

### Inferences
- The €400 cap is about **2,000–2,100 lei a year** at 2026 rates (EUR/RON ≈ 5.1–5.2). It is the de facto ceiling for employer prevention spend per employee **[Plausible]**.
- About 2.2m subscribers out of 5.76m employees is roughly **38% penetration**, concentrated in large firms and big cities. In Bihor, Medicris alone had 22,000 subscribers in 2022, about 12% of the county's 187k employees. That indicates real local demand, now captured by MedLife **[Plausible]**.
- Prevention add-ons for employers will compete for room inside the €400 bundle, or sit in OH (a deductible legal obligation). **OH is the less contested entry point for an independent vendor** **[Plausible]**.

### Gaps
- No primary PwC study and no ANAF or INS data on the number of tax-exempt subscriptions.
- Medicover's subscriber count was not found.
- No subscription penetration data for Bihor.

## 5. Oradea/Bihor: verifiable OH providers, independent labs and clinics, elderly-care homes and home-care agencies

### Takeaway
Oradea has a **cluster of small, apparently independent OH cabinets**: Medimun SRL, Carimed Center, Clinica Endodigest, Alfa Medica, Gecoprosana and possibly Neoklinik. They sit alongside network-owned OH centres: Medicris/MedLife, MedLife Ronald Reagan, Regina Maria and Pelican/Medicover. Independent labs are scarce: Humanamed is the only one found. Independent multi-specialty clinics include GrandMed, NewMedics, Medena and Ovidius. **Private elderly-care homes could not be verified**, and the only home-care provider found is Caritas Eparhial Oradea (2015 record) **[Strong emerging; ownership of the "independents" not checked in company registries]**.

### Cited Findings

**OH providers: network-owned (IT and contracts likely decided centrally)** **[Established]**
- **Medicris Oradea (MedLife since June 2022)**:
  - "the largest OH and related-services centre in Bihor", 20+ years old
  - 9 specialties (OH, ophthalmology, internal medicine, ENT, psychology…)
  - **22,000+ subscribers**
  - acquired through Genesys Arad
  - Sources: [MedLife release](https://www.medlife.ro/comunicat-de-presa/medlife-bifeaza-o-noua-tranzactie-la-oradea); [Economica.net](https://www.economica.net/medlife-preia-compania-medicris-oradea-cel-mai-mare-centru-de-medicina-muncii-si-servicii-conexe-din-judetul-bihor_594049.html); [StartupCafe](https://startupcafe.ro/companie-servicii-medicale-private-medlife-tranzactie-oradea-htm-19982); [Revista Biz](https://www.revistabiz.ro/medlife-achizitioneaza-pachetul-integral-de-actiuni-al-societatilor-din-grupul-medicris-oradea/)
- **MedLife Ronald Reagan clinic (Oradea, 2025)**: OH, **road-safety medical and psychological exams for drivers of vehicles over 2.5 t**, outpatient care and lab under one roof; some specialties under CAS Bihor contract — [MedLife Ronald Reagan](https://www.medlife.ro/clinica-medlife-ronald-reagan)
- **Regina Maria – Centru de Medicina Muncii Oradea** (online booking) — [Regina Maria](https://www.reginamaria.ro/clinici/centru-de-medicina-muncii-oradea)
- **Spitalul Clinic Pelican (Medicover)**: has an OH department (prior note).

**OH providers: apparently independent (candidate pilots; verify ownership on Termene/ONRC)** **[Strong emerging]**
- **Medimun SRL**: Str. Republicii 53/A, Oradea. Full OH services (hiring, adaptation, periodic, return to work). Appointments Mon–Fri 08:00–16:00, at its centre or at client sites. Tel. 0770.161.642 / 0259.421.101 — [medimun.ro](https://www.medimun.ro/); [Sfatul Medicului – Medimun](https://www.sfatulmedicului.ro/clinici/medimun-srl-centru-de-medicina-muncii_299)
- **Carimed Center ("Cabinet Medicina Muncii Bihor")**: Str. Rovine 10 (contact address nr. 17, ap. 2). Serves private companies, public institutions and PFAs in Oradea, Bihor and beyond. **Staff travel to employer sites by appointment.** Tel. 0770.453.086 / 0359.462.124 — [carimedcenter.ro – despre noi](https://carimedcenter.ro/despre-noi/)
- **Clinica Medicală Endodigest**: Str. Olimpiadei 5. Lists job-change exams and the individual medical file / fitness certificate. Tel. 0359-440.444 — [Sfatul Medicului – OH Oradea](https://www.sfatulmedicului.ro/clinici/medicina_muncii-oradea)
- Directory-only listings (some entries more than 2,400 days old):
  - **Alfa Medica**: Str. Tudor Vladimirescu 8
  - **Gecoprosana**: Str. George Enescu 16/1
  - **Humanamed**: also offers OH
  - Sources: [Pagini Aurii – medicina muncii Oradea](https://www.paginiaurii.ro/firmy/ORADEA/q_medicina+muncii/1/); [Cylex Oradea](https://oradea.cylex.ro/medicina+muncii.html); [Romedic – OH Bihor](https://www.romedic.ro/cabinete/medicina-muncii/bihor); [Sfatul Medicului – clinici OH Oradea](https://www.sfatulmedicului.ro/clinica/medicina_muncii-oradea)
- **Neoklinik**: listed in a directory for OH, general medicine, ozone therapy, lab tests and **home medical care**. Not otherwise verified — [Sfatul Medicului – control medical periodic Oradea](https://www.sfatulmedicului.ro/clinici/oradea/control_medical_periodic-fse474)

**Laboratories**
- **MedLife Genesys Oradea** (network): ISO 15189, online results. MedLife also runs collection points on Republicii and Decebal — [MedLife Genesys](https://www.medlife.ro/laborator-medlife-genesys-oradea); [MedLife Republicii](https://www.medlife.ro/punct-de-recoltare-medlife-oradea-republicii); [MedLife Decebal](https://www.medlife.ro/punct-de-recoltare-medlife-oradea-decebal) **[Established]**
- **Humanamed** (apparently independent):
  - founded 2003 on the site of the former Children's Polyclinic No. 1 lab in Oradea
  - hematology, biochemistry, immunology, microbiology, endocrinology, tumour markers, genetics, TORCH and Down screening
  - **CAS contract** for insured patients referred by GPs or specialists
  - accreditation and current status unverified
  - Source: [Sfatul Medicului – labs Oradea](https://www.sfatulmedicului.ro/arhiva-medicala/laboratoare-de-analize-medicale-oradea-pagina_5) **[Strong emerging, directory]**
- **Bioclinica Oradea**: a directory page titled "Bioclinica Oradea – laborator de analize medicale" appeared, but no address could be confirmed. **Still unverified** (same status as in the prior note).
- **Regina Maria / Biostandard** collection point (prior note). Synevo's Oradea presence was not checked.

**Independent or other private clinics (ownership not verified)** **[Strong emerging, directories]**
- **GrandMed (Clinica Medicală GrandMed)**: Calea Republicii 32. Diabetology, cardiology, psychiatry, endocrinology, nephrology, neurology, internal medicine and ultrasound, plus labs. **CAS contract**. Tel. 0359 804 334 — [grandmed.ro](https://www.grandmed.ro/); [Cybo Oradea internists](https://www.cybo.com/RO/oradea/internist)
- **Clinica NewMedics SRL**: Str. Vlădeasa 70. Day and continuous hospitalisation plus outpatient care in internal medicine, diabetes, gastroenterology, nutrition, dermatology, nephrology and pneumology. Tel. 0359 100 440. The city subdomain suggests more than one site — [oradea.clinica-newmedics.ro](https://oradea.clinica-newmedics.ro/)
- **Clinica Medena**: cardiology, dermatology, diabetes, endocrinology, laboratory, internal medicine, psychology — [oradeni.ro – private internal medicine](https://www.oradeni.ro/info/clinicispitale/with--medicina_interna-privat/)
- **Ovidius Clinical Hospital (Oradea)**: private hospital listed for urology, oncology, radiotherapy, neurology, neurosurgery, nephrology — [Sfatul Medicului – palliative Oradea](https://www.sfatulmedicului.ro/clinica-ingrijiri_paliative/oradea)
- **Euroclinic** and **Centrul de sănătate și imagistică medicală Maria**: named in directories only — [Sfatul Medicului – Oradea clinics p.3](https://www.sfatulmedicului.ro/clinici/oradea/page-3)
- Network-owned for comparison:
  - **Dr. Leahu** dental clinic Oradea (2019, €600k) — [ZF](https://www.zf.ro/companii/reteaua-de-clinici-dentare-dr-leahu-deschide-un-centru-de-19544612)
  - **Diaverum** dialysis Oradea — [BookDialysis](https://bookdialysis.com/en/romania/clinica-de-nefrologie-si-dializa-diaverum-oradea)
- Public: SCJU Bihor invested over 73m lei in 2025 — [Agerpres, 16 Mar 2026](https://agerpres.ro/sanatate/2026/03/16/bihor-investitii-de-peste-73-de-milioane-de-lei-la-spitalul-clinic-judetean-din-oradea-in-anul-2025--1537848)

**Elderly care and home care**
- **Asociația Caritas Eparhial Oradea**: a home care and assistance service for the elderly, on a **2015** Monitorul Oficial list of subsidised social services. **Asociația Caritas Catolica** is listed with a home-care centre. Current activity is unverified — [legeaz.net – MO 185/2015 list](https://legeaz.net/monitorul-oficial-185-2015/lista-2015-67-din-26022015) **[Strong emerging, dated]**
- **DASO Oradea** (municipal social-assistance directorate): its 2023 activity report covers day centres, residential centres and home-based services. It is the referral and licensing contact — [DASO 2023 report (eBihoreanul download)](https://www.ebihoreanul.ro/ebh/force_download/UmFwb3J0dWxfZGVfYWN0aXZpdGF0ZV9EQVNPX3BlbnRydV9hbnVsXzIwMjMucGRm)
- A small "Senior Care Oradea" home-visit project appears only in classified ads — [Publi24](https://www.publi24.ro/anunturi/servicii/menaj-ingrijire-persoane/bihor/oradea/) **[weak]**
- Licensed elderly homes are registered under social-service code **8730 CR-V-I** in a Ministry of Labour register. Argeș publishes such lists, but **no Bihor list was found** — [CJ Argeș example list, Jul 2026](https://www.cjarges.ro/documents/10865/3347732/Camine_pentru_persoane_varstnice_licentiate_raza_Judetului_Arges_23.07.2026.pdf/ac6869b9-6068-4403-9997-2568b72cc510)

### Inferences
- **Best-fit OH pilot candidates** are **Medimun SRL** and **Carimed Center**. Both visibly serve employers and do on-site exams, which means multi-employer scheduling: exactly the coordination pain an add-on would address. Endodigest, Alfa Medica and Gecoprosana come second **[Plausible]**.
- **Clinic pilots for follow-up and recall:** GrandMed (diabetology, cardiology, endocrinology, CAS contract) and NewMedics (diabetes, nutrition, gastro) treat chronic conditions where lab-driven recall matters **[Plausible]**.
- **Lab pilots:** Humanamed is the only independent lab found. Everything else in Oradea belongs to the networks, so lab-side integration in Bihor means a single small partner or nothing **[Plausible]**.
- Elderly care is **not a verifiable near-term pilot segment** from public sources **[Plausible]**.

### Gaps
- Ownership, CUI, turnover and headcount for Medimun, Carimed, Endodigest, Alfa Medica, Gecoprosana, Neoklinik, Humanamed, GrandMed, NewMedics, Medena and Ovidius were **not checked** (Termene and Listafirme not reached).
- The Bihor list of licensed elderly homes (DGASPC Bihor, Ministry of Labour register) and the CAS Bihor home-care contract list were not found.
- Bioclinica and Synevo collection points in Oradea are unverified.
- What software these cabinets use is unknown.

## 6. e-SănătateaMea and PIAS: published API or 2026 obligations for private software vendors; are non-CNAS private clinics affected?

### Takeaway
**No public developer API, sandbox or third-party read-access for e-SănătateaMea was found.** The 2026 obligations land on **CNAS-contracted providers and their software vendors**:
- From **1 Sep 2026**, referral slips, medical letters and home-care recommendations issued in third-party software must flow to the portal via the **SIUI interface specifications** (cnas.ro/siui).
- Electronic-ID card (CEI) use was **postponed**.
- Online booking via the platform becomes mandatory for CNAS-contracted providers in **Q4 2026** after a pilot.

I found **no 2026 provision obliging private clinics without a CNAS contract** to feed the record **[Established for the CNAS-contracted obligations; non-CNAS: no evidence found]**.

### Cited Findings
- CNAS asked providers that use their **own or third-party software** to contact their vendors and install compatible versions before the medical-forms component went live on 1 Sep 2026. Without the update, a referral or medical letter "may not appear in the portal even if issued". The technical specifications are at cnas.ro → "Informații furnizori" → "SIUI" → "Specificații de interfațare SIUI", and they are aimed at software producers "to ensure interoperability". The forms covered are referral slips to other specialties or for admission, medical letters, and home-care recommendations **[Established]** — [Alba24](https://alba24.ro/cnas-de-la-1-septembrie-formularele-medicale-vor-fi-disponibile-in-esanatateamea-ce-trebuie-sa-faca-furnizorii-de-servicii-1155597.html); [Wall-Street.ro – CNAS cere actualizarea aplicațiilor](https://www.wall-street.ro/articol/sanatate/cnas-cere-actualizarea-aplicatiilor-medicale); [CNAS SIUI](https://cnas.ro/siui/)
- **CEI not mandatory** for providers from 1 Sep 2026 because of the short adaptation window. Patients' access to services is not conditioned on CEI — [Wall-Street.ro](https://www.wall-street.ro/articol/sanatate/cei-nu-devine-obligatorie-pentru-medici-de-la-1-septembrie) **[Established]**
- The platform "is designed to work with the software already used by practices and hospitals". All CNAS-contracted providers will have to use it for **appointment management** (Q4 2026, after a pilot). Patients authenticate via **ROeID or via a CNAS-contracted provider** — [Economedia](https://economedia.ro/?p=369115); [Digi24 – law adopted](https://www.digi24.ro/digieconomic/digital/istoricul-medical-retetele-si-programarile-la-medic-vor-fi-disponibile-online-parlamentul-a-adoptat-legea-108035) **[Established]**
- **Law 45/2019 (DES):** the electronic health record is created when doctors from the units listed in **art. 30(1)** send a patient's first medical document, **without patient consent**. The snippets did not show whether units without a CNAS contract are covered by art. 30 — [Law 45/2019 PDF](https://www.hosptm.ro/files/juridic/2019/Legea-nr-45-din-8-martie-2019.pdf) **[Established text; scope unclear]**
- Context: CNAS's March 2026 announcement of DES access for every patient from summer 2026 — [Agerpres, 31 Mar 2026](https://agerpres.ro/sanatate/2026/03/31/seful-cnas-dosarul-electronic-de-sanatate-va-fi-disponibil-pentru-fiecare-pacient-incepand-cu-vara-a--1542731)
- Sources disagree on timing: the law passed by the Senate was described as effective from the second half of 2026, while CNAS communications say 1 Sep 2026 — [Economedia](https://economedia.ro/?p=369551)

### Inferences
- For a solo founder, **e-SănătateaMea is not a data source to build on** in 2026–2027. It offers no consented third-party read API, and private out-of-pocket encounters are likely absent from it. It is a **compliance surface** for CNAS-contracted customers, and the incumbents (icMED, BizMedica, MediNote, which already do SIUI) own that surface **[Plausible]**.
- **OH and employer prevention sit largely outside CNAS.** OH is employer-paid and not CNAS-reimbursed, so an OH-first product avoids PIAS/SIUI certification work in its first phase **[Plausible]**.
- The Q4 2026 booking mandate could push small CNAS-contracted clinics (e.g., GrandMed, Humanamed with CAS contracts) to rely on the national booking system. That weakens a standalone booking or recall product for them, unless it syncs with e-SănătateaMea **[Speculative]**.

### Gaps
- The content of the current SIUI/PIAS interface specifications (formats, authentication, whether REST or SOAP) was not read; cnas.ro was not fetched.
- I found no evidence that an e-SănătateaMea patient-consented data-sharing API (EHDS-style) is planned, nor any date for one.
- Whether art. 30(1) of Law 45/2019 covers private units without a CNAS contract, and any sanctions, are unconfirmed.
- No uptake numbers for e-SănătateaMea booking since the launch.
