# Emerging enabling technologies, structural changes and payers for preventive/predictive health software (Europe + Romania), as of October 2026

**Method notes for the report writer:**
- Every WebFetch attempt was refused by the egress proxy (EGRESS_BLOCKED). That covered gkv-spitzenverband.de, forbes.com.au, barmer.de, romania-insider.com, pmc.ncbi.nlm.nih.gov, pressone.ro, health.ec.europa.eu and tryterra.co. As a result, **every fact below comes from search-engine result snippets or summaries** and should be read as "(search snippet)" unless stated otherwise.
- The shared WebSearch budget for this session ran out after about 26 queries. Several sub-topics are therefore listed under Gaps instead of being researched.
- Items marked **[BK]** are background knowledge from my training data (cut-off mid-2026). I did not verify them in this session and they have no URL. Verify them before relying on them.
- Evidence labels: **[Established]**, **[Strong emerging]**, **[Plausible]**, **[Speculative]**.
- Forecasts are labelled **FORECAST**. Observed or reported revenue is labelled **OBSERVED**.

---

## Q1. For each emerging area: what must become true for it to exist at scale, which early indicators to watch, and what "picks-and-shovels" software could be sold now?

### Takeaway
The enabling layers are scaling today: consumer sensors, cheap consumer diagnostics, ambient AI, EU data-portability law and operational AI. The clinical prediction markets built on top of them are not, because no one is yet paying routinely for prediction itself. Sellable now are the "plumbing" products (data intake and normalization, consent and portability, recall and outreach automation, documentation helpers) to buyers who already have budgets: private clinics, labs, employers and occupational-health providers. EHDS deadlines (2027, 2029, 2031) are the clearest forcing function for data-plumbing demand in Europe.

### Cited Findings

#### A. New continuous physiological data sources (rings, OTC CGM, cuffless BP, at-home sensors)
- **Oura (smart ring): OBSERVED revenue.**
  - Reported S-1 figures: fiscal-2025 revenue of **$907.9M**, up from **$406.8M** the year before — [BeInCrypto](https://beincrypto.com/oura-ipo-nasdaq-16-billion-valuation/).
  - Nine months to 30 June 2026: revenue of **$1.21B**, up from $697.6M (+74%) — [Forbes Australia](https://www.forbes.com.au/?p=207282).
  - Trailing four quarters to June 2026: about **$1.43B** — [BeInCrypto](https://beincrypto.com/oura-ipo-nasdaq-16-billion-valuation/).
  - The search summary also reports **5 million paying members as of 30 June 2026** across 56 markets, and **membership (subscription) revenue of $240.5M for the nine months (+121%)**. I could not tell whether these two figures come from Forbes AU or BeInCrypto — [Forbes Australia](https://www.forbes.com.au/?p=207282); [BeInCrypto](https://beincrypto.com/oura-ipo-nasdaq-16-billion-valuation/).
  - Sacra *estimates* 2025 revenue at about $1B, with roughly 80% from hardware and 20% from subscriptions. This is a third-party estimate, not a filing — [Sacra](https://sacra.com/research/oura).
  - Oura raised about $900M at about an **$11B valuation in October 2025**. It had sold **5.5M rings** cumulatively as of that round — [Fortune, 23 Sep 2025](https://www.fortune.com/2025/09/23/oura-ring-11-billion-valuation-series-e-finland-875-million-raise-unicorn); [HLTH, 15 Oct 2025](https://hlth.com/insights/news/oura-reaches-11b-valuation-becomes-europe-s-first-health-tracking-decacorn-2025-10-15).
  - Oura filed a confidential draft S-1 on **21 May 2026**. The IPO was set at "up to $2.2B", but I did not confirm whether it priced — [Forbes Australia](https://www.forbes.com.au/?p=207282).
  - Label: [Established] that consumers pay recurring fees for sleep and readiness tracking at the scale of millions.
  - The revenue figures reconcile if Oura's fiscal year ends 30 September. That is my inference, not a stated fact.
- **OTC CGM (Dexcom Stelo, Abbott Lingo).**
  - Stelo launched in the US in August 2024 at **$89/month (subscription) or $99 for two sensors** — [MedTech Dive](https://www.medtechdive.com/news/abbott-dexcom-over-the-counter-cgm-launch/719928/).
  - **OBSERVED:** Dexcom reported FY2025 revenue of $4.662B. **Stelo contributed about $130M in FY2025** per a search summary of earnings coverage, and **more than $100M in its first 12 months** per the Q3-2025 call — [SEC 8-K Q3 2025](https://www.sec.gov/Archives/edgar/data/1093557/000109355725000278/dxcm09302025-exhibit991.htm); [Motley Fool Q3 2025 call transcript](https://www.fool.com/earnings/call-transcripts/2026/04/08/dexcom-dxcm-q3-2025-earnings-call-transcript/); [Close Concerns memo](https://cckb.closeconcerns.com/r/b1d6f2e3/pdf).
  - **FORECAST vs reality:** in 2024, BTIG forecast **$190M Stelo and $134M Lingo sales for 2025**, and roughly $650M combined by 2026 — [MedTech Dive](https://www.medtechdive.com/news/dexcom-stelo-otc-cgm-insulet-tandem-type-2-diabetes/716335/). If the $130M figure is correct, Stelo came in about 30% below that forecast.
  - I found **no separate actual sales figure for Lingo**. Abbott reports CGM growth only in aggregate (+19.5% year on year in Q2 2025) — [BioWorld](https://www.bioworld.com/keywords/50592-lingo).
  - Signos received FDA clearance in August 2025 for an OTC glucose system combining Stelo with an AI platform, which shows "sensor + software" bundles getting cleared — [BioWorld](https://www.bioworld.com/keywords/50592-lingo).
  - Label: [Strong emerging] OTC CGM is a real, nine-figure market in the US but still small. [Plausible] Europe follows more slowly.
- **Cuffless BP.**
  - Aktiia's Hilo band (G0) received **FDA 510(k) clearance for OTC use around 8 July 2025**, the first cuffless OTC BP monitor in the US. It was validated against double auscultation in 140 patients — [MobiHealthNews](https://www.mobihealthnews.com/news/aktiia-gets-fda-clearance-otc-cuffless-blood-pressure-monitor); [HLTH](https://hlth.com/insights/news/aktiia-gets-fda-clearance-for-otc-cuffless-blood-pressure-monitor-2025-07-08); [Fierce Biotech](https://www.fiercebiotech.com/medtech/fda-clears-over-counter-cuffless-blood-pressure-monitor-hilo-bracelet).
  - In Europe it already held a **CE mark as a Class IIa device**. Cumulative sales were reported at **120,000–130,000 devices** (sources differ) — [BioAlps](https://bioalps.org/hilo-by-aktiia-received-fda-510k-clearance); [Notebookcheck](https://www.notebookcheck.net/Aktiia-G0-cuffless-blood-pressure-monitor-now-FDA-approved.1053807.0.html).
  - Label: [Strong emerging] that cuffless BP is entering regulated consumer use. [Plausible] that clinicians will accept it.
- **Whole-body scan / "prevention clinic" model (Neko Health, Sweden/UK).**
  - Neko raised **$260M in January 2025 at about $1.8B**, then **$700M in July 2026 at about $7B** — [Axios](https://www.axios.com/2025/01/23/spotify-founder-neko-health); [The Next Web](https://thenextweb.com/news/neko-health-700m-series-c-us-expansion).
  - It reports **more than 100,000 scans** in the UK and Sweden and **350,000 people on its waitlist**. The UK price is **£299 per scan** — [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/whole-body-imaging-firm-neko-health-raises-700m); [Axios](https://www.axios.com/2025/01/23/spotify-founder-neko-health).
  - No revenue is disclosed. The American College of Radiology does not recommend full-body scans, and Neko's outcome reports are self-selected cohorts without controls — [Axios](https://www.axios.com/2025/01/23/spotify-founder-neko-health); [ai2.work](https://ai2.work/blog/neko-health-s-700m-series-c-bets-full-body-ai-scans-go-mainstream).
  - Label: [Strong emerging] that affluent European consumers pay out of pocket for prevention "experiences". [Speculative] that this improves outcomes.
- **Integration and aggregation APIs (picks and shovels that already exist).**
  - **Terra** (unified wearable API) prices by active users/credits: "plans start at $399/month on the annual plan", and the pricing page lists Quick Start "from $499/month" with 100k credits. It claims Apple Health, Garmin, Fitbit, Google Fit, Samsung Health, Oura, WHOOP, Polar, Withings and blood-testing providers. Source counts conflict (500+ on one page, 90+ on a third-party listing) — [Terra pricing](https://tryterra.co/pricing); [Terra home](https://www.tryterra.co/); [FitGap](https://us.fitgap.com/products/terra-api).
  - **Thryve** (Berlin) offers SDK/API "harmonized data across 500+ devices", GDPR/ISO 27001 compliance and Health Connect support. It does not publish prices — [Thryve Health Connect](https://thryve.health/health-connect-api).
  - Thryve says Google Fit APIs are deprecated and new clients must use **Android Health Connect**. Its pages disagree on whether the shutdown date is 30 June 2025 or 2026 — [Thryve blog](https://thryve.health/blog/google-fit-api-deprecation-and-the-new-health-connect-by-android-what-thryve-customers-need-to-know/).
  - Label: [Established] that wearable-aggregation middleware is commoditised and venture-funded. A solo founder should consume these APIs, not compete with them.

#### B. Cheaper or more accessible diagnostics (at-home and finger-prick blood testing, consumer labs)
- European DTC lab-testing **FORECASTS conflict by about 5×**:
  - Meticulous Research: **$1.59B by 2032**, 10.8% CAGR — [Meticulous Research](https://www.meticulousresearch.com/pressrelease/875/europe-dtc-laboratory-testing-market-2032).
  - Another publisher: **$1.02B (2025) → $8.20B (2033)**, 29.8% CAGR — [Market Data Forecast](https://www.marketdataforecast.com/market-reports/europe-direct-to-consumer-laboratory-testing-market).
  - Neither is observed revenue. Do not use either as a market size.
- **Thriva (UK):** the only revenue figures found are early-stage (£2.2M turnover, "nearing £5M" the next year, undated Sifted interview). It had processed more than 115,000 at-home tests by 2020 — [Sifted](https://sifted.eu/articles/thriva-founder-interview); [UKTN 2020](https://www.uktech.news/news/proactive-health-company-thriva-secures-4m-funding-from-pan-european-venture-capital-firm-target-global-to-further-establish-at-home-health-service-20200526).
  - Thriva scaled mainly through **consumer subscriptions and employer/insurer benefit partnerships, not NHS commissioning** — [Bridgehead Communications](https://www.bridgeheadcommunications.com/medtech-index/thriva).
  - Label: [Strong emerging] that consumer lab testing in Europe is funded mainly B2C plus B2B2C (employers/insurers).
- I found no revenue data for Lykon or Cerascreen. A claim that "30% of DTC test complaints involved inaccurate information (EMA)" appeared only in a market-report summary with no primary source, so treat it as unverified — [Market Data Forecast](https://www.marketdataforecast.com/market-reports/europe-direct-to-consumer-laboratory-testing-market).

#### C. Preventive screening adoption (EU targets, Romania)
- **Europe's Beating Cancer Plan** aimed to **offer** breast, cervical and colorectal screening to **90% of eligible people by 2025** — [Digestive Cancers Europe](https://digestivecancers.eu/from-plans-to-patients-are-eu-cancer-screening-and-ncd-policies-delivering/).
  - The **May 2025 mid-term review** identified regions with participation below 60% through the European Cancer Inequalities Registry. It cited **€300M under EU4Health** for rolling out screening — [World Bladder Cancer Patient Coalition, 27 May 2025](https://worldbladdercancer.org/news_events/europes-beating-cancer-plan-mid-term-review-key-takeaways/).
- The **European Cancer Organisation's November 2025 report** ("Next Level for Cancer Screening") scores national screening policies from **26% to 91%** — [European Cancer Organisation](https://www.europeancancer.org/resources/news/press-release-new-report-warns-europe-must-scale-up-cancer-screening-to-save-lives.html); [OncoDaily](https://oncodaily.com/health-policy/european-cancer-summit-screening).
- The OECD/EC **EU Country Cancer Profiles 2025** (July 2025) carry per-country screening coverage. The Romania profile is at [JRC Cancer Inequalities](https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-ro-2024-1682-en.pdf). I could not open it.
- **Romania, cervical screening:**
  - **6.2% of eligible women tested (Eurostat 2025 data, cited by the NGO FABC)**, the lowest in the EU, against an EU average above 60% for these programmes — [TVR Info](https://tvrinfo.ro/romania-fara-niciun-program-national/); [Bursa](https://www.bursa.ro/romania-ramane-codasa-europei-la-preventia-bolilor-09329755). I could not confirm exactly which outlet carries the 6.2% figure.
  - A self-reported survey (IRES, January 2025) gives **30%**, which is not comparable to measured coverage — [IRES report](https://www.presshub.ro/wp-content/uploads/2026/02/ires_sanatatea-romanilor_sondaj-national_raport-de-cercetare_preventie-oncologica.pdf); [TVR Info](https://tvrinfo.ro/romania-fara-niciun-program-national/).
  - **Administrative data from CNAS (via PressOne):** in the previous year, **only 263 cervical-screening services were reimbursed nationally via day-hospitalisation**, and **36 counties had none** — [PressOne](https://pressone.ro/exclusiv-in-zeci-de-judete-din-romania-statul-nu-deconteaza-servicii-esentiale-pentru-sanatatea-femeilor-lista-oraselor-mari-unde-nu-s-a-facut-nicio-investigatie-pentru-depistarea-cancerelor-de-san).
  - A Roche-commissioned study found that **more than 90% of Romanian women had not taken part** in early-detection programmes for breast, cervical or ovarian cancer — [Economica.net](https://www.economica.net/peste-90prc-dintre-femei-nu-au-participat-la-programe-de-depistare-precoce-a-cancerelor-de-san-de-col-uterin-si-ovarian-studiu-roche_134371.html/amp).
  - Romania has the **highest cervical-cancer incidence and mortality in the EU** (ECIS data cited in a 2026 parliamentary question) — [Camera Deputaților interpellation 2026](https://www.cdep.ro/interpel/2026/i4290A.pdf).
  - A January 2025 TVR piece says **no national population screening programme was functioning** at the time, and that tests are reimbursed only via clinics contracted with CNAS — [TVR Info](https://tvrinfo.ro/romania-fara-niciun-program-national/); [Europa Liberă](https://romania.europalibera.org/a/preventia-punctul-vulnerabil-in-lupta-cu-cancerul-in-romania-ce-programe-de-screening-sunt-disponibile/33668528.html).
  - Label: [Established] Romania's organised screening uptake is the lowest in the EU and its administrative throughput is tiny.

#### D. Interoperable records and data portability (EHDS, Data Act)
- **EHDS (Regulation (EU) 2025/327) timeline:**
  - Entered into force on **26 March 2025**. General application and the deadline for key implementing acts is **26 March 2027**.
  - **March 2029:** cross-border exchange of **patient summaries and ePrescriptions/eDispensations** in all Member States, and **most secondary-use rules** apply, with Health Data Access Bodies operational and data permits available.
  - **March 2031:** second wave covering **medical imaging, lab results and discharge reports**, plus secondary use of genomic and other remaining categories.
  - **2035:** final milestone. The EHDS Committee first met on 16 June 2025.
  - Sources: [European Commission EHDS page](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en); [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/pharma-and-life-sciences/european-health-data-space-regulation-primary-use-provisions); [Kennedys 2026](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-health-data-space-is-in-force-implications-for-healthcare-medtech-and-life-sciences); [Baker McKenzie](https://healthcarelifesciences.bakermckenzie.com/?p=967).
  - **Conflict:** Noze dates primary-use provider obligations to **March 2027** and EHR-system requirements to **March 2028** — [Noze](https://www.noze.it/en/insights/ehds-secondary-use-2027/). Check against the Regulation text.
- Regulators are already publishing **data-holder guidance** (HIQA Ireland, June 2026), a sign that preparation is moving to the provider level — [HIQA](https://www.hiqa.ie/sites/default/files/2026-06/EHDS_What-I-need-to-know-as-a-health-data-holder.pdf).
- **[BK]** The EU Data Act has applied since **12 September 2025**. It gives users rights to access and share data generated by connected products, which arguably includes wearables and home devices. EHDS adds a labelling regime for wellness apps that claim EHR interoperability.

#### E. Privacy-preserving AI and federated learning (FL) in practice
- **MELLODDY** (EU IMI, 10 pharma companies) is the canonical success:
  - It used more than **2.6 billion** experimental data points, and every partner improved its own models without sharing data.
  - Returns **saturated** as data volume grew, and gains were largest in pharmacokinetics and safety-panel tasks.
  - **Reconciling data across partners** limited which endpoints could be federated.
  - Sources: [PMC/J Chem Inf Model 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11005050/); [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/6345c0f91f323d61d7567624).
- **The hospital FL reality is governance, not code.** The Nordic–Baltic **FederatedHealth** network (5 countries, 9 institutions, 3 years) reported coordination burden, divergent privacy and risk interpretations, and no legal framework for multi-country distributed learning. Its conclusion was that "technical privacy measures alone cannot replace trust-building" — [University of Turku](https://www.utupub.fi/items/f50c8b83-3d13-4875-a726-389342d0341b/full).
- **NHS pilot (Oxford):** FL clients on Raspberry Pi 4B devices across **4 NHS trusts**, presented in March 2025. No published results were found — [Wolfson College Oxford](https://wolfson.ox.ac.uk/event/scalable-and-low-cost-federated-learning-in-the-nhs-using-micro-computing).
- Label: [Established] FL works technically for pharma consortia. [Strong emerging] hospital FL is limited by governance. **EHDS's 2029 secondary-use regime routes most access through Health Data Access Bodies and secure processing environments rather than ad-hoc FL** ([Noze](https://www.noze.it/en/insights/ehds-secondary-use-2027/)).

#### F. Clinical AI agents and ambient AI scribes (adoption, pricing, willingness to pay)
- **Pricing signals:**
  - **Doctolib** consultation assistant launched in October 2024 at **€79/month** for GPs and paediatricians. A 2026 comparison lists a "Médecin" plan with AI at **€199/month**; it is unclear whether that covers AI only or the whole bundle. It reports **6 million uses** — [Maddyness, 15 Oct 2024](https://www.maddyness.com/2024/10/15/intelligence-artificielle-doctolib-lance-son-assistant-de-consultation/); [Lonasanté 2026](https://www.lonasante.com/?p=11708); [Clubic](https://www.clubic.com/actualite-589885-fini-les-appels-sans-reponse-chez-le-medecin-grace-a-l-assistant-intelligent-de-doctolib.html).
  - **Heidi** (vendor claim): **$110 per user/month billed annually or $150 monthly**, plus a free tier with unlimited notes — [Heidi blog](https://www.heidihealth.com/en-ca/blog/nabla-copilot-alternative).
  - **Nabla:** a free tier of about 30 consults/month and a Pro tier of about **$119/month**. This is a third-party estimate, "estimated_not_official" — [rfp.wiki](https://www.rfp.wiki/specialty-industries/healthcare-life-sciences/healthcare/ambient-clinical-documentation/nabla/ambience-healthcare); [eesel.ai](https://www.eesel.ai/blog/nabla-ai-pricing).
  - **Tandem** and **Microsoft Dragon Copilot (UK/EU)**: no public prices found.
- **Capital and adoption in Europe:**
  - **Tandem** (Stockholm) raised a **$50M Series A** (30 June 2025; Kinnevik describes it as a €40M round) and claims "tens of thousands of clinicians" in the UK, Germany, France and Spain. Through **Accurx**, **more than 200,000 NHS professionals have access**. It raised a **$100M Series B on 15 September 2026** (Scaleup Europe Fund/EQT), bringing total funding to $160M — [Tandem](https://www.tandemhealth.ai/de/news-articles/tandem-secures-50m-to-build-an-ai-native-operating-system-for-clinical-workflows-across-europe); [Kinnevik](https://www.kinnevik.com/insights/tandem-health-funding-round/); [HLTH, 15 Sep 2026](https://hlth.com/insights/news/tandem-health-raises-100m-to-expand-clinical-ai-across-europe).
  - **Heidi** (Australia) raised a $65M Series B in October 2025 at $465M, and about $340M in September 2026 (Blackbird + General Catalyst growth financing; sources split this differently). It claims more than 2M consultations a week in 110 languages — [DealStreetAsia](https://media.dealstreetasia.com/stories/blackbird-backed-heidi-raises-new-round-at-465m-valuation-458546); [Startbase](https://www.startbase.com/news/heidi-erhaelt-340-millionen-dollar-fuer-ki-im-gesundheitswesen/).
  - **Microsoft Dragon Copilot** launched to the NHS on **4 September 2025**. It is MHRA Class I and DTAC/DCB0129-compliant, and was previewed with 7 organisations, 200+ clinicians and more than 10,000 consultations. UK results were "too early" to report; the benefit figures quoted come from the US. An NHS study estimated **£834M/year** of potential value from national AVT rollout — [Digital Health](https://www.digitalhealth.net/2025/09/microsoft-launches-ambient-ai-assistant-to-the-nhs); [Hospital Healthcare Europe](https://hospitalhealthcare.com/in-depth/health-technology/ambient-voice-technology-tool-launched-by-microsoft-to-support-consultations/).
  - ChipSoft (Dutch EHR) is a launch partner — [ChipSoft](https://www.chipsoft.com/en/news/microsoft-launches-ai-platform-dragon-copilot-with-chipsoft-as-launching-partner/).
- **Evidence quality:**
  - **UCLA RCT (NEJM AI, November 2025):** 238 physicians, three arms (Nabla, DAX, usual care), November 2024–January 2025. Nabla cut time per note significantly, by about 9.5% relative to control. **DAX was not statistically significant**. Burnout effects were a secondary outcome and only "potential" — [UCLA Health](https://uclahealth.org/news/release/ucla-study-finds-ai-scribes-may-reduce-documentation-time); [Nabla press](https://nabla.com/press-release/nejm-ai-trial-reports-efficiency-gains-for-physicians-using-nablas-ambient-ai-assistant).
  - **UW Health trial (NEJM AI, two papers):** about **0.36 h/day** less documentation without loss of note quality. Professional fulfilment rose but not significantly — [UW Clinical Trials, 12 Dec 2025](https://uwclinicaltrials.org/2025/12/12/studies-find-ai-technology-for-clinical-documentation-aids-efficiency-and-reduces-burnout/).
  - **Yale-led QI study (JAMA Netw Open, October 2025):** non-randomised. Burnout fell from 51.9% to 38.8% after 30 days (via a secondary blog) — [Consultant360](https://www.consultant360.com/exclusive/ambient-ai-scribes-linked-lower-work-exhaustion-multistate-pragmatic-trial).
  - Label: [Strong emerging] modest, real time savings and a burnout signal. [Established] clinicians and practices pay roughly **€80–200 (≈$110–150) per clinician-month**.

#### G. Aging population, home monitoring and long-term care (LTC)
- **Romania:**
  - People aged 65+ rose from **16.3% (2013) to 19.7% (2023)** and are projected to reach **30.6% by 2050**.
  - Preventive care and LTC are **below the EU average** as shares of health spending (EU State of Health 2025 profile, via search summary) — [Romania Insider, December 2025](https://www.romania-insider.com/eu-state-of-health-ro-dec-2025); [OECD Reviews of Health Systems: Romania 2025](https://www.oecd.org/en/publications/oecd-reviews-of-health-systems-romania-2025_f52e4a98-en/full-report/the-resilience-and-sustainability-of-romania-s-healthcare-system_89b96253.html).
  - INSSE reports **LTC (health) at 5.6% of current health expenditure in 2023** — [INSSE](https://insse.ro/cms/sites/default/files/com_presa/com_pdf/scs2023e.pdf).
  - Catastrophic health spending falls heavily on poorer and older households — [WHO Europe](https://www.who.int/europe/publications/i/item/9789289057905).

#### H. Value-based and outcomes-based incentives
- **Netherlands bundled payment (diabetes care groups):**
  - RIVM's evaluation found task delegation to practice nurses and limited patient involvement. Quality effects were "not easy to interpret" — [RIVM](https://www.rivm.nl/bibliotheek/rapporten/260013002.pdf); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3225242/).
- **Sweden, Stockholm value-based reimbursement (spine surgery):**
  - Average **one-year episode cost fell 11%** in the first two years, while patient numbers rose 22%, so **total cost rose 8%**. Part of the saving may be cost-shifting onto providers — [PMC (Frontiers Public Health, December 2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11668751/).
  - A Karolinska report on hip/knee bundled payments (endorsement text) says complications "dropped substantially" — [KI](https://ki.se/media/95244/download).
- **Romania:** no value-based or outcome-based payment scheme was found (see Gaps). The WHO/Observatory 2026 review mentions **incentives for preventive care in primary care** among ongoing reforms — [WHO/Observatory Romania HiT 2026](https://eurohealthobservatory.who.int/publications/i/romania-health-system-review-2026).

#### I. Employer-sponsored health (Romania focus)
See Q2 for figures. In short, Romania has a large employer-paid **clinic-subscription** market dominated by Regina Maria and MedLife.

#### J. Reimbursement pathways for digital health
See Q2. In short:
- **DiGA:** growing usage, but the payer is pushing back on prices and benefit.
- **PECAN:** a one-year bridge for telemonitoring and therapeutic devices.
- **mHealthBelgium:** only a handful of apps reimbursed, all tied to care pathways.

#### K. Consumer willingness to pay for personal health records (PHR) and tracking
See Q2.

#### L. Operational AI with immediate ROI (no-shows, reminders, capacity)
- **Randomised QI study (safety-net primary care, about 2022–23; URL mapping from the search summary is likely but unconfirmed):** a random-forest model flagged patients at ≥15% no-show risk for scheduler calls. The intervention arm had **33% vs 36%** no-shows (p<0.01), and racial disparities were monitored — [PMC10150669](https://pmc.ncbi.nlm.nih.gov/articles/PMC10150669).
- **MRI (AJR, pre/post, no control):** an XGBoost model on 32,957 appointments plus targeted calls to the top risk quartile cut no-shows from **19.3% to 15.9%** — [Healthcare Finance News](https://www.healthcarefinancenews.com/news/artificial-intelligence-helps-cut-down-mri-no-shows).
- **JAMIA systematic review:** predictive modelling plus SMS, call or navigator reminders is "**probably effective**". It is **unclear whether risk-targeting beats reminding everyone** — [Glasgow eprints](https://eprints.gla.ac.uk/287844/1/287844.pdf). Caveat: the search summary did not explicitly tie this URL to the JAMIA review; the mapping is likely but unconfirmed.
- **Dutch REDUCING trial** (forensic mental health, approved November 2024): reminder calls for patients with predicted risk ≥0.50. No results yet — [ISRCTN28960722](https://www.isrctn.com/pdf/ISRCTN28960722).
- **Romania, private clinic access:**
  - MedOcean analysed more than 100,000 private-clinic calls (January 2025–January 2026). **39.6% of callers seeking a new appointment ended the first call without one**. Booking was 83.8% with empathetic operators vs 21.9% with cold ones. This is vendor data, from a sibling note in this repo — [AGERPRES press release, 30 Jan 2026](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680).
  - Romanian reminder vendors already exist, all making vendor claims:
    - VAstoma: WhatsApp plus AI reminder calls 24h/2h before — [VAstoma](https://vastoma.ro/)
    - DentAIM: WhatsApp reminders — [DentAIM](https://dentaim.ro/)
    - AI Frontdesk: claims "60% fewer no-shows" — [AI Frontdesk](https://aifrontdesk.ro/servicii/agent-vocal)
  - Romanian Law 506/2004 bans automated commercial calls without prior express consent, so reminders need opt-in captured at booking (sibling note) — [infocontact.ro](https://www.infocontact.ro/blocare-apeluri-spam-telemarketing-gdpr/).
  - Label: [Established] that reminders reduce no-shows. [Strong emerging] that ML targeting adds a few percentage points. [Plausible but unproven] that ML adds value beyond universal reminders.

### Inferences
Per area: what must become true (MBT), indicators to watch (IND), picks-and-shovels sellable now (P&S), and fit for a solo founder (FIT).

**A. Continuous sensors**
- **MBT:**
  1. Clinicians or payers must accept consumer-grade data for clinical decisions. That requires validated devices (Class IIa CE, like Hilo) and liability clarity.
  2. Someone must pay for interpreting the data: a reimbursed remote-monitoring code, an employer, or an insurer.
  3. EHR and EHDS pipes must ingest patient-generated data.
- **IND:**
  - Oura membership revenue growing faster than hardware: +121% vs +74% overall, already visible.
  - OTC CGM revenue vs forecasts: Stelo about $130M actual vs $190M forecast, so slower than hyped.
  - Lingo or Stelo launches in more EU countries.
  - Remote-monitoring reimbursement codes that accept consumer devices (Belgian or French telemonitoring pathways).
  - EHDS wellness-app labelling going live.
  - Label: [Plausible].
- **P&S now:**
  - (a) "Patient-generated data intake" for private clinics: import Apple Health/Health Connect exports, Oura or CGM CSVs and lab PDFs into a structured, clinician-readable summary, using Terra/Thryve underneath or direct exports.
  - (b) Consent and audit ledger for such data.
  - (c) Normalisation to FHIR Observation/LOINC.
- **FIT:** feasible for a solo founder **as a B2B add-on to clinics or employers**, not as a consumer app. The wearable-aggregation layer itself is commoditised (Terra from about $399–499/month) [Strong emerging].
- **Data volume:** Dexcom-class CGMs sample about every 5 minutes, about 288 points/day/user, so storage is trivial. The hard part is interpretation and liability, not volume [BK].

**B. Diagnostics**
- **MBT:**
  1. Sample collection that is cheap and reliable at home (finger-prick validity).
  2. Results that are clinically actionable, which needs a GP/clinic loop.
  3. A payer: consumer, employer or insurer.
- **IND:**
  - Romanian private labs (Synevo, MedLife, Regina Maria, Bioclinica) offering home-collection subscriptions, or employer "check-up" bundles.
  - Neko-type clinics entering CEE.
  - Thriva-style employer/insurer partnerships.
- **P&S now:** lab-result normalisation and longitudinal trend views for clinics, labs and occupational-health providers, including "re-test due" recall automation. Parse PDF lab reports with LLMs, then map to LOINC.
- **FIT:** good fit for a solo founder (Python/SQL/LLM). It stays administrative or informational as long as it does not produce individual diagnostic predictions, which would trigger MDR Rule 11 (Class IIa or higher) [BK] [Plausible].

**C. Screening**
- **MBT:**
  1. Romania must actually run organised, population-register-based call/recall programmes.
  2. GPs must be paid per screened or invited person.
  3. Lab, colposcopy and endoscopy capacity must be in place.
  4. EU or PNRR money must be spent.
- **IND:**
  - CNAS reimbursed screening volumes rising from the "263 services" baseline.
  - EU Country Cancer Profiles coverage figures rising.
  - Calls for tender for screening IT (registries, invitation systems).
  - New CNAS preventive packages for family doctors.
  - Romanian EU-funded regional screening projects [BK: ROCCAS/POS 2021–2027 projects exist; amounts not verified].
- **P&S now:**
  - Invitation/recall and eligibility engines for **GP practices** (list-based: who is due for Pap/HPV, mammography or FIT, with outreach by SMS/WhatsApp/letter and outcome tracking).
  - Dashboards for regional programme managers and NGOs.
  - Data-quality tools for screening registries.
- **FIT:**
  - Realistic as a small-scale SaaS or service to GP practices and NGO/regional projects. APEX suits registry-style apps.
  - Public tenders bring procurement friction. Romania's low uptake is both the problem and the risk: demand depends on public money flowing [Plausible].

**D. EHDS and portability**
- **MBT:**
  1. Implementing acts, due by March 2027.
  2. A Romanian national contact point and the PIAS/DES (Dosarul Electronic de Sănătate) infrastructure must be able to exchange **patient summaries (IPS/FHIR) by 2029** [BK on PIAS/DES naming].
  3. Private providers must face enforceable obligations to make data available to patients.
- **IND:**
  - Implementing acts published.
  - Romania designating its digital health authority and Health Data Access Body.
  - National FHIR profiles published.
  - Regulators issuing data-holder guidance (HIQA June 2026 is an early example).
  - Private hospital groups issuing tenders or RFPs for "EHDS readiness".
- **P&S now (2026–2029 window):**
  - EHDS readiness assessments for private clinics.
  - FHIR/IPS export modules from legacy clinic software (many Romanian clinics run custom or local systems; Oracle-based systems are common in hospitals [BK]).
  - Patient-access portals with download-in-standard-format.
  - Consent and opt-out registries.
  - Data catalogues/metadata (DCAT-AP Health) for future secondary-use requests.
- **FIT:** good for a solo technical founder with SQL/PL-SQL/APEX skills **as consulting plus productised connectors**. The regulatory clock creates urgency, but buyers will defer spending until national rules are clear, probably 2027–2028 [Plausible].

**E. Federated learning and secure processing environments**
- **MBT:** EHDS Health Data Access Bodies and secure processing environments (SPEs) must be operational (from 2029), and institutions must standardise data (OMOP/FHIR).
- **IND:** data permits issued, OMOP conversions in Romanian hospitals, EU-funded projects.
- **P&S now:** OMOP/FHIR ETL services, de-identification and pseudonymisation pipelines, synthetic-data generation for testing.
- **FIT:** heavy. It needs institutional partners, data access and multi-year governance work. **Not realistic as a solo product; possible only as ETL consulting** [Strong emerging, based on the FederatedHealth governance findings].

**F. Ambient AI and patient-communication agents**
- **MBT:** already mostly true. Clinicians pay about €80–200/month, and RCT evidence of modest efficiency exists.
- **IND (Romania):**
  - Romanian-language accuracy.
  - Integration with Romanian EHRs and CNAS documents (scrisoare medicală, bilet de trimitere, concediu medical).
  - Large Romanian networks (Regina Maria, MedLife, Sanador) announcing scribe deployments.
- **P&S now:**
  - Romanian-specific templates and post-processing for CNAS forms.
  - Integration connectors to local practice software.
  - Patient-communication agents for booking, pre-visit questionnaires and post-visit instructions, which are not diagnostic.
- **FIT:**
  - The **core scribe market is crowded and heavily capitalised** (Tandem $160M total, Heidi about $340M in 2026, Microsoft, Doctolib). A solo founder should not build a general scribe [Strong emerging].
  - Niche Romanian workflow add-ons and patient-communication agents are feasible [Plausible].

**G. Aging and home care**
- **MBT:**
  1. A funded LTC/home-care benefit in Romania, public or private (LTC insurance).
  2. A home-care provider workforce that uses digital tools.
- **IND:**
  - LTC reforms in Romania's PNRR or the European Care Strategy implementation [BK].
  - CNAS home-care reimbursement changes.
  - Private home-care chains growing.
- **P&S now:** scheduling, visit verification and care-plan tools for home-care agencies; family-caregiver portals.
- **FIT:** feasible but the market is small and fragmented. Romania's LTC spending is below the EU average [Plausible].

**H. Value-based care**
- **MBT:** payers that contract on outcomes. That does not exist in Romania as far as I found.
- **IND:** CNAS pilots tying payment to prevention indicators in primary care (the WHO/Observatory 2026 review mentions preventive-care incentives).
- **P&S now:** PROMs/outcome-collection tools that private clinics can use for **marketing quality**, and that would be ready if payers move.
- **FIT:** speculative in Romania. The Dutch and Swedish experience shows mixed or slow results even where schemes exist [Speculative for Romania].

**I. Employer health**
- **MBT:** employers must see prevention as a cost lever (absenteeism, retention) and want aggregate analytics. A tax-advantaged channel already exists (EUR 400/year).
- **IND:** clinic networks bundling "prevention analytics" into corporate subscriptions; HR-tech platforms (benefits marketplaces) adding health.
- **P&S now:**
  - Occupational-health (medicina muncii) workflow digitalisation: scheduling, aptitude certificates and exam recalls.
  - Anonymised utilisation/prevention dashboards for HR buyers, delivered via clinics.
- **FIT:** good fit for B2B automation with n8n and APEX [Plausible].

**J. Reimbursement pathways**
- **MBT for a Romanian startup:** CE marking under MDR as a medical device (DiGA requires Class I/IIa, and from 2026 some IIb), GDPR/BSI-type security, German-language product, evidence (an RCT within 1–2 years for a permanent listing) [BK].
- **FIT:** **not realistic** on €25k and 10–12 h/week.

**K. PHR**
- A standalone consumer PHR is the historically failing model (see Q2). Distribute B2B2C through clinics, labs or employers [Strong emerging].

**L. Ops AI**
- **MBT:** already true. Clinics lose appointments and capacity, and reminders work.
- **IND:** local competitors' traction; WhatsApp Business API costs.
- **P&S now:**
  - Reminder, recall and waitlist backfill.
  - Prediction-ranked outreach, with A/B tests built in so the clinic sees ROI.
  - Call analytics.
- **FIT:** **the most immediately realistic** for a solo founder. Differentiate on measured ROI (built-in control groups) and integration with Romanian clinic software, because competitors already sell basic WhatsApp reminders [Strong emerging].

### Gaps
- **Sensors:**
  - Lingo and other OTC CGM **actual** sales, and OTC CGM availability or sales in **Europe and Romania**: not found.
  - Wearable penetration in Romania: not found.
  - Smart patches and at-home sensor market data: not researched (search budget exhausted).
- **Diagnostics:**
  - Lab-pricing trends in Romania or the EU: not found.
  - Romanian consumer lab-test volumes, and whether finger-prick panels are sold in Romania: not found.
- **Screening:**
  - Breast and colorectal screening uptake in Romania, and EU-level coverage per cancer, from the 2025 Country Cancer Profiles: not retrieved.
  - Whether the 90% offer target was met: not assessed in the sources found.
  - Budgets of Romanian EU-funded screening projects (ROCCAS etc.): not retrieved.
- **EHDS:** primary-use obligations date conflict (2027 vs 2029). Verify against the Regulation (EU) 2025/327 text.
- **Data Act:** application details for wearables [BK only].
- **Federated learning:** no 2025–2026 European hospital-network deployment with quantitative outcomes found. The Oxford NHS pilot results are unpublished.
- **Ambient AI:**
  - Tandem pricing and Dragon Copilot EU pricing: not public.
  - No Romanian scribe-adoption data.
  - The 6M Doctolib "uses" is undated.
- **Long-term care:**
  - LTC public spending as % of GDP for Romania vs the EU (2024 Ageing Report) and Romania's home-care financing (CNAS home-care days, social-assistance law): **not researched (search budget exhausted)**.
  - [BK] Romania's public LTC spending is among the lowest in the EU (well under 1% of GDP vs an EU average of about 1.7%). Needs verification.
- **Value-based care:**
  - Sweden's OrthoChoice-specific results: not retrieved.
  - **No evidence found of any value-based payment in Romania**. Absence in search results is not proof.
- **Occupational health:** digitalisation in Romania (medicina muncii providers, market size, e-documents) not researched.
- **Ops AI:** a Cochrane-type estimate of SMS-reminder effect size was not retrieved. [BK: the Cochrane 2013 review found SMS reminders improved attendance vs no reminder, with an effect similar to phone calls.]

---

## Q2. Who pays for prevention in Europe and Romania today (patients, employers, insurers, public payers), how much, and through which reimbursement pathways?

### Takeaway
- **Europe:** public payers fund organised screening and, in a few countries, reimbursed digital therapeutics or telemonitoring. DiGA is the largest, at about €400M of cumulative statutory spend in 5 years and 1.6M uses, but its prices and benefit are increasingly contested. Consumers pay for premium prevention: Oura subscriptions, Neko scans at £299, at-home tests.
- **Romania:** public prevention spending is minimal. Organised screening barely functions, and health spending is 5.8% of GDP with prevention below the EU average.
- **The real prevention payers in Romania are employers**, through clinic subscriptions (claimed 2.2M beneficiaries, more than €250M, a weak source) with a EUR 400/year tax channel. Out-of-pocket patients and a small but double-digit-growing private health insurance market (about 0.7bn lei in H1 2025) make up the rest.
- **Standalone consumer willingness to pay for health-record or tracking software is historically weak**, except when bundled with hardware (Oura) or delivered through "captive members" (insurers, employers, clinics).

### Cited Findings

#### Public payers: Europe's reimbursement pathways
- **Germany: DiGA (statutory health insurance, GKV).**
  - **DiGA-Bericht 2025** (GKV-Spitzenverband, released **8 April 2026**, covering September 2020–December 2025):
    - **1.6 million DiGA used** cumulatively, with **about €400M total GKV spending** since 2020.
    - Usage rose **63% year on year**.
    - One outlet reports **about 695,000 activation codes redeemed in 2025**.
    - Of **74 DiGA ever listed, fewer than one in five showed proven benefit at listing**, and **16 were removed** for lack of proven benefit.
    - The GKV says most DiGA still enter the benefits catalogue without proof of benefit, and insurers must pay manufacturer prices in year one.
    - Sources: [GKV-Spitzenverband press release, 8 Apr 2026](https://www.gkv-spitzenverband.de/gkv_spitzenverband/presse/pressemitteilungen_und_statements/pressemitteilung_2239872.jsp); [Krankenkasseninfo](https://www.krankenkasseninfo.de/ratgeber/nachrichten/diga-auf-rezept-nehmen-zu-schon-16-millionen-verordnungen-62539.html); [Ärzte Zeitung](https://www.aerztezeitung.de/Wirtschaft/Kassenverband-beklagt-systematisch-ueberhoehte-DiGA-Preise-im-ersten-Jahr--462610.html); [Barmer](https://www.barmer.de/politik/meldungen/2026-meldungen/diga-bericht-2025-1498776).
  - **Prior report (April 2025, data for 2024):** average **manufacturer price €541** vs average **negotiated/reimbursed price €226** — [GKV-Spitzenverband, 2 Apr 2025](https://www.gkv-spitzenverband.de/gkv_spitzenverband/presse/pressemitteilungen_und_statements/pressemitteilung_2011904.jsp); [Barmer DiGA-Bericht 2024](https://www.barmer.de/politik/meldungen/2025-meldungen/diga-bericht-2024-1328232).
  - **Policy direction:** Barmer calls for an AMNOG-style benefit assessment for DiGA. Eleven industry associations, by contrast, demand an end to "over-regulation" — [Barmer](https://www.barmer.de/politik/meldungen/2026-meldungen/diga-bericht-2025-1498776); [Verbandsbüro](https://www.verbandsbuero.de/diga-2025-elf-verbaende-fordern-ende-der-ueberregulierung/).
  - Label: [Established] DiGA is a real but **therapy-focused (not primarily preventive)** reimbursement route with a contested price trajectory.
- **France: PECAN** (prise en charge anticipée numérique).
  - A **one-year, non-renewable transitional reimbursement** for CE-marked digital medical devices (therapeutic or telemonitoring) presumed innovative. The manufacturer must file for standard listing within 9 months (telemonitoring) or 6 months (others) — [ANS webinar](https://esante.gouv.fr/webinaires/prise-en-charge-anticipee-des-dispositifs-medicaux-numeriques-pecan-point-dactualite-sur-ce-mode-de-remboursement); [AP-HP legal (arrêté 10 Sep 2024)](https://affairesjuridiques.aphp.fr/textes/arrete-du-10-septembre-2024-relatif-a-la-prise-en-charge-anticipee-numerique-de-certains-dispositifs-medicaux-numeriques-a-visee-therapeutique-et-certaines-activites-de-telesurveillance-medicale-en-ap/?pdf=635961).
  - **Examples:** Continuum+ Connect (from 23 September 2024), Axomoove (December 2024), and Cureety (PECAN in 2023, then on the telemonitoring list LATM from 31 March 2025).
  - HAS/CNEDiMTS PECAN evaluation principles were validated on 1 July 2025 and updated in September 2025 — [HAS](https://has-sante.fr/upload/docs/application/pdf/2025-09/principes_devaluation_de_la_cnedimts_prise_en_charge_anticipee_pecan.pdf).
  - **No total count** of PECAN or LATM listings was found.
- **Belgium: mHealthBelgium.**
  - **7 apps reached Level 3+ (regular reimbursement) in February 2025**, all only within the **chronic heart-failure remote-monitoring care pathway**: BeWell Well@Home, Comarch HomeHealth 2.0, Comunicare, FibriCheck, Healthentia, moveUP and RemeCare.
  - By **April 2025** there were **8** (Chambers).
  - In **April 2026, 5 apps were added** for the oncology remote-monitoring pathway: moveUP, Noona, Malea, RemeCare and Resilience PRO.
  - Sources: [MTRC](https://mtrconsult.com/news/belgium); [Chambers Digital Healthcare 2025](https://gpg-pdf.chambers.com/digital-healthcare-2025/20/).
  - Label: [Established] reimbursement exists only inside predefined care pathways, and volumes are small.
- **EU screening money:** **€300M of EU4Health** for rolling out breast, cervical and colorectal screening schemes — [WBCPC](https://worldbladdercancer.org/news_events/europes-beating-cancer-plan-mid-term-review-key-takeaways/).

#### Public payer: Romania
- **Health spending:**
  - **5.8% of GDP (2023) vs 10% in the EU**.
  - **€1,800 per capita (PPP) vs €3,832 in the EU**.
  - **77% public vs 23% private, almost all private spending out of pocket**, driven by outpatient drugs and dental care.
  - **Prevention and LTC shares are below the EU average**.
  - Sources: [Romania Insider (State of Health in the EU, December 2025)](https://www.romania-insider.com/eu-state-of-health-ro-dec-2025); [OECD Reviews of Health Systems: Romania 2025](https://www.oecd.org/en/publications/oecd-reviews-of-health-systems-romania-2025_f52e4a98-en/full-report/overview-of-romania-s-health-system_32c90b33.html).
- **Screening throughput:** CNAS reimbursed only **263 cervical screenings via day-hospitalisation** in the year reported, and **36 counties had none** — [PressOne](https://pressone.ro/exclusiv-in-zeci-de-judete-din-romania-statul-nu-deconteaza-servicii-esentiale-pentru-sanatatea-femeilor-lista-oraselor-mari-unde-nu-s-a-facut-nicio-investigatie-pentru-depistarea-cancerelor-de-san).
- **Reforms:** reforms aim to shift care toward ambulatory and preventive services, including **incentives for preventive care in primary care** — [WHO/Observatory Romania Health System Review 2026](https://eurohealthobservatory.who.int/publications/i/romania-health-system-review-2026).
- **No DiGA-like digital reimbursement pathway in Romania** was found in any source (see Gaps).

#### Employers (Romania)
- **Market size (weak source):** "**more than 2.2 million Romanians** benefit from employer subscriptions; market **above €250M**", attributed to "PwC estimates and industry data" in a **sponsored advertorial by a competing clinic** (October 2025). I did not find the original PwC report — [Bursa (advertorial)](https://www.bursa.ro/advertorial-enayati-medical-city-lanseaza-abonamentele-aniversare-corporate-27561751); [Revista Biz](https://www.revistabiz.ro/enayati-medical-city-lanseaza-abonamentele-aniversare-corporate/).
- **Operators:**
  - **Regina Maria** claims a portfolio of **more than 750,000 subscriptions** (undated) — [BestJobs company profile](https://bestjobs.eu/it/company-profile/regina-maria).
  - **MedLife** serves "almost one million" employees (Forbes România interview) — [Forbes România](https://www.forbes.ro/?p=267117).
  - **EY (2019 data):** value-chain impact of €776M and value added of €263M (0.1% of GDP). This is not direct market size — [Economedia](https://economedia.ro/fiecare-loc-de-munca-generat-de-abonamentele-medicale-contribuie-la-crearea-altor-2-locuri-de-munca-in-economia-romaniei-analiza-ey.html).
  - **2016:** more than 1M subscriptions and about €50M turnover (outdated) — [Revista Biz](https://www.revistabiz.ro/un-milion-de-romani-beneficiaza-de-abonamente-de-sanatate/).
- **Tax treatment:**
  - A **EUR 400/year per person** ceiling applies to medical subscriptions and voluntary health insurance — [Romania Insider: "Medical subscriptions, tax exempt up to EUR 400 per year"](https://www.romania-insider.com/medical-subscriptions-tax-exempt-eur-400-per-year-romania).
  - When **paid by employees**, they are **deductible from taxable salary income up to EUR 400/year**, including for dependants — [Romania Insider](https://www.romania-insider.com/medical-subscriptions-tax-exempt-eur-400-per-year-romania); [Contabilul.manager.ro](https://contabilul.manager.ro/a/30196/abonamentul-de-servicii-medicale-pentru-salariat-si-membrii-de-familie-care-este-tratamentul-fiscals.html).
  - Since **February 2023**, employer-paid **sports subscriptions** (CAEN 9311–9313, including bundles with medical services) are exempt from income tax and social contributions up to EUR 400/year. They count within the overall **33% of base salary** cap on benefits — [PwC Romania (Law 34/2023)](https://www.pwc.ro/en/tax-legal/alerts/new-salary-benefits-with-favourable-tax-treatment-can-be-granted.html).
  - A former Health Minister (Rafila) said "quite few people benefit" from the EUR 400 deduction (date unclear) — [Newsweek România](https://newsweek.ro/sanatate/cati-bani-vor-putea-deconta-romanii-in-sistemul-privat-putini-au-asigurari-medicale-private).

#### Private health insurers (Romania)
- **Q1 2025 health gross written premiums:** **361M lei** (ZF) or **380M lei including branches** (Financial Intelligence), **+12–13% year on year**. There were **255,325 contracts in force** (+10%), and **claims paid rose about 30%** — [Ziarul Financiar](https://www.zf.ro/banci-si-asigurari/piata-de-asigurari-in-t1-2025-asigurarile-de-sanatate-au-ajuns-la-22845837); [Financial Intelligence](https://financialintelligence.ro/piata-asigurarilor-din-romania-a-crescut-cu-7-in-primul-trimestru-la-6-miliarde-lei/).
- **H1 2025:** health insurance **above 680M lei**, within a total insurance market of 12.3bn lei — [Revista Biz (ASF report)](https://www.revistabiz.ro/raport-asf-despre-piata-asigurarilor-din-romania-crestere-solida-maturizare-si-incredere/).
- **Full-year 2025 total insurance market:** about **25.8bn lei (+10%)**. The health line is not broken out in the snippets — [Capital](https://www.capital.ro/piata-asigurarilor-din-romania-a-crescut-in-2025-primele-brute-au-depasit-25-miliarde-de-lei.html); [Digi24](https://www.digi24.ro/digieconomic/financiar/document-piata-asigurarilor-creste-cu-10-in-2025-rca-ramane-dominant-iar-despagubirile-urca-accelerat-96293).

#### Consumers (Europe)
- **Hardware plus subscription:** Oura has **5M paying members**, and **membership revenue was $240.5M in the nine months to June 2026 (+121%)** — [Forbes Australia](https://www.forbes.com.au/?p=207282); [BeInCrypto](https://beincrypto.com/oura-ipo-nasdaq-16-billion-valuation/).
- **Premium prevention service:** Neko Health charges **£299 per scan** in the UK and has done more than 100k scans — [Axios](https://www.axios.com/2025/01/23/spotify-founder-neko-health); [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/whole-body-imaging-firm-neko-health-raises-700m).
- **Standalone PHR failures:**
  - Google said Google Health was closing because it **had not achieved widespread adoption**. It attracted mainly tech-savvy and fitness users.
  - A **2011 survey found only 7% had ever used a PHR**.
  - The founder's critique was that it was just "a place to store data".
  - It lacked lab connections, provider messaging and scheduling.
  - Sources: [InformationWeek](https://www.informationweek.com/it-sectors/5-reasons-why-google-health-failed); [Computerworld](https://www.computerworld.com/article/1534713/why-google-health-failed-too-little-too-soon.html); [MobiHealthNews](https://mobihealthnews.com/node/102016); [Univ. of Twente study (51 user interviews)](https://research.utwente.nl/en/publications/personal-health-records-success-why-google-health-failed-and-what/).
  - Microsoft HealthVault "was not dramatically successful" and struggled to reach critical mass — [Computerworld](https://www.computerworld.com/article/1534713/why-google-health-failed-too-little-too-soon.html). [BK] HealthVault was shut down in November 2019.
- **Stated willingness to pay is old and inflated:**
  - Accenture (2005, about 520 people): just over half would pay at least $5/month. Accenture (2007): 51% would pay "if reasonable" — [Healthcare IT News](https://healthcareitnews.com/news/consumers-willing-pay-health-it); [CIO Insight](https://www.cioinsight.com/news-trends/patients-willing-to-pay-for-electronic-medical-records-surveys-show/).
  - Korea (2008): 59.8% willing to use, **27.8% willing to pay** — [Healthcare Informatics Research](https://www.e-hir.org/journal/view.php?number=523).
  - Accenture's key point: successful patient-record services had "**captive members**" who did not pay directly, with the service bundled with a health plan — [Nextgov](https://www.nextgov.com/digital-government/2005/07/consumers-willing-to-pay-for-health-it/209872/).

#### Clinicians and practices as payers (adjacent but relevant)
- Ambient scribes cost about **€79–199/month** (Doctolib) and about **$110–150/month** (Heidi; Nabla Pro estimated at about $119). Clinicians and practices pay these, not health insurers — see Q1-F sources.

### Inferences
- **Romania's prevention money sits mainly with employers and households, not the state.** Strong emerging evidence:
  - The employer subscription channel (2.2M beneficiaries, if the advertorial figure holds; [BK] Romania has roughly 5–6M salaried employees, so this would be about 35–45% of them, which looks high and may include family members or double counting across networks) is the largest organised buyer of preventive check-ups.
  - Private health insurance is small (about 0.7bn lei, roughly €140M, per half-year; annualised **about €280M** is my extrapolation) but growing at double digits.
  - Annual prevention spend per covered employee is capped in practice by the EUR 400/year tax-advantaged ceiling, so software must be priced as a **small fraction of an existing subscription** (for example €0.5–2 per member-month via the clinic), not as a new budget line [Plausible].
- **Public-payer routes for a Romanian startup are effectively foreign.** DiGA, PECAN and mHealthBelgium all require CE-marked medical devices, local language, local evidence, and, in Belgium, membership of a care pathway. DiGA's payer is cutting prices (€541 manufacturer vs €226 negotiated) and pushing for AMNOG-style assessment, so the "DiGA gold rush" economics are fading [Strong emerging].
- **Romania has no digital-health reimbursement pathway.** The near-term route to the Romanian public payer is through **CNAS-contracted providers** (GPs, labs, ambulatory clinics) buying administrative tools out of their own fees, or through **EU-funded programme budgets** for screening [Plausible].
- **Consumer willingness to pay works only when software is bundled** with a device (Oura), an experience (Neko) or a captive membership (employer, insurer or clinic subscription). This is consistent with the Google Health and HealthVault history and Accenture's "captive members" observation [Strong emerging].
- **For Romania specifically, B2B2C via private clinic networks and employers is the realistic path.** Romania's low incomes (spending per capita less than half the EU average) make direct-to-consumer subscriptions harder than in the UK or Nordics [Plausible].

### Gaps
- **Public prevention spending:**
  - EU-level share of health spending on preventive care (Eurostat/OECD) and Romania's exact percentage: not retrieved.
  - [BK] The EU average is usually reported at about 3–6% of current health expenditure; Romania's is lower. Verify in Health at a Glance: Europe.
  - Germany's statutory prevention spending under §20 SGB V (Präventionsgesetz) and workplace health promotion budgets: not researched.
- **DiGA:**
  - 2025 average negotiated price, number currently listed (permanent vs provisional) and share of prescriptions by indication: not retrieved, because the primary report was blocked.
  - From the snippets, about 58 remain if 74 were listed and 16 removed. That subtraction is my inference.
- **PECAN:** total listings and amounts paid per patient per month were not found.
- **Employer channel:**
  - Original PwC source for the €250M / 2.2M Romanian corporate-subscription figure: not found.
  - Regina Maria and MedLife corporate-segment revenue for 2025: not retrieved. [BK] MedLife's annual reports split revenue by business line, including corporate; check there.
  - Employer-paid medical subscriptions:
    - Exact current Fiscal Code treatment (art. 76 and art. 25) and any 2024–2026 changes, such as health-contribution (CASS) treatment of benefits, were not confirmed.
    - [BK] My understanding is that employer-paid medical subscriptions and voluntary health insurance premiums are non-taxable for the employee up to EUR 400/year and deductible for the employer up to the same limit. Verify with a Romanian tax adviser.
  - European corporate-wellness market size and **evidence of employer demand for prevention analytics** (Europe or Romania): not found. Search budget exhausted.
- **Insurers:** full-year 2025 Romanian health-insurance premiums (ASF annual report): not retrieved.
- **Consumers:**
  - Romanian survey evidence on willingness to pay for health apps or PHRs: not found.
  - Recent (2023–2026) European survey evidence on PHR willingness to pay: not found. The cited WTP evidence is 2005–2011.

---

## Q3. Which opportunities are realistic for a solo founder (Bihor SRL, about €25k capital, 10–12 h/week, Python/SQL/PL-SQL/Oracle APEX/LLM APIs/n8n, no clinical data access) and which need heavy capital or clinical validation?

### Takeaway
Realistic now: non-device, administrative "plumbing" for buyers who already have budgets. That means:
- Reminder, recall and no-show automation with measured ROI.
- Screening call/recall for GP practices.
- Lab-result and patient-generated-data intake and normalisation for clinics.
- Occupational-health and employer-prevention workflow tools.
- EHDS/FHIR readiness connectors from 2027.

Heavy capital or clinical validation is needed for anything that makes individual clinical predictions (MDR Class IIa or higher, EU AI Act high-risk), general ambient scribes, DiGA/PECAN reimbursement, federated learning, and consumer apps that need marketing spend.

### Cited Findings
- **Competition and capital intensity in ambient AI:**
  - Tandem has raised a total of $160M ($100M Series B, September 2026) — [HLTH](https://hlth.com/insights/news/tandem-health-raises-100m-to-expand-clinical-ai-across-europe).
  - Heidi has raised about $340M (2026) — [Startbase](https://www.startbase.com/news/heidi-erhaelt-340-millionen-dollar-fuer-ki-im-gesundheitswesen/).
  - Microsoft Dragon Copilot holds MHRA Class I status — [Digital Health](https://www.digitalhealth.net/2025/09/microsoft-launches-ambient-ai-assistant-to-the-nhs).
  - Doctolib bundles its assistant at €79–199/month — [Maddyness](https://www.maddyness.com/2024/10/15/intelligence-artificielle-doctolib-lance-son-assistant-de-consultation/).
- **Reimbursement routes need evidence:**
  - DiGA: fewer than one in five showed benefit at listing, 16 were delisted, and the payer pushes for AMNOG-style assessment — [GKV-Spitzenverband](https://www.gkv-spitzenverband.de/gkv_spitzenverband/presse/pressemitteilungen_und_statements/pressemitteilung_2239872.jsp); [Barmer](https://www.barmer.de/politik/meldungen/2026-meldungen/diga-bericht-2025-1498776).
  - PECAN requires CE marking and filing for full listing within 6–9 months — [ANS](https://esante.gouv.fr/webinaires/prise-en-charge-anticipee-des-dispositifs-medicaux-numeriques-pecan-point-dactualite-sur-ce-mode-de-remboursement).
  - mHealthBelgium reimbursement exists only inside care pathways — [MTRC](https://mtrconsult.com/news/belgium).
- **Federated learning is limited by governance** (5 countries, 9 institutions, 3 years) — [University of Turku](https://www.utupub.fi/items/f50c8b83-3d13-4875-a726-389342d0341b/full).
- **Aggregation middleware is already productised:** Terra from $399–499/month; Thryve SDK across 500+ devices — [Terra](https://tryterra.co/pricing); [Thryve](https://thryve.health/health-connect-api).
- **Ops-AI evidence is modest:**
  - 33% vs 36% no-shows (randomised QI) — [PMC10150669](https://pmc.ncbi.nlm.nih.gov/articles/PMC10150669).
  - 19.3% to 15.9% (pre/post) — [Healthcare Finance News](https://www.healthcarefinancenews.com/news/artificial-intelligence-helps-cut-down-mri-no-shows).
  - The JAMIA review says targeting has not been shown to beat universal reminders — [Glasgow eprints](https://eprints.gla.ac.uk/287844/1/287844.pdf).
- **Romanian ops-AI competitors** already sell WhatsApp/voice reminders (VAstoma, DentAIM, AI Frontdesk). Romanian AI-voice vendors price at about €299–499/month — [VAstoma](https://vastoma.ro/); [DentAIM](https://dentaim.ro/); [AI Frontdesk](https://aifrontdesk.ro/servicii/agent-vocal); [Agentul Vocal](https://agentulvocal.ro/); [Vocalyy](https://www.vocalyy.ro/).
- **Romanian demand signal:** 39.6% of new-appointment callers to private clinics end the first call without booking (vendor dataset) — [AGERPRES/MedOcean](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680).
- **Romanian screening gap:** 6.2% cervical coverage (Eurostat, via FABC); 263 CNAS-reimbursed cervical screening services; 36 counties with none — [TVR Info](https://tvrinfo.ro/romania-fara-niciun-program-national/); [PressOne](https://pressone.ro/exclusiv-in-zeci-de-judete-din-romania-statul-nu-deconteaza-servicii-esentiale-pentru-sanatatea-femeilor-lista-oraselor-mari-unde-nu-s-a-facut-nicio-investigatie-pentru-depistarea-cancerelor-de-san).
- **EHDS timeline creates dated obligations** (2027 general application; 2029 patient summaries and secondary use; 2031 lab and imaging) — [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/pharma-and-life-sciences/european-health-data-space-regulation-primary-use-provisions); [Kennedys](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-health-data-space-is-in-force-implications-for-healthcare-medtech-and-life-sciences).

### Inferences
Feasibility matrix. These are my inferences; the labels reflect the evidence behind each.

**Tier 1: realistic now for a solo founder (low capital, no clinical data, not a medical device)**
1. **Appointment reminder, recall and no-show reduction for private clinics, dental and labs, with built-in control groups to prove ROI.**
   - Buyers already pay.
   - Evidence that reminders work is [Established]; the ML-targeting increment is [Plausible].
   - Differentiators against local competitors: measured ROI reporting, integration with the clinic's existing scheduling software, and an Oracle/APEX back office.
   - Risk: crowded at the low end, and Law 506/2004 consent requirements.
2. **Preventive recall for GP practices and clinics.**
   - Covers "due for Pap/HPV, mammography, FIT, annual check-up or occupational exam" lists, outreach, and tracking of completion.
   - Ties to Romania's huge screening gap. Payer: the practice, NGO or EU-funded project budgets, or a clinic network's corporate-subscription value proposition [Plausible].
3. **Lab-report and patient-generated-data intake and normalisation for clinics and occupational-health providers.**
   - LLM PDF parsing, mapping to LOINC/FHIR, trend views, re-test reminders.
   - Must stay informational or administrative to avoid MDR Rule 11 [BK] [Plausible].
4. **Occupational-health (medicina muncii) workflow and employer prevention dashboards** with aggregated, anonymised data, sold through clinic networks or occupational-health firms [Plausible; market size not verified].

**Tier 2: realistic with timing or partners (2027–2029)**
5. **EHDS/FHIR readiness:** IPS patient-summary export, patient-access portals, consent and opt-out registries, data catalogues for private providers. PL-SQL and APEX skills on Oracle-based hospital systems are a niche advantage [Plausible; depends on Romanian implementing rules].
6. **Romanian-language workflow add-ons around ambient scribes:** CNAS form generation, templates and connectors, rather than a competing scribe [Plausible].

**Tier 3: needs heavy capital, clinical validation or institutions**
7. Individual risk-prediction or diagnostic software (CE Class IIa or higher, clinical evaluation, AI Act high-risk obligations) [BK on MDR/AI Act; Established as a regulatory burden].
8. DiGA, PECAN or mHealthBelgium reimbursed products [Strong emerging].
9. A general ambient scribe [Strong emerging].
10. Federated learning and secure-processing-environment platforms [Strong emerging].
11. Consumer wearables or PHR apps needing marketing spend [Strong emerging, based on the Google Health and HealthVault history].
12. Neko-style prevention clinics or hardware [Established as capital-intensive: at least $960M raised in the January 2025 and July 2026 rounds alone].

**Time budget:** at 10–12 hours a week, Tier 1 items fit only if delivered as **configurable services on a shared core** (n8n plus APEX plus LLM). Selling to a few dozen clinics at €50–300/month each is plausible; that price band is inferred from Romanian voice and reminder vendor prices. Enterprise sales to the big networks (Regina Maria, MedLife) take long cycles and may not fit the time budget [Speculative].

**Early indicators the founder should track:**
- **Funding:** EU or POS screening project tenders in the North-West region (Bihor).
- **Public payer:** CNAS rule changes paying GPs for prevention; Romanian EHDS implementing decisions and national FHIR profiles.
- **Private networks:** private networks' announcements of AI scribes or patient apps (partnership or integration targets).
- **Products:** OTC CGM or Hilo-type devices sold in Romanian pharmacies; growth in Romanian health insurance premiums (ASF quarterly).

### Gaps
- No Romanian data was found on clinic software penetration (which practice-management or EHR systems private clinics and GPs use), which matters for integration strategy.
- No evidence was found on what Romanian clinics actually pay for reminder or recall tools, beyond vendor list prices for voice agents.
- No Romanian data on employer appetite for prevention analytics, or on occupational-health digitalisation, was found.
- MDR Rule 11 and EU AI Act high-risk timing (August 2026/2027 for AI in medical devices) were not verified in this session [BK].
- No Romanian public-procurement data (SEAP/SICAP) on screening IT tenders was retrieved.
