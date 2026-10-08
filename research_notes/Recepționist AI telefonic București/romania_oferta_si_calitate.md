# Supply side of AI phone answering / AI voice agents in Romania (Bucharest focus) and Romanian voice-AI quality, as of Oct 2026

*Method note: The egress proxy blocked direct fetches of nearly every source (start-up.ro, zf.ro, mdpi.com, voicefleet.ai, autocalls.ai, arxiv.org, elevenlabs.io and others all returned EGRESS_BLOCKED / HTTP 000). So **every fact below comes from WebSearch result snippets/summaries**, not from a full read of the page. Treat exact figures as "as reported in search snippet". Vendor self-claims are labelled **[vendor claim]**; independent/press/academic items are labelled **[independent]** or **[press]**. Note that press items based on a company's own release are still company-sourced. Dates are given where the snippet showed them.*

## Q1. Who sells AI voice agents / AI receptionists in Romanian, to whom, and at what price?

### Takeaway
The market is already crowded on two levels. (a) Enterprise players (Wonderful, Druid AI, Autocalls, plus telco in-house bots like Orange Djia and Vodafone TOBi) sell to banks, telecoms, utilities and debt collectors. (b) There is a long tail of at least 25 small Romanian vendors and agencies selling "agent vocal AI" / "recepționer AI" / "robot telefonic" to SMBs (clinics, salons, car services, restaurants, taxi, real estate). They publish prices from about 99–200 RON/month at entry level, through roughly €139–€499/month for packaged plans, up to €1,200–€2,500+ setup fees for custom builds. Several are Bucharest-based (Voxbee, Gimfy, AI Factory, AgentVocal.ro, Autocalls per Tracxn). Telcos (Vodafone, Telekom, Digi) do **not** appear to sell an AI receptionist to SMBs.

### Cited Findings

**Enterprise / scale players**
- **Wonderful (Israeli, entered Romania 13 Oct 2025)** [press]: opened a local office and named Lucia Stoicescu (ex-CEO of mindit.io) Country Manager. Its platform handles voice and chat/email in Romanian plus 22 other European languages. It claims to handle Romanian grammar (postposed definite articles, diacritics) and says it has started working with "some of Romania's largest banks, utilities, telecom and energy providers" (no named clients). Compliance claims: GDPR, EU AI Act, DORA, SOC2, NIS2 — [Romania Insider](https://www.romania-insider.com/wonderful-enters-romanian-market-2025); [The Diplomat](https://www.thediplomat.ro/2025/10/13/global-ai-company-wonderful-enters-the-romanian-market-appoints-lucia-stoicescu-as-country-manager/); [Forbes.ro](https://www.forbes.ro/wonderful-intra-pe-piata-din-romania-si-o-numeste-pe-lucia-stoicescu-country-manager-470379); [ZF](https://www.zf.ro/business-hi-tech/wonderful-platforma-globala-agentic-intra-piata-romania-birou-local-22925674)
- Wonderful target sectors per Forbes.ro: telecom, utilities/energy, health, retail, banks and insurance. These are all enterprise sectors; there is no SMB offer and no public pricing — [Forbes.ro](https://www.forbes.ro/wonderful-intra-pe-piata-din-romania-si-o-numeste-pe-lucia-stoicescu-country-manager-470379)
- At Future Banking Summit 2025, Wonderful Romania said it had clients in banking, telecom and insurance. It also said AI-handled calls last about 50% less than human-handled calls [vendor claim] — [Wall-Street.ro](https://www.wall-street.ro/articol/finante-banci/future-banking-summit-ce-rezultate-au-deja-agentii-ai-folositi-de-companii.html)
- Funding: $34M seed (Jul 2025); $100M Series A (Nov 2025) — [TechCrunch](https://techcrunch.com/2025/11/11/wonderful-raised-100m-series-a-to-put-ai-agents-on-the-front-lines-of-customer-service/). Sept 2026: a $550M Series C at a $5B valuation, operations in 35+ markets, and Yannis Jacob-Drăghici named GM for Romania & Moldova — [start-up.ro (snippet)](https://start-up.ro/wonderful-compania-ai-evaluata-la-5-miliarde-de-dolari-il-numeste-pe-yannis-jacob-draghici-la-conducerea-operatiunilor-din-romania-si-moldova). Romanian Bogdan Putinică was appointed to lead Wonderful across 29 countries (Oct 2025) — [Romania Insider](https://www.romania-insider.com/bogdan-putinica-wonderful-gm-october-2025)
- **Autocalls.ai (Romanian startup)** [press, company-sourced]: founded by Alex Filoti (CEO) and Ștefan Petrea (CTO). It began in May 2023 as a side project at the founders' software firm Hip Services and launched in Romania in June 2024. Development investment was €300k from own funds, with Microsoft/Amazon sponsoring AI training. It claims 25 languages, targets high-volume sectors (auto, call centers, HoReCa, banking, insurance) and estimated €500k first-year revenue (a projection) — [Economedia](https://economedia.ro/startup-ul-romanesc-autocalls-ai-lanseaza-roboti-vocali-fluenti-in-25-limbi-si-capabili-sa-interactioneze-natural-cu-clientii-in-urma-unei-investitii-de-300-000-de-euro.html); [StartupCafe](https://startupcafe.ro/idee-afacere-romani-investitie-roboti-vocali-inteligenta-artificiala-htm-27374); [Agerpres (14 Jun 2024)](https://www.agerpres.ro/ots/2024/06/14/inteligenta-artificiala-preia-controlul-apelurilor-vocale-autocalls-ai-lanseaza-roboti-vocali-fluenti-in-25-limbi-si-capabili-sa-interactioneze-natural-cu-clientii--654099)
- Autocalls implementation time: about 2 weeks for a simple flow (appointment confirmations), 2–3 months for complex flows such as debt collection with installment plans [vendor claim, 2024] — [Revista Biz](https://www.revistabiz.ro/startup-ul-romanesc-autocalls-ai-lanseaza-roboti-vocali-ai-fluenti-in-25-limbi-piata-potentiala-de-500-mld/)
- In a ZF interview the Autocalls CTO set a goal of 50 clients on the Romanian market "this year" (year not visible in snippet; likely 2024) — [ZF IT Generation](https://www.zf.ro/zf-it-generation/zf-it-generation-stefan-petrea-cofondator-si-cto-al-autocalls-ai-22411619)
- Autocalls scale estimates (third-party, low reliability): Getlatka estimates $220K ARR for 2025 and 2 employees — [Getlatka](https://getlatka.com/companies/autocalls.ai). Tracxn (2026) calls it an unfunded Bucharest company founded 2023 — [Tracxn](https://tracxn.com/d/companies/autocallsai/__UP1kowo9iFoBFfoXTeG7jc0ujwy14NARG3ENIfatmPI). The pricing page structured data names the legal entity MULTICODE S.R.L., Iași, so HQ sources conflict — [Autocalls pricing (snippet)](https://autocalls.ai/pricing)
- **Autocalls pricing** (USD, self-serve) [vendor]:
  - Usage is "from $0.09/min all-inclusive" (LLM + TTS + STT + telephony).
  - Agency plan: $249/month with 1,700 minutes. White Label plan: $419/month with 3,500 minutes — [Autocalls pricing](https://autocalls.ai/pricing).
  - A third-party roundup lists Starter at $34/month (120 min) and Pro at $129/month (700 min) — [ainora.lt](https://ainora.lt/compare/autocalls). Conflicting figures also appear: Starter $27, Pro $103, Agency $199, White Label $355, and the homepage shows Pro at $103 with $0.16 per extra minute.
  - Romanian virtual numbers cost from $3.99/month and inbound from $0.01/min. The platform offers 10 Romanian voices — [Autocalls Romania number](https://autocalls.ai/country/romania); [Autocalls Romanian](https://autocalls.ai/language/romanian)
- Autocalls runs a **white-label program for agencies/resellers**. A solo provider could resell it rather than compete with it — [Barchart](https://www.barchart.com/story/news/404927/autocalls-launches-whitelabel-ai-voice-agent-program-for-agencies-and-resellers); [Autocalls white-label](https://autocalls.ai/white-label)
- **Druid AI (Romanian, enterprise conversational AI)** [vendor/press]:
  - In Nov 2024, with KRUK (debt collection), it launched **KARINA**, presented as the first Romanian-speaking voice-based AI agent. Callers can check outstanding amounts, installments and payment confirmations, transfer to inbound queues, and receive outbound campaigns — [Druid AI news](https://www.druidai.com/news/druid-ai-and-kruk-are-launching-karina-the-first-romanian-speaking-voice-based-ai-agent)
  - Druid's voice page mentions a Bucharest municipality citizen-support voice AI [vendor claim] — [Druid voice agents](https://www.druidai.com/ai-voice-agents)
  - May 2026: IT HIT became a reseller for healthcare, banking, insurance, retail and higher-education clients — [Romania Insider](https://www.romania-insider.com/it-hit-druid-ai-reseller-partnership-may-2026)
  - Druid claims 350+ enterprise clients. It is enterprise-only, with no public SMB pricing found.
- **Orange Romania – Djia** [press, Sept 2021]: Djia is a Romanian-language virtual voice operator on the 300 customer line. It handles bills, subscription resources, PUK, invoice copies, payment confirmation and payment deferral, and transfers complex cases to humans after identifying the caller. The pilot started April 2021 with a reported **success rate above 52%** — [Bursa](https://www.bursa.ro/orange-lanseaza-djia-asistentul-virtual-call-center-care-ofera-clientilor-suport-vocal-in-limba-romana-61982448); [Orange newsroom](https://newsroom.orange.ro/comunicate/orange-lanseaza-djia-asistentul-virtual-call-center-care-ofera-clientilor-suport-vocal-in-limba-romana/); [Orange Djia page](https://www.orange.ro/servicii/asistent-vocal-djia/). This is an in-house bot, not sold to SMBs.
- **Vodafone Romania**:
  - TOBi is an app/chat support assistant for Vodafone's own accounts — [CDI case study](https://www.conversationdesigninstitute.com/case-studies/vodafone-tobi-assistant)
  - An older ZF report (date not shown; likely years old) says Vodafone replaced its keypad IVR with a robot that "understands what customers say" — [ZF](https://www.zf.ro/zf-24/apelurile-catre-call-center-ul-vodafone-preluate-de-un-robot-care-intelege-ce-spun-clientii-13156315)
  - For SMBs Vodafone sells **Cloud Voice**, a managed virtual PBX, with no AI receptionist found — [Vodafone Cloud Voice](https://www.vodafone.ro/business/solutii-de-business/afacerea-ta-pregatita-pentru-viitor/mareste-productivitatea/cloud-voice)
- **Telekom Romania / Digi**: search found only Telekom's "Tim" support assistant and its 1933 business line, and Digi's fixed E1 telephony with an optional Digi PBX. Neither showed an AI receptionist product for SMBs — [Digi Tel Conect Plus](https://www.digi.ro/business/servicii/telefonie-fixa/digi-tel-conect-plus-v2); [Digi startup pack](https://www.digi.ro/business/startup)
- **Daktela** (Czech CCaaS, Romanian-language website): sells an AI voicebot (inbound, 24/7). Its public demo is in English and no explicit Romanian voicebot support was found — [Daktela AI](https://daktela.com/ai); [Daktela voicebot demo](https://daktela.com/ai/demo-voicebot)
- **CloudTalk** (Slovak cloud telephony): markets AI voice agents in Romanian-language pages, including a "Funcție nouă Agenți vocali AI" page and a Romanian blog post updated 9 Apr 2026. It claims 70+ languages (elsewhere 60+), but no explicit Romanian speech confirmation was found — [CloudTalk RO AI voice agents](https://www.cloudtalk.io/ro/ai-voice-agents/); [CloudTalk RO blog](https://www.cloudtalk.io/ro/blog/ce-sunt-agentii-vocali-ai/); [CloudTalk EN](https://www.cloudtalk.io/ai-voice-agents/)
- **Vatis Tech** (Romanian STT company): sells speech-to-text, claiming 97% accuracy in Romanian and up to 95% in hard domains (medical, legal, call center). It hosted a webinar on building conversational AI voicebots, in which it supplies the ASR layer. **No finished voice-agent/receptionist product found** — [Juridice.ro](https://www.juridice.ro/678811/vatis-tech-finalizeaza-tehnologia-de-recunoastere-vocala-si-depaseste-gigantii-tech-ai-lumii-ajungand-la-o-acuratete-de-97-la-limba-romana.html); [Wall-Street.ro](https://www.wall-street.ro/articol/Start-Up/290605/vatis-tech-acuratete-de-pana-la-95-in-domenii-grele-pentru-tehnologiile-speech-to-text-precum-medical-juridic-si-call-center.html); [Vatis webinar](https://vatis.tech/event/how-to-build-conversational-ai-voicebots)
- **Genezio**: not a voice-agent vendor. It is a "GenAI brand perception" platform (it simulates customer-persona conversations with AI engines) with enterprise logos (Vodafone, Kaufland, BCR, Druid AI, SmartBill) and a $2M pre-seed (2024) — [Romania Insider](https://www.romania-insider.com/romanian-startup-genezio-ai-perception-brands-2025); [Genezio](https://genezio.com/)
- **Trimaranix**: a Romanian–Bulgarian agentic-AI consultancy launched in 2026, enterprise-oriented (details not in snippet) — [Romania Insider](https://www.romania-insider.com/romanian-bulgarian-tech-companies-trimaranix-2026)

**SMB-focused Romanian vendors / agencies (all [vendor claim] unless noted)**
- **Voxbee (Bucharest, Sector 3)**:
  - Its AI receptionist books, changes and cancels appointments in the calendar and sends SMS confirmations. A simple booking agent is quoted at 2–3 working days to deploy, and the company claims to be on the ANCOM telecom-provider register — [Voxbee AI receptionist](https://voxbee.ro/ai-receptionist)
  - Stack: LiveKit on servers hosted in Romania, Google Gemini / OpenAI GPT-4 for understanding, ElevenLabs and Google TTS for Romanian voices — [Voxbee AI agenți](https://voxbee.ro/ai-agenti)
  - Prices: restaurant ordering agent from **200 RON/month** — [Voxbee restaurant blog](https://voxbee.ro/blog/comenzi-restaurant). Taxi-dispatch AI at about **2 euro-cents/min** of conversation, built with a Deva taxi dispatcher that uses it daily — [Voxbee taxi](https://voxbee.ro/blog/software-dispecerat-taxi-gratuit)
  - It also sells cloud PBX — [Voxbee](https://voxbee.ro/centrala-telefonica-virtuala)
- **AgentVocal.ro**: offers 24/7 phone reception, outbound cold-calling, lead qualification and AI dispatch. It calls itself a "leader in Romania" and claims 50+ Romanian firms automated. Case studies: a client handling 10,000+ calls/month; Brasadas Imobiliare saving up to €5,000; a real-estate agency with 64% conversion; an auto-dismantling yard using an AI receptionist. Price depends on volume and customization (not published) — [AgentVocal.ro](https://agentvocal.ro/)
- **Gimfy (Bucharest)**: custom software, automations and AI agents. Its case study is Rovent, where an AI assistant takes reception requests — [Gimfy](https://www.gim-fy.com/)
- **AI Factory (Tag Information Technology SRL, Iuliu Maniu 14, Bucharest)**: sells chatbots, an "AI telephone exchange" and OCR, claiming up to 40% cost reduction — [AI Factory](https://aifactory.ro/)
- **Callio (dental/medical clinics)**:
  - Founders are Cristi Goia and Robert Stemler, self-funded. Work started Dec 2025 and the first real clinic test was Feb 2026 — [start-up.ro (snippet, ~mid-2026)](https://start-up.ro/callio-agentul-vocal-ai-care-preia-telefonul-receptiei-din-clinicile-stomatologice)
  - Prices: **Flex €139/month** (no 24/7), **Starter €189/month** (24/7, 1–3 doctors), **Professional €299/month** (1–7 doctors, reports). Clinic Pro is custom (WhatsApp Business). Packages include 300 / 700 / 1,500 minutes and 300 / 500 / 1,000 SMS — [Callio](https://callio.ro/)
- **DOTRO SmartPBX VoiceAI**: a 24/7 Romanian AI assistant inside its cloud PBX. It collects booking data and pushes it to the team, CRM or calendar, and works only with SmartPBX.
  - Its product page shows **€79/month** — [Dotro VoiceAI](https://www.dotro.ro/asistent-vocal-ai-smartpbx/)
  - Its blog says virtual PBX from €14/month and AI voice assistant "from €19/month" (internal inconsistency) — [Dotro blog](https://www.dotro.ro/blog/cate-apeluri-pierde-o-firma)
- **Codly**: **0.34 lei/min**, pay-per-use. Its example: 1,100 calls × 2 min = 748 lei/month. It claims the best price in Romania — [Codly](https://codly.ro/)
- **Vocalyy**: Starter **€299/month** with 1,000 inbound minutes and 2 simultaneous calls, aimed at clinics, salons, workshops and law offices nationwide — [Vocalyy](https://www.vocalyy.ro/)
- **Agentul Vocal (agentulvocal.ro)**: **€299 / €399 / €499 per month**. The START plan includes a 24/7 assistant and a custom script; the top tier adds CRM integration. Search metadata suggests the page may be ~15 months old — [Agentul Vocal](https://agentulvocal.ro/)
- **Receptionerul Virtual**: car-service page (Pașcani) shows **99 RON/month with 200 minutes**, while its structured data lists 199 / 399 / 599 RON tiers (conflict) — [Receptionerul Virtual](https://receptionerulvirtual.ro/industrii/service-auto/pascani); [home](https://receptionerulvirtual.ro/)
- **ArhAI (Oradea)**: voice agents from **8,900 lei setup + 690 lei/month**, 2–3 weeks to deliver. About half of last year's projects were done remotely, including for Bucharest clients. It also has Mecanio, car-service software with an AI phone agent — [ArhAI](https://arhai.ro/)
- **Nextjourney (Brașov)**: "Voice Pilot" at **€2,500** for one conversational flow. Stack: ElevenLabs, Vapi, Chatterbox TTS — [Nextjourney](https://nextjourney.ro/servicii/agents)
- **Other vendors seen in search**: generic pages only, no prices unless noted:
  - NexAI Agency (car service and other verticals, 30+ languages, free demo) — [NexAI](https://nexaiagency.ro/agent-vocal-ai)
  - AloAI ("15 years, 50+ implementations") — [AloAI](https://aloai.ro/)
  - CallManager (cloud PBX + AI robot, "deploy in 2–3 hours") — [CallManager](https://callmanager.ro/agent-vocal-ai)
  - Zudu (<500 ms latency, accents in "42 counties", RO–EN code-switching) — [Zudu](https://zudu.ai/language/ro/asistent-vocal-ai-in-limba-romana/)
  - VoiceGenie (ElevenLabs Romanian voices) — [VoiceGenie](https://voicegenie.ai/en/voice-ai-agent-in-romanian)
  - AI Frontdesk (salons, claims 60% fewer no-shows) — [AI Frontdesk](https://aifrontdesk.ro/servicii/agent-vocal)
  - Synvoxa (dental, Cluj testimonial, <2 s response) — [Synvoxa](https://synvoxa.com/)
  - VAstoma (WhatsApp + AI reminder calls 24h/2h before, claims 87% resolved without intervention) — [VAstoma](https://vastoma.ro/)
  - DentAIM (WhatsApp reminders) — [DentAIM](https://dentaim.ro/)
  - Voicefleet (Romanian-language blog targeting dental and professional services, May 2026) — [Voicefleet RO blog](https://voicefleet.ai/ro/blog/receptioner-ai-servicii-profesionale-romania-consultatii-pret-leaduri-2026-05-31)
  - Also: STVN — [STVN](https://stvn.ro/services/asistent-ai-vocal/); AsistentVocal.ro — [AsistentVocal](https://asistentvocal.ro/); Agentul Tău Vocal — [agentultauvocal.ro](https://agentultauvocal.ro/); aireceptionist.ro (80+ countries, 45+ languages) — [AI Receptionist RO](https://aireceptionist.ro/); Robomarketing voicebot — [Robomarketing](https://robomarketing.ro/servicii/agent-vocal-ai-voicebot/); Kallina — [Kallina](https://kallina.info/compare/voice-ai-vs-ivr); centrala-telefonica.com — [centrala-telefonica.com](https://centrala-telefonica.com/)
- A Romanian price guide puts voice-agent implementation at about **€1,200+** with a custom monthly fee — [automatizez.ro](https://automatizez.ro/blog/cat-costa-chatbot-ai-2026)
- A Romanian guide notes the per-minute model price (it quotes "$0.05/min" for a GPT voice layer) is only part of total cost. Telephony, integrations, storage, monitoring and human intervention come on top — [agentiadeai.ro](https://agentiadeai.ro/blog/agenti-vocali-ai-romania-ghid-complet-companii)

### Inferences
- Price anchors a Bucharest SMB will see (vendor-published):
  - Ultra-low: 99–200 RON/month (Receptionerul Virtual, Voxbee restaurant), €19–79/month bundled with a PBX (Dotro), or pay-per-minute at 0.34 lei/min (Codly).
  - Mid: €139–€299/month (Callio, Vocalyy, Agentul Vocal).
  - Custom: €1,200–€2,500 setup, or 8,900 lei + 690 lei/month (ArhAI).
  - A new solo provider would be squeezed between cheap self-serve/bundled offers and established niche products. Differentiation would have to come from local hands-on setup, integration with the SMB's calendar/booking software, and in-person service in Bucharest, not from the technology itself.
- Most SMB vendors appear to be small agencies building on the same commodity stack (Vapi/Retell/LiveKit + GPT/Gemini + ElevenLabs/Google TTS), so barriers to entry are low on both sides. The cost of building is low for a new entrant, but so is the cost for the next competitor.
- Autocalls' white-label program makes reselling a realistic low-capex route for a solo provider.
- Enterprise players (Wonderful, Druid, Autocalls enterprise deals) are not direct competitors for a 1–10-employee clinic or salon. However, their marketing raises awareness that the technology exists.

### Gaps
- No public prices found for Wonderful, Druid, AgentVocal.ro, Gimfy, AI Factory, NexAI or Synvoxa.
- I could not verify any vendor's client count, case-study numbers or revenue. No independent reviews (G2/Capterra-style) were found for any Romanian SMB voice-agent vendor.
- **Bluepink** and other Romanian chatbot firms: no relevant voice-agent results found. **UiPath-adjacent** voice-agent offers for Romanian SMBs: none found (UiPath search hits were only Bucharest event pages).
- **Marketplaces** (Jobbers, OLX, Okazii, Fiverr, Upwork): searches returned only Romanian voice-over artists (Fiverr gigs up to ~$50; a Hubstaff profile at $8/h) and no "agent vocal AI" freelancer listings. The Romanian freelancer supply could not be quantified. The search covered Fiverr — [Fiverr seller example](https://www.fiverr.com/bmd240) — and Hubstaff — [Hubstaff profile](https://hubstafftalent.net/profiles/ecaterina-humeniuc).
- LinkedIn/Facebook ad libraries could not be searched in this environment.
- The current Djia status in 2026 is unknown.

## Q2. Documented Romanian SMB adoption of AI phone answering (case studies 2024–2026; Bucharest)

### Takeaway
Documented SMB cases are few, recent (mostly 2026), small-scale and almost entirely vendor- or startup-press-sourced. The best-documented is Callio at the Hub of Smiles dental clinic in Timișoara (200+ calls, 100+ bookings over a few months). The only Bucharest-specific press-covered pilot found is Meridian Taxi: an AI ordering line tested from August (year likely 2025) that handled only 10–15% of calls in the test phase. No independent case study of a Bucharest clinic, salon, auto service or restaurant using an AI phone receptionist was found.

### Cited Findings
- **Callio @ Hub of Smiles (Timișoara dental clinic)**: over a few months, 200+ calls handled and 100+ appointments booked. A few other clinics were active and others in onboarding as of the article (start-up.ro, ~summer 2026) [press, startup-sourced] — [start-up.ro](https://start-up.ro/callio-agentul-vocal-ai-care-preia-telefonul-receptiei-din-clinicile-stomatologice); [investments.ro mirror](https://investments.ro/post/callio-agentul-vocal-ai-care-preia-telefonul-receptiei-din-clinicile-stomatologice-1)
- **Meridian Taxi (Bucharest)** [press]:
  - Coverage reports a voice AI ordering system "tested in Bucharest starting in August", described as the first AI taxi ordering service tested in Romania. The aim is to remove waiting on the phone, since at peak hours "thousands of calls remain unanswered" because of limited operators.
  - In the test phase the technology took **10–15% of incoming calls**, with automatic transfer to a human operator. The demo number did not generate real rides.
  - Owner Dan Boabeș: "The real challenge is context. People don't say where they are, but what they see."
  - Search metadata suggested August 2025; current production status is unconfirmed.
  - Sources: [go4it.ro](https://www.go4it.ro/content/inteligenta-artificiala/exclusiv-primul-serviciu-de-comenzi-taxi-prin-ai-testat-in-romania-dan-boabes-provocarea-reala-e-contextul-oamenii-nu-spun-unde-sunt-ci-ce-vad-19254829); [Mediafax](https://www.mediafax.ro/social/una-dintre-cele-mai-cunoscute-companii-de-taxi-se-reinventeaza-lanseaza-primul-serviciu-de-comenzi-prin-ai-testat-in-romania-23587660); [Pozitivești](https://pozitivesti.ro/meridian-taxi-preluare-comenzi-ai/)
- **Taxi, other**:
  - A Deva dispatcher uses Voxbee's AI dispatch platform daily [vendor claim] — [Voxbee](https://voxbee.ro/blog/software-dispecerat-taxi-gratuit)
  - Taxi ADA Dorohoi advertised ordering "through a dispatch robot" (date not shown; may be a legacy IVR) — [Dorohoi News](https://www.dorohoinews.ro/informatii_utile-4641-Taxi-ADA-Dorohoi:-Acum-%C3%AE%C8%9Bi-po%C8%9Bi-comanda-o-ma%C8%99in%C4%83-prin-intermediul-unui-robot-de-dispecerat.html)
  - Bucharest regulation requires taxi orders to be transmitted to drivers via authorized dispatchers' radio stations (older ZF article). This is relevant if an AI takes orders — [ZF](https://www.zf.ro/business-hi-tech/decizie-socanta-primariei-capitalei-taximetristii-bucuresti-vor-primi-comenzile-clienti-statii-radio-dispecerate-autorizate-indiferent-transmise-online-telefon-16895215)
- **Dental, other**:
  - Synvoxa shows a testimonial from a Cluj-Napoca clinic [vendor] — [Synvoxa](https://synvoxa.com/)
  - Dentasisto (24/7 phone/site/WhatsApp) appears in a promo index of the May 2026 issue of *Actualități Stomatologice* — [dentalnews.ro](https://dentalnews.ro/index-promo-editia-de-vara-actualitati-stomatologice-nr-110/)
  - Prima Dental Clinic runs an OpenAI-based **website** assistant (AVAI), not phone — [Prima Dental Clinic](https://www.primadentalclinic.ro/avai/)
- **Real estate / auto**:
  - AgentVocal.ro lists Brasadas Imobiliare SRL (up to €5,000 saved), an unnamed real-estate agency (64% conversion of AI-qualified calls) and an auto-dismantling yard [vendor claims] — [AgentVocal.ro](https://agentvocal.ro/)
  - Robomarketing claims an unnamed real-estate client with zero missed after-hours calls [vendor] — [Robomarketing](https://robomarketing.ro/servicii/agent-vocal-ai-voicebot/)
  - Gimfy cites Rovent (reception requests handled by an AI assistant) [vendor] — [Gimfy](https://www.gim-fy.com/)
- **Restaurants**: no Romanian restaurant case found. The closest is Esushi in the **Republic of Moldova** (agent "Ana" handling reservations and orders on IG, WhatsApp and phone in RO/RU, integrated with Syrve POS) — [aichat.md](https://aichat.md/horeca-restaurant/). Voxbee markets a 200 RON/month restaurant ordering agent with no named client — [Voxbee](https://voxbee.ro/blog/comenzi-restaurant)
- **Enterprise adoption examples (not SMB)**:
  - KRUK debt collection (Druid KARINA, Nov 2024) — [Druid](https://www.druidai.com/news/druid-ai-and-kruk-are-launching-karina-the-first-romanian-speaking-voice-based-ai-agent)
  - Orange Djia (2021) — [Bursa](https://www.bursa.ro/orange-lanseaza-djia-asistentul-virtual-call-center-care-ofera-clientilor-suport-vocal-in-limba-romana-61982448)
  - Wonderful's unnamed banks, telecoms and utilities (2025–26) — [Romania Insider](https://www.romania-insider.com/wonderful-enters-romanian-market-2025)
  - Dacia used a Druid text assistant in 2024 (voice unclear) — [Romania Insider](https://www.romania-insider.com/druid-implements-virtual-assistant-dacia-romania-2024)

### Inferences
- SMB adoption in Romania is at the **early-adopter stage**: products launched in late 2025 or 2026, with handfuls of clinics per vendor. This suggests the market is not saturated by actual users, even though it is crowded with sellers.
- The Meridian Taxi test (10–15% of calls automated) and Orange's Djia (~52% success in 2021) suggest **partial automation with human fallback** is the realistic outcome in Romanian. That supports a pitch of "answer missed / after-hours calls and take bookings" rather than "replace the receptionist".
- The absence of Bucharest SMB case studies is both a risk (no proof points to show prospects) and an opening: a local provider who documents 2–3 Bucharest clients could stand out.

### Gaps
- No independent (non-vendor) data on how many Romanian SMBs use AI phone answering. No surveys found (INS/Eurostat SMB AI adoption was out of scope here).
- No Bucharest clinic, salon, auto-service or restaurant case study found. Meridian Taxi's year and current production status are unverified.
- Callio's and others' full articles could not be read (blocked), so case numbers come only from snippets.

## Q3. How good are Romanian STT/TTS and voice-agent stacks in 2026?

### Takeaway
All major component vendors now officially support Romanian:
- STT: Deepgram Nova-3 (since Nov 2025), ElevenLabs Scribe, Google Chirp 3 (GA), Azure, OpenAI gpt-realtime and Whisper.
- TTS: ElevenLabs multilingual v2 / Flash v2.5, Azure Alina/Emil neural voices, Google Chirp 3 HD ro-RO (since Nov 2025).

On clean benchmark audio the best Romanian ASR reaches about 3–10% WER. Robustness on real phone calls is much weaker and poorly documented: Whisper large-v3 scores about 20–27% WER on some Romanian sets, and dialect speech is worse. Known problem areas are numbers (14 vs 40), names, addresses, word stress in TTS, dialects and noisy spontaneous speech. There is **no independent end-to-end benchmark of Romanian voice agents**; quality claims are vendor marketing. Structured tasks like bookings are workable with careful design (confirmation read-backs, SMS confirmations, human fallback).

### Cited Findings

**Academic / independent ASR benchmarks**
- *Modern Speech Recognition for Romanian Language* (MDPI *Applied Sciences* 16(4):1928, 2026; DOI 10.3390/app16041928) [independent, academic]:
  - It releases CRoWL (9,000 h of weakly labelled Romanian speech) alongside Echo (378 h, crowd-sourced). The best result is **3.01% WER** (Conformer on Echo+CRoWL); wav2vec 2.0 reaches 4.04% (Echo) and 4.17% (Echo+CRoWL). Models are open-sourced — [DOI/MDPI](https://doi.org/10.3390/app16041928); [synapsesocial listing](https://www.synapsesocial.com/papers/699405774e9c9e835dfd64bf)
  - The same paper cites prior results: **Whisper large-v3: 10.8% (Common Voice), 8.2% (FLEURS), 13.8% (VoxPopuli), 27.2% (Echo), 24.9% (RSC)**. A Romanian fine-tuned Whisper-RO (small) scored 12.2 / 10.9 / 9.4 / 7.3 / 5.4% on the same sets — [MDPI](https://www.mdpi.com/2076-3417/16/4/1928)
  - The authors caution that cross-paper WER comparisons are unreliable due to differing test sets and normalization — [MDPI](https://www.mdpi.com/2076-3417/16/4/1928)
- **Echo** dataset origin: a crowd-sourcing platform with 300+ hours (Ungureanu & Dascălu, *Interaction Design and Architecture(s)* no. 62, Nov 2024) — [DOAJ](https://doaj.org/article/96eb50bfafa04ddd923dde278887c976)
- **RoDia** (2023): Whisper-Large scored **19.8% WER** on Romanian Common Voice. On the RoDia dialect test set error rates were higher; Muntenesc (closest to standard Romanian, the Bucharest region) had the lowest at 24.1% — [arXiv 2309.03378](https://arxiv.org/pdf/2309.03378)
- **UPB SpeeD lab** (Pirlogeanu, Georgescu, Cucu; SpeD 2025, Cluj; arXiv 5 Nov 2025): an open-source Romanian FastConformer (hybrid CTC/TDT, NeMo) trained on 2,600+ h, claiming SOTA on read, spontaneous and domain-specific Romanian benchmarks with **up to 27% relative WER reduction** vs previous best. Code is at GitHub SpeD-RoASR — [arXiv 2511.03361](https://arxiv.org/abs/2511.03361); [GitHub](https://github.com/gabitza-tech/SpeD-RoASR)
- **RO-N3WS** (arXiv 2603.02368, Mar 2026): Whisper Large and Whisper Small+Echo strongly outperform wav2vec 2.0 zero-shot. On one news set Whisper Small+Echo scored 9.4% WER vs 12.3% for Whisper Large — [arXiv 2603.02368](https://arxiv.org/html/2603.02368)
- **RACAI** (~2020): DeepSpeech2-based Romanian ASR with a best of 9.91% WER / 2.81% CER, trained on 230 h — [Proceedings of the Romanian Academy](https://acad.ro/sectii2002/proceedings/doc2020-4/11-Avram_Tufis.pdf)
- A 2026 arXiv paper on Romanian-accented speech recognition (ROMPAR) exists; only its reference list was visible — [arXiv 2606.15984](https://arxiv.org/pdf/2606.15984)
- I found **no published WER for Romanian 8 kHz telephone/call-center speech** from RACAI, UPB or others. The RoDigits connected-digits corpus (154 speakers, ~37.5 h) exists for digit recognition — [UPB Sci. Bulletin](https://www.scientificbulletin.upb.ro/rev_docs_arhiva/rezab7_316868.pdf)

**Vendor benchmarks / support (vendor claims)**
- **ElevenLabs**:
  - Its Romanian STT page claims Scribe reaches **3.1% WER on FLEURS and 5.5% on Common Voice**, vs Whisper large-v3 at 13.0% on FLEURS. Romanian is listed in the "excellent" (≤5% WER) tier — [ElevenLabs RO STT](https://elevenlabs.io/speech-to-text/romanian)
  - Romanian TTS is in multilingual v2 and Flash v2.5, with Romanian library voices (e.g., "Andrei", "Anca") — [ElevenLabs RO TTS](https://elevenlabs.io/text-to-speech/romanian); [json2video list](https://json2video.com/ai-voices/elevenlabs/languages/romanian/)
  - ElevenAgents bundles its own fine-tuned ASR — [ElevenAgents docs](https://elevenlabs.io/docs/eleven-agents/overview)
- **Speechmatics** (vendor-run FLEURS): Enhanced 5.28% WER vs Whisper large-v3 12.31% — [Speechmatics RO](https://www.speechmatics.com/speech-to-text/romanian)
- **Deepgram**: Romanian (`ro`) was added to monolingual Nova-3 on 24 Nov 2025, with Romanian among the largest relative WER reductions vs Nova-2 ("in several cases exceeding 20%"). Romanian is **not** in the Nova-3 multilingual / code-switching set. Flux (Deepgram's recommended real-time agent model) Romanian support was not confirmed — [Deepgram blog](https://deepgram.com/learn/deepgram-expands-nova-3-with-10-new-languages-and-multilingual-keyterm-prompting); [Deepgram changelog](https://developers.deepgram.com/changelog/2025/11/24); [Deepgram models](https://developers.deepgram.com/docs/models-languages-overview)
- **OpenAI gpt-realtime**:
  - Romanian is listed in Microsoft's Voice Live language list for gpt-realtime / gpt-realtime-mini. Microsoft notes OpenAI lists only languages meeting a WER threshold and that quality varies with acoustics and speaking style — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/voice-live-language-support)
  - gpt-realtime-translate accepts Romanian input (70+ input languages). OpenAI's guide advises testing names, numbers, dates, currency, phone numbers, accents and code-switching — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/voice_solutions/realtime_translation_guide)
  - No Romanian-specific quality score was published.
  - A developer forum thread (~2024) reports non-English unreliability and transcription drifting into the reply language — [OpenAI community](https://community.openai.com/t/languages-in-realtime-api/980149)
- **Google Cloud**:
  - Chirp 3 STT lists ro-RO as GA (API v2; streaming, sync and batch) — [Google Chirp 3 STT](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)
  - Chirp 3 HD TTS added ro-RO on 10 Nov 2025, **but pause control and custom pronunciations are not available for ro-RO** — [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd); [Google TTS release notes](https://docs.cloud.google.com/text-to-speech/docs/release-notes)
- **Microsoft Azure**: neural TTS voices ro-RO-AlinaNeural (F) and ro-RO-EmilNeural (M), GA since 2020 at 24 kHz. MAI-Transcribe 1.5/2 list Romanian — [Microsoft Ignite 2020 blog](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/ignite-2020-neural-tts-updates-new-language-support-more-voices-and-flexible-dep/1698544); [Azure language support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support); [json2video Alina](https://json2video.com/ai-voices/azure/voices/ro-ro-alinaneural/)

**Reported Romanian-specific problems**
- **Numbers**: a Romanian pilot checklist warns specifically about "paisprezece" (14) vs "patruzeci" (40), digits dictated in groups, and place names. It also recommends testing regional accents, traffic noise, fast speech, hesitations, diminutives, rare names, addresses, masked CNPs and alphanumeric codes. It warns that English performance does not predict Romanian performance — [agentiadeai.ro](https://agentiadeai.ro/blog/agenti-vocali-ai-romania-ghid-complet-companii)
- **Word stress in TTS**: a Romanian diction site (about a year old, from a party with an interest in human voice actors) argues no voice AI yet places Romanian word stress correctly on every word — [dictie.ro](https://www.dictie.ro/vocile-generate-tot-mai-greu-de-diferentiat/)
- **Location/context understanding**: Meridian Taxi's owner said people "don't say where they are, but what they see". That is a natural-language-understanding problem, not only an ASR one — [go4it.ro](https://www.go4it.ro/content/inteligenta-artificiala/exclusiv-primul-serviciu-de-comenzi-taxi-prin-ai-testat-in-romania-dan-boabes-provocarea-reala-e-contextul-oamenii-nu-spun-unde-sunt-ci-ce-vad-19254829)
- **Dialects**: Vatis's CEO discussed the difficulty of transcribing Romanian correctly and training on the Moldovan dialect — [Wall-Street.ro](https://www.wall-street.ro/articol/Companii/290819/adrian-ispas-ceo-vatis-tech-cat-de-dificil-e-sa-faci-o-aplicatie-care-transcrie-corect-limba-romana-si-cum-inveti-ai-ul-cu-dialectul-moldovenesc.html). RoDia dialect WERs are 24%+ for Whisper — [arXiv 2309.03378](https://arxiv.org/pdf/2309.03378)
- **Hallucinations (general, not Romania-specific)**: an opinion piece claims voice models without grounding can invent answers in 15–30% of real calls and advises measuring resolution rate rather than calls handled — [Unite.ai RO](https://www.unite.ai/ro/voice-ai-myths-enterprise-deployments/)
- **Vendor quality claims** (unverified): Zudu says it handles accents in 42 counties and RO–EN code-switching at <500 ms — [Zudu](https://zudu.ai/language/ro/asistent-vocal-ai-in-limba-romana/). Nexa says diacritics are pronounced correctly — [NexAI](https://nexaiagency.ro/agent-vocal-ai). Wonderful says it handles postposed articles and diacritics — [Romania Insider](https://www.romania-insider.com/wonderful-enters-romanian-market-2025)
- **Real-world partial success rates**: Orange Djia pilot >52% success (2021) — [Bursa](https://www.bursa.ro/orange-lanseaza-djia-asistentul-virtual-call-center-care-ofera-clientilor-suport-vocal-in-limba-romana-61982448). Meridian Taxi test: 10–15% of calls handled — [Mediafax](https://www.mediafax.ro/social/una-dintre-cele-mai-cunoscute-companii-de-taxi-se-reinventeaza-lanseaza-primul-serviciu-de-comenzi-prin-ai-testat-in-romania-23587660)

### Inferences
- The large spread in Whisper large-v3 Romanian WER (8% on FLEURS to 27% on Echo) likely reflects normalization, domain and recording conditions. A plausible extra Romanian-specific factor (my inference, not stated by sources) is diacritic encoding (ș/ț comma-below vs ş/ţ cedilla) and missing diacritics in references, which can inflate WER. For a phone agent, what matters is semantic accuracy on names, dates and numbers, not diacritics in transcripts.
- Phone audio (8 kHz, noise, spontaneous speech) is the weak spot, and no Romanian telephone benchmark exists publicly. Expect noticeably worse than headline benchmark numbers. Mitigations: read-back confirmation of date/time/phone number, SMS confirmation, keyterm prompting (Deepgram), and constrained booking flows.
- TTS is the more mature half: ElevenLabs, Azure and Google Romanian voices are production-grade for short transactional phrases. Stress errors and missing custom-pronunciation control (Google ro-RO) can still affect names and brands.
- Overall: Romanian voice AI in 2026 looks "good enough" for narrow SMB tasks (answer, collect name/phone/reason, offer slots, book, confirm by SMS, escalate). It is not proven for open-ended conversations or callers with strong regional accents. Part-time human oversight and call-review are prudent.

### Gaps
- No independent end-to-end evaluation (task success, latency, caller satisfaction) of any Romanian-language voice agent was found.
- No Romanian telephone-band ASR WER found. ElevenLabs/Deepgram Romanian telephone-specific numbers were not published.
- Exact Whisper rows in the original OpenAI Whisper paper and the UPB paper's Table II could not be retrieved (fetch blocked).
- No Romanian-language YouTube or independent reviews/demos of Romanian voice agents were found via search.

## Q4. What do Romanian call-center/BPO and telecom players say about voice-AI adoption?

### Takeaway
The prevailing Romanian narrative (March 2026, ZF Live with Vatis Tech's Adrian Ispas) is that voice agents are mainstream in the US/Western Europe and will arrive in Romania "within 1–2 years". In that picture most call-center calls end up robot-handled and humans keep only complex or delicate cases. Meanwhile BPOs are still hiring in Bucharest, and the big global BPOs present in Romania (Teleperformance, Concentrix/Webhelp) talk about AI globally but have no Romanian-language voice-agent announcements in search results. Telcos have had Romanian voice bots for their own care lines since 2021 (Orange Djia).

### Cited Findings
- **ZF Live, ~31 Mar 2026, Adrian Ispas (founder & CEO, Vatis Tech)** [press]: voice agents are "very popular in the US and Western Europe; entire call centers are making the transition". Romania has not reached this stage but will within **1–2 years**. Most call-center calls would be picked up by a robot and only complicated or delicate cases would reach humans. He also notes the sector employs tens of thousands of people in Romania — [ZF Live](https://www.zf.ro/zf-live/zf-live-adrian-ispas-vatis-tech-call-centere-intregi-fac-tranzitia-23102197); [ZF Live (follow-up)](https://www.zf.ro/zf-live/era-call-center-incepe-se-apuna-cat-va-mai-dura-pana-cand-robotii-23113293)
- RomaniaTV's headline on the same theme claims "over 50,000 Romanians" in call centers will lose jobs. The source of the figure is not shown (sensationalist) — [RomaniaTV](https://www.romaniatv.net/inteligenta-artificiala-va-inlocui-angajatii-din-call-center-peste-50-000-de-romani-vor-ramane-in-viitor-fara-loc-de-munca_9505054.html)
- Coverage cited an aggregated statistic that about 80% of companies plan to integrate AI voice tech in customer service by 2026 (secondary, unsourced) — [ZF Live](https://www.zf.ro/zf-live/era-call-center-incepe-se-apuna-cat-va-mai-dura-pana-cand-robotii-23113293)
- Vatis had a call-center vertical in its pipeline in earlier years (date unclear) and targeted €1M ARR in a ZF IT Generation update — [ZF IT Generation](https://www.zf.ro/zf-it-generation/zf-it-generation-start-up-update-adrian-ispas-fondator-ceo-vatis-22448911)
- **BPO hiring continues**: CGS România plans to hire 500 call-center agents in Bucharest and Brașov by year-end (ZF; year not visible in snippet) — [ZF](https://www.zf.ro/business-hi-tech/cgs-romania-angajeaza-500-de-agenti-call-center-in-bucuresti-si-brasov-6413331)
- **Global BPOs**:
  - Concentrix completed its Webhelp acquisition (Webhelp Romania has centers in Bucharest, Iași, Galați, Ploiești) — [ClubITC](https://www.clubitc.ro/2023/09/27/concentrix-si-webhelp-si-au-unit-fortele/)
  - Bloomberg (30 Jun 2026): Concentrix and Teleperformance shares fell on fears AI makes them "uninvestible"; short interest in Teleperformance rose to 12%+ by May 2026 — [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-30/call-center-stocks-fall-on-worry-ai-is-makes-them-uninvestible)
  - A secondary report attributes 20–30% automation of routine queries to TP.ai FAB (no primary source) — [Luminix](https://www.useluminix.com/reports/company-overviews/concentrix-company-overview-cx-outsourcing-ai-strategy-business-model-and-market-position-2026/source/4)
  - No Romanian-language voice-agent announcements by these BPOs were found.
- **Wonderful Romania** said AI calls last 50% less than human calls and cost far less (Future Banking Summit 2025) [vendor] — [Wall-Street.ro](https://www.wall-street.ro/articol/finante-banci/future-banking-summit-ce-rezultate-au-deja-agentii-ai-folositi-de-companii.html)
- **Telecom**: Orange's Djia (launched 14 Sep 2021; pilot from April 2021, >52% success; complex cases go to humans) — [Economica.net](https://www.economica.net/orange-lanseaza-djia-asistentul-virtual-call-center-care-ofera-clientilor-suport-vocal-in-limba-romana_531668.html); [Comunic.ro](https://comunic.ro/dupa-chatbot-ul-djingo-call-center-ul-orange-are-un-nou-asistent-virtual-djia-care-vorbeste-romaneste/). Vodafone moved from keypad IVR to a speech-understanding system (older, undated ZF) — [ZF](https://www.zf.ro/zf-24/apelurile-catre-call-center-ul-vodafone-preluate-de-un-robot-care-intelege-ce-spun-clientii-13156315)

### Inferences
- The "1–2 years" claim (March 2026) frames Romania as roughly 1–2 years behind Western markets for enterprise call centers. SMB adoption typically lags enterprise further. For a solo provider in October 2026 this means early timing: limited buyer awareness, but few entrenched local competitors with proven SMB references.
- The enterprise narrative focuses on cost and job replacement. For SMBs, the more credible value is not missing calls (after-hours, peak, lunch breaks) rather than headcount cuts.

### Gaps
- I could not read full ZF Live transcripts (blocked), so quotes are paraphrased from snippets and translated.
- No statements were found from ARCC/other Romanian call-center associations, or from Telekom/Digi executives, on voice AI.
- No quantitative Romanian adoption survey of voice AI in contact centers was found.

## Q5. Human substitutes: virtual receptionist / "secretariat virtual" / outsourced call answering for SMBs, and cost

### Takeaway
A human-answering market for SMBs exists but is thin and mostly quote-based. Published anchors:
- **TransTel Services "secretariat virtual"**: from **€250/month + VAT** (24/7 operator + IVR, 6-month minimum).
- **StartHUB secretarial services**: **€30/hour** or €150 per 10 hours.
- Regus/Spaces virtual offices: call answering as an add-on (no price).
- Outsourced call centers: about **$12–22/hour per agent** (≈53–97 lei/h; a full-time equivalent ≈ 8,500–15,500 lei/month).
- In-house: an entry-level receptionist/operator costs about 2,500–3,000 lei **net**/month (more with employer taxes).

Most AI offers (€19–€299/month) undercut human options, though full-time human staff remain the norm in clinics.

### Cited Findings
- **TransTel Services – Secretariat virtual**: "starting at €250/month excl. VAT", minimum contract 6 months. A trained operator answers the company's calls and gives information 24/7, combined with phone robot/IVR (page undated) — [tts.ro](http://www.tts.ro/secretariat-virtual.html)
- **StartHUB** secretarial services: €30/hour, a 10-hour pack at €150, and a "10 hours monthly" subscription quoted at €600 computed over 6 months (as given in the snippet; likely €100/month). Premium activities cost €52/h, excl. VAT, charged in EUR at the daily rate + 2% — [StartHUB](https://www.starthub.ro/servicii/servicii-de-secretariat)
- **Regus** virtual office: prices on request (24-month contracts) — [Regus RO](https://www.regus.com/ro-ro/virtual-offices). **Spaces**: call answering is included in "Virtual Office Plus" or available as an add-on, with operators answering in the company's name; no price shown — [Spaces RO](https://www.spacesworks.com/ro/virtual-offices)
- Other secretarial/VA providers with quote-based pricing: OfficeManager.ro (depends on tasks, volume, frequency; monthly or per project) — [OfficeManager](https://officemanager.ro/servicii/servicii-secretariat/); TeAsist — [teasist.ro](https://teasist.ro/servicii-de-secretariat/)
- **Outsourced call center for SMBs**: IPI Solutions targets SMBs with "affordable prices" but publishes no rate — [IPI Solutions](https://ipisolutions.ro/ro/acasa/). Other quote-based providers: externalizare-callcenter.ro — [link](https://externalizare-callcenter.ro/); servicii-callcenter.ro — [link](https://servicii-callcenter.ro/); inafaceri.ro — [link](https://inafaceri.ro/servicii/servicii-call-center)
- Market rate signals: Romanian call-center agents at about **$12–22/hour** depending on language and complexity (promotional site) — [Worldwide Call Centers](https://www.worldwidecallcenters.com/call-centers-in-romania/). Clutch Romania profiles mostly show a **<$25/hour** band — [Clutch](https://clutch.co/ro/call-centers)
- **Wage benchmarks**: ERI SalaryExpert puts a Bucharest call-center agent at about 28 RON/hour gross — [SalaryExpert Bucharest](https://www.salaryexpert.com/salary/job/call-center-agent/romania/bucharest). Randstad reports about 3,000 lei net/month on average and about 2,500 lei net for entry-level operators — [Randstad](https://www.randstad.ro/candidati/profil-loc-de-munca/operator-call-center/)
- **AI/PBX vendors framing the substitute**: Dotro positions a virtual PBX (from €14/month) and AI voice assistant (from €19/month) as the cheap alternative to missing calls [vendor] — [Dotro blog](https://www.dotro.ro/blog/cate-apeluri-pierde-o-firma)

### Inferences
- Human 24/7 answering at €250+/month (6-month lock-in) or €30/hour sets a ceiling. AI offers at €100–€300/month sit below it, with 24/7 coverage and no lock-in, which is the main economic argument.
- The real substitute for most Bucharest SMBs is likely not an outsourcing firm but the **owner/existing receptionist answering, or calls simply being missed**. Search found no evidence of widespread use of human answering services by Romanian clinics or salons. That makes "recovered missed calls" the key ROI story.
- A part-time solo provider could price around the €100–€250/month band, between the cheapest self-serve AI and human secretariat. Since the cheap AI tiers already exist, setup and maintenance would need to be bundled as service value.

### Gaps
- No published per-call or per-minute prices for human answering services in Romania were found, beyond TransTel's €250/month floor.
- No data on how many Romanian SMBs use human virtual receptionists.
- The TransTel and StartHUB pages are undated; prices may be stale.
