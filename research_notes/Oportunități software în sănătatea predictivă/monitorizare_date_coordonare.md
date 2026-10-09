# Monitoring, data and care coordination in predictive healthcare: evidence, maturity, timelines (notes as of October 2026)

**How these notes were made, and how far to trust them (read first).**
- The session's shared WebSearch budget ran out after 24 searches.
- Every WebFetch was blocked by the egress proxy: health.ec.europa.eu, economy-finance.ec.europa.eu, pubmed, clinicaltrials.gov, jacc.org, ncbi/PMC, cov.com, and a curl test of about 40 other medical and EU domains. So **no primary document was opened in this session.**
- Each fact is tagged by where it came from:
  - **(snippet)**: taken from a WebSearch result summary in this session. The original was not opened, so it is a secondary summary.
  - **(BK)**: background knowledge (knowledge cutoff mid-2026) of a well-known, peer-reviewed or official publication. I give the canonical DOI or official URL, or a PubMed search link when I'm unsure of the DOI. These were **not re-opened this session**, so the report writer should spot-check exact numbers before quoting them.
  - **(PN)**: taken from this project's earlier research notes (`research_notes/Recepționist AI telefonic București/`). Those notes cite their own sources, and the URLs are repeated here.
- **Evidence grades:**
  - **[EST]** Established evidence: several RCTs or meta-analyses, or guideline-level.
  - **[SEE]** Strong emerging evidence: one or two good RCTs, or consistent prospective data.
  - **[PBU]** Plausible but unproven: mechanism or accuracy data only, no outcome trial.
  - **[SPEC]** Speculative.
- Throughout, I keep three distinctions: **detection accuracy vs improved outcomes**, **forecast vs observed**, and **technical vs commercial feasibility**.

---

## 1. Continuous and passive monitoring and consumer wearables vs clinical-grade sensors: what is proven (detection vs outcomes)?

### Takeaway
Consumer wearables are proven at *detecting* atrial fibrillation (AF). Notifications are confirmed as AF on an ECG patch 84–98% of the time, and wearable screening multiplies AF diagnoses 2–4×. But **no trial has shown that wearable or consumer screening reduces stroke or death.** Anticoagulating short, device-detected AF reduces ischaemic stroke by about a third but increases major bleeding. Blood-pressure and glucose wearables are a step earlier: Apple's FDA-cleared hypertension notification has 41% sensitivity, cuffless BP has no accepted clinical validation, and OTC CGM in people without diabetes has no outcome evidence.

### Cited Findings
**AF detection: large virtual studies (detection accuracy, not outcomes)**
- **Apple Heart Study** (NEJM, Nov 2019): 419,297 self-enrolled participants. 0.52% received an irregular-pulse notification. Among notified participants who returned an ECG patch, AF was found in 34%. The PPV of a notification for concurrent AF on the patch was 0.84. Only about a quarter of notified participants returned patches. **[EST for detection accuracy]** (BK) — [Perez et al., NEJM 2019](https://doi.org/10.1056/NEJMoa1901183); ACC.19 coverage (snippet) — [ACC.org](https://acc.org/Latest-in-Cardiology/Articles/2019/03/08/15/32/sat-9am-apple-heart-study-acc-2019)
- In the Apple Heart Study, notification rates were over 3% in participants older than 65. Limitations included the low patch return rate and self-reported data (snippet) — [ACC.org](https://acc.org/Latest-in-Cardiology/Articles/2019/03/08/15/32/sat-9am-apple-heart-study-acc-2019)
- **Fitbit Heart Study** (Circulation, 2022): 455,699 participants, about 1% notified. AF was found on a follow-up ECG patch in 32.2% of those who wore one, and the PPV of a notification during patch wear was about 98%. **[EST for detection accuracy]** (BK) — [Lubitz et al., Circulation 2022](https://doi.org/10.1161/CIRCULATIONAHA.122.060291)
- **Huawei Heart Study** (JACC, 2019): 187,912 participants, 0.23% "suspected AF", PPV 91.6% (BK) — [Guo et al., JACC 2019](https://doi.org/10.1016/j.jacc.2019.08.019)

**AF screening RCTs: detection ↑, hard outcomes unproven**
- **eBRAVE-AF** (Nature Medicine, 2022): a randomised trial of smartphone-PPG screening in 5,551 insured adults. It roughly doubled new AF diagnoses leading to anticoagulation (OAC) within 6 months (about 1.33% vs 0.66%). It was not powered for stroke. **[SEE: detection → treatment]** (BK) — [Rizas et al., Nat Med 2022](https://doi.org/10.1038/s41591-022-01979-w)
- **EQUAL trial** (JACC, 2026, Netherlands): patients ≥65 years at elevated stroke risk (CHA₂DS₂-VASc ≥2 men, ≥3 women) were randomised to 6 months of smartwatch PPG + single-lead ECG monitoring or to standard care. New-onset AF was found in 9.6% vs 2.3%. The trial reports detection only, not stroke outcomes (snippet) — [JACC](https://www.jacc.org/doi/10.1016/j.jacc.2025.11.032)
- **LOOP** (Lancet, 2021): 6,004 people aged 70–90 with risk factors got an implantable loop recorder. AF detection was about 31.8% vs 12.2%, and OAC was started in about 29.7% vs 13.1%. Stroke or systemic embolism was **not significantly reduced** (HR 0.80, 95% CI 0.61–1.05). **[EST: more detection ≠ proven stroke reduction]** (BK) — [Svendsen et al., Lancet 2021](https://doi.org/10.1016/S0140-6736(21)01698-6)
- **STROKESTOP** (Lancet, 2021): about 28,768 people aged 75–76 were screened with intermittent handheld ECG. The composite outcome showed a small net benefit (HR 0.96, 95% CI 0.92–1.00). That is a marginal effect from a *clinical-grade* intermittent ECG, not from a consumer wearable (BK) — [Svennberg et al., Lancet 2021](https://doi.org/10.1016/S0140-6736(21)01637-8)
- **Heartline** (Apple/J&J, US adults ≥65): randomised watch + app vs control. Its primary endpoint is time to clinical AF diagnosis from claims, with cardiovascular outcomes secondary. The design paper was published in 2023 (snippet) — [Am Heart J design paper](https://www.sciencedirect.com/science/article/pii/S0002870323000145). **I found no published Heartline outcome results in this session** (see Gaps).
- **USPSTF (2022):** "I" statement, meaning insufficient evidence to assess screening asymptomatic adults ≥50 for AF (BK) — [USPSTF](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/atrial-fibrillation-screening)
- **ESC 2024 AF guidelines:** a clinical AF diagnosis requires ECG confirmation (12-lead, or single or multiple leads). A PPG alert alone is not a diagnosis. DOAC for device-detected subclinical AF with elevated risk is only a weak recommendation that "may be considered" (Class IIb, from memory) (BK) — [Van Gelder et al., Eur Heart J 2024](https://doi.org/10.1093/eurheartj/ehae176)

**Treating what monitoring finds: anticoagulation for device-detected or subclinical AF**
- **NOAH-AFNET 6** (NEJM, 2023): edoxaban vs placebo in 2,536 patients with device-detected atrial high-rate episodes. It was stopped early, the primary composite outcome was not significantly reduced, and bleeding increased (BK) — [Kirchhof et al., NEJM 2023](https://doi.org/10.1056/NEJMoa2303062)
- **ARTESiA** (NEJM, 2024): apixaban vs aspirin in 4,012 patients with subclinical AF. Stroke or systemic embolism was about 0.78% vs 1.24% per year (HR 0.63). Major bleeding was about 1.71% vs 0.94% per year (BK) — [Healey et al., NEJM 2024](https://doi.org/10.1056/NEJMoa2310234)
- **Study-level meta-analysis** of both trials (McIntyre et al., Circulation 2023/24; 6,548 patients): ischaemic stroke RR 0.68 (0.50–0.92, rated high-quality evidence), major bleeding RR 1.62 (1.05–2.5), with no significant reduction in cardiovascular or all-cause mortality. The benefit is real but smaller than in clinical AF **[EST]** (snippet) — [SGUL open-access PDF](https://openaccess.sgul.ac.uk/id/eprint/115979/1/mcintyre-et-al-2023-direct-oral-anticoagulants-for-stroke-prevention-in-patients-with-device-detected-atrial.pdf); [UKE portal](https://fis.uke.de/portal/de/publications/direct-oral-anticoagulants-for-stroke-prevention-in-patients-with-devicedetected-atrial-fibrillation-a-studylevel-metaanalysis-of-the-noahafnet-6-and-artesia-trials(39a8ce1f-0311-498c-bf94-6eb316323a55).html)
- A German press release says the stroke benefit was smaller than expected in NOAH-AFNET 6 (snippet) — [idw](https://idw-online.de/de/news833864)

**Blood pressure from wearables**
- **Apple Watch Hypertension Notifications:** FDA-cleared in **September 2025** for non-pregnant adults ≥22. The watch uses PPG over 30-day windows with an ML model, gives a notification only (no BP values), and tells the user to take home cuff readings for 7 days. In a validation study of more than 2,000 participants, **sensitivity was 41.2%** (214 of 585 people with BP ≥130/80) and **specificity 92.3%**. A JAMA modelling study (Feb 2026, NHANES) estimated a PPV of about 69%. Without an alert, an estimated 21% of users still have undiagnosed hypertension (34% at age ≥60). In January 2026, a *Hypertension* editorial by six researchers said performance is "not suitable for large-scale, reliable hypertension screening". **[PBU for screening benefit; detection characteristics known]** (snippet) — [AAFP blog](https://www.aafp.org/pubs/afp/afp-community-blog/entry/smartwatch-screening-for-hypertension.html); [Medical Economics, 10 Sep 2025](https://www.medicaleconomics.com/view/the-newest-apple-watch-will-flag-possible-hypertension-pending-fda-clearance); [Houston Methodist, May 2026](https://www.houstonmethodist.org/blog/articles/2026/may/smartwatch-hypertension-notifications-how-seriously-should-you-take-it/)
- **Cuffless BP validation:**
  - The ESH Working Group's 2022 statement says cuff-based validation protocols are inadequate for cuffless devices.
  - ESH's 2023 recommendations define six validation tests: static accuracy, hydrostatic position, BP decrease with treatment, awake/asleep, exercise, and recalibration drift.
  - ISO 81060-3:2022 is the cuffless standard.
  - Some cuffless devices are marketed as "validated" under cuff protocols that were not designed for them.
  - Most cuffless devices need individual cuff calibration.
  - (snippet) — [ESH statement record](https://researchers.mq.edu.au/en/publications/cuffless-blood-pressure-measuring-devices-review-and-statement-by/); [ESH validation recommendations record](https://researchers.mq.edu.au/en/publications/european-society-of-hypertension-recommendations-for-the-validati/); [Frontiers Med Technol 2024](https://www.frontiersin.org/journals/medical-technology/articles/10.3389/fmedt.2024.1464473/pdf)
- **US regulatory loosening for wellness wearables:** In mid-2025 the FDA sent WHOOP a warning letter over BP estimation. On **6 Jan 2026** it revised the General Wellness guidance (and the Clinical Decision Support guidance) so that non-invasive devices estimating BP, SpO₂, glucose or HRV can be sold as wellness products if they make no disease claims. On **23 Jan 2026** it issued a **draft guidance on cuffless BP devices** that sets out the evidence expected for medical-device claims. Commentators disagree on how far this goes (Hardian: "not really" a free pass) (snippet) — [Covington, Jan 2026](https://www.cov.com/news-and-insights/insights/2026/01/fda-issues-revised-guidance-on-general-wellness-products); [Foley](https://www.foley.com/p/102meea/digital-health-policy-fda-relaxes-restrictions-over-wearables-and-ai-decision-ma/); [Hardian Health](https://www.hardianhealth.com/insights/fda-wearables-guidelines-update-2026); vendor framing: [Oura blog](https://ouraring.com/blog/new-fda-guidance/)

**Glucose: OTC CGMs for people not on insulin**
- **Dexcom Stelo** was FDA-cleared on 5 March 2024 as the first over-the-counter CGM, for adults not using insulin (BK) — [FDA press release](https://www.fda.gov/news-events/press-announcements/fda-clears-first-over-counter-continuous-glucose-monitor).
- **Abbott Lingo** was cleared as an OTC CGM for adults without diabetes in June 2024 (snippet) — [MedTech Dive](https://www.medtechdive.com/news/dexcom-over-the-counter-cgm/709615/)
- **No trial evidence of benefit in people without diabetes.**
  - A May 2025 review asks whether there is any benefit at all.
  - A clinical commentary answers "we don't know" on whether these devices drive weight loss, healthier eating or earlier detection of prediabetes.
  - At a January 2026 congress, an expert said "we need more studies".
  - **[PBU]** (snippet) — [Clinical Correlations, 22 May 2025](https://www.clinicalcorrelations.org/2025/05/22/could-adults-without-diabetes-benefit-from-continuous-glucose-monitoring/); [Healio, 20 Jan 2026](https://www.healio.com/news/endocrinology/20260120/cgm-may-be-beneficial-for-people-without-diabetes-but-more-research-needed)
- **Reference CGM ranges in healthy adults:** mean glucose is about 99 mg/dL, with about 96% of time in 70–140 mg/dL. Short post-meal "spikes" are normal physiology (BK) — [Shah et al., JCEM 2019](https://doi.org/10.1210/jc.2018-02763)
- **FDA safety communication (Feb 2024):** do not use smartwatches or smart rings that claim to measure blood glucose non-invasively. None is FDA-authorised (BK) — [FDA](https://www.fda.gov/medical-devices/safety-communications/do-not-use-smartwatches-or-smart-rings-measure-blood-glucose-levels-fda-safety-communication)

**Other regulated wearable features (status, not outcomes)**
- Sleep-apnoea risk notifications were authorised by the FDA for Samsung Galaxy Watch (De Novo, Feb 2024) and Apple Watch (510(k), Sep 2024). Both are detection or risk-flag features with no outcome data (BK) — verify in the [FDA De Novo database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm) and the [FDA 510(k) database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm)
- Apple's "AFib History" (AF burden estimate) became the first digital health technology qualified under the FDA's MDDT programme (May 2024), for use as a biomarker in cardiac-ablation trials (BK) — [FDA MDDT programme](https://www.fda.gov/medical-devices/medical-device-development-tools-mddt)

### Inferences
- **Underlying technology:**
  - Wrist or finger PPG gives pulse irregularity, HR, HRV, SpO₂ and sleep staging.
  - Single-lead ECG (watch crown or electrodes) confirms rhythm.
  - Accelerometry measures activity, gait and falls.
  - Minimally invasive CGM measures interstitial glucose.
  - PPG plus ML gives BP *classification* (Apple) or calibrated BP estimates (various).
  - Clinical-grade comparators are ECG patches (e.g., 14-day), implantable loop recorders, validated cuff ABPM/HBPM, and lab HbA1c.
- **Maturity:** AF detection is technically mature and widely deployed (hundreds of millions of devices). BP and glucose wearables are at the "regulatory foothold" stage: Apple's notification is a classifier, not a measurement.
- **The bottleneck is not sensing but clinical pathway and outcome evidence.** Each alert must be confirmed (ECG, ABPM, HbA1c), reviewed by a clinician, and turned into a treatment decision whose benefit-risk is uncertain in low-burden disease (ARTESiA vs NOAH-AFNET 6). **[EST]** that the alert itself is not the diagnosis.
- **Barriers:**
  - Low PPV in low-prevalence (young) users, which drives anxiety and extra visits.
  - No reimbursement for reviewing consumer data.
  - Clinicians lack time and lack a way to ingest consumer data into the EHR.
  - Liability for "seen but not acted on" data.
  - MDR/FDA status differs by feature and region.
  - Validation standards for cuffless BP are still forming: draft FDA guidance January 2026, ISO 81060-3 from 2022.
- **Timelines (forecasts, my judgement):**
  - **2026–2030:** watch AF alerts and hypertension and sleep-apnoea notifications become routine *referral triggers* **[SEE]**. OTC CGM grows as consumer wellness, with clinical value outside diabetes unproven **[PBU]**. Cuffless BP is used for trends and screening, not for diagnosis or titration **[PBU]**.
  - **2030–2035:** validated cuffless BP (ISO 81060-3 / FDA-guidance compliant) is plausibly accepted for home monitoring in some pathways **[PBU]**. Outcome trials of consumer-wearable screening, Heartline-type, may settle whether earlier AF detection reduces stroke **[PBU]**.
  - **2035–2040:** non-invasive optical glucose and fully passive, calibration-free continuous BP at clinical grade **[SPEC]**. No authorised device exists today (FDA Feb 2024 warning).
- **Software implications (no device manufacturing needed):**
  - (a) **Ingestion and normalisation**: Apple HealthKit, Android Health Connect, vendor cloud APIs (Withings, Oura, Fitbit/Google, Dexcom), mapped to FHIR Observations.
  - (b) **The "alert → confirmation → decision" workflow**: an ECG/ABPM confirmation order, a clinician review queue, an audit trail, and patient messaging. This is the gap between millions of alerts and few clinical actions.
  - (c) **Population-specific thresholds and de-duplication**, to cut low-PPV noise.
  - Commercially, consumer-facing "wellness dashboards" are crowded and dominated by device makers. The B2B workflow layer for clinics that receive wearable-triggered patients is less contested (inference).
  - **Regulatory boundary:** software that interprets wearable data to diagnose or recommend treatment is medical-device software (EU MDR Rule 11, usually Class IIa+). Storing, displaying and routing data with clinician-set thresholds is lower risk. The boundary needs case-by-case qualification under the EU's MDCG guidance — [EC MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en) (BK).

### Gaps
- **Heartline outcome results:** two searches found none. Status (presented, published or pending) is unknown. This is the key outcome trial for consumer AF screening.
- **Smart rings (Oura):** I could not verify Oura's validation studies, sales figures, or whether any Oura feature is FDA-cleared or CE-marked as a medical device. Only Oura's own blog on the FDA guidance was surfaced.
- **Aktiia/Hilo and Samsung cuffless BP:** I could not verify whether any cuffless optical BP device has FDA 510(k) clearance or CE marking under MDR, or a full ISO 81060-3 validation, as of October 2026.
- **CE/MDR status in the EU of Apple's hypertension and sleep-apnoea features:** not verified.
- **Any RCT of OTC CGM in normoglycaemic adults with clinical outcomes:** none found. Prediabetes trials were not retrieved.
- **The exact ESC 2024 recommendation class and wording on smartwatch screening:** not re-verified.

---

## 2. Remote patient monitoring and chronic disease management: where does RPM improve outcomes, and what staffing/workflow model makes it work?

### Takeaway
RPM improves hard outcomes only when **monitoring is wired to a clinical team that acts on a protocol.** The clearest examples are:
- **heart failure** with a 24/7 physician–nurse telemedicine centre (TIM-HF2: about 30% lower all-cause mortality);
- **implanted pulmonary-artery pressure sensors**: about 30% fewer HF hospitalisations, no mortality effect;
- **hypertension** with self-monitoring plus medication titration: about 3–5 mmHg lower SBP at 12 months.

Monitoring-only programmes, such as Tele-HF, BEAT-HF, and BP-monitoring-only digital tools, show little or no benefit. US fee-for-service RPM shows signs of billing without full service delivery.

### Cited Findings
**Heart failure: non-invasive telemonitoring**
- **TIM-HF2** (Lancet, 2018; Germany): 1,538 HF patients sent weight, BP, ECG, SpO₂ and self-rated health daily to a **Telemedical Interventional Management Centre staffed 24/7 by physicians and HF nurses**, who coordinated with the patients' own doctors.
  - Percentage of days lost to unplanned cardiovascular hospitalisation or death: 4.88% vs 6.64% (ratio about 0.80, p≈0.046).
  - All-cause mortality: HR about 0.70 (95% CI 0.50–0.96).
  - **[SEE/EST for this staffed model]** (BK) — [Koehler et al., Lancet 2018](https://doi.org/10.1016/S0140-6736(18)31880-4)
- **Negative telemonitoring RCTs:** monitoring without a strong clinical response loop failed.
  - **Tele-HF** (NEJM, 2010; 1,653 patients, telephone IVR symptom and weight reporting): no difference in readmission or death at 180 days.
  - **BEAT-HF** (JAMA Intern Med, 2016; 1,437 patients): no difference in 180-day readmission.
  - **[EST that monitoring alone ≠ benefit]** (BK) — [Chaudhry et al., NEJM 2010](https://doi.org/10.1056/NEJMoa1010029); [Ong et al., JAMA Intern Med 2016](https://doi.org/10.1001/jamainternmed.2015.7712)
- **2025 meta-analysis** (Cureus, 15 studies: 9 RCTs and 6 cohorts): RPM reduced HF hospitalisation (RR 0.80, 95% CI 0.77–0.84), with larger effects from implantable haemodynamic and CIED monitoring. The mortality results were not visible in the snippet. A 2024 review of 61 studies found a trend toward lower mortality, but more rehospitalisation, in monitored patients. A 2026 medRxiv preprint argues the mortality evidence is firmer, but it is not peer-reviewed (snippet) — [Cureus meta-analysis via PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12538109/)

**Heart failure: implantable pulmonary-artery pressure (CardioMEMS)**
- **CHAMPION** (Lancet, 2011; 550 patients): about 28% fewer HF hospitalisations at 6 months (BK) — [Abraham et al., Lancet 2011](https://doi.org/10.1016/S0140-6736(11)60101-3)
- **GUIDE-HF** (Lancet, 2021; 1,000 patients, NYHA II–IV, sham-controlled): the overall primary composite was **neutral** (HR about 0.88). In the pre-COVID analysis it was HR about 0.81 (p≈0.049). This led to US guideline Class 2b, and the FDA expanded the indication to NYHA II (BK and snippet) — [Lindenfeld et al., Lancet 2021](https://doi.org/10.1016/S0140-6736(21)01754-2); [ACC MONITOR-HF summary](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/07/18/17/21/monitor-hf)
- **MONITOR-HF** (Lancet, 2023; 348 patients, 25 Dutch sites, open-label): better quality of life (KCCQ) and fewer HF hospitalisations (snippet) — [ACC summary](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/07/18/17/21/monitor-hf)
- **Meta-analyses:**
  - Clephas et al., Eur Heart J 2023 (CHAMPION + GUIDE-HF + MONITOR-HF, 1,898 patients): total HF hospitalisations 0.41 vs 0.59 per patient-year (HR 0.70, 95% CI 0.58–0.86), with **no clear mortality effect**.
  - A 2024 Scientific Reports meta-analysis (5 RCTs, 2,572 patients): HF hospitalisation RR 0.72, no mortality effect.
  - **[EST for hospitalisation; no mortality benefit]** (snippet) — [ACC journal scan](https://www.acc.org/latest-in-cardiology/journal-scans/2023/10/10/16/38/efficacy-of-pulmonary-artery); [Sci Rep 2024](https://link.springer.com/10.1038/s41598-024-63742-0)

**Germany: reimbursed HF telemonitoring (the European reference model)**
- **How the service works:** patient data go to a **telemedical centre (TMZ)**. The TMZ evaluates them and forwards them to the **primary treating physician (PBA)** when predefined thresholds are crossed.
- **Billing:**
  - EBM codes GOP 13583–13587 are paid **outside the practice budget** (extrabudgetär).
  - The PBA codes for indication and enrolment are 03325/04325/13578, and the care flat rate is 03326/04326/13579.
  - Since **July 2025**, a transmitter-cost flat rate, GOP 40909, worth €396.67, is billable.
- **Eligibility:** NYHA II–III with LVEF <40%, plus an implanted ICD/CRT or an HF hospitalisation in the last 12 months.
- **Approval:** practices need KV approval under a quality-assurance agreement.
- **Extension:** a regional contract (AOK Baden-Württemberg / Bosch BKK) added HFpEF/HFmrEF coverage (E42b, €263) from 1 Oct 2025.
- (snippet) — [KBV: Telemonitoring Herzinsuffizienz](https://www.kbv.de/praxis/digitalisierung/anwendungen/telemonitoring-herzinsuffizienz); [KBV Praxisnachricht 26 Jun 2025](https://www.kbv.de/praxis/tools-und-services/praxisnachrichten/2025/06-26/transmitter-fuer-telemonitoring-und-telemedizinische-funktionsanalyse-abrechnung-ab-juli-ueber-den-ebm-moeglich); [KV Hessen approval form](https://www.kvhessen.de/fileadmin/user_upload/kvhessen/Mitglieder/Qualitaet_Behandlung/GENEHMIGUNG_Telemonitoring_bei_Herzinsuffizienz_TmHi_Antrag.pdf); [MEDI Verbund, Sep 2025](https://www.medi-verbund.de/wp-content/uploads/2025/10/2025-09-24_Kardio-Verguetungsanpassungen-01.07.25__01.10.25.pdf)
- No official national enrolment numbers were found. One figure in a Medtronic slide (2.2 million) has unclear scope and should not be used (snippet).

**Hypertension**
- **TASMINH4** (Lancet, 2018; 1,182 UK primary-care patients): GPs used self-monitored BP to titrate medication, with or without telemonitoring. SBP at 12 months was lower by about 3.5 mmHg (self-monitoring) and about 4.7 mmHg (telemonitoring) vs usual care **[EST]** (BK) — [McManus et al., Lancet 2018](https://doi.org/10.1016/S0140-6736(18)30309-X)
- **HOME BP** (BMJ, 2021; 622 patients): a digital self-monitoring and self-titration intervention cut SBP by about 3.4 mmHg (95% CI −6.1 to −0.8) at 12 months and was judged cost-effective. Its digital system worked with the practice's prescribing plan, at low staff time **[EST]** (BK) — [McManus et al., BMJ 2021](https://doi.org/10.1136/bmj.m4858)
- **IPD meta-analysis** (PLoS Med, 2017): self-monitoring *alone* gives a small BP reduction. Effects are larger when combined with co-interventions such as medication titration, education and counselling (BK) — [Tucker et al., PLoS Med 2017](https://doi.org/10.1371/journal.pmed.1002389)
- **PHTI (Oct 2024)** assessed 11 US digital hypertension solutions:
  - **Medication-management** models showed clinically meaningful BP reductions and long-term savings.
  - **BP-monitoring-only** and behaviour-change solutions lowered SBP only marginally vs standard of care.
  - A 2025 Peterson Center policy report says RPM is most effective for hypertension, notably in the first 6 months.
  - (snippet) — [PHTI Digital Hypertension Assessment PDF](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Assessment-Report.pdf); [Fierce Healthcare](https://www.fiercehealthcare.com/digital-health/remote-monitoring-hypertension-worth-zilch-without-medication-management-phti); [MedCity News, Apr 2025](https://medcitynews.com/2025/04/remote-monitoring-policy/)
- **Ochsner "Digital Medicine"** (Am J Med 2017): home BP feeding a pharmacist plus health-coach team reached about 71% BP control vs 31% in usual care at 90 days. This was not randomised (BK; numbers to verify) — [PubMed search: Milani Ochsner digital hypertension 2017](https://pubmed.ncbi.nlm.nih.gov/?term=Milani+improving+hypertension+control+patient+engagement+digital+tools)

**Diabetes**
- **CGM in insulin-treated T2D:** the MOBILE RCT (JAMA, 2021; 175 patients on basal insulin) found HbA1c lower by about 0.4 percentage points vs fingerstick monitoring. CGM in T1D and insulin-treated T2D is guideline-standard **[EST]** (BK) — [Martens et al., JAMA 2021](https://doi.org/10.1001/jama.2021.7444)
- **PHTI's diabetes RPM assessment** (tools using non-continuous glucometers) was largely unfavourable: little clinical benefit, higher spending (snippet) — [PHTI Diabetes RPM brief](https://phti.org/wp-content/uploads/sites/3/2023/11/Assessment-Area-Brief-Diabetes-RPM-1-1.pdf); [Fierce Healthcare](https://www.fiercehealthcare.com/digital-health/remote-monitoring-hypertension-worth-zilch-without-medication-management-phti)

**COPD**
- **2024 systematic review** (Frontiers in Digital Health; 29 studies, 4,326 patients, 2012–2023): telemonitoring can reduce COPD readmissions but most likely does not reduce HF readmission burden. The authors call for more high-quality studies. A 2025 Spanish article cites a Cochrane review (29 studies) showing a "moderate reduction in readmissions", and a meta-analysis giving RR 0.74 for exacerbation-related admissions. I could not verify the Cochrane review directly **[SEE/PBU, heterogeneous]** (snippet) — [Stergiopoulos et al., Front Digit Health 2024](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2024.1441334/full); [Open Respiratory Archives 2025](https://www.elsevier.es/en-revista-open-respiratory-archives-11-pdf-download-S2659663625000414)

**Health-system scale telehealth and telecare (UK)**
- **Whole System Demonstrator** (BMJ, 2012; about 3,230 patients with diabetes, COPD or HF): telehealth was associated with fewer emergency admissions and lower 12-month mortality. But the cost-effectiveness analysis (BMJ, 2013) found it **not cost-effective** at the time, at about £92k per QALY (BK) — [Steventon et al., BMJ 2012](https://doi.org/10.1136/bmj.e3874); [Henderson et al., BMJ 2013](https://doi.org/10.1136/bmj.f1035)

**US RPM billing context, and signs of "data without care"**
- **CPT codes:**
  - 99453: setup and education.
  - 99454: device supply, 16–30 days of data.
  - 99457/99458: treatment management, first 20 minutes / each additional 20 minutes.
  - 99091.
- **CY2026 Physician Fee Schedule** (final rule 31 Oct 2025): adds **99445** (2–15 days of data, paid at the 99454 rate) and **99470** (first about 10 minutes of management with real-time interaction, about half of 99457). Sources differ on exact thresholds (snippet) — [Physicians Practice, 5 Nov 2025](https://www.physicianspractice.com/view/2026-physician-fee-schedule-final-rule-is-here-what-it-means-for-rpm-and-remote-care); [HRS blog](https://www.healthrecoverysolutions.com/blog/2026-rpm-and-ccm-reimbursement-codes-and-payment-updates); [Prevounce, Feb 2026](https://blog.prevounce.com/cms-confirms-cpt-99445-will-be-covered-for-fqhcs-and-rhcs-in-2026-rpm-programs)
- **HHS-OIG report (Sept 2024):**
  - Medicare RPM users grew from about 55,000 (2019) to more than 570,000 (2022), and payments rose more than 20×.
  - About **43% of enrollees did not receive all three components** (education, device, treatment management): 28% had no setup or education, 23% no device, 12% no treatment management.
  - CMS does not know what is being monitored or who ordered it.
  - Industry argues the codes are separable services, so read this as a warning signal, not proof of fraud.
  - (snippet) — [Healthcare Dive](https://www.healthcaredive.com/news/remote-patient-monitoring-medicare-oversight-oig/728039/); [DLA Piper, Sep 2024](https://dlapiper.com/insights/publications/2024/10/oig-report-recommends-oversight-for-remote-patient-monitoring-in-medicare)

**Staffing burden and alert fatigue**
- A 2026 survey of 103 nurses in nurse-led remote **post-operative** care found that a high volume of digital alerts is linked to "digital alert fatigue". Higher alert fatigue was associated with **lower escalation behaviour**, even after adjusting for workload and escalation protocols (snippet) — [BMC Nursing 2026](https://link.springer.com/article/10.1186/s12912-026-04486-2)
- In inpatient and ICU settings, alarm-fatigue reviews report that alarms are seen as too frequent, reduce trust, and have been linked to missed events. This is a different setting but shows the same mechanism (snippet) — [PubMed 33202907](https://pubmed.ncbi.nlm.nih.gov/33202907/)

### Inferences
- **What makes RPM work.** Synthesising TIM-HF2, the negative Tele-HF and BEAT-HF trials, TASMINH4/HOME BP, PHTI and CardioMEMS, five conditions are needed together:
  1. **A high-risk population** with frequent, preventable events (recently decompensated HFrEF; uncontrolled hypertension).
  2. **A physiologic signal that maps to an action**: weight or PA pressure → diuretic change; home BP → titration step.
  3. **A named team responsible for review, with service levels**: a 24/7 physician–nurse centre (TIM-HF2, the German TMZ), an HF-nurse team (CardioMEMS), pharmacist/coach teams (Ochsner), or the patient self-titrating under a GP plan (HOME BP).
  4. **Protocolised escalation to the treating physician.**
  5. **Payment for the service, not the device** (German EBM; US 99457/99470 management codes).
  When condition 2 or 3 is missing (Tele-HF, BEAT-HF, BP-monitoring-only tools), the result is "data without benefit".
- **Staffing models, ranked by evidence:**
  - (A) Centralised telemedicine centre plus treating physician (German TMZ/PBA) **[SEE/EST, HF]**.
  - (B) Specialist-nurse review of implanted-sensor data **[EST for HF hospitalisation]**.
  - (C) Pharmacist- or nurse-led protocol titration for hypertension **[EST]**.
  - (D) Patient self-management with a digital titration plan and light GP oversight **[EST for BP, about 3 mmHg]**.
  - (E) US-style outsourced vendor nurse call centres paid per CPT code: good **commercial** traction, weak and uneven **clinical** evidence, and OIG scrutiny **[PBU]**.
- **The core economic problem is human review time per patient per month.** Software that cuts it gives operators margin and capacity, which makes it the most defensible software value in RPM (inference). It does this through:
  - rules and ML triage;
  - suppression of non-actionable alerts;
  - pre-drafted notes;
  - auto-documentation of time and interactions for billing or quality assurance;
  - patient self-titration guidance.
- **Maturity:**
  - HF and hypertension RPM: clinically proven and reimbursed in Germany and the US.
  - COPD: mixed.
  - Diabetes: the outcome benefit comes from CGM itself, not generic RPM.
  - In most of the EU, including Romania (not verified), RPM is not systematically reimbursed. It exists as pilots, hospital programmes or private-pay services.
- **Barriers:**
  - Staffing.
  - Alert fatigue.
  - Integration with the EHR and with whoever prescribes.
  - Liability for missed alerts.
  - Reimbursement.
  - Patient adherence (device return and daily measurement rates fall over time).
  - Device logistics.
  - Fraud and abuse scrutiny in the US.
- **Timelines (forecasts):**
  - **2026–2030:** RPM for HFrEF after hospitalisation and for uncontrolled hypertension becomes standard where paid (DE, parts of NL/FR/Nordics, US). Other EU countries copy the German TMZ model slowly **[SEE]**.
  - **2030–2035:** RPM bundled into chronic-care payment (value-based or DRG-adjacent). AI triage cuts nurse review time substantially. That cut is **[PBU]**, since no RCT shows AI triage preserves outcomes.
  - **2035–2040:** monitoring as a default part of chronic-disease care plans **[SPEC]**.
- **Software implications for a solo founder:** the device layer is commoditised (Withings, Omron, A&D, plus cellular hubs such as Tenovi). Opportunities are:
  1. A **review-queue / triage workbench** for clinics or TMZ-like services: threshold rules, escalation, notes, audit, time tracking.
  2. A **hypertension titration-protocol workflow** for GP or private-clinic chains, HOME BP-like, in Romanian.
  3. **Reporting and quality-assurance exports** for payers.
  - Oracle APEX/PL-SQL and n8n fit internal-tool and operations dashboards well.
  - Clinical decision logic (e.g., suggesting dose changes) moves the product into MDR Class IIa+, which a solo founder with €25k cannot certify quickly (inference).

### Gaps
- **German HF telemonitoring uptake:** number of TMZs, enrolled patients 2022–2026, and outcomes in routine care were not found. KBV, Zi or GKV-SV data are needed.
- **Benchmarks for workload per patient:** alerts per patient per month, minutes of review, nurse:patient ratios. No robust published figure was retrieved.
- **Cost-effectiveness:** TIM-HF2 economic evaluation, and the CardioMEMS NICE position, were not retrieved.
- **The Cochrane COPD telemonitoring review:** exact citation and certainty grades not verified.
- **Romania:** whether CNAS or any private insurer reimburses telemonitoring for HF or hypertension. Not searched, because the budget was exhausted.

---

## 3. Aging populations, home healthcare and long-term monitoring: how big is the need (EU, Romania) and what is the evidence for fall detection, ambient sensors and care-home monitoring?

### Takeaway
The demographic need is certain and large. The EU's working-age to 65+ ratio falls from about 2.8 (2020) to about 1.7 (2070). Romania's population is projected to shrink to about 14–15.6 million by 2080–2100, with old-age dependency rising sharply. But the evidence that monitoring technologies improve outcomes for older people is **weak**: about 98.5% of fall-detection studies use simulated falls, real-world false alarms are high, and the UK's large telecare RCT found no reduction in service use. Products here should be sold on **operational efficiency and family reassurance**, not proven clinical outcomes.

### Cited Findings
**EU demographics**
- The 2024 Ageing Report (European Commission), as cited in a 2026 Romanian journal article: in 2020 there were 28 people aged 20–64 for every 10 people aged 65+ in the EU. This is projected to fall to 19 by 2045 and 17 by 2070 (snippet) — [Drăghici, Romanian J. Political Science 2026](https://rjps.reviste.ubbcluj.ro/wp-content/uploads/2026/06/2.-Draghici.pdf); report page (not opened, egress-blocked) — [EC 2024 Ageing Report](https://economy-finance.ec.europa.eu/publications/2024-ageing-report-economic-and-budgetary-projections-eu-member-states-2022-2070_en)
- The EU population share aged 65+ was about 21.3% on 1 Jan 2023 and is rising (BK; verify against the latest Eurostat edition) — [Eurostat: Population structure and ageing](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Population_structure_and_ageing)
- Eurostat's latest projections (reported April 2026): the EU share aged 20–64 falls from 58% to 50% by 2100 (snippet) — [Romania-Insider, Apr 2026](https://romania-insider.com/eurostat-romania-population-decline-april-2026)

**Romania**
- Eurostat projections (reported April 2026): Romania's population falls to about **14.4 million by 2100** (snippet) — [Romania-Insider, Apr 2026](https://romania-insider.com/eurostat-romania-population-decline-april-2026)
- INS national projection (July 2026): about **15.633 million in 2080** (snippet) — [Agerpres, 10 Jul 2026](https://agerpres.ro/2026/07/10/populatia-romaniei-ar-urma-sa-scada-la-15-633-milioane-de-locuitori-in-2080-proiectie-ins--1574943)
- An earlier Commission projection (2020 country report round): 13.65 million in 2070, with old-age dependency rising from 28.6% (2019) to 56.9% (2070) (snippet) — [Economedia](https://economedia.ro/romanias-population-will-decrease-to-13-65-million-people-in-2070-the-european-commission-predicts.html)
- Observed figures:
  - Old-age dependency (65+/15–64) of 31.1 in 2024 (World Bank via FRED).
  - Total dependency ratio (young + old) of 56.8 per 100 adults on 1 Jan 2024 (INS).
  - (snippet) — [FRED SPPOPDPNDOLROU](https://fred.stlouisfed.org/series/SPPOPDPNDOLROU); [INS press release Jan 2024](https://insse.ro/cms/sites/default/files/com_presa/com_pdf/poprez_ian2024e.pdf)
- Older studies predict "one third of Romanians will be over 65 in 2050". I saw only the headline and the projection round is unclear (snippet) — [Romania-Insider](https://www.romania-insider.com/one-third-of-romanians-will-be-over-65-in-2050-studies-predict)

**Fall detection and ambient sensors: evidence quality**
- **Systematic review of ambient-assisted-living and smart-home fall detection** (Sensors, 23 Oct 2025; 80 studies): non-wearable and hybrid (wearable + ambient) sensors and deep learning performed best. These are mostly benchmark metrics (snippet) — [Gorce & Jacquier-Bret 2025, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12609574/)
- **Systematic review of fall detection 2008–2025:** **98.5% of studies relied on simulated falls**. Only two validated against real-world, unanticipated falls in the target population (snippet) — [Univ. of Catania repository](https://www.iris.unict.it/handle/20.500.11769/705569)
- **Small field trial of a wearable fall detector:** 84 false alarms vs 1 true detected fall. Wearable and depth-camera systems "suffer mostly from high false alarms", and multi-sensor fusion helps (snippet) — [Chaudhuri 2015 (UW)](https://bime.uw.edu/wordpress/wp-content/uploads/2016/11/Chaudhuri-Shomir-2015.pdf); [survey, PMC7805655](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7805655/)
- **2021 meta-review of wearable fall-detection accuracy:** too heterogeneous for meta-analysis. Trunk, foot or leg placement and multiple sensors gave the best accuracy (snippet) — [BMC Public Health 2021 (DOAJ)](https://doaj.org/article/6a9bb62668144d39b0cc9bc6ec71efa5)
- **Whole System Demonstrator telecare arm** (Age & Ageing 2013; pendant alarms and home sensors in a cluster RCT): **did not significantly reduce health and social care service use** over 12 months **[EST for that generation of telecare]** (BK) — [Steventon et al., Age Ageing 2013](https://doi.org/10.1093/ageing/aft008)

### Inferences
- **Technology:**
  - Wearable pendants and watches (accelerometer plus barometer).
  - Ambient sensors: PIR motion, door and bed sensors, smart plugs, mmWave radar, depth or thermal cameras, acoustic monitoring in care homes.
  - "Activity-of-daily-living" pattern models that flag deviations: no kitchen activity, night wandering, bathroom frequency as an early UTI or heart-failure signal.
  - Plus a classic telecare alarm-receiving centre.
- **Evidence:**
  - Detection accuracy in the lab: **[SEE]**.
  - Real-world detection accuracy: **[PBU]**.
  - Better outcomes (fewer long lies, admissions or deaths): **[PBU]**.
  - Better cost or service use: older RCT evidence was negative.
- **Maturity:** commercially deployed at scale (telecare is mainstream in the UK, Nordics and Spain), but adoption is driven by social-care budgets and family demand, not clinical evidence. **Technical feasibility is high; proven clinical value is low.**
- **Barriers:**
  - False alarms create workload for alarm centres and families.
  - Privacy, especially cameras and audio.
  - Older users do not wear the device.
  - Fragmented health vs social-care budgets.
  - Romania-specific: limited funded home-care capacity, low digital skills among older adults, rural connectivity (not verified this session).
- **Timelines:**
  - **2026–2030:** smartwatch and phone fall detection plus a family-alert app is normal for digitally active seniors. Ambient sensor kits are sold B2B2C via home-care agencies and insurers **[SEE for deployment, PBU for outcomes]**.
  - **2030–2035:** radar or multi-sensor "passive" monitoring becomes standard in newer care homes. ADL-deviation analytics feed GP or community-nurse dashboards **[PBU]**.
  - **2035–2040:** integrated home "digital twin" monitoring prompts proactive interventions for frail people at population scale **[SPEC]**.
- **Software implications:**
  - The defensible software layer is **event triage and care-team coordination**: alarm-centre or agency dashboards, rota and visit planning, family communication, incident logs, escalation trees.
  - It does not need novel sensing. It integrates commodity sensors via vendor APIs or MQTT.
  - Romanian home-care agencies, care homes (cămine de bătrâni) and Romanian diaspora families paying for parents' care are a plausible niche (inference, not market-tested).
  - Sell on staff time saved, documentation and peace of mind, not on clinical claims, which would also trigger MDR.

### Gaps
- **Ageing Report 2024 exact figures:** old-age dependency ratio path, long-term-care spending as % of GDP 2022→2070, Romania country fiche. The EC site was egress-blocked.
- **EUROPOP2023 shares for Romania:** 65+ and 80+ shares for 2030, 2040 and 2050 were not retrieved.
- **Evidence on acoustic or radar monitoring in care homes:** UK NHS or NIHR evaluations were not retrieved.
- **Romania's home-care financing:** CNAS-reimbursed îngrijiri la domiciliu volumes, private long-term-care insurance, and the number of care homes and beds were not researched.
- **Apple Watch fall-detection real-world performance data:** none retrieved.

---

## 4. Digital biomarkers and multimodal health data (voice, gait, typing, sleep, HRV): what is validated or qualified vs exploratory?

### Takeaway
A small number of digital measures have **regulatory qualification as clinical-trial tools**. The EMA qualified **stride velocity 95th centile (SV95C)** for Duchenne, as a secondary endpoint in 2019 and a primary endpoint in 2023. The FDA qualified **Apple AFib History** as an MDDT in 2024. A few wearable features are **FDA-cleared screening notifications** (AF, sleep apnoea, hypertension). Voice, typing and HRV "biomarkers" for diagnosing depression, cognitive decline and similar conditions remain **exploratory, with no qualified clinical use found**. The near-term market is pharma and CRO trials, not routine care.

### Cited Findings
- **EMA SV95C:** wearable-derived (ankle sensor). Qualified by the EMA as a secondary endpoint for ambulatory Duchenne muscular dystrophy trials (2019), then as a **primary endpoint** (2023). It is widely described as the first wearable-derived digital primary endpoint qualified by a major regulator **[EST as a regulatory precedent]** (BK; dates to verify) — [PubMed search: SV95C qualification](https://pubmed.ncbi.nlm.nih.gov/?term=stride+velocity+95th+centile+qualification)
- **FDA MDDT:** Apple Watch "AFib History" was qualified in May 2024 as a tool to estimate AF burden as a biomarker in clinical studies of cardiac ablation. It was the first digital health technology qualified via MDDT (BK) — [FDA MDDT programme](https://www.fda.gov/medical-devices/medical-device-development-tools-mddt)
- **FDA final guidance "Digital Health Technologies for Remote Data Acquisition in Clinical Investigations"** (Dec 2023): sets out verification, validation and usability expectations for DHT-derived endpoints (BK) — [FDA guidance page](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/digital-health-technologies-remote-data-acquisition-clinical-investigations)
- **FDA-cleared wearable notifications built on digital-biomarker algorithms:**
  - irregular rhythm / AF (Apple, Fitbit);
  - sleep-apnoea risk (Samsung 2024 De Novo, Apple 2024 510(k));
  - hypertension notification (Apple, Sept 2025: sensitivity 41.2%, specificity 92.3%).
  - (BK; snippet for hypertension) — [AAFP blog](https://www.aafp.org/pubs/afp/afp-community-blog/entry/smartwatch-screening-for-hypertension.html); [FDA De Novo database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm)
- **Regulatory treatment of HRV and other wellness metrics:** the FDA's January 2026 General Wellness revision explicitly covers wearables reporting HRV, SpO₂, BP and glucose for wellness without disease claims. These metrics can therefore be sold without validation as biomarkers, as long as no clinical claim is made (snippet) — [Foley](https://www.foley.com/p/102meea/digital-health-policy-fda-relaxes-restrictions-over-wearables-and-ai-decision-ma/)
- **Detection vs outcome** is shown here too: Apple's hypertension classifier is regulator-cleared, yet experts say its sensitivity is unsuitable for population screening (snippet) — [Houston Methodist, May 2026](https://www.houstonmethodist.org/blog/articles/2026/may/smartwatch-hypertension-notifications-how-seriously-should-you-take-it/)

### Inferences
- **Technology:**
  - Passive sensing: accelerometer gait (speed, stride), PPG (HRV, resting HR), sleep staging.
  - Smartphone sensing: typing dynamics, voice acoustics, mobility and GPS.
  - Active tasks: finger tapping, speech tasks.
  - Multimodal fusion models.
- **Evidence ladder:** technical verification → analytical validation → clinical validation (V3 framework) → regulatory qualification for a context of use → evidence that using it **improves decisions or outcomes**.
  - Gait speed in neuromuscular disease and AF burden have reached qualification **[EST for trial use]**.
  - Voice, typing and HRV for depression, Parkinson's or cognitive decline: many association and accuracy studies, few prospective decision-impact studies **[PBU]**.
  - HRV is a robust *prognostic* association in epidemiology, but there is no evidence that HRV-guided interventions improve outcomes (inference from the general literature; not re-sourced this session).
- **Maturity:**
  - In pharma trials: growing; regulators accept DHT endpoints case by case.
  - In clinical care: almost nil outside AF and sleep apnoea.
  - Consumer: ubiquitous, unvalidated "scores" (readiness, stress, body battery).
- **Barriers:**
  - Validation cost: multi-site cohorts, years.
  - Device and firmware drift breaks validation.
  - Population bias (skin tone and PPG, accents and voice).
  - Missing data.
  - Regulators require a clear context of use.
  - Under GDPR, voice and biometric data are special-category data.
- **Timelines:**
  - **2026–2030:** more qualified digital endpoints in rare and neuromuscular disease, PD and HF trials **[SEE]**.
  - **2030–2035:** a handful of digital biomarkers used in routine care pathways, e.g. gait speed for frailty, AF burden, nocturnal SpO₂/HRV for HF decompensation alerts **[PBU]**.
  - **2035–2040:** validated multimodal passive "digital phenotyping" for mental health and cognitive decline in primary care **[SPEC]**.
- **Software implications:**
  - Biomarker discovery needs data access, cohorts and validation budgets far beyond €25k and 10–12 hours a week. **Not a fit.**
  - Adjacent feasible niches:
    - data pipelines and quality assurance for DHT data in trials (completeness, wear-time, device-version tracking, audit trails, 21 CFR Part 11 / GCP-style logging);
    - an EDC/eCOA integration layer for academic or CRO studies in Romania or CEE.
  - Both need domain partners (inference).

### Gaps
- **Mobilise-D (IMI) real-world gait-speed endpoints:** whether EMA issued a formal qualification opinion (vs letters of support) by 2026 was not verified.
- **Voice-biomarker companies** (e.g., Kintsugi, Canary Speech, Sonde): regulatory status and corporate status in 2025–2026 not verified. I found no evidence of any FDA-cleared or EMA-qualified voice biomarker for diagnosis.
- **Typing-dynamics biomarkers** (e.g., nQ Medical): status not verified.
- **DiMe Library of Digital Endpoints counts**, and the FDA's list of trials using DHT endpoints: not retrieved.

---

## 5. Medical data interoperability and patient-controlled data: how mature is Europe (incl. Eastern Europe), what will EHDS change and when, and why did PHRs fail?

### Takeaway
The legal framework is now fixed. The **EHDS Regulation (EU) 2025/327** entered into force in March 2025 and applies from March 2027. **Cross-border exchange is mandatory from 2029** for patient summaries and ePrescriptions, and **from 2031** for images, lab results and discharge reports. EHR systems must meet EU interoperability and logging requirements on the same schedule. In practice, maturity is very uneven: Estonia and the Nordics are mature, Germany is catching up fast with the opt-out ePA (2025), and Romania is early (the national e-SănătateaMea portal becomes mandatory for CNAS-contracted providers only from Q4 2026). Standalone consumer PHRs failed for lack of data supply and clinical workflow. EHDS addresses the supply side by law, but not the workflow side.

### Cited Findings
**EU legal framework**
- **EHDS Regulation (EU) 2025/327:** published in the Official Journal on 5 March 2025, in force 26 March 2025, generally applicable from **26 March 2027**.
  - Primary-use obligations (patient access, MyHealth@EU exchange, EHR-system requirements) phase in by data category:
    - **Group 1**, patient summaries and ePrescriptions/eDispensations: **26 March 2029**.
    - **Group 2**, medical images and reports, lab results and reports, hospital discharge reports: **26 March 2031**.
  - Secondary-use provisions (Health Data Access Bodies, data permits) apply largely from **2029**, with some data categories later (2031).
  - Patients get rights to free, immediate electronic access, to restrict access, to add information, and to see who accessed their data.
  - Member States may allow opt-out from secondary use.
  - (BK; dates are well established but should be checked against Art. 105 of the text) — [EUR-Lex: Regulation (EU) 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj)
- **EHR systems** placed on the EU market must comply with "harmonised components":
  - an interoperability component based on the **European Electronic Health Record Exchange Format**;
  - a logging component;
  - self-certification with CE-type marking for EHR systems.
  - These follow the same 2029/2031 category phasing. The technical specifications come through implementing acts, which the Commission is preparing with the Xt-EHR joint action and HL7 Europe FHIR implementation guides (BK) — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2025/327/oj); [Xt-EHR joint action](https://www.xt-ehr.eu/); [HL7 Europe](https://hl7.eu/)
- **International Patient Summary (IPS):**
  - ISO 27269 plus the HL7 FHIR IPS implementation guide.
  - It is the global minimal patient summary (problems, medications, allergies, immunisations, results).
  - The EU patient summary used in MyHealth@EU is aligned with it.
  - (BK) — [HL7 FHIR IPS IG](https://hl7.org/fhir/uv/ips/); [IPS website](https://international-patient-summary.net/)
- **MyHealth@EU** is the operational cross-border infrastructure through National Contact Points for eHealth. It is live in a subset of Member States for patient summaries and/or ePrescriptions. I could not retrieve the current country list or Romania's status (EC page egress-blocked) — [EC: cross-border health services](https://health.ec.europa.eu/ehealth-digital-health-and-care/electronic-cross-border-health-services_en)

**National examples**
- **Germany:**
  - The opt-out **"ePA für alle"** launched in pilot regions on 15 Jan 2025 and nationwide on 29 April 2025. Providers have been obliged to use and fill it since 1 Oct 2025.
  - The E-Rezept (ePrescription) has been mandatory since 1 Jan 2024.
  - Implementation is through gematik's Telematikinfrastruktur.
  - (BK; dates to verify) — [gematik ePA](https://www.gematik.de/anwendungen/epa)
- **Estonia:** a national e-health record since 2008, ePrescriptions since 2010, and near-universal digital prescribing. Patients see access logs via a portal. This is the EU benchmark for "patient-controlled" transparency (BK) — [e-Estonia: e-health records](https://e-estonia.com/solutions/healthcare/e-health-records/)
- **Romania:**
  - The national **e-SănătateaMea** portal is meant to let patients see prescriptions, referrals and medical history and book online.
  - CNAS-contracted providers must use it from **Q4 2026**.
  - Patients can still book by phone, and patient organisations want phone booking kept for rural and low-digital-skill users.
  - (PN) — [Digi24](https://www.digi24.ro/stiri/actualitate/social/romanii-ar-putea-consulta-online-retetele-trimiterile-si-istoricul-medical-cum-va-functiona-platforma-e-sanatateamea-din-septembrie-3906571); [medic24](https://medic24.ro/portalul-esanatateamea-ajunge-la-promulgare-programari-online-din-trimestrul-iv/)
- **Romanian public-system usage:** an AtlasIntel survey (March 2026, n=2,325) found 32.6% had made online appointments in the public health system. In June 2026 (n=2,002), about 88% said they would choose online booking for state hospitals (PN) — [StartupCafe](https://startupcafe.ro/romanii-si-serviciile-digitale-de-stat-plata-taxelor-pe-primul-loc-ce-vor-ei-in-2026-studiu-96599)

**US comparison**
- **21st Century Cures Act** (2016) and the ONC Cures Act Final Rule (2020):
  - Information-blocking prohibitions have applied since 5 April 2021.
  - Certified EHRs had to provide standardised **FHIR R4 / US Core APIs** for patient and population access by 31 Dec 2022.
  - This created the legal basis for apps to pull records.
  - (BK) — [ONC Cures Act Final Rule](https://www.healthit.gov/topic/oncs-cures-act-final-rule)
- **TEFCA** (the national network-of-networks) went live in December 2023 with the first designated QHINs, and exchange volumes have been growing (BK) — [ONC TEFCA](https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca)
- **CMS "Health Tech Ecosystem" / Interoperability Framework** (July 2025): more than 60 companies, including big tech and EHR vendors, pledged patient-facing apps, "kill the clipboard" and conversational AI assistants, with early deliverables targeted for 2026 (BK; verify) — [CMS Health Technology Ecosystem](https://www.cms.gov/health-technology-ecosystem)
- **Apple Health Records:** launched in January 2018, pulling records from provider FHIR APIs into the iPhone Health app, starting in the US and later in the UK and Canada (BK) — [Apple Newsroom, Jan 2018](https://www.apple.com/newsroom/2018/01/apple-announces-effortless-solution-bringing-health-records-to-iphone/)

**Why personal health records (PHRs) failed**
- **Google Health** (2008–2012): discontinued because it was "not having the broad impact that we hoped", with adoption limited to some groups (BK) — [Google blog, 24 Jun 2011](https://googleblog.blogspot.com/2011/06/update-on-google-health-and-google.html)
- **Microsoft HealthVault** (2007–2019) shut down in November 2019 (BK) — [Wikipedia: Microsoft HealthVault](https://en.wikipedia.org/wiki/Microsoft_HealthVault)

### Inferences
- **Why PHRs failed (synthesis):**
  1. **No data supply.** Before the Cures Act and FHIR APIs, data had to be typed in or came from a few partners.
  2. **No clinical workflow.** Clinicians never looked at the PHR, so patients had little reason to curate it.
  3. **Episodic consumer motivation.** Health data matter only around illness events.
  4. **No business model** that did not conflict with privacy.
  - EHDS and the Cures Act fix (1) by law. Points (2) to (4) remain, so a new "patient-controlled health wallet" startup faces the same headwinds. Value now sits in **workflow-embedded** uses: pre-visit summaries, referral packages, care-plan sharing, consented data flows to RPM services.
- **What EHDS will actually change:**
  - **2027:** general obligations and governance start; Member States designate digital health authorities.
  - **2029:** every Member State must offer patients electronic access to group-1 data and exchange patient summaries and ePrescriptions via MyHealth@EU. EHR vendors selling group-1 functionality must comply with the EEHRxF interoperability and logging components.
  - **2031:** labs, imaging and discharge reports.
  - **From about 2029:** secondary use via Health Data Access Bodies.
  - Practical impact will lag the legal dates, especially in Eastern Europe, where baseline digitisation, EHR vendor capacity and FHIR skills are lower (inference).
- **Eastern Europe and Romania maturity:** Romania has centralised CNAS systems for claims, ePrescription and an electronic health record (DES), with historically low clinical use, and a new patient portal from Q4 2026. **[PBU]** that Romania meets the 2029 obligations on time. Expect national FHIR profiles and a national contact point to be built 2026–2029, plausibly with PNRR or EU funds (inference; the PNRR digital-health components were not verified this session).
- **Timelines:**
  - **2026–2030:** FHIR APIs and IPS-style summaries become a procurement requirement for EHR and clinic software in the EU. Big private networks and the German ePA lead **[SEE, legally mandated]**.
  - **2030–2035:** cross-border and in-country exchange of labs, images and discharge reports is normal in Western and Northern Europe and patchy in CEE. Patients routinely export data to apps **[SEE as forecast]**.
  - **2035–2040:** truly patient-controlled, consent-driven data flows to third-party services (RPM, AI agents) at scale **[PBU/SPEC]**.
- **Software implications (most relevant to the founder's skills):**
  - Romanian and CEE clinic, lab and EHR software vendors, many small and some on Oracle/PL-SQL stacks (inference, not verified), will need:
    - FHIR R4 façades and APIs over legacy databases;
    - mappings from local codes to LOINC, SNOMED CT and ATC;
    - generation of IPS / EU Patient Summary documents;
    - EHDS logging and access-transparency components;
    - consent and patient-access portals.
  - These are **B2B, regulation-driven, deadline-dated (2029/2031)** needs, and are not medical-device software if limited to data transport and formatting (inference).
  - Python, SQL/PL-SQL and APEX skills map directly to this work.
  - Risks: the work is slow to sell to vendors, and open-source FHIR servers (HAPI) and big vendors compete.

### Gaps
- **MyHealth@EU:** the current list of live Member States and services, and Romania's NCPeH status. Not retrieved.
- **Quantitative FHIR adoption in EU Member States:** no HL7 Europe or WHO/Europe survey figures were retrieved.
- **Romania's DES/SIUI actual usage statistics, PNRR e-health investment amounts and timelines, the national EHDS implementation plan:** not retrieved.
- **Germany ePA uptake numbers** (records created, active app users, provider usage): not retrieved.
- **EHDS implementing acts:** not verified. In particular, the exact Art. 105 transition dates for EHR-system certification and the secondary-use categories.
- **Android Health Connect medical-records (FHIR) feature status in 2025–2026:** not verified.

---

## 6. AI agents coordinating appointments, tests, follow-ups and care plans: what is deployed (2025–2026), what outcomes and safety evidence exist?

### Takeaway
LLM voice and text agents are **deployed at scale for administrative and protocolised outreach**: scheduling, reminders, pre-visit prep, benefits and payer calls, post-discharge or post-op check-ins. Vendors such as Hippocratic AI, Infinitus, Notable, Hyro and Luma in the US, and Doctolib, Tucuvi and Ufonia in the EU/UK, report large call volumes. **Peer-reviewed outcome evidence is thin**:
- simple automated reminders have established attendance benefits;
- LLM-drafted clinician messages reduce burnout scores but not time;
- autonomous clinical follow-up calls have a few validation studies (e.g., post-cataract).

The EU regime (AI Act Art. 50 transparency since August 2026; high-risk obligations from 2027–2028; MDR for clinical triage) makes **administrative coordination the low-risk entry point.**

### Cited Findings
- **Baseline evidence for automated outreach:** mobile-phone message reminders increase appointment attendance vs no reminder (RR about 1.14). The evidence is low-certainty but consistent **[EST that simple reminders help]** (BK) — [Gurol-Urganci et al., Cochrane 2013](https://doi.org/10.1002/14651858.CD007458.pub3)
- **LLM-drafted replies to patient messages:**
  - Stanford (JAMA Netw Open, 2024): AI drafts were used about 20% of the time and were associated with lower task load and emotional exhaustion, with **no significant time savings**.
  - UC San Diego (JAMA Netw Open, 2024): drafts were associated with **longer read time** and no reduction in reply time.
  - **[SEE: wellbeing benefit, no efficiency proof]** (BK) — [Garcia et al., JAMA Netw Open 2024](https://doi.org/10.1001/jamanetworkopen.2024.3201); [Tai-Seale et al., JAMA Netw Open 2024](https://doi.org/10.1001/jamanetworkopen.2024.6565)
- **Hippocratic AI:** published a "Polaris" safety-focused multi-agent LLM architecture for patient-facing, non-diagnostic nurse-like calls (pre-op, post-discharge, chronic-care check-ins). Its evaluations used panels of nurses and physicians (vendor-authored preprint) (BK) — [Polaris, arXiv 2403.13313 (Mar 2024)](https://arxiv.org/abs/2403.13313); [Hippocratic AI](https://www.hippocraticai.com/)
  - Press-reported funding: about $141M Series B (Jan 2025, about $1.6B valuation) and a later round in late 2025 at a higher valuation (BK; amounts to verify).
  - Health-system deployments (e.g., outreach for cancer-screening preparation) are reported in vendor and press material. No peer-reviewed RCT of patient outcomes was found.
- **US vendors (vendor material only; claims not verified):**
  - **Infinitus:** AI voice agents making payer and pharmacy calls (benefits verification, prior-authorisation status) for providers and pharma hubs — [infinitus.ai](https://www.infinitus.ai/)
  - **Notable:** AI agents and automation for intake, registration, scheduling, prior auth and care-gap outreach — [notablehealth.com](https://www.notablehealth.com/)
  - **Hyro:** conversational AI for health-system call centres (scheduling, Rx refills, FAQs) — [hyro.ai](https://www.hyro.ai/)
  - **Luma Health:** patient-access platform with AI agents for scheduling, reminders and referrals — [lumahealth.io](https://www.lumahealth.io/)
- **EU/UK examples (BK; vendor and press, details not verified this session):**
  - **Doctolib** (FR/DE/IT) added AI assistants, including a phone assistant, for practices in 2025.
  - **Tucuvi** (Spain): the voice agent "LOLA" makes protocolised follow-up calls to chronic and post-discharge patients for public hospitals, positioned as a CE-marked medical device.
  - **Ufonia** (UK): the autonomous voice agent "Dora" makes routine post-cataract-surgery follow-up calls in NHS trusts, with peer-reviewed feasibility and validation studies.
  - Verify the regulatory class and study details before citing.
- **Safety:** ECRI's annual Top 10 Health Technology Hazards placed AI risks at #1 for 2025 and **misuse of AI chatbots** at #1 for 2026 (BK; verify) — [ECRI Top 10 hazards](https://www.ecri.org/top-ten-tech-hazards). I found **no documented, vendor-specific patient-harm incident** for the named care-coordination agents. That reflects absence of evidence: no adverse-event reporting system exists for non-device administrative AI.
- **EU AI Act:**
  - **Art. 50** (AI-interaction disclosure) applies from **2 August 2026**, was not postponed by the Digital Omnibus (Reg. (EU) 2026/1744), and carries fines up to €15M or 3%.
  - High-risk deadlines moved: **Annex III to 2 Dec 2027, Annex I (e.g., AI in MDR devices) to 2 Aug 2028**.
  - (PN) — [AI Act Blog NL](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- **Romania:**
  - Under Romanian Law 190/2018 art. 3, automated triage decisions need explicit consent (PN) — earlier project notes in `lege_si_telefonie.md`.
  - MedOcean analysed **100,000+ calls** between patients and private-clinic operators (Jan 2025–Jan 2026), showing that phone volume remains high in Romanian private healthcare (vendor data) (PN) — [AGERPRES press release](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680)

### Inferences
- **Technology:**
  - LLM-based voice and text agents: speech-to-text, LLM with tool-calling, text-to-speech.
  - Integrated with scheduling and EHR APIs (FHIR Appointment/Slot, HL7v2 SIU), telephony (SIP/Twilio), and messaging (SMS/WhatsApp).
  - Orchestration and workflow engines (n8n-class), guardrails, human hand-off, and call recording and audit.
- **Evidence grades by task:**
  - Reminders and recalls: **[EST]** for attendance.
  - Agent-led scheduling and intake: **[SEE]** for operational metrics (vendor-reported throughput, call deflection), not for patient outcomes.
  - Protocolised clinical follow-up calls (post-op, chronic): **[SEE/PBU]**, with early validation studies (e.g., post-cataract).
  - Autonomous care-plan management (ordering tests, adjusting therapy): **[SPEC]**, and regulated as a medical device if done.
- **Maturity:** US deployment is broad (driven by labour costs and payer-call burden). EU deployment is growing via practice-software platforms (Doctolib) and public-hospital pilots (Tucuvi). Romania is early: clinics still depend on call centres and phone, and the national portal goes live in Q4 2026.
- **Barriers:**
  - Integration with scheduling and EHR systems, which is often closed in Romania.
  - Clinical safety for anything beyond admin tasks.
  - AI Act transparency and, for triage, high-risk and MDR obligations.
  - GDPR special-category data and DPAs with LLM vendors (EU hosting).
  - Romanian-language speech quality.
  - Patient acceptance, especially among older callers.
  - Liability for missed red-flag symptoms during "admin" calls, which needs escalation scripts.
- **Timelines:**
  - **2026–2030:** AI agents handling scheduling, reminders, recalls, results-ready notifications, pre-visit questionnaires and no-show recovery become **normal** in private EU clinics **[SEE for adoption]**.
  - **2030–2035:** protocolised clinical follow-up agents (post-discharge, post-op, chronic check-ins) under nurse supervision become common as CE-marked devices. Agents coordinate across providers using EHDS data **[PBU]**.
  - **2035–2040:** autonomous "care-coordinator" agents managing whole care plans across organisations **[SPEC]**.
- **Software implications for the founder:** this is the most accessible area (Python, LLM APIs, n8n, web backends).
  - Build in the **administrative coordination** lane:
    - recall and follow-up campaigns for private clinics (e.g., "your annual check / lab test is due");
    - results-ready and missed-appointment flows;
    - referral tracking ("did the patient book the cardiology appointment the GP ordered?");
    - pre-visit data collection;
    - **closing the loop after a wearable or RPM alert** (scheduling the confirmatory ECG or ABPM).
  - Keep clinical judgement with humans (escalation rules, red-flag scripts). Disclose AI per Art. 50.
  - This connects areas 1–2 (alerts that need action) with area 5 (data exchange). The care-coordination layer is where "data without benefit" becomes "data → action" (inference).

### Gaps
- **Measured outcomes from named vendors:** no peer-reviewed RCT or controlled outcome study was retrieved this session for Hippocratic AI, Infinitus, Notable, Hyro or Luma. Only vendor and press claims exist, and they were not verified.
- **Tucuvi and Ufonia:** exact regulatory class (MDR/UKCA), study citations and outcome metrics not verified.
- **Documented safety incidents** involving care-coordination voice agents: none found. Searching was limited.
- **Romanian or CEE deployments of LLM agents in healthcare:** beyond vendor lists in earlier project notes, no evidence was retrieved.

---

## 7. Cross-cutting: where is there RCT or prospective evidence of outcome benefit from monitoring, and where does monitoring create data without benefit (or extra workload and false alarms)?

### Takeaway
Outcome benefit is proven only in narrow, high-risk, action-coupled settings: HF telemonitoring with a staffed centre, implanted PA-pressure sensors, BP self-monitoring with titration, and CGM in insulin-treated diabetes. Broad, low-risk, consumer or alert-only monitoring mostly produces **detections, alerts and workload without proven hard-outcome benefit**: AF screening, OTC CGM, BP monitoring without medication management, generic diabetes RPM, fall detectors, and first-generation telecare.

### Cited Findings
**Outcome benefit shown**
- HF telemonitoring with a 24/7 physician–nurse centre: mortality HR about 0.70 (TIM-HF2) **[SEE/EST]** — [Lancet 2018](https://doi.org/10.1016/S0140-6736(18)31880-4)
- PA-pressure-guided HF management: HF hospitalisation HR about 0.70, no mortality effect **[EST]** — [ACC journal scan of Eur Heart J meta-analysis](https://www.acc.org/latest-in-cardiology/journal-scans/2023/10/10/16/38/efficacy-of-pulmonary-artery)
- BP self-monitoring with titration: about −3.4 to −4.7 mmHg SBP at 12 months **[EST]** — [TASMINH4](https://doi.org/10.1016/S0140-6736(18)30309-X); [HOME BP](https://doi.org/10.1136/bmj.m4858)
- Anticoagulating device-detected AF: ischaemic stroke RR 0.68, but bleeding RR 1.62 **[EST, net benefit depends on the patient]** — [McIntyre meta-analysis](https://openaccess.sgul.ac.uk/id/eprint/115979/1/mcintyre-et-al-2023-direct-oral-anticoagulants-for-stroke-prevention-in-patients-with-device-detected-atrial.pdf)
- CGM in insulin-treated T2D: HbA1c about −0.4 points vs fingerstick **[EST]** — [MOBILE, JAMA 2021](https://doi.org/10.1001/jama.2021.7444)
- COPD telemonitoring: readmission reduction in some studies **[SEE/PBU]** — [Front Digit Health 2024](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2024.1441334/full)

**Detection or data without proven outcome benefit, or with net workload**
- AF screening raises detection 2–4× (LOOP, eBRAVE-AF, EQUAL), but there is no significant stroke reduction (LOOP) and only a marginal composite benefit (STROKESTOP). USPSTF: "I" statement — [LOOP](https://doi.org/10.1016/S0140-6736(21)01698-6); [STROKESTOP](https://doi.org/10.1016/S0140-6736(21)01637-8); [USPSTF](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/atrial-fibrillation-screening)
- Telemonitoring without a strong response loop showed no benefit (Tele-HF, BEAT-HF) — [NEJM 2010](https://doi.org/10.1056/NEJMoa1010029); [JAMA IM 2016](https://doi.org/10.1001/jamainternmed.2015.7712)
- BP-monitoring-only digital solutions gave a marginal SBP effect (PHTI). Diabetes RPM with fingerstick glucometers was unfavourable (PHTI) — [PHTI hypertension report](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Assessment-Report.pdf); [PHTI diabetes brief](https://phti.org/wp-content/uploads/sites/3/2023/11/Assessment-Area-Brief-Diabetes-RPM-1-1.pdf)
- OTC CGM in non-diabetics: no outcome evidence — [Clinical Correlations 2025](https://www.clinicalcorrelations.org/2025/05/22/could-adults-without-diabetes-benefit-from-continuous-glucose-monitoring/)
- The hypertension wearable notification misses about 59% of hypertensive users. Experts call it unsuitable for population screening — [AAFP](https://www.aafp.org/pubs/afp/afp-community-blog/entry/smartwatch-screening-for-hypertension.html)
- Fall detection: 98.5% of studies use simulated falls, and a field trial found 84 false alarms per true fall — [Catania review](https://www.iris.unict.it/handle/20.500.11769/705569); [Chaudhuri 2015](https://bime.uw.edu/wordpress/wp-content/uploads/2016/11/Chaudhuri-Shomir-2015.pdf)
- Telecare did not reduce service use (WSD). Telehealth was not cost-effective (WSD) — [Age Ageing 2013](https://doi.org/10.1093/ageing/aft008); [BMJ 2013](https://doi.org/10.1136/bmj.f1035)
- US RPM: 43% of Medicare RPM enrollees lacked at least one service component — [Healthcare Dive on OIG](https://www.healthcaredive.com/news/remote-patient-monitoring-medicare-oversight-oig/728039/)
- Alert fatigue reduces nurse escalation in remote post-op care — [BMC Nursing 2026](https://link.springer.com/article/10.1186/s12912-026-04486-2)

### Inferences
- **Rule of thumb for the report:** benefit scales with (baseline event risk) × (actionability of the signal) × (reliability of the human or protocol response). Remove any one factor and the result is data without benefit.
- The **commercial opportunity sits in the response loop**: triage, routing, coordination, documentation. More sensing is not where the value is. This is the software layer that turns existing signals (watch alerts, home BP, RPM readings, portal data) into protocolised action. Solo founders can build it without devices or primary clinical data (inference).
- **Technical vs commercial feasibility:** almost everything above is *technically* feasible today. *Commercial* feasibility depends on a payer or budget holder: the German EBM, US CPT codes, private clinic subscriptions, employers or insurers. Romania lacks reimbursement for RPM, as far as found, so near-term buyers are private clinic networks, private insurers and corporate health programmes (inference; Romanian market not researched here).

### Gaps
- No head-to-head study was retrieved that compares staffing models (centralised centre vs practice-based vs vendor nurse) on outcomes and cost.
- No quantified false-alarm or "alerts per actionable event" benchmarks for consumer AF or BP alerts in primary care were retrieved.

---

## 8. Cross-cutting: what will realistically be normal by 2030, 2035 and 2040 vs speculative, and what software and infrastructure does each area need?

### Takeaway
By about 2030, the "normal" set is:
- wearable alerts as referral triggers;
- reimbursed HF and hypertension RPM in a few systems;
- EHDS group-1 exchange (patient summaries, ePrescriptions) live across the EU;
- AI agents handling administrative coordination.

By about 2035: lab, imaging and discharge data exchange; validated cuffless BP; protocolised AI follow-up as certified devices. Truly autonomous AI care coordination and calibration-free non-invasive glucose or BP remain speculative for 2040. For a small software founder, the durable opportunities are the **workflow, integration and coordination layers** that regulation (EHDS) and payment (EBM, CPT) make necessary.

### Cited Findings (anchors for the forecast; details in sections 1–6)
- EHDS legal milestones: 2027 application; 2029 patient summaries and ePrescriptions; 2031 images, labs and discharge reports — [EUR-Lex 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj) (BK)
- AI Act milestones: Art. 50 from 2 Aug 2026; high-risk Annex III from 2 Dec 2027; Annex I from 2 Aug 2028 — [AI Act Blog NL](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) (PN)
- Romania: e-SănătateaMea mandatory for CNAS providers from Q4 2026 — [medic24](https://medic24.ro/portalul-esanatateamea-ajunge-la-promulgare-programari-online-din-trimestrul-iv/) (PN)
- FDA's January 2026 wellness loosening plus the draft cuffless BP guidance shape the consumer-sensor market — [Hardian](https://www.hardianhealth.com/insights/fda-wearables-guidelines-update-2026) (snippet)
- German HF telemonitoring is reimbursed, with a transmitter flat rate from July 2025 — [KBV](https://www.kbv.de/praxis/digitalisierung/anwendungen/telemonitoring-herzinsuffizienz) (snippet)
- US RPM codes expanded in 2026 (99445/99470) — [Physicians Practice](https://www.physicianspractice.com/view/2026-physician-fee-schedule-final-rule-is-here-what-it-means-for-rpm-and-remote-care) (snippet)

### Inferences

**Forecast table** (my judgement; grades show confidence that this will be *normal practice*, not technical possibility)

| Area | Normal by 2030 | Normal by 2035 | 2040 / speculative |
|---|---|---|---|
| 1. Wearables / continuous monitoring | Watch AF, sleep-apnoea and hypertension notifications as routine referral triggers with ECG/ABPM confirmation [SEE]. OTC CGM as wellness [SEE adoption / PBU benefit]. Cuffless BP for trends only [PBU] | Validated cuffless BP accepted for home monitoring in some pathways [PBU]. Clearer evidence on whether consumer AF screening reduces stroke [PBU] | Calibration-free non-invasive glucose; clinical-grade passive BP everywhere [SPEC] |
| 2. RPM / chronic disease | HF (post-hospitalisation HFrEF) and uncontrolled-hypertension RPM reimbursed in DE, US and a few others. TMZ-like services spread [SEE] | RPM bundled into chronic-care payment in more EU states. AI triage cuts review time [PBU] | Monitoring as a default part of every chronic care plan [SPEC] |
| 3. Aging / home care | Fall detection on watches; ambient kits via home-care agencies and insurers [SEE deployment / PBU outcomes] | Passive radar or multi-sensor monitoring standard in new care homes; ADL-deviation analytics to community nurses [PBU] | Population-scale proactive home "digital twins" [SPEC] |
| 4. Digital biomarkers | More qualified trial endpoints (DMD, PD, HF, AF burden) [SEE] | A few biomarkers (gait speed, AF burden, nocturnal HRV/SpO₂ in HF) in routine pathways [PBU] | Validated voice, typing or multimodal mental-health and cognition screening in primary care [SPEC] |
| 5. Interoperability / patient data | EHDS group 1 (patient summaries, ePrescriptions) exchange and patient access in most EU states by 2029. Romania lagging [SEE legally / PBU on time] | Group 2 (labs, images, discharge) by 2031; certified EHR interoperability components. HDAB secondary use operating [SEE legally] | Patient-directed, consented data flows to any third-party service as routine [PBU/SPEC] |
| 6. AI agents | Admin agents (scheduling, reminders, recalls, intake, payer calls) normal in private clinics, with AI disclosure [SEE] | Certified protocolised clinical follow-up agents under nurse supervision; cross-provider coordination using EHDS data [PBU] | Autonomous care-plan coordinators across organisations [SPEC] |

**Infrastructure and software each area requires** (what must exist for the forecast to happen, and where a small software firm can play):
- **Data ingestion:** HealthKit, Health Connect and vendor cloud APIs. Normalised to FHIR Observation, Device and Provenance. Time-series storage (Postgres/Timescale or Oracle). Device-agnostic.
- **Rules and triage engine:** clinician-configurable thresholds, alert de-duplication and suppression, escalation trees, SLAs, worklists. **This is the core RPM value.**
- **Care-coordination and task layer:** orders and referrals tracking, appointment booking (FHIR Appointment), patient messaging (SMS, WhatsApp, voice AI), closing the loop after an alert.
- **Documentation and billing evidence:** time tracking, interaction logs, exports for EBM/CPT or private-payer reporting, and audit trails (EHDS logging).
- **Interoperability:**
  - a FHIR R4 façade over legacy databases (Oracle/PL-SQL fit);
  - terminology mapping (LOINC, SNOMED CT, ATC);
  - IPS / EU patient summary generation;
  - consent management;
  - readiness for MyHealth@EU and EHDS EHR certification by 2029/2031.
- **Compliance scaffolding:**
  - GDPR (Art. 9 health data, DPIA, EU hosting, DPAs with LLM vendors);
  - AI Act Art. 50 disclosure;
  - an MDR qualification and classification assessment (MDCG guidance; Rule 11) to stay non-device or Class I where possible.

**Founder-fit filter** (inference: Romania, solo, €25k, 10–12 h/week, no device manufacturing, no clinical data at first)
- **Good fit** (B2B, workflow and integration, non-device):
  - (i) FHIR/IPS integration adapters and EHDS-readiness tooling for Romanian/CEE clinic, lab and EHR software vendors (deadline-driven 2029/2031).
  - (ii) Care-coordination and recall/follow-up automation for private clinic networks: AI-assisted but administrative, Art. 50-compliant.
  - (iii) An RPM operations workbench (triage queue, escalation, documentation) for cardiology, GP or private RPM services, sold as non-diagnostic workflow software.
  - (iv) Operations software for home-care agencies and care homes with commodity-sensor event integration.
- **Poor fit:**
  - own wearables;
  - digital-biomarker discovery or validation;
  - diagnostic AI (MDR Class IIa+ certification costs and timelines);
  - consumer PHR or "health wallet" apps (the Google Health / HealthVault failure pattern);
  - US RPM billing businesses (OIG scrutiny, distance from the market).
- **Key commercial uncertainty:** who pays in Romania. CNAS reimbursement for RPM and telemonitoring was not found. Private networks and insurers are the likely early buyers. This needs validation by the market-focused research stream.

### Gaps
- No authoritative forecast (EC, OECD, WHO Europe) of RPM or AI-agent adoption by 2030/2035 was retrieved. The table above is my judgement, anchored on legal deadlines and current evidence.
- Romanian payer landscape (CNAS, private insurers, corporate subscriptions) for monitoring and coordination services: not researched in this stream.
- OECD / WHO Europe digital-health maturity indices for Romania vs EU peers: not retrieved (egress-blocked).
