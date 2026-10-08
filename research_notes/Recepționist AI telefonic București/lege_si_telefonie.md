# Legal, regulatory and telecom constraints for an AI phone receptionist for small businesses in Romania (Bucharest), as of October 2026

> Method note: these are research notes, not legal advice. In this environment the egress proxy blocked direct fetching of every primary source I tried (EUR-Lex, dataprotection.ro, ancom.ro, legislatie.just.ro, twilio.com, telnyx.com, orange.ro, twobirds.com, legeaz.net, artificialintelligenceact.eu). **Every finding below therefore comes from WebSearch result snippets and summaries, not from a full read of the page.** The URL given is the page the snippet came from. Where the search summary did not make clear which page a fact came from, I say so. Before relying on any exact wording (statute text, tariffs, dates), check it against the official source.

## 1. GDPR and call recording in Romania (legal basis, notice, ANSPDCP enforcement, voice data, US AI providers and transfers, DPAs)

### Takeaway
Recording inbound calls is lawful in Romania if the business (the controller) is a participant in the call, or records for commercial-evidence purposes under Law 506/2004 art. 4, **and** it meets GDPR: a documented legal basis (usually legitimate interest, or real opt-in consent), a short spoken notice at the start, a full layered privacy notice, retention limits, and an Art. 28 DPA with the agency and every sub-processor. US AI vendors are usable because the EU–US Data Privacy Framework (DPF) is still in force as of September 2026. But the DPF is under real legal and political pressure (CJEU appeal C-703/25 P is pending, and the EDPB asked for a review after *Trump v. Slaughter*), so SCCs and EU-region hosting should be the fallback. Enforcement is manageable rather than a blocker. ANSPDCP's call-related fines have been for failing to answer access requests for recordings, not for recording itself. Fines in 2026 are rising, though, e.g. Orange at €100,000 for security failures.

### Cited Findings
**Romanian telecom and criminal law on recording**
- Law 506/2004 art. 4 ("Confidențialitatea comunicărilor"). Para. (2) prohibits listening to, recording, intercepting or monitoring communications, except (a) by a user who is a participant in the communication, (b) with the participants' prior written consent, or (c) by competent authorities. Para. (4) says the prohibitions do not affect "înregistrări autorizate, în condiţiile legii … în cadrul unor practici profesionale licite, în scopul de a furniza proba unui act comercial sau a unei comunicări realizate în scopuri comerciale". This text was seen via an aggregator snippet, not the official consolidated text. — [legeaz.net – Art. 4 Legea 506/2004](https://legeaz.net/legea-506-2004-prelucrare-date-caracter-personal/articolul-4)
- A secondary legal guide says that under Law 506/2004 any participant in a phone call may record it without notifying the other parties. Recording a conversation you are not part of is a criminal offence under art. 302 of the Criminal Code (violarea secretului corespondenței). — [RecordingLaw – Romania recording laws](https://www.recordinglaw.com/ro/world-laws/world-recording-laws/romania-recording-laws/)
- Romanian press links recording without the parties' agreement to art. 226 of the Criminal Code (violarea vieții private). One legal site gives 6 months to 3 years' imprisonment or a fine for unlawful interception. — [Playtech](https://playtech.ro/?p=703108); [Legal Badger](https://legalbadger.org/stiri/informatii-utile/cand-este-infractiune-daca-inregistrezi-pe-cineva/); [Capital.ro](https://www.capital.ro/inregistrarea-apelurilor-telefonice-violarea-vietii-private-pedepse.html)

**GDPR legal basis and notice**
- A Romanian VoIP provider's GDPR blog says call recording is permitted but must meet GDPR and Law 506/2004 conditions. The usual bases are consent (an IVR notice that the caller accepts by staying on the line) or a documented legitimate interest disclosed in the privacy policy. It says recording without explicit consent is possible with a documented legitimate interest plus an informative privacy policy. — [Voxbee blog – GDPR și înregistrarea convorbirilor](https://voxbee.ro/blog/gdpr-inregistrare-convorbiri)
- Counterpoint: if consent is the basis, it "must be freely given and cannot be assumed through silence or continued participation in the call". Callers must be told that the call is recorded, why, on what legal basis, for how long, and what rights they have. A short spoken warning can be the first layer, with the rest in a linked notice. — [GDPRLocal – GDPR recording calls](https://gdprlocal.com/gdpr-recording-calls/)
- The Danish DPA ruled (2019) that affirmative consent was required where a company recorded customer calls and gave disclosures but no opt-in/opt-out mechanism. — [Ballard Spahr – Denmark DPA on voice recordings](https://www.ballardspahr.com/insights/alerts-and-articles/2019/04/denmark-dpa-rules-on-how-gdpr-applies-to-voice-recordings)
- Real Romanian example: APS Romania's call-centre notice cites consent, legal obligation and legitimate interest together. On inbound calls the caller hears at the start that the call is recorded, and staying on the line is treated as agreement. On outbound calls the announcement comes before identification and agreement is requested. — [APS Romania – Notă de informare call center (PDF)](https://ro.aps-holding.com/data/documents/ro-data-proccessing/Call%20Center_Nota%20de%20informare%20privind%20protectia%20datelor.pdf)
- Searches found **no ANSPDCP or EDPB guideline dedicated to call recording** and **no mandatory Romanian wording** for "această convorbire este înregistrată". This is a negative finding from search summaries.

**ANSPDCP enforcement relevant to calls and voice**
- Vodafone Romania was fined 4,961 lei (about €1,000) in 2023 after refusing a customer's request for recordings of his call-centre conversations. The breach was Art. 15(3) GDPR, because Vodafone could not show it answered the access request within 30 days. The fine was for the access failure, not for recording. — [BizBrașov](https://bizbrasov.ro/2023/06/26/vodafone-amenda-client-convorbiri-call-center/)
- A veterinary clinic was reportedly fined €1,000 after a person asked for access to a phone conversation with an employee and to camera footage. The search summary did not say which page this came from; possibly the [ANSPDCP press release of 16.07.2025](https://www.dataprotection.ro/?page=Comunicat_Presa_16.07.2025), but that attribution is unconfirmed.
- Practitioner advice: when a data subject requests a call recording, edit out the employee's voice before handing it over, because you cannot disclose a third party's data. — [Personal Data Training](https://personaldata.training/ce-facem-cand-ni-se-cer-inregistrari-din-call-center/)
- 2026 fines are larger. In July 2026 ANSPDCP fined Orange România 523,900 lei (€100,000). About €20,000 was for Art. 25(1) (privacy by design) and about €80,000 for Art. 32 security, after a 2025 app incident in which a customer could download other customers' invoices. — [Gadget.ro](https://gadget.ro/orange-romania-a-primit-o-amenda-de-100-000-de-euro-pentru-o-bresa-de-securitate-pe-parte-de-gdpr/); [StartupCafe](https://startupcafe.ro/gdpr-2026-amenda-usturatoare-de-100-000-eur-pentru-orange-motivul-sanctiunii-103524). Earlier in 2026 Orange received a €40,000 fine over erasure requests. — [Profit.ro](https://profit.ro/povesti-cu-profit/it-c/orange-primeste-in-romania-o-amenda-gdpr-de-40-000-euro-speta-cu-o-persoana-care-voia-sa-ia-abonament-21918139)

**Voice data**
- EDPB Guidelines 02/2021 on virtual voice assistants, version 2.0, were adopted on 7 July 2021. — [Digital Policy Alert](https://digitalpolicyalert.org/event/1016-edpb-adopts-guidelines-on-virtual-voice-assistants-vva-version-20)
- Per a law-firm summary of those guidelines: using the voice to *recognise/identify* a user needs explicit consent, and only registered users can give it. Unregistered users should only have their commands executed. Recordings should be deleted as soon as possible, and anonymisation must leave the voice unidentifiable. — [Lexgo – New EDPB guidelines on VVAs](https://www.lexgo.be/en/news-and-articles/10794-new-edpb-guidelines-on-virtual-voice-assistants)
- Romanian Law 190/2018 art. 3(1): processing genetic, biometric or health data "în scopul realizării unui proces decizional automatizat sau pentru crearea de profiluri" is allowed only with the data subject's explicit consent or under express legal provisions. — [Rubinian – Legea 190/2018](https://www.rubinian.com/legea-190-2018-masuri-de-punere-in-aplicare-a-regulamentului-ue-2016-679-gdpr); [ANSPDCP document](https://www.dataprotection.ro/servlet/ViewDocument?id=1520)

**International transfers (US AI and telephony vendors)**
- The General Court upheld the DPF adequacy decision in *Latombe v Commission* (T-553/23, September 2025). Latombe appealed (C-703/25 P, lodged 31 October 2025, limited to points of law, four grounds including the independence of the Data Protection Review Court and bulk collection). — [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework); [EUR-Lex – notice of appeal C-703/25 P](https://eur-lex.europa.eu/eli/C/2025/6610/oj/eng); [Digital Policy Alert](https://digitalpolicyalert.org/event/35459-latombe-filed-appeal-against-general-court-dismissal-of-challenge-to-european-unionunited-states-data-protection-framework-adequacy-decision-in-latombe-v-commission)
- The search summary said no hearing date had been announced as of July 2026 and that the DPF remained in force as of 11 September 2026. These are secondary sources whose dates are inconsistent. — [European MarTech – DPF 2026 status](https://europeanmartech.eu/blog/eu-us-data-privacy-framework-2026-status); [next-levels.de](https://next-levels.de/en/wiki/eu-us-data-privacy-framework)
- In June 2026 the US Supreme Court decided *Trump v. Slaughter* (6–3), upholding presidential removal of FTC commissioners; the FTC is a DPF enforcement body. On 31 July 2026 EDPB Chair Anu Talus asked Commissioner McGrath to assess whether the ruling affects the adequacy decision. Neither the EDPB nor the Commission has told companies to stop using the DPF. — [IAPP](https://iapp.org/news/a/edpb-requests-review-of-eu-us-data-privacy-framework-following-trump-v-slaughter); [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/edpb-calls-for-review-of-eu-u-s-data-privacy-framework-after-u-s-supreme-court-decision-on-ftc-independence); [Faegre Drinker (Sept 2026)](https://www.faegredrinker.com/en/insights/publications/2026/9/trump-v-slaughter-implications-of-the-us-supreme-court-ruling-for-eu-us-data-transfers-and-the-data-privacy-framework)
- noyb reportedly sent the Commission a letter on 30 June 2026 calling for an orderly withdrawal from the DPF. I could not confirm a new lawsuit, and the search summary did not identify the page. — possibly [Corp-Intl](https://corp-intl.com/news/is-the-data-privacy-framework-still-valid). Advisers recommend SCCs alongside DPF reliance as a fallback (same secondary sources).
- **OpenAI:** European data residency for the API has been available since February 2025. It is set per project and only for *new* projects. Requests are processed in Europe with zero data retention. Third-party trackers disagree on whether ZDR is automatic or approval-gated. Nothing found confirms that the Realtime (voice) API is covered. — [OpenAI – Introducing data residency in Europe](https://openai.com/index/introducing-data-residency-in-europe/); [OpenAI Help – Data residency for the API](https://help.openai.com/en/articles/10503543-data-residency-for-the-openai-api)
- **ElevenLabs:** data is stored in the US by default. EU residency is for Enterprise customers only and runs in a separate workspace and API (`api.eu.residency.elevenlabs.io`). Processing may still happen outside the EU (affiliates, sub-processors, moderation) unless Zero Retention Mode is used. Custom LLMs and post-call webhooks can still leave the EU. Its DPA was updated on 8 April 2026 and incorporates the 2021 SCCs. — [ElevenLabs docs – Data residency](https://elevenlabs.io/docs/overview/administration/data-residency); [ElevenLabs blog](https://elevenlabs.io/blog/introducing-european-data-residency); [ElevenLabs DPA](https://elevenlabs.io/zh/dpa)
- **Vapi:** documents an EU region as a separate organisation, with its own dashboard, API and SIP hosts (e.g. `api.eu.vapi.ai`). Support replies conflict on whether all orchestration and media stay in the EU. — [Vapi docs – EU region](https://docs.vapi.ai/security-and-privacy/eu-region); [Vapi support thread](https://support.vapi.ai/t/33109014/eu-vs-us-data-storage-processing)
- **Retell AI:** I found no official documentation of EU hosting. A community post from an EU/NIS2 developer could not get a clear answer. It relays second-hand claims about SCCs, 15-day notice of sub-processor changes and breach notice within 5 business days. — [Retell community](https://community.retellai.com/t/retell-nis2-is-full-eu-data-residency-actually-possible/2541)

**Controller and processor contracts**
- The Romanian College of Physicians (CMR) GDPR guide gives a model confidentiality/processing agreement. It binds processors (IT firms, couriers) to GDPR arts. 5, 28 and 32 and names the clinic as controller. — [CMR – Anexa 2 model acord împuterniciți (PDF)](https://gdpr.cmr.ro/wp-content/uploads/2023/07/Anexa-2_Model-de-Acord-de-confidentialitate-in-relatie-cu-colaboratorii-persoane-imputernicite.pdf)
- GDPR Art. 28 requires a written contract with each processor. It must cover documented instructions, confidentiality, Art. 32 security, sub-processor authorisation and flow-down, help with data subject rights and DPIAs, deletion or return at the end, and audits. This comes from my knowledge of the regulation text, not fetched this session. — [EUR-Lex – GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

### Inferences
- **Roles.** The business (clinic, salon, service firm) is the controller. The agency running the AI receptionist is the processor. Vapi/Retell, OpenAI, ElevenLabs, Twilio/Telnyx and the STT vendor are sub-processors. The agency needs (a) a DPA with each client, (b) the vendors' DPAs accepted, and (c) a sub-processor list the client has authorised. Templates should be ready before selling.
- **Legal basis.** Legitimate interest (dispute evidence, quality, building the appointment record) plus a clear spoken notice is the realistic basis for SMB inbound calls. Do not rely on "staying on the line = consent". If consent is used, offer a real way to decline, e.g. "say 'fără înregistrare'" with transcript-only or no-retention mode. A suggested opening line: "Bună ziua, ați sunat la [Firma]. Sunt asistentul virtual bazat pe inteligență artificială al [Firma]. Convorbirea este înregistrată și transcrisă pentru gestionarea programării; detalii la [site]/gdpr." This one line covers both the AI Act and GDPR first-layer notice.
- **Law 506 art. 4.** The AI agent answers *on behalf of* the business, which is a participant, and para. (4) adds a commercial-evidence route. Recording by the business's own system should not be unlawful interception. This is my interpretation; no ANSPDCP or court guidance was found.
- **Voice is not biometric by default.** Plain recording and transcription is not "biometric data" unless the voice is used to identify the speaker. Avoid voice-ID or caller voiceprints, which trigger Art. 9, explicit consent and Law 190/2018 art. 3.
- **Practical risk** is access requests (callers asking for their recording), breaches and over-retention, not the act of recording. The system must be able to find, export and redact a caller's recording within 30 days.
- **Transfers** are manageable today (DPF plus SCCs). EU-region options (OpenAI EU project, ElevenLabs EU, Vapi EU) reduce exposure if the DPF falls. The DPF is a medium-term risk to track, not a current blocker.

### Gaps
- I could not verify the consolidated official text of Law 506/2004 art. 4 on legislatie.just.ro, or whether para. (4) needs a separate "authorisation".
- I found no ANSPDCP decision that fined a company *for recording* calls without proper notice.
- Twilio's and Telnyx's DPF certification status and Romania-specific DPA terms were not confirmed (sites blocked).
- I found no confirmation of OpenAI Realtime API eligibility for EU residency or ZDR.

## 2. EU AI Act Article 50: disclosing that the caller is talking to an AI

### Takeaway
Since **2 August 2026**, an AI phone receptionist must tell callers clearly that they are talking to an AI, at the latest at the first interaction. For voice, that means a spoken statement at the start of the call, with reminders in long calls; tones or a "virtual assistant" label are not enough. The Digital Omnibus (Reg. (EU) 2026/1744, in force 27 July 2026) did **not** postpone this. It only gave already-marketed systems until 2 December 2026 for the Art. 50(2) machine-readable marking duty. Fines go up to €15M or 3% of turnover. In Romania, ANCOM was named market-surveillance authority only by a government memorandum (12 March 2026). The national law that would give it sanction powers was still being drafted in September 2026. The duty applies directly anyway.

### Cited Findings
- Art. 50 applies from 2 August 2026, and the duty to tell users they are interacting with an AI was not postponed by the Omnibus. — [AI Act Blog NL](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026); [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/)
- The Digital Omnibus on AI is Regulation (EU) 2026/1744, dated 8 July 2026, published in the OJ on 24 July 2026 and in force from 27 July 2026. Provisional agreement came on 7 May 2026 and Council approval on 29 June 2026. These details come from law-firm summaries; I did not see the OJ text. — [Lewis Silkin](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo); [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force); [FASI](https://fasi.eu/en/articles/news/29051-digital-omnibus-package.html)
- High-risk deadlines moved: Annex III to 2 December 2027 and Annex I to 2 August 2028. — [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- Art. 50(2) marking of synthetic audio, image, video and text: systems placed on the market before 2 August 2026 have until 2 December 2026. — [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article50-watermarking-deadline/)
- Commission Art. 50 guidelines C(2026) 5054 final are dated 20 July 2026. The Commission communication says formal adoption will follow once all language versions exist, and the guidelines apply only from then. Bird & Bird and others describe them as the adopted final version. — [Commission Communication 20 July 2026 (PDF via dirittobancario)](https://www.dirittobancario.it/wp-content/uploads/2026/07/Communication-European-Commission-20-July-2026.pdf); [Bird & Bird](https://www.twobirds.com/en/insights/2026/european-commission-adopts-final-guidelines-on-ai-act-article-50-transparency-obligations-first-impr); [Digital Policy Alert](https://digitalpolicyalert.org/event/41927-european-commission-released-guidelines-on-the-implementation-of-the-transparency-obligations-for-certain-ai-systems-under-article-50-of-ai-act)
- The transparency Code of Practice, on marking and labelling AI content, was published on 10 June 2026. It is voluntary and the Commission confirmed it as adequate. It covers Art. 50(2)/(4) marking and labelling, not the interaction disclosure. — [Faegre Drinker](https://www.faegredrinker.com/en/insights/publications/2026/7/eu-ai-act-commission-confirms-transparency-code-of-practice-as-adequate-and-publishes-final-version-of-its-guidelines-on-transparency-obligations); [Reed Smith](https://www.reedsmith.com/our-insights/blogs/viewpoints/102nbz0/transparency-obligations-for-ai-generated-content-the-code-of-practice-adequacy/)
- Telephony specifics, as relayed by compliance and vendor blogs summarising the guidelines (I could not identify which blog quoted which line):
  - The guidelines call for "explicit spoken statements at the beginning of the interaction, combined, as appropriate, with periodic reminders in longer interactions, in particular in case of interruptions or a change of the role of the AI system".
  - Tones alone are not enough.
  - The disclosure must be clear and given at the latest at the first interaction.
  - A disclosure buried in T&Cs, machine-readable only, or generic does not count, and the label "virtual assistant" alone is insufficient.
  - The "obvious" exception is narrow and judged by the average-consumer standard, taking vulnerable groups into account. It does not cover public-facing helpdesk bots.
  - AI agents must disclose both that they are artificial and on whose behalf they act.
  - Sources: [Disclo.eu](https://disclo.eu/blog/ai-voice-agent-article-50-disclosure); [Famulor](https://www.famulor.io/blog/eu-ai-act-article-50-what-your-ai-phone-agent-must-say); [DILR](https://www.dilr.ai/blog/ai-voice-disclosure-compliance-eu-ai-act-article-50); [Justas Butkus](https://justasbutkus.com/eu-ai-act/voice-agent-disclosure/)
- Art. 50(1) places the design duty on the *provider*; deployers carry Art. 50(3)/(4). Someone who ships a white-label bot under their own name becomes a provider under Art. 25. If the system imitates a real person's voice, the Art. 50(4) deep-fake disclosure applies; synthetic audio also triggers Art. 50(2) marking. — [Blck Alpaca](https://blckalpaca.at/en/knowledge-base/ai-agents/eu-ai-act-for-ai-agents/article-50-for-chatbots-and-ai-agents-what-you-must-disclose); [William Fry](https://www.williamfry.com/knowledge/part-1-ai-act-articles-501-and-502-transparency-obligations/)
- Penalties: breaches of Art. 50 fall under Art. 99 (up to €15 million or 3% of worldwide annual turnover, whichever is higher). — [Softcery](https://softcery.com/lab/eu-voice-ai-regulations-founders-guide); [Justas Butkus](https://justasbutkus.com/eu-ai-act/voice-agent-disclosure/). From my knowledge of the Act, not fetched: for SMEs and start-ups Art. 99(6) applies the *lower* of the two amounts.
- **Romania.** A government memorandum of 12 March 2026 names:
  - ANCOM as market-surveillance authority and single point of contact
  - ADR (Autoritatea pentru Digitalizarea României) as notifying authority
  - ANSPDCP for certain high-risk biometric uses
  - ASF and BNR for the financial sector

  Romania missed the EU designation deadline of 2 August 2025. — [Capital.ro](https://www.capital.ro/regulamentul-european-privind-ai-intra-in-aplicare-din-2-august-ancom-va-coordona-supravegherea-in-romania.html); [Money.ro](https://www.money.ro/stiri/romania-pregateste-legea-pentru-inteligenta-artificiala-ancom-va-supraveghea-pia-ms2xace6); [Edupedu](https://www.edupedu.ro/romania-ramane-fara-autoritate-desemnata-pentru-ai-act-in-timp-ce-alte-state-ue-au-deja-sanctiuni-operationale/)
- The memorandum gives no control or sanction powers. ANCOM said on 24 July 2026 that the national act (authorities, cooperation, sanctions) was still being drafted. Bursa reported on 4 August 2026 that the authorities cannot yet impose sanctions. A parliamentary question of 14 September 2026 (A/PNL/539, deputy Sebastian Burduja) presses ANCOM on the missing sanction mechanism. — [Bursa.ro](https://www.bursa.ro/ai-act-lege-europeana-fara-8222dinti8221-in-romania-autoritatile-nu-pot-aplica-sanctiuni-inca-06767950); [Camera Deputaților – interpelare (PDF)](https://www.cdep.ro/interpel/2026/i6258A.pdf)
- The Regulation applies directly, so companies cannot wait for the Romanian law before complying. — [Economica.net – ANCOM](https://www.economica.net/ancom-anunta-ca-regulamentul-ue-privind-inteligenta-artificiala-trebuie-pus-in-aplicare-de-romania-incepand-cu-data-de-2-august_962288.html)

### Inferences
- **Who is the provider.** An agency that configures a Vapi/Retell agent and sells it under its own brand to clinics is most likely the "provider" of that AI system (or becomes one under Art. 25). The client business is the deployer. The agency should build the disclosure into every agent by default and make it impossible for clients to switch off.
- **Concrete compliance.** Use a fixed Romanian greeting stating (1) AI nature and (2) whose behalf, e.g. "Sunt asistentul virtual AI al Clinicii X". Repeat it on transfer or hand-off and when asked "vorbesc cu un om?". Never claim to be human. Log that the greeting played.
- **Synthetic voice.** Real-time synthetic speech is "AI-generated audio". The Art. 50(2) marking duty sits with the TTS/model provider (ElevenLabs, OpenAI), and from 2 December 2026 at the latest. The agency should check its vendors' marking support. Do not clone a real person's voice (e.g. the clinic owner's) without consent and explicit deep-fake disclosure.
- **Enforcement.** Romanian administrative enforcement is not yet operational (no sanction law as of September 2026). That is not a reason to skip compliance: the duty is directly applicable, and the national law could arrive at any time. Disclosure costs almost nothing, so this is a **manageable requirement, not a blocker**.

### Gaps
- I could not read the official guideline text C(2026) 5054, so the telephony wording above is second-hand.
- I could not confirm whether the guidelines have been formally adopted in all languages by October 2026.
- I found no Romanian draft AI law text, so national penalty levels are unknown.

## 3. Health data: dental and medical clinics

### Takeaway
Any appointment data that can reveal health (the specialty, symptoms, "durere de măsea", a treatment type) is GDPR Art. 9 health data. A clinic can process it for care and appointment management under Art. 9(2)(h), but only under professional-secrecy safeguards (Art. 9(3)) and Romanian patient-confidentiality law (Law 46/2003). This is **manageable** with three safeguards:
- a strong DPA plus confidentiality undertakings
- data minimisation: the AI books slots and records only a short reason, with no triage or diagnosis
- EU-hosted, short-retention processing and a DPIA

It becomes high-risk if the AI makes automated triage decisions, which need explicit consent under Romanian Law 190/2018 art. 3. A **potential blocker** is any vendor that uses call audio or transcripts for its own model training.

### Cited Findings
- Art. 9(2)(h) covers processing needed for preventive medicine, diagnosis and provision of care, on the basis of law or a contract with a health professional. Art. 9(3) requires the processing to be done by, or under the responsibility of, someone bound by professional secrecy. A frequent error is relying on (h) for staff who are not bound to secrecy. The CJEU reads "health data" broadly: data merely capable of revealing health status is caught. — [Legiscope – Health data, Art. 9](https://www.legiscope.com/blog/health-data-article-9-gdpr.html)
- Law 46/2003 on patient rights, arts. 21–22: information on a patient's condition, diagnosis, treatment and personal data is confidential, even after death. It may be disclosed only with the patient's explicit consent or where the law expressly requires it. Art. 23: consent is not needed for disclosure to other accredited providers involved in treatment. Art. 24: the patient has access to their medical data. — [Ministerul Sănătății – Notă de fundamentare](https://audit.ms.ro/media/documents/NF-03.02.2023.doc); [Legea 46/2003 (PDF, Spitalul Sf. Spiridon)](https://www.spitalspiridon.ro/docs/2024/Legislatie/LEGEA%20drepturilor%20pacientului%20nr.%2046%20din%2021%20ianuarie%202003.pdf)
- The CMR guide names the clinic as controller and IT or other service firms as processors bound by GDPR arts. 5, 28 and 32. — [CMR GDPR Guide (PDF)](https://gdpr.cmr.ro/wp-content/uploads/2023/09/GhidCMR.pdf); [CMR Anexa 2](https://gdpr.cmr.ro/wp-content/uploads/2023/07/Anexa-2_Model-de-Acord-de-confidentialitate-in-relatie-cu-colaboratorii-persoane-imputernicite.pdf)
- Law 190/2018 art. 3(1): health data used for automated decision-making or profiling requires explicit consent or an express legal basis. — [Rubinian](https://www.rubinian.com/legea-190-2018-masuri-de-punere-in-aplicare-a-regulamentului-ue-2016-679-gdpr)
- ANSPDCP fines in the medical and dental sector, per legal-news summaries. Exact attribution per case is uncertain because pages were not readable.
  - **March 2025:** a dental clinic was fined €1,000 for refusing a patient access to their own medical file.
  - **August 2025:** a clinic's patient and staff data ended up online after an employee's backup to a personal hard disk.
  - **February 2026:** a dental practice was sanctioned for not giving inspectors the information they requested.
  - **Date not shown:** MedLife was fined 14,755.50 lei (€3,000) and Centrul Medical dr. Furtuna Dan 4,918.50 lei, both for security failures.
  - Sources: [e-juridic – policlinică amendată](https://e-juridic.manager.ro/articole/policlinica-amendata-pentru-incalcarea-gdpr-28543.html); [e-juridic – centre medicale private amendate (WhatsApp/e-mail)](https://e-juridic.manager.ro/articole/centre-medicale-private-amendate-pentru-incalcarea-gdpr-datele-pacientilor-divulgate-fara-drept-pe-whatsapp-sau-prin-e-mail-29342.html); [Avocatnet – ANSPDCP](https://www.avocatnet.ro/t15633/anspdcp.html)
- Vendor marketing cites HIPAA and SOC 2 (Retell, Vapi). These are US frameworks and do not establish GDPR compliance. — [andrew.ooo ranking (Apr 2026)](https://andrew.ooo/answers/best-ai-voice-agent-platforms-april-2026/); [Vapi changelog summary](https://aitoolsatlas.ai/tools/vapi-ai/changelog)

### Inferences
- **Scope the AI to booking, not triage.** Collect name, phone, preferred slot, doctor or service, and an optional short reason. Avoid detailed symptom intake. Do not let the AI decide urgency or refuse care. That keeps processing under 9(2)(h) and avoids Law 190/2018 art. 3 and GDPR Art. 22. For an emergency, play a fixed message: "pentru urgențe sunați la 112". The AI does not assess the emergency.
- **Professional secrecy.** The agency and its staff should sign confidentiality undertakings (CMR model). Transcripts should be accessible only to the clinic. Vendors must contractually commit to no training on the data and to minimal retention (ZDR/EU modes).
- **DPIA.** Systematic processing of health data with new technology (AI, voice) is a classic DPIA trigger (Art. 35). The clinic, as controller, should hold a DPIA, and the agency can supply a template. ANSPDCP's national DPIA list was not checked; see Gaps.
- **Notice wording for clinics** should mention that call content may include health information and that it is used only to manage the appointment.

### Gaps
- I did not find ANSPDCP's list of processing operations requiring a DPIA (ANSPDCP Decision 174/2018, from my background knowledge) or any ANSPDCP guidance on clinic appointment handling.
- I did not find any Romanian rule specific to medical appointment-booking channels (e.g. CMR or Ministry of Health rules on phone booking or AI). The avocatnet page mentions an amendment obliging doctors to schedule follow-up investigations, but I could not verify it.
- I found no CMSR (dentists' college) guidance.

## 4. Outbound calls: what is not allowed

### Takeaway
Under Law 506/2004 art. 12, automated calling systems that need no human operator may **not** be used for commercial communications without the recipient's *prior* consent; ANSPDCP has demanded "express and unequivocal" consent. So outbound AI marketing calls, offers or reactivation campaigns to people who have not opted in are effectively prohibited. The safe position is inbound-only. Appointment reminders are a grey zone: arguably transactional rather than commercial, but still needing a GDPR basis and preferably consent captured at booking. ANCOM's anti-spoofing blocking also means outbound calls must use a number legitimately held on the carrier that sends them.

### Cited Findings
- Art. 12 Law 506/2004 prohibits "efectuarea de comunicări comerciale prin utilizarea unor sisteme automate de apelare care nu necesită intervenția unui operator uman", by fax, e-mail or any other method using public electronic communications services, unless the recipient has given prior consent. A customer's e-mail obtained at the point of sale may be used for similar products with an easy, free opt-out. The text is as quoted in press and ANSPDCP releases; I did not verify the official consolidated text. — [Avocatnet – Vodafone amendată 7.000 lei](https://www.avocatnet.ro/articol_14849/Vodafone-Romania-amendata-contraventional-cu-7000-lei-pentru-mesaje-de-tip-spam.html); [Avocatnet – Orange amendată 5.000 lei](https://www.avocatnet.ro/articol_15269/Orange-amendata-cu-5000-lei-pentru-mesaje-comerciale-nesolicitate.html)
- In the Orange case (2009), ANSPDCP said Orange had sent commercial communications "fără … să fi obținut, în prealabil, consimțământul expres și neechivoc". These fines are old (2009) and the current fine ceilings were not found. — [Avocatnet – Orange](https://www.avocatnet.ro/articol_15269/Orange-amendata-cu-5000-lei-pentru-mesaje-comerciale-nesolicitate.html)
- Recent ANSPDCP marketing-related fines were under GDPR, not Law 506:
  - Whitedecor SRL: 5,082 lei (€1,000), October 2025, unsolicited commercial SMS. — [Alba24](https://alba24.ro/amenda-pentru-o-firma-care-a-transmis-sms-uri-nesolicitate-catre-clienti-spam-cu-oferte-pe-telefon-1107033.html)
  - A firm fined €2,000 "pentru SMS-uri și apeluri telefonice", its second sanction in a few months (headline only). — [StartupCafe](https://startupcafe.ro/gdpr-romania-o-firma-a-primit-o-amenda-de-2-000-eur-pentru-sms-uri-si-apeluri-telefonice-a-doua-sanctiune-in-cateva-luni-106406)
- ANCOM anti-spoofing. Operators were told to block calls arriving from abroad that display Romanian numbers (start date 7 July 2025). A decision reported on 8 October 2025 targets fixed-number spoofing, with calls stopped in the network before they reach the recipient. Mobile numbers are excluded because of legitimate roaming. Exceptions apply where the operator can verify legitimate use, e.g. roaming or calls *redirected to a national number*. — [Spotmedia](https://spotmedia.ro/stiri/eveniment/gata-cu-apelurile-false-din-strainatate-care-afiseaza-numere-romanesti-ancom-le-blocheaza); [Profit.ro](https://profit.ro/povesti-cu-profit/it-c/decizie-furnizorii-de-telefonie-vor-putea-bloca-apelurile-din-afara-romaniei-ce-afiseaza-numere-nationale-false-22056862); [Euronews România](https://www.euronews.ro/articole/ancom-blocheaza-apelurile-false-din-strainatate-care-par-a-veni-din-romania); [Puterea.ro](https://www.puterea.ro/?p=528253)
- Twilio's Romania voice guidance, per the search snippet: calls showing non-Twilio Romanian numbers as caller ID are not permitted, and customers should use Twilio numbers for domestic calls. ANCOM has enforced measures against CLI spoofing. Calls to Romanian emergency services over Twilio are not allowed. — [Twilio – Romania voice guidelines](https://www.twilio.com/en-us/guidelines/ro/voice)

### Inferences
- **Not allowed without prior opt-in:** AI-voice promotional calls, win-back campaigns, "we have a discount" calls, or automated surveys with a sales element, to anyone. This applies to existing customers too; the "similar products" exception quoted is for e-mail.
- **Grey zone (needs opt-in and legal review):** automated appointment-reminder or confirmation calls. They are probably not "comunicări comerciale" if purely service-related. Still, capture explicit agreement at booking ("Doriți să vă sunăm/trimitem SMS de confirmare?"), keep them strictly transactional, and give an opt-out. SMS reminders are lower-risk than AI voice calls.
- **Allowed:** inbound answering, and calling back a person who asked for a call-back during their inbound call (documented request).
- **Technical:** any outbound or call-back calls must present a number the business or provider actually holds on the originating carrier, e.g. a Twilio/Telnyx-hosted Romanian number. Spoofing the clinic's Orange mobile number from a foreign platform is likely to be blocked and is non-compliant.

### Gaps
- I did not obtain the official current text of art. 12 or the fine levels in art. 13 of Law 506/2004 as amended.
- I could not confirm which authority (ANSPDCP or ANCOM) handles human-operator telemarketing complaints.
- I found no Romanian guidance on whether automated reminder calls count as "commercial communications".
- I could not confirm whether Romania has a national do-not-call (Robinson) register.

## 5. Telecom: connecting an AI agent to a Romanian business number

### Takeaway
There are three realistic architectures:
- **(A) Conditional call forwarding** from the business's existing mobile or fixed line to a Romanian DID hosted at Twilio, Telnyx or a local SIP provider and connected to Vapi/Retell. This is cheapest to set up, but Orange charges about €0.17/min + VAT for each forwarded minute outside its network, prepaid lines can't forward, and forwarding to *international* numbers is not available. So the target must be a **Romanian** number.
- **(B) Port the business number** (or get a new 021/031 number) to a SIP provider and point it at the AI platform's SIP endpoint.
- **(C) Use the business's existing PBX or SIP trunk**, e.g. Orange Business, and route overflow or after-hours calls via SIP.

Foreign CPaaS providers do sell Romanian numbers, but with KYC: a Romanian address with proof and company registration. Telnyx requires the end-user to be physically in Romania, and its advertised local inventory is in provincial 03xx ranges rather than Bucharest. None of this is a blocker, but number provisioning and forwarding cost are real friction.

### Cited Findings
**Operator forwarding**
- **Orange:** forwarding is set via phone settings or My Orange (Servicii › Redirecționare apeluri). Calls forwarded outside the Orange network do not use bundle minutes and are charged from the first minute at the standard off-net rate of €0.17/min excl. VAT. Calls forwarded to Orange numbers use the bundle. Forwarding is not available on PrePay, and forwarding to international numbers is not available. The date of the tariff page is unclear. — [Orange Help – Cât costă redirecționarea apelurilor](https://www.orange.ro/help/cat-costa-redirectionarea-apelurilor-99); [Orange Help – Cum redirecționez un apel](https://www.orange.ro/help/cum-redirectionez-un-apel-98); [Orange Help – coduri de rețea](https://www.orange.ro/help/arhiva/abonamente/cum-imi-redirectionez-apelurile-de-pe-numarul-meu-de-abonament-orange-pe-alt-numar-de-telefon-utilizand-coduri-de-retea-85364)
- **Vodafone:** forum users say forwarding to another number is charged and works only on subscriptions (postpaid), not prepaid. No official per-minute rate was found. — [Softpedia forum – redirecționare Vodafone](https://forum.softpedia.com/topic/916792-redirectionare-apeluri-vodafone-abonament/)
- **Digi / Vodafone / Telekom:** a 2023 forum commenter claims national forwarding is free on Vodafone, Digi and Telekom. Another says forwarding to another number is generally paid and only voicemail is free. Both claims are anecdotal and unverified. — [Softpedia forum – redirecționare apeluri](https://forum.softpedia.com/topic/1223714-redirecionare-apeluri/)
- **GSM codes:** Digi's *Spanish* service documents **21*number# for unconditional forwarding and **61*number# for no-answer. I found no Romanian operator page confirming codes. — [Selectra.es – Digi desvío de llamadas](https://selectra.es/internet-telefono/companias/digi-mobil/desvio-llamadas)
- **Telekom Romania Mobile no longer exists as an independent operator.** On 1 October 2025 Vodafone took postpaid and business customers and Digi took prepaid, spectrum and towers. Prepaid migration to Digi started 27 October 2025, and unmigrated prepaid numbers were to be disconnected from 7 May 2026. The Vodafone–Telekom legal merger was scheduled for 30 June 2026 and reported completed. — [G4Media](https://www.g4media.ro/telekom-romania-mobile-communications-a-devenit-din-1-octombrie-subsidiara-detinuta-majoritar-de-vodafone-romania.html); [Capital.ro](https://www.capital.ro/vodafone-romania-a-preluat-telekom-mobile-ce-se-schimba-pentru-clientii-cu-abonament-si-cei-de-business.html); [StartupCafe](https://startupcafe.ro/vodafone-romania-fuziune-telekom-final-iunie-2026-100338); [Gadget.ro](https://gadget.ro/?p=366599)

**Romanian numbers from CPaaS and VoIP providers**
- **Twilio:**
  - Regulatory requirements for Romania: for local numbers, the address must be within the locality or region of the number's prefix, and a PO Box is not acceptable.
  - Proof of address: government ID with the local address, a utility bill, tax notice, rent receipt or title deed.
  - Businesses: trade registry certificate, fiscal/VAT certificate or registry excerpt.
  - Without this information there is "a high risk the local regulators or carriers will disconnect the phone number".
  - Twilio's English (US) version is looser for businesses: the business address must be in Romania.
  - A missing address causes error 21615.
  - Sources: [Twilio – Romania regulatory guidelines](https://www.twilio.com/en-us/guidelines/ro/regulatory); [Twilio error 21615](https://static0.twilio.com/docs/api/errors/21615)
- Twilio added Romania documentation requirements in April 2019 and requirements for Romanian *national* numbers in May 2021. — [Twilio – Regulatory changelog](https://www.twilio.com/docs/phone-numbers/regulatory/changelog)
- **Twilio porting:** non-geographic numbers (+40 37) are listed as portable. A port needs a letter of authorisation dated within 90 days, a bill from the last 30 days and an ID copy, and takes 2–4 weeks. Most such numbers are voice-only; two-way SMS is not supported. — [Twilio – Romania porting](https://www.twilio.com/en-us/guidelines/ro/porting); [Twilio – Romania SMS](https://www.twilio.com/en-us/guidelines/ro/sms)
- **Telnyx:**
  - Local, national and toll-free numbers all need the same documents:
    - individuals: name, phone, ID or passport
    - businesses: authorised representative and company registration certificate
    - both: a Romanian street address with proof dated within 3 months
  - The end-user must be physically present in Romania when purchasing.
  - Advertised inventory: 250+ local numbers each in Arad (357), Dolj (351), Covasna (367), Harghita (366) and Mehedinți (352). No Bucharest range appeared in the snippet.
  - Telnyx's October 2023 Romania launch included calling, fax, porting and 112 access.
  - Sources: [Telnyx – Romania DID requirements](https://support.telnyx.com/en/articles/3739552-romania-did-requirements); [Telnyx – Romania numbers](https://telnyx.com/phone-numbers/romania); [Telnyx release notes – Romania PSTN replacement](https://telnyx.com/release-notes/romania-pstn-replacement)
- **Other resellers:**
  - Zadarma: Mehedinți +40 352 number at $0 setup and $2/month, with incoming calls free. — [Zadarma – numbers Romania/Mehedinți](https://zadarma.com/en/tariffs/numbers/romania/mehedinti)
  - Zernio: local $3/month, national $5/month, toll-free $30/month, with ID and proof of address within 3 months. — [Zernio](https://zernio.com/phone-numbers/romania)
  - DIDWW: country-specific verification by its compliance team. — [DIDWW regulation docs](https://doc.didww.com/api3/2026-04-16/regulation-resources/index.html)
  - Symbo: Romania numbers are not self-serve. — [Symbo – Romania DID requirements](https://help.symbo.ai/en/articles/10404537-romania-did-requirements)
- **Local SIP and enterprise options:** Orange Business offers SIP trunking for fixed voice (10–500 concurrent calls). — [Orange Business – voce fixă SIP](https://www.orange.ro/business/colaborare/voce-fixa-sip-tdm); [Orange Wholesale – SIP trunking](https://www.orange.ro/wholesale/sip-trunking)
- A third-party guide lists other Bucharest VoIP/SIP providers: Iristel România, ClickPhone, Voxbee and Optivoice (Opticom). I could not verify the details or prices. — [Oki-Toki blog (third-party)](https://tst.oki-toki.net/blog/sip-telefoniya-gde-kupit-sip-nomer-dlya-rumynii); [Voxbee](https://voxbee.ro/blog/gdpr-inregistrare-convorbiri)
- **AI platform SIP:** Vapi's EU region has its own SIP host, separate from the US region. The API key, endpoints and SIP host must be in the same region. — [Vapi docs – EU region](https://docs.vapi.ai/security-and-privacy/eu-region)

**ANCOM numbering rules**
- The National Numbering Plan (PNN) is ANCOM President's Decision 375/2013, amended among others by 1069/2018 and 71/2023. — [ANCOM – Decizia 375/2013 consolidată (PDF)](https://www.ancom.ro/uploads/forms_files/Decizia_ANCOM_Nr_375_2013_Consolidata_15_feb_20231702643537.pdf)
- A 2018 ANCOM decision allows 9-digit geographic numbers (e.g. 021/031) to be used outside their original area, including after porting. Offering this is optional for providers and requires technical changes. — [Profit.ro](https://profit.ro/stiri/ancom-propune-pastrarea-numarului-de-telefon-fix-si-la-portarea-dintr-un-judet-in-altul-de-cand-va-fi-valabil-18242156); [Infocons](https://infocons.ro/ancom-propune-pastrarea-numarului-de-telefon-fix-si-la-portarea-dintr-un-judet-in-altul/)
- The search summary said the PNN maps "21" to Bucharest and "31" to Ilfov, which looks garbled. My understanding is that both 021 and 031 serve Bucharest–Ilfov, with 02x historically for the incumbent and 03x for alternative operators. — [ANCOM PNN consolidat](https://www.ancom.ro/uploads/forms_files/Decizia_ANCOM_Nr_375_2013_Consolidata_15_feb_20231702643537.pdf)

**Latency**
- Retell markets about 600 ms voice-to-voice latency. — [andrew.ooo (Apr 2026)](https://andrew.ooo/answers/best-ai-voice-agent-platforms-april-2026/)

### Inferences
- **Forwarding target must be a Romanian number.** Orange does not forward to international numbers, so you cannot forward straight to a US Twilio number. Use a Romanian DID (Twilio, Telnyx, Zadarma, DIDWW, or a local SIP provider) connected by SIP to Vapi or Retell.
- **Forwarding cost** is the hidden cost driver. At €0.17/min + 19% VAT (Orange off-net), 500 forwarded minutes a month is about €101 including VAT, billed by Orange to the client on top of the AI platform's per-minute fees.
  - Mitigations: use *conditional* forwarding only (no answer **61*, busy **67*, unreachable **62*; these are standard GSM codes that need testing on each network), or after-hours-only forwarding.
  - Prefer a business plan where forwarded minutes are included.
  - Or move the business number to a SIP provider (option B), so calls land directly on the SIP trunk with no double PSTN leg.
- **Prepaid lines cannot forward** on Orange (and reportedly Vodafone). Some micro-businesses use prepaid SIMs; they would need a subscription or a new number.
- **Bucharest 021/031 DIDs** are easiest from local Romanian SIP providers, which have a local address and company KYC in Romania. Foreign CPaaS inventory may be limited to provincial 03xx ranges or +40 37 national numbers. A national +40 37 number on a website may look less "local" to Bucharest callers. The agency could hold numbers in the *client's* name, which gives cleaner KYC and makes the client the end-user.
- **Caller ID on forwarded calls.** Forwarded calls normally present the original caller's CLI to the AI. Confirm with each operator, because ANCOM's anti-spoofing rules explicitly treat calls redirected to national numbers as legitimate, and the DID provider must pass CLI through.
- **Latency.** Forwarding adds a PSTN hop, and an EU-hosted platform (Vapi EU) plus an EU-region LLM/TTS reduces round-trip time compared with US hosting. Expect the AI's response latency (around 0.6–1.5 s) to dominate rather than the forwarding itself. This is an inference; no Romanian measurements were found.
- **112 / emergency.** Twilio does not allow emergency calls from Romanian numbers. Inbound-only AI numbers don't need 112, but the AI must tell callers in an emergency to hang up and dial 112.

### Gaps
- I found no official Vodafone or Digi Romania tariff for forwarded minutes, and no confirmed Romanian forwarding codes.
- I found no Telekom fixed-line details. From background knowledge (not verified this session), Telekom Romania's fixed business was sold to Orange in 2021 and now runs as Orange Romania Communications.
- Twilio's current Romanian number types and prices (local 021/031 availability, mobile numbers) could not be read; the site was blocked.
- I found no prices from Romanian SIP providers for 021/031 DIDs or per-minute rates.
- I found no ANCOM rule explicitly on foreign (non-Romanian-authorised) providers holding Romanian numbers. Providers assigned numbers generally need ANCOM general authorisation; CPaaS providers resell through locally authorised carriers. This is an assumption, not verified.

## 6. Consumer protection, AI voices impersonating humans, and recording-consent rules

### Takeaway
There is no specific Romanian statute yet on AI voices in customer calls. The binding rules are AI Act Art. 50 (disclose AI and on whose behalf; never pretend to be human) and GDPR transparency. For recording, Romania is effectively a **one-party** jurisdiction under Law 506/2004 art. 4: a participant may record. A business recording customers still owes GDPR notice. Two pending Romanian bills are worth tracking:
- the "deepfake" labelling law, passed by the Senate in 2023 and stalled in the Chamber
- the USR "5-minute human operator" call-centre bill, passed by the Senate in 2023 and stalled in the Chamber as of February 2026

If the second passes, it could force a human fallback for complaint or information calls in sectors that may include medical services.

### Cited Findings
- **Deepfake bill.** The Senate adopted it in June 2023 (77 for, 17 against, 10 abstentions). The Chamber of Deputies is the decisive chamber. The bill was withdrawn from the plenary for further committee work after controversy over criminal penalties. It would require labelling such as "Acest material conține ipostaze imaginare", enforced by CNA for audiovisual content. I found no evidence of final adoption or publication in Monitorul Oficial. — [Cursdeguvernare](https://cursdeguvernare.ro/interzicerea-folosirii-matioase-a-tehnologiei-lege-adoptata-in-senat-amenzi-pentru-deepfake-nesemnalizat-pe-televiuni.html); [Europa Liberă](https://romania.europalibera.org/a/32816725.html); [Alba24](https://alba24.ro/legea-deepfake-la-vot-final-amenzi-de-pana-la-90-000-de-lei-si-inchisoare-pentru-clipuri-generate-cu-inteligenta-artificiala-1018965.html); [Euronews România](https://www.euronews.ro/articole/legea-deepfake-amanata-din-nou-de-deputati-ce-sanctiuni-vor-primi-cei-care-distri)
- **"5-minute human operator" bill.** It amends OUG 49/2009: providers established in Romania would have to have complaint or information calls taken by a human operator within 5 minutes of the customer selecting that option, except in force majeure.
  - Adoption: the Senate adopted it on 3 May 2023 (72 votes, 3 abstentions).
  - Fines: 1,000–5,000 lei in the Senate text, versus 50,000–100,000 lei claimed by the sponsors.
  - Scope per press: banks, telecoms, transport, hospitals and medical services, notaries, gambling and public authorities. Critics say the term "prestatori" is vague enough to reach small firms such as barbers or taxis.
  - Status: still stuck in the Chamber of Deputies as of February 2026.
  - Sources: [Economedia](https://economedia.ro/apelurile-din-call-center-trebuie-preluate-de-un-operator-uman-in-maximum-5-minute-proiect-usr-adoptat-in-senat.html); [Profit.ro](https://www.profit.ro/perspective/schimbari-legislative-pentru-firme/obligatia-de-a-raspunde-clientilor-la-telefon-in-cel-mult-5-minute-prin-operator-uman-extinsa-la-banci-it-c-transporturi-si-autoritati-publice-amenzi-in-caz-contrar-21105934); [DCNews](https://www.dcnews.ro/call-center-5-minute-avramescu-pnl-dupa-propunerea-usr-risca-sa-loveasca-in-mediul-de-afaceri-astfel-de-scapari-nu-ar-trebui-sa-existe-in-parlament_914869.html); [B1TV (Feb 2026)](https://www.b1tv.ro/eveniment/romanii-ar-fi-putut-scapa-de-robotii-din-call-center-legea-care-obliga-raspunsul-in-5-minute-este-blocata-in-parlament-1666426.html)
- An April 2026 article reported that over 4,000 Romanians complained to ANPC (consumer protection) in the previous year about interactions with automated call-centre systems, with fines of over 280,000 lei. The search summary did not show which page this came from; possibly [Observator News](https://observatornews.ro/eveniment/legea-care-limiteaza-la-5-minute-timpul-de-asteptare-in-callcenter-blocata-de-trei-ani-646146.html) or the B1TV piece above. Treat as unverified.
- **One-party recording.** Under Law 506/2004 art. 4(2)(a), a participant may record; a secondary guide says any participant can record without notifying the others. — [legeaz.net](https://legeaz.net/legea-506-2004-prelucrare-date-caracter-personal/articolul-4); [RecordingLaw](https://www.recordinglaw.com/ro/world-laws/world-recording-laws/romania-recording-laws/)
- AI agents must disclose their artificial nature and on whose behalf they act (Art. 50 guidelines, as summarised). — [Blck Alpaca](https://blckalpaca.at/en/knowledge-base/ai-agents/eu-ai-act-for-ai-agents/article-50-for-chatbots-and-ai-agents-what-you-must-disclose)

### Inferences
- An AI receptionist that denies being an AI, or invents a human name and persona without disclosure, would breach Art. 50. It could also be argued to be a misleading commercial practice under the general Romanian unfair-practices law (Law 363/2007, the UCPD transposition). That second point is my inference; no source was found linking it to AI voices.
- Always offer a "talk to a human" path (transfer to the business's mobile during working hours, or a promised call-back). This is good practice, reduces ANPC complaint risk, and pre-empts the 5-minute bill if it is ever adopted.
- If the deepfake law passes in its 2024 form, it seems aimed at audiovisual and public content, not at private service calls, but its wording should be checked.

### Gaps
- I found no ANPC guidance or decision on AI voice agents.
- I could not check whether Law 363/2007 or the Consumer Code has been applied to automated phone systems.
- I could not confirm the current Chamber of Deputies status of either bill after February 2026.

## 7. Synthesis: real blockers vs manageable requirements

### Takeaway
I found **no legal blocker** to offering an inbound AI receptionist to Bucharest small businesses in October 2026. Most requirements are manageable with templates and configuration:
- AI disclosure
- recording notice
- DPAs
- EU hosting
- KYC for numbers

The **real blockers or hard limits** are:
- (1) automated outbound marketing calls without prior consent, which are prohibited
- (2) forwarding to a foreign or US number, which Orange does not offer, plus no forwarding on prepaid lines
- (3) spoofing the client's number on outbound calls from a foreign platform, which is blocked by ANCOM measures
- (4) for clinics, any vendor that trains on or retains health-related call data without controls, or AI that performs triage or automated decisions on health data without explicit consent

### Cited Findings
- Prohibited without prior consent: automated commercial calls (Law 506/2004 art. 12). — [Avocatnet](https://www.avocatnet.ro/articol_15269/Orange-amendata-cu-5000-lei-pentru-mesaje-comerciale-nesolicitate.html)
- Orange: no forwarding to international numbers, none on PrePay, €0.17/min + VAT off-net. — [Orange Help](https://www.orange.ro/help/cat-costa-redirectionarea-apelurilor-99)
- ANCOM blocks international-route calls showing Romanian fixed numbers. — [Spotmedia](https://spotmedia.ro/stiri/eveniment/gata-cu-apelurile-false-din-strainatate-care-afiseaza-numere-romanesti-ancom-le-blocheaza)
- Art. 50 disclosure applies from 2 August 2026, not postponed. — [AI Act Blog NL](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026)
- The DPF is in force but under pressure (C-703/25 P pending; EDPB review request of 31 July 2026). — [IAPP](https://iapp.org/news/a/edpb-requests-review-of-eu-us-data-privacy-framework-following-trump-v-slaughter)
- Law 190/2018 art. 3: automated decisions on health data need explicit consent. — [Rubinian](https://www.rubinian.com/legea-190-2018-masuri-de-punere-in-aplicare-a-regulamentului-ue-2016-679-gdpr)

### Inferences
**Manageable checklist for the provider/agency:**
1. Fixed Romanian opening line: AI nature + whose behalf + recording notice + link to the privacy notice. Repeat it on hand-off.
2. A layered privacy notice template per client (purpose, legal basis = legitimate interest, retention e.g. 30–90 days for audio, rights, sub-processors, transfers).
3. An Art. 28 DPA template between the client and the agency, plus a flow-down list (Vapi/Retell, OpenAI/LLM, ElevenLabs/TTS, STT, Twilio/Telnyx). Use EU regions and no-training settings.
4. For clinics: booking-only scope, minimal health data, no triage, a 112 message, a DPIA template and confidentiality undertakings.
5. An access-request procedure: find and export a caller's recording or transcript within 30 days, with employee-voice redaction where relevant.
6. Telephony: a Romanian DID in the client's name (local SIP provider for 021/031, or Twilio/Telnyx with KYC), conditional forwarding codes, and an upfront estimate of the client's forwarding cost per carrier.
7. Inbound only. Outbound only as call-backs the caller explicitly requested, or transactional reminders with opt-in captured at booking.
8. Track three developments:
   - the Romanian AI Act implementing law (ANCOM sanction powers)
   - the CJEU's DPF ruling (C-703/25 P) and the Commission's response to the EDPB letter
   - the 5-minute human-operator bill

### Gaps
- No lawyer-validated Romanian opinion was found that combines all of these for AI receptionists specifically. The synthesis above is my inference from separate sources.
- Exact forwarding costs for Vodafone, Digi and business plans are unknown and should be checked per client contract.
