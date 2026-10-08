# AI phone receptionists / AI voice agents for SMBs abroad (US, UK, EU) and the "AI receptionist agency" model

Method note: research done 8 October 2026. WebFetch was blocked by the egress proxy for almost every domain tried (fortune.com, gartner.com, businesswire.com, retellai.com, help.gohighlevel.com, frontdeskreview.com, beside.com, uctoday.com, reddit.com). Reddit could not be searched at all, because the search tool refuses reddit.com. **Every fact below therefore comes from search-result snippets and search-engine summaries, not from full pages I read**, unless noted otherwise. Labels used: [VENDOR] = the source sells AI receptionists, platforms, courses or agency services; [INDEP] = government, analyst, press, law firm or court; [AGG] = aggregator or price tracker. Prices are as reported in mid/late 2026 unless dated otherwise.

## 1. How big is the SMB AI receptionist market in 2025–2026, who are the main players, and what do they charge?

### Takeaway
No reliable market-size figure exists. Published 2026 estimates run from about $2.1B to $4.6B, with incompatible definitions. Firm-level traction is the better signal: RingCentral grew from 5,800 to 16,400 AI Receptionist customers in three quarters, Beside reached 20,000+ paying customers, and Avoca (HVAC) reached a $1B valuation. Off-the-shelf SMB products cost about $25–$300/month (US) and €27–€600/month (EU). Raw infrastructure (Vapi, Retell, Bland, Synthflow, HighLevel) costs about $0.07–$0.25/minute all-in, which is the cost floor an agency resells on top of.

### Cited Findings
**Market size (all weak)**
- 2026 market-size claims conflict. One puts the "virtual receptionist service" market at $4.64B in 2026 (Business Research Insights, 9.8% CAGR). Another puts the "AI receptionist" market at $2.7B (2025) → $3.5B (2026), 27.8% CAGR. A third gives $2.1B in 2026 → $5.1B by 2030 (24.3% CAGR). A fourth uses the same 24.3% CAGR but reaches $14.6B by 2030. [AGG/VENDOR stats pages] — [SchedulingKit stats](https://www.schedulingkit.com/statistics/ai-receptionist-statistics); [AInora market stats](https://ainora.lt/blog/virtual-receptionist-market-statistics-2026); [Sci-Tech Today](https://www.sci-tech-today.com/stats/ai-receptionist-statistics/)
- One compiler says there is "no reliable standalone market-size figure" for virtual receptionists and that headline numbers disagree by an order of magnitude. It suggests anchoring on Grand View Research's conversational-AI market instead: about $11.6B in 2024, projected to $41.39B by 2030. [VENDOR] — [AInora](https://ainora.lt/blog/virtual-receptionist-market-statistics-2026)
- US Census BTOS [INDEP]: overall business AI use hovered at 17–20% between December 2025 and May 2026. Use rose among firms with 20+ employees but "didn't change significantly" among firms with fewer than 20, and fewer than 20% of firms with ≤4 employees used AI. The question was reworded in November 2025 from "producing goods or services" to "any business function", which breaks the time series. — [Census Bureau, May 2026](https://census.gov/library/stories/2026/05/ai-use-businesses.html)
- SBA Office of Advocacy [INDEP]: 8.8% of small firms (<250 employees) used AI in production, up from 6.3% six months earlier (old question wording, 2025). — [SBA Advocacy](https://advocacy.sba.gov/tag/ai)

**Traction signals for players**
- RingCentral AI Receptionist (AIR) [INDEP press on earnings]: 5,800 customers (Q3 2025) → 8,300+ (Q4 2025) → 11,800+ paying (Q1 2026) → 16,400 (Q2 2026, reported 23 July 2026). Launched in the UK with an SME focus. — [No Jitter](https://nojitter.com/ucaas/ringcentral-posts-strong-ai-receptionist-customer-growth); [No Jitter Q2 2026](https://nojitter.com/contact-centers/ringcentral-strong-2q-2026-powered-by-customer-growth-across-several-products)
- Beside (Fortune, November 2025) [INDEP press]: raised $32M. Before launch it reached $4M ARR with 20,000+ paying customers in 18 months of stealth (as "M1") and handles "millions of calls per month". It targets individuals and small businesses that can't afford an assistant. Implied ARPU is about $200/year, roughly $17/month (my arithmetic). — [Fortune](https://www.fortune.com/2025/11/11/beside-ai-voice-startup-raises-32-million-ai-receptionist-for-small-business/)
- Avoca (April 2026) [press]: raised $125M+ across seed, A and B at a $1B valuation (Series B led by Meritech and General Catalyst; A by Kleiner Perkins; seed by YC). It sells voice agents to HVAC, plumbing, roofing and electrical firms, and went from ~10 customers (2024) to 800+ (2026). The founders first built restaurant phone AI before pivoting to HVAC. — [Idlen](https://www.idlen.io/news/avoca-ai-1-billion-valuation-kleiner-perkins-services-economy-voice-agents-april-2026); [LetsDataScience](https://letsdatascience.com/news/avoca-raises-125m-reaches-1b-valuation-1f84b3d8)
- Retell AI (infrastructure, widely used by agencies): its own about page claims $40M annualized revenue, profitable, 25 people. Tracker arr.club logs $36M ARR (November 2025) and $50M+ (May 2026), but its entries are internally inconsistent. — [Retell about page](https://www.retellai.com/de/about-us); [arr.club Nov 2025](https://www.arr.club/retell/retell-reaches-3600000000-arr-2025-11); [arr.club May 2026](https://www.arr.club/retell/retell-scales-to-50m-arr-with-a-team-of-30-people)
- Vapi: $20M Series A in December 2024 (Bessemer) and a reported $50M Series B in May 2026 (Peak XV). Positioning is increasingly enterprise. — [VCA Online](https://www.vcaonline.com/news/2024121201/vapi-dials-in-20m-in-series-a-led-by-bessemer-to-bring-ai-voice-agents-to-enterprise/); [AF.net](https://af.net/cn/realtime/vapi-secures-50-million-in-series-b-funding-led-by-peak-xv-partners/)
- Synthflow (Berlin): about $20M (or €20M; sources differ) Series A in June 2025 (Accel). It reportedly processes 10M+ conversations per month (May 2025). — [VCBacked](https://www.vcbacked.co/company/synthflow-ai); [deutsche-startups](https://www.deutsche-startups.de/tag/Synthflow/)
- HighLevel (GoHighLevel) Voice AI [VENDOR blog]: 1M+ Voice AI conversations per month in December 2025 (10× year on year) and 2M+ completed calls in a single month by June 2026. — [HighLevel](https://www.gohighlevel.com/post/highlevel-hits-one-million-monthly-ai-calls)
- Vertical SaaS and platforms are bundling their own receptionists. **Yelp** launched Yelp Host ($149/month, or $99 for Guest Manager users) and Yelp Receptionist (from $99/month) in fall 2025. **Jobber** made its AI Receptionist generally available for home services and reports 200,000+ conversations. — [Restaurant Technology News](https://restauranttechnologynews.com/2025/10/yelp-expands-ai-portfolio-with-new-tools-to-handle-restaurant-calls-bookings-and-guest-inquiries/); [TechCrunch, Apr 2025](https://techcrunch.com/2025/04/29/yelp-is-adding-ai-powered-voice-agents-for-restaurants-and-services); [Agile Brand Guide](https://agilebrandguide.com/jobber-launches-ai-powered-receptionist-to-answer-calls-and-texts-for-busy-home-service-businesses/)
- Slang.ai (restaurants) closed a $36M Series B. — [Pulse 2.0](https://pulse2.com/slang-ai-36-million-series-b/amp/)
- Goodcall: its only verified funding is a $4M seed (2021), launched with a Yelp partnership. No customer count is public. — [TechCrunch 2021](https://techcrunch.com/2021/09/01/goodcall-picks-up-4m-yelp-partnership-to-answer-merchant-inbound-calls)

**Published SMB prices (US)**
- **Smith.ai** AI receptionist: a June 10, 2026 snapshot showed Starter $95/30 calls, Basic $270/90 calls, Pro $800/300 calls, $2.40 per extra call and $3 per live-agent handoff. A June 22 recheck found the page now leads with a **$500/month "Managed" plan** and no longer shows the self-serve tiers. Human virtual-receptionist tiers are about $300, $810 and $2,100/month. [AGG] — [FrontDeskReview](https://frontdeskreview.com/ai-receptionists/vendors/smith-ai/); [PricingSaaS](https://pricingsaas.com/companies/smith)
- **Goodcall**: $79 / $129 / $249 per agent per month, covering 100 / 250 / 500 *unique callers*, with unlimited minutes and $0.50 per extra caller. One phone line equals one agent. 14-day trial. Older 2025 guides showed a $59 entry plan. [AGG/competitor] — [CloudTalk](https://www.cloudtalk.io/blog/goodcall-pricing/); [ServiceAgent](https://serviceagent.ai/blogs/goodcall-pricing/)
- **Rosie**: $49/250 min (message-taking only, no booking), $149/1,000 min (booking and transfers), $299/2,000 min. 7-day trial; every call rounds up to a full minute. Sources disagree on overage ($0.25/min versus an auto-upgrade). Rosie claims "over 2,000 businesses". [competitor] — [CloudTalk](https://cloudtalk.io/blog/rosie-ai-answering-service-pricing); [Quo](https://www.quo.com/blog/rosie-ai-pricing/)
- **My AI Front Desk**: free plan (20 min), "Business-in-a-Box" $99/month with 200 minutes ($79 billed annually), $0.25/min overage. [VENDOR] — [My AI Front Desk](https://www.myaifrontdesk.com/blogs/my-ai-front-desk-pricing-2026-unpacking-the-costs-of-your-virtual-receptionist)
- **Dialzara**: $29/60 min, $99/220 min, $199/500 min, $349/1,000 min, with overage of $0.35–$0.48/min. Outbound voice plans cost $750–$1,500/month. [competitor] — [CloudTalk](https://www.cloudtalk.io/dialzara-pricing/)
- **Upfirst**: $24.95/30 calls, $59.95/90, $159.95/300, $299/600, with $0.70–$1.50 per extra call and 20% off annually. [competitor] — [AInora](https://ainora.lt/blog/dialzara-vs-upfirst-ai-receptionist-comparison-2026)
- A vendor-side summary range for SMB AI receptionists is "$49–$299/month", against $30,000–$60,000/year for a human receptionist. [VENDOR] — [Brilo](https://brilo.ai/resources/ai-receptionist-trends-2026)
- Sameday AI (YC W23, trades): I could not find a published price. Funding data is inconsistent ($125K–$500K). — [ToolChase](https://toolchase.com/tool/sameday/); [StartupHub](https://www.startuphub.ai/startups/sameday.md)
- Air AI: see Q6. It was sued by the FTC and is not a credible SMB product benchmark.

**Infrastructure/platform costs (what agencies build on)**
- **Vapi**: $0.05/min platform fee plus STT, LLM and TTS at provider cost (or bring your own keys), with telephony extra. Realistic all-in is about $0.07–$0.25+/min. Includes 10 concurrent lines, then $10/line/month. HIPAA add-on $2,000/month. [AGG/competitor] — [Layer3 Labs](https://www.layer3labs.io/guides/vapi-pricing); [Trillet](https://trillet.ai/blogs/vapi-pricing-per-minute)
- **Retell**: about $0.07/min base. Realistic all-in is about $0.11–$0.135/min, depending on LLM and voice. — [andrew.ooo](https://andrew.ooo/answers/retell-vs-vapi-vs-bland-voice-agents-april-2026/); [BetOnAI](https://betonai.net/?p=1872)
- **Bland**: Start $0.14/min (no platform fee), Build $299/month + $0.12/min, Scale $499/month + $0.11/min. Telephony may be extra. — [FrontDeskReview](https://frontdeskreview.com/software/ai-voice-agents/bland-ai/); [PricingSaaS](https://pricingsaas.com/companies/bland)
- **Synthflow**: voice engine $0.09/min, plus LLM $0.02–$0.05 and telephony about $0.02, for a real cost of about $0.13–$0.20+/min. Its billing docs list Pay-As-You-Go at $0.15–$0.24/min and say the old Pro/Agency plans are being phased out for new subscribers. — [Ringly](https://www.ringly.io/blog/synthflow-pricing); [Synthflow billing docs](https://docs.synthflow.ai/billing)
- **HighLevel Voice AI**: sources conflict. One guide gives $0.13/min agency-level (1-minute minimum, 6-second rounding). Another cites a $0.045/min voice-engine meter effective 20 May 2026. An "AI Employee Unlimited" plan costs $97/month per sub-account with unlimited Voice AI minutes, telephony metered separately. [AGG/affiliate] — [NetPartners](https://netpartners.marketing/gohighlevel-voice-ai-conversation-ai-pricing-2026/); [The Stack Insiders](https://www.thestackinsiders.com/blog/gohighlevel-voice-ai-cost); [GHL Central](https://ghlcentral.com/?p=19044)
- At 20,000 minutes/month, one comparison estimates Vapi ≈ $2,101, Retell ≈ $2,202 and Bland ≈ $2,869. — [BetOnAI](https://betonai.net/?p=1872)

**UK and EU prices**
- **UK**: Moneypenny does not publish prices. Third-party figures put live-answer tiers at about £145 (90 min) and £259 (150 min), with overage at £1.65–£1.85/min. Its AI voice agent is a quote-only add-on. — [ServiceAgent](https://serviceagent.ai/blogs/moneypenny-pricing/). UK AI receptionist range: £99–£2,000+/month with most SMEs at £150–£500 ([Softomate](https://www.softomatesolutions.com/blog/ai-receptionist-pricing-uk/), a custom builder), or £30–£500+ ([Fasthosts](https://www.fasthosts.co.uk/blog/how-much-does-an-ai-receptionist-cost/)). A full-time UK receptionist costs about £24,000–£35,000+/year ([Fasthosts](https://www.fasthosts.co.uk/blog/how-much-does-an-ai-receptionist-cost/)). BT has added an AI Receptionist to its UK business offer ([Mobile World Live](https://www.mobileworldlive.com/?p=514888)).
- **EU (DACH)**: fonio.ai Solo €99/month (annual) or €119 (monthly) for 1,000 minutes and 1 concurrent call, the hard limit being that a second simultaneous caller doesn't reach the AI. Team €299/€359 (3 concurrent calls, outbound). Scale €499/€599. Extra minutes €15 per 100. No trial but a 30-day money-back guarantee. — [CloudTalk on fonio](https://www.cloudtalk.io/blog/fonio-ai-pricing/). Famulor: €0.18/min prepaid with no base fee, or from €27/month for 100 minutes (annual); Agency tier overage €0.12/min; telephony extra. Famulor's own example: a medical practice with 800 calls × 2 min pays €288/month. — [Famulor cost guide](https://www.famulor.io/de/ki-telefonassistent-kosten)

### Inferences
- The retail SMB price anchor abroad is now **$50–$300/month for self-serve**, and big distribution platforms (RingCentral, Yelp, Jobber, BT) bundle receptionists at about $99–$149/month. An agency's managed service must justify a premium over these through setup, integration, monitoring and local language, not through the AI itself.
- Infrastructure at roughly $0.10–$0.20/min means a typical local SMB using 300–800 minutes/month costs an agency about $30–$160/month in usage, before platform fees and telephony (my arithmetic from the cited per-minute ranges).
- Beside's implied ~$17/month ARPU and Goodcall/Upfirst's $25–$79 entry tiers show that the low end of the market is being commoditized by product companies. Agencies survive in the gap between DIY tools and expensive human answering services such as Smith.ai and Moneypenny.

### Gaps
- No credible, methodology-backed SMB-specific market size for 2025–2026. Analyst reports (Grand View, market.us, Business Research Insights) could not be opened.
- No published customer counts or churn for Goodcall, Smith.ai, My AI Front Desk, Dialzara or Upfirst.
- Vendor pricing pages themselves could not be fetched, so all prices are third-party snapshots and may have changed.
- Could not confirm the current HighLevel Voice AI per-minute rate. Sources conflict between $0.13 and $0.045 plus LLM.

## 2. How does the agency/reseller model work, what do agencies charge, and what are realistic revenue, clients per operator and margins?

### Takeaway
The model is real and well tooled. An agency builds on HighLevel, Synthflow, Vapi, Retell or a white-label receptionist such as My AI Front Desk, puts each client in a sub-account, and rebills usage at a markup. Commonly cited pricing is $0–$1,500 setup plus $297–$500/month for a single-location trade, with more for dental, legal and medical. Almost all revenue, margin and client-count figures come from platform vendors and course sellers with an interest in making the model look lucrative. I found **no independent or audited data** on solo-operator revenue, client counts or margins.

### Cited Findings
**Mechanics**
- HighLevel lets agencies rebill AI usage to client sub-accounts in two ways. **Markup** charges e.g. 1.5× or 2× the actual token cost. **Fixed rate** charges e.g. $0.10 per Voice AI minute while the agency pays actual consumption, keeping the spread. Models can differ by product and sub-account. [VENDOR help center, via snippet] — [HighLevel Help: Fixed-Rate Rebilling](https://help.gohighlevel.com/support/solutions/articles/155000008422-fixed-rate-rebilling-for-ai-products)
- A third-party HighLevel guide says AI rebilling needs the $497/month Agency Pro plan (unconfirmed). It gives a "common arrangement" of charging a client **$297/month** for an AI receptionist that costs the agency **$97 plus telephony**. — [NetPartners](https://netpartners.marketing/gohighlevel-voice-ai-conversation-ai-pricing-2026/) / [The Stack Insiders](https://www.thestackinsiders.com/blog/gohighlevel-voice-ai-cost) (snippet did not make clear which of these two pages)
- HighLevel shipped Voice AI "snapshots" (February 2025), letting an agency clone a configured agent, settings and workflows to other client sub-accounts minus the phone number. That is the core of templated reselling. Usage fees are drawn from an agency "wallet". — [HighLevel Help: Voice AI snapshots](https://help.gohighlevel.com/support/solutions/articles/155000005151-voice-ai-configuration-support-for-snapshots); [HighLevel AI plans](https://help.gohighlevel.com/support/solutions/articles/155000008991-choosing-the-right-highlevel-ai-plan)
- HighLevel's last first-party customer count was 20,000+ customers at end-2022, with 1,582 "SaaS-mode" agencies running about 12,000 sub-accounts (≈7.6 sub-accounts per SaaS agency, my arithmetic). Later job ads claim "over 2 million businesses" on the platform. — [HighLevel 2022 review](https://www.gohighlevel.com/post/highlevel-2022-year-in-review)
- Synthflow white-label offers your own logo, sub-accounts, your own plans and minute allocations, and usage-based pricing for sub-accounts. The legacy Agency plan was listed at about **$1,250/month** (with 6,000 minutes, extra at $0.15/min) but is being phased out for new subscribers. A competitor claims Synthflow now charges $2,000/month for white-label or ~$30,000/year Enterprise (unverified). — [Synthflow docs](https://docs.synthflow.ai/docs/new-agency-whitelabel-overview); [TopAdvisor](https://www.topadvisor.com/products/synthflow/pricing); [Synthflow billing](https://docs.synthflow.ai/billing); [Trillet (competitor)](https://trillet.ai/blogs/synthflow-alternative-for-agencies)
- My AI Front Desk white-label: free reseller signup. The reseller buys each receptionist (vendor blog: **$54.99 wholesale**, unclear if monthly) and resells at any price via Stripe rebilling, with custom domain, unlimited sub-accounts and sales scripts. The vendor claims 70–90% margins at $250–$500+/month client prices. A competitor says the program "starts around $500/month" and is application-based. — [My AI Front Desk white-label blog](https://www.myaifrontdesk.com/blogs/unlock-agency-growth-transparent-my-ai-front-desk-white-label-pricing-revealed); [MAIFD tutorial](https://www.myaifrontdesk.com/tutorials/how-to-sign-up-as-a-white-label-reseller-for-my-ai-front-desk); [Autocalls (competitor)](https://autocalls.ai/article/my-ai-front-desk-pricing)
- Famulor (EU) has an "Agency" tier with €0.12/min overage. — [Famulor](https://www.famulor.io/de/ki-telefonassistent-kosten)

**What agencies charge clients (all VENDOR/course sources)**
- Trillet (white-label voice platform):
  - Single-location trades, professional services and retail: **$297–$497/month**.
  - Setup: **no fee for HVAC, plumbing, roofing and landscaping** (the monthly fee covers setup time); **$500–$1,500** for dental, medical and legal (compliance and PMS integration); $250–$500 per location for multi-location.
  - Claims 60%+ margin at $397/month. Its business-model guide gives $297–$997/month and $500–$2,000 setup.
  - Sources: [Trillet pricing guide](https://www.trillet.ai/blogs/voice-agent-pricing-strategy-guide); [Trillet: how agencies should price](https://trillet.ai/blogs/how-agencies-should-price-voice-ai-services); [Trillet business model](https://trillet.ai/blogs/voice-ai-agency-business-model)
- Ciela (agency-pricing guide): $300–$800/month for a single agent and $1,500–$5,000 setup for a single-purpose agent. It argues for value-based rather than cost-plus pricing. — [Ciela](https://ciela.ai/blogs/how-much-to-charge-for-ai-voice-agent)
- A Skool training community says its builds run "~$6K to $12K per build". A forum poster notes some people sell voice agents for **$199/month** after the setup fee, showing price pressure. — [Skool Q&A](https://www.skool.com/brendan/inside-this-weeks-qa-how-to-actually-price-voice-ai); [Skool: Are AI voice agents profitable?](https://www.skool.com/learn-ai/are-ai-voice-agents-profitable)
- A course seller advertises "$1,000+ to set it up, and $500/mo to keep it running". — [Whop course listing](https://whop.com/ai-receptionist-mastery)
- Buldrr claims from "50+ business deployments": $3,000 setup for starter agents up to $15,000+, with retainers of $300–$1,500/month. — [Buldrr](https://buldrr.com/7-ai-agents-businesses-are-paying-for-in-2026/)
- Growwstacks recommends charging ~10% of assumed lost revenue. Its dental example (7 missed calls/day × $150) yields **$3,150/month**, a pitch number rather than an observed price. — [Growwstacks](https://growwstacks.com/blog/how-to-sell-ai-receptionist)
- A vendor piece says AI-agency tooling typically runs about $75–$150/month, cheaper than the old social-media-agency model. — [Ciela: Is AI automation agency a scam?](https://ciela.ai/blogs/is-ai-automation-agency-a-scam)
- Prices are reportedly falling. One source claims AI voice pricing dropped 40% since 2024, without citing data. — [Superdupr](https://superdupr.com/blog/ai-voice-agent-cost)

**Agency revenue, client counts and margins (scarce, unverified)**
- A business-broker listing for a 7-year-old AI automation agency in Tampa (not receptionist-specific) reports **26 active clients** on 12-month auto-renewing retainers with 60-day notice, and **3% annual client churn**. This is a seller's document. — [BusinessBroker.net](https://www.businessbroker.net/business-for-sale/ai-agent-automation-and-enterprise-transformation-tampa-florida/1015443.aspx)
- The subreddit r/voice_ai_agency had only about 253 members, too small for benchmarks. — [GummySearch](https://gummysearch.com/r/voice_ai_agency/)
- Agencies recruit commission-only cold callers at **15% of each closed deal on $3k–$8k offers**. That implies typical first-year contract values of about $3k–$8k at those agencies (my inference from the offer sizes). — [Skool job post](https://www.skool.com/ai-automation-society/hiring-commission-only-cold-callers-ai-receptionist)
- Vendasta's AI receptionist "success stories" cite client revenue (e.g. a pet/vet business at $47k monthly revenue; a real-estate auction house with $20k–$30k estimated commission) but no baseline or agency economics. — [Vendasta](https://www.vendasta.com/ai-employee-types-success-story/ai-receptionist/)
- A practitioner video critique says YouTube is full of young creators claiming $200k–$300k/month from AI agencies. The speaker says most of his own 100k+ earnings came from teaching and community, not agency work. — [Gist summary of YouTube video](https://gist.ly/youtube-summarizer/the-truth-about-ai-agency-income-claims)
- SaaStr argues AI-agent revenue is fragile because "prompts are portable" and every customer re-decides buy/no-buy every 12 months. — [SaaStr](https://www.saastr.com/the-wave-of-ai-agent-churn-to-come-prompts-are-portable)

### Inferences
- Unit economics on paper look attractive. A $297–$497/month retainer against about $30–$160/month in usage plus a share of platform fees (e.g. HighLevel $97/sub-account, or Agency Pro $497 spread over clients) gives gross margins of roughly 50–80% per client at modest call volumes. But this rests on vendor price points, and churn (see Q5) dominates lifetime value.
- For a solo operator, the realistic constraint is not technology but sales and account management. The agencies with real numbers (the broker listing) have ~26 clients after 7 years with annual contracts. There is no evidence that solo receptionist agencies routinely reach 50+ clients.
- Setup fees appear to be negotiable or zero for simple trades, so first-month cash comes mostly from the retainer. Higher setup fees are tied to integration-heavy verticals (dental, medical, legal).

### Gaps
- No independent data (survey, tax, platform disclosure) on the number of clients per solo AI receptionist agency, median MRR, or net margin after the operator's time.
- Could not read Reddit threads (r/AI_Agents, r/automation, r/smallbusiness, r/sweatystartup); both search and fetch of reddit.com are blocked in this environment.
- No first-party data from HighLevel, Synthflow, Vapi or Retell on how many of their customers are agencies, or on agency survival rates.

## 3. Which SMB verticals adopt AI phone answering most, and why?

### Takeaway
Adoption clusters where (a) calls are the main lead channel, (b) staff are busy with hands-on work or patients, (c) the value per booked job or patient is high, and (d) after-hours demand exists. That points to **home services and trades (HVAC, plumbing, roofing, electrical), healthcare/dental, legal intake, restaurants (reservations) and auto repair**. Funding and product launches (Avoca for HVAC, Slang.ai for restaurants, Jobber for trades, Yelp for restaurants and services) are the strongest evidence. The vertical adoption percentages in circulation trace back mostly to one vendor compilation and are unverified.

### Cited Findings
- Vertical adoption percentages, all from one vendor stats page with sources I could not open [VENDOR, unverified]:
  - Healthcare: 38% of US/EU healthcare practices deployed AI for phone answering, scheduling or triage in 2025, up from 12% in 2023.
  - Legal: ~30% of firms use AI for intake or after-hours routing, 36% among 2–10 attorney firms (attributed to the ABA 2025 Legal Technology Survey).
  - Dental clinics using AI phone systems: 29% in Western Europe, 34% in the Nordics.
  - Other sectors: 19% of hotels with 50+ rooms; 19% of independent repair shops (2× more often at 5+ bay shops); beauty/wellness 17%; real estate 15%; veterinary 14%.
  - Source: [AInora stats](https://ainora.lt/blog/ai-receptionist-statistics-2026)
- A directory counts 200+ AI receptionist tools across 15 verticals (dental, home services, legal, restaurants, healthcare, real estate, automotive, etc.), meaning the market has "gone vertical". — [Stork.ai](https://www.stork.ai/blog/ai-receptionists-by-industry-2026)
- **Home services/trades**: Avoca's $1B valuation is built on HVAC, plumbing, roofing and electrical. Its founders pivoted from restaurants after meeting an HVAC firm. — [Idlen](https://www.idlen.io/news/avoca-ai-1-billion-valuation-kleiner-perkins-services-economy-voice-agents-april-2026). Jobber built its receptionist for "in-demand and on-the-go service pros" — [Agile Brand Guide](https://agilebrandguide.com/jobber-launches-ai-powered-receptionist-to-answer-calls-and-texts-for-busy-home-service-businesses/). Rosie names plumbing, HVAC, construction, real estate, law, salons and automotive as its core users — [Quo](https://www.quo.com/blog/rosie-ai-pricing/). Vendor content argues conventional answering services get overwhelmed during weather-driven call spikes [VENDOR] — [Callin.io](https://callin.io/answering-service-for-hvac-company-2/)
- **Restaurants**: dedicated vendors (Slang.ai, Yelp Host) handle reservations and FAQs. Slang reports about 15% of calls arriving after hours and large shares of overlapping calls (e.g. 13.4k of 62k), plus a testimonial that "80% of calls would go unanswered because staff was too busy". [VENDOR] — [Slang: The Restaurant People](https://www.slang.ai/customers/the-restaurant-people); [Slang customers](https://slang.ai/customers)
- **Medical/legal/home services/real estate missed-call rates** (CallRail, January 2025 small-business benchmark): medical 32%, legal 28%, home services 14%, real estate 9%. The healthcare and legal miss rates are highest, which explains vendor focus there. [VENDOR but a large call-tracking dataset] — [CallRail via BusinessWire](https://www.businesswire.com/news/home/20250114793850/en/CallRail-Releases-Report-Benchmarking-Marketing-Efforts-for-Small-Businesses)
- Dental/medical/legal deployments carry higher setup fees ($500–$1,500) because of compliance and practice-management integration (insurance checks, booking by provider/operatory). [VENDOR] — [Trillet](https://trillet.ai/blogs/how-agencies-should-price-voice-ai-services); [AInora](https://ainora.lt/blog/ai-receptionist-statistics-2026)
- UK vendors name dental practices, estate agents, trades, solicitors and letting agents as high-ROI sectors. [VENDOR] — [Softomate UK guide](https://www.softomatesolutions.com/blog/ai-receptionist-uk-complete-guide/)
- Automotive: auto repair (19% adoption claim above). RingCentral and Yelp target general SMB services.

### Inferences
- The "why" is consistent across sources. These are owner-operated businesses where the person who answers the phone is also doing the work (on a roof, in a patient's mouth, in the kitchen), so calls are missed exactly when demand peaks. A single booked job or new patient is worth hundreds to thousands of dollars, so a $300/month tool pays back with one or two recovered jobs.
- Integration-light verticals (trades taking messages or booking estimate visits, salons using online booking tools) are easier for a solo agency to serve. Healthcare and legal pay more but carry compliance, PMS integration and liability burdens.
- The fact that vertical SaaS (Jobber, Yelp, ServiceTitan-integrated Rosie/Avoca) is bundling receptionists means an agency serving a vertical whose software already offers one faces built-in competition.

### Gaps
- No independent (non-vendor) adoption rates by vertical. The ABA, MGMA and dental association reports could not be accessed, so the AInora percentages remain unverified.
- No HVAC- or trades-specific adoption rate from a trade association.
- No EU-specific vertical data beyond the unverified dental figures.

## 4. Evidence on the underlying pain: missed calls, voicemail behavior and the value of a missed call

### Takeaway
Small businesses do miss a meaningful share of calls, but the rate depends heavily on definition and dataset. Measured figures range from **9–32% (CallRail by industry)** and **~48% not answered live (Invoca home services)** up to **~62% (411 Locals, a 2024 study of 85 businesses)**. Popular companion statistics, such as "85% never call back", "80% won't leave voicemail" and "$126,000/year lost", are **untraceable vendor marketing**. Calls are high-intent, but the famous "calls convert 10–15× better than web leads" figure dates from around 2013 and comes from a call-tracking vendor.

### Cited Findings
- **411 Locals (2024)**: of calls to 85 businesses across 58 industries, only 37.8% were answered by a live person. 37.8% went to voicemail and 24.3% got no response at all, giving the "62% unanswered" headline. 411 Locals is a local-marketing vendor, and I could not open the original. — [Getaira summary](https://getaira.io/blog/missed-business-calls-statistics); [AnswerConnect](https://www.answerconnect.com/blog/?p=8179)
- **CallRail (January 2025)**: missed-call rates of medical 32%, legal 28%, home services 14%, real estate 9%. Based on call-tracking data. [VENDOR, large dataset] — [BusinessWire](https://www.businesswire.com/news/home/20250114793850/en/CallRail-Releases-Report-Benchmarking-Marketing-Efforts-for-Small-Businesses)
- **Invoca 2026 home-services benchmark** (9 sub-industries): only 52% of callers reach a live person (65% when very short calls are excluded). 38% of digital-marketing calls are leads, and 55% of businesses never ask leads to buy or book. A sponsored page gives conflicting figures: 35% of answered calls are leads, 37% convert on the call, 35% never ask for the sale. [VENDOR] — [Invoca report page](https://invoca.com/reports/the-invoca-lead-conversion-benchmarks-report-2026); [Stealth Agents summary](https://stealthagents.com/research/home-services-missed-call-revenue-statistics-2026); [Pipelineon](https://pipelineon.com/blog/missed-lead-statistics-home-services/)
- Signpost: home-service contractors miss over a quarter of inbound calls. [VENDOR] — [Signpost](https://www.signpost.com/resources/8-key-stats-about-missed-calls)
- NextPhone analysis of about 1.4M calls across 2,074 businesses: 51.2% were real leads and 28.5% arrived after hours. [VENDOR] — [CallMissed](https://www.callmissed.com/blog/ai-receptionist-small-business-stop-losing-leads)
- Twig estimates SMBs miss 27–40% of inbound calls, with only 10–20% recovered via voicemail and callback. No methodology given. [VENDOR] — [Twig](https://twig.so/blog/ai-front-desk-missed-calls-lost-revenue-recovery)
- **UK**:
  - 47% (67 of 142) small businesses missed the first call in a telephone study commissioned by TelePA/Mendip Hub. Firms with a live answering service answered 85%. [VENDOR-commissioned] — [Alliance Virtual Offices](https://www.alliancevirtualoffices.com/virtual-office-blog/shocking-research-finds-small-businesses-miss-almost-half-of-incoming-calls/); [Comms Business](https://commsbusiness.co.uk/content/news/is-anyone-there)
  - A Time Etc test of 200 Birmingham small businesses found only 82 answered (~59% unanswered), and a Moneypenny survey of 300 micro-businesses found 33% failed to answer (both vendors). — [Moneypenny small business call report](https://www.moneypenny.com/uk/resources/news/small-business-call-report/)
  - BT estimates UK small businesses lose £3.7bn/year to missed calls (BT sells an AI receptionist). — [Mobile World Live](https://www.mobileworldlive.com/?p=514888)
- **Voicemail behavior**:
  - A CallRail 2025 survey of 1,000 US consumers found 42% *say* they leave a voicemail when a business doesn't answer. A 2026 roundup says platform data shows fewer than 3% actually do (secondhand, unverified). — [JustCall voicemail stats](https://justcall.io/blog/voicemail-statistics-2026.html)
  - The widely repeated "80% of callers sent to voicemail don't leave a message" traces back to a November 2014 Information Today article crediting an unlocated Forbes piece. — [Information Today, Nov 2014](https://read.nxtbook.com/informationtoday/crm/november2014/insight_businessvoicemail.html); [SellCell](https://www.sellcell.com/blog/voicemail-statistics/)
- **Fact-checks of popular statistics**: Beside (itself an AI receptionist vendor) labels "missed calls cost small businesses $126,000 a year" as untraceable and says "85% of callers never call back" has no primary source. Both are still widely repeated, e.g. "62% missed, 85% never call back" on Brilo. — [Beside](https://beside.com/blog/missed-calls-cost-small-business); [Brilo](https://brilo.ai/resources/ai-receptionist-trends-2026)
- **Value of calls**: "Inbound phone calls are 10–15× more likely to convert than web leads" comes from Convirza research reposted around 2013 and is reused by Invoca and others. A SEMrush-hosted deck claims 31% of calls convert to revenue within 3 months versus 2% of web leads (source unnamed). — [Conversion Sciences](https://conversionsciences.com/mobile-phone-calls-higher-conversion-rates/); [SlideShare/SEMrush](https://www.slideshare.net/slideshow/semrush-webinar-why-calls-are-better-than-clicks/51114945)
- A hypothetical value-per-missed-call calculation: a 25% call-to-customer rate × $2,000 customer value ≈ $500 per missed call. [VENDOR, illustrative] — [Callin.io](https://callin.io/missing-calls-case-study/)
- MaxContact (UK 2025): 55% of people abandon calls when waits get too long. — [MaxContact](https://www.maxcontact.com/articles/what-uk-customers-really-want-from-contact-centres-in-2025)

### Inferences
- The pain is real but smaller and more variable than agency pitch decks claim. A defensible pitch uses the business's own call logs (or a mystery-call test) rather than the 62% / 85% / $126k figures.
- After-hours share (~15–28% of calls in the vendor datasets) and overlapping calls during peaks are the most concrete, measurable reasons an AI answerer adds value even for businesses that "usually answer".
- Since most callers who reach voicemail don't leave messages (self-report 42%, platform data far lower), "voicemail is fine" is a weak objection. But measured callback and loss rates are not well documented.

### Gaps
- No independent academic or government study of SMB missed-call rates in the US, UK or EU.
- Original 411 Locals, Invoca and CallRail reports could not be opened to check methodology.
- No credible, measured "value of a missed call" by vertical. Only vendor hypotheticals exist.
- No data on missed-call rates in EU countries outside the UK.

## 5. Outcomes and retention: measured results, churn, satisfaction and caller acceptance of AI voices

### Takeaway
Vendor case studies show large call volumes handled and bookings captured, e.g. Slang.ai restaurants with about 50% of calls fully automated and thousands of reservations. Before/after controlled results are rare. Caller attitudes are mixed. Surveys show **~29–31% say they'd hang up on an AI** and **58–85% prefer a human**, especially for complex or urgent issues. But the largest behavioral dataset (Upfirst, 450k calls) found that **disclosing the AI is associated with ~20% fewer hang-ups**, and most hang-ups happen in the first seconds regardless of configuration. Churn data is all vendor-sourced and contradictory, from 3–5% per month up to double-digit monthly churn in an agency's first year. General SMB SaaS churn runs 3–7% per month.

### Cited Findings
**Measured outcomes (vendor case studies)**
- Slang.ai, Fireman Hospitality Group: over 90 days, ~27,000 inbound calls (2,500+ simultaneous) and 2,400+ reservations, ~8% of them after hours via the OpenTable integration. No before/after booking %. [VENDOR] — [Slang case](https://slang.ai/customers/fireman-hospitality-group)
- Slang.ai, The Restaurant People: over 4 months, 62,000+ calls with no staff involvement, 3,200+ reservations, 15% after hours, 94.6% caller satisfaction. [VENDOR] — [Slang case](https://www.slang.ai/customers/the-restaurant-people)
- Slang.ai, PLANTA: 87,578 calls in a year, 50% fully handled without humans, 3,598 reservations. [VENDOR] — [CaseStudies.com](https://www.casestudies.com/company/slangai/case-study/planta-answers-87578-calls-with-slangai)
- Slang's homepage claims 85% CSAT, 50% of calls handled and an "80% increase in reservations" (not tied to a client). A trade article relays a vendor claim of a 2× increase in phone reservations for Texas de Brazil, Carmine's, Riot Hospitality and Dineamic. [VENDOR] — [Slang.ai](https://slang.ai/); [Pulse 2.0](https://pulse2.com/slang-ai-36-million-series-b/amp/)
- Jobber AI Receptionist: 200,000+ conversations since its August 2025 launch. No booking-rate data published. [VENDOR/directory] — [Stork.ai on Jobber](https://www.stork.ai/en/jobber-ai-receptionist-2)
- A small product company's "year in review" reports 8,000+ calls handled in 2025. [VENDOR] — [ai-receptionist.com](https://ai-receptionist.com/blog/year-in-review-2025/)
- Deepgram/Opus Research State of Voice AI 2025 (400 senior leaders, mostly large enterprises): only ~1 in 5 were very satisfied with their *traditional* voice agents. [VENDOR-sponsored, enterprise] — [Deepgram](https://deepgram.com/learn/state-of-voice-ai-2025)

**Caller acceptance: behavioral data**
- **Upfirst report (July 2026)**, about 450,700 inbound calls across 503 AI receptionist deployments, each with 200+ completed calls [VENDOR but behavioral]:
  - Configuration (greeting, voice, training) explained only ~13% of the *variation in hang-up rates between businesses*. Many hang-ups happened in the first seconds.
  - **Disclosing that it's an AI was associated with ~20% lower hang-ups.**
  - Also associated with fewer hang-ups: greeting with the business name, ending the opener with a question, mentioning that calls may be recorded, and enabling booking, transfers and SMS.
  - Voice gender, greeting length and question phrasing had no measurable effect.
  - The co-founder's advice: "Your raw hang-up rate grades your phone number's reputation more than your receptionist."
  - Findings are correlational.
  - Sources: [NewsBytes](https://www.newsbytesapp.com/news/science/upfirst-report-finds-companies-fine-tune-ai-receptionists-to-cut-hang-ups/tldr); [Devdiscourse](https://www.devdiscourse.com/article/business/3957545-ai-customer-service-enters-next-phase-as-businesses-focus-on-optimisation-rather-than-adoption-report)

**Caller acceptance: surveys (stated preference)**
- OnePoll for serviceforge (a home-services software vendor), October 2025, 6,000 adults:
  - 29% would hang up on reaching AI, 33% would continue, 33% not sure or "depends" (headlined as "1 in 3").
  - 85% prefer a real person when contacting a *local service*; 83% have asked to speak to a human instead of AI; 54% find AI customer service frustrating.
  - Sources: [serviceforge PDF](https://assets.serviceforge.com/serviceforge/pdf/ai-survey-report-serviceforge.pdf); [serviceforge report page](https://www.serviceforge.com/ai-report)
- Gartner (survey of 5,728 customers, December 2023; published July 2024; older data) [INDEP]:
  - **64% would prefer companies didn't use AI for customer service**; 53% would consider switching to a competitor.
  - Top concern: it will be harder to reach a person; then job loss and wrong answers.
  - Source: [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2024-07-09-gartner-survey-finds-64-percent-of-customers-would-prefer-that-companies-didnt-use-ai-for-customer-service)
- MaxContact UK 2025 (contact-centre vendor):
  - Humans preferred for unique situations (70%), emergencies (67%) and complaints (61%).
  - 45% are comfortable with AI chatbots and assistants, 36% uncomfortable. Comfort is 65% among 25–34-year-olds versus 27% among over-55s.
  - Source: [MaxContact](https://www.maxcontact.com/articles/what-uk-customers-really-want-from-contact-centres-in-2025)
- TCN 2025 US consumer survey: 58% still prefer a live phone agent, up year on year. [VENDOR] — [TCN](https://www.tcn.com/resources/2025-consumer-survey-results-ebook/)
- NextPhone blog: 49% prefer a human, 12% AI, 25% "depends", 14% no preference; 51% prefer AI when they want immediate service. [VENDOR] — [NextPhone](https://www.getnextphone.com/blog/customers-prefer-ai-or-human-receptionist)

**Churn and retention (all VENDOR, contradictory)**
- SMB SaaS benchmark: **3–7% monthly churn (≈30–58% annual)**, citing Recurly/Paddle 2025, against 0.3–1% monthly for B2B SaaS overall. [VENDOR blog citing benchmarks] — [Vena](https://venasolutions.com/blog/saas-churn-rate)
- AI automation agency blog: SMB clients "commonly turn over at 3 to 5 percent per month", and ~70% of churn happens in the first 90 days. — [Ciela](https://ciela.ai/blogs/why-ai-automation-clients-churn-and-how-to-keep-them)
- Voice AI platform: "New voice AI agencies commonly see double-digit monthly churn in their first year". Clients with 4+ integrations churn far less than phone-only setups (anecdotal). — [Trillet churn reduction](https://trillet.ai/blogs/voice-agent-client-churn-reduction); [Trillet retention](https://trillet.ai/blogs/voice-agent-client-retention-strategies)
- Another vendor: "well-run" agencies see 5–8% monthly churn (12–20 month average client life), while "set it and forget it" accounts lose 10–20% of clients per month. It notes that at 15% monthly churn you lose half your clients in under 5 months. Its ranking of cancellation reasons is "illustrative, not a published benchmark". — [MyVoiceAIConnect](https://www.myvoiceaiconnect.com/blog/reduce-ai-receptionist-client-churn-rate)
- AI Frontdesk claims ~30% of users abandon AI tools within six months, citing a "Customer Service Institute" study that could not be located. [VENDOR] — [My AI Front Desk reseller blog](https://www.myaifrontdesk.com/reseller-blogs/how-to-prevent-ai-receptionist-churn-and-boost-your-client-retention)
- The broker-listed agency claims 3% *annual* churn on 12-month contracts (see Q2). — [BusinessBroker.net](https://www.businessbroker.net/business-for-sale/ai-agent-automation-and-enterprise-transformation-tampa-florida/1015443.aspx)

### Inferences
- Measured product outcomes are credible for restaurants: high call volume, simple intents (hours, reservations), and integration with OpenTable-type systems. Restaurant-group results may not transfer to a single-location trade with complex quoting.
- Caller resistance is real (about 3 in 10 say they'd hang up), but behavioral data suggests transparent disclosure plus useful capabilities (booking, transfer) reduces abandonment. That is convenient, since the EU AI Act requires disclosure anyway (Q6).
- Planning should assume SMB-typical churn of 3–7% per month unless clients sign annual contracts, and higher in the first 90 days. Lifetime value at $300/month with 5% monthly churn ≈ $6,000 gross (my arithmetic: 1/0.05 = 20 months).

### Gaps
- No independent, controlled before/after study of AI receptionist impact on SMB bookings or revenue.
- No published churn or retention figures from any AI receptionist product company (Goodcall, Rosie, Smith.ai, RingCentral AIR, etc.).
- No independent behavioral data on hang-up rates for AI versus voicemail versus human at SMBs, beyond Upfirst's vendor dataset.
- No EU-specific caller-acceptance survey (e.g. Germany, France, Romania) found.

## 6. What fails: cancellation reasons, caller complaints, hallucinations, integration, latency, accents, regulation, and agency hype

### Takeaway
Failures fall into four buckets:
1. **Setup and integration**: incomplete knowledge base leading to invented answers, calendar sync, wrong service durations, number porting, SMS registration.
2. **Speech-technology limits**: latency above ~500 ms, poor barge-in handling, accent and noise errors, edge cases.
3. **Client-relationship failure**: the client can't see ROI, the agent "works quietly" and gets cancelled anyway, templates are not customized.
4. **Legal/regulatory exposure**: TCPA consent for outbound calls and texts, US state bot-disclosure laws, California wiretap (CIPA) suits over AI listening to calls, the EU AI Act Art. 50 disclosure duty in force since 2 August 2026, and UK PECR for automated outbound calls.

The "AI agency" space also carries documented hype and fraud: the FTC sued Air AI in 2025 over deceptive earnings claims made to small businesses.

### Cited Findings
**Product and technical failure modes**
- Hallucination: Joist's support docs say that when the knowledge base is incomplete, its AI receptionist "can provide information that was not explicitly configured, mention names, services, or policies that don't exist, and make assumptions when information is missing". Bookipi says responses "can vary slightly each time". Moneypenny markets "patent-pending" drift and hallucination detection with human handoff. — [Joist support](https://support.joistapp.com/en/articles/15704750-how-does-ai-receptionist-respond-to-callers); [Bookipi](https://bookipi.com/au/wp-json/wp/v2/posts/18700); [Moneypenny](https://moneypenny.com/uk/videos/how-can-you-stop-an-ai-receptionist-from-guessing-or-hallucinating)
- Wrong bookings are mostly setup errors, according to a practitioner blog: calendars syncing too slowly, wrong service durations, rules living in the prompt instead of the booking system, misheard names or numbers. — [Sagnik Bhattacharya](https://sagnikbhattacharya.com/blog/ai-receptionist-booking-mistakes-fix). A RingCentral user feature request asks that AIR stop double-booking already-taken slots — [RingCentral Ideas](https://ideas.ringcentral.com/forums/958502-ai-conversation-expert-ace-formerly-ringsense/suggestions/51303631-ai-receptionist-should-not-allow-double-booking-fo)
- A Plivo talk on production failure modes lists five that teams "hit in week one": end-to-end latency (target under 550 ms to first audio, which may require disabling LLM reasoning modes), brittle STT, unstructured data collection, unnormalized TTS input, and turn detection/barge-in. Modeling inputs as typed schema fields raised data-collection accuracy from 30% to 95%. — [Sean Weldon summary of Plivo talk](https://www.sean-weldon.com/blog/2026-09-17-5-voice-agent-failure-modes-youll-hit-in-week-one-venky-b-plivo)
- Other guides make the same points:
  - Latency is "the number-one production failure", with the STT→LLM→TTS pipeline needing to finish in under 500 ms.
  - Barge-in has two failure directions: the agent flinches at coughs, or talks over callers.
  - Agents handle "the easy 90%" and stumble on "the 10% that actually matters".
  - Problems often surface only via customer complaints, days or weeks late.
  - Sources: [Murf](https://murf.ai/blog/why-ai-voice-agents-fail-in-production); [AlexCloudStar](https://alexcloudstar.com/blog/ai-voice-agents-production-2026/); [The Silicon Review](https://thesiliconreview.com/2026/08/real-time-voice-agents-latency-and-interruption-handling-are-the-real-product)
- Accents [INDEP research, partly old]:
  - A Washington Post-commissioned study (2018) found smart speakers were 30% less likely to understand non-American accents. A separate project found 35% word error rate for African American speakers versus 19% for white speakers across major vendors. — [VentureBeat](https://venturebeat.com/ai/study-finds-that-even-the-best-speech-recognition-systems-exhibit-bias)
  - An academic study of Dutch ASR found higher errors for regional and non-native accents. — [arXiv 2103.15122](https://arxiv.org/pdf/2103.15122)
  - A 2025 evaluation of Whisper, Wav2Vec2 and Vosk still found accent limitations. — [NHSJS 2025](https://nhsjs.com/wp-content/uploads/2025/12/Evaluating-the-Accessibility-of-Automatic-Speech-Recognition-Technology-Across-Accent-2.pdf)
- Concurrency limits: fonio's Solo plan allows only 1 concurrent call, so a second simultaneous caller doesn't reach the AI. — [CloudTalk on fonio](https://www.cloudtalk.io/blog/fonio-ai-pricing/)

**Why clients cancel (vendor sources, no independent study)**
- Churn verbatims compiled by a phone vendor:
  - Number port stalled 18 days, leaving the customer paying for two systems.
  - Reception-style businesses rejected softphone-only setups and wanted desk handsets.
  - Voicemail transcripts were too inaccurate to trust.
  - Source: [Allo churn verbatims](https://www.withallo.com/es/ai-workflows/churn-reasons-verbatims)
- "No visible ROI" is "consistently the largest single driver of cancellations". Another dominant type is the agent "ran quietly and they never noticed it". Unmodified industry templates also lead to cancellations. — [MyVoiceAIConnect](https://www.myvoiceaiconnect.com/blog/reduce-ai-receptionist-client-churn-rate); [MyVoiceAIConnect voice-quality complaints](https://www.myvoiceaiconnect.com/blog/client-complaints-ai-voice-quality-agency)
- Four fixable churn reasons per an AI automation agency: no early value, ROI not visible, "something broke quietly and eroded trust", no clear reporting. Clients "quietly cancel before Month 4". — [Ciela](https://ciela.ai/blogs/why-ai-automation-clients-churn-and-how-to-keep-them); [ScaleLogix on DEV](https://dev.to/scalelogix_ai/how-to-retain-ai-agency-clients-a-playbook-for-long-term-operator-success-521a)
- Guides advise promising only a *partial* replacement for a receptionist and widening the AI's autonomy only after reviewing 200–300 calls. — [Trillet sustainable agency](https://trillet.ai/blogs/building-sustainable-ai-voice-agency-2026)
- Missed-call text-back: if A2P 10DLC is not registered, carriers silently filter texts while dashboards show "sent", so the business thinks missed calls are being recovered. — [JustCall](https://justcall.io/blog/a2p-10dlc-text-incoming-caller.html); [NextPhone A2P guide](https://www.getnextphone.com/blog/a2p-10dlc-small-business-texting)

**Regulation: US**
- FCC Declaratory Ruling (adopted unanimously 8 February 2024): AI-generated voices, including cloned voices, are "artificial" under the TCPA. Calls using them need prior express consent (absent emergency or exemption), plus identification, disclosure and opt-out. The FCC, private plaintiffs and state AGs can enforce. Calls are illegal only if they fail the same TCPA rules as other artificial or prerecorded calls. [INDEP] — [FCC](https://WWW.FCC.GOV/document/fcc-makes-ai-generated-voices-robocalls-illegal); [Wilson Sonsini](https://wsgr.com/en/insights/fcc-rules-ai-generated-voices-are-artificial-under-the-tcpa.html); [Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/fcc-issues-declaratory-ruling-on-ai-generated-voice-robocalls)
- TCPA violations carry $500–$1,500 statutory damages each. There is no federal law requiring bots to self-identify. — [JustCall disclosure laws](https://justcall.io/blog/ai-voice-agent-disclosure-laws.html)
- TCPA consent revocation: the FCC adopted a new Report & Order on 30 September 2026 (one designated revocation method). The "revoke-all" provision is delayed to 31 January 2027. — [TCPAWorld](https://tcpaworld.com/2026/01/07/breaking-fcc-pushes-back-tcpa-consent-revocation-rule-new-effective-date-now-january-31-2027/); [Burr & Forman](https://www.burr.com/telephone-consumer-protection-act/2026/01)
- State bot-disclosure laws:
  - **Utah** AI Policy Act (SB 149, effective 1 May 2024): disclose generative AI when asked, and proactively in regulated occupations. Narrowed by SB 226 (May 2025). Fines up to $2,500 per violation. — [Davis Wright Tremaine](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2024/04/utah-enacts-ai-and-bot-business-disclosure-law); [Alston & Bird](https://www.alstonprivacy.com/new-artificial-intelligence-laws-in-effect-in-utah/)
  - **California**: the B.O.T. Act (2019) applies only to bots that "knowingly deceive" to drive a sale or vote. AB 2905 (reported effective 1 January 2025) requires disclosure of AI-generated voices in robocalls; penalty figures are unverified. — [Ashurst Perkins Coie](https://www.ashurstperkinscoie.com/en/insights/do-you-have-to-disclose-when-your-users-are-interacting-with-a-bot/); [Getaira compliance guide](https://www.getaira.io/resources/california-ai-voice-disclosure)
  - **Colorado**: reported bot-disclosure duty from 1 February 2026 (unverified). — [JustCall](https://justcall.io/blog/ai-voice-agent-disclosure-laws.html)
- **Wiretap/CIPA risk**: in *Ambriz v. Google* (N.D. Cal.), the court on 10 February 2025 let a class action proceed alleging that Google's Contact Center AI "listened" to Verizon customer calls in violation of California's Invasion of Privacy Act. The theory was that a vendor with the *capability* to use call data for its own purposes can be a third-party eavesdropper. The suit seeks $5,000 per violation, and a parallel suit names Home Depot. Commentators warn this applies to businesses using third-party AI voice tools. A December 2025 commentary says the Ninth Circuit's *Popa* decision may undercut it. [INDEP law firms] — [ZwillGen](https://www.zwillgen.com/privacy/federal-judge-allows-google-customer-service-ai-class-action-to-proceed/); [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2025/02/alerts-practices-dpc-ftec-ai-voice-products-subject-to-california-invasion-of-privacy-claims); [Maine Law SJIPL](https://sjipl.mainelaw.maine.edu/2025/12/18/the-collapse-of-capability-theory-ambriz-popa-and-the-future-of-article-iii-standing-in-ai-privacy-cases/)

**Regulation: EU and UK**
- **EU AI Act Article 50(1)** [INDEP law firms]:
  - Providers of AI systems that interact directly with people must ensure those people are told they're dealing with an AI unless that is obvious. The duty applies from **2 August 2026** and was not postponed by the Digital Omnibus.
  - The Commission published final non-binding Art. 50 guidelines on 20 July 2026: disclosure must be prominent, separate from other content, and given at the latest at first interaction. Guidance reads the "obvious" exception narrowly, so human-sounding voice agents must disclose, and a human name like "Sarah" is not enough.
  - Breaches fall in fine tier 2: up to €15M or 3% of worldwide turnover, with SMEs reportedly subject to the lower of the two.
  - Rebranding a white-label bot under your own name may make you a "provider" under Art. 25 (vendor/blog reading, not confirmed in Commission text).
  - Sources: [Pearl Cohen](https://www.pearlcohen.com/european-commission-publishes-final-guidelines-on-ai-transparency-obligations/); [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/ai-transparency-european-commissions-guidelines-on-article-50-part-2-deployer-obligations); [Covington / Inside Global Tech](https://www.insideglobaltech.com/2026/05/12/10-takeaways-european-commission-draft-guidelines-on-ai-transparency-under-the-eu-ai-act/); [Famulor (vendor)](https://www.famulor.io/blog/eu-ai-act-article-50-what-your-ai-phone-agent-must-say); [Aliteq checklist](https://aliteq.com/eu-ai-act-chatbot-disclosure-checklist)
- **UK** [mixed]:
  - Outbound automated or AI marketing calls fall under PECR Regulation 19 and require prior opt-in consent. TPS screening is not enough. — [DMA](https://www.dma.org.uk/about/articles/automated-outbound-contact-and-the-collapse-of-the-human-review)
  - The ICO fined two energy firms a combined £550,000 for millions of automated calls using "voice-avatar" software that made recipients think they were talking to local agents. — [Freevacy](https://www.freevacy.com/news/ico/ico-fines-two-energy-companies-ps550000-under-pecr-for-making-illegal-robocalls/6758)
  - For inbound AI receptionists, no UK rule expressly mandates AI disclosure, but UK GDPR fairness and transparency make it the default (DMA view). A claimed Ofcom "disclose within 5 seconds" rule could not be corroborated. — [DMA](https://www.dma.org.uk/about/articles/automated-outbound-contact-and-the-collapse-of-the-human-review); [Softomate GDPR/PECR guide](https://www.softomatesolutions.com/blog/gdpr-pecr-call-recording-ai-voice-agents-uk-2026/)

**Agency hype, fraud and failure**
- **FTC v. Air AI** (complaint August 2025, D. Ariz.) [INDEP]:
  - Air AI and its owners allegedly sold business coaching, an "Access Card" program and reseller licenses since February 2023 with claims that buyers would "earn back tens of thousands of dollars in a matter of days or months" and that some could make millions.
  - Victims, many of them small-business owners, lost up to $250,000 each, and "guaranteed" refunds were often denied. Alleged violations: the Business Opportunity Rule and the Telemarketing Sales Rule.
  - A March 2026 settlement bans Air AI from marketing business opportunities.
  - Sources: [FTC press release](https://search.ftc.gov/news-events/news/press-releases/2025/08/ftc-sues-stop-air-ai-using-deceptive-claims-about-business-growth-earnings-potential-refund); [FTC](https://www.ftc.gov/node/297672); [GRC Report](https://www.grcreport.com/post/ftc-sues-air-ai-over-deceptive-business-claims-seeks-to-halt-scheme-targeting-small-businesses)
- Gartner (June 2025) predicts over 40% of agentic AI projects will be cancelled by end-2027 due to cost, unclear value or risk controls. It warns of "agent washing", where chatbots, RPA or assistants are rebranded as agents. This is an enterprise forecast. [INDEP] — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- Critiques of "AI automation agency" content say:
  - Many YouTube "start an AI agency" creators earn mainly from courses and communities, not agencies.
  - The playbook "rhymes with the 2019 dropshipping and SMMA era".
  - Scarcity tactics ("only 3 spots left") are manufactured.
  - These come mostly via vendor blogs summarizing Reddit, so carry a conflict of interest. — [Ciela: AI automation agency Reddit honest truth](https://ciela.ai/blogs/ai-automation-agency-reddit-honest-truth); [Ciela: is it a scam](https://ciela.ai/blogs/is-ai-automation-agency-a-scam); [Gist YouTube summary](https://gist.ly/youtube-summarizer/the-truth-about-ai-agency-income-claims)
- Course and community products sell the dream directly: e.g. a $29.99/month community for selling AI receptionists, and courses promising "$10k/month in 60–90 days". — [Whop AI Reception Hub](https://whop.com/ai-reception-hub); [Growwstacks](https://growwstacks.com/blog/sell-ai-receptionists-local-businesses/)
- Structural risk: low switching costs, since "prompts are portable". — [SaaStr](https://www.saastr.com/the-wave-of-ai-agent-churn-to-come-prompts-are-portable)

### Inferences
- Most failure modes a solo operator can control are operational: knowledge-base completeness, calendar and booking-system integration, monthly ROI reporting, call review, SMS registration. That means real ongoing labor per client, which undercuts "passive income" claims.
- For an EU (Romanian) operator, Art. 50 disclosure ("this is an AI assistant for [business]") at the start of each call is now mandatory in practice. Upfirst's data suggests it may not hurt and may even help. If the agency white-labels and rebrands the system, it may itself be treated as a provider.
- GDPR call recording and processing (the controller/processor contract with the SMB, sub-processors outside the EU such as US LLM, STT and TTS vendors) is the EU analogue of the US CIPA risk. It is a legal workload an agency must handle per client.
- Outbound use (reminders, lead callbacks) carries much higher legal risk than inbound answering in the US (TCPA), the UK (PECR) and likely the EU (ePrivacy). A replicator should start with inbound only.
- The Air AI case shows that the riskiest part of this ecosystem is selling "AI agency" business opportunities, not the receptionist service itself. A founder should discount guru-sourced revenue claims.

### Gaps
- No systematic Trustpilot, G2 or Capterra analysis of 1–2 star reviews with cancellation reasons for specific products. Review pages could not be fetched, and search surfaced only a 4-review Trustpilot listing.
- No quantified hallucination or wrong-booking rates from any vendor or independent test.
- No data on ASR accuracy for Romanian (or other smaller EU languages) in AI receptionist stacks. This is a key unknown for Bucharest.
- Could not verify California AB 2905 penalty details, Colorado's effective date or the claimed Ofcom rule.
- No documented case of a specific small AI receptionist agency failing, with numbers. Only generic critiques.

## 7. How do agencies acquire SMB clients, and what conversion rates are reported?

### Takeaway
The standard playbook is demo-first outbound:
- Cold-call or cold-email local businesses in one niche, often after a "missed-call audit" or mystery call that shows the owner their own unanswered calls.
- Let the prospect call a live demo agent customized to their business.
- Price against the estimated value of lost calls.

Some agencies use commission-only callers. Distribution partnerships (Yelp, Jobber, RingCentral) dominate at the product level. **No credible conversion rates specific to AI receptionist sales were found.** Generic cold-email benchmarks are ~3–4% reply and ~0.7–1% meeting-booked per email sent.

### Cited Findings
- **Missed-call audit as an opener**:
  - Vendors describe a sequence of auditing missed-call rates, calculating revenue impact, then piloting after-hours coverage. — [Dialora](https://www.dialora.ai/blog/missed-calls-costing-bookings-ai-phone-agents); [Twig](https://twig.so/blog/ai-front-desk-missed-calls-lost-revenue-recovery)
  - A Vendasta partner feature request asks for a client-facing monthly report estimating lost revenue from missed calls (using the client's conversion rate and average customer value) to sell and retain AI receptionist clients. — [Vendasta feedback](https://feedback.vendasta.com/ai-workforce/p/client-facing-report-that-shows-missed-calls-by-month)
  - Mystery-caller assessments, calling at different times of day to test answer rates, are suggested. The example figures are unattributed. — [Callin.io](https://callin.io/missing-calls-case-study/)
- **Demo calls**: a sales blog says industry-specific, human-sounding demos "convert at 5–10X higher rates" (no source) and claims its cold-call script led to $5,000 demos (no conversion rate). [VENDOR/course] — [Growwstacks cold-call script](https://growwstacks.com/blog/ai-receptionist-cold-call-script); [Growwstacks cold calls](https://growwstacks.com/blog/sell-ai-receptionists-to-local-businesses-with-cold-calls/)
- **Commission-only appointment setters**: agencies hire cold callers on commission (15% of each closed deal on $3k–$8k offers; 10–15% for calling real-estate agencies), tracking show rate as a key metric. — [Skool hiring post 1](https://www.skool.com/ai-automation-society/hiring-commission-only-cold-callers-ai-receptionist); [Skool hiring post 2](https://www.skool.com/ai-automation-society/hiring-looking-for-cold-callers-appt-setters-ai-agency)
- **Value-based pricing as a closing tool**: charge a percentage (e.g. 10%) of the revenue the owner is estimated to lose to missed calls. — [Growwstacks](https://growwstacks.com/blog/how-to-sell-ai-receptionist). Ciela: "a price should reflect the value you protect, not the cost you incur" — [Ciela](https://ciela.ai/blogs/how-much-to-charge-for-ai-voice-agent)
- **Niche focus**: a columnist calls chasing any client instead of one niche a "$100,000 mistake" because ROI becomes hard to prove. Vertical niches and "demo-first outbound" are claimed to still have few serious operators (seller's claim). — [Stork.ai niche article](https://www.stork.ai/blog/this-ai-agency-mistake-costs-100k); [Ciela](https://ciela.ai/blogs/is-ai-automation-agency-a-scam)
- **Generic cold-email benchmarks** (B2B, not local-service specific):
  - A self-reported analysis of 200k+ cold emails (Q1 2026) found 3.7% average reply, 1.6% positive reply and 8.2 meetings booked per 1,000 emails. — [PuzzleInbox](https://puzzleinbox.com/community/i-analyzed-200k-cold-emails-sent-in-q1-2026-here-are-the-benchmarks)
  - Another analysis found 3.1% reply and 0.7% meeting-booked, needing ~4.8 touches to a first reply and 7.4 to book a meeting. — [Mean CEO blog](https://blog.mean.ceo/?p=10236)
  - Instantly benchmarks ~1% of sends turning into booked meetings. — [Instantly](https://instantly.ai/blog/meeting-email-metrics-to-track-response-booking-rates/)
- **Product-level distribution**: Goodcall launched via a Yelp partnership (2021). Yelp, Jobber, RingCentral and BT now sell receptionists inside existing SMB subscriptions, which is a channel advantage independent agencies lack. — [TechCrunch 2021](https://techcrunch.com/2021/09/01/goodcall-picks-up-4m-yelp-partnership-to-answer-merchant-inbound-calls); [Restaurant Technology News](https://restauranttechnologynews.com/2025/10/yelp-expands-ai-portfolio-with-new-tools-to-handle-restaurant-calls-bookings-and-guest-inquiries/); [No Jitter](https://nojitter.com/ucaas/ringcentral-posts-strong-ai-receptionist-customer-growth)
- **Expectation-setting in the sale**: practitioners advise selling a *partial* receptionist replacement and conservative escalation rules at launch, to avoid post-sale disappointment and churn. — [Trillet](https://trillet.ai/blogs/building-sustainable-ai-voice-agency-2026)
- **Guru demo content**: e.g. "The best cold call you've ever seen (178k/month AI agency)". The revenue claim is unverified. — [SozAI transcript](https://sozai.app/transcript/best-cold-call-ai-agency/index.md)

### Inferences
- At ~0.7–1.1% meetings per email (generic benchmarks), 10 demos would take roughly 900–1,400 well-targeted emails. With an unknown but plausibly modest demo-to-close rate, a part-time founder would need sustained outbound volume or warm referrals to reach 10–20 clients. This is my arithmetic; no AI receptionist close rates exist.
- The missed-call audit or mystery call is the most persuasive and cheapest opener because it turns abstract statistics (which are often untraceable) into the prospect's own evidence. It also sets up the monthly ROI report that the churn sources say drives retention.
- In Romania, the absence of a Yelp/Jobber-style bundled competitor may be an opening, but there are also fewer local distribution partners. Local accountant, telecom or booking-software partnerships would be the analogue of the Yelp/Goodcall channel (inference).

### Gaps
- No reported conversion rates (connect → demo → close) for AI receptionist offers to local businesses, from either independent or credible practitioner sources.
- No data on referral share or customer acquisition cost for AI receptionist agencies.
- Reddit practitioner threads, the most likely source of real-world funnel numbers, could not be accessed in this environment.
