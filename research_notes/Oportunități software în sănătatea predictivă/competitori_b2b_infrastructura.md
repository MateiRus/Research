# B2B healthcare software competitors: data infrastructure, interoperability, RPM, patient engagement/recall, clinical workflow automation and clinical AI (US/UK/Western Europe, plus AU/CA reference cases): company-by-company evidence for a solo founder in Romania

**Method and source-quality caveat (read first).** Research date: 2026-10-09. The egress proxy blocked every WebFetch of primary pages, including company pricing pages (cliniko.com, jane.app, heidihealth.com, tryterra.co, thryve.health, medplum.com) and press sites (TechCrunch, Sifted, BusinessWire, MobiHealthNews, TheNextWeb). The shared web-search budget for this turn (200 searches) ran out partway through. **Every fact below therefore comes from WebSearch result snippets, accessed 2026-10-09**, and the cited URL is the page the snippet came from. I could not open those pages to check them in full. The figures come in three kinds, marked throughout:
- (a) company or filing disclosures reported by press, e.g. Weave's 10-K-based results release and Doctolib's ARR via Sifted;
- (b) company marketing claims, e.g. Heidi's "2M consults/week";
- (c) third-party estimates from aggregators such as Latka, Sacra, Spendbase, CostBench, Capterra and usagepricing.com. Treat these as estimates, not facts.

Evidence labels: **[Established]**, **[Strong emerging]**, **[Plausible]**, **[Speculative]**.

The notes cover 29 companies plus a US reimbursement reference. Companies the brief asked for but where I found no usable evidence (Evidation, Particle Health beyond its litigation, Dentally, Jane pricing) are listed under Gaps.

---

## Objective: Company-by-company evidence: which B2B models are informative for a small software company?

### Takeaway
The most transferable lessons come from mid-sized, narrow vendors, not from mega-rounds:
- **Practice-software and messaging companies built over a decade:** Cliniko, Jane, Weave, Accurx, Semble.
- **Unglamorous plumbing:** Lifen, which went from secure document sending to EHR integration and was profitable at €20M+ ARR in 2025.
- **Small API businesses:** Thryve and Terra for wearables, Validic for devices.
- **Small specialized exits to a strategic buyer:** Kaiku Health (about €1.3M revenue, 35 staff, bought by Elekta) and Luscii (bought by OMRON).

The heavily funded AI scribes (Abridge, Heidi, Tandem, Nabla) show fast adoption but also commoditized per-clinician pricing ($0 free tiers up to about $150/user/month), plus regulatory creep into EU MDR Class IIa. That makes them a poor head-on target for a solo founder. **[Strong emerging]**

### Cited Findings

#### A. Summary evidence table (29 entries)

Legend: **V** = disclosed by the company, a filing or a regulator/NHS body (as reported in snippets). **C** = company marketing claim. **E** = third-party estimate. "RO fit" means how well part of the model transfers to a Romania/EU solo founder (High / Med / Low).

| # | Company (HQ, founded) | Segment | First narrow wedge → expansion | Who pays / model | Pricing seen (date, quality) | Traction (V/C/E) | Regulation / compliance seen | RO fit |
|---|---|---|---|---|---|---|---|---|
| 1 | **Cliniko** (AU, 2010) | Practice mgmt (allied health) | Booking + notes for physio/allied clinics; stayed focused | Clinic; flat SaaS by practitioner band | 1 practitioner $45/mo … 26–200 practitioners $395/mo ([CostBench](https://costbench.com/software/scheduling/cliniko/), E); conflicting $49/$99/$149 ([SchedulingKit](https://www.schedulingkit.com/pricing-guides/cliniko-pricing), E) | No VC; 2025 rev ≈$1.5M; ~14 staff ([Latka](https://getlatka.com/companies/cliniko.com), E, low confidence) | Not found | **High** (model) |
| 2 | **Jane App** (CA) | Practice mgmt (allied health) | Booking/charting for allied health → payments, telehealth (expansion detail not verified) | Clinic; per-practitioner SaaS | Not retrieved (site blocked) | 404–420 staff ([Built In](https://builtin.com/company/jane-app), [Bitscale](https://bitscale.ai/directory/jane-app), E); ~$100M revenue/ARR claimed (E, unverified); $4.7M run-rate 2018 ([Latka](https://www.getlatka.com/companies/janeapp), E); 2023 growth round $7.58M (E, conflicting) | Not found | **High** (model) |
| 3 | **Weave** (US, public: WEAV) | Patient comms/engagement for dental, optometry, vet SMBs | Phone + SMS for dental offices → payments, reviews, AI | Practice location; subscription + payments | Historical $499/mo (older VentureBeat article) ([VentureBeat](https://venturebeat.com/ai/utahs-weave-raises-37-5-million-for-its-patient-communication-software), old) | FY2025 revenue $239.0M (+17%), GM 72.1%, FCF $12.9M ([BusinessWire, 2026-02-18](https://www.businesswire.com/news/home/20260218591820/en/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/), V); net loss $28.1M ([StockTitan](https://www.stocktitan.net/financials/WEAV), V via aggregator) | US HIPAA (not checked) | **High** (recall/comms wedge) |
| 4 | **Lighthouse 360** / **Solutionreach** (US) | Dental recall / reminders | Automated recall + reminders tied to dental PMS | Practice; flat monthly | LH360 $329/mo + $299 setup ([SoftwarePundit](https://www.softwarepundit.com/node/40), E); Solutionreach Essentials $199/mo, Plus $249/mo ([Spendbase](https://www.spendbase.co/?p=36425), E); Capterra "from $329" ([Capterra](https://www.capterra.in/software/160916/solutionreach), E) | Not found | Not found | **High** |
| 5 | **Accurx** (UK, inc. 17 May 2016) | NHS GP/hospital messaging, online consultation | One-off SMS from the GP desktop → batch messaging, video, online consultation, self-booking, NHS App messages | NHS commissioners (ICBs) / practices; per-practice contracts | Regional award £1.41M (Humber & N. Yorks, Apr 2025–Mar 2026) ([Contracts Finder, 2025-06-16](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b), V) | "98% of practices in England"; peak 2M messages/day (G-Cloud pricing doc, C) ([G-Cloud doc](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/708675/281422867192066-pricing-document-2026-07-13-1411.pdf)); revenue €39.1M 2023 ([Dealroom](https://app.dealroom.co/companies/accurx), E) | NHS G-Cloud listed | **High** (wedge pattern) |
| 6 | **Doctolib** (FR) | Booking → practice software → AI | Online appointment booking → agenda/PMS, teleconsultation, clinical/financial suite, AI | Practitioner; per-practitioner monthly SaaS | €139–149/mo per practitioner (base); €199–298/mo top tier ([Spendbase](https://www.spendbase.co/?p=38167), E, ~2025); 2023: Agenda €139/mo, tele add-on €79/mo ([TheBrandHopper](https://thebrandhopper.com/2023/07/11/doctolib-history-founders-business-model-investors-funding/), E, older) | 2024 ARR €348M (+22.5%), loss €53.8M (vs €87.1M) ([Sifted](https://sifted.eu/articles/doctolib-results-2024), V) | Not checked | **Med** (pricing benchmark) |
| 7 | **Semble** (UK; formerly Heydoc) | Private-clinic EHR/PMS | EHR for UK private clinics → payments (Semble Pay), France | Clinic; per-user SaaS | ~£119/user/mo starting ([Pabau, competitor](https://pabau.com/blog/semble-pricing/); [Capterra UK](https://www.capterra.co.uk/software/181314/semble), E) | 1,700+ orgs, 80+ specialties UK+FR (C) ([Semble](https://www.semble.io/articles/sembles-ps30m-series-c-funding-explained)); £30M Series C ([Seedtable, 2026-06](https://seedtable.com/companies/semble/funding-rounds/series-c-2026-06)) | Not found | **Med** |
| 8 | **Healthie** (US) | EHR/PM infra for virtual & wellness practices | Nutrition/wellness practice software → API-first EHR for digital-health startups (expansion not verified) | Provider / digital-health company; per-provider tiers | Core $19.99 (10 clients), Essentials $49.99 (250), Plus $129.99, Group $149 per provider/mo ([SoftwareFinder](https://softwarefinder.com/emr-software/healthie/pricing); [Capterra](https://www.capterra.com/p/167439/Healthie/pricing/), E) | Series B led by TCV, amount unknown ([Preqin](https://www.preqin.com/data/profile/asset/healthie-inc-/235140)) | US HIPAA (not checked) | **Med** |
| 9 | **Canvas Medical** (US) | Developer-oriented EMR | EMR → FHIR R4 API/SDK, AI scribe ("Hyperscribe"), coding agent | Care-delivery orgs; **per monthly active patient** | Builder $4,000/mo incl. 1,000 MAP ([SaaSrat](https://saasrat.com/products/canvas-medical), E); Capterra: Clinic $499, Builder $3,950, Enterprise $9,950/mo ([Capterra](https://www.capterra.com/p/248163/Canvas/pricing/), E) | $24M Series B (M13), date unclear ([HIT Consultant](https://hitconsultant.net/?p=66900)) | US | **Low–Med** (pricing idea) |
| 10 | **Luma Health** (US) | Patient access/engagement for health systems | Reminders/scheduling → full patient access automation | Health systems, FQHCs; enterprise | Not found | $130M Series C 2021, total $160M; 550+ health systems/clinic networks (2021) ([Fierce Healthcare](https://www.fiercehealthcare.com/digital-health/patient-engagement-platform-luma-health-picks-up-130m-to-automate-provider-patient), V-old) | Not found | **Med** (pattern) |
| 11 | **Heidi Health** (AU) | Ambient AI scribe → "AI Care Partner" | Free scribe for individual clinicians → practice/enterprise, care partner | Clinician (self-serve) + practices/health systems | Free tier; Pro $90/user/mo, Practice $120 (cached Heidi page) ([Heidi](https://webflow.heidihealth.com/pricing)); Feb 2026 "Clinician" $150/user/mo ([VeroScribe](https://www.veroscribe.com/blog/heidi-health-review-2026); [Twofold](https://www.trytwofold.com/compare/heidi-health-pricing-2026-guide), E) | $65M Series B Oct 2025 at ~$465M valuation ([TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72); [DealStreetAsia](https://media.dealstreetasia.com/stories/blackbird-backed-heidi-raises-new-round-at-465m-valuation-458546)); 2M+ consults/week, 116 countries (C) ([HLTH](https://hlth.com/insights/news/heidi-health-secures-65m-to-scale-ai-care-partner-platform-globally-2025-10-07)) | Not verified | **Low** head-on; Med for Romanian-language niche |
| 12 | **Tandem Health** (SE) | AI scribe → "AI-native clinic OS" | Scribe → coding assistant, decision support → patient flow, triage, scheduling, patient comms | Care orgs; enterprise/per clinician (not verified) | Not found | $50M Series A Jun 2025 ([Tandem](https://www.tandemhealth.ai/sv/news-articles/tandem-secures-50m-to-build-an-ai-native-operating-system-for-clinical-workflows-across-europe), V); $100M Series B (Scaleup Europe Fund/EQT), total $160M ([TheNextWeb](https://thenextweb.com/news/tandem-health-100m-series-b-scaleup-europe-fund)); 10,000 care orgs, 14 markets (C) | **EU MDR Class IIa** for scribe, coding assistant, decision support ([TheNextWeb](https://thenextweb.com/news/tandem-health-100m-series-b-scaleup-europe-fund)) | **Low** head-on (regulatory signal) |
| 13 | **Nabla** (FR) | Ambient AI scribe | Free individual scribe → enterprise contracts, US health systems | Clinician + enterprise | Free (~30 consults/mo); Pro ≈$119/mo **unverified** ([usagepricing](https://usagepricing.com/blueprint/nabla); [Vantaige](https://vantaige.io/ai-tool/nabla), E) | $70M Series C Jun 2025, total ~$114–120M; 85,000 clinicians, 130 orgs mid-2025 (C) ([Dealroom](https://dealroom.co/companies/nabla/); [CB Insights](https://www.cbinsights.com/compare/nabla-vs-sayvant)) | Not verified | **Low** head-on |
| 14 | **Abridge** (US) | Ambient AI scribe (enterprise) | Patient-facing visit recorder → enterprise scribe embedded in Epic | Health systems; per clinician/yr or unlimited enterprise | ≈$2,500/clinician/yr ([Sacra](https://sacra.com/c/abridge/), E); $199–208/mo floor up to $300–600/mo ([usagepricing](https://usagepricing.com/blueprint/abridge), E) | ARR ≈$100M May 2025 (E) ([Sacra](https://sacra.com/research/abridge)); $300M Series E at $5.3B Jun 2025 ([Maginative](https://www.maginative.com/article/abridge-raises-300m-series-e-at-5-3b-valuation/)) | US | **Low** |
| 15 | **Lifen** (FR, 2015; formerly Honestica) | Document routing / hospital integration | Secure sending of medical documents/letters (hospital → GP) → automatic integration into the hospital EHR (DPI) → data platform | Hospitals (and private professionals) | Not found | "Lifen Care" profitable in 2025, ARR >€20M (C) ([FrenchWeb](https://www.frenchweb.fr/lifen-la-startup-qui-digitalise-lhopital-sans-jamais-apparaitre-a-lecran/454591); [Lifen co-founder post](https://lifen.substack.com/p/lifen-turned-10)); 800+ hospitals, 20,000 private professionals ([MACSF](https://macsf.fr/nos-produits-services/services-et-formations-macsf/lifen-la-messagerie-securisee-de-sante)) | FR health messaging ecosystem (not detailed) | **High** (wedge pattern) |
| 16 | **Redox** (US) | Integration engine / EHR connectivity | Single API to connect apps to hospital EHRs → network of 12,000+ orgs | Software vendors (ISVs) and providers; platform + connection + transaction fees | Fee structure only, no numbers ([Purpose Jobs posting](https://www.purpose.jobs/discover/companies/redox/jobs/93133409-senior-pricing-manager)) | 2024 rev ≈$181M (E) ([Latka](https://www.getlatka.com/companies/redoxengineredox)); 280+ ISVs, 11,900+ provider orgs, 95+ EHRs (C) ([Redox](https://www.redoxengine.com/case-studies)) | US | **Low** (US EHR market) |
| 17 | **Health Gorilla** (US) | Interoperability network / national record exchange | Diagnostic-test ordering marketplace (2014) → clinical data network (record retrieval) | Digital-health cos, labs, providers | Not found | $50M Series C 2022, total $80M ([Health Gorilla](https://healthgorilla.com/blog/health-gorilla-secures-50-million-in-series-c-funding), V); sued by Epic + 4 providers over alleged misuse of "treatment" access ([Healthcare IT News](https://www.healthcareitnews.com/news/epic-and-health-systems-sue-health-gorilla-and-data-companies)) | US HIPAA/TEFCA context | **Low** |
| 18 | **Particle Health** (US) | Record-retrieval API | API on top of national networks | Digital-health cos | Not found | Antitrust suit vs Epic survived motion to dismiss on core claims ([Healthcare IT News](https://www.healthcareitnews.com/news/epic-and-health-systems-sue-health-gorilla-and-data-companies)) | US | **Low** |
| 19 | **Medplum** (US, YC S22) | Open-source FHIR backend | Apache-2.0 FHIR server + SDK → hosted cloud | Developers/health startups; hosted SaaS + services | No public prices found ([AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-gfbi35l2l7mma): private offers) | Funding sources disagree 50×: $125k–$6.5M ([HealthcareDiscovery](https://healthcarediscovery.ai/companies/medplum/), E) | Not verified | **High** as a *tool* for the founder |
| 20 | **Thryve** (DE, Berlin) | Wearable/health-data API | Unified API for 100+ wearable APIs (500+ devices) → health analytics/assessments | Insurers, DiGA makers, pharma, CROs | Not retrieved | €4M Series A Aug 2024 (Capricorn, IBB, CRB, Carma) ([Tech.eu, 2024-08-30](https://tech.eu/2024/08/30/german-thryve-secures-4m-series-a-to-accelerate-international-growth/), V); customers in 20+ countries (C); AOK, Sanitas, TK named (E) ([invest-in.berlin](https://www.invest-in.berlin/n/thryve-a-game-changer-for-preventive-healthcare/)) | "GDPR-compliant, ISO-certified" (C via aggregator) ([parsers.vc](https://parsers.vc/startup/thryve.health/)) | **Med–High** (EU-native API; or as a supplier) |
| 21 | **Terra** (UK/US, YC) | Wearable data API ("Plaid for fitness data") | Unified API for 500+ apps/wearables/labs | Developers, health/fitness apps | Consumption pricing ([TechCrunch 2021](https://techcrunch.com/2021/06/09/terra-raises-2-8m-to-build-the-plaid-for-fitness-data)); "from $499" unverified ([FitGap](https://us.fitgap.com/products/terra-api), E) | $2.8M seed 2021 (V); total ~$2.9–3.3M (E) ([CB Insights](https://www.cbinsights.com/company/terra-2/financials)) | Not verified | **Med** (supplier) |
| 22 | **Validic** (US) | Device-data integration for RPM | Device data aggregation → bought Infometers, Trapollo → acquired by ChartSpan (CCM/RPM services) Jun 2026 | Health systems, RPM programs | Not found | Acquired by ChartSpan 2026-06-22, terms undisclosed; 700+ devices, 20M connected lives (C) ([HIT Consultant](https://hitconsultant.net/2026/06/22/chartspan-acquires-validic-remote-patient-monitoring/)) | US | **Low** |
| 23 | **Luscii** (NL, 2018) | RPM / virtual wards | Home-measurement app for hospital chronic care (NL) → NHS virtual wards (UK) → acquired by OMRON (Apr 2024) | Hospitals, NHS trusts/ICBs | G-Cloud listed ([G-Cloud](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/219340919489109)); prices not retrieved | OMRON acquisition Apr 2024 ([CB Insights](https://www.cbinsights.com/company/luscii)); SBRI award £211,333 (Jul 2024) ([SBRI](https://sbrihealthcare.co.uk/impact-case-studies/company-directory/luscii-healthtech-b-v), V) | Not verified | **Med** (EU public-payer RPM) |
| 24 | **Huma** (UK; formerly Medopad) | RPM / regulated platform | Hospital apps (Medopad) → RPM for pharma/clinics → "regulated cloud platform" → M&A (Aluna 2025) | Pharma, health systems, clinics | Not found | EU Class IIb SaMD Mar 2023 ([BioWorld](https://www.bioworld.com/keywords/32000-huma-therapeutics-ltd), V); ~45 layoffs citing revenue slowdown ([Sifted](https://sifted.eu/articles/uk-healthtech-huma-layoffs)) | **EU MDR Class IIb**, FDA 510(k) (C) ([StartupHub PR](https://www.startuphub.ai/ai-news/press-release/2025/huma-therapeutics-acquires-aluna-and-secures-growth-partnership-with-eckuity-capital)) | **Low** (cautionary) |
| 25 | **Biofourmis** (SG→US) | RPM / hospital-at-home | AI analytics on biosensor data → care-at-home services; merged with CopilotIQ | US health systems, payers | Not found | Laid off 120 (48 US); CEO stepped down; US focus ([MobiHealthNews](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally)) | US | **Low** (cautionary) |
| 26 | **Kaiku Health** (FI; earlier corporate name Netmedi per CB Insights slug) | Oncology ePRO / symptom monitoring | Digital symptom monitoring for cancer patients → acquired by Elekta | Cancer centres / hospitals | Not found | 2019 revenue €1.3M, 35 staff; acquired by Elekta May 2020, price undisclosed ([ArcticStartup](https://arcticstartup.com/kaiku-health-exits-elekta/?amp=1); [CB Insights](https://www.cbinsights.com/company/netmedi)) | Not verified | **Med–High** (niche-exit pattern) |
| 27 | **Lindera** (DE, 2017) | Fall-risk / nursing-care AI | Smartphone-camera gait analysis for fall risk in care homes | Care facilities, insurers | Not found | 350+ care facilities/therapy centres (2021) ([Presseportal](https://www.presseportal.de/pm/156286/5083103), C); ~€6M Series A ([MobiHealthNews](https://www.mobihealthnews.com/news/emea/german-based-lindera-secures-eu6m-series-investment)) | DiGA/DiPA status not verified | **Med** |
| 28 | **Cera** (UK) | Tech-enabled home care (service, not pure SaaS) | Home-care operator with in-house software/AI | NHS & local government (~90% of revenue) | n/a (care services) | >$300M annualised revenue (C); EBITDA+ 2023, FCF+ 2024 (C); $150M mostly debt Jan 2025 ([HLTH](https://hlth.com/insights/news/uk-healthcare-tech-leader-cera-secures-150m-to-expand-ai-driven-home-care-services-2025-01-14); [Sifted](https://sifted.eu/articles/cera-biggest-elderly-care-round)) | Care regulator (not checked) | **Low** (capital heavy) |
| 29 | **Docbook** (RO; reference, via sibling notes) | Booking marketplace (Romania) | Online doctor booking | Doctors/clinics | Not retrieved here | ~7,500 doctors in 225+ cities (Aug 2024); 500k+ cumulative bookings ([Ziarul News](https://ziarulnews.ro/2024/08/28/docbook-depaseste-500-000-de-programari-online-77-dintre-pacienti-verifica-recenziile-inainte-de-a-alege-un-medic/); [Forbes.ro](https://www.forbes.ro/peste-500-000-de-programari-online-la-medici-prin-platforma-docbook-77-dintre-pacienti-sunt-atenti-la-recenzii-405930)) (from sibling research notes, not re-verified) | RO/GDPR | Local competitor/partner |

#### B. Company cards (detail beyond the table)

**1. Cliniko (Australia), bootstrapped practice management for allied health**
- Latka estimates 2025 revenue of **$1.5M**, founded 2010, "without raising any venture capital", about **14 employees** (reached in September 2025), and a "most recent disclosed valuation" of $4.6M. All of this is unverified aggregator data — [Latka](https://getlatka.com/companies/cliniko.com)
- Pricing is by practitioner band: 1 practitioner $45/mo; 2–5 $95; 6–8 $145; 9–12 $195; 13–25 $295; 26–200 $395. The currency (AUD or USD) is not shown in the snippet — [CostBench](https://costbench.com/software/scheduling/cliniko/). SchedulingKit gives different tiers: Solo $49, 2–5 $99, 6–10 $149, 11–30+ $249–349. It also says there is no free plan, only a 30-day trial — [SchedulingKit](https://www.schedulingkit.com/pricing-guides/cliniko-pricing). The sources conflict, and cliniko.com was blocked.
- Takeaway: flat, transparent, band-based pricing with no per-patient fees and no VC. **[Strong emerging]** that it is bootstrapped. **[Plausible]** for the size figures, because the Latka numbers look low for a product of this reach and need checking.

**2. Jane App (Canada), allied-health practice management**
- Headcount is about **404** ([Built In](https://builtin.com/company/jane-app)) or **420** ([Bitscale](https://bitscale.ai/directory/jane-app)). Latka gives an older figure of 340 and a **2018 revenue run-rate of $4.7M** ([Latka](https://www.getlatka.com/companies/janeapp)). Profiles mention "~$100M ARR in late 2024" but no primary source backs it. One source claims a **$7.58M growth equity round on 2023-10-01** (total $16.9M), which contradicts the "bootstrapped" label ([Dealroom](https://app.dealroom.co/companies/jane_4)). **[Plausible]**: Jane was long self-funded and later took minority growth capital, but this is not verified.

**3. Weave (US, NYSE: WEAV), patient communications for dental/optometry SMBs**
- FY2025 revenue was **$239.0M**, up 17.0% from $204.3M. Q4 2025 revenue was $63.4M, GAAP gross margin 72.1% and free cash flow **$12.9M** — [BusinessWire, 2026-02-18](https://www.businesswire.com/news/home/20260218591820/en/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/). The GAAP net loss was **$28.1M** — [StockTitan](https://www.stocktitan.net/financials/WEAV). **[Established]**
- It targets "small and medium dental, medical, veterinary, and optometry businesses" — [Telarus](https://www.telarus.com/suppliers/weave/). Dental is about 45% of customers by one unverified estimate — [BMC template blog](https://businessmodelcanvastemplate.com/blogs/target-market/weave-target-market). An older funding article cites "thousands of customers" paying **$499/month** — [VentureBeat](https://venturebeat.com/ai/utahs-weave-raises-37-5-million-for-its-patient-communication-software) (old).
- Lesson: a narrow comms wedge into dental offices compounds into a $239M-revenue public company. It still had not reached GAAP profit in 2025. **[Established]**

**4. Lighthouse 360 and Solutionreach (US), dental recall/reminders**
- Lighthouse 360 costs **$329/mo**, has no long-term contract and charges a **$299 one-time setup fee**. Physical mail is $1 per postcard and $2 per letter — [SoftwarePundit](https://www.softwarepundit.com/node/40) (undated). A 2021 promo offered $99/mo for 6 months, now expired — [LH360](https://www.lh360.com/cyberweek).
- Solutionreach: Essentials **$199/mo** (includes recall), Plus **$249/mo**, Enterprise custom — [Spendbase](https://www.spendbase.co/?p=36425). Capterra shows "starting $329, flat-rate" — [Capterra](https://www.capterra.in/software/160916/solutionreach). G2 says no vendor pricing is published — [G2](https://g2.com/products/solutionreach/pricing). One blog estimates $300–500/mo per location — [AppPricingLab](https://saas.apppricinglab.com/alternatives/solutionreach).
- **[Strong emerging]**: US dental recall/reminder SaaS sells at roughly **$200–350 per location per month**, flat-rate.

**5. Accurx (UK), the clearest "narrow wedge to platform" case in Europe**
- Incorporated 17 May 2016 (company 10184077) — [Companies House](https://find-and-update.company-information.service.gov.uk/company/10184077/filing-history?page=2). The founders met at Entrepreneur First — [EF](https://www.joinef.com/companies/accurx/?pagenum=2). Funding: Series A £8.8M led by Atomico — [TechCrunch](https://techcrunch.com/?p=1787850); Series B £27.5M (Sept 2021, Lakestar) — [Wellfound](https://wellfound.com/company/accurx/funding).
- Scale claims: "used by 98% of practices in England", reaches up to 60M patients, message volume peaked at **2M/day**, and it is "the largest sender of messages into the NHS App" — [G-Cloud pricing doc 2026-07](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/708675/281422867192066-pricing-document-2026-07-13-1411.pdf) (C)
- Buyer: NHS commissioners. One example is a **£1.41M** regional contract (Humber & North Yorkshire, Apr 2025–Mar 2026) covering online/video consultation, appointment reminders, booking and SMS — [Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b). The cost of SMS fragments is a real issue: NEL ICB asked practices to cut text fragments and was "reviewing funding arrangements" — [NEL ICB letter, 2024](https://primarycare.northeastlondon.icb.nhs.uk/wp-content/uploads/2024/09/Letter-to-practices-on-text-messages-and-fragments-usage-1-1.pdf)
- Revenue: Dealroom shows €1.3M (2018) rising to **€39.1M (2023)**, but it is unclear whether that is reported or estimated — [Dealroom](https://app.dealroom.co/companies/accurx). **[Plausible]**
- Partnership: Tandem's scribe is distributed via Accurx, giving "200,000+ NHS professionals" access — [Vestbee](https://vestbee.com/insights/articles/tandem-health-lands-100-m) (C)

**6. Doctolib (France/Germany/Italy/NL), booking to practice software to AI**
- 2024 ARR was **€348M**, up 22.5%. The loss narrowed 38% to **€53.8M** (from €87.1M) — [Sifted](https://sifted.eu/articles/doctolib-results-2024); confirmed by [Ärzteblatt](https://www.aerzteblatt.de/news/doctolib-umsatz-gesteigert-weiter-in-verlustzone). Sifted's sources say it is already profitable in France, which Doctolib declined to confirm. A 2025 forecast of €420M+ ARR and EBITDA breakeven is a third-party projection — [healthcare.digital](https://www.healthcare.digital/single-post/doctolib-s-potential-3-year-strategic-outlook-2026-to-2028-ipo-ai-and-international-expansion). **[Established]** for 2024. **[Speculative]** for 2025.
- Pricing (third party, about 2025): free online-presence tier; **€139–149/mo per practitioner** for the patient-base tier; €135–149/mo plus mandatory add-ons from about €30/mo for the clinical and financial suite; **€199–298/mo** for the top tier plus setup fees — [Spendbase](https://www.spendbase.co/?p=38167). In 2023: Agenda €139/mo, Médecin €135/mo, teleconsultation add-on €79/mo, Agenda annual €1,668 — [TheBrandHopper](https://thebrandhopper.com/2023/07/11/doctolib-history-founders-business-model-investors-funding/). In about 2015 it was €109/mo — [MobiHealthNews](https://www.mobihealthnews.com/news/french-startup-doctolib-raises-28m-online-appointment-booking-platform) (old).

**7. Semble (UK; formerly Heydoc), private-clinic EHR/PMS**
- CB Insights indexes Semble under the "heydoc" slug — [CB Insights](https://www.cbinsights.com/compare/heydoc-1-vs-yourdoctors). Series C was **£30M** (Revaia lead, Partech, Mercia, Octopus) — [Semble](https://www.semble.io/articles/sembles-ps30m-series-c-funding-explained); [Seedtable (dated 2026-06)](https://seedtable.com/companies/semble/funding-rounds/series-c-2026-06). An earlier Series B of about €13.8M (Mercia) funded expansion into France — [Silicon Canals](https://siliconcanals.com/?p=55955).
- Claims "1,700+ healthcare organisations across 80+ specialities" in the UK and France (C).
- Pricing is "from about **£119 per user/month**". The source is a competitor (Pabau). Booking, reminders and Semble Pay sit on higher tiers — [Pabau](https://pabau.com/blog/semble-pricing/); Capterra lists a £119 starting price, flat-rate — [Capterra UK](https://www.capterra.co.uk/software/181314/semble). **[Plausible]**

**8. Healthie (US)**
- Per-provider tiers (third party, 2025–26): Core $19.99/mo (10 active clients), Essentials $49.99 (250 clients), Plus $129.99 (unlimited), Group $149. About 17% off for annual billing — [SoftwareFinder](https://softwarefinder.com/emr-software/healthie/pricing); [Capterra](https://www.capterra.com/p/167439/Healthie/pricing/); [Toolradar](https://toolradar.com/tools/healthie/pricing)
- Series B led by TCV. The amount was not visible in the snippet — [Preqin](https://www.preqin.com/data/profile/asset/healthie-inc-/235140)
- Note: pricing is capped by **active-client count** at low tiers, which keeps the solo-practitioner entry price very low. **[Strong emerging]**

**9. Canvas Medical (US)**
- Prices by **monthly active patients**, not seats. Builder is **$4,000/mo** with unlimited users and the first 1,000 MAP, and rises with patient volume. It bundles a FHIR R4 API, SDK, "Hyperscribe" AI and a claim coding agent — [SaaSrat](https://saasrat.com/products/canvas-medical). Capterra shows Clinic $499, Builder $3,950 and Enterprise $9,950 per month — [Capterra](https://www.capterra.com/p/248163/Canvas/pricing/). The two sources conflict. **[Plausible]**
- Funding: $24M Series B led by M13, date not visible — [HIT Consultant](https://hitconsultant.net/?p=66900). Earlier funding was just over $3M (Upfront) — [MobiHealthNews](https://www.mobihealthnews.com/news/canvas-medical-bumps-total-funding-above-3m-launches-administrative-platform)

**10. Luma Health (US)**
- **$130M Series C** led by FTV Capital, total $160M (2021). At that time it served "550+ health systems, hospitals, FQHCs and clinic networks" — [Fierce Healthcare](https://www.fiercehealthcare.com/digital-health/patient-engagement-platform-luma-health-picks-up-130m-to-automate-provider-patient). Earlier $16M Series B (Aug 2019, PeakSpan) — [PeakSpan](https://peakspancapital.com/partnerships-news/patient-engagement-leader-luma-health-raises-16-million-to-accelerate-delivery-of-modern-patient-access-technology). There is no data after 2021. **[Established]** (2021 only)

**11. Heidi Health (Australia), AI scribe**
- **US$65M Series B** led by Point72 (Oct 2025), with Blackbird, Headline and LocalGlobe, at a reported **US$465M valuation** — [TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72); [DealStreetAsia](https://media.dealstreetasia.com/stories/blackbird-backed-heidi-raises-new-round-at-465m-valuation-458546). A A$27M Series A top-up followed in March 2025 — [SmartCompany](https://www.smartcompany.com.au/startupsmart/heidi-health-98-million-raise-valuation-704-million). Total raised is about $86.6–100M, depending on source ([Sacra](https://sacra.com/c/heidi-health/)).
- Company claims: "18M hours returned" in 18 months; "2M+ consultations/week in 110 languages across 116 countries" — [HLTH](https://hlth.com/insights/news/heidi-health-secures-65m-to-scale-ai-care-partner-platform-globally-2025-10-07). A snippet attributes "used by more than 60% of NHS GPs" to Digital Health — [Digital Health](https://www.digitalhealth.net/?p=244853). Not verified. **[Plausible]**
- Model: free tier with limits. Pro was **US$90/user/mo** (annual) and Practice US$120 on a cached Heidi page — [Heidi pricing (cached)](https://webflow.heidihealth.com/pricing). After a February 2026 restructure, the "Clinician" plan is **$150/user/mo** — [VeroScribe](https://www.veroscribe.com/blog/heidi-health-review-2026); [Twofold](https://www.trytwofold.com/compare/heidi-health-pricing-2026-guide). Sacra describes "unlimited users within practices, billing tied to usage" — [Sacra](https://sacra.com/c/heidi-health/).
- Revenue is **not disclosed** in anything I found.

**12. Tandem Health (Sweden), AI scribe to clinic OS**
- **$50M Series A** led by Kinnevik with Northzone, Amino and Visionaries; total $59.5M ([Tandem, 2025-06-30](https://www.tandemhealth.ai/sv/news-articles/tandem-secures-50m-to-build-an-ai-native-operating-system-for-clinical-workflows-across-europe)). Kinnevik describes it as a €40M round ([Kinnevik](https://www.kinnevik.com/insights/tandem-health-funding-round/)).
- **$100M Series B** led by the EU-backed Scaleup Europe Fund (EQT-managed), announced 14 September (the year is not shown in the snippet; most likely 2026); total $160M; valuation undisclosed — [TheNextWeb](https://thenextweb.com/news/tandem-health-100m-series-b-scaleup-europe-fund)
- Claims "10,000 care organisations in 14 European markets", including Ramsay Santé and Humanitas. Accurx gives 200k+ NHS professionals access (C) — [Vestbee](https://vestbee.com/insights/articles/tandem-health-lands-100-m)
- **Regulation: scribe, coding assistant and decision support are certified EU MDR Class IIa** — [TheNextWeb](https://thenextweb.com/news/tandem-health-100m-series-b-scaleup-europe-fund). **[Strong emerging]**: EU scribe vendors are moving their products into regulated medical-device territory.
- Expansion: "AI-native Clinic Operating System" adding patient-flow management, triage, scheduling and patient communications — [Tandem](https://www.tandemhealth.ai/sv/news-articles/tandem-secures-50m-to-build-an-ai-native-operating-system-for-clinical-workflows-across-europe)

**13. Nabla (France), AI scribe**
- **$70M Series C** (June 2025; HV Capital and Highland Europe; with DST, Cathay, Build Collective); total about $114–120M. Company-claimed "5× revenue growth in the prior six months" — [Dealroom](https://dealroom.co/companies/nabla/); [CB Insights](https://www.cbinsights.com/compare/nabla-vs-sayvant)
- 85,000 clinicians and 130+ organisations by mid-2025 (C).
- Pricing: no official page; the /pricing URL returns 404. A free individual tier (about 30 consults/mo) is reported, plus Pro at about **$119/mo**, labelled "estimated_not_official" — [usagepricing](https://usagepricing.com/blueprint/nabla); [Vantaige](https://vantaige.io/ai-tool/nabla). The same comparison pages estimate Suki at about **$299/clinician/mo** and Abridge enterprise at **$2,500–7,200+/clinician/yr** — [rfp.wiki](https://www.rfp.wiki/specialty-industries/healthcare-life-sciences/healthcare/ambient-clinical-documentation/nabla/abridge). **[Plausible]**

**14. Abridge (US), enterprise AI scribe**
- Sacra estimates ARR at **$60M (end 2024)** and **$100M (May 2025)**. Contracted ARR was $117M in Q1 2025 — [Sacra](https://sacra.com/research/abridge) (E)
- **$300M Series E at a $5.3B valuation** (June 2025, a16z), up 93% from $2.75B four months earlier — [Maginative](https://www.maginative.com/article/abridge-raises-300m-series-e-at-5-3b-valuation/)
- Deployments: Kaiser (24,600 physicians across 40 hospitals) and Mayo (2,000+). It reports 150 to 300+ health systems, depending on source — [Sacra](https://sacra.com/c/abridge/); [multiples.vc](https://multiples.vc/private-comps/abridge)
- No public prices. Estimates run from about $2,500/clinician/yr up to $300–600/clinician/mo for full deployments. Abridge is testing an "unlimited enterprise agreement" — [usagepricing](https://usagepricing.com/blueprint/abridge) (E)

**15. Lifen (France, founded 2015 as Honestica), document routing to integration**
- Funding: **€7.5M (2017)** from Daphni and Serena — [FrenchWeb](https://www.frenchweb.fr/lifen-leve-75-millions-deuros-pour-faciliter-lechange-de-documents-medicaux-entre-professionnels-de-sante/319039); **about €20M** led by Partech — [TechCrunch](https://techcrunch.com/?p=1841961); **€50M Series C (Nov 2021)** from Creadev and Lauxera — [FrenchWeb](https://www.frenchweb.fr/le-francais-lifen-leve-50-millions-deuros-pour-digitaliser-les-etablissements-de-sante/430093)
- In 2025 its historic business "Lifen Care" became **profitable** and passed **€20M ARR**; the company has **160 staff** — [FrenchWeb](https://www.frenchweb.fr/lifen-la-startup-qui-digitalise-lhopital-sans-jamais-apparaitre-a-lecran/454591); [Lifen co-founder Franck Le Ouay](https://lifen.substack.com/p/lifen-turned-10) (C, self-reported)
- Products: **Lifen Documents** sends medical documents. **Lifen Intégration** automatically files incoming documents into the hospital EHR (DPI); CHRU Nancy was an early user. Reach is 800+ hospitals and 20,000 private health professionals (2025) — [MACSF](https://macsf.fr/nos-produits-services/services-et-formations-macsf/lifen-la-messagerie-securisee-de-sante). The 2021 figure was "600 establishments, 240,000 doctors", a different definition.
- **[Strong emerging]**: unglamorous document and result routing became a profitable €20M ARR business, though only after about 10 years and roughly €77M+ raised.

**16. Redox (US), EHR integration platform**
- Latka estimates revenue at **$181M (2024)** and $162.3M (2023), with $146.1M raised — [Latka](https://www.getlatka.com/companies/redoxengineredox) (E)
- Redox posted a notice of a **14%** staff reduction (undated) — [Redox](https://www.redoxengine.com/?p=28293). Another source says it "lays off a quarter of their staff". The two figures conflict — [The Health Care Blog](https://thehealthcareblog.com/blog/tag/redox/)
- Pricing structure combines a **platform fee, connection pricing and transaction pricing** — [Redox job posting](https://www.purpose.jobs/discover/companies/redox/jobs/93133409-senior-pricing-manager)
- Network claim: 280+ ISVs, 11,900+ provider organisations, 95+ EHRs — [Redox](https://www.redoxengine.com/case-studies) (C)

**17–18. Health Gorilla and Particle Health (US), record retrieval and interoperability**
- Health Gorilla started in **diagnostic testing**. A 2014 headline reads "raises $1.2M for expansion in diagnostic test market" — [MedCity News, 2014](https://medcitynews.com/2014/08/startup-health-gorilla-raising-1-2m-expansion-diagnostic-test-markeet). It later raised a **$50M Series C (2022, SignalFire), total $80M** — [Health Gorilla](https://healthgorilla.com/blog/health-gorilla-secures-50-million-in-series-c-funding)
- **Epic and four providers** (Reid Health, Trinity Health, UMass Memorial, OCHIN) sued Health Gorilla on Jan 12 (year not in snippet). They allege that downstream customers pulled records under a "treatment" purpose and resold them, including to mass-tort law firms. Health Gorilla moved to dismiss and calls the suit anticompetitive — [Healthcare IT News](https://www.healthcareitnews.com/news/epic-and-health-systems-sue-health-gorilla-and-data-companies); [Healthcare IT News](https://www.healthcareitnews.com/news/health-gorilla-asks-court-throw-out-epics-request-jury-trial). Co-defendant GuardDog Telehealth settled and is permanently barred from TEFCA and Carequality — [HIPAA Journal](https://www.hipaajournal.com/guarddog-telehealth-admits-improper-access-to-medical-records/)
- Particle Health's antitrust suit against Epic (SDNY) survived a motion to dismiss on its core monopolization claims — [Healthcare IT News](https://www.healthcareitnews.com/news/epic-and-health-systems-sue-health-gorilla-and-data-companies)
- **[Established]**: US record-retrieval businesses carry large legal and platform risk, tied to Epic and to the HIPAA "permitted purpose" rules.

**19. Medplum (US), open-source FHIR backend**
- Most of the platform is **Apache 2.0**: FHIR server, APIs, SDKs, React components and CLI. "You are free to build products and businesses on top" — [Medplum](https://www.medplum.com/open-source)
- It makes money from a hosted service (api.medplum.com) and services — [API Evangelist](https://providers.apievangelist.com/providers/medplum/); [Caplight](https://www.caplight.com/company/medplum). YC S22, CEO Reshma Khilnani — [YC](https://ycombinator.com/companies/medplum). Funding figures disagree by about 50×: $125k (Tracxn), $550k (PitchBook), $6.5M (CB Insights) — [HealthcareDiscovery](https://healthcarediscovery.ai/companies/medplum/)

**20. Thryve (Berlin), wearable/health-data API**
- **€4M Series A** (Aug 2024) led by Capricorn Partners with IBB Ventures, CRB Health Tech and Carma Fund. The money funds international growth (customers in 20+ countries) and analytics/prevention — [Tech.eu, 2024-08-30](https://tech.eu/2024/08/30/german-thryve-secures-4m-series-a-to-accelerate-international-growth/). Techleap dates it Sept 2025, a conflict — [Techleap](https://finder.techleap.nl/news/feed/thryve-secures-4m-in-series-a-funding)
- One integration covers 100+ wearable APIs (Apple Watch, Oura and others). It already offers mental, cardiovascular and metabolic assessments — [Tech.eu](https://tech.eu/2024/08/30/german-thryve-secures-4m-series-a-to-accelerate-international-growth/). Another source says 500+ devices and a "GDPR-compliant and ISO-certified environment" — [parsers.vc](https://parsers.vc/startup/thryve.health/)
- Customers (aggregator, unverified): AOK, Sanitas, Techniker Krankenkasse; "50M people in Europe" — [invest-in.berlin](https://www.invest-in.berlin/n/thryve-a-game-changer-for-preventive-healthcare/). Target buyers are insurers, digital-health companies, pharma and CROs.

**21. Terra (London/US, YC)**
- **$2.8M** in June 2021 (General Catalyst, Samsung Next, NEXT Ventures). Described as "Plaid for fitness data" with **consumption pricing** in the style of Twilio and Plaid — [TechCrunch, 2021-06-09](https://techcrunch.com/2021/06/09/terra-raises-2-8m-to-build-the-plaid-for-fitness-data). Total raised is about $2.9–3.3M — [CB Insights](https://www.cbinsights.com/company/terra-2/financials); [Caplight](https://www.caplight.com/company/tryterra)
- Covers 500+ sources (Garmin, Apple Health, Oura, Fitbit, Whoop and others). The accelerator gives up to $100k in API credits — [Terra](https://tryterra.co/accelerator). "From $499" pricing is unverified — [FitGap](https://us.fitgap.com/products/terra-api). No revenue is disclosed.

**22. Validic (US)**
- **Acquired by ChartSpan** (a chronic-care-management services company) on 2026-06-22, with BIP Capital financing; terms undisclosed. Claims 700+ devices and 20M connected lives — [HIT Consultant](https://hitconsultant.net/2026/06/22/chartspan-acquires-validic-remote-patient-monitoring/). It earlier acquired Infometers ("44% more device integrations") — [MedCity News](https://medcitynews.com/?p=65862) and Trapollo, which made Cox an investor — [Citybiz](https://www.citybiz.co/?p=416876)
- **[Strong emerging]**: a standalone device-data API was absorbed by a **US CCM/RPM reimbursement-driven** service company.

**23. Luscii (Utrecht, 2018), RPM / virtual wards**
- Acquired by **OMRON Healthcare in April 2024** — [CB Insights](https://www.cbinsights.com/company/luscii)
- UK public-payer traction:
  - SBRI acute-virtual-ward award of **£211,333** (July 2024) — [SBRI Healthcare](https://sbrihealthcare.co.uk/impact-case-studies/company-directory/luscii-healthtech-b-v)
  - Welsh Ambulance pilot — [Giant Health](https://giant.health/blog/929/luscii-launches-remote-monitoring-pilot-with-sbri-)
  - NHS Dorset system-wide partnership (2025), building on OMRON's BP@Home, which claims a 71% cost saving — [NHS Dorset](https://nhsdorset.nhs.uk/luscii-and-nhs-dorset-partner-to-drive-system-wide-digital-healthcare-transformation/)
  - Graphnet/Luscii partnership (Stockport, March 2026) — [Stockport NHS](https://www.stockport.nhs.uk/news_25933)
  - Imperial heart failure (iCareConnect) — [Building Better Healthcare](https://www.buildingbetterhealthcare.com/nhs-and-remote-healthcare-innovator-partner-to-support-heart-failure-patients--177238)
- Outcome claim: a Leeds pilot (Jul 2023–Jun 2024) reported **47% of patients with fewer A&E visits** and **£398k+ net savings**. This is a vendor/partner evaluation — [Health Innovation Network](https://thehealthinnovationnetwork.co.uk/?p=12711). **[Plausible]**
- An aggregator claims about 70% of Dutch hospitals use it. The page looks AI-generated, so this is unverified — [Dealroom](https://app.dealroom.co/companies/luscii)

**24. Huma (UK; formerly Medopad), cautionary case**
- Formerly Medopad — [CB Insights](https://www.cbinsights.com/compare/luscii-vs-medopad)
- First **EU Class IIb SaMD** approval, March 2023 — [BioWorld](https://www.bioworld.com/keywords/32000-huma-therapeutics-ltd). Claims FDA 510(k) and a platform used by "4,500+ clinics in 70 countries" — [StartupHub PR, 2025](https://www.startuphub.ai/ai-news/press-release/2025/huma-therapeutics-acquires-aluna-and-secures-growth-partnership-with-eckuity-capital) (sponsored, C)
- Series D of **$80M+** with "revenue doubled year-on-year" and a target of profitability (C) — [Med-Tech News](https://med-technews.com/news/Digital-in-Healthcare-News/huma-completes-series-d-funding-round-with-over-80m-and-launches-cloud-platform)
- Later laid off about **45 staff**, citing "slowdown in revenues", clients cutting technology investment and a need to "focus on becoming profitable" (date not visible) — [Sifted](https://sifted.eu/articles/uk-healthtech-huma-layoffs)
- 2025: acquired Aluna (US respiratory, digital spirometry) with backing from Eckuity Capital — [StartupHub](https://www.startuphub.ai/ai-news/press-release/2025/huma-therapeutics-acquires-aluna-and-secures-growth-partnership-with-eckuity-capital)
- **[Established]**: heavy funding plus a Class IIb certification did not guarantee revenue growth.

**25. Biofourmis (Singapore→US), cautionary case**
- Laid off **120 globally (48 in the US)** to focus on "accelerating growth in the US market". The CEO stepped down a month later — [MobiHealthNews](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally); [MobiHealthNews](https://www.mobihealthnews.com/news/biofourmis-ceo-steps-down-month-after-global-layoffs). It merged with General Atlantic-backed CopilotIQ to form an "AI in-home care platform" — [Becker's](https://beckershospitalreview.com/digital-health/virtual-care-company-biofourmis-cuts-dozens-of-jobs.html). The year (about 2024) is inferred from article sequence.

**26. Kaiku Health (Finland), small specialized exit**
- Acquired by **Elekta** (radiotherapy medtech) with 100% of shares, effective 15 May 2020; terms undisclosed — [CB Insights](https://www.cbinsights.com/company/netmedi); [Elekta release](https://ir.elekta.com/files/Main/35/3115273/release.pdf); [Debiopharm](https://www.debiopharm.com/wp-content/uploads/2020/05/Kaiku_press_Release_REVISED-V5-250520-ENGLISH-FINAL.pdf)
- 2019: **€1.3M revenue, 35 employees**; Series A €4.4M; total about $6.3M — [ArcticStartup](https://arcticstartup.com/kaiku-health-exits-elekta/?amp=1). Debiopharm says the deal gives "thousands of cancer treatment centers" access to its digital patient monitoring — [Debiopharm](https://www.debiopharm.com/wp-content/uploads/2020/05/Kaiku_press_Release_REVISED-V5-250520-ENGLISH-FINAL.pdf). The data is from 2020, flagged as older.
- **[Established]**: a vendor with about €1M revenue in one clinical niche (oncology symptom monitoring) was strategically valuable to a medtech incumbent with matching distribution.

**27. Lindera (Berlin, 2017), fall-risk AI for nursing care**
- Uses ordinary smartphone cameras to analyse gait and flag fall risk. In 2021 it was used in **350+ care facilities and therapy centres in Germany**, with "long-term cooperations with customers and health insurers" — [Presseportal](https://www.presseportal.de/pm/156286/5083103); about €6M Series A — [MobiHealthNews](https://www.mobihealthnews.com/news/emea/german-based-lindera-secures-eu6m-series-investment). Data is from 2021.
- German context: DiGA costs are fully reimbursed by statutory health insurance (GKV). DiPA (care apps) are reimbursed by statutory long-term care insurance (SPV, SGB XI) and tied to care-level status — [pflegenetz.at presentation, 2026-02](https://www.pflegenetz.at/wp-content/uploads/2026/02/4.-Fachtagung-KI-und-Pflege-DiGA-und-DiPA-Jonas-Albert.pdf). Lindera's own DiGA/DiPA status was not verified.

**28. Cera (UK), tech-enabled home care (a service, not SaaS)**
- **$150M (Jan 2025), mostly debt** (BDT & MSD, Schroders) — [HLTH](https://hlth.com/insights/news/uk-healthcare-tech-leader-cera-secures-150m-to-expand-ai-driven-home-care-services-2025-01-14)
- Claims: EBITDA-positive 2023 and FCF-positive 2024 — [Healthcare Technology Report](https://thehealthcaretechnologyreport.com/cera-secures-150m-to-expand-ai-driven-home-healthcare/); "passing $300M annualised revenue"; **90% of revenue from public providers (NHS, local government)**; operating in the UK and Germany — [Sifted](https://sifted.eu/articles/cera-biggest-elderly-care-round) (C). Aggregator revenue estimates (about $62M) conflict — [Prospeo](https://prospeo.io/c/cera-revenue).

### Inferences
- Of the 29 entries, the ones closest to a solo founder's reality are Cliniko, Lighthouse/Solutionreach, Kaiku, Lindera and Thryve/Terra. All are small or mid-sized, narrow, and sell a clearly priced product to one buyer type. The scribe giants and RPM unicorns are useful mainly as **pricing anchors and warnings**. **[Plausible]**
- Two European exits (Kaiku → Elekta, Luscii → OMRON) and one US exit (Validic → ChartSpan) were all bought by companies with **distribution in the same niche** (a radiotherapy vendor, a BP-device maker, a CCM service). A solo founder's realistic "exit" is a sale to a regional PMS/EHR vendor, lab network or device distributor that already sells to the same clinics. **[Plausible]**
- Funding is not evidence of success here. Huma (Class IIb, $80M+ Series D) cut staff over slowing revenue; Biofourmis (unicorn) cut 120 and changed CEO; Weave is GAAP loss-making at $239M revenue; Doctolib was still losing €54M in 2024. **[Established]**

### Gaps
- **Evidation**, **Particle Health** (funding, revenue, pricing), **Dentally** (UK dental cloud), **Jane App pricing**, **Thryve/Terra/Medplum list prices**, **Luma pricing**, **Heidi/Nabla/Tandem revenue**: the search budget ran out or the primary pages were blocked. Nothing was found, so none is reported.
- No **regulatory class** was verified for Luscii, Kaiku, Lindera, Heidi or Nabla. Only Tandem (Class IIa) and Huma (Class IIb) have snippet evidence. Certification status for ISO 27001, NHS DSPT and HIPAA/SOC 2 was not verified for any company.
- Leads from background knowledge, **not verified in this session** (do not use without checking): Cliniko headcount may be well above Latka's 14; Jane was bootstrapped for most of its life; Health Gorilla is a designated TEFCA QHIN; Kaiku's ePRO has published survival or outcome studies.

---

## Q1: Which B2B health software models reached meaningful recurring revenue with small teams or bootstrapping?

### Takeaway
Clinic practice-management software sold by the practitioner seat, and narrow clinic-communication tools sold per location, are the only categories where bootstrapped or lightly funded companies show meaningful recurring revenue. Cliniko and Jane are the reference cases, though their numbers are mostly estimates. Lifen and Kaiku show that narrow plumbing or niche monitoring can reach profitability or a strategic exit, but both were VC-backed. No AI-scribe or RPM company in this set has evidence of bootstrapped success. **[Strong emerging]**

### Cited Findings
- **Cliniko**: no VC, founded 2010, est. **$1.5M** 2025 revenue, about 14 staff (estimates) — [Latka](https://getlatka.com/companies/cliniko.com). Pricing is transparent by practitioner band ($45–395/mo) — [CostBench](https://costbench.com/software/scheduling/cliniko/)
- **Jane App**: 2018 run-rate **$4.7M** with no reported funding at that time — [Latka](https://www.getlatka.com/companies/janeapp). Now **~400–420 staff** — [Built In](https://builtin.com/company/jane-app); [Bitscale](https://bitscale.ai/directory/jane-app). Claimed ~$100M ARR (unverified). A 2023 growth round of $7.58M is reported by one source — [Dealroom](https://app.dealroom.co/companies/jane_4)
- **Lifen**: profitable core business at **€20M+ ARR** in 2025, 160 staff, but about €77M+ in VC raised over 2017–2021 — [FrenchWeb](https://www.frenchweb.fr/lifen-la-startup-qui-digitalise-lhopital-sans-jamais-apparaitre-a-lecran/454591); [FrenchWeb Series C](https://www.frenchweb.fr/le-francais-lifen-leve-50-millions-deuros-pour-digitaliser-les-etablissements-de-sante/430093)
- **Kaiku Health**: **€1.3M revenue, 35 staff** (2019), total funding about $6.3M, then acquired by Elekta — [ArcticStartup](https://arcticstartup.com/kaiku-health-exits-elekta/?amp=1)
- **Weave**: $239M revenue and FCF-positive ($12.9M), but VC-funded and GAAP loss-making — [BusinessWire](https://www.businesswire.com/news/home/20260218591820/en/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/); [StockTitan](https://www.stocktitan.net/financials/WEAV)
- **Terra** built a 500+ source wearable API on about **$2.8–3.3M** total funding — [TechCrunch](https://techcrunch.com/2021/06/09/terra-raises-2-8m-to-build-the-plaid-for-fitness-data); [CB Insights](https://www.cbinsights.com/company/terra-2/financials). **Thryve** did so on a **€4M** Series A — [Tech.eu](https://tech.eu/2024/08/30/german-thryve-secures-4m-series-a-to-accelerate-international-growth/). Neither discloses revenue.
- **Cera** is profitable at the operating level (claimed), but it is a care-services company that depends on debt and public contracts — [Sifted](https://sifted.eu/articles/cera-biggest-elderly-care-round)

### Inferences
- **Practice management (PMS/EHR-lite) for allied-health and private clinics** is the archetypal bootstrappable B2B health SaaS. It has a clear buyer (the clinic owner), per-practitioner pricing, low regulatory burden (not a medical device) and high switching costs once records live there. The cost is a long build: Cliniko took about 15 years to reach an estimated ~$1.5M. **[Plausible]**
- For a solo founder with 10–12 h/week, a full PMS is too big a first product. Narrower add-ons that sit **next to** an existing PMS fit better: recall/reminders like Lighthouse, document/result delivery like Lifen Documents, or fall-risk screening like Lindera. **[Plausible]**
- The Kaiku data point (≈€1.3M revenue, strategic exit) suggests a narrow vendor does not need scale to be valuable, if it owns a niche workflow an incumbent wants. **[Plausible]**

### Gaps
- No verified revenue for Cliniko or Jane from company or filing sources. Cliniko's headcount and revenue may be badly underestimated by Latka.
- Bootstrapped European examples comparable to Cliniko (for example UK dental and allied-health PMS vendors) were not retrieved because the search budget was exhausted.

---

## Q2: Which narrow wedge products expanded into platforms, and how?

### Takeaway
The strongest European wedge stories share four traits: they start with **one message type**, they **attach to an existing system of record**, they **win by distribution** (NHS-wide, hospital-wide, or a free individual tier), and they expand along the same workflow into adjacent modules:
- Accurx: SMS → full GP comms
- Lifen: document sending → EHR integration
- Doctolib: booking → practice software → AI
- Tandem and Heidi: free or cheap scribe → coding, decision support and clinic OS

**[Strong emerging]**

### Cited Findings
- **Accurx**: started with SMS from the GP desktop. Now offers online/video consultation, appointment reminders, booking and batch SMS, paid through regional NHS contracts (e.g., £1.41M Humber & North Yorkshire) — [Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b). Claims 98% of English practices, peak 2M messages/day, and the largest sender into the NHS App — [G-Cloud doc](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/708675/281422867192066-pricing-document-2026-07-13-1411.pdf). It is now a **distribution channel** for third-party AI (Tandem's scribe reaches 200k+ NHS staff) — [Vestbee](https://vestbee.com/insights/articles/tandem-health-lands-100-m)
- **Lifen**: Lifen Documents (secure sending of medical documents) → Lifen Intégration (automatic filing into the hospital EHR/DPI) → "infrastructure for health digitisation". The original business turned profitable at €20M+ ARR — [FrenchWeb](https://www.frenchweb.fr/lifen-la-startup-qui-digitalise-lhopital-sans-jamais-apparaitre-a-lecran/454591); [Lifen post](https://lifen.substack.com/p/lifen-turned-10)
- **Doctolib**: in about 2015 it was online booking at about €109/mo — [MobiHealthNews](https://www.mobihealthnews.com/news/french-startup-doctolib-raises-28m-online-appointment-booking-platform). By about 2025 it had layered tiers: free presence → €139–149 base → clinical/financial suite → €199–298 top tier — [Spendbase](https://www.spendbase.co/?p=38167). 2024 ARR was €348M — [Sifted](https://sifted.eu/articles/doctolib-results-2024)
- **Tandem**: scribe → coding assistant and decision support (all MDR Class IIa) → "AI-native clinic OS" (patient flow, triage, scheduling, patient comms) — [Tandem](https://www.tandemhealth.ai/sv/news-articles/tandem-secures-50m-to-build-an-ai-native-operating-system-for-clinical-workflows-across-europe); [TheNextWeb](https://thenextweb.com/news/tandem-health-100m-series-b-scaleup-europe-fund)
- **Heidi**: free scribe → paid individual (Pro/Clinician) → Practice/enterprise → "AI Care Partner" — [HLTH](https://hlth.com/insights/news/heidi-health-secures-65m-to-scale-ai-care-partner-platform-globally-2025-10-07); [Heidi pricing (cached)](https://webflow.heidihealth.com/pricing)
- **Health Gorilla**: diagnostic-test ordering (2014) → national clinical-data network — [MedCity News](https://medcitynews.com/2014/08/startup-health-gorilla-raising-1-2m-expansion-diagnostic-test-markeet); [Health Gorilla](https://healthgorilla.com/blog/health-gorilla-secures-50-million-in-series-c-funding)
- **Thryve**: single wearable-data API → health assessments (mental, cardiovascular, metabolic) and prevention analytics — [Tech.eu](https://tech.eu/2024/08/30/german-thryve-secures-4m-series-a-to-accelerate-international-growth/)
- **Validic**: device-data aggregation → bought Infometers and Trapollo → absorbed by a CCM/RPM services company — [HIT Consultant](https://hitconsultant.net/2026/06/22/chartspan-acquires-validic-remote-patient-monitoring/); [MedCity News](https://medcitynews.com/?p=65862)
- **Huma/Medopad**: hospital apps → regulated RPM platform (Class IIb) → M&A roll-up (Aluna) — [BioWorld](https://www.bioworld.com/keywords/32000-huma-therapeutics-ltd); [StartupHub](https://www.startuphub.ai/ai-news/press-release/2025/huma-therapeutics-acquires-aluna-and-secures-growth-partnership-with-eckuity-capital)
- **Luscii**: hospital RPM in NL → NHS virtual wards and hypertension (UK) → acquired by a device maker (OMRON) — [CB Insights](https://www.cbinsights.com/company/luscii); [NHS Dorset](https://nhsdorset.nhs.uk/luscii-and-nhs-dorset-partner-to-drive-system-wide-digital-healthcare-transformation/)
- **Canvas Medical**: EMR → FHIR API/SDK + AI scribe + coding agent, priced per active patient — [SaaSrat](https://saasrat.com/products/canvas-medical)
- **Semble (Heydoc)**: UK private-clinic EHR → payments (Semble Pay) → France — [Pabau](https://pabau.com/blog/semble-pricing/); [Silicon Canals](https://siliconcanals.com/?p=55955)

### Inferences
Wedges that expanded share these mechanics. **[Plausible]**, a synthesis across the cases:
1. **Attach to the system of record rather than replace it** (Accurx on the GP EHR, Lifen into the DPI, Lighthouse on the dental PMS).
2. **Own a high-frequency message type** (reminders, results/letters, notes). Frequency creates data and habit.
3. **Add adjacent modules along the same workflow**: booking → reminders → payments → forms; or documents → integration → structured data.
4. **Distribution is the moat.** Accurx's near-universal NHS footprint lets it resell other vendors' AI.

Clinical-AI wedges (scribes) move **into** regulated territory as they expand; Tandem's coding and decision support are Class IIa. That is a cost a solo founder should avoid early. **[Strong emerging]**

For Romania, the analogous wedges are:
- results/document delivery from private labs and clinics to patients via SMS/WhatsApp/email;
- recall/reminders bolted onto local clinic software;
- a wearable data bridge built on Thryve/Terra rather than built in-house.

**[Speculative]** until other researchers confirm Romanian demand and willingness to pay.

### Gaps
- Exact timelines (year the second product launched) for Accurx, Lifen and Doctolib were not retrieved.
- No public evidence was found on how much revenue the expansion modules contribute versus the original wedge.

---

## Q3: Which models depend on US reimbursement (RPM CPT codes, CCM) and won't transfer to Romania?

### Takeaway
US RPM and CCM businesses (Validic's acquirer ChartSpan, Biofourmis/CopilotIQ, most US RPM vendors) are built on Medicare billing codes worth roughly $26–52 per code per patient per month. This revenue logic has no Romanian equivalent. US interoperability businesses (Health Gorilla, Particle, Redox) depend on US-specific networks (TEFCA/Carequality), HIPAA permitted-purpose rules and the Epic-dominated EHR market. Neither transfers. What transfers is the **clinic-paid SaaS** (PMS, recall, messaging, documents) and **public-payer or insurer contracts** (the NHS model via Accurx and Luscii; the German DiGA/DiPA model). **[Strong emerging]**

### Cited Findings
- 2026 Medicare RPM codes (vendor sources, national averages):
  - new **99445** (2–15 days of device data/month): about **$47–52**
  - **99470** (first 10 min of management with a real-time interaction): about **$26**
  - **99454** (16+ days): proposed at **$47.06**, up from $43.02
  - **99457**: about **$52**
  - **99458**: about **$41**
  - 99445 and 99454 cannot both be billed in a month
  - Sources: [Prevounce](https://blog.prevounce.com/medicares-2026-pfs-proposed-rule-supercharges-rpm); [ThoroughCare](https://www.thoroughcare.net/blog/2026-remote-patient-monitoring-cpt-codes); [Health Recovery Solutions](https://www.healthrecoverysolutions.com/blog/2026-rpm-and-ccm-reimbursement-codes-and-payment-updates); [Newswire](https://www.newswire.com/news/2026-new-remote-patient-monitoring-rpm-cpt-codes-22681195)
- CMS confirmed 99445 for FQHCs/RHCs retroactive to 2026-01-01 — [Prevounce, 2026-02-06](https://blog.prevounce.com/cms-confirms-cpt-99445-will-be-covered-for-fqhcs-and-rhcs-in-2026-rpm-programs). CMS also requested information on paying for SaaS — [McDermott+](https://www.mwe.com/?p=326656)
- **Validic** was absorbed by **ChartSpan**, a CCM/RPM care-management services company — [HIT Consultant](https://hitconsultant.net/2026/06/22/chartspan-acquires-validic-remote-patient-monitoring/)
- **Biofourmis** cut ex-US staff to focus on "accelerating growth in the US market" — [MobiHealthNews](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally)
- **Health Gorilla/Particle**: the business depends on US record-exchange frameworks (TEFCA/Carequality) and Epic's cooperation, and both are in litigation with Epic — [Healthcare IT News](https://www.healthcareitnews.com/news/epic-and-health-systems-sue-health-gorilla-and-data-companies); [Fierce Healthcare](https://www.fiercehealthcare.com/health-tech/epics-lawsuit-against-health-gorilla-raises-broader-issues-about-future-data-sharing)
- **Redox** sells into a US market of 95+ EHRs and 11,900+ provider organisations with platform, connection and transaction fees — [Redox](https://www.redoxengine.com/case-studies); [Redox job posting](https://www.purpose.jobs/discover/companies/redox/jobs/93133409-senior-pricing-manager)
- **Abridge**'s distribution is tied to **Epic** at US health systems (Kaiser, Mayo) — [Sacra](https://sacra.com/c/abridge/)
- European payer equivalents:
  - NHS commissioners pay for RPM and messaging (Luscii SBRI £211,333; Accurx £1.41M regional contract) — [SBRI](https://sbrihealthcare.co.uk/impact-case-studies/company-directory/luscii-healthtech-b-v); [Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b)
  - German statutory insurance pays DiGA costs (GKV) and DiPA costs (SPV, SGB XI) — [pflegenetz.at](https://www.pflegenetz.at/wp-content/uploads/2026/02/4.-Fachtagung-KI-und-Pflege-DiGA-und-DiPA-Jonas-Albert.pdf)
  - Cera gets ~90% of revenue from NHS and local government — [Sifted](https://sifted.eu/articles/cera-biggest-elderly-care-round)
- Romania context (from sibling research notes, not re-verified): CNAS-contracted providers must use the national **e-SănătateaMea** portal for online booking from Q4 2026 — [medic24](https://medic24.ro/portalul-esanatateamea-ajunge-la-promulgare-programari-online-din-trimestrul-iv/). Docplanner does not operate in Romania; Docbook is the local booking leader — [Docplanner](https://www.docplanner.com/); [Ziarul News](https://ziarulnews.ro/2024/08/28/docbook-depaseste-500-000-de-programari-online-77-dintre-pacienti-verifica-recenziile-inainte-de-a-alege-un-medic/)

### Inferences
- **Doesn't transfer:**
  - US RPM/CCM "bill the codes" businesses: the device + monitoring + billing service model that ChartSpan and Validic represent.
  - US national record retrieval (Health Gorilla, Particle).
  - US EHR-integration middleware (Redox).
  - Enterprise scribes sold through Epic (Abridge).

  **[Strong emerging]**
- **Transfers with changes:**
  - Clinic-paid recall/reminders and practice software (Lighthouse, Weave, Cliniko, Semble), at lower EU/RO price points.
  - Document and result routing (Lifen).
  - Wearable-data middleware (Thryve/Terra), as a buyer or reseller of the API rather than a builder.
  - Public-payer RPM (Luscii) only where a payer exists; this is unconfirmed for Romania.

  **[Plausible]**
- RPM in Romania would need a private payer: a private clinic network subscription, a corporate health plan, an insurer, or patient out-of-pocket. There is no equivalent of the US CPT revenue per patient per month. **[Plausible]**, with Romanian payer details left to other researchers.

### Gaps
- The official CMS final-rule amounts (Addendum B) were not retrieved; the figures are vendor-reported national averages.
- Whether Romanian CNAS or private insurers reimburse any remote monitoring or digital therapeutics was not researched here (outside scope or search budget).

---

## Q4: What pricing levels do clinics pay for patient engagement, recall, scribe and practice-management software in Europe (with US/AU anchors)?

### Takeaway
Verified official European price lists were not reachable. Third-party evidence gives these ranges (2024–2026):
- **Practice management + booking:** about **€119–150 per practitioner/month** (Doctolib €139–149 base, up to €298; Semble from about £119/user).
- **AI scribes:** **free tiers** up to **about $90–150 per clinician/month** for self-serve (Heidi), with enterprise at about $2,500+/clinician/year (Abridge, US).
- **US dental recall/reminder tools:** **about $199–499 per location/month**, flat (Solutionreach, Lighthouse 360, historical Weave).
- **Bootstrapped allied-health PMS:** about **$45–49/month for one practitioner**, scaling by band to about $395 (Cliniko).

**[Plausible]**: the price points come from aggregators.

### Cited Findings
| Category | Product | Price seen | Unit | Date / quality | Source |
|---|---|---|---|---|---|
| PMS + booking (EU) | Doctolib | €139–149/mo base; €135–149 + add-ons from ~€30; €199–298 top tier + setup | per practitioner/month | ~2025, aggregator | [Spendbase](https://www.spendbase.co/?p=38167) |
| PMS + booking (EU) | Doctolib | Agenda €139/mo; teleconsultation add-on €79/mo; annual €1,668 | per practitioner | 2023, aggregator | [TheBrandHopper](https://thebrandhopper.com/2023/07/11/doctolib-history-founders-business-model-investors-funding/) |
| Private clinic EHR (UK) | Semble | from ~£119 | per user/month | undated, competitor blog + Capterra | [Pabau](https://pabau.com/blog/semble-pricing/); [Capterra UK](https://www.capterra.co.uk/software/181314/semble) |
| Allied-health PMS (AU/global) | Cliniko | $45 (1) … $395 (26–200 practitioners), or $49/$99/$149/$249–349 | per account by practitioner band/month | 2025–26, aggregators (conflict) | [CostBench](https://costbench.com/software/scheduling/cliniko/); [SchedulingKit](https://www.schedulingkit.com/pricing-guides/cliniko-pricing) |
| EHR/PM (US) | Healthie | $19.99 / $49.99 / $129.99 / $149 | per provider/month | 2025–26, aggregators | [SoftwareFinder](https://softwarefinder.com/emr-software/healthie/pricing) |
| EMR platform (US) | Canvas | $499 / $3,950 / $9,950; or $4,000 incl. 1,000 active patients | per org/month; per monthly active patient | undated, aggregators (conflict) | [Capterra](https://www.capterra.com/p/248163/Canvas/pricing/); [SaaSrat](https://saasrat.com/products/canvas-medical) |
| Dental recall (US) | Lighthouse 360 | $329/mo + $299 setup; postcards $1, letters $2 | per practice/month | undated, review site | [SoftwarePundit](https://www.softwarepundit.com/node/40) |
| Recall/engagement (US) | Solutionreach | Essentials $199, Plus $249; Capterra "from $329"; blog est. $300–500 | per location/month | 2025–26, aggregators | [Spendbase](https://www.spendbase.co/?p=36425); [Capterra](https://www.capterra.in/software/160916/solutionreach); [AppPricingLab](https://saas.apppricinglab.com/alternatives/solutionreach) |
| Engagement (US) | Weave | $499 (historical) | per office/month | old article | [VentureBeat](https://venturebeat.com/ai/utahs-weave-raises-37-5-million-for-its-patient-communication-software) |
| AI scribe (AU/UK/EU) | Heidi | Free; Pro $90; Practice $120 (annual); "Clinician" $150 after Feb 2026 | per user/month (USD) | cached vendor page; 2026 reviews | [Heidi (cached)](https://webflow.heidihealth.com/pricing); [VeroScribe](https://www.veroscribe.com/blog/heidi-health-review-2026) |
| AI scribe (FR/EU/US) | Nabla | Free (~30 consults/mo); Pro ~$119 (unofficial) | per clinician/month | 2025–26, aggregator, flagged unofficial | [usagepricing](https://usagepricing.com/blueprint/nabla) |
| AI scribe (US) | Suki | ~$299 (estimate) | per clinician/month | aggregator | [rfp.wiki](https://www.rfp.wiki/specialty-industries/healthcare-life-sciences/healthcare/ambient-clinical-documentation/nabla/abridge) |
| AI scribe (US enterprise) | Abridge | ~$2,500/yr (floor ~$199–208/mo) up to $300–600/mo | per clinician | 2025–26, aggregator | [Sacra](https://sacra.com/c/abridge/); [usagepricing](https://usagepricing.com/blueprint/abridge) |
| Wearable API | Terra | consumption-based; "from $499" unverified; up to $100k credits for startups | usage | 2021 + aggregator | [TechCrunch](https://techcrunch.com/2021/06/09/terra-raises-2-8m-to-build-the-plaid-for-fitness-data); [FitGap](https://us.fitgap.com/products/terra-api); [Terra accelerator](https://tryterra.co/accelerator) |
| Integration engine (US) | Redox | platform fee + connection fee + transaction fee | per deal | job posting (no numbers) | [Redox job](https://www.purpose.jobs/discover/companies/redox/jobs/93133409-senior-pricing-manager) |
| NHS messaging (UK) | Accurx | £1.41M regional ICB contract (12 months) | per region via commissioner | 2025, public notice | [Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b) |

### Inferences
- **Scribe pricing is collapsing toward free at the bottom.** Heidi and Nabla offer free tiers, while enterprise per-clinician prices stay high in the US. For an RO/EU solo founder, a general-purpose scribe would compete with free, well-funded tools that already support many languages; Heidi claims 110. Differentiation would have to come from **Romanian-specific templates, outputs for the local EHR/CNAS forms, and integration with local clinic software**. Medical-device classification risk remains if it drifts into coding or decision support, as Tandem's Class IIa shows. **[Plausible]**
- **Per-location flat pricing (~$200–350/mo in the US)** for recall and reminders is the most solo-founder-compatible model. It is simple to sell, has no clinical-claims burden, and its ROI is easy to explain (filled hygiene chairs, fewer no-shows). Romanian price points would likely be a fraction of US levels. A working hypothesis of **€30–100 per location/month** is **[Speculative]** and must be validated by the Romania-focused researchers.
- **Per-practitioner PMS pricing in Western Europe (~€120–150)** is a ceiling reference only. A Romanian private clinic is unlikely to pay Doctolib-level prices per doctor. **[Speculative]**
- **Usage or active-patient pricing** (Canvas per MAP, Terra consumption, Redox per connection/transaction, Heidi usage-linked) works for infrastructure and API products. A solo founder could charge, for example, per result delivered or per active monitored patient, which lines cost up with SMS and LLM spend. Accurx's SMS-fragment cost issue shows why messaging cost must be passed through. **[Plausible]**

### Gaps
- **Official 2026 European list prices** for Doctolib, Semble, Heidi, Tandem, Nabla and Cliniko were not verified, because vendor pages were blocked.
- **No European recall/reminder-specific vendor prices** were retrieved (e.g., UK/DE dental recall tools, Doctolib reminder add-ons). This is the most important missing benchmark for a Romanian recall product.
- **Romanian clinic willingness to pay** for any of these categories was not researched here and is left to other researchers.
- **Opportunity summary for the solo founder** (synthesis, not a finding). In order of fit with ~€25k, 10–12 h/week, and Python/SQL/APEX/LLM/n8n skills:
  1. Recall/reminder and results-delivery automation that attaches to existing Romanian clinic, lab or dental software, sold per location per month (Lighthouse/Accurx/Lifen pattern). **[Plausible]**
  2. A GDPR-native wearable-data-to-clinician dashboard for a narrow niche (e.g., cardiology or sports medicine clinics), built on Thryve/Terra APIs rather than device integrations built from scratch. **[Speculative]**
  3. Romanian-language documentation templates and post-visit patient summaries using LLM APIs, positioned as administrative (not decision support) to stay outside MDR. **[Speculative]**, with regulatory risk signalled by Tandem's Class IIa.

  Avoid: US-style RPM billing models, national record retrieval, enterprise scribes, and anything needing Class IIa+ certification early. **[Strong emerging]**
