# Administrative prevention workflows (test-result follow-up, screening recall, no-show reduction): evidence base, European price benchmarks and regulatory date checks (as of 9 Oct 2026)

How to read this:
- **Labels:** [EST] = Established evidence; [SEE] = Strong emerging evidence; [PBU] = Plausible but unproven; [SPEC] = Speculative.
- **Source access:** WebFetch was blocked by the egress proxy (403) for eur-lex.europa.eu, eumonitor.eu, streamlex.eu and the UK G-Cloud asset server. Every figure below therefore comes from **web-search result snippets** unless marked (BK). Snippets summarise their source and can mis-map a URL; where the mapping is uncertain, the entry says so.
- **(BK)** = from background knowledge, not re-verified this session.
- **Pre-2015 studies** are marked **[foundational, pre-2015]**.
- **Scope:** I checked the sibling notes first and avoided repeating them:
  - `emergente_si_platitori.md` §L already covers no-show ML studies and Romanian reminder vendors.
  - `competitori_b2b_infrastructura.md` already covers Doctolib ARR and pricing and the Accurx Humber contract.
  - `reglementare_ue_ro.md` §§3, 4, 7 already covers AI Act, EHDS and PLD dates.
  - This file adds: the follow-up / screening evidence base (not covered elsewhere), intervention effect sizes, SMS and targeting meta-analyses, new price points, and independent re-verification of the regulatory dates.

---

## 1. How big and how well documented is missed follow-up of abnormal results and overdue screening?

### Takeaway
Missed or delayed follow-up of abnormal results is one of the best-documented failure modes in ambulatory care. Studies have documented it for 15+ years, in many settings, and EHR alerts alone do not fix it:
- **Lab results:** non-follow-up ranges from **7–62%** across studies.
- **Imaging results:** **1–36%**.
- **Diagnostic follow-up after a positive screening test:** 10–35% of people never get it, even inside organised European programmes. Losses after HPV-positive results are larger still.

Malpractice data show that follow-up and communication failures contribute to a material share of ambulatory diagnostic claims. The size and existence of the problem is **[EST]**. What is weak is precise, current European prevalence data. Romanian data are absent.

### Cited Findings

**Lab and imaging results not followed up (ambulatory)**
- **Callen, Westbrook, Georgiou et al.**, "Failure to follow-up test results for ambulatory patients: a systematic review", *J Gen Intern Med* vol. 27(10):1334–48, doi:10.1007/s11606-011-1949-5. **[EST; foundational, pre-2015 literature 1995–2010]** — [Springer](https://link.springer.com/doi/10.1007/s11606-011-1949-5); [AHRQ PSNet](https://psnet.ahrq.gov/issue/failure-follow-test-results-ambulatory-patients-systematic-review)
  - **19 studies** met inclusion out of 768 screened.
  - Non-follow-up ranged from **6.8% (79/1,163) to 62% (125/202)** for laboratory tests and **1.0% (4/395) to 35.7% (45/126)** for radiology.
  - Studies linked the failures to harm, including **missed cancer diagnoses**.
  - EHRs improved follow-up, "although a substantial proportion of abnormal results were not followed up even with EHRs".
  - Processes varied widely across sites and causes were multifactorial.
  - Caveat: press coverage that says "up to two-thirds" overstates the 62% maximum.
- Same evidence base: a later analysis noted that across the hospital and ambulatory reviews, **only 31 studies over 20 years** existed, and evidence on interventions was "particularly lacking". **[SEE]** (snippet; the exact paper behind this quote is not confirmed and may be [PMC4975222](https://pmc.ncbi.nlm.nih.gov/articles/PMC4975222/))
- **Singh et al., *Arch Intern Med* 2009, VA Houston** (outpatient imaging alerts, Nov 2007–Jun 2008). **[EST; foundational, pre-2015]** — [ScienceDaily](https://www.sciencedaily.com/releases/2009/09/090928172349.htm); [HospiMedica](https://www.hospimedica.com/medical-imaging/articles/294726055/electronic-alerts-on-abnormal-imaging-test-results-do-not-always-result-in-timely-follow-up.html)
  - Of **123,638 imaging tests**, **1,196 (0.97%)** generated alerts.
  - **217 alerts (18.1%) were never acknowledged.**
  - **92 alerts (7.7%) lacked timely follow-up at 4 weeks**: 7.3% of acknowledged alerts vs 9.7% of unacknowledged ones. In other words, reading the alert did not protect the patient.
  - **26 of the 92 were new diagnoses, 11 of them cancers.**
  - The authors recommended explicit responsibility rules and requiring a signed action before an alert can drop off the screen.
- **Murphy, Singh et al. cluster RCT** (*J Clin Oncol*, about 2015–16; 72 primary care physicians at 2 VA sites, Apr 2011–Jul 2012). **[EST for the baseline gap in a VA setting]** — [ecancer](https://ecancer.org/en/news/7664-electronic-trigger-reduces-delays-in-evaluation-for-cancer-diagnosis); [AHRQ digital](https://digital.ahrq.gov/ahrq-funded-projects/using-electronic-data-improve-care-patients-known-or-suspected-cancer)
  - E-triggers flagged **1,256 of 10,673 patients with red-flag findings (11.8%)** as having no timely diagnostic evaluation.
  - "Timely" meant 30 days for lung, 60 days for colorectal and 90 days for prostate.
  - Results of the intervention are in §2.

**Incidental imaging findings**
- An ACR case summary cites a study with a **71% failure rate** in follow-up of incidental pulmonary nodules. **[SEE]** (snippet; primary study not identified) — [ACR, Tracking Actionable Incidental Findings](https://acr.org/Practice-Management-Quality-Informatics/Imaging-3/Case-Studies/Quality-and-Safety/Tracking-Actionable-Incidental-Findings)
- Applied Radiology reports that **about 30% of radiology follow-up recommendations** lack confirmation of completion. **[PBU]** (secondary citation, not verified) — [Applied Radiology](https://appliedradiology.com/Articles/managing-incidental-findings)

**Abnormal screening results: positive FIT to colonoscopy in Europe**
- **Italy, national survey:**
  - Mean attendance at total colonoscopy after a positive FIT was **81.2%**; two regions (Molise, Campania) were **below 70%**.
  - Colonoscopy completion once attended was **91%**.
  - The 2010 survey gave **81.4%** attendance and **88.7%** completion.
  - **[EST]** (snippet) — [IRIS Univr](https://iris.univr.it/handle/11562/1128754); [QxMD 2010 survey](https://read.qxmd.com/read/23293271/-screening-for-colorectal-cancer-in-italy-2010-survey)
- **Paris, first 18 months of the national FIT programme:** only **70.5% (2,706/3,839)** of FIT-positive people had a colonoscopy with an available report. **[EST]** (snippet) — [PMC5841338](https://pmc.ncbi.nlm.nih.gov/articles/PMC5841338/)
- **Multi-country comparison** (France, Flanders, Netherlands, Basque Country): **compliance with colonoscopy referral was 64–92%** and completion 92–99%. The authors stress continuous monitoring. **[EST]** (snippet; probable URL) — [Gut 2022;71(3):561](https://gut.bmj.com/content/71/3/561)
- **Veneto (Italy)**, which phones FIT-positive people and offers free colonoscopy, keeps adherence at about **80% at 3 months**. A meta-analysis gives about **80% compliance** in real-world FIT programmes, with some programmes **as low as 50%**. **[SEE]** (snippet; URLs not individually mapped) — [PMC8862019](https://pmc.ncbi.nlm.nih.gov/articles/PMC8862019); [PMC7222964](https://pmc.ncbi.nlm.nih.gov/articles/PMC7222964)

**Abnormal cervical screening (HPV or cytology)**
- **Estonia, national cohort** (44,282 women aged 30–65, follow-up 2021–2024):
  - **57.7% of hrHPV-positive women** had no repeat HPV test, colposcopy or post-colposcopy care within 12 months.
  - Among women referred, **77.9%** had colposcopy within 6 months.
  - **[SEE]** (snippet; journal and year not confirmed) — [Synapse Social record](https://www.synapsesocial.com/papers/69db375f4fe01fead37c558c)
- **Netherlands (Loopik 2020, via a review table):**
  - **8.1%** had no initial follow-up after an abnormal result.
  - Further loss after colposcopy referral was **26%** for clinician-taken samples vs **55.5%** for self-samples.
  - **[PBU]** (secondary table; verify against the original) — [PMC10337158 table](https://pmc.ncbi.nlm.nih.gov/articles/PMC10337158/table/Tab2)
- **Germany (MARZY cohort; Liang et al., *BMC Women's Health* 2022):** a population-based prospective study of colposcopy non-attendance after positive co-testing. It states that "a considerable proportion of cervical cancer diagnoses in high-income countries are due to lack of timely follow-up of an abnormal screening result". The headline rate was not in the snippet. **[SEE]** — [PMC9270801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9270801/)

**Malpractice and safety data (US, CRICO/Harvard)**
- **2016 dataset:** CRICO **N=175** ambulatory diagnosis-failure claims, made 1 Jan 2011–31 Aug 2016. The comparative benchmarking system (CBS) baseline was **2,919** cases. Contributing factors:
  - physician follow-up with the patient: **21%** of cases (CBS 18%);
  - patient compliance with the follow-up plan: **14%** (CBS 17%);
  - receipt or transmittal of test results to the provider: **4%** (CBS 5%).
  - These are factor shares; one claim can list several.
  - **[EST]** (snippet; slide deck URL mapping likely) — [CRICO 2016 slides](https://rmf.harvard.edu/-/media/Files/CRICO/PDFs/SaferCare/Presentations/CRICO_AYS_Bundle_slides_2016.pdf)
- **2007–2011 dataset:** 1,998 outpatient diagnosis-related cases. Contributing factors:
  - follow-up: **12%**;
  - receipt or transmittal of results: **9%**;
  - patient compliance: **14%**;
  - ordering of tests: **50%**, the largest factor.
  - **[EST]** (snippet) — [CRICO 2012 ambulatory](https://www.rmf.harvard.edu/-/media/Files/CRICO/HighGearPresentations/2012-HG_ambulatory.pdf)
- CRICO's 2014 benchmarking covered **more than 23,000** malpractice cases, and **57%** arose in ambulatory settings excluding the ED. **[EST]** — [CRICO DX Benchmarking Report](https://rmfcd1-prod.rmf.harvard.edu/Podcasts/2015/DX-Benchmarking-Report)

### Inferences
- **[EST]** The problem is real, recurrent and cross-system. Even with an EHR, organised screening and alerts, roughly **1 in 5 to 1 in 3 FIT-positive people in some European programmes** do not reach colonoscopy within the programme's window. Losses after HPV-positive results can be larger. The binding failure is **ownership and tracking**, not detection.
- **[PBU]** In Romania, organised screening is minimal (6.2% cervical coverage; see `emergente_si_platitori.md` §C) and abnormal results are delivered by e-mail or WhatsApp (see `romania_piata.md`). The follow-up gap is therefore likely **at least as large** as the European figures, but **no Romanian measurement exists**. A founder would need to measure it in a pilot clinic, for example the share of abnormal HbA1c, PSA, FIT or Pap results with no documented action at 30, 60 or 90 days.
- **[PBU]** The CRICO factor shares suggest that follow-up and communication failures are minority but persistent contributors to diagnostic claims (about 4–21% depending on the factor). Under the new PLD, a vendor whose tracking tool fails could share exposure (§5).

### Gaps
- No pooled post-2015 estimate of abnormal lab-result non-follow-up was found. The Callen ranges are pre-2015. Post-2015 primary-care studies (for example Singh-group work after 2020) were not retrieved.
- No European or UK malpractice data on test-result management were found. NHS Resolution figures were not searched because of the search budget.
- No Romanian data on abnormal-result follow-up, colposcopy attendance or FIT-to-colonoscopy completion. Romania has no national FIT programme to measure.
- The Estonian and Dutch HPV figures come from snippets or secondary tables; the primary papers were not opened.

---

## 2. Which interventions (software and workflow) have evidence that they close the loop, and how big are the effects?

### Takeaway
Three kinds of intervention have evidence:
- **Organised invitations** for screening uptake: invitation letters raise uptake by about 1.7× vs none **[EST]**.
- **Outreach** for screening uptake: mailed FIT and navigation each add about **+20 percentage points** **[EST, US]**.
- **For abnormal results:** **patient navigation** (RR about 1.27) and **clinician-facing e-triggers or tracking with active outreach** (73% vs 52% evaluated) **[SEE]**.

Passive EHR alerts on their own are insufficient **[EST]**. Effects are strongest when tracking is paired with a human who acts (a navigator or coordinator, or a phone call), which is the "closed-loop" design.

### Cited Findings

**E-triggers and tracking for abnormal results**
- **Murphy/Singh cluster RCT** (*J Clin Oncol*, about 2015–16). Clinicians were notified of patients flagged by e-triggers, by e-mail and then phone. **[EST, single RCT, VA]** — [ecancer](https://ecancer.org/en/news/7664-electronic-trigger-reduces-delays-in-evaluation-for-cancer-diagnosis); [HCInnovation](https://www.hcinnovationgroup.com/clinical-it/news/13025625/research-electronic-triggers-reduce-delays-in-cancer-diagnosis-evaluations)
  - **73.4% vs 52.2%** received a diagnostic evaluation by final review.
  - **Colorectal:** median time to evaluation **104 vs 200 days** (n=557).
  - **Prostate:** 40% evaluated at 144 vs 192 days (n=157).
  - **Lung:** not significant (65 vs 93 days, only 19 patients).
- **Related trigger work:**
  - Positive predictive value was **57.3%** for a lung-imaging trigger and **60.1%** for a TSH trigger.
  - In a 2016 follow-up, **e-mail prompted only about 11%** of providers to act, while **more than two-thirds acted after a phone call**. This shows the human touch matters.
  - **[SEE]** (snippet) — [PMC4613876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4613876); [AHRQ PSNet](https://psnet.ahrq.gov/issue/communicating-findings-delayed-diagnostic-evaluation-primary-care-providers)

**Radiology closed-loop tracking**
- **RADAR (Brigham and Women's, *AJR*; retrospective):** a closed-loop system for incidental pulmonary nodules. **[SEE]** — [PubMed 30779667](https://www.pubmed.ncbi.nlm.nih.gov/30779667/); [Radiology Business](https://radiologybusiness.com/topics/care-delivery/healthcare-quality/follow-recommendations-pulmonary-nodules-arrs)
  - Radiologist and PCP agree a shared follow-up plan, and completion is tracked.
  - Voluntary adoption was **58%** overall, rising from **40% to 70%**.
  - All PCPs agreed with the recommendations.
  - It improved the *quality of recommendations*; patient completion figures were not in the snippet.
- **Secondary reports, not verified:**
  - a nodule tracking system cut missed follow-up from **74% to 10%**;
  - actionable-incidental-finding tracking raised completion from **43% to 71%** at one institution.
  - **[PBU]** — [Applied Radiology](https://appliedradiology.com/Articles/managing-incidental-findings)

**Navigation and reminders after a positive FIT or faecal blood test**
- **Selby et al., *Annals of Internal Medicine* 2017** (23 studies: 7 randomised, 16 non-randomised). **[SEE]** — [ACP Gastroenterology](https://gastroenterology.acponline.org/archives/2017/10/27/2.htm); [CancerNetwork](https://cancernetwork.com/view/navigators-reminders-may-improve-follow-after-positive-fecal-blood-test)
  - Moderate evidence supports **patient navigators** and **provider reminders or performance feedback**.
  - Evidence for system-level interventions is low.
  - Low-cost options: **EHR clinician reminders** and **notifying the endoscopist directly** of positive tests.
  - An economic evaluation cited by the review puts navigation for abnormal screening follow-up at **about $275 extra per patient** (95% CI $260–290).
- **2026 systematic review and meta-analysis, *J Gen Intern Med*** (health-disparity populations; 10 studies: 8 navigation, 1 registry-based QI collaborative, 1 low-touch result notification). **[SEE]** (abstract-level snippet; URL mapping uncertain) — [McMaster PLUS](https://plus.mcmaster.ca/kt/Home/Article/390649)
  - Navigation raised colonoscopy completion: **RR 1.27 (95% CI 1.10–1.46), moderate certainty**.
  - Effects did not differ between randomised and non-randomised designs.
- **Contradicting estimate:** a US meta-analysis found navigation **not significantly** associated with colonoscopy completion after an abnormal initial test: **RR 1.21 (0.92–1.60)**, risk difference 14% (0–29%). **[SEE that effects vary by setting]** (snippet; source paper not individually mapped) — [Springer DDS 2021](https://link.springer.com/doi/10.1007/s10620-021-06866-x)
- **One US academic system** reached only **31.1%** diagnostic colonoscopy completion after a positive FIT even after navigation was introduced, because barriers operate at several levels. **[SEE]** (snippet; URL mapping uncertain) — [PMC6583619](https://pmc.ncbi.nlm.nih.gov/articles/PMC6583619)

**Screening uptake (recall and invitation)**
- **Dougherty et al., *JAMA Intern Med* 2018** (doi:10.1001/jamainternmed.2018.4637; 73 US RCTs, n=366,766). **[EST, US settings]** — [MDedge / The Hospitalist](https://community.the-hospitalist.org/content/blood-test-outreach-navigation-could-close-colorectal-cancer-screening-gap)
  - **Mailed faecal-test outreach** and **patient navigation** each raised colorectal screening completion by **about 20 percentage points**.
  - Patient reminders, patient education and clinician reminders also helped.
  - **Combinations beat single components.**
  - Effects may be smaller in disadvantaged, low-uptake groups.
- **Cochrane review on cervical screening uptake** (Everett 2011, updated Staley 2021, CD002834.pub3). **[EST]** (snippet; Cochrane PDF not opened) — [Cochrane abstract](https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD002834.pub3/pdf/CDSR/CD002834/CD002834_abstract.pdf); [Stirling repository](https://www.storre.stir.ac.uk/bitstream/1893/10620/1/Everett%20et%20al_Cochrane_2011.pdf); [AAFP summary](https://www.aafp.org/afp/2012/0301/p443)
  - **Invitation letters:** RR **1.71 (1.49–1.96; 24 trials, n=141,391)**. Personalised invitations and letters with a **fixed appointment time** worked better than standard invitations.
  - **Educational materials:** RR 1.35 (1.18–1.54; 13 trials).
  - Automated telephone systems with added functions slightly increased uptake (moderate certainty).
  - Caveat: these pooled figures may come from the 2011 version rather than the 2021 update.
- **Veneto:** active phone follow-up of FIT-positive people kept colonoscopy adherence at about 80% (§1). This is a programme-level, non-randomised data point. **[SEE]**

### Inferences
- **[SEE]** The evidence-supported product shape is **"registry + worklist + human action"**:
  1. detect results or overdue recalls from data;
  2. assign an owner;
  3. contact the patient or clinician by an escalating channel (SMS, then phone);
  4. log closure.

  Passive alerts or one-shot e-mails are the weakest designs (Singh 2009; e-mail about 11% vs phone more than two-thirds).
- **[PBU]** For a Romanian private clinic, the relevant effect sizes are:
  - about +20 percentage points for active screening outreach;
  - RR about 1.27 for navigation after an abnormal result;
  - about 1.7× for invitation letters vs no invitation.

  These come mostly from US or organised-programme settings. Transfer to fee-for-service Romanian clinics, where the patient pays and recall is commercial, is unproven.
- **[PBU]** Navigation costs about $275 per patient in US data. Software that automates the tracking and triage part of navigation, leaving humans to make the calls, is the obvious cost lever. No study was found that isolates the software-only component.

### Gaps
- No European RCT of software-only result-tracking (without navigators) was found.
- No cost-effectiveness study of closed-loop result management in European primary care was found.
- The Cochrane review on interventions to increase uptake of organised colorectal screening (European invitation designs, GP-endorsed letters, advance notification) was not retrieved.
- UK data on cervical-screening fail-safe and recall failures were not retrieved.

---

## 3. No-show and reminder evidence: how much do SMS reminders help, and does predictive targeting beat reminding everyone?

### Takeaway
- **SMS reminders raise attendance modestly but reliably.** Pooled risk ratios are **1.06–1.23** vs no reminder; Robotham 2016 found attendance of **67% vs 54%**. SMS performs about the same as phone calls at **55–65% of the cost per attended appointment** **[EST]**.
- **Predictive targeting** (calling patients at high predicted risk) reduces no-shows within the high-risk group by about **3–6 percentage points** in RCTs **[SEE]**.
- **No trial was found showing that targeting beats universal reminders.** The JAMIA 2022 review explicitly lists this as an open question **[PBU]**.
- **The cost of no-shows is large and well documented in the NHS:** 5% of GP sessions are missed, costing about £216M a year (2019 figure), and the 2021/22 outpatient DNA rate was 7.6% **[EST]**.

### Cited Findings

**Meta-analyses of SMS reminders**
- **Cochrane review, mobile-phone messaging reminders** (Gurol-Urganci et al., 2013, CD007458.pub2). **[EST; foundational, pre-2015]** — [Cochrane](https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007458.pub2); [AAFP summary 2013](https://www.aafp.org/pubs/afp/issues/2013/0701/p20.pdf); [SUPPORT summary](https://supportsummaries.epistemonikos.org/support-summaries/show/does-the-use-of-mobile-phone-messaging-reminders-increase-attendance-at-healthcare-appointmentsa)
  - Text reminders vs none: attendance **RR 1.10 (1.03–1.17)**, from 4 RCTs with 3,547 participants; low-to-moderate quality.
  - SMS and phone reminders had similar effects.
  - The SMS cost per attended appointment was **55–65%** of the phone-call cost.
- **Free et al., *PLoS Medicine* 2013** (mHealth review). **[EST; foundational, pre-2015]** — [DOAJ / PLoS Med](https://doaj.org/article/ec8bd443e42040e79ee9b9beb32785bd); [LSHTM](https://researchonline.lshtm.ac.uk/id/eprint/639123)
  - SMS vs no reminder: **RR 1.06 (1.05–1.07), I²=6%**.
  - SMS vs other reminder types: RR 0.98 (0.94–1.02).
  - No effect on cancellations: RR 1.08 (0.89–1.30).
  - No trial had low risk of bias.
- **Robotham et al., *BMJ Open* 2016**, "Using digital notifications to improve attendance in clinic" (searches to April 2015; 26 articles, 21 in the meta-analysis; 8,345 notified vs 7,731 not notified). **[EST]** (snippet; lead author recalled from BK and consistent with the title) — [PubMed 27798006](https://pubmed.ncbi.nlm.nih.gov/27798006/)
  - Attendance **RR 1.23 (67% vs 54%)**.
- An overview of 7 reviews (CES Medicina 2018) found attendance RRs of about **1.09** in both the 24–40 and 50–63 age groups, with no difference by age. **[SEE]** — [Redalyc](https://www.redalyc.org/journal/2611/261157133003/html)
- A sibling note (`monitorizare_date_coordonare.md`) cites RR about 1.14, rated low certainty. That is consistent with the range above.

**Predictive targeting**
- **Shah et al. 2016, RCT** (Massachusetts General Hospital primary care; 2,247 patients with predicted no-show risk >15%). **[SEE, single RCT]** — [PMC5130951](https://pmc.ncbi.nlm.nih.gov/articles/PMC5130951); [BIDMC listing](https://research.bidmc.org/alexa-kimball/publications/targeted-reminder-phone-calls-patients-high-risk-no-show-primary-care-appointment)
  - A coordinator phone call 7 days ahead, on top of the usual automated call, gave **22.8% vs 29.2%** no-shows (−6.4 percentage points).
  - The comparison is within high-risk patients only, not against universal calls.
- **Oikonomidi et al., *JAMIA* 2022, systematic review** (doi:10.1093/jamia/ocac242). **[SEE]** (snippet) — [Crossref](https://api.crossref.org/works/10.1093%2FJAMIA%2FOCAC242); [Glasgow eprints](https://eprints.gla.ac.uk/287844/1/287844.pdf); [Manchester](https://research.manchester.ac.uk/en/publications/predictive-model-based-interventions-to-reduce-outpatient-no-show/)
  - Predictive-model-based **SMS** reminders reduce no-shows: **high-certainty evidence, but from one RCT**.
  - Predictive-model-based **phone** reminders: **moderate certainty, 3 RCTs**.
  - The authors state further research is needed on **targeted vs non-targeted** interventions.
  - This confirms the URL mapping that `emergente_si_platitori.md` §L marked as unconfirmed.
- **Kaiser Permanente Washington, randomised QI:** among high-risk patients, **two texts vs one** cut no-shows by **7%** in primary care and **11%** in mental health. This tests reminder *intensity* for high-risk patients, not targeting vs universal reminders. **[SEE]** (snippet; URL mapping uncertain) — [PMC9933067](https://pmc.ncbi.nlm.nih.gov/articles/PMC9933067)
- Already in the sibling note: a safety-net RCT found **33% vs 36%** no-shows ([PMC10150669](https://pmc.ncbi.nlm.nih.gov/articles/PMC10150669)), and an MRI pre/post study found 19.3% → 15.9%.

**Cost of no-shows (NHS England)**
- **GP practices (January 2019 estimate):**
  - about **307M** practice sessions a year, of which **5% (≈15.4M)** were missed without notice;
  - about **7.2M** of the missed sessions were with GPs, at about **£30 each, ≈ £216M a year**.
  - The £216M is GP-only and is a dated estimate.
  - **[EST]** — [PharmaTimes](https://pharmatimes.com/news/1_in_20_gp_appointments_missed_costing_216m_1273651/); [MDDUS](https://www.mddus.com/resources/resource-library/news-digest/2019/january/missed-gp-appointments-cost-216m-per-year)
- **Hospital outpatients 2021/22:** **103M** appointments booked, **7.6% DNA**, about **650,000 slots a month**. **[EST]** — [NHS England, Reducing DNAs](https://www.england.nhs.uk/long-read/reducing-did-not-attends-dnas-in-outpatient-services/)
- **Northern Ireland outpatients 2024/25:** **7.8%** DNA. **[EST]** — [NISRA](https://datavis.nisra.gov.uk/health/ni-outpatient-stats-24-25.html)

### Inferences
- **[EST]** A plain SMS reminder is commodity, evidence-backed functionality. Effects are modest: about +6–23% relative attendance, or a few percentage points absolute when baseline no-shows are 5–10%. Every PMS (practice-management system) and booking platform already bundles it (§4), so it cannot be a differentiated product by itself.
- **[PBU]** The defensible "predictive" layer is narrow: spending **expensive** channels (a human call, a double reminder, overbooking) only on high-risk slots. The evidence supports a gain of a few percentage points over automated calls alone in high-risk patients. It does **not** yet show that targeting beats universal cheap reminders. Pitch it as cost allocation of staff time, not as superior clinical efficacy.
- **[PBU]** For prevention specifically, the bigger value is likely **recall of patients who never booked** (overdue screening or chronic-care checks; §2: about +20 percentage points with outreach) rather than reducing no-shows for already-booked visits.

### Gaps
- No post-2020 Cochrane update or large meta-analysis of SMS reminders was retrieved. WhatsApp and RCS reminder evidence was not searched.
- No European (non-UK) national no-show rates were found. Romanian no-show rates are unknown; the sibling note cites only vendor claims.
- No RCT randomising **all** patients to targeted vs universal reminders was found.

---

## 4. What do European vendors charge for reminder, recall and follow-up tools?

### Takeaway
Reminders and recall are **almost never sold standalone** in Europe. They are bundled into:
- booking or practice platforms priced **per practitioner per month**: Doctolib about **€139**; Jameda about **€99–199**; Doctoralia from about **€69**;
- dental practice-management systems priced **per surgery**: Dentally about **£125–320/month** for one surgery;
- UK GP messaging toolkits priced **per registered patient per year**: Accurx about **£0.20–0.97**.

SMS is often **billed separately** at about **€0.05–0.10 per message**. For Romania, the only firm local reference is MediNote at **50 lei/user/month** (sibling note). International API SMS to Romania costs about **$0.06–0.074 per message**. No local Romanian aggregator rate card was found.

### Cited Findings

**Accurx (UK, NHS GP), G-Cloud 14 pricing documents, 2026**
- Licences are priced **per registered patient per year**, excluding VAT, with **SMS charged separately**. **[SEE]** (snippet of the PDF; the PDF itself was blocked) — [G-Cloud 14 pricing doc, Aug 2026](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/708675/281422867192066-pricing-document-2026-08-10-1029.pdf); [Feb 2026 version](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/708675/281422867192066-pricing-document-2026-02-16-0938.pdf); [Accurx support (quotes)](https://support.accurx.com/en/articles/768406)
- **July 2026 toolkit prices** (flagged as a short-window "flash sale"):

  | Toolkit | Tier 1 (1–14,999 patients) | Tier 4 (800,000+ patients) |
  |---|---|---|
  | Bronze | £0.43 | £0.20 |
  | Silver | £0.75 | £0.44 |
  | Gold | £0.97 | £0.65 |

- The Feb 2026 sheet had Bronze Tier 4 at **£0.24**.
- The sheet's own example: a 900,000-patient population on Gold costs **£585,000 a year** before VAT and SMS.
- A standalone **two-way patient messaging** module was **£0.23 per patient** at Tier 4.
- "Batch messaging and appointment reminders" is a named feature, but its tier placement was unclear.
- **My arithmetic, not a quote:** an 8,000-patient practice would pay about **£3,440 a year on Bronze** and about **£7,760 a year on Gold** (≈ £290–650/month) before VAT and SMS.
- The sibling note records the regional contract: **£1.41M** for Humber & North Yorkshire (Apr 2025–Mar 2026).

**Dentally (UK dental cloud PMS, includes recall)**
- **September 2026** (review site reading the vendor page; affiliate site): **[SEE]** — [Whito](https://whito.co.uk/dentists/tools/best-software-for-uk-dental-practices/); vendor page [dentally.com (IE)](https://dentally.com/en-ie/pricing)
  - **Starter £125, Essentials £220, Pro £320 per month** for one surgery, excluding VAT.
  - Prices scale with surgeries up to **£575 / £720 / £945** for 8 surgeries; unlimited users; 9+ surgeries on request.
  - Setup fees and minimum terms are not published.
- **Older or conflicting figures:** **[PBU]** — [TrustRadius](https://www.trustradius.com/products/dentally/pricing); [ToolRadar](https://toolradar.com/tools/dentally/pricing)
  - TrustRadius: £50 / £84 / £108 per surgery per month (older structure).
  - ToolRadar: Starter £195, Pro £415.
  - Ireland: Basic at **€50 per surgery per month**.
- **Software of Excellence:** no price found (gap).

**Doctolib (France, Germany)**
- **France** (June 2026, third-party review): about **€139 per month including VAT** for patient management and about **€135** for the clinical/financial suite, excluding options. **[SEE]** — [Lonasanté](https://www.lonasante.com/?p=11708)
- **Germany** (April 2026): **[SEE]** — [GIGA](https://www.giga.de/tech/was-kostet-doctolib-diese-preise-und-tarife-gibt-es-aktuell--01KPN5Y6VMKWGMSGVS4BDCZ046)
  - **"Patientenmanagement Light" at €139/month per doctor, which includes reminders**;
  - higher tiers at **€229, €299 and €475**;
  - an AI consultation assistant add-on at **€59/month**.
- **How reminders are sent:** by SMS 24–48 hours before the appointment, unless app notifications are on; the channels are not combined. No separate per-SMS fee was identified. **[SEE]** — [Selectra](https://selectra.info/telecom/actualites/marche/sms-de-rappel-de-rendez-vous-medical)
- **Competitor benchmark:** PagesJaunes' ClicRDV charged **€0.10 per SMS, capped at €30/month** (date unclear). **[PBU]** — [Le Quotidien du Médecin](https://infectiologie.lequotidiendumedecin.fr/sante-societe/e-sante/loffensive-tarifaire-de-pagesjaunes-sur-le-marche-des-e-agendas)
- Consistent with the sibling note's €139–149 figure.

**Docplanner group (Doctoralia in Spain, Jameda in Germany)**
- **Doctoralia** (third party, June 2025): from about **€69 per user/month** for individual professionals and about **€129/month** for clinic plans. SMS and e-mail reminders are included, but the plan that includes them is unclear. Capterra reviews from March 2026 complain about frequent price rises. **[PBU]** — [ZoftwareHub](https://zoftwarehub.com/products/doctoralia/pricing); [Capterra reviews](https://www.capterra.com/p/253301/Doctoralia-Pro/reviews/)
- **Jameda** (third party, April 2026): **[PBU]** — [KI-Syndikat](https://www.ki-syndikat.de/tools/jameda/); [Medizinio](https://medizinio.de/hersteller/jameda)
  - free basic profile;
  - **Gold Pro €119/month** and **Platin €199/month**, both paid annually, plus a **€299 one-time setup fee**;
  - automated reminders are mentioned, tier unspecified.
  - Another directory gives **€99 / €159**.
- This fills the sibling gap "no verified Docplanner pricing", but only with third-party data.

**Romania**
- **MediNote** (from the sibling note `romania_piata.md`): **50 lei/user/month** for a cloud practice-management system including SMS reminders. **[SEE]**
- **SMS to Romania via international APIs** (Twilio, Plivo, Sinch, Infobip): about **$0.06–0.0737 per message** (2025 guide); volume discounts are available. **[SEE]** — [Sent.dm Romania SMS pricing](https://www.sent.dm/en/resources/sms-pricing/romania-sms-pricing)
- **Local aggregators:** SMSLink sent more than **245M** messages in 2021; sendSMS.ro offers 100 free messages and then "preferential" pricing. **No per-SMS lei rates were visible in snippets.** **[SEE for existence; price is a gap]** — [Forbes.ro](https://www.forbes.ro/?p=264872); [Base.com integration](https://base.com/ro-RO/integrari/pricero/sendsms/)
- **Zarina CRM** (Romanian clinic CRM) offers SMS and e-mail confirmations; no price was visible. — [Zarina CRM](https://www.zarinacrm.ro/crm-cabinet-medical/programari-calendar/)

**Kaiku-like patient-reported-outcome tools:** no public pricing found (gap). Sibling notes give Kaiku's 2019 revenue of €1.3M only.

### Inferences
- **[SEE]** Western European willingness to pay for "booking + reminders" is about **€70–200 per practitioner per month**, with reminders treated as a bundled feature. In the UK NHS, **per-patient-per-year** pricing (about £0.2–1) is the norm for population messaging and recall. That model fits a *recall and follow-up* product better than per-seat pricing, because value scales with panel size.
- **[PBU]** A Romanian standalone recall and follow-up tool would anchor against MediNote's 50 lei/user (about €10) and against free CNAS apps. A realistic price band is perhaps **€20–60 per location per month plus SMS at cost**. This is my extrapolation (about a quarter to a third of Western bundles, per local PMS pricing), not observed data.
- **[PBU]** SMS unit cost (about €0.05–0.07) is non-trivial at Romanian price points. For example, 1,000 recall messages a month cost about €50–70, which equals the whole subscription. WhatsApp or e-mail channels, and passing SMS through at cost, matter for margin.

### Gaps
- No vendor-page-verified prices were obtained; every figure is third-party or a snippet.
- Not found: Software of Excellence prices; Polish ZnanyLekarz prices; Romanian SMS aggregator rate cards (SMSLink, sendSMS, Netopia); Kaiku, Noona or Varian PRO tool pricing; Romanian WhatsApp Business API costs.
- The Accurx G-Cloud figures may be time-limited promotional prices.

---

## 5. Verification of key regulatory dates

### Takeaway
The dates in `reglementare_ue_ro.md` **check out against independent secondary sources**, with three refinements:
1. **EHDS lab results and other category-2 data apply from 26 March 2031, not 2029.** The binding text dates Chapter III conformity for EHR systems put into service under Art. 26(2) to 2031. However, the Commission's Q&A says that from 26 March 2029 only EHR systems compliant with the harmonised-component specifications may be placed on the market. There is also a **2035** date, for Art. 75(5) on third-country participation in HealthData@EU.
2. **AI Act Omnibus (Reg. 2026/1744):** in force 27 July 2026; Annex I-A products, including MDR devices, from **2 Aug 2028**; Annex III from **2 Dec 2027**; both are now fixed calendar dates.
3. **MDR revision:** still at Parliament draft-report stage, with no adopted Parliament position or Council general approach found.

The **PLD** applies to products placed on the market **after 9 Dec 2026**. National transposition is lagging.

### Cited Findings

**(a) EU AI Act, Digital Omnibus on AI = Regulation (EU) 2026/1744**
- **Dates:** published in the OJ **24 July 2026**; **entered into force 27 July 2026**, on the third day after publication rather than the usual twentieth. **[EST]** (multiple law-firm snippets agree; OJ not opened) — [Akin Gump](https://www.akingump.com/en/insights/alerts/EU-AI-act-amendments-defer-and-clarify-obligations); [Steptoe](https://www.steptoe.com/en/news-publications/steptechtoe-blog/eu-ai-act-amendments-enter-into-force.html); [National Law Review](https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force); [Pillitteri](https://pasqualepillitteri.it/en/news/8951/eu-regulation-2026-1744-digital-omnibus-ai-act); [Abreu Advogados](https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/)
- **Annex III stand-alone high-risk systems:** **2 Dec 2027**, previously 2 Aug 2026. **[EST]**
- **Annex I Section A** (AI that is, or is a safety component of, a product under EU harmonisation legislation): **2 Aug 2028**, previously 2 Aug 2027. **[EST]**
  - The **MDR (2017/745) and IVDR (2017/746) are listed in Annex I Section A** (BK). So AI medical-device software needing notified-body assessment (class IIa+) becomes high-risk under the AI Act on 2 Aug 2028.
  - AI in machinery moved from Section A to Section B.
- **No conditionality:** the final text dropped the draft's link to standards readiness, so these are **unconditional calendar dates** (one commentator). **[SEE]**
- **Legacy systems:** high-risk systems already used by public authorities have until **2 Aug 2030** (one source). **[SEE]**
- **New Art. 5 prohibitions** (non-consensual intimate imagery and CSAM generation) apply from **2 Dec 2026**. **[SEE]**
- **What did not move:** obligations already in force (prohibitions, GPAI) are not deferred, and transparency obligations "generally apply from 2 Aug 2026". **[SEE]** (any Art. 50(2) grace period was not verified; see the sibling gap)
- **Consistency:** this matches `reglementare_ue_ro.md` §3 exactly.

**(b) EHDS, Regulation (EU) 2025/327**
- **Publication and entry into force:** published in the OJ **5 March 2025**.
  - EU Monitor gives entry into force as **25 March 2025**; Wikipedia and Kennedys give **26 March 2025**.
  - A 20-day lag from 5 March points to 25 March, but this is a one-day discrepancy and I did not settle it.
  - **[EST, with a ±1-day discrepancy]** — [EU Monitor](https://www.eumonitor.eu/9353000/1/j9vvik7m1c3gyxp/vmlg5gptv7zp); [Kennedys 2026](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-health-data-space-is-in-force-implications-for-healthcare-medtech-and-life-sciences); [Wikipedia](https://en.wikipedia.org/wiki/European_Health_Data_Space)
- **26 March 2027:** **general date of application**. Other deadlines on that date include Art. 99. A separate Art. 102(1) deadline falls on **26 March 2033**. **[EST]**
- **26 March 2029:** **[EST]** (snippet quoting the Art. 105 text) — [EC DG SANTE EHDS Q&A](https://health.ec.europa.eu/document/download/4dd47ec2-71dd-49fc-b036-ad7c14f6ed68_en?filename=ehealth_ehds_qa_en.pdf); [Noerr](https://www.noerr.com/en/insights/the-european-health-data-space-is-on-its-way-an-overview); [Lexology](https://www.lexology.com/library/detail.aspx?g=8560c1c7-2e2c-44be-8c24-20363a440738); [StreamLex Art. 105](https://streamlex.eu/articles/ehds-en-art-105/)
  - Primary-use provisions apply to **priority category 1** under Art. 14(1)(a)–(c): **patient summaries, ePrescriptions and eDispensations**.
  - They also apply to **EHR systems the manufacturer intends to process those categories**.
  - The Commission Q&A: "from 26 March 2029, you will only be allowed to place on the market EHR systems that comply with the common specifications for the harmonised components".
- **26 March 2031:** **[EST]** (snippet) — same sources; [Digital Policy Alert](https://digitalpolicyalert.org/event/28170-general-application-of-european-health-data-space-regulation-2025327-enters-into-force)
  - **Priority category 2** under Art. 14(1)(d)–(f) applies: **medical images and image reports; laboratory and other diagnostic results and reports; discharge reports**.
  - The binding text quoted in snippets says **Chapter III "shall apply to EHR systems put into service in the Union referred to in Article 26(2) from 26 March 2031"**.
  - Secondary commentary describes Art. 105(3) as the 2029 date and Art. 105(4) as the 2031 date.
  - **Tension:** Commission material implies a 2029 start for harmonised-component compliance, while the Art. 26(2) in-service systems date is 2031. The legal text governs.
- **26 March 2035:** **Art. 75(5)** (third-country participation in HealthData@EU). **[SEE]** — [EU Monitor](https://www.eumonitor.eu/9353000/1/j9vvik7m1c3gyxp/vmlg5gptv7zp)
- **Secondary use:** the bulk of Chapter IV (HDABs, data permits) applies from **2029**, with some data categories later (BK, consistent with the sibling note). The exact Art. 105 sub-paragraph for Chapter IV was **not verified** this session. **[PBU for exact split]**
- **Implementing acts:** first EHDS implementing regulations on **MyHealth@EU and HealthDCAT-AP** were reported in **September 2026**. Only the title was seen. **[SEE]** — [Produktkanzlei, 23 Sep 2026](https://www.produktkanzlei.com/en/2026/09/23/myhealtheu-and-healthdcat-ap/)
- **Relevance for a follow-up or recall product:**
  - it reads **lab results** (category 2, so 2031 obligations if it qualifies as an EHR system);
  - it may display **patient-summary** data (category 1, 2029).

**(c) MDR/IVDR targeted revision proposal (December 2025)**
- **Proposal:** COM(2025) 1023 final, adopted **16 December 2025**, procedure **2025/0404(COD)**; a 170-page proposal covering both regulations. **[EST]** — [Mason Hayes & Curran](https://www.mhc.ie/latest/insights/eu-commission-proposes-reform-of-the-medical-devices-regulation); [A&O Shearman](https://www.aoshearman.com/en/insights/life-sciences-and-healthcare-insights/medical-devices-eu-commission-proposes-mdr-and-ivdr-revision); [Hogan Lovells](https://hlc.com/en/publications/european-commissions-proposal-to-amend-the-mdr); [RAPS](https://www.raps.org/resource/eu-officials-detail-proposed-mdr-ivdr-revisions.html)
  - Removes the 5-year maximum validity of notified-body certificates.
  - Moves surveillance audits from annual to every two years where justified.
  - Cuts notified-body fees by **50% for micro** and **25% for small** enterprises.
- **Parliament:** the **SANT rapporteur's draft report was published 1 July 2026**, with **more than 130 amendments**, including a new "niche device" category and more coordination between authorities. **[SEE]** — [Mondaq, "How will the EU Parliament shape the MDR/IVDR revision"](https://www.mondaq.com/product-liability-safety/1827990/how-will-the-eu-parliament-shape-the-mdrivdr-revision-draft-report-indicates-how-parliament-may-seek-to-amend-commissions-proposals)
  - The sibling note (DSV, July 2026) says work "launched 14 July 2026", with a **SANT vote scheduled 3 Dec 2026** and a plenary in early 2027. These are compatible: draft report on 1 July, committee kick-off mid-July.
- **Council:** BioMed Alliance (June 2026) says Parliament and Council are "currently discussing". **No Council general approach or Parliament plenary position was found as of Oct 2026.** **[SEE]** — [BioMed Alliance](https://www.biomedeurope.org/?p=275923)
- **Status:** **the current MDR applies unchanged.** Adoption is not expected before 2027, and application later still. **[SEE]**

**(d) Product Liability Directive (EU) 2024/2853**
- **Dates:** transposition deadline **9 December 2026**; maximum harmonisation. **[EST]** — [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive); [Xictron](https://www.xictron.com/en/blog/new-product-liability-law-software-december-2026/); [Buse](https://buse.de/en/blog-en/commercial-en/what-will-change-with-the-new-eu-product-liability-directive-eu-2024-2853/); [IBA](https://www.ibanet.org/European-Product-Liability-Directive-liability-for-software)
  - It applies to products **placed on the market or put into service after 9 Dec 2026**.
  - Older products stay under Directive 85/374 **unless substantially modified**, for example by an extensive software upgrade.
- **Software is now a product:** software, including AI systems and SaaS components, is expressly a "product". The exception is **non-commercial** open-source software. There is **no cap** on compensation. **[EST]**
- **Transposition status:**
  - **Howden Re (April 2026, data to November 2025):** Netherlands, Sweden and Germany had drafts or formal steps. **Romania** was among states with "preparatory or scheduling measures". Most states had not reported any updates. **[SEE]** — [Howden Re, Apr 2026](https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-04/Howden%20Re%20Casualty%20in%20focus%20%234%20-%20%20the%20new%20EU%20product%20liability%20directive%20%26%20AI%20April212026.pdf)
  - **Germany:** the draft *Gesetz zur Modernisierung des Produkthaftungsrechts* had its Bundestag first reading on **4 March 2026**. Final passage was not confirmed. **[SEE]** — [Buse](https://buse.de/en/blog-en/commercial-en/what-will-change-with-the-new-eu-product-liability-directive-eu-2024-2853/)
- **Consistency:** matches `reglementare_ue_ro.md` §7.

### Inferences
- **[EST]** For a follow-up, recall or reminder product launched in 2027 (non-device, no AI-driven diagnosis), the binding near-term regime is: **GDPR now, the PLD for any version released after 9 Dec 2026, and AI Act Art. 50 transparency if it has a chatbot.** EHDS EHR-system obligations would bite only in **2029** (if it handles patient summaries) or **2031** (if it handles lab results), and only if it qualifies as an "EHR system".
- **[PBU]** Because category 2 data (lab results) moves to 2031, an abnormal-lab follow-up tracker has a **longer runway before EHDS certification** than a patient-summary viewer. EHDS-standard lab-result exchange (EEHRxF) will also not be mandatory before 2031, so Romanian integrations will stay bespoke (HL7v2, PDF or CSV) until then.
- **[PBU]** The PLD makes "a missed recall caused by a software defect" a potential strict-liability claim for versions placed on the market after 9 Dec 2026. Logging, audit trails and explicit "clinician remains responsible" workflow design are risk controls, not just features.

### Gaps
- The **Official Journal texts** of Reg. 2026/1744 and Reg. 2025/327 Art. 105 could not be opened (EUR-Lex blocked). All dates are from consistent secondary snippets.
- The exact Art. 105 sub-paragraph numbering for Chapter IV (secondary use) and the full list of 2029 provisions need a EUR-Lex check.
- Romania's PLD transposition law was not found; whether Romania will meet 9 Dec 2026 is unknown.
- The MDR revision's Council general approach and the SANT vote date (3 Dec 2026, per the sibling note) were not confirmed against EP or Council records.
