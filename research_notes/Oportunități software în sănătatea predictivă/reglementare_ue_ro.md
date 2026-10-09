# Regulatory, clinical-validation and data-access feasibility of healthcare software in Romania / EU (as of 9 Oct 2026)

These are research notes, not legal advice. Every classification below is indicative only and depends on the exact intended purpose, functionality and claims.

How to read the labels:
- Evidence strength: **[EST]** Established evidence · **[SEE]** Strong emerging evidence · **[PBU]** Plausible but unproven · **[SPEC]** Speculative.
- Provenance: **(snippet)** means the fact comes from a WebSearch result summary in this session; the page itself could NOT be opened because WebFetch was blocked by the egress proxy for EUR-Lex, health.ec.europa.eu, cms.law, orrick.com, openregulatory.com, eumonitor.eu and every other domain tried. **(BK)** means the fact comes from the researcher's background knowledge of the legal text. It was not re-verified in this session, and the canonical text URL is given so it can be checked. The session also ran out of its web-search budget, so several sub-questions stayed open (see Gaps).

---

## 1. GDPR for health data: Art. 9 bases, processor duties, DPIA, Romanian specifics, pseudonymisation, US AI transfers

### Takeaway
A vendor building tools for clinics is normally a **processor** (Art. 28). It relies on the clinic's own Art. 9(2)(h) basis and must sign a DPA. As soon as the vendor reuses the data for its own purposes (training a predictive model, benchmarking, a B2C product), it becomes a **controller** and needs its own Art. 6 + Art. 9 basis. In Romania, Legea 190/2018 art. 3 additionally requires **explicit consent or an express legal provision** for automated decision-making or profiling that uses health data. Pseudonymised data stays personal data for anyone who can re-identify it. The 2025 *EDPS v SRB* ruling opens only a narrow, recipient-side door. The EU-US DPF is valid but its appeal is pending at the CJEU.

### Cited Findings
**Art. 9 legal bases**
- Art. 9(1) GDPR prohibits processing health data unless an Art. 9(2) exception applies. The relevant exceptions are:
  - (a) explicit consent;
  - (h) processing necessary for preventive or occupational medicine, assessment of working capacity, medical diagnosis, provision of health or social care or treatment, or management of health/social care systems, "on the basis of Union or Member State law or pursuant to contract with a health professional", subject to the Art. 9(3) professional-secrecy safeguard;
  - (i) public health;
  - (j) scientific research, which needs Union or Member-State law plus Art. 89(1) safeguards.

  Art. 9(4) lets Member States add further conditions for genetic, biometric and health data. [EST] (BK) — [GDPR, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

**Processor obligations and DPO**
- Art. 28 requires a written processor contract covering: processing only on documented instructions, confidentiality, Art. 32 security, prior authorisation of sub-processors with flow-down, assistance with data-subject rights and with Arts. 32–36, deletion or return at the end, and audits. Under Art. 28(10), a processor that determines purposes and means itself is treated as a controller. [EST] (BK) — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- Art. 37(1)(c) requires a DPO where core activities consist of large-scale processing of special-category data. [EST] (BK) — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

**DPIA**
- Art. 35(3)(b) makes a DPIA mandatory for large-scale processing of special categories. Recital 91 says processing of patient data by an individual physician is not "large scale". [EST] (BK) — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- The WP29/EDPB DPIA guidelines (WP248 rev.01) list nine criteria. Processing that meets two or more generally needs a DPIA. The criteria include: sensitive data, vulnerable data subjects (patients), innovative technology, evaluation or scoring, systematic monitoring, large scale, and matching or combining datasets. A typical health-AI product meets three or more. [EST] (BK) — [WP248 rev.01](https://ec.europa.eu/newsroom/article29/items/611236)

**Automated decisions and profiling**
- Under Art. 22(4) GDPR, automated decisions with legal or similarly significant effects may not be based on special-category data unless Art. 9(2)(a) (explicit consent) or (g) (substantial public interest) applies, with suitable safeguards. [EST] (snippet) — [gdpr-text.com Art. 22 (RO)](https://gdpr-text.com/ro/read/article-22); see also [WP251 guidelines on automated decision-making](https://ec.europa.eu/newsroom/article29/items/612053)

**Romanian specifics**
- **Legea 190/2018, art. 3(1):** "Prelucrarea datelor genetice, biometrice sau a datelor privind sănătatea, în scopul realizării unui proces decizional automatizat sau pentru crearea de profiluri, este permisă cu consimțământul explicit al persoanei vizate sau dacă prelucrarea este efectuată în temeiul unor dispoziții legale exprese", with appropriate safeguards. [EST] (snippet) — [ANSPDCP text](https://www.dataprotection.ro/servlet/ViewDocument?id=1520); [Rubinian commentary](https://www.rubinian.com/legea-190-2018-masuri-de-punere-in-aplicare-a-regulamentului-ue-2016-679-gdpr)
- **Legea 190/2018, art. 3(2):** health data processed for public-health purposes (in the sense of Reg. 1338/2008) "nu se poate efectua ulterior, în alte scopuri, de către terțe entități". [EST] (snippet) — same sources. The consolidated versions seen were current to about March 2025, so later amendments are unchecked.
- **Legea 190/2018, art. 4 (CNP):** processing the national identification number (CNP) on a legitimate-interest basis requires specific safeguards: technical and organisational measures, appointing a DPO, set retention periods, and periodic staff training. This matters because Romanian patient records are keyed on CNP. [SEE] (BK; exact wording not re-verified) — [ANSPDCP text](https://www.dataprotection.ro/servlet/ViewDocument?id=1520)
- **ANSPDCP DPIA list:** Decizia ANSPDCP nr. 174 of 18 Oct 2018, published in Monitorul Oficial nr. 919 of 31 Oct 2018 and adopted under Art. 35(4), sets the list of operations for which a DPIA is mandatory. It is recorded in the EDPB consistency register. [EST] (snippet) — [EDPB register entry](https://www.edpb.europa.eu/our-work-tools/consistency-findings/register-decisions/2018/romania-sas-list-kind-processing_ro); [copy of the decision](https://primariabt.ro/gdpr/legislatie/Decizie174_18.10.2018.pdf). The exact health-related items could not be retrieved (see Gaps).

**Legea 46/2003 (patient rights)**
- **Art. 21:** all information about the patient's condition, test results, diagnosis, prognosis, treatment and personal data is confidential, **even after death**. [EST] (snippet) — [Legea 46/2003 consolidated, MS, 20.11.2023](https://audit.ms.ro/media/documents/LEGE_Nr._46_2003_forma_la_data_de_20.11.2023.pdf)
- **Art. 22:** confidential information may be disclosed only with the patient's **explicit consent** or where the law expressly requires it. [EST] (snippet) — same source
- **Art. 24(2):** the patient may designate a person with access to the information, both during life and after death. [EST] (snippet) — same source
- A February 2023 draft OUG proposed a new art. 22^1 on access by relatives of deceased patients. Its adoption is unconfirmed. [PBU] (snippet) — [MS draft OUG 03.02.2023](https://management-documente.ms.ro/media/documents/TEXT-PROIECT-OUG-03.02.2023.docx)

**Pseudonymisation**
- GDPR Art. 4(5) defines pseudonymisation. Recital 26 states that pseudonymised data which could be attributed to a person using additional information "should be considered to be information on an identifiable natural person". [EST] (BK) — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- The EDPB adopted Guidelines 01/2025 on pseudonymisation in January 2025 for public consultation. They treat pseudonymised data as personal data and pseudonymisation as a risk-reduction safeguard. [SEE] (BK; final-version status not checked) — [EDPB Guidelines 01/2025](https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en)
- **CJEU C-413/23 P, *EDPS v SRB*, 4 Sept 2025** (snippet):
  - Pseudonymised data can be personal data for the original controller but **not** for a recipient that cannot reverse the pseudonymisation or identify data subjects by other reasonably likely means. [SEE] — [Bird & Bird](https://cm.twobirds.com/en/insights/2025/eu-the-srb-decision-a-new-era-for-personal-data-and-data-processing-agreements); [Jones Day](https://www.jonesday.com/de/insights/2025/09/cjeu-clarifies-scope-of-personal-data-in-edps-v-srb-decision)
  - Information duties attach at the point of collection, from the original controller's perspective, so recipients must still be disclosed. [SEE] — [Jones Day](https://www.jonesday.com/de/insights/2025/09/cjeu-clarifies-scope-of-personal-data-in-edps-v-srb-decision); [A&O Shearman](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cjeu-clarifies-concept-of-personal-data-for-a-transfer-of-pseudonymised-data-to-third-parties)
  - The case arose under Reg. 2018/1725, but the definitions are identical to the GDPR's, so the ruling carries interpretative weight for private parties. [SEE] — [Baker Botts](https://ourtake.bakerbotts.com/post/102l35z/cjeu-clarifies-requirements-and-definition-of-pseudonymisation)
  - Bird & Bird raises, as an open question rather than a holding, whether DPAs are needed with processors that cannot identify anyone. [PBU] — [Bird & Bird](https://cm.twobirds.com/en/insights/2025/eu-the-srb-decision-a-new-era-for-personal-data-and-data-processing-agreements)

**Transfers to US AI providers (EU-US DPF)**
- The EU-US DPF adequacy decision was adopted 10 July 2023. [EST] (BK)
- On 3 Sept 2025 the General Court dismissed *Latombe v Commission* (T-553/23), assessing the US situation as at the date of adoption. [EST] (snippet) — [Epstein Becker Green](https://www.ebglaw.com/workforce-bulletin/adequacy-of-the-eu-u-s-data-privacy-framework-survives-challenge); [Streamlex](https://streamlex.eu/news/general-court-ruling-latombe-commission/)
- Latombe appealed to the Court of Justice on 31 Oct 2025 (C-703/25 P). On 4 June 2026 the CJEU President admitted Microsoft as an intervener supporting the Commission. No hearing date had been announced as of July 2026. [SEE] (snippet) — [DataGuidance](https://www.dataguidance.com/news/eu-cjeu-admits-microsoft-intervener-appeal-concerning); [EDPL 2026/1](https://edpl.lexxion.eu/article/EDPL/2026/1/15)
- One source says noyb threatened a separate annulment action after a 30 June (2026) letter. This is single-source and unverified. [PBU] (snippet) — [SecurePrivacy](https://secureprivacy.ai/blog/is-the-eu-us-data-privacy-framework-at-risk-the-ftc-ruling-explained-2026)
- One commentary says the DPF is currently still valid and the simplest route for transfers to certified US recipients. [SEE] (snippet) — [Corp-Intl](https://corp-intl.com/news/is-the-data-privacy-framework-still-valid)

### Inferences
- **B2B clinic tools:** the clinic is controller (Art. 9(2)(h) plus Legea 95/2006 and Legea 46/2003); the vendor is processor. The minimum compliance kit is:
  - an Art. 28 DPA;
  - a sub-processor list (cloud, email/SMS, LLM API);
  - Art. 32 measures;
  - help with the clinic's DPIA;
  - EU hosting.

  This is the cheapest compliance position. [SEE]
- **Training a model on clinic data:** this is not covered by the clinic's 9(2)(h) basis by default. If the vendor decides to do it, the vendor becomes a controller under Art. 28(10). Realistic routes are:
  - (a) explicit patient consent (Art. 9(2)(a)), which Legea 190 art. 3 requires anyway for profiling;
  - (b) the clinic commissioning the model for its own care purposes, with the vendor as processor. Whether 9(2)(h) covers this is contested. [SPEC]
  - (c) true anonymisation, which must meet the Recital 26 test. Pseudonymisation is not enough;
  - (d) research collaborations under 9(2)(j) with an ethics committee. Romania's national research-law basis is unclear (see Gaps);
  - (e) EHDS secondary-use permits from 2029 onward (Section 4). [SEE]
- **Indirect health data:** under CJEU case law (C-184/20 *OT*, 1 Aug 2022; C-21/23 *Lindenapotheke*, 4 Oct 2024), data that indirectly reveal health status are special-category data (BK). Appointment histories at a specialty clinic, or no-show data from an oncology department, are therefore likely health data. "Operational" prediction such as no-show risk may then trigger Legea 190 art. 3, meaning explicit consent or an express legal basis for profiling. [PBU]
- **SRB nuance:** it can help a recipient of strongly pseudonymised data (for example, a vendor receiving key-coded extracts with no access to the key) argue that the data is not personal data in its own hands. It does **not** help the clinic, which still holds the key, and it does not remove the clinic's transparency duties. Romanian confidentiality under Legea 46/2003 art. 21–22 applies to the clinic regardless. Never treat pseudonymised patient data as unrestricted. [SEE]
- **US LLM APIs:** sending prompts that contain patient data is a transfer, plus a processor arrangement. Today this can rely on the DPF if the provider is certified, with SCCs plus a transfer impact assessment as fallback. Because the appeal is pending, prefer EU-region processing and zero-retention options, keep SCCs in the DPA as backup, and minimise or redact identifiers before calls. [SEE]

### Gaps
- The text of Decizia ANSPDCP 174/2018 could not be retrieved, so its health-specific items are unverified. It probably covers large-scale special-category data, vulnerable persons, innovative technology and systematic monitoring. [PBU]
- No ANSPDCP fines specific to health-sector processors were found in this session.
- Not checked: whether Legea 190/2018 has a specific scientific-research derogation article usable under 9(2)(j), or whether Romanian law provides any express legal provision allowing profiling with health data.
- The Commission's November 2025 "Digital Omnibus" proposal reportedly sought to amend GDPR definitions, codifying a relative approach to personal data, and to ease processing for AI development. Its legislative status as of Oct 2026 was not checked (BK, [PBU]).
- The status of US oversight bodies relevant to DPF adequacy (PCLOB, FTC independence) in 2025–2026 was not verified in this session.

---

## 2. EU MDR 2017/745: when software is a medical device, Rule 11, examples, and cost/time of class I vs IIa

### Takeaway
Whether software qualifies as a device is driven by the **intended purpose as stated by the manufacturer, including in promotional and sales materials**. The MDR definition explicitly includes **"prediction" and "prognosis"**, so patient-level predictive software with a medical purpose is a device. Rule 11 pushes almost all software that provides information for diagnostic or therapeutic decisions to **class IIa or higher**, which needs a notified body. Unlike the US, the EU has **no "transparent CDS" carve-out**. Purely administrative, storage, communication and "simple search" software is not a device. A December 2025 proposal could move more software to class I, but it is not law (as of Oct 2026).

### Cited Findings
**Definitions**
- Art. 2(1) MDR defines a medical device as including software intended for "diagnosis, prevention, monitoring, **prediction, prognosis**, treatment or alleviation of disease". [EST] (BK) — [MDR, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
- Art. 2(12) defines "intended purpose" as the use for which a device is intended according to the manufacturer's data on the label, in the instructions for use, **in promotional or sales materials or statements**, and as specified in the clinical evaluation. [EST] (BK) — [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
- Recital 19: software specifically intended for a medical purpose is a device. "Software for general purposes, even when used in a healthcare setting, or software intended for life-style and well-being applications is not a medical device." [EST] (BK) — [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj)

**Rule 11 (Annex VIII)**
- Software intended to provide information used to take decisions with diagnostic or therapeutic purposes is **class IIa**. It is **class III** if such decisions may cause death or irreversible deterioration of health, and **class IIb** if they may cause serious deterioration of health or a surgical intervention.
- Software intended to monitor physiological processes is **class IIa**. It is **class IIb** if it monitors vital physiological parameters whose variations could result in immediate danger.
- All other software is **class I**.

[EST] (BK) — [MDR Annex VIII](https://eur-lex.europa.eu/eli/reg/2017/745/oj)

**MDCG 2019-11 Rev.1**
- The Commission published Rev.1 on **17 June 2025**. [EST] (snippet) — [European Commission](https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en)
- Reported changes include:
  - stronger emphasis on a clearly documented intended purpose, traceable in labelling and technical documentation;
  - Rule 11(a) clarified with **illness-prevention examples**;
  - an expanded chapter on modules and modular software;
  - AI explicitly in scope;
  - the interplay with the EHDS for EHR systems, including when EHR systems may qualify as devices;
  - new examples, including a new class I example.

  Commentators disagree on how substantive the changes are: Emergo says "no substantive changes", others call it a "significant rewrite". [SEE] (snippet) — [Emergo by UL](https://www.emergobyul.com/news/european-revision-primary-software-guidance-mdcg-2019-11-revision-1-small-changes-meaningful); [GMP Insiders](https://gmpinsiders.com/mdcg-2019-11-rev1-mdr-ivdr/); [Casus Consulting](https://casusconsulting.com/mdcg-2019-11-rev-1-updated-guidance-software-qualification-classification-mdr-ivdr/); [MDR Regulator](https://mdrregulator.com/news/revised-mdcg-2019-11-guidance-updated-approach-to-qualification-and-classification-of-medical-software)
- The MDCG 2019-11 qualification decision tree: software whose only action on data is **storage, archival, communication, simple search or lossless compression** is not medical device software (MDSW). The action must be for the benefit of **individual patients**. [EST] (BK) — [MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- MDCG 2019-11 examples: hospital information systems supporting patient administration (admission, **appointment scheduling**, insurance and billing) are not devices. Additional modules with a medical purpose, such as decision-support modules, can be MDSW. The same reasoning applies to EHRs that only store and transfer data. [SEE] (BK) — [MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- MDCG 2019-11 contains an IMDRF-based table (seriousness of the condition × significance of the information: treat/diagnose, drive or inform clinical management). In practice, everything that informs individual clinical management lands in IIa or higher. [SEE] (BK)
- A consultancy summary says most medical device software is "at least class IIa" under the MDR. [SEE] (snippet) — [Spyrosoft](https://spyro-soft.com/blog/ce-marking)
- Under MDCG 2019-11, software whose information comes solely from IVD data (for example, interpreting lab results) is assessed under the **IVDR** rather than the MDR. [SEE] (BK; also noted in snippet) — [MDCG 2019-11 summaries](https://www.regdesk.co/blog/qualification-and-classification-of-software-under-eu-mdr-2017-745-and-ivdr-2017-746/)

**MDR reform proposal (not law)**
- The Commission proposed a targeted MDR/IVDR revision on **16 Dec 2025** (COM(2025) 1023, 2025/0404(COD)). It would:
  - amend the software classification rule, which "could lead to significantly more software being classified as Class I";
  - remove the 5-year maximum validity of notified-body certificates in favour of risk-based reviews.

  [SEE for the proposal; PBU for the final outcome] (snippet) — [MedTech Europe, 16.12.2025](https://www.medtecheurope.org/2025/12/16/revision-proposal-is-first-step-towards-fixing-europes-complex-medical-devices-diagnostics-rules/); [Mantra Systems](https://mantrasystems.com/articles/fixing-the-mdr-and-ivdr-eu-commissions-proposed-amendments-what-they-mean-for-manufacturers); [A&O Shearman](https://www.aoshearman.com/en/insights/ao-shearman-on-life-sciences/eu-commission-proposes-much-anticipated-mdr-and-ivdr-revision); [Casus (feedback period to 4 Mar 2026)](https://casusconsulting.com/mdr-ivdr-reform-proposal-com20251023-open-feedback-period-until-4-march-2026/)
- Status: the European Parliament (ENVI/SANT) rapporteur Oliver Schenk launched work on 14 July 2026, with a **SANT committee vote scheduled 3 Dec 2026** and a plenary position expected in **early 2027**. The Council (Irish Presidency) aims for a general approach by end-2026. Another source suggests adoption could slip to 2028. Until adoption, the **current MDR applies**. [PBU] (snippet; secondary source, not checked against EP records) — [DSV Europe, July 2026](https://dsv-europa.de/en/news/2026/07/mdr-ivdr.html); [meddeviceguide](https://meddeviceguide.com/blog/eu-mdr-ivdr-simplification-proposal-2026-guide)

**Other MDR obligations relevant to a small company**
- Art. 5(5) "in-house" exemption: health institutions may manufacture and use devices internally, without CE marking, under conditions. These include a justification that an equivalent device on the market cannot meet the target patient group's needs, and no transfer to another legal entity. [EST] (BK) — [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
- Art. 15(2): micro and small enterprises need not employ a Person Responsible for Regulatory Compliance (PRRC) but must have one "permanently and continuously at their disposal". [EST] (BK) — [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
- Art. 10(16): manufacturers must have measures giving sufficient financial coverage for product liability, proportionate to risk class and company size. In practice this means liability insurance. [EST] (BK) — [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
- Class I software follows manufacturer self-declaration (Art. 52(7), technical documentation per Annexes II–III). Even class I still requires a QMS (Art. 10(9)), clinical evaluation (Art. 61), risk management, post-market surveillance, vigilance, UDI and EUDAMED registration. [EST] (BK) — [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
- Class IIa requires a notified body (Annex IX QMS plus technical documentation sampling, or Annex XI). [EST] (BK)
- MDCG 2020-1 sets out clinical evaluation for MDSW on three pillars: valid clinical association (scientific validity), technical performance, and clinical performance. [EST] (BK) — [MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- Core standards: ISO 13485 (QMS), IEC 62304 (software lifecycle), ISO 14971 (risk), IEC 62366-1 (usability), IEC 82304-1 (health software). ISO 13485 certification alone does not equal MDR compliance. [EST] (snippet for the last point) — [DQS](https://www.dqsglobal.com/en/explore/blog/eu-mdr-certification-process-ce-marking-medical-devices)
- MDCG 2025-6 (with the AI Board) gives FAQ guidance on the interplay between the MDR/IVDR and the AI Act (June 2025). [SEE] (BK) — [MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)

**Costs and timelines (estimates)**
- Notified-body fees: one published list (SIQ, Slovenia, 2022) shows:
  - MDR basic fee for class IIa: **€2,000**;
  - annual fee for class IIa: **€1,500**;
  - technical-documentation review from **€240/h**;
  - clinical-evaluation review from **€250/h**;
  - ISO 13485 QMS audit from **€140/h**.

  These are 2022 figures, and the total depends on hours. [SEE] (snippet) — [SIQ fee list](https://www.siq.si/wp-content/uploads/2021/12/MDR-DN021E.pdf)
- Notified bodies must publish standard fees (MDR Art. 50), and the Commission has published a compiled list. [EST] (snippet) — [MDR Regulator](https://mdrregulator.com/news/european-commission-published-notified-body-list-of-standard-fees-for-mdr-and-ivdr-related-services); [TÜV Nord list 2025](https://www.tuv-nord.com/fileadmin/Sites/TUEV_NORD_Worldwide/ScandinaviaMNB/Files/PDF/EN/List-of-standard-fees-publik-20250103.pdf)
- A vendor-blog estimate (2026) puts **class IIa total cost at €32,000–110,000 over 9–18 months**. This covers QMS, technical file, notified-body fees, clinical evaluation, testing and EUDAMED, and **excludes clinical investigations**. Treat it as order-of-magnitude only. [PBU] (snippet) — [meddeviceguide, 2026](https://meddeviceguide.com/blog/ce-marking-cost-medical-devices-guide)
- Other guides give 6 months to 2 years for certification, depending on documentation quality and notified-body workload. [PBU] (snippet) — [Jama Software](https://www.jamasoftware.com/?p=10952); [DQS](https://www.dqsglobal.com/en/explore/blog/eu-mdr-certification-process-ce-marking-medical-devices)

### Inferences
**Indicative qualification of the example product types.** None of these is a definitive classification.

| Product idea | Likely status | Label | What flips it |
|---|---|---|---|
| Appointment booking / recall on dates set by staff | Not a device (HIS administration) | [SEE] | System **decides** who needs recall or earlier review from clinical data or individual risk → likely MDSW |
| Patient portal (view documents/results, messaging, booking) | Not a device (storage, communication, display) | [SEE] | Adds interpretation, symptom advice or risk outputs → MDSW. It may also be an **EHR system** under EHDS (Section 4) |
| Lab-result routing (HL7/PDF delivery, notifications) | Not a device (communication) | [SEE] | New flags, trend predictions or prioritisation beyond the lab's own reference flags → MDSW, possibly under the **IVDR** if derived solely from IVD data |
| Data aggregation / visualisation | Not a device if it only displays data faithfully | [SEE] | Computes new clinical parameters, scores or alerts for individual patients → MDSW |
| Risk calculator implementing a validated score (SCORE2, CHA2DS2-VASc) | Likely **MDSW class IIa**: patient-level information for therapeutic decisions such as statin or anticoagulant initiation | [SEE] | No EU equivalent of FDA's 520(o)(1)(E) carve-out. "It is just a published formula" is not a recognised exemption. Population-level stratification for administrative outreach is borderline. [SPEC] |
| Patient triage chatbot / symptom checker | Likely **MDSW class IIa or higher** | [SEE] | Also AI Act: Annex III high-risk if it is "emergency healthcare patient triage"; Art. 50 disclosure applies now (Section 3) |
| Wellness app (sleep, fitness, stress, generic nutrition) | Not a device (Recital 19) | [EST] | Claims such as "detects AF", "prevents diabetes", "manages hypertension", "predicts your risk of disease" → device |
| RPM dashboard with thresholds/alerts | **MDSW**: monitoring physiological processes → IIa; vital parameters with immediate-danger potential → **IIb** | [SEE] | A pure data pipe from a CE-marked device with no alerting may not be a device, but could be an accessory [PBU] |
| LLM scribe / visit summariser | Borderline. Pure transcription or summarisation is arguably not a device | [PBU] | Suggests diagnoses, orders or codes used for clinical decisions → MDSW |
| ICD/DRG coding and CNAS reporting help, billing | Not a device (administrative) | [SEE] | — |

- **Marketing claims are a classification input.** Words such as "diagnose, detect, predict risk of [disease], triage, monitor [condition], prevent [disease], personalised treatment" in the website, app store, pitch deck or sales emails can create a medical intended purpose under Art. 2(12). Software that is functionally identical but marketed for workflow use may stay non-MD. Regulators look at the totality of claims, so a "not a medical device" disclaimer does not cure medical claims. [SEE]
- **Class I under Rule 11 is narrow today.** It covers essentially software with a medical purpose that does not inform diagnosis or therapy decisions and does not monitor physiological processes. Some prevention or lifestyle-medicine software, depending on Rev.1's illness-prevention examples, might fit. The Dec 2025 proposal may widen class I, but not before about 2027–2028. [PBU]
- **Class I cost:** it is self-certified, but QMS, IEC 62304 documentation, a clinical evaluation, PMS and PRRC access are still needed. For a solo founder with about €25k and 10–12 h/week, class IIa (notified body, roughly €32–110k and 9–18 months, plus a clinical-evidence burden) is out of reach as a first product. Class I is feasible but slow. [SPEC]

### Gaps
- The MDCG 2019-11 Rev.1 PDF and the current Borderline & Classification Manual were not opened. Exact new examples (especially illness-prevention and class I examples) are unverified.
- No sourced cost estimate was found for **class I software** (internal QMS plus technical file plus consultants), nor current notified-body lead times in 2026.
- No Romanian notified body for MDR software was identified. The role of ANMDMR (Romanian competent authority) in registering class I software was not verified.
- The 2025–2026 EUDAMED mandatory-module timeline was not verified.

---

## 3. EU AI Act (Reg. 2024/1689): which medical AI is high-risk, timelines after the Digital Omnibus, Art. 50, providers vs deployers, GPAI via API

### Takeaway
AI that is itself, or is part of, a medical device requiring **notified-body** conformity assessment (MDR class IIa and above) is high-risk under **Art. 6(1)**. After the **Digital Omnibus on AI (Regulation (EU) 2026/1744, OJ 24 July 2026)**, those obligations apply from **2 Aug 2028** instead of 2 Aug 2027. Annex III stand-alone high-risk systems (including **emergency healthcare patient triage** and life/health insurance pricing) apply from **2 Dec 2027**. **Art. 50 transparency obligations apply since 2 Aug 2026.** A founder who calls a foundation model via API is normally the **provider of their own AI system**, not a GPAI-model provider.

### Cited Findings
**What is high-risk**
- Art. 6(1): an AI system is high-risk when (a) it is a safety component of a product, or is itself a product, covered by Annex I legislation (MDR and IVDR are in Annex I, Section A), **and** (b) that product must undergo **third-party conformity assessment**. Self-certified class I MDSW therefore does not meet 6(1)(b). [EST] (BK) — [AI Act, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Annex III point 5 lists as high-risk:
  - (a) AI used by public authorities to evaluate eligibility for essential public services, **including healthcare services**;
  - (c) risk assessment and pricing in **life and health insurance**;
  - (d) emergency-call evaluation and dispatch prioritisation, "as well as of **emergency healthcare patient triage systems**".

  [EST] (BK) — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

**Roles and obligations**
- Roles: "provider" (Art. 3(3)) develops an AI system, or has it developed, and places it on the market or puts it into service under its own name. "Deployer" (Art. 3(4)) uses it under its authority. Under Art. 25, a deployer or other third party becomes a provider if it puts its name on a high-risk system, substantially modifies it, or changes its intended purpose so that it becomes high-risk. [EST] (BK) — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Deployer obligations for high-risk systems (Art. 26): use per instructions, assign human oversight, ensure input-data relevance, monitor and report incidents, keep logs (at least 6 months), and inform workers. Under Art. 27, a fundamental-rights impact assessment applies to public bodies and private entities providing public services, plus Annex III 5(b)/(c) deployers. [EST] (BK) — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Art. 50 transparency:
  - (1) providers must design systems that interact with people so users know they are dealing with AI, unless obvious;
  - (2) providers of generative systems must mark synthetic audio, image, video or text in a machine-readable way, with exceptions for assistive or standard editing;
  - (3) deployers of emotion-recognition or biometric-categorisation systems must inform people;
  - (4) deployers must disclose deep fakes and certain AI-generated public-interest text.

  [EST] (BK) — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

**Original timeline**
- The Act entered into force 1 Aug 2024. Prohibitions and AI literacy (Art. 4) applied from 2 Feb 2025, GPAI obligations from 2 Aug 2025, most provisions from 2 Aug 2026, and Art. 6(1) originally from 2 Aug 2027. [EST] (BK) — [AI Act Art. 113](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

**Digital Omnibus on AI**
- Adopted as **Regulation (EU) 2026/1744**: European Parliament endorsement 16 June 2026, Council final approval 29 June 2026, OJ publication **24 July 2026**, entry into force **27 July 2026**. Some sources give 8 July (likely the signature date). [SEE] (snippet; OJ not opened) — [Orrick, July 2026](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes); [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/); [Praxikon](https://www.praxikon.com/en/posts/digital-omnibus-high-risk-postponement-december-2027)
- New dates:
  - Annex I / Art. 6(1) high-risk (including **medical devices**): **2 Aug 2028**, previously 2 Aug 2027;
  - Annex III high-risk: **2 Dec 2027**, previously 2 Aug 2026;
  - a separate **2 Aug 2030** date reported for systems used by public authorities.

  The stated reason is that standards and national authorities were not ready. It is a deferral, not a repeal. [SEE] (snippet) — [Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon); [Cooley](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/); [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- **Art. 50 transparency obligations have applied since 2 Aug 2026** and were not deferred, per most sources. One Usercentrics snippet says there was "no formal delay"; this appears to be outdated content. [SEE] (snippet) — [Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon); conflicting: [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/)

**GPAI**
- The Commission's GPAI guidelines and the GPAI Code of Practice were published in July 2025. Under the guidelines, a downstream actor that only integrates a model via API is not a GPAI-model provider. A modifier becomes one only if the modification uses compute above roughly one-third of the original model's training compute. [SEE] (BK) — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

### Inferences
- **Solo founder using an LLM API:**
  - Obligations: AI literacy for themselves and staff (Art. 4, unless changed by the Omnibus; see Gaps); Art. 50(1) disclosure in any chatbot; Art. 50(2) marking if the product generates synthetic content; contractual reliance on the GPAI provider's Art. 53 documentation.
  - Not high-risk if the product is administrative or wellness, or class I MDSW.
  - Becomes high-risk from **2 Aug 2028** if it is class IIa+ MDSW with AI (the MDR and AI Act conformity assessments are combined through the same notified body).
  - Becomes high-risk from **2 Dec 2027** if it does emergency triage or insurance risk pricing.

  [SEE]
- **Clinics using a vendor's high-risk AI** are deployers with Art. 26 duties. They will push those duties contractually onto the vendor through logs, instructions for use and oversight design. [PBU]
- The Omnibus buys time but adds no carve-out for medical AI. Predictive clinical AI built today should be designed to the high-risk requirements (data governance under Art. 10, logging, human oversight, accuracy/robustness) because the notified body will check them from Aug 2028. [SEE]

### Gaps
- The final Omnibus text was not opened. Unverified reported elements of the Nov 2025 proposal [PBU] (BK) are:
  - whether Art. 4 AI literacy was converted from an operator duty into a Commission/Member-State promotion duty;
  - a grace period for Art. 50(2) watermarking for systems already on the market;
  - extension of SME relief to small mid-caps;
  - a legal basis for processing special-category data for bias detection;
  - removal of EU-database registration for Art. 6(3) "not high-risk" self-assessments.
- No Romanian AI Act market-surveillance authority designation was verified.
- The final content of MDCG 2025-6 was not reviewed.

---

## 4. European Health Data Space (Regulation (EU) 2025/327)

### Takeaway
The EHDS entered into force on **26 March 2025** and **applies generally from 26 March 2027**. Its main operational obligations bite in **2029** (first priority data categories, EHR-system rules, most secondary-use rules) and **2031** (further categories). Software that qualifies as an **"EHR system"** will need self-certified conformity (essential requirements, CE marking, EU database registration). Wellness apps face labelling rules only if they **claim interoperability with EHR systems**. Secondary use through Health Data Access Bodies will eventually provide a lawful route to data for training and validating predictive models, but not before about 2029. Romania's readiness is unclear.

### Cited Findings
- Published in the OJ on 5 March 2025; **entered into force 26 March 2025**. One source says 25 March. [EST] (snippet) — [Heuking](https://www.heuking.de/en/news-events/newsletter-articles/detail/eu-regulation-on-the-european-health-data-space-ehds-published.html); [noze](https://www.noze.it/en/insights/ehds-regulation-2025-327/)
- **General application from 26 March 2027**, with partial-application dates in Art. 105. [EST] (snippet) — [European Parliament OEIL summary](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1805726); [EU Monitor](https://www.eumonitor.eu/9353000/1/j9vvik7m1c3gyxp/vmlg5gptv7zp)
- **26 March 2031**: extension of interoperability to further categories (imaging, hospital/discharge reports, laboratory results) and further EHR-system obligations. One source cites **2035** for full application to all categories. [SEE for 2031; PBU for 2035] (snippet) — [noze](https://www.noze.it/en/insights/ehds-regulation-2025-327/)
- EHR systems must show conformity with EU technical specifications on interoperability, security and access logging, including an EU declaration of conformity. They must support the European EHR exchange format. [SEE] (snippet) — [PLMJ](https://www.plmj.com/xms/files/NL_European_Health_Data_Space_Regulation.pdf); [fireup.pro](https://fireup.pro/blog/ehds-compliance-healthtech-dach)
- Wellness apps (for example fitness trackers) are subject to labelling and information requirements **if the manufacturer claims interoperability with EHR systems**. [SEE] (snippet) — [fireup.pro](https://fireup.pro/blog/ehds-compliance-healthtech-dach)
- Further structure of the Regulation [SEE] (BK, not re-verified) — [EHDS, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2025/327/oj):
  - **Priority categories.** Group 1 is patient summaries, ePrescriptions and eDispensations. Group 2 is medical images and image reports, lab results and reports, and discharge reports. Group 1 obligations (patient access, MyHealth@EU exchange, EHR-system requirements for these categories) apply from **26 March 2029**. Group 2 obligations apply from **26 March 2031**.
  - **EHR-system definition.** An "EHR system" is software intended by the manufacturer to store, intermediate, import, export, convert, edit or view priority-category data, for use by healthcare providers in patient care or by patients accessing their data.
  - **Manufacturer obligations.** Comply with the Annex II essential requirements, with mandatory **harmonised components**: the European interoperability software component and the European logging software component. Draw up technical documentation and an EU declaration of conformity, affix CE marking, and register in the EU database. This is **self-certification without a notified body**. The Commission adopts common specifications by implementing act.
  - **Devices and AI claiming EHR interoperability.** MDSW and high-risk AI systems that claim interoperability with EHR systems must also meet the harmonised-component requirements.
  - **Secondary use (Chapter IV).**
    - Health Data Access Bodies (HDABs) issue data permits.
    - Allowed purposes include scientific research, innovation activities, and **training, testing and evaluating algorithms, including in medical devices, AI systems and digital health applications**.
    - Prohibited uses include decisions detrimental to individuals, increasing insurance premiums, and advertising.
    - Data are provided in secure processing environments, anonymised by default and pseudonymised only where justified.
    - Individuals have an **opt-out** right from secondary use.
    - Micro-enterprises are, as a rule, exempt from data-holder duties.

### Inferences
- **Patient portal or clinic EMR:** if it stores or displays group 1 or group 2 data for providers or patients, it is likely an "EHR system". From 2029 (group 1) and 2031 (group 2) the founder would have to self-certify against Annex II and integrate the harmonised components. This is a moderate, foreseeable cost (no notified body), comparable to a security-and-interoperability certification project. [PBU]
- **Admin tools** (scheduling, billing, reminders) that do not store or view priority-category clinical data are likely outside the EHR-system definition. [PBU]
- **Wellness apps:** the EHDS burden is optional. It applies only if the app markets "interoperable with EHR". [SEE]
- **Secondary use as the data route for predictive models:** from 2029, a vendor can apply to an HDAB for a data permit to train or validate models. This is the clearest future lawful route to population-scale Romanian or EU data, but it depends on Romania designating and staffing an HDAB and on fees and timelines. Until then, data access must rely on consent or controller partnerships. [SEE for the mechanism; SPEC for Romanian timing]

### Gaps
- The Art. 105 text could not be opened. The precise article-by-article split of 2027/2029/2031 (and any 2034/2035 date) needs checking on EUR-Lex.
- The EHDS implementing acts due by March 2027 (EHR specifications, wellness label format) were not checked for status.
- **Romania's readiness** (HDAB designation, digital health authority, status of the national DES/PIAS, PNRR digital-health investments) was not checked because the search budget was exhausted.

---

## 5. Cybersecurity: NIS2 and Romania's OUG 155/2024, MDR cybersecurity (MDCG 2019-16), what clinics will demand from vendors

### Takeaway
Under NIS2, healthcare providers (medium and large) and medical-device manufacturers (medium and large) are in scope. A solo or micro software vendor is generally **not** an NIS2 entity itself, but will receive **supply-chain security requirements** from in-scope clinics. Romania transposed NIS2 through OUG 155/2024, approved by Legea 124/2025. Registration with DNSC was due around September 2025. MDSW must meet the MDR cybersecurity essential requirements (MDCG 2019-16). The Cyber Resilience Act excludes MDR/IVDR devices but can catch non-device downloadable health software, with reporting duties since 11 Sept 2026.

### Cited Findings
**NIS2 (EU level)**
- Annex I "Health" covers healthcare providers (as defined in Directive 2011/24/EU), EU reference laboratories, R&D of medicinal products, manufacturers of basic pharmaceutical products, and manufacturers of medical devices considered critical in a public-health emergency. Annex II covers manufacturers of medical devices and IVDs. [EST] (BK) — [NIS2 Directive, EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- Size cap: medium (50 or more staff, or above €10M turnover/balance sheet) and large entities are in scope, with limited exceptions. [EST] (BK)
- Art. 21(2)(d) requires in-scope entities to manage supply-chain security, including the security of their direct suppliers. [EST] (BK)
- Art. 23 incident reporting: early warning within 24h, notification within 72h, final report within 1 month. [EST] (BK) — [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)

**Romania**
- OUG 155/2024, approved and amended by **Legea 124/2025**, fully transposes NIS2. A draft order on control and sanctions was published for consultation in **October 2025**; its entry into force was unconfirmed at the time of that briefing. [SEE] (snippet) — [Clifford Chance Badea, Dec 2025](https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2025/12/cc-badea-client-briefing-navigating-nis2.pdf)
- DNSC registration: Order 1/2025 took effect **20 Aug 2025**, with a 30-day registration deadline of about **22 Sept 2025** (one tracker says about 19 Sept). This applies to entities in sectors in Annexes 1–2 of OUG 155/2024, healthcare included. Registration is via the NIS2@RO platform or tool. Late registrants are exposed to sanctions. [SEE] (snippet) — [CMS Romania](https://cms.law/en/rou/legal-updates/romania-launches-orders-to-implement-the-nis2-framework-30-day-registration-deadline-in-effect); [Wolf Theiss](https://www.wolftheiss.com/insights/deadline-approaches-nis2-registration-and-risk-evaluation-in-romania); [risidata](https://www.risidata.com/regulations/nis2/countries/ro)
- One search summary mentioned Romanian notification windows of **6 and 24 hours**. The summary did not make clear which result this came from (the candidates were the CMS, Wolf Theiss and risidata pages above). It is unverified and possibly stricter than NIS2's 24/72h, so it needs checking. [PBU] (snippet) — [Wolf Theiss](https://www.wolftheiss.com/insights/deadline-approaches-nis2-registration-and-risk-evaluation-in-romania); [risidata](https://www.risidata.com/regulations/nis2/countries/ro)

**MDR cybersecurity and the Cyber Resilience Act**
- MDR Annex I GSPR 17.2 (software development per state of the art, including information security), 17.4 (minimum IT/security requirements) and 18.8 (protection against unauthorised access) are elaborated in **MDCG 2019-16** (Dec 2019, rev.1 July 2020). Its topics include security risk management, secure design, an SBOM-like inventory, and post-market vulnerability handling. [EST] (BK) — [MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- Cyber Resilience Act (Reg. 2024/2847) [EST] (BK) — [CRA, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/2847/oj):
  - it does not apply to products covered by the MDR or IVDR;
  - reporting of actively exploited vulnerabilities and severe incidents applies from **11 Sept 2026**;
  - the main obligations apply from **11 Dec 2027**;
  - pure SaaS is largely outside scope unless it is the remote data-processing solution of a product with digital elements.

### Inferences
- **What Romanian clinics and hospitals will typically demand from a vendor**, especially NIS2-registered ones [PBU] (no Romanian procurement source found):
  - an Art. 28 DPA with sub-processor list and EU hosting;
  - a security questionnaire and evidence (ISO 27001 or SOC 2 is often preferred, but not legally required for vendors);
  - incident-notification SLAs fast enough to meet their own NIS2 deadlines;
  - audit rights;
  - access logging, MFA and encryption;
  - business-continuity and backup commitments;
  - vulnerability management;
  - professional or cyber liability insurance.
- For a solo founder, **full ISO 27001 certification is likely unaffordable at first**. A pragmatic path is to align to ISO 27001/NIS2 controls, document them, use certified EU cloud providers, and certify later when a large customer requires it. [SPEC]
- A **downloadable** non-device health app sold in the EU is a "product with digital elements" under the CRA. Vulnerability reporting duties already apply (Sept 2026), and full essential requirements apply from Dec 2027. A web/SaaS-only product reduces CRA exposure. [SEE]

### Gaps
- The text of OUG 155/2024 Annexes was not checked: exactly which health activities are listed, and whether small healthcare providers are pulled in by Romanian-specific criteria.
- The current status of the DNSC sanctions order and Romania's exact notification timelines are unverified.
- No sector-specific Romanian (Ministry of Health or CNAS) security requirements for software vendors were found.

---

## 6. Romania-specific: CNAS systems (SIUI/PIAS, SIPE, CEAS, DES), telemedicine, EMRs and retention, liability for recommendations, occupational health

### Takeaway
Third-party software can and does interface with CNAS's PIAS (SIUI reporting, SIPE e-prescription, CEAS card). CNAS publishes **interface specifications for software producers** (v3.7.32, 7 Apr 2026). Access is through the **provider's** qualified digital certificates. E-prescription applications must be **registered in the CNAS system**. A formal "certification" procedure for vendor software was not confirmed. Integration does **not** give the vendor any data rights: the vendor acts for the provider. Telemedicine has a permanent legal basis: OUG 196/2020 into Legea 95/2006, norms in HG 1133/2022, and OG 2/2026 (from 2 Feb 2026) requiring differentiation by specialty. Implementing norms per specialty were still pending.

### Cited Findings
**CNAS / PIAS integration**
- CNAS publishes "Specificații de interfațare cu PIAS – pentru producătorii de aplicații software". The latest listed is "Interfațare cu SIUI+SIPE+CEAS pentru aplicațiile de raportare ale furnizorilor de servicii medicale și farmaceutice … **v3.7.32 – 07.04.2026**". A GitHub repository (portal-pias/specificatii) is referenced. [SEE] (snippet) — [CNAS PIAS specifications portal](https://portal.cnas.ro/cnas/pias/specificatii); [CNAS SIUI interface spec PDF](https://cnas.ro/wp-content/uploads/2021/10/Specificatie-Interfatare-SIUI-Aplicatii_de_Raportare_pentru_Furnizori.pdf)
- The CNAS SIUI helpdesk provides CNAS's own reporting applications and installation kits for SIUI+SIPE+CEAS. Providers can use these instead of third-party software. [SEE] (snippet) — [CNAS SIUI helpdesk](https://cnas.ro/siui/)
- Each provider registers in SIUI the **digital certificates** its operators use to access SIUI online services. Certificates come from STS-recognised certification authorities. [SEE] (snippet) — [CNAS CAS Dâmbovița procedure](http://www.cnas.ro/casdj/page/procedura-inregistrare-a-certificatului-digital-si-de-deblocare-regenerare-a-cheii-de-activare.html)
- For e-prescriptions, the prescriber or pharmacist needs a qualified digital certificate and "o aplicație informatică dedicată înregistrată în sistemul CNAS". A prescription is "online electronic" when the app can reach SIPE and validate and register it before printing. [SEE] (snippet; secondary source) — [AFSC](https://afsc.ro/reteta-electronica/)
- CNAS issues notices addressed "în atenția dezvoltatorilor de soft pentru aplicații de prescriere și eliberare". For example, on 16 May 2022 it announced validation-schema changes, with rule PHM266 moving from warning to error from 1 June 2022. Vendors must track schema versions. [EST] (snippet) — [CNAS/CAS MB notice 2022-05-16](http://cas.cnas.ro/casmb/post/type/local/2022-05-16-informare-cnas-in-atentia-dezvoltatorilor-de-soft-pentru-aplicatii-de-prescriere-si-elibe.html)
- CNAS made an experimental test environment available to software producers (first installed in 2012). Whether it is still used today is unconfirmed. [PBU] (snippet) — [CNAS e-prescription page](http://siui.casan.ro/cnas/prescriptia_electronica)

**Telemedicine**
- OUG 196/2020 amended Legea 95/2006 and created a general, permanent telemedicine framework. Recognised services include teleconsultation, teleexpertise, telemonitoring, teleradiology, telepathology and teleassistance. [EST] (snippet) — [CMS Romania](https://cms.law/en/rou/legal-updates/romania-permanently-regulates-telemedicine); [Profit.ro](https://www.profit.ro/legal/reglementarea-telemedicinei-in-romania-scurte-consideratii-asupra-potentialelor-provocari-pentru-furnizorii-implicati-22375669)
- The implementing norms are in **HG 1133/2022**. [EST] (snippet) — [Ministry of Health explanatory note](https://ms.ro/media/documents/NOT%C4%82_DE_FUNDAMENTARE_20_ian.pdf); [norms annex copy](https://brcconline.eu/wp-content/uploads/2022/09/Norme-Telemedicina_HGANEXE.pdf)
- CNAS reimbursement norms for telemedicine were made official in **June 2023**, covering remote consultations for **51 specialties**. After the framework contract took effect on 1 July 2023, CNAS said remote consultations and e-prescriptions continue. [SEE] (snippet) — [Wall-Street.ro](https://www.wall-street.ro/articol/Sanatate/289552/lista-serviciilor-medicale-care-pot-fi-realizate-prin-telemedicina-in-romania.html); [Newsweek RO](https://newsweek.ro/sanatate/cojan-cnas-eliberarea-retetelor-in-format-electronic-si-consultatiile-telefonice-se-pastreaza)
- **OG 2/2026** (applicable from **2 Feb 2026**):
  - adds to art. 30^1 of Legea 95/2006 that telemedicine is provided "diferențiat, în funcție de specialitatea medicală și de tipul de serviciu", within the limits of the medical act and patient-safety requirements;
  - introduces art. 30^12, under which the norms will set, per specialty, the permitted telemedicine types, their limits, and **when an in-person consultation is mandatory**;
  - the Senate adopted it on **18 March 2026** with an amendment adding **telerecuperare** (tele-rehabilitation).

  [SEE] (snippet) — [MS draft ordinance](https://www.ms.ro/media/documents/ORDONAN%C8%9AA_completare_Lg_95_din_2006_20_ian.pdf); [Observator News](https://observatornews.ro/sanatate/senatul-a-adoptat-ordonanta-care-prevede-ca-telerecuperarea-devine-parte-din-telemedicina-649146.html); [Avocatnet](https://avocatnet.ro/t17055/telemedicina.html)
- A separate legislative proposal on telemedicine and a national integrated pre-hospital telemedicine system received a CES opinion on 25 Feb 2026. Its adoption is unknown. [PBU] (snippet) — [CES opinion](https://www.ces.ro/newlib/PDF/avize/2026/2.17-b52-PDV-CES-25.02.2026.pdf)

**Liability of medical providers (Legea 95/2006, Title XV)**
- Title XV regulates civil liability of medical personnel and providers (malpraxis) and requires mandatory malpractice insurance. One provision makes healthcare units liable for damage resulting from "acceptarea de echipamente și dispozitive medicale … de la furnizori fără asigurarea prevăzută de lege, precum și subcontractarea de servicii medicale sau nemedicale de la furnizori fără asigurare de răspundere civilă în domeniul medical". [PBU] (BK; article number and wording to verify in the consolidated text) — [Legea 95/2006 on legislatie.just.ro](https://legislatie.just.ro/Public/DetaliiDocument/71139)

### Inferences
- **CNAS integration is feasible for a third-party vendor.** Specs are public and versioned. Expect continuous maintenance as CNAS changes schemas, and possibly an application-registration step for e-prescription. The vendor never gets its own CNAS access; it operates under the provider's certificates and contract. Treat this as a processor activity under Section 1. Technical integration ≠ data access rights. [SEE]
- **Telemedicine platforms:** the regulated actor is the authorised medical provider. A software platform enabling teleconsultations is not itself a telemedicine provider, but must enable the provider to meet confidentiality, identification, consent and record-keeping duties (Legea 46/2003; HG 1133/2022). OG 2/2026's per-specialty norms may change which services can be remote, which is a product-scope risk for telemedicine-centred ideas. [PBU]
- **Liability for recommendations:** the treating physician remains professionally responsible for clinical decisions under the malpraxis regime. The clinic may, however, seek recourse against suppliers, and Title XV links provider liability to supplier insurance. Vendors of anything that touches clinical decisions should expect clinics to demand liability insurance. [PBU]

### Gaps
- No current official CNAS procedure was found for **certifying or registering third-party software** (beyond the e-prescription "registered application" mention), nor any fee or timeline.
- Not checked: how the **DES (Dosarul Electronic de Sănătate)** can be accessed by third parties (likely not via a public API), the status of the CNAS framework contract for 2026, and whether PIAS migration or "PIAS 2.0" projects change integration.
- **Medical-record retention periods** in Romania were not found (search budget exhausted). Romania-specific periods for observation sheets and outpatient records are set through archival nomenclatures under Legea 16/1996 and Ministry of Health orders; consult those before designing retention. Rules on electronic medical records (electronic signature after Legea 214/2024 replaced Legea 455/2001; BK, [PBU]) were also not verified.
- **Occupational health:** the Romanian rules (Legea 319/2006; HG 355/2007 on workers' health surveillance) were not verified in this session. At EU level, Directive 2004/37/EC requires keeping medical records of workers exposed to carcinogens for at least 40 years after exposure ends [SEE] (BK) — [Directive 2004/37/EC](https://eur-lex.europa.eu/eli/dir/2004/37/oj). The practice whereby the employer receives only the aptitude conclusion (fișa de aptitudine), not diagnoses, is BK and [PBU].

---

## 7. Liability: new Product Liability Directive, professional liability, contractual allocation

### Takeaway
From **9 December 2026**, the new PLD (Directive (EU) 2024/2853) makes **software, including AI and SaaS components, a "product" under strict, no-fault liability**. It applies to products placed on the market after that date, or substantially modified after it. It brings disclosure duties and presumptions of defect and causation. Liability toward injured persons **cannot be excluded by contract**. The AI Liability Directive was withdrawn. For a health-software vendor, liability exposure therefore rises sharply exactly when a product starts influencing care.

### Cited Findings
**Scope and timing**
- The PLD was published in the OJ on 18 Nov 2024. Transposition deadline is **9 Dec 2026**, when it replaces Directive 85/374/EEC. It applies to products placed on the market or put into service after 9 Dec 2026. Older products can enter the regime if substantially modified, for example by an extensive software upgrade. [EST] (snippet) — [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive); [Norton Rose Fulbright](https://connections.nortonrosefulbright.com/post/102jpjp/revised-product-liability-directive-introducing-rules-on-strict-liability-for-ai); [Xictron](https://www.xictron.com/en/blog/new-product-liability-law-software-december-2026/)
- Software, whether standalone, embedded, or a service component, falls under strict product liability for the first time. [EST] (snippet) — [Wolf Theiss](https://www.wolftheiss.com/insights/software-digital-products-and-ai-stricter-safety-requirements-on-the-horizon/); [Nemko](https://digital.nemko.com/regulations/eu-product-liability-directive)

**Mechanics relevant to developers**
- Rebuttable presumptions of defect and causation apply where technical complexity makes proof excessively difficult. Courts can order disclosure of evidence. Missed updates or security patches can make a product defective. [SEE] (snippet) — [Norton Rose Fulbright](https://connections.nortonrosefulbright.com/post/102jpjp/revised-product-liability-directive-introducing-rules-on-strict-liability-for-ai); [Xictron](https://www.xictron.com/en/blog/new-product-liability-law-software-december-2026/)
- Further details [EST] (BK) — [PLD, EUR-Lex](https://eur-lex.europa.eu/eli/dir/2024/2853/oj):
  - free and open-source software supplied outside a commercial activity is excluded;
  - compensable damage covers death, personal injury (including medically recognised psychological harm), property, and destruction or corruption of non-professional data;
  - the liability period is 10 years, extended to 25 years for latent personal injury;
  - liability toward the injured person cannot be limited or excluded by contract;
  - component manufacturers can be jointly liable.

**AI Liability Directive and national transposition**
- The AI Liability Directive proposal was withdrawn. Sources differ on the date (Feb 2025 announcement vs. Oct 2025 OJ notice following a 16 July 2025 decision). The PLD is now the main EU civil-liability instrument for AI. [SEE] (snippet) — [Shaping Tomorrow scan, July 2026](https://decision-intel.shapingtomorrow.com/scans/regulation-standards-policy-change/2026-07-06-ex-post-liability-turn/scan.html)
- Transposition is uneven: Germany's bill drew a split expert hearing, and most CEE states were reported as "pre-implementation". [PBU] (snippet) — [Shaping Tomorrow scan](https://decision-intel.shapingtomorrow.com/scans/regulation-standards-policy-change/2026-07-06-ex-post-liability-turn/scan.html)

### Inferences
- **Admin software** is a "product" too. Personal-injury claims are unlikely unless a failure leads to harm (for example, a lost lab result or a missed recall). Clinical-decision or predictive software carries real strict-liability exposure. Budget for product liability and professional indemnity / cyber insurance before any patient-facing or clinical-decision feature. MDR Art. 10(16) already requires financial coverage for devices. [SEE]
- **Contract allocation between vendor and clinic** remains possible: liability caps, indemnities, defined intended use, an "instructions for use" duty on the clinic, and an update-installation duty. These terms cannot bind injured patients. Romanian clinics will likely require supplier insurance because of the Legea 95/2006 Title XV linkage. [PBU]
- **Practical design implications:** keep update logs and versioned releases, maintain security patching (a missed patch can be a defect), document intended use and limitations, and keep a disclosure-ready technical file. [SEE]

### Gaps
- Romania's PLD transposition status (draft law, ministry, timeline) as of Oct 2026 was not found. If transposition is late, the directive's date still governs EU-law interpretation, but national procedure is uncertain. [PBU]
- No Romanian case law on liability of health-software vendors was found.

---

## 8. Synthesis: classifying product ideas into the four categories, cost/complexity, and low-regulation entry points toward predictive healthcare

### Takeaway
In the EU, category (3) "clinical decision-support software" largely **collapses into category (4)**. Patient-specific information used for diagnostic or therapeutic decisions is MDSW of class IIa or higher under Rule 11, and there is no US-style CDS exemption. The realistic low-regulation entry points for a solo founder with €25k are therefore:
- **(1) administrative/workflow tools**, including *operational* (non-clinical) prediction such as capacity or no-show forecasting, with care around health-data profiling under Legea 190 art. 3;
- **(2) wellness software** with disciplined, non-medical claims.

Both are built so the founder accumulates consented data, clinical partnerships and QMS discipline for a later class I/IIa predictive product, timed for 2028–2029, when the AI Act high-risk rules, the MDR reform and EHDS secondary use converge.

### Cited Findings
(Synthesis of Sections 1–7. Underlying sources are cited there.)
- Intended purpose, including promotional material, drives MDR qualification; general-purpose and lifestyle software is excluded — [MDR Art. 2(12), Recital 19](https://eur-lex.europa.eu/eli/reg/2017/745/oj) [EST] (BK)
- Rule 11 makes decision-informing software class IIa or higher; storage, communication and simple search are not MDSW — [MDR Annex VIII](https://eur-lex.europa.eu/eli/reg/2017/745/oj); [MDCG 2019-11 Rev.1 update](https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en) [EST]/[SEE]
- Class IIa: roughly €32–110k and 9–18 months (vendor-blog estimate); notified-body hourly rates of €140–250 — [meddeviceguide](https://meddeviceguide.com/blog/ce-marking-cost-medical-devices-guide); [SIQ](https://www.siq.si/wp-content/uploads/2021/12/MDR-DN021E.pdf) [PBU]/[SEE]
- AI-enabled class IIa+ MDSW is high-risk under the AI Act from 2 Aug 2028 — [Orrick](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes) [SEE]
- Profiling with health data in Romania requires explicit consent or an express legal provision — [Legea 190/2018 art. 3](https://www.dataprotection.ro/servlet/ViewDocument?id=1520) [EST]

### Inferences
**Classification and indicative burden.** Burden is shown as relative tiers. Euro amounts appear only where sourced; everything else is [SPEC].

**(1) Administrative / workflow software**
- **Typical examples:** scheduling and recall (calendar-based), reminders and no-show reduction, CNAS/SIUI reporting and billing helpers, document and consent management, intake forms, occupational-health clinic logistics (exam scheduling, aptitude-certificate expiry tracking), GDPR/NIS2 compliance tooling for clinics, telemedicine scheduling and video infrastructure.
- **Main regimes:**
  - GDPR as **processor** (Art. 28 DPA, Art. 32);
  - Legea 46/2003 confidentiality via the clinic;
  - NIS2 flow-down;
  - PLD from Dec 2026;
  - CRA if downloadable;
  - possibly EHDS "EHR system" rules from 2029/2031 if it stores or views priority clinical data;
  - CNAS spec maintenance if integrated.
- **Validation needs:** none clinical; software QA and security.
- **Burden:** **Low.** Mainly legal templates, security hygiene and EU hosting. [SEE]

**(2) General health / wellness software**
- **Typical examples:** fitness, sleep, stress and generic nutrition coaching; health-literacy content; habit trackers; consumer data vaults.
- **Main regimes:**
  - GDPR as **controller** with explicit consent (Art. 9(2)(a));
  - DPIA;
  - Legea 190 art. 3 if profiling or automated decisions;
  - consumer law;
  - AI Act Art. 50 for chatbots;
  - CRA if downloadable;
  - EHDS label only if it claims EHR interoperability.
- **Validation needs:** none regulatory; claims substantiation under consumer law.
- **Burden:** **Low to medium.** Controller duties and B2C trust. The main risk is **claim creep** into medical purposes. [SEE]

**(3) Clinical decision-support software, non-device subset**
- **Typical examples:** guideline or knowledge lookup ("simple search"), display of data without interpretation, population-level quality dashboards, operational analytics.
- **Main regimes:** as (1), with heavy reliance on precise intended-purpose wording.
- **Validation needs:** usability and correctness; no MDR clinical evaluation if truly non-device.
- **Burden:** **Medium.** Borderline-qualification risk; get a written qualification memo, ideally reviewed by an MDR consultant. [PBU]

**(4) Regulated medical software (MDSW)**
- **Typical examples:** risk calculators for individual patients (SCORE2), triage or symptom checkers, RPM with alerts, predictive or prognostic models for individual patients, AI interpretation.
- **Main regimes:**
  - MDR: class I self-cert (rare under the current Rule 11) or IIa/IIb via a notified body;
  - QMS (ISO 13485), IEC 62304, ISO 14971, IEC 62366-1;
  - clinical evaluation (MDCG 2020-1);
  - PMS and vigilance; EUDAMED; PRRC; liability insurance;
  - AI Act high-risk from 2 Aug 2028 if AI and notified body;
  - Annex III from 2 Dec 2027 for emergency triage;
  - GDPR controller or processor;
  - EHDS harmonised components if it claims EHR interoperability.
- **Validation needs:** valid clinical association, technical and clinical performance; often retrospective validation on local data and sometimes prospective studies.
- **Burden:** **High.** Class IIa is about €32–110k and 9–18 months excluding clinical investigations (estimate). Class I is cheaper but still a QMS-plus-documentation project. [SEE]/[PBU]

**How the same feature changes class through intended use, functionality and claims** [SEE]/[PBU]:
- *"Reminds patients of the follow-up date the doctor set"* is (1). *"Identifies which patients are overdue for screening per guidelines"* is borderline (1)/(4), especially after Rev.1's illness-prevention examples. *"Identifies which patients are at high risk and should be seen sooner"* is (4).
- *"Shows the lab report"* is (1). *"Highlights abnormal values and predicts deterioration"* is (4), possibly under the IVDR.
- *"Tracks your steps and sleep"* is (2). *"Detects arrhythmia / predicts diabetes risk"* is (4).
- *"Forecasts clinic no-shows and capacity"* is (1) under the MDR, because it has no individual medical purpose. Under GDPR, however, it may be **profiling with health data** (Legea 190 art. 3), so it needs explicit consent or an express legal basis, or a design on non-health or aggregated features. [PBU]
- *"Chatbot answering opening hours and booking"* is (1) plus Art. 50 disclosure. *"Chatbot advising whether symptoms need a doctor"* is (4), and potentially Annex III if it does emergency triage.

**Low-regulation entry points that build toward predictive healthcare** [SPEC unless noted]:
1. **Clinic operations software with CNAS integration** (reporting, billing, scheduling and recall). Builds a clinic customer base, a processor-grade compliance stack and an understanding of Romanian data flows. It does not by itself give model-training rights.
2. **Operational prediction** (no-shows, demand, staffing, stock). Real ML without the MDR. GDPR design must avoid health-data profiling, or obtain consent.
3. **Occupational-health clinic logistics.** A recurring, legally mandated workflow (periodic exams) with mostly administrative features. Strict confidentiality applies: the employer must not receive diagnoses (to verify).
4. **Consent-first patient data vault or wellness app** with explicit, granular consent for future research and product development. This is the most direct lawful route to a training dataset that the founder controls.
5. **Research partnerships** with a university hospital (ethics approval, clinic as controller) to retrospectively validate a published score or model. This produces the clinical-evaluation evidence needed later for class I/IIa.
6. **From 2027 to 2029:** watch the MDR Rule 11 reform (possible class I path), prepare AI Act high-risk documentation (Aug 2028), and apply for EHDS secondary-use permits once Romania's HDAB operates (about 2029+).

Two cross-cutting points:
- **Validated scores still need validation.** "Implementing a validated score" does not remove MDR clinical evaluation. The founder must still show correct implementation (technical performance) and clinical performance for the intended population, though literature on the score supports valid clinical association. [SEE] (BK, MDCG 2020-1)
- **Budget reality.** With about €25k and 10–12 h/week, a notified-body route is not feasible as a first product. Category (1)/(2) products with a "regulatory-ready" architecture are feasible: IEC 62304-style documentation discipline, audit logs, versioning and a clear intended-purpose statement. That architecture lowers the later MDR cost. [SPEC]

### Gaps
- No sourced figure was found for the cost of class I MDSW self-certification, ISO 13485 certification for a micro company, or ISO 27001 for a micro vendor in Romania. All non-cited euro or time judgements above are speculative.
- No Romanian regulatory precedent (ANMDMR, ANSPDCP decisions) was found on borderline health software, operational analytics, or no-show prediction.
- **Method limits:** the web-search budget for the session was exhausted midway, and WebFetch was blocked for all primary-source domains tried (EUR-Lex, EC health pages, cms.law, law-firm sites, openregulatory, eumonitor). Many findings therefore rest on search-result summaries or on background knowledge of the legal texts, as labelled. **High-priority items to verify on primary sources:**
  - the Regulation 2026/1744 text (Art. 4, Art. 50 grace periods);
  - EHDS Art. 105;
  - MDCG 2019-11 Rev.1 examples;
  - Decizia ANSPDCP 174/2018 items;
  - the OUG 155/2024 annexes and notification timelines;
  - Romanian medical-record retention rules;
  - the CNAS software registration procedure;
  - Romania's PLD transposition.
