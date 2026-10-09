# Science, maturity and timelines of the "prediction and prevention" side of predictive healthcare (status October 2026)

How to read these notes:

- **Evidence grade tags:** **[EST]** Established evidence · **[SEE]** Strong emerging evidence · **[PBU]** Plausible but unproven · **[SPEC]** Speculative.
- **Source-quality tags:**
  - **(PR)** a peer-reviewed primary study, reached through a search summary.
  - **(CO)** company or sponsor press material. Treat with caution.
  - **(SN)** a detail that appears only in a search-result summary or trade/news coverage.
  - **(PK)** comes from the researcher's prior knowledge. The DOI or URL was given but not re-checked this session. Verify before quoting.
  - **(FC)** a forecast, plan or policy target, not an observed result.
- **Method limits:**
  - WebFetch was blocked by the egress proxy for every primary domain tried: bmj.com, pmc.ncbi.nlm.nih.gov, fda.gov, nice.org.uk, grail.com, health.ec.europa.eu and uwclinicaltrials.org. No full texts were read. Every non-PK fact comes from WebSearch result summaries of the linked pages.
  - The shared WebSearch budget ran out after about 31 queries. Some planned checks therefore rest on (PK) items or are listed under Gaps: AF screening trials, the Camden Coalition RCT, EHDS dates, the FDA AI device count, the NHS EDITH breast-AI trial, and the OECD digital chapters.
- **Core distinction used throughout:** *accuracy* (AUC, sensitivity, detection rate) ≠ *process change* (more tests ordered, more diagnoses) ≠ *patient outcome* (stage shift, morbidity, mortality, quality of life) ≠ *commercial feasibility*.

---

## Key Question 1 — Which predictive/preventive technologies have RCT or prospective evidence of improved outcomes, and which only have retrospective accuracy?

### Takeaway
Only a few predictive technologies have randomized or prospective evidence of benefit that goes beyond accuracy. The strongest are:
- **AI-supported mammography reading:** an RCT with fewer interval cancers.
- **Autonomous diabetic-retinopathy screening:** an RCT showing many more exams completed and more follow-through.
- **AI-ECG for low ejection fraction:** a pragmatic RCT showing more diagnoses.
- **Hospital deterioration and sepsis alerts:** prospective but non-randomized mortality associations, and only when paired with a response workflow.
- **Lifestyle diabetes prevention:** RCT, including an AI-delivered version that was non-inferior.
- **Digital-twin-guided AF ablation:** one RCT, conference data.

Almost everything else is retrospective accuracy only: EHR foundation models, polygenic scores, lung-nodule AI, most dermatology AI, consumer biomarker panels and full-body MRI. Multi-cancer blood testing has its first RCT, NHS-Galleri, which **missed its primary endpoint**.

### Cited Findings

#### Area 1 — AI-assisted early detection and risk stratification

**AI mammography — MASAI RCT (Sweden)**
- **Design:** more than 100,000 women were randomized to AI-supported reading (Transpara) or standard double reading. Final results were published in *The Lancet* in early 2026 (DOI 10.1016/S0140-6736(25)02464-X). [SEE] (PR via SN) — [Lund University](https://www.lunduniversity.lu.se/article/ai-support-breast-cancer-screening-fewer-missed-cancer-cases); [Textbook of Digital Health news, 2026-01-29](https://www.textbookofdigitalhealth.com/news/2026-01-29-masai-ai-mammography.html)
- **Final results, reported by the vendor and the press:**
  - 12% fewer interval cancers, which is an outcome-proximal endpoint.
  - 16% fewer invasive interval cancers.
  - 21% fewer large (T2+) interval cancers.
  - 27% fewer non-luminal-A (aggressive) interval cancers.
  - Sensitivity 80.5% vs 73.8% at the same specificity.
  - No increase in false positives.
  — (CO/SN) [ScreenPoint Medical](https://screenpoint-medical.com/insights/final-results-masai-trial); [AXIS Imaging News](https://axisimagingnews.com/radiology-products/womens-imaging/mammography/ai-supported-mammography-screening-reduces-aggressive-breast-cancers)
- **Earlier MASAI reports:** 29% higher cancer detection and 44% lower screen-reading workload than double reading. (CO/SN) — [ScreenPoint Medical](https://screenpoint-medical.com/insights/final-results-masai-trial)
- **Caveats:** one programme, short follow-up, and enrolment counts that vary between sources (100k, 105k, 106k). Breast-cancer mortality has not been measured. (SN) — [Textbook of Digital Health](https://www.textbookofdigitalhealth.com/news/2026-01-29-masai-ai-mammography.html)

**AI mammography — PRAIM (Germany), real-world implementation study**
- **Design:** observational, prospective, non-inferiority study. 463,094 women were screened (260,739 with AI support) by 119 radiologists at 12 sites, July 2021 to February 2023. *Nature Medicine*, January 2025, DOI 10.1038/s41591-024-03408-6. [SEE] (PR via SN) — [Pharmacy Times, 2025-01-10](https://pharmacytimes.com/view/ai-improves-breast-cancer-screening-and-detection-rates-in-real-world-study); [Univ. Lübeck record](https://research.uni-luebeck.de/en/publications/nationwide-real-world-implementation-of-ai-for-cancer-detection-i/)
- **Results:**
  - Cancer detection was 6.7 vs 5.7 per 1,000, a relative increase of 17.6% (95% CI +5.7% to +30.8%), or roughly one extra cancer per 1,000.
  - Recall was 37.4 vs 38.3 per 1,000, which met the non-inferiority bar.
  - Radiologists chose voluntarily whether to use the AI, so selection bias is possible.
  - The vendor (Vara) co-ran the study.
  — (SN) [Pharmacy Times](https://pharmacytimes.com/view/ai-improves-breast-cancer-screening-and-detection-rates-in-real-world-study); [Vara press release](https://vara.ai/press-releases/ai-supported-mammography-revolutionizes-breast-cancer-detection) (CO)

**AI-ECG for low ejection fraction — EAGLE pragmatic cluster RCT (Mayo Clinic, NCT04000087)**
- **Design:** 120 primary-care teams (358 clinicians) and 22,641 adults without prior heart failure. *Nature Medicine* 2021. [SEE for process outcome] (PR via SN) — [Nature Medicine via Springer](https://link.springer.com/article/10.1038/s41591-021-01335-4); [TCTMD](https://www.tctmd.com/news/ai-ecg-allows-early-diagnosis-low-ef)
- **Results:**
  - New low-EF diagnoses within 90 days: 2.1% vs 1.6% (OR 1.32), about 5 extra diagnoses per 1,000 screened.
  - Overall echo use was unchanged: 19.2% vs 18.2% (p=0.17).
  - Among AI-positive patients, echo use rose from 38.1% to 49.6%. Even when alerted, only about half got the confirmatory test.
  - Whether earlier detection improves long-term outcomes is still unresolved.
  — (SN) [Mayo Clinic News Network](https://newsnetwork.mayoclinic.org/discussion/trial-demonstrates-early-ai-guided-detection-of-heart-disease-in-routine-practice/); [TCTMD](https://www.tctmd.com/news/ai-ecg-allows-early-diagnosis-low-ef)

**Autonomous diabetic-retinopathy screening (IDx-DR / LumineticsCore)**
- **Pivotal trial:** a prospective study (npj Digital Medicine 2018) supported FDA De Novo authorization in April 2018. It reported sensitivity of about 87% and specificity of about 91%. [EST for accuracy] (PK) — [Abràmoff et al., npj Digit Med 2018](https://doi.org/10.1038/s41746-018-0040-6)
- **ACCESS RCT** (youth aged 8–21 with diabetes; Nature Communications, January 2024; NCT05131451):
  - Exam completion within six months was 100% with point-of-care autonomous AI vs 22% with referral.
  - Among abnormal results, follow-through to an eye-care provider was 64% vs 22% (p<0.001).
  - This shows a care-gap closure effect, not an accuracy effect. [SEE]
  — (PR via SN) [UW Ophthalmology](https://www.ophth.wisc.edu/blog/2024/01/11/autonomous-artificial-intelligence-increases-screening-and-follow-up-for-diabetic-retinopathy-in-youth-the-access-randomized-control-trial); [Healio](https://www.healio.com/news/optometry/20240122/ai-system-boosts-diabetic-eye-exam-completion-rates-among-youth-with-diabetes)

**Sepsis and deterioration prediction**
- **Epic Sepsis Model** (University of Michigan, 38,455 hospitalizations; *JAMA Internal Medicine* 2021):
  - AUC 0.63, sensitivity 33%, PPV 12%.
  - This was retrospective external validation. Epic disputed the threshold choice.
  [EST that the proprietary model underperformed vendor claims] (PR via SN) — [JAMA Intern Med](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781313); [Healthcare IT News](https://www.healthcareitnews.com/news/research-suggests-epic-sepsis-model-lacking-predictive-power)
- **TREWS** (Johns Hopkins; *Nature Medicine* 2022; prospective, multisite, non-randomized):
  - 590,736 patients were monitored across 5 hospitals; the analysis covered 6,877 sepsis patients.
  - When an alert was confirmed by a clinician within 3 hours, mortality was about 18.7% lower in relative terms than when it was not. This is an association and confounding is possible.
  - About 89% of alerts were evaluated.
  [SEE, observational] (PR via SN) — [Scientific American](https://www.scientificamerican.com/article/algorithm-that-detects-sepsis-cut-deaths-by-nearly-20-percent/); DOI (PK) [10.1038/s41591-022-01894-0](https://doi.org/10.1038/s41591-022-01894-0)
- **Other prospective deployments of deterioration models with outcome signals.** All of these are non-randomized and come from prior knowledge, so verify before citing:
  - Kaiser Permanente "Advance Alert Monitor", rolled out in staggered fashion across Kaiser Permanente Northern California hospitals and paired with a remote nurse response team. The exact hospital count was not verified. It was associated with lower 30-day mortality. [SEE] (PK) — [Escobar et al., NEJM 2020](https://doi.org/10.1056/NEJMsa2001090)
  - UCSD COMPOSER sepsis model, before/after design, about 17% relative reduction in in-hospital sepsis mortality. (PK) — [Boussina et al., npj Digit Med 2024](https://doi.org/10.1038/s41746-023-00986-6)
  - Toronto CHARTwatch, about 26% relative reduction in non-palliative deaths. (PK) — [Verma et al., CMAJ 2024](https://doi.org/10.1503/cmaj.240132)

**Lung-nodule AI**
- **Retrospective validation** (Radboud, *Radiology*, September 2025):
  - Trained on NLST and tested on DLCST, MILD and NELSON: more than 4,000 participants and about 8,000 nodules.
  - At 100% sensitivity, it classed 68.1% of benign nodules as low risk vs 47.4% for PanCan, a 39.4% relative reduction in false positives.
  - AUC for indeterminate nodules was 0.95 vs 0.91.
  [PBU for outcomes, SEE for accuracy] (PR via SN) — [RSNA news, Sept 2025](https://www.rsna.org/news/2025/september/ai-estimates-lung-cancer-risk)
- **LUNA25 challenge** (*Radiology: AI*, July 2026): AI beat the average radiologist on 5–15 mm nodules. The authors say prospective studies are still needed. (SN) — [Radboudumc 2026](https://www.acc.radboudumc.nl/en/research/news/News-items-by-our-research-institute/2026/AI-estimates-cancer-risk-in-difficult-lung-nodules-better-than-radiologists)
- **Prospective studies:** one is registered (Qure.ai qXR, NCT05817110). No published prospective outcome data were found. (SN) — [ClinicalTrials.gov NCT05817110](https://clinicaltrials.gov/study/NCT05817110)

**Dermatology AI (Skin Analytics DERM)**
- **Regulatory status:** the first dermatology AI with a Class III CE mark under EU MDR for autonomous use. A smartphone version, "DERM Zero", is also CE Class III according to the company. (CO/SN) — [EMJ](https://www.emjreviews.com/innovations/news/the-worlds-first-autonomous-ai-skin-cancer-detector-approved-for-use-in-europe/)
- **NICE (HTE24, May 2025):** recommends it *conditionally* for 3 years while more evidence on clinical and cost-effectiveness is generated. (SN) — [PharmaTimes](https://pharmatimes.com/news/nice-recommends-first-ai-medical-device-for-skin-cancer-diagnosis-in-the-nhs/)
- **Headline performance claims:**
  - 97% of cancers detected and a melanoma NPV of 99.8%.
  - An NHS England-commissioned analysis covered 33,693 real-world lesions.
  - These figures are mostly vendor or NHS-linked. No peer-reviewed prospective outcome RCT was found.
  [SEE for safe triage/discharge of benign lesions; PBU for outcomes] (CO/SN) — [NHS England AI skin lesion page](https://www.england.nhs.uk/elective-care/best-practice-solutions/ai-based-skin-lesion-analysis-technology/)

#### Area 2 — Predictive analysis of longitudinal health records

**Delphi-2M** (*Nature*, September 2025, DOI 10.1038/s41586-025-09529-3)
- A modified GPT trained on about 0.4M UK Biobank participants and validated, unchanged, on 1.9M Danish individuals.
- It predicts more than 1,000 diseases with "accuracy comparable to existing single-disease models".
- It can simulate synthetic health trajectories up to 20 years ahead.
- **Caveats:**
  - The authors call it a proof of concept.
  - It learned biases from UK Biobank.
  - Accuracy falls over longer horizons.
  - It does better for chronic diseases than for infections or trauma.
  - The weights are restricted under UK Biobank access rules.
- **Evidence status:** retrospective only, no outcome evidence. [PBU] (PR via SN) — [UK Biobank publication page](https://www.ukbiobank.ac.uk/publications/learning-the-natural-history-of-human-disease-with-generative-transformers/); [Scientific American](https://www.scientificamerican.com/article/new-ai-tool-predicts-which-of-1-000-diseases-someone-may-develop-in-20-years/)

**Foresight** (*Lancet Digital Health*, 2024;6(4):e281–e290; a retrospective modelling study)
- Trained on more than 811,000 patients from King's College Hospital and South London and Maudsley (structured data plus free text via CogStack) and on MIMIC-III.
- Precision@10 for the next concept was 0.80, 0.81 and 0.91 across the three datasets.
- A 2025 pilot is running in the NHS England Secure Data Environment.
- **Evidence status:** no outcome evidence. [PBU] (PR via SN) — [KCL news](https://www.kcl.ac.uk/news/researchers-investigate-ability-of-their-new-ai-tool-to-predict-medical-events); [Maudsley BRC, 7 May 2025](https://www.maudsleybrc.nihr.ac.uk/news/groundbreaking-ai-trained-on-de-identified-patient-data-to-predict-healthcare-needs/)

**CLMBR-T-base and MOTOR (Stanford)**
- CLMBR-T-base has 141M parameters and was trained on 2.57M patients' structured EHR data. It is released with the EHRSHOT benchmark of 6,739 patients, and the weights are gated.
- MOTOR (ICLR 2024) is a time-to-event foundation model trained on EHR and claims data.
- Evidence of cross-site generalization is limited.
- An LLM-embedding approach matched CLMBR on 15 EHRSHOT tasks.
[PBU] (SN) — [EHRSHOT arXiv](https://arxiv.org/pdf/2307.02028); [Stanford HAI slides](https://hai.stanford.edu/sites/default/files/2024-06/%28Jason%20Fries%29%20EHR%20Foundation%20Models.pdf)

**Shortcomings of EHR foundation models in evaluation** (PK)
- A 2023 review found that EHR foundation models are mostly evaluated on narrow accuracy tasks and on a few datasets.
- It found little evaluation of clinically meaningful use.
— [Wornow et al., npj Digit Med 2023](https://doi.org/10.1038/s41746-023-00879-8)

**Classic validated risk scores (QRISK3, SCORE2, FINDRISC, CHA2DS2-VASc)**
- These are embedded in guidelines, so their accuracy is [EST].
- Direct RCT evidence that *giving people or clinicians a risk score* improves hard outcomes is weak.
- A Cochrane review found low-certainty evidence that providing CVD risk scores slightly lowers risk-factor levels and slightly increases preventive prescribing. It found no clear evidence on cardiovascular events. [PBU for outcome effect of score use] (PK) — [Karmali et al., Cochrane 2017](https://doi.org/10.1002/14651858.CD006887.pub4)
- Specific accuracy statistics for each score were not collected this session (see Gaps).

**Polygenic risk scores (PRS)**
- **Pooled cohort equations:** adding a CAD PRS raised the C-statistic by only about 0.02 (n=352,660). The authors say more investigation is needed before clinical use. (PR via SN) — [JAMA 2020](https://jamanetwork.com/journals/jama/article-abstract/2761088)
- **QRISK2, seven UK cohorts:** AUROC was 0.635 alone and 0.623 with the gene score, i.e. "minimal incremental population-wide utility". The authors suggest a possible role at intermediate risk (10–20%), where about one event could be prevented per 462 people screened (modelled). (PR via SN) — [Brunel repository](https://bura.brunel.ac.uk/handle/2438/19071?mode=full)
- **Outcome trials:** none with hard outcomes were found. A small RCT (MI-GENES) showed that disclosing genetic risk lowered LDL at 6 months, a surrogate measure. [PBU] (PK) — [Kullo et al., Circulation 2016](https://doi.org/10.1161/CIRCULATIONAHA.115.020109)

#### Area 3 — Blood biomarkers, periodic preventive testing, MCED and full-body MRI

**General health checks**
- **Cochrane 2019 review:** 17 trials. All-cause mortality RR 1.00 (95% CI 0.97–1.03; 11 trials, 233,298 people; high certainty). Cancer mortality RR 1.01. Cardiovascular mortality RR 1.05. [EST: no mortality benefit] (PR via SN) — [AAFP summary of Cochrane CD009009.pub3](https://www.aafp.org/afp/2019/1201/p676); [Cochrane](https://www.cochrane.org/CD009009/general-health-checks-for-reducing-illness-and-mortality)

**Broad consumer panels (Function Health-style)**
- No peer-reviewed outcome study of Function's model was found.
- The company runs tests through Quest Diagnostics, offers 100+ biomarkers twice a year, ran more than 3M tests in 2023, and acquired Ezra (full-body MRI) in May 2025.
- **Grading:** benefit [PBU]; harms from false positives and cascades are [PBU→SEE by analogy with health-check and incidental-finding literature].
— (SN) [Wikipedia: Function Health](https://en.wikipedia.org/wiki/Function_Health); [Sacra](https://sacra.com/c/function-health/)
- **Expert opinion:** the Society of General Internal Medicine discourages routine general checks for asymptomatic adults, and critics such as H. Gilbert Welch describe testing-driven overdiagnosis. (SN) — [KQED](https://www.kqed.org/futureofyou/1373/tracking-your-own-health-data-too-closely-can-make-you-sick); [NHPR](https://www.nhpr.org/national/2016-05-12/diy-blood-tests-theres-a-downside-to-ordering-your-own)

**Multi-cancer early detection (MCED) — NHS-Galleri RCT**
- **Design:** 142,250 people aged 50–77, three annual rounds. Full results were presented at ASCO on 30 May 2026; topline results came out in February 2026.
- **Primary endpoint missed:** the trial **did not meet** its primary endpoint of reducing stage III+IV cancers combined.
- **Secondary findings:**
  - Stage IV for 12 prespecified cancers fell 9%, 22% and 26% in rounds 1, 2 and 3. The overall IRR was 0.86 (95% CI 0.744–0.998), nominally significant.
  - Screen-detected cancers increased fourfold.
  - Symptomatic presentations fell 21%.
  - Stage I–II diagnoses in the 12 cancers rose 16%.
- **What is missing:** no mortality data yet; the results are sponsor-reported and await a peer-reviewed paper.
- **Grading:** detection [EST]; stage shift [PBU]; mortality [unknown].
— (CO/SN) [GRAIL press release via BioSpace](https://www.biospace.com/press-releases/grail-reports-full-results-from-nhs-galleri-trial-demonstrating-substantial-reduction-in-stage-iv-cancer-diagnoses-at-2026-asco-annual-meeting); [Clinical Lab Products](https://clpmag.com/disease-states/cancer/galleri-multi-cancer-blood-test-reduces-stage-iv-diagnoses-nhs-trial/)

**MCED — PATHFINDER 2** (about 36,000 participants in North America; ESMO October 2025)
- Cancer signal detected in 0.93% of participants; cancer detection rate 0.57%; PPV 61.6% (133 of 216).
- Adding Galleri to USPSTF A/B screenings raised detection more than sevenfold.
- The data are being submitted for FDA PMA.
- The ICR's Clare Turnbull cautioned about false-positive MCED results with no cancer found.
- This is single-arm and has no outcome endpoint. [PBU]
— (CO/SN) [GRAIL press release](https://grail.com/press-releases/grail-pathfinder-2-results-show-galleri-multi-cancer-early-detection-blood-test-increased-cancer-detection-more-than-seven-fold-when-added-to-uspstf-a-and-b-recommended-screenings/); [Touch Oncology](https://touchoncology.com/insight/pathfinder-2-galleri-mced-detects-early-cancers/); [Science Media Centre](https://www.sciencemediacentre.org/?p=56559)

**Full-body MRI in asymptomatic adults**
- **2019 meta-analysis:** critical or indeterminate incidental findings in 32.1%, false positives in 16.0%, and no verification of negatives beyond 5 years. (PR via SN) — [J Magn Reson Imaging meta-analysis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850647/)
- **CFPC Tools for Practice, 2026:** 94% have a radiologic abnormality; up to 30% need more investigation; 1.1–1.6% have a confirmed cancer; no mortality data and **no RCTs**. [EST: no proven benefit; harms documented] (SN) — [CFPC Tools for Practice #410 (PDF)](https://cfpclearn.ca/wp-content/uploads/2026/03/TFP-410-English.pdf)
- **American College of Radiology:** finds insufficient evidence to recommend total-body screening in asymptomatic people. The statement date was not confirmed. (SN) — [Reed Smith summary](https://www.reedsmith.com/our-insights/blogs/viewpoints/102inhp/even-as-questions-remain-whole-body-mri-screening-studies-grow-in-popularity/)

**Guideline (organised) screening**
- **EU Council Recommendation of 9 December 2022 (2022/C 473/01):** replaced the 2003 version. It targets 90% of eligible people being offered breast, cervical and colorectal screening by 2025. It adds a stepwise, pilot-first approach to lung screening (LDCT in high-risk groups), prostate screening (PSA + MRI) and gastric screening (*H. pylori* screen-and-treat), with €38.5M from EU4Health (2023). (SN) — [European Commission press release IP/22/7548](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_22_7548/IP_22_7548_EN.pdf); [FEAM statement](https://www.feam.eu/statement-on-the-european-council-cancer-screening-recommendations/)
- **AIM criticism:** the mutual insurers' group AIM noted that no RCTs support mass PSA screening. (SN) — [AIM press release](https://www.aim-mutual.org/wp-content/uploads/2022/12/PressRelease_CancerScreening.pdf)
- **USPSTF:** has A/B recommendations for breast, cervical, colorectal and lung (LDCT) screening, statins and prediabetes screening. It has **no** recommendation for MCED tests, consumer biomarker panels or full-body MRI. (PK) — [USPSTF A and B list](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics/uspstf-a-and-b-recommendations)
- **Detection is not the same as mortality benefit, even for colonoscopy:** in NordICC, *inviting* people to colonoscopy cut colorectal cancer incidence by about 18% at 10 years, with no significant reduction in CRC death in the intention-to-screen analysis (42% participation). (PK) — [Bretthauer et al., NEJM 2022](https://doi.org/10.1056/NEJMoa2208375)

#### Area 4 — Personalized recommendations and preventive interventions

**Diabetes Prevention Program (original RCT)**
- Intensive lifestyle intervention cut diabetes incidence by 58% (metformin by 31%) vs placebo. [EST] (PK) — [Knowler et al., NEJM 2002](https://doi.org/10.1056/NEJMoa012512)
- The effect attenuates over time: about a 27% lower incidence at 15 years in DPPOS. (PK) — [DPPOS, Lancet Diabetes Endocrinol 2015](https://doi.org/10.1016/S2213-8587(15)00291-0)

**AI-delivered DPP vs human-coached DPP** (Mathioudakis et al., *JAMA*, 27 October 2025; 2025;334(23):2079–2089; NCT05056376)
- **Design:** phase 3 pragmatic non-inferiority RCT with 368 adults with prediabetes and overweight. The AI arm used an app, a Bluetooth scale and reinforcement-learning push notifications.
- **Results:**
  - 31.7% vs 31.9% met CDC risk-reduction benchmarks at 12 months, which counted as non-inferior.
  - Initiation was 93.4% vs 82.7%.
  - Completion was 63.9% vs 50.3%.
- **Criticism:** a February 2026 JAMA letter called the 15% non-inferiority margin too wide.
- **Grading:** non-inferiority on surrogates is [SEE]; diabetes incidence was not measured.
— (PR via SN) [Patient Care](https://www.patientcareonline.com/view/ai-powered-diabetes-prevention-program-intervention-matches-human-coaching-daily-dose); [ConscienHealth](https://conscienhealth.org/2025/10/can-ai-replace-human-coaches-for-diabetes-prevention/)

**Personalized nutrition — ZOE METHOD RCT** (*Nature Medicine*, May 2024; 347 US adults)
- The primary outcome improved for triglycerides only. LDL was not significant.
- Secondary outcomes (weight, waist, gut microbiome diversity) improved.
- Company-run; methodology was criticized.
[PBU / weak SEE] (PR via SN) — [FoodNavigator](https://www.foodnavigator.com/Article/2024/05/10/Zoe-hails-personalized-nutrition-trial-success-results-come-under-scrutiny/); [TwinsUK](https://twinsuk.ac.uk/study-reveals-zoe-personalised-diets-yield-health-improvements-2/)

#### Area 5 — AI-assisted clinical workflows and clinical decision support (CDS)

**Classic computerized CDS** (Kwan et al., *BMJ* 2020;370:m3216; meta-analysis of 122 controlled trials)
- Process improvements were modest and very heterogeneous.
- In the 30 trials with clinical endpoints, the median improvement in the proportion reaching guideline targets was only **0.3%**, with no significant clinical improvement.
- The median process-of-care improvement is recalled as about 5.8% (PK). It could not be confirmed this session, so verify it. The authors' 2010 review had found typical process gains below 5%.
[EST: small process effects, little or no clinical-outcome effect] (PR via SN) — [BMJ](https://www.bmj.com/content/370/bmj.m3216); [Kwan BMJ blog](https://blogs.bmj.com/bmj/2020/09/18/janice-kwan-what-i-have-learned-about-clinical-decision-support-systems-over-the-past-decade/)

**Ambient AI scribes — RCTs**
- **UCLA** (Lukac et al., *NEJM AI*, November 2025): 238 outpatient physicians randomized 1:1:1 to Microsoft DAX, Nabla or usual care.
  - Time writing each note: Nabla −41 s vs −18 s for control. DAX was not significant.
  - Burnout benefits were only "potential".
  - Inaccuracies were "occasional" and one mild adverse event was reported.
  - Single site, short duration.
  — (PR via SN) [UCLA Health](https://www.uclahealth.org/news/release/ucla-study-finds-ai-scribes-may-reduce-documentation-time); [NCT06792890](https://clinicaltrials.gov/study/NCT06792890)
- **UW Health** (*NEJM AI*, two papers, December 2025): a trial framework paper and a paper reporting improved practitioner burnout and well-being. Exact effect sizes were not retrieved. (SN) — [Wisconsin Technology Council](https://wisconsintechnologycouncil.com/uw-health-new-research-shows-ambient-ai-measurably-improves-healthcare-practitioner-well-being)
- **Multistate pragmatic stepped-wedge trial:** documentation time fell by 0.36 h/day without loss of note quality, and work exhaustion was lower. Journal details were not confirmed. (SN) — [Consultant360](https://www.consultant360.com/exclusive/ambient-ai-scribes-linked-lower-work-exhaustion-multistate-pragmatic-trial)
- **Grading:** time saving is [SEE], modest. Burnout reduction is [SEE→PBU]. Patient-outcome effects are unknown.

**LLM decision support**
- **Goh et al., *JAMA Network Open* 2024 RCT** (50 physicians): GPT-4 access did not significantly improve diagnostic reasoning (74% vs 76%). GPT-4 alone scored 92%. (PR via SN) — [Medical Dialogues](https://medicaldialogues.in/amp/mdtv/medicine/videos/can-gpt-4-improve-diagnosis-study-provides-insights-137499); [Nature Medicine supplementary table](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04539-8/MediaObjects/41591_2026_4539_MOESM1_ESM.pdf)
- **Goh et al., *Nature Medicine* 2025 RCT** (92 physicians, management vignettes): +6.5 points with GPT-4 (95% CI 2.7–10.2), but more time spent per case. This used simulated vignettes. (PR via SN) — [The Hospitalist](https://www.the-hospitalist.org/hospitalist/article/39729/in-the-literature/gpt-4-assistance-for-improvement-of-physician-performance-on-patient-care-tasks-a-randomized-controlled-trial/)
- **Penda Health / OpenAI "AI Consult"** (Nairobi, 15 clinics, 39,849 visits; a quality-improvement study, *not randomized*; arXiv July 2025):
  - 16% fewer diagnostic errors and 13% fewer treatment errors, as rated by independent physicians.
  - Benefit depended on workflow-aligned design and active deployment.
  [SEE→PBU] (SN, preprint) — [arXiv 2507.16947](https://arxiv.org/abs/2507.16947v1)
- **Chen et al., *Nature Medicine*, March 2026** (LLM-assisted review of 4,609 clinical LLM studies, January 2022 to September 2025):
  - Only 1,048 studies used real patient data, and only **19 were prospective RCTs**.
  - Most studies were simulated (1,857) or exam-style (1,704).
  - LLMs beat humans in 33% of 1,046 comparisons, depending strongly on how realistic the task was.
  — (PR via SN) [cancer.fr summary, March 2026](https://www.cancer.fr/professionnels-de-sante/veille/nota-bene-cancer/bulletin-n-677-du-12-mars-2026/llm-assisted-systematic-review-of-large-language-models-in-clinical-medicine)

#### Area 6 — Population health analytics (risk stratification + case management)

**PRISMATIC** (Wales; randomized stepped-wedge trial; 32 practices; 230,099 patients; *BMJ Quality & Safety* 2019)
- Introducing the PRISM predictive risk-stratification tool **increased** emergency admissions by about 1%, ED attendances by about 3%, outpatient visits by about 5% and bed-days by about 3%.
- There was no evidence of benefit to patients or to the NHS.
- A concurrent payment incentive is a possible confounder.
[EST in this setting: risk-stratification software alone did not reduce admissions] (PR via SN) — [PMC6820297](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820297/); [BMJ Qual Saf](https://qualitysafety.bmj.com/content/28/9/697)

**Camden Coalition "hotspotting" RCT** (800 high-utilizer patients)
- Intensive care management after targeting by data showed no difference in 180-day readmission (about 62% in both arms). (PK) — [Finkelstein et al., NEJM 2020](https://doi.org/10.1056/NEJMsa1906848)

**Inpatient contrast**
- Where prediction was paired with a dedicated response team (Kaiser Permanente AAM), an outcome signal appeared. (PK) — [Escobar et al., NEJM 2020](https://doi.org/10.1056/NEJMsa2001090)

#### Area 7 — Digital twins

**CUVIA-PRR RCT** (ESC Congress 2025; 4 Korean centres; 304 patients with persistent AF)
- Digital-twin-guided ablation plus PVI vs PVI alone. Freedom from atrial arrhythmia at 18 months was 77.9% vs 59.5% (HR 0.52; 95% CI 0.33–0.82).
- Procedure time was similar.
- Stable targets were found in only 43.2% of the twin arm.
- These are conference results; a full paper was not confirmed.
[SEE→PBU, one narrow procedural use] (SN) — [ESC press release](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Digital-twin-technology-helps-reduce-the-recurrence-of-atrial-arrhythmias-after-catheter-ablation-for-persistent-atrial-fibrillation); [Cardiac Rhythm News](https://cardiacrhythmnews.com/digital-twin-technology-helps-reduce-atrial-arrhythmia-recurrence-after-catheter-ablation-for-persistent-af/)

**EU Virtual Human Twins (VHT) Initiative**
- Launched in December 2023, with more than 90 manifesto signatories.
- EDITH roadmap: first draft July 2023; "final draft" January 2025; policy brief October 2025, with the full roadmap pending approval.
- Five prototype use cases: cancer, cardiovascular, ICU, osteoporosis and brain.
- A €24M Digital Europe-funded VHT platform is "forthcoming", with no launch date found.
[SPEC for a whole-body twin; PBU for organ-specific twins] (SN) — [European Commission](https://digital-strategy.ec.europa.eu/en/news/virtual-human-twins-launch-european-virtual-human-twins-initiative); [Zenodo roadmap final draft](https://zenodo.org/records/14645647); [Zenodo policy brief](https://zenodo.org/records/16910818)

### Inferences
- **Evidence-tier summary (as of October 2026):**
  - **RCT with an outcome-proximal benefit:**
    - AI mammography (MASAI: interval cancers).
    - DPP lifestyle (diabetes incidence).
    - Autonomous DR screening (care-gap closure).
    - Digital-twin AF ablation (recurrence; single RCT, conference data).
  - **RCT with a process or surrogate benefit only:**
    - EAGLE AI-ECG (more diagnoses).
    - AI-DPP (CDC benchmarks).
    - ZOE (triglycerides).
    - Ambient scribes (minutes saved).
    - LLM management vignettes.
  - **RCT negative on the primary outcome:**
    - NHS-Galleri (stage III–IV).
    - PRISMATIC risk stratification (admissions went up).
    - Camden care management (PK).
    - General health checks (Cochrane).
  - **Prospective observational benefit with a response workflow:** TREWS, KP AAM, COMPOSER, CHARTwatch (PK for the last three).
  - **Retrospective accuracy only:** Delphi-2M, Foresight, CLMBR/MOTOR, PRS add-ons, lung-nodule malignancy AI, consumer biomarker panels, full-body MRI.
- **The consistent pattern:** benefit appears when prediction is attached to (a) a specific, effective action (confirm, treat or ablate), (b) a staffed workflow that acts on alerts, and (c) completion of follow-up. Area 1 is the most mature because imaging screening programmes already have that workflow, and AI is slotted into an existing reading step.
- **Commercial vs technical feasibility:** MASAI, PRAIM and DERM show CE-marked AI being bought by organised screening programmes. That market is dominated by regulated vendors (ScreenPoint, Vara, Skin Analytics). A solo founder without a validated model cannot compete there. The founder can, however, sell the *surrounding* non-device software: invitations, tracking, follow-up, audit and data quality.

### Gaps
- I could not confirm MASAI's exact Lancet numbers, confidence intervals or enrolment count. Coverage is vendor-heavy, and the full text was blocked.
- No peer-reviewed NHS-Galleri paper had been found as of the searches (results were ASCO 2026, sponsor-reported). There are no mortality data. The NHS decision on national rollout and the FDA PMA status of Galleri as of October 2026 were not found.
- No Delphi-2M AUC figures were retrieved. No prospective deployment of any EHR foundation model with outcome measurement was found.
- AF screening trials (LOOP, STROKESTOP, GUARD-AF) and DANCAVAS were planned as "detection ≠ benefit" examples, but the search budget ran out. From prior knowledge: LOOP found 3× more AF with no significant stroke reduction (Lancet 2021); STROKESTOP showed a small borderline benefit. These need verification and were not cited above.
- The UK "EDITH" AI breast-screening trial (about 700,000 women, announced 2025) was not verified. It is distinct from the EU EDITH digital-twin project.
- Peer-reviewed effect sizes for UW Health's ambient-AI burnout outcomes were not retrieved, and the journal of the multistate stepped-wedge trial was not confirmed.
- No study of outcomes, false-positive rates or follow-up cascades specific to Function Health, Superpower or similar consumer panels was found.
- No oncology digital twin in routine care was found. Unlearn.ai-style "digital twin" control arms in trials (an EMA qualification of a PROCOVA-type method, PK) were not verified.

---

## Key Question 2 — What is the documented gap between prediction and benefit (deployment failures, dataset shift, alert fatigue)?

### Takeaway
The gap between prediction and benefit is well documented and recurs across domains:
- Vendor accuracy claims shrink on external validation.
- Models degrade when case mix shifts.
- Alert volumes swamp clinicians.
- Even accurate positive flags are often not followed up.
- More detection does not reliably translate into fewer late-stage cancers or deaths.
- Risk stratification without an effective intervention can *increase* utilization.
- Clinicians given a strong AI tool often fail to capture its standalone accuracy.

### Cited Findings
- **External-validation shrinkage:** the Epic Sepsis Model had AUC 0.63 at Michigan, against 0.76–0.83 in Epic's internal documentation. Sensitivity was 33% and PPV 12%, so about 8 of 9 alerts were false. — [JAMA Intern Med 2021](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781313); [2 Minute Medicine](https://www.2minutemedicine.com/external-validation-shows-epic-sepsis-model-is-a-poor-predictor-of-sepsis-in-hospitalized-patients)
- **Dataset shift and alert fatigue during COVID-19:**
  - Across 24 hospitals in 4 systems, the share of patients triggering Epic sepsis alerts per day rose from 9% to 21% while census fell 35%.
  - Michigan deactivated the model in April 2020 because of false-positive load.
  — [Healthcare IT News](https://www.healthcareitnews.com/news/epic-generated-sepsis-alerts-increased-during-covid-19-study-shows); [Fierce Healthcare](https://www.fiercehealthcare.com/tech/epic-s-sepsis-algorithm-may-have-caused-alert-fatigue-43-alert-increase-during-pandemic)
- **Dataset shift as a general, documented failure mode:** reviews describe dataset shift (changes in practice, population and IT systems) as a well-documented cause of accuracy decay, with little guidance on prospective validation and monitoring. — [Finlayson et al., NEJM 2021 record](https://hls.harvard.edu/bibliography/the-clinician-and-dataset-shift-in-artificial-intelligence/); [systematic review on temporal shift](https://snorkel.ai/research-paper/systematic-review-of-approaches-to-preserve-machine-learning-performance-in-the-presence-of-temporal-dataset-shift-in-clinical-medicine); [JMIR Med Inform 2025](https://medinform.jmir.org/2025/1/e78309)
- **Follow-through gap after a positive prediction:**
  - In EAGLE, only 49.6% of AI-ECG-positive patients in the intervention arm got an echocardiogram (38.1% in control). — [TCTMD](https://www.tctmd.com/news/ai-ecg-allows-early-diagnosis-low-ef)
  - In ACCESS, only 22% of controls completed a referred eye exam. AI at the point of care raised completion to 100% and follow-through after abnormal results to 64%. — [UW Ophthalmology](https://www.ophth.wisc.edu/blog/2024/01/11/autonomous-artificial-intelligence-increases-screening-and-follow-up-for-diabetic-retinopathy-in-youth-the-access-randomized-control-trial)
- **The response workflow is what carries the benefit:**
  - TREWS' mortality association depends on clinicians *confirming the alert within 3 hours*.
  - Patients whose alerts sat unreviewed may reflect overwhelmed teams, i.e. confounding.
  — [Scientific American](https://www.scientificamerican.com/article/algorithm-that-detects-sepsis-cut-deaths-by-nearly-20-percent/); [Freethink](https://www.freethink.com/health/sepsis-ai)
  - Penda's benefit "required a clinical workflow-aligned implementation and active deployment". — [arXiv 2507.16947](https://arxiv.org/abs/2507.16947v1)
- **Detection is not outcome:**
  - NHS-Galleri quadrupled screen-detected cancers but missed the stage III–IV primary endpoint. — [BioSpace/GRAIL](https://www.biospace.com/press-releases/grail-reports-full-results-from-nhs-galleri-trial-demonstrating-substantial-reduction-in-stage-iv-cancer-diagnoses-at-2026-asco-annual-meeting)
  - General health checks show RR 1.00 for mortality. — [AAFP/Cochrane](https://www.aafp.org/afp/2019/1201/p676)
- **Risk stratification without an effective intervention:**
  - PRISMATIC raised emergency admissions about 1%, ED attendances about 3% and outpatient visits about 5%. — [PMC6820297](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820297/)
  - Camden care management showed no readmission effect (PK). — [NEJM 2020](https://doi.org/10.1056/NEJMsa1906848)
- **CDS clinical-outcome gap:** across 30 trials with clinical endpoints, the median improvement was 0.3% and not significant. — [Kwan BMJ 2020 commentary](https://www.bmj.com/content/370/bmj.m3216)
- **Human–AI integration gap:** in the GPT-4 diagnostic RCT, physicians with GPT-4 scored 76% vs 74% without it, while GPT-4 alone scored 92%. — [Nature Medicine supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04539-8/MediaObjects/41591_2026_4539_MOESM1_ESM.pdf)
- **Evaluation gap for LLMs:** only 19 of 4,609 clinical LLM studies were prospective RCTs, and at least 25% of studies had n<30. — [cancer.fr summary of Chen et al., Nature Medicine 2026](https://www.cancer.fr/professionnels-de-sante/veille/nota-bene-cancer/bulletin-n-677-du-12-mars-2026/llm-assisted-systematic-review-of-large-language-models-in-clinical-medicine)
- **Small incremental value of new predictors:**
  - PRS added about 0.02 to the C-statistic over pooled cohort equations. — [JAMA 2020](https://jamanetwork.com/journals/jama/article-abstract/2761088)
  - With QRISK2, AUROC was 0.635 vs 0.623. — [Brunel](https://bura.brunel.ac.uk/handle/2438/19071?mode=full)
- **Incidental-finding cascades:**
  - Whole-body MRI: 94% have an abnormality, up to 30% get further tests, and 1.1–1.6% have a confirmed cancer. — [CFPC TFP 410](https://cfpclearn.ca/wp-content/uploads/2026/03/TFP-410-English.pdf)
  - Pooled false positives: 16%. — [JMRI meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850647/)
- **Bias learned from training data:** Delphi-2M's explainability analyses surfaced biases from UK Biobank, and accuracy declines over longer horizons. — [Scientific American](https://www.scientificamerican.com/article/new-ai-tool-predicts-which-of-1-000-diseases-someone-may-develop-in-20-years/); [the-decoder](https://the-decoder.com/delphi-2m-predicts-disease-risks-for-over-1000-conditions-using-health-records/)
- **Regulator-mandated evidence generation:** NICE recommended DERM only *conditionally* for 3 years, pending evidence on clinical and cost-effectiveness. — [PharmaTimes](https://pharmatimes.com/news/nice-recommends-first-ai-medical-device-for-skin-cancer-diagnosis-in-the-nhs/)

### Inferences
- **Six recurring failure points between a model and a benefit:**
  1. Local performance below vendor claims (needs local validation).
  2. Drift after case-mix or IT changes (needs monitoring and recalibration).
  3. Alert overload (needs threshold tuning and alert-burden metrics).
  4. No owner of the alert (needs routing, escalation and response-team staffing).
  5. Positive result not followed up (needs a closed-loop tracking and fail-safe process).
  6. Downstream harms such as overdiagnosis, cascades and anxiety (needs follow-up protocols and audit of harms).
- **Implication for the founder:** points 1 to 5 are mostly *software and operations* problems, not model-building problems. They are addressable by an integrator using SQL, APEX, n8n and FHIR, without owning a medical AI model. This is the most defensible inference for the founder's purposes.
- **Evidence implies little stand-alone value for population-risk dashboards:** this matters for Romanian insurers and employers, where software only creates value if attached to a funded, effective intervention such as a DPP-style programme or a screening invitation, plus outcome tracking.

### Gaps
- No quantitative data were found on the prevalence of local AI validation or drift monitoring in European hospitals, or specifically in Romanian ones.
- No primary data were found on alert-override rates for modern AI alerts beyond the Epic sepsis example. The general CDS alert-override literature was not retrieved this session.

---

## Key Question 3 — What is realistically "normal" by 2030, 2035 and 2040 according to credible sources, and what remains speculative?

### Takeaway
Credible institutional sources forecast a shift to digital, preventive and genomics-informed care, with the NHS England 10-Year Plan the most concrete. None of them provide outcome evidence for that shift; they are plans (FC).

Grounded in the evidence above, the realistic picture by period is:
- **By 2030:**
  - AI-supported reading becomes normal in European organised breast screening.
  - Autonomous DR screening becomes normal where it is reimbursed.
  - Ambient scribes become normal in primary care in the UK and US.
  - Interoperable patient summaries and ePrescriptions become normal in the EU under EHDS.
- **2030–2035:** EHR or foundation-model risk flags and integrated PRS+clinical risk scores are likely deployed, though their outcome benefit is still unproven.
- **Speculative even for 2040:** whole-body "virtual human twins", individual 20-year disease forecasting driving care, and consumer full-body screening with proven benefit.

### Cited Findings

#### Institutional forecasts and plans (all FC: forecasts, not observed results)

**NHS England 10-Year Health Plan, "Fit for the Future" (3 July 2025)**
- **Three shifts:** hospital to community, analogue to digital, sickness to prevention. — [Executive summary (gov.uk PDF)](https://assets.publishing.service.gov.uk/media/6888a0996478525675738f3a/fit-for-the-future-10-year-health-plan-for-england-executive-summary.pdf)
- **Digital commitments, per council briefings (secondary summaries):**
  - The NHS App becomes the "front door" by 2028.
  - A single patient record by 2028.
  - National procurement of ambient AI scribing.
  - A "HealthStore" of approved apps.
  — [Havering Council briefing](https://democracy.havering.gov.uk/documents/s79968/NHS%2010%20Year%20Plan%20Briefing.pdf); [WHO Health Systems Monitor](https://eurohealthobservatory.who.int/monitors/health-systems-monitor/updates/hspm/hspm-united-kingdom-2022/ten-year-plan-for-the-english-nhs)
- **Prevention and genomics commitments:**
  - Polygenic risk scores combined with clinical factors into "integrated risk scores".
  - Whole-genome sequencing for risk prediction in CVD, kidney disease and diabetes.
  - A 150,000-adult WGS programme to evaluate preventive use.
  - A genomics population health service including newborns.
  - Easier access to weight-loss drugs.
  — [UK Clinical Pharmacy Association](https://ukclinicalpharmacy.org/clinical/genomics/genomics-at-the-heart-of-englands-nhs-10-year-plan/); [Leicestershire summary slides](https://democracy.leics.gov.uk/documents/s191303/Appendix%20-%2010%20Year%20Plan%20summary%20slides.pdf)
- **Why it matters for grading:** these PRS commitments are policy bets made against modest accuracy evidence (C-statistic +0.02, see KQ1).

**Topol Review (Health Education England, February 2019)**
- Forecast that genomics, AI/digital medicine and robotics would reshape NHS roles, and that within 20 years about 90% of NHS jobs would require digital skills. (PK) — [topol.hee.nhs.uk](https://topol.hee.nhs.uk/)

**WHO**
- *Global Strategy on Digital Health 2020–2025*. (PK) — [WHO](https://www.who.int/publications/i/item/9789240020924)
- WHO guidance on the ethics and governance of large multimodal models for health (2024). (PK) — [WHO](https://www.who.int/publications/i/item/9789240084759)
- Whether and how the strategy was extended beyond 2025 was not verified (see Gaps).

**European Commission**
- **VHT initiative:** a platform and organ-specific prototypes. A whole-body virtual human twin is framed as a long-term ambition, and no platform launch date was found. — [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/virtual-human-twins-launch-european-virtual-human-twins-initiative); [Zenodo VHT roadmap](https://zenodo.org/records/14645647)
- **Cancer screening:** 90% offer-coverage target for breast, cervical and colorectal by 2025, plus lung, prostate and gastric pilots. — [EC IP/22/7548](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_22_7548/IP_22_7548_EN.pdf)
- **European Health Data Space, Regulation (EU) 2025/327** (in force March 2025). Phased application, from prior knowledge:
  - General application from 2027.
  - Patient summaries and ePrescriptions exchangeable by about 2029.
  - Lab results, medical images and discharge reports by about 2031.
  - Secondary-use rules phasing in from about 2029.
  (PK; verify exact dates) — [EUR-Lex 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj)

**OECD *Health at a Glance 2025***
- OECD health spending was about 9.3% of GDP in 2024.
- Spending is expected to keep rising, driven by technology, expectations and ageing.
- Many preventive interventions are highly cost-effective, especially on risk factors such as obesity, smoking and alcohol.
- The OECD digital and AI chapters were not retrieved.
— (SN, secondary summary) [EASO commentary](https://easo.org/a-renewed-focus-on-value-why-prevention-and-obesity-management-must-be-at-the-centre-of-sustainable-health-systems/)

#### Observed-evidence anchors for timeline judgments (not forecasts)
- **AI mammography:** an RCT with interval-cancer reduction (MASAI, Lancet 2026) and nationwide real-world deployment in Germany (PRAIM). — [Lund University](https://www.lunduniversity.lu.se/article/ai-support-breast-cancer-screening-fewer-missed-cancer-cases); [Pharmacy Times](https://pharmacytimes.com/view/ai-improves-breast-cancer-screening-and-detection-rates-in-real-world-study)
- **MCED:** the first RCT missed its primary endpoint. Stage IV reductions emerged only in rounds 2–3, implying any mortality signal needs years more follow-up. — [BioSpace/GRAIL](https://www.biospace.com/press-releases/grail-reports-full-results-from-nhs-galleri-trial-demonstrating-substantial-reduction-in-stage-iv-cancer-diagnoses-at-2026-asco-annual-meeting)
- **Lung-nodule AI:** the authors of the most recent studies (2025–2026) still call for prospective trials. — [Radboudumc 2026](https://www.acc.radboudumc.nl/en/research/news/News-items-by-our-research-institute/2026/AI-estimates-cancer-risk-in-difficult-lung-nodules-better-than-radiologists)
- **Digital twins:** one RCT exists, in a narrow procedural use (AF ablation). — [ESC](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Digital-twin-technology-helps-reduce-the-recurrence-of-atrial-arrhythmias-after-catheter-ablation-for-persistent-atrial-fibrillation)
- **LLM clinical RCTs:** 19 RCTs exist across the whole field to September 2025. — [Chen et al. summary](https://www.cancer.fr/professionnels-de-sante/veille/nota-bene-cancer/bulletin-n-677-du-12-mars-2026/llm-assisted-systematic-review-of-large-language-models-in-clinical-medicine)

### Inferences
Researcher's timeline judgment, synthesized from the evidence above. These are inferences, not sourced forecasts.

| Area | 2026–2030 (likely "normal") | 2030–2035 | 2035–2040 |
|---|---|---|---|
| 1. AI early detection | **Likely [SEE]:** AI-supported reading in many EU and UK breast-screening programmes; autonomous DR screening where reimbursed; AI-ECG in a few US systems; AI skin triage in UK pathways (NICE conditional window). Sepsis/deterioration alerts are widespread but benefit is uneven. | **Plausible [PBU]:** AI as standard reader across imaging screening (breast, lung LDCT programmes as they scale under the EU 2022 recommendation); first long-term outcome data (mortality proxies) for AI screening; risk-adapted screening intervals piloted. | **Speculative [SPEC]:** autonomous reading of most normal screens; screening intervals personalised routinely by AI risk. |
| 2. Longitudinal record prediction | **Likely:** classic scores (QRISK3, SCORE2, CHA2DS2-VASc) embedded in EHR prompts. **[PBU]:** foundation models (Delphi-2M, Foresight) in research and secure data environments only; NHS piloting integrated PRS+clinical scores (FC). | **[PBU]:** vendor-embedded foundation-model risk flags with mandatory local validation; first prospective impact studies. | **[SPEC]:** individual 20-year multi-disease forecasts driving routine prevention. |
| 3. Biomarkers and periodic testing | **Likely:** organised screening expands (lung pilots, colorectal FIT); consumer panels and full-body MRI grow commercially without outcome evidence; MCED available as a paid add-on (US; FDA status unverified); no guideline endorsement of MCED expected before more data. | **[PBU]:** MCED mortality and stage data from long-term NHS-Galleri follow-up may decide policy; consumer panels possibly regulated or integrated into primary care. | **[SPEC]:** proven-benefit, guideline-endorsed blood-based multi-cancer screening at population scale. |
| 4. Personalised interventions | **Likely [SEE]:** digital and AI-coached DPP-style programmes as a reimbursable alternative; GLP-1 era reshapes weight-management programmes (NHS plan, FC). | **[PBU]:** durable (5-year or longer) outcome evidence for digital coaching; personalised nutrition remains niche. | **[SPEC]:** fully personalised multi-omic prevention plans with proven outcome benefit. |
| 5. AI CDS and workflows | **Likely [SEE]:** ambient scribes routine in UK and US primary care (NHS national procurement, FC); LLM "safety-net" copilots in pilots; few RCTs. | **[PBU]:** LLM CDS with RCT evidence for specific tasks, integrated in EHRs; formal monitoring obligations (EU AI Act, MDR). | **[SPEC]:** agentic AI managing chronic-disease panels semi-autonomously. |
| 6. Population health analytics | **Likely:** risk-stratification dashboards standard in NHS and value-based contexts despite weak evidence (PRISMATIC). | **[PBU]:** analytics tied to specific funded interventions with outcome accounting. | **[SPEC]:** population-scale predictive commissioning with proven admission reduction. |
| 7. Digital twins | **[PBU]:** organ-specific twins in narrow procedures (cardiac ablation); EU VHT platform prototypes. | **[PBU→SPEC]:** multi-organ twins in specialist centres; in-silico trial components. | **[SPEC]:** whole-body personal virtual human twin in routine care. |

- **Interoperability timeline:** the EHDS phase-in (patient summaries and ePrescriptions about 2029; labs, images and discharge reports about 2031, PK) is the most concrete infrastructure timeline for Romania and the EU. It means *longitudinal, cross-provider data* that most predictive tools need will realistically become routinely available only in the early 2030s.
- **Most plausible "normal" by 2030:** AI that slots into existing, funded workflows (screening reads, documentation, DR screening at the point of care), not new standalone prediction products.

### Gaps
- No credible quantitative forecasts (for example, % adoption by year) from WHO, OECD or the EC for specific predictive technologies were found. Institutional documents give direction, not adoption curves.
- The OECD *Health at a Glance 2025* and *Health at a Glance: Europe 2024* digital/AI content was not retrieved; the website was blocked, and search returned unreliable secondary pages.
- The exact EHDS application dates and the EU AI Act timing for high-risk medical AI (including any delay proposals in the 2025 "digital omnibus") were not verified this session. A regulation-focused researcher should confirm.
- The WHO strategy's post-2025 status was not verified.
- No credible source gave a specific "2035" or "2040" forecast for digital twins or EHR foundation models. The table's columns for those periods are researcher judgment.

---

## Key Question 4 — What software and data infrastructure is a prerequisite in each area, and where could a solo, non-model-building founder fit?

### Takeaway
Every outcome-positive example depends on *non-AI* infrastructure:
- a screening programme with invitations and reading workflow (mammography);
- point-of-care testing plus referral tracking (DR);
- EHR alert delivery plus a confirmatory test order (EAGLE);
- staffed alert-response teams (TREWS, AAM);
- structured coaching delivery and engagement tracking (DPP).

The documented failure modes (drift, alert fatigue, unfollowed positives, cascades) are mostly data-pipeline, monitoring and workflow problems. That is where a Python/SQL/APEX/n8n founder can add value without owning or validating a medical AI model. The founder must still stay outside MDR "medical device software" scope, or partner with CE-marked vendors.

### Cited Findings
- **Follow-up completion is a measurable, software-addressable gap:** 22% vs 100% exam completion and 22% vs 64% follow-through (ACCESS); 49.6% echo uptake after a positive AI-ECG (EAGLE). — [UW Ophthalmology](https://www.ophth.wisc.edu/blog/2024/01/11/autonomous-artificial-intelligence-increases-screening-and-follow-up-for-diabetic-retinopathy-in-youth-the-access-randomized-control-trial); [TCTMD](https://www.tctmd.com/news/ai-ecg-allows-early-diagnosis-low-ef)
- **Monitoring and drift tooling is needed:** alert rates doubled under COVID case-mix shift, the model was deactivated, and there is little guidance on monitoring and updating. — [Healthcare IT News](https://www.healthcareitnews.com/news/epic-generated-sepsis-alerts-increased-during-covid-19-study-shows); [temporal shift review](https://snorkel.ai/research-paper/systematic-review-of-approaches-to-preserve-machine-learning-performance-in-the-presence-of-temporal-dataset-shift-in-clinical-medicine)
- **Local validation is needed:** vendor AUC was 0.76–0.83 vs 0.63 when externally validated. — [2 Minute Medicine](https://www.2minutemedicine.com/external-validation-shows-epic-sepsis-model-is-a-poor-predictor-of-sepsis-in-hospitalized-patients)
- **Response workflow, audit and timestamps are needed:** TREWS outcomes depend on alert confirmation within 3 hours, and the companion analysis tracked the share of alerts evaluated (about 89%) and the time to evaluation. — [Scientific American](https://www.scientificamerican.com/article/algorithm-that-detects-sepsis-cut-deaths-by-nearly-20-percent/); [Freethink](https://www.freethink.com/health/sepsis-ai)
- **Structured longitudinal data and NLP pipelines are needed:** Foresight needed CogStack to extract free text plus structured data across trusts. — [KCL](https://www.kcl.ac.uk/news/researchers-investigate-ability-of-their-new-ai-tool-to-predict-medical-events)
- **ICD-10 histories with ages at onset are needed:** Delphi-2M inputs are ICD-10 code timelines plus BMI, smoking and alcohol, so it is only as good as longitudinal coding. — [Scientific American](https://www.scientificamerican.com/article/new-ai-tool-predicts-which-of-1-000-diseases-someone-may-develop-in-20-years/)
- **Evidence-generation infrastructure is needed:** NICE's conditional 3-year recommendation for DERM requires ongoing real-world evidence collection. — [PharmaTimes](https://pharmatimes.com/news/nice-recommends-first-ai-medical-device-for-skin-cancer-diagnosis-in-the-nhs/)
- **Engagement tracking is the operating metric for digital prevention:** AI-DPP initiation was 93.4% vs 82.7% and completion 63.9% vs 50.3%. — [Patient Care](https://www.patientcareonline.com/view/ai-powered-diabetes-prevention-program-intervention-matches-human-coaching-daily-dose)
- **Ambient AI requires an evaluation framework:** UW Health published a separate NEJM AI paper on protocols to "design, monitor and evaluate ambient AI within routine care". — [Wisconsin Technology Council](https://wisconsintechnologycouncil.com/uw-health-new-research-shows-ambient-ai-measurably-improves-healthcare-practitioner-well-being)
- **National systems are buying ambient AI and a single patient record:** NHS England plans national procurement of ambient scribing and a single patient record by 2028 (FC). — [Havering briefing](https://democracy.havering.gov.uk/documents/s79968/NHS%2010%20Year%20Plan%20Briefing.pdf)
- **Regulatory boundary (PK):**
  - Under EU MDR Annex VIII Rule 11, software that provides information used for diagnostic or therapeutic decisions is at least Class IIa. — [EU MDR 2017/745](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
  - AI in such devices is "high-risk" under the EU AI Act. — [EU AI Act 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
  - Administrative, scheduling, tracking and data-integration software is generally outside device scope. Verify with regulatory notes.

### Inferences
Researcher synthesis. Areas are ranked by fit for a solo founder with €25k, working 10–12 hours a week, with no clinical data and no own model.

| Area | Prerequisite infrastructure (from evidence) | Founder-feasible, non-device software angles (inference) | Avoid / high barrier |
|---|---|---|---|
| 1. Early detection AI | Screening registries; invitation, recall and reminders; reading-workflow integration (PACS/RIS); result communication; fail-safe tracking of positives to diagnosis; AI performance audit (detection, recall and interval-cancer rates); post-market evidence collection | (a) Screening and follow-up "closed-loop" tracker for clinics, labs and private networks (APEX + n8n reminders, SMS/e-mail, escalation lists). (b) AI-deployment audit dashboard: local KPIs (recall, PPV, interval cancers) for hospitals buying CE-marked AI. (c) Integration glue (DICOM/HL7/FHIR metadata, not pixels) | Building or validating detection models (Class IIa–III MDR, RCT-level evidence now expected) |
| 2. Longitudinal prediction | Clean, coded longitudinal records (ICD-10, labs, meds); terminology mapping; patient-level linkage; secure data environment; calibration and drift monitoring | (a) Data-quality and coding-completeness tooling for clinics and labs (prerequisite for any risk score). (b) Calculating *already-validated* published scores (QRISK3, SCORE2, FINDRISC) inside workflows. This still likely counts as device software if used for clinical decisions, so check the MDR route or embed via a certified partner. (c) Model-monitoring service (calibration, drift, subgroup performance) for third-party models | Training or selling own foundation model or PRS products (no outcome evidence; heavy data access and regulation) |
| 3. Biomarkers and testing | Lab result interoperability (EHDS labs about 2031, PK); reference ranges; abnormal-result follow-up workflows; incidental-finding management; harm audit | (a) Abnormal-result follow-up and navigation workflow for private labs and clinics (who must act, by when, was it done). (b) Patient-facing *explanation* of results limited to lab reference ranges and guideline screening schedules, with clinician sign-off (keep outside diagnosis). (c) Screening-eligibility reminders based on EU 2022 / national guidelines | Selling broad "longevity" panels or MRI interpretation as medical value (no outcome evidence; reputational and regulatory risk) |
| 4. Personalised interventions | Program delivery platform; engagement analytics; outcome capture (weight, HbA1c); coaching CRM; durability follow-up | (a) Operations platform for DPP-style or corporate prevention programmes (enrolment, attendance, weight logs, outcome reporting to payers and employers). (b) LLM-assisted coaching *messages* under human supervision (wellness, not diagnosis) | Claims of disease prevention without trial evidence; personalised-nutrition algorithms |
| 5. CDS and workflows | EHR integration (CDS Hooks/FHIR); alert routing; threshold tuning; alert-burden metrics; scribe-to-EHR note pipelines; evaluation framework (time-in-note, error audits) | (a) Integrating and localising (Romanian language) ambient documentation using LLM APIs for private clinics, with documentation-only scope. (b) Alert-burden and override analytics for hospitals. (c) Evaluation harness for LLM tools (sampling notes, error tagging, clinician review queues) | LLM diagnostic or treatment recommendations to clinicians (device + AI Act high-risk; RCT evidence scarce) |
| 6. Population health | Population registers; risk lists; *intervention capacity*; outcome accounting (admissions, costs) | Analytics only when tied to an action list and outcome tracking (e.g. invite-to-screening, DPP enrolment, vaccination recall) for insurers, employers and municipalities | Selling risk-stratification dashboards as admission-reducing (PRISMATIC evidence is against) |
| 7. Digital twins | Imaging-derived patient-specific models; HPC simulation; validation; VHT platform standards | Practically none for a solo founder in 2026–2030, beyond data-management tooling for research consortia | Building twins (research-grade, capital-intensive) |

- **Cross-cutting prerequisite stack** that nearly every area needs and that matches the founder's skills:
  - Data ingestion and terminology mapping (ICD-10, LOINC, FHIR).
  - Longitudinal patient timeline.
  - Worklists and task assignment.
  - Reminders and escalation (n8n).
  - Audit logs with timestamps.
  - KPI dashboards (APEX).
  - Drift and calibration monitoring for third-party models.
  - Evidence and outcome registries.
- **Key insight from the evidence:** the "last mile" of acting on a prediction, following it up and measuring the outcome is where benefits are won or lost, and it is under-tooled.
- **Timing:** demand for that infrastructure probably rises before 2030 in the EU, driven by EHDS interoperability phasing (PK), EU AI Act and MDR post-market monitoring duties (PK), and screening-programme expansion under the 2022 Council Recommendation (sourced). Benefits from predictive models themselves stay uneven.
- **Commercial vs technical feasibility:** technically, all the "founder-feasible" angles are buildable with the founder's stack. Commercially, Romanian public procurement cycles and hospital IT budgets are likely slow. Private lab and clinic networks and occupational-health or insurer programmes are probably more reachable. These are not evidenced here and should be checked against the market and Romania research notes.

### Gaps
- No Romanian data were collected in this research thread on any of: screening participation, the abnormal-result follow-up gap, EHR coding quality, or EHDS readiness. These are needed to size the "closed-loop follow-up" opportunity locally.
- No primary source was retrieved on the exact MDR classification boundary for result-tracking, screening-reminder or scribe software (MDCG 2019-11 guidance was not fetched). A regulation-focused researcher should confirm which angles stay outside device scope.
- No evidence was found on the willingness of European hospitals to pay for third-party AI monitoring or audit tools, or on existing competitors in that niche.
- No cost-effectiveness data were retrieved for any of the AI interventions above, apart from NICE's statement that DERM's cost-effectiveness still needs confirming.
