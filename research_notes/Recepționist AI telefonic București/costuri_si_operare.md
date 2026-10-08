# Costuri și operare: recepționist AI telefonic (limba română, clienți IMM din București), furnizor solo cu 10–12 ore/săptămână

> Method note (read first): every attempt to open vendor pages directly (vapi.ai, retellai.com, elevenlabs.io, twilio.com, techsy.io, autocalls.ai, developers.deepgram.com) was blocked by the egress proxy (EGRESS_BLOCKED). **All facts below come from web-search result snippets/summaries** that quote or paraphrase those pages, plus third-party trackers. Most sources are dated May–Sept 2026. Many are blogs run by competing vendors (Trillet, Ringly, Famulor, Autocalls, Growwstacks, Ciela, Macha). Treat every price as "check before you sign". All prices are USD unless marked; the writer should convert to lei at the BNR rate of the day (I did not look up an exchange rate).

---

## 1. Platform options, 2026 pricing, per-minute all-in cost, concurrency, Romanian support

### Takeaway
For Romanian calls, the safest low-effort stack in Oct 2026 is a bundled platform whose voices are ElevenLabs (Romanian is confirmed in ElevenLabs Flash v2.5, which ElevenLabs Agents uses). Realistic all-in cost is about **$0.09–0.15/min** (ElevenLabs Agents ~$0.08 + LLM + ~$0.01 Romanian telephony). Orchestrators (Vapi, Retell, Synthflow) land at about $0.10–0.30/min. Romanian STT support is the weak point: it is confirmed only on some engines, and vendor docs for Retell, Synthflow, Bland, Gemini Live and OpenAI Realtime did not show up in search for Romanian specifically.

### Cited Findings

**Vapi (orchestrator, BYO providers)**
- Build plan: $0.05/min platform fee, no monthly subscription. STT/LLM/TTS billed at provider cost or via your own API keys. Telephony is separate. 10 concurrent lines included, then $10 per extra line/month. HIPAA add-on $2,000/mo, Zero Data Retention $1,000/mo. Scale plan is an annual contract; custom deal suggested above ~50,000 min/month. — [omidsaffari.com Vapi pricing](https://omidsaffari.com/blog/vapi-pricing); [layer3labs Vapi guide (Jul 2026)](https://www.layer3labs.io/guides/vapi-pricing); [trillet.ai Vapi per-minute](https://trillet.ai/blogs/vapi-pricing-per-minute)
- Realistic all-in: "$0.10–0.30/min" (one guide). Modeled examples (Aug 2026 assumptions) run from $0.071/min (low-cost web call) to $0.215/min (premium US outbound, big context). One comparison says BYOK platforms like Vapi land at $0.13–0.31/min. — [omidsaffari.com](https://omidsaffari.com/blog/vapi-pricing); [morphllm comparison](https://www.morphllm.com/comparisons/vapi-vs-retell-vs-bland-vs-synthflow)
- Vapi has an **EU region** (dashboard.eu.vapi.ai, api.eu.vapi.ai, sip.eu.vapi.ai). Regions are isolated. EU webhooks/tool calls come from a fixed list of EU IPs. A forum reply says the EU region runs on AWS Frankfurt, but default providers (e.g., OpenAI) may route to the US, so use your own keys (BYOK) for full EU processing. — [Vapi docs: EU region](https://docs.vapi.ai/security-and-privacy/eu-region); [Vapi support forum: EU latency](https://support.vapi.ai/t/32982063/eu-latency)

**Retell AI**
- Voice infrastructure $0.055/min. TTS $0.015/min (Retell/MiniMax/Fish/Cartesia/OpenAI/Inworld voices) or **$0.040/min for ElevenLabs voices**. LLM extra. Knowledge base +$0.005/min, PII removal +$0.01/min, AI QA $0.10/min after 100 free min. Realistic total $0.13–0.31/min; GPT-4.1 setup about $0.13/min all-in. One source says that with a current-generation model the cost passes $0.23. — [dailyaifixs Retell 2026](https://dailyaifixs.com/blog/retell-ai-pricing-2026-the-0-07-minute-myth); [morphllm](https://www.morphllm.com/comparisons/vapi-vs-retell-vs-bland-vs-synthflow)
- Concurrency: 20 free concurrent calls on pay-as-you-go, then $8 per concurrent line/month. "Burst" overflow adds $0.10/min to the **whole** call, capped at min(3× limit, limit+300). New accounts get $10 credit. Concurrency billed upfront and prorated daily since Feb 2026. — [dailyaifixs](https://dailyaifixs.com/blog/retell-ai-pricing-2026-the-0-07-minute-myth); [layer3labs Retell](https://www.layer3labs.io/guides/retell-ai-pricing)
- Conflict: an aggregator lists the voice engine at ~$0.07–0.08/min instead of $0.055. — [flexprice.io](https://flexprice.io/pricing-index/retell-ai)
- Romanian: Retell's 2025 multilingual blog claims "31+ languages", but the snippet was cut off before any Romanian entry. **Not confirmed.** — [Retell blog (ES/IT versions)](https://www.retellai.com/es/blog/how-to-use-ai-phone-agents-for-multilingual-communication)

**ElevenLabs Agents (ElevenAgents, formerly Conversational AI)**
- $0.08 per call minute on every paid plan; $0.003 per text message. LLM billed on top, from ~$0.0005/min (GPT-5 Nano) to ~$0.0446/min (GPT-5.5). No ElevenLabs telephony fee (your SIP/carrier bills separately). Silences >10 s get a 95% discount, but billing runs on total connection time. Annual billing brings included minutes to ~$0.067/min. Example: a 1,000-min/month line ≈ $105–130/mo depending on LLM (toll-free US number). — [getmacha (Sep 2026)](https://www.getmacha.com/blog/elevenlabs-agents-pricing-explained); [inworld benchmark (Jul 2026)](https://inworld.ai/resources/voice-agent-cost-per-minute-2026)
- Plans (pricing page as quoted in search): Free 15 min / 4 concurrent; Starter ($6) 75 min / 6; Creator ($11 first month; another source uses $22) 275 min / 10; Pro ($99) 1,238 min / 20; Scale 3,738 min / 30; Business ($990) 12,375 min / 40. Burst: up to 3× concurrency at 2× rate ($0.16/min). An older help-center table lists Business at 30 concurrent instead of 40. — [ElevenLabs agents pricing page via search](https://elevenlabs.io/pricing/agents); [ElevenLabs help: concurrency](https://help.elevenlabs.io/hc/en-us/articles/31601651829393-How-many-ElevenAgents-requests-can-I-make-and-can-I-increase-it); [getmacha](https://www.getmacha.com/blog/elevenlabs-agents-pricing-explained)
- **Romanian: supported.** ElevenLabs help center says every language supported by Flash v2.5 and Turbo v2.5 can be used in Agents. Flash v2.5 covers 32 languages (~75 ms latency), and Romanian (`ro`) appears in its language table (Replicate listing). Eleven v3 also lists Romanian. The voice library has native Romanian voices (e.g., "Robert Mihai"). — [ElevenLabs help: Agents languages](https://help.elevenlabs.io/hc/en-us/articles/29298127196945-Which-languages-can-I-use-with-ElevenLabs-Agents-formerly-Conversational-AI); [Replicate Flash v2.5](https://replicate.com/elevenlabs/flash-v2.5); [ElevenLabs: languages supported](https://elevenlabs.io/docs/help-center/other/what-languages-do-you-support); [json2video Romanian voices](https://json2video.com/ai-voices/elevenlabs/languages/romanian/)

**Synthflow**
- Pricing changed in 2026; sources disagree. One says fixed Starter/Pro/Growth tiers were retired and only pay-as-you-go remains. Others still list an Agency tier (~$1,250–1,400/mo, 6,000 min) or a Pro tier at $375/mo for 1,500 min. Realistic all-in: ~$0.13–0.24/min (Trillet, a competitor). LLM adds $0.02–0.05/min and Twilio ~$0.02/min. 5 concurrent calls included, +$20 per unit/month. Phone numbers $1.50 each. — [frontdeskreview Synthflow (Sep 2026)](https://frontdeskreview.com/software/ai-voice-agents/synthflow/); [dailyaifixs Synthflow](https://dailyaifixs.com/blog/synthflow-pricing-2026-the-real-per-minute-cost); [trillet Synthflow alternative](https://trillet.ai/blogs/synthflow-alternative-for-agencies); [famulor review](https://www.famulor.io/blog/synthflow-review-2026-pricing-features-and-honest-evaluation)
- Romanian: no source found.

**Bland AI**
- Tiered since a 5 Dec 2025 restructure (was a flat $0.09/min). Start: free, $0.14/min, 100 calls/day, 10 concurrent. Build: $299/mo, $0.12/min, 2,000 calls/day, 50 concurrent. Scale: $499/mo, $0.11/min, 5,000 calls/day, 100 concurrent. Transfers $0.05→$0.03/min. Telephony passed through. — [layer3labs Bland](https://www.layer3labs.io/guides/bland-ai-pricing); [ringly Bland](https://www.ringly.io/blog/bland-ai-pricing); [cloudtalk](https://www.cloudtalk.io/bland-ai-pricing/)
- Romanian: no source found. Bland runs a closed in-house stack, so language quality cannot be fixed by switching providers (my inference from the "closed in-house stack" description in [morphllm](https://www.morphllm.com/best-ai-voice-agent-platforms)).

**OpenAI Realtime (gpt-realtime family, speech-to-speech)**
- Token-billed: audio input $32/1M tokens, cached input $0.40/1M, audio output $64/1M (third-party listing checked 21 Sep 2026; a news report gives the same for GPT-Realtime-2). There is no official per-minute rate. A forum back-calculation of ~600 input tokens/min gives ≈$0.02/min input (rough). One blog plans $0.04–0.10/min for "gpt-realtime-2.1" with caching + VAD (unverified model name). Cost grows during long calls because context is re-sent. Streaming STT model gpt-realtime-whisper costs $0.017/min. — [economize gpt-realtime](https://www.economize.cloud/resources/open-ai/pricing/gpt-realtime/); [eastmoney GPT-Realtime-2](https://finance.eastmoney.com/a/202605083730524992.html); [aireiter Realtime pricing](https://aireiter.com/blog/openai-realtime-api-pricing); [OpenAI model page gpt-realtime-whisper](https://developers.openai.com/api/docs/models/gpt-realtime-whisper); [OpenAI forum](https://community.openai.com/t/confusion-between-per-minute-audio-pricing-vs-token-based-audio-pricing/1073222/2)
- Romanian quality for gpt-realtime: no source found. Soniox's vendor benchmark puts OpenAI's Romanian STT WER at 3.24% (vs Soniox 1.25%), which suggests OpenAI does handle Romanian speech recognition. — [Soniox vs OpenAI Romanian](https://soniox.com/compare-stt/soniox-vs-openai/romanian)

**Google Gemini Live API**
- Gemini 3.1 Flash Live preview: audio input $3.00/1M tokens, text input $0.75/1M, audio output ~$12/1M (third-party). That works out to ≈$0.018/min of audio output. Audio is 25 tokens/s per one blog (a forum says 32). Some figures conflict or are outdated. — [tokenkarma Gemini Live pricing](https://tokenkarma.app/blog/gemini-live-api-pricing-voice-agents-2026/); [tokencost 3.1 Flash Live](https://tokencost.app/models/gemini-3-1-flash-live); [Google AI forum](https://discuss.ai.google.dev/t/could-someone-help-me-understand-gemini-live-pricing/81303)
- Romanian: Vertex docs say the Live API supports **24 languages**, but the list was not visible in search. Romanian appears in the general Gemini API language list, and was not in the 2024 consumer Gemini Live 40-language rollout. **Not confirmed for Live audio.** — [Vertex AI Live API overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api?authuser=0); [androidheadlines](https://www.androidheadlines.com/2024/10/gemini-live-more-languages.html)

**Deepgram Voice Agent API**
- Standard bundled rate $0.075/min (≈$4.50/h); Advanced up to $0.163/min. "Custom/BYO LLM" pay-as-you-go rate rose from $0.056 to $0.065/min in Aug 2026 (Growth $0.059). Nova-3 streaming STT $0.0048/min pay-as-you-go (another guide calls this promotional; standard $0.0077). Aura-2 TTS $0.030/1k characters. — [usagepricing Deepgram tracker](https://usagepricing.com/blueprint/activity/deepgram-2026-08-26-price-change); [diyai Deepgram 2026](https://diyai.io/ai-tools/speech-to-text/deepgram-pricing-2026/); [happyrobot Deepgram](https://www.happyrobot.ai/hub/deepgram-pricing)
- Romanian: Deepgram's July 2026 changelog lists Romanian (`ro`) among improved Nova-3 monolingual **batch** models. Romanian was not in the streaming list for that update, so streaming quality is unconfirmed. — [Deepgram changelog 16 Jul 2026](https://developers.deepgram.com/changelog/2026/7/16)

**LiveKit Agents (open source + LiveKit Cloud)**
- Framework is open source. Cloud plans: Build $0, Ship from $50/mo, Scale $500/mo. Inference credits: $2.50 (~50 min), $5 (~100 min) and $50 (~1,000 min) on those tiers. Concurrent inference sessions capped at 5/20/50. Agent-session overage ≈$0.01/min (tracker). LiveKit's calculator example stack (Gemma 4 31B + Deepgram Nova-3 + Cartesia Sonic 3) ≈ $0.0672/min, of which $0.02 is LiveKit's own fees. A forum user found GPT-5.4 via LiveKit Inference ~2× OpenAI direct price; using your own key avoids the markup. — [LiveKit pricing.md](https://livekit.com/pricing.md); [usagepricing LiveKit](https://usagepricing.com/blueprint/livekit); [LiveKit community](https://community.livekit.io/t/why-is-gpt-5-4-pricing-via-livekit-inference-about-2x-openai-direct/1087)

**Pipecat (open source) / Pipecat Cloud (Daily)**
- Framework is free, BSD-2. Pipecat Cloud compute costs $0.01 per session-minute (0.5 vCPU/1 GB; larger containers $0.02–0.03). Daily PSTN dial-in/out $0.018/min, SIP $0.005/min. Audio recording $0.005/min. Krisp noise cancellation included up to 10,000 min/month, then $0.0015/min. — [Daily: Pipecat Cloud pricing](https://www.daily.co/pricing/pipecat-cloud); [frontdeskreview Pipecat Cloud](https://frontdeskreview.com/software/ai-voice-agents/pipecat-cloud/)

**Twilio ConversationRelay**
- Starts at $0.07/min (pricing page as of July 2026). This covers only the relay (Twilio's STT/TTS orchestration over a websocket). Voice minutes and your LLM/hosting are extra. Billing counts active AI-agent session time. — [Twilio pricing](https://www.twilio.com/en-us/pricing); [rywalker ConversationRelay notes](https://rywalker.com/research/twilio-conversation-relay)

**Autocalls.ai (Romanian startup)**
- Official pricing page claims a $0.09/min all-inclusive rate (vendor compares itself to "$0.18–0.34/min API cost elsewhere"). A third-party blog (Aug 2026) lists Starter $34/mo (120 min), Pro $129, Agency $249, White Label $419 (unconfirmed on the official page). Romanian voices come via ElevenLabs. Romanian virtual numbers from $3.99/mo, $0.01/min inbound. The company launched in Romania in June 2024 and claims 25 languages. Its site pushes a "$0→$50K MRR voice AI playbook", which is a hype flag. — [Autocalls pricing (via search)](https://autocalls.ai/pricing); [dailyaifixs Autocalls](https://dailyaifixs.com/blog/autocalls-ai-pricing-2026-the-120-minute-start); [Autocalls Romania page](https://autocalls.ai/country/romania); [Autocalls Romanian language page](https://autocalls.ai/language/romanian); [revistabiz](https://www.revistabiz.ro/startup-ul-romanesc-autocalls-ai-lanseaza-roboti-vocali-ai-fluenti-in-25-limbi-piata-potentiala-de-500-mld/)

**HighLevel (GoHighLevel) Voice AI (white-label CRM route)**
- Voice engine $0.045/min (effective 20 May 2026) + TTS $0.015–0.170/min + LLM tokens + telephony ≈ $0.06–0.215/min. Other guides quote $0.13–0.16/min. Local number $1.15/mo. — [netpartners GHL Voice AI 2026](https://netpartners.marketing/gohighlevel-voice-ai-conversation-ai-pricing-2026/); [thestackinsiders](https://www.thestackinsiders.com/blog/gohighlevel-voice-ai-cost)

**Romanian STT quality signals**
- Soniox vendor claim: 1.25% WER on real-world Romanian vs 3.24% for OpenAI. Soniox also says Azure does worse on fast Romanian conversation and on unclean audio. — [Soniox vs OpenAI (Romanian)](https://soniox.com/compare-stt/soniox-vs-openai/romanian); [Soniox vs Azure (Romanian)](https://soniox.com/compare-stt/soniox-vs-azure/romanian)
- Coval's independent STT benchmark (31 models, July 2026, third-party summary): AssemblyAI Universal 3.5 Pro best overall; GPT-4o Transcribe best on accents and noise. The summary did not say whether Romanian was covered. — [Coval blog/benchmarks](https://www.coval.ai/blog/benchmarks)

### Inferences
- **Per-minute all-in for a Bucharest inbound call** (my arithmetic from the figures above; Twilio RO local inbound is $0.01/min, see section 2):
  - ElevenLabs Agents + small/mid LLM + Twilio RO number: $0.08 + $0.001–0.045 + $0.01 ≈ **$0.09–0.135/min**. About $0.077–0.12 on annual billing.
  - Vapi + Deepgram/Soniox STT + ElevenLabs TTS + GPT-class LLM + Twilio RO: ≈ **$0.10–0.20/min**. The ElevenLabs TTS passthrough price inside Vapi was not found.
  - Retell with ElevenLabs voice: $0.055 + $0.040 + LLM $0.01–0.05 + $0.01 ≈ **$0.115–0.155/min**. More if the KB/PII add-ons are used.
  - Autocalls.ai: ~$0.09/min plus number (vendor claim); Romanian-native vendor.
  - Self-built LiveKit/Pipecat with Soniox/Deepgram + ElevenLabs Flash + cheap LLM: possibly **$0.05–0.08/min**, but it costs founder time for hosting, monitoring and on-call. That trade is poor at 10–12 h/week.
  - Native speech-to-speech (gpt-realtime / Gemini Live): cheap per minute on Gemini (~$0.02–0.03 audio) and $0.04–0.10 on OpenAI. Romanian quality and voice naturalness are unverified, so test before committing.
- Concurrency is a non-issue for a solo provider with 5–15 SMB clients. Vapi 10, Retell 20, ElevenLabs Pro 20 and Bland 10 are all far above the realistic peak of 2–4 simultaneous calls across a small portfolio. ElevenLabs Creator (10) is enough to start.
- Best fit for the founder's skills: n8n for tool webhooks and post-call automation, Python only if moving later to LiveKit/Pipecat to cut cost, WordPress for the landing page/demo, Oracle APEX for a client dashboard or call-log reporting. The low-maintenance path is ElevenLabs Agents or Vapi (EU region) + n8n. Retell is attractive for its tooling, but its Romanian support needs a test call.

### Gaps
- Official, directly read vendor pricing pages (all blocked); figures are from search snippets.
- Romanian support status for Retell (both STT and native voices), Synthflow, Bland, Gemini Live (24-language list not visible), OpenAI gpt-realtime voice quality in Romanian, and Deepgram Aura-2 TTS (no evidence of Romanian; assume none until tested).
- No independent Romanian-language WER/naturalness benchmark across vendors. Soniox numbers are vendor-published.
- ElevenLabs TTS passthrough price inside Vapi; Vapi's own list of Romanian-capable transcribers.

---

## 2. Telephony cost for Romania (virtual numbers, inbound per minute, call forwarding)

### Takeaway
A Romanian local virtual number costs about **$2–4/month**, and inbound runs **~$0.01/min** (Twilio) or free (Zadarma). Bucharest (021/031) availability at Telnyx is unclear, and Romanian numbers require KYC documents. The hidden cost is **call forwarding from the client's existing number**: Orange bills forwarding to other networks at **€0.17/min + VAT from the first minute**, outside included minutes. That can cost more than the AI itself, so check the operator or use conditional forwarding/SIP.

### Cited Findings
- **Twilio Romania (pricing page current as of Aug 2026):** local number $3.00/mo + $0.0100/min inbound. Toll-free $25.00/mo + $0.2406/min inbound. BYOC trunking inbound $0.0040/min. — [Twilio Voice pricing RO](https://www.twilio.com/en-us/voice/pricing/ro)
- Twilio bills per call leg and rounds partial minutes up to the next full minute (older support article; billing rule only). — [Twilio support](https://support.twilio.com/hc/en-us/articles/223179868-How-Much-Will-My-Voice-Application-Cost-per-Minute)
- **Telnyx:** its Romania page lists local codes for Arad, Dolj, Covasna, Harghita and Mehedinți (250+ numbers each). Bucharest was **not** in the visible list, and no price was shown. Requirements: local ID or passport, proof of Romanian address under 3 months old, company registration for businesses, and the end user must be **physically present in Romania** when buying. — [Telnyx Romania numbers](https://telnyx.com/phone-numbers/romania); [Telnyx Romania DID requirements](https://support.telnyx.com/en/articles/3739552-romania-did-requirements)
- **Zadarma:** Mehedinți (+40 352) local number $2/mo, no connection fee. Incoming calls to numbers bought on the site are free (except toll-free). Office plan $22/mo (2,000 min), Corporation $44 (4,000 min). Outbound to Bucharest $0.012–0.015/min. Bucharest price not confirmed. — [Zadarma Mehedinti numbers](https://zadarma.com/en/tariffs/numbers/romania/mehedinti); [Zadarma Romania call rates](https://zadarma.com/en/tariffs/calls/romania/)
- **Zernio (reseller):** RO local numbers from $3/mo, national $5/mo, toll-free $30/mo. Needs ID + proof of address; live in 1–3 business days. — [Zernio Romania](https://zernio.com/phone-numbers/romania)
- **Autocalls.ai:** RO virtual numbers from $3.99/mo, $0.01/min inbound. — [Autocalls Romania](https://autocalls.ai/country/romania)
- **HighLevel:** local number $1.15/mo (US context). — [thestackinsiders](https://www.thestackinsiders.com/blog/gohighlevel-voice-ai-cost)
- **Daily (Pipecat):** PSTN $0.018/min, SIP $0.005/min. — [Daily Pipecat Cloud pricing](https://www.daily.co/pricing/pipecat-cloud)
- **Forwarding from Orange (official help page):** forwarding to Orange numbers uses plan minutes, even on unlimited plans. Forwarding to **other networks is not included in plan minutes and is billed from the first minute at the standard off-net rate of €0.17/min excl. VAT**. Not available on PrePay, and not to international numbers. A forum user reported surprise extra charges after a few days of forwarding on Orange. — [Orange: cât costă redirecționarea apelurilor](https://www.orange.ro/help/cat-costa-redirectionarea-apelurilor-99); [Softpedia forum](https://forum.softpedia.com/topic/916792-redirectionare-apeluri-vodafone-abonament/)
- **Vodafone / Digi:** no official forwarding tariff found. A forum user says Vodafone forwarding works only on subscriptions (not prepaid). A 2023 forum claim says national forwarding is free on Vodafone, Digi and Telekom (unverified). Digi 2026 plans include unlimited national minutes and SMS, but forwarding is not addressed. — [Softpedia forum (Vodafone)](https://forum.softpedia.com/topic/916792-redirectionare-apeluri-vodafone-abonament/); [Softpedia forum (redirecționare)](https://forum.softpedia.com/topic/1223714-redirecionare-apeluri/); [bugetul.ro Digi 2026](https://www.bugetul.ro/noile-preturi-la-digi-romania-compania-de-telecomunicatii-si-a-schimbat-tarifele-din-anul-2026/)

### Inferences
- Telephony itself is cheap: a Twilio RO number + 500 inbound minutes ≈ $3 + $5 = **$8/month**.
- **Forwarding risk (key operational finding):** if a salon's Orange business mobile forwards all calls to a Twilio/Zadarma 021 number (off-net), 500 min/month × €0.17 = **€85 + VAT on the client's Orange bill**. That is more than the AI platform cost. Mitigations:
  - (a) Conditional forwarding (no-answer/busy/unreachable) only, so only missed calls are forwarded.
  - (b) Check whether the client's Vodafone/Digi/Telekom plan treats national forwarding as included.
  - (c) Give the client a new 021/031 number and publish it on Google Business Profile and the website.
  - (d) Move the client's landline to a VoIP/SIP provider and route by SIP (no PSTN forwarding leg).
  - Include this check in the onboarding checklist and in the contract (who pays forwarding charges).
- KYC (ID, address proof, sometimes physical presence) means the founder's own Romanian company/ID will likely be the number holder. Alternatively, the client buys the number. Plan 1–3 business days of lead time.
- Toll-free (0800) inbound on Twilio costs $0.24/min, 24× a local number. Avoid it.

### Gaps
- Official Telnyx and Vonage Romania prices, and whether Bucharest 021/031 numbers are available at Telnyx and Twilio (search showed only provincial codes for Telnyx).
- Official Vodafone, Digi and Telekom forwarding tariffs.
- Local Romanian SIP providers' prices (e.g., for porting a client's 021 landline). No sources found in this pass.
- Number portability of a geographic number to a CPaaS provider in Romania (ANCOM process/timeline). Not researched.

---

## 3. Typical call profile, monthly minutes and cost per client

### Takeaway
Vendor data suggests an average AI-handled call of **~1.75–3 minutes** (restaurant ~1:45, receptionist ~2 min, auto repair 3–5 min). Volume ranges from about 25–80 calls/day for dental, auto repair and restaurants (US data). An overflow/after-hours receptionist for a Bucharest SMB is likely **~200–600 AI minutes/month (≈$25–90 platform cost)**. A full front desk for a busy clinic can reach 1,500–2,500 min (≈$180–350). These are vendor-sourced US numbers, so Romanian volumes need validating with call logs.

### Cited Findings
- AI receptionist vendor Trillet: average call ~2 minutes. — [Trillet receptionist pricing](https://trillet.ai/receptionist/pricing)
- 3CX forum: intake-style calls take 3–5 min. 3CX staff consider 3 min fine for basic reception and set a 7-min cap. — [3CX community](https://www.3cx.com/community/threads/ai-timeout.137534/)
- Dental (US, vendor-compiled): 1–3 provider practice gets 40–80 inbound calls/day (~800–1,600/month). Other sources say 30–50/day, with "up to 50" attributed to the ADA. Orthodontic 25–50/day (longer calls), pediatric 50–100/day. — [ainora dental call statistics 2026](https://ainora.lt/blog/dental-practice-phone-call-statistics-2026); [agentzap dental statistics](https://agentzap.ai/blog/dental-practice-phone-statistics)
- Vendor claim: AI can handle 60–70% of dental calls (scheduling, FAQs, reminders, intake). — [myaifrontdesk dental](https://www.myaifrontdesk.com/other-industries/dental)
- Small auto repair: 25–50 calls/day, 3–5 min each. Restaurants: 40–80 calls/day, 2–3 min. Methodology unclear. — [ainora business phone statistics 2026](https://ainora.lt/blog/business-phone-call-statistics-2026)
- Maple (restaurant voice AI): 1.2M AI-handled calls, 1,000+ US locations, late 2023–late 2025. **Average ≈1 min 45 s**. 40% of daily calls fall 5–9 PM. Friday is 18–20% of weekly calls. — [Maple: restaurant phone insights](https://maple.inc/blog/the-state-of-restaurant-phone-communication-insights-from-1-million-calls)
- Auto repair: ~25% of open-hours calls unanswered (attributed to the Automotive Service Association, unverified). Peaks 7:30–9 AM and 4:30–6 PM. — [agentzap auto repair](https://agentzap.ai/blog/auto-repair-phone-statistics)
- Salons: no reliable per-day benchmark. A salon-focused vendor sells Starter $499/mo with up to 800 min ("small or single-stylist salons"). — [salonreception](https://salonreception.carrd.co/); [Zenoti salon call conversion](https://www.zenoti.com/blog/how-to-measure-your-salon-call-conversion-rate)
- 411 Locals study (2024, **n=85 businesses**, 30 days): only 37.8% of calls were answered by a human. 62.2% were "unanswered", which includes 37.8% that went to voicemail; 24.3% got no answer at all. — [alliancevirtualoffices summary](https://www.alliancevirtualoffices.com/virtual-office-blog/shocking-research-finds-small-businesses-miss-almost-half-of-incoming-calls/); [getaira missed-call stats](https://getaira.io/blog/missed-business-calls-statistics)
- Messaging add-on costs (Romania): WhatsApp utility template ≈ **$0.0305/message** since 1 Jul 2026 (another table says $0.029). Utility templates are free inside an open 24-h customer-service window. Marketing ≈ $0.09. A BSP fee may be added. Twilio SMS to Romania ≈ **$0.0737/segment**; Plivo $0.0656–0.0774/SMS. — [GoHighLevel WhatsApp pricing changelog](https://ideas.gohighlevel.com/changelog/updated-whatsapp-per-message-pricing-effective-july-2026); [Meta WhatsApp pricing](https://developers.facebook.com/docs/whatsapp/pricing); [zernio WhatsApp](https://zernio.com/blog/whatsapp-business-api-pricing); [Twilio SMS RO](https://twilio.com/sms/pricing/ro); [Plivo SMS RO](https://www.plivo.com/sms/pricing/ro/)

### Inferences
Monthly volume and cost scenarios (my arithmetic; assumed all-in $0.11/min for ElevenLabs/Vapi-class + $3 number; WhatsApp confirmations at $0.03):

| Client type (Bucharest) | Mode | Assumed AI calls | Avg min | AI min/month | Voice cost | + number + ~100–300 WhatsApp | ≈ Total COGS |
|---|---|---|---|---|---|---|---|
| Salon / barber, 1–3 chairs | overflow + after-hours | 5–10/day × 26 days | 2 | 260–520 | $29–57 | $6–12 | **$35–70** |
| Dental clinic (1–3 chairs) | overflow + after-hours | 10–15/day × 22 | 2.5 | 550–825 | $60–91 | $6–12 | **$65–105** |
| Dental clinic | full front desk (60–70% of 40/day) | 24–28/day × 22 | 2.5 | 1,320–1,540 | $145–170 | $6–12 | **$150–185** |
| Auto service | overflow (~25% of 25–50/day) | 6–12/day × 24 | 4 | 600–1,150 | $66–127 | $3–6 | **$70–135** |
| Restaurant | reservations, peak only | 15–30/day × 30 | 1.75 | 790–1,575 | $87–173 | $10–20 | **$95–195** |

- If forwarding goes through Orange off-net, add €0.17/min to the **client's** bill (section 2).
- A pooled ElevenLabs Pro plan ($99, 1,238 min, 20 concurrent) would cover roughly 2–4 overflow-mode clients. Above that, minutes cost $0.08 + LLM.
- Romanian SMBs are probably smaller than the US practices in these benchmarks, so treat the low end as the default and validate with 2 weeks of the client's call logs.

### Gaps
- No Romania-specific call-volume or call-length data. All benchmarks are US vendor data, with little methodology.
- No reliable salon call-volume benchmark.
- The 85% "won't call back" stat (BIA/Kelsey) could not be traced to the original. — [growwstacks niches](https://growwstacks.com/blog/best-ai-voice-agency-niches-for-beginners/)

---

## 4. Integrations needed and how n8n is used with Vapi / Retell / ElevenLabs

### Takeaway
The standard pattern: the voice platform calls n8n webhooks as **tools** during the call (check_availability, book_appointment, take_message). After the call, an end-of-call/post-call webhook fires an n8n workflow that writes to the calendar/CRM/Sheets and sends a summary to the owner (WhatsApp/email) and a confirmation to the caller (WhatsApp/SMS). Free and cheap templates exist, but none is an official, production-ready Romanian receptionist template.

### Cited Findings
- **Vapi + n8n (official docs):** use an "API Request" tool. Vapi calls the n8n workflow's **production** webhook URL and gives its JSON response to the assistant. The starter is a 3-node flow (Webhook → Code → Respond to Webhook) that only checks business hours, with no holidays or availability. The HTTP method must match the tool's method. — [Vapi docs: n8n integration](https://docs.vapi.ai/tools/integrations/n8n)
- Common pitfall (community thread): the assistant called the tool but the n8n webhook never received it. Likely cause: pointing at n8n's test URL instead of the production URL, or an inactive workflow (inferred, not confirmed in the thread). — [Vapi community](https://vapi.ai/community/m/1435306405648404570)
- **Retell + n8n (Growwstacks guide):** two custom functions, `check_availability` and `book_appointment`. On the n8n side: POST Webhook trigger → AI Agent node (GPT-4.1) → Google Calendar. The guide's "40–60% more bookings" claim is vendor marketing. — [growwstacks Retell + n8n](https://growwstacks.com/blog/build-voice-ai-receptionist-retell-n8n/)
- **Retell → n8n → Google Calendar + Sheets pipeline:** passes caller number, service and preferred time. n8n creates/updates events and logs a call summary to Sheets. Covers securing API keys and **webhook signatures**. — [undercodetesting deep dive](https://undercodetesting.com/how-we-built-an-ai-voice-receptionist-that-never-misses-a-booking-a-deep-dive-into-retell-ai-n8n-and-google-apis-video/)
- **ElevenLabs + n8n free template (Growwstacks):** computes free slots with **deterministic JavaScript** instead of asking the LLM, to avoid double bookings. — [growwstacks ElevenLabs + Google Calendar](https://growwstacks.com/blog/ai-voice-agent-google-calendar-n8n/)
- Other templates: Growwstacks virtual-receptionist JSON (chat-oriented); Buldrr anti-double-booking workflow (Webhook + Google Calendar + Airtable); Neura Market free salon-booking workflow (AI + Google Calendar + email) and a $9.18 booking-confirmation workflow. — [growwstacks workflow](https://growwstacks.com/workflows/create-an-ai-powered-virtual-receptionist-with-google-calendar-and-sheets); [buldrr n8n booking](https://buldrr.com/workflows/automate-appointment-booking-n8n-google-calendar/); [Neura Market](https://www.neura.market/workflow/automate-your-webhook-creation-with-n8n-for-enhanced-productivity)
- Vapi EU region sends webhooks/tool calls from a fixed EU IP list, which matters if self-hosted n8n filters by IP. — [Vapi EU region docs](https://docs.vapi.ai/security-and-privacy/eu-region)
- HighLevel offers built-in CRM/calendar plus rebilling (markup e.g. 1.5–2× or a fixed rate such as $0.10/Voice-AI minute). — [HighLevel: fixed-rate rebilling](https://help.gohighlevel.com/support/solutions/articles/155000008422-fixed-rate-rebilling-for-ai-products); [HighLevel: Conversation AI rebilling](https://help.gohighlevel.com/support/solutions/articles/155000001357-pricing-and-rebilling-conversation-ai)
- Messaging costs for confirmations and summaries: WhatsApp utility ≈ $0.03/msg in RO (free in an open service window); SMS ≈ $0.074/segment via Twilio (section 3).

### Inferences
- Minimum viable integration set per client:
  1. Tool webhooks: `get_business_info` (or a KB), `check_availability`, `book/cancel/reschedule`, `take_message`, `transfer_to_human`.
  2. Post-call workflow: summary + caller number + intent sent to the owner via WhatsApp (Meta Cloud API or BSP) and email; booking confirmation to the caller via WhatsApp (cheaper than SMS in RO); a row in Google Sheets or the founder's Oracle APEX dashboard.
  3. Calendar: Google Calendar or Cal.com covers salons and small clinics. Romanian clinic/salon software needs per-vendor API checks.
- One reusable n8n "receptionist core" workflow, parameterized per client (calendar ID, services, hours, owner phone), is the key leverage for staying within 10–12 h/week. Compute slot availability in code, not in the LLM.
- Self-hosted n8n on a cheap EU VPS (or n8n Cloud) keeps data in the EU and avoids per-execution fees. Not priced here.

### Gaps
- Official, maintained Retell or ElevenLabs n8n templates (only third-party ones found).
- APIs/integrations of Romanian clinic/salon booking software (no sources gathered in this pass).
- n8n Cloud vs self-host cost (not researched).
- WhatsApp BSP fees in Romania (only Meta's rate found).

---

## 5. Setup time per client and monthly maintenance

### Takeaway
There is no independent, measured data. Vendor claims range from **30–60 minutes** (templated, auto-generated from the client's website) to **2–4 hours** (onboarding to live in 24 h), and a vendor claims "40+ hours wasted" when done manually. Ongoing work is reviewing calls (a vendor suggests a 15-minute daily review routine) and fixing edge cases. Plan for custom Romanian builds taking much longer than the template claims.

### Cited Findings
- Trillet (vendor, school-hours agency guide): onboarding means pasting the client's website URL, reviewing the auto-generated agent and customizing it, **30–60 min per client**. Daily **15-minute morning routine** to check the previous day's calls and tweak edge cases. Hypothetical: 5 clients × $297 = $1,485/mo working 15–20 h/week. — [trillet: AI receptionist agency around school hours](https://trillet.ai/blogs/ai-receptionist-agency-around-school-hours)
- Trillet onboarding article (updated 31 Jul 2026): **2–4 hours** setup, live within 24 h. — [trillet: client onboarding process](https://trillet.ai/blogs/voice-agent-client-onboarding-process)
- Growwstacks (sells the ChatDash platform): agencies "waste 40+ hours per client" on manual setup (logins, rebuilt workflows, chasing invoices). Its templated flow saves 5–7 hours per client. Vendor marketing. — [growwstacks deployment playbook](https://growwstacks.com/blog/voice-ai-agency-client-deployment-playbook)
- Failure review: a sample of 50–100 failed calls is usually enough to surface the top misrecognized phrases and intent gaps (vendor rule of thumb). — [webfuse voice agent failures](https://www.webfuse.com/blog/top-5-voice-ai-agent-failures-and-how-to-fix-them)
- Churn and onboarding: ~70% of churn happens in the first 90 days, driven by slow early value, unclear ROI, unnoticed breakdowns and missing reports. — [ciela: why AI automation clients churn](https://ciela.ai/blogs/why-ai-automation-clients-churn-and-how-to-keep-them)
- Freelancer offer: $299/mo includes 300 min, $0.20/min overage, setup included in the first month, ongoing management/monitoring included. — [webeminence](https://webeminence.com/voice-ai-lp/)

### Inferences (my estimates for a Romanian custom build; no source has measured this)
- **First client (building the template):** 20–40 h (Romanian prompt and voice selection, STT tuning for names, phone numbers, dates and street names, n8n core workflow, WhatsApp setup, number KYC, 50+ test calls).
- **Each subsequent client in the same niche:** 4–8 h. That covers a 1-h intake call, a 1–2 h KB/prompt build from the website and price list, 1 h calendar/WhatsApp wiring, 1–2 h of test calls including noisy-background and older-caller tests, 0.5 h forwarding setup with the operator check, and go-live monitoring.
- **Maintenance:** ~1–2 h/client/month in steady state (weekly transcript skim, monthly report, price/hours updates, prompt fixes), plus 2–4 h in the first month for hypercare.
- **Capacity at 10–12 h/week (≈45–50 h/month):**
  - Example mix: 8 steady clients × 1.5 h = 12 h; 1 new client/month × 6 h; 10–15 h sales/demos; 5 h admin/billing; ~10 h buffer for incidents.
  - Result: **~8–12 active clients** is a realistic ceiling without hiring, if all clients share one niche template.
- Romanian-specific extra work: number/date readback in Romanian (e.g., "07xx" mobile numbers, "joi la ora 14"), diacritics in the KB, and Romanian names. Budget extra test time; no source quantifies it.

### Gaps
- No practitioner time logs (Reddit/forums not indexed by the search tool). All figures are vendor claims or my estimates.
- No data on support-ticket volume per client.

---

## 6. Pricing benchmarks (setup + monthly + overage), margins, white-label options

### Takeaway
US agency benchmarks cluster at a **$1,500–4,000 setup + $300–650/month** retainer. Freelancer and SaaS anchors sit lower: $49–299/mo with 150–300 minutes, overage ~$0.20/min. Gross margin on platform cost alone is often 80–90%, but those claims exclude labor, sales and churn. No Romanian (lei) price lists were found. White-label is expensive on Synthflow ($2,000/mo add-on) and cheap on HighLevel (rebilling built in) and Autocalls (~$419/mo, unverified).

### Cited Findings
- Ciela (Jan 2026, illustrative): entry tier $1,500–2,500 setup + $300–450/mo; booking tier $2,500–4,000 setup + $450–650/mo. Example: $550 retainer, ~500 min, platform cost ~$60–100, so >80% gross margin on the retainer. The market spans $0.05–1.00/min, and a few hundred SMB minutes cost the agency ~$20–60. Price on outcome value. — [ciela: how much to charge for an AI voice agent](https://ciela.ai/blogs/how-much-to-charge-for-ai-voice-agent)
- Growwstacks: minimum $300/mo, $500 "sweet spot". Start with after-hours-only at ~$300 and upsell. Another guide shows $500 price vs ~$50 cost ("90% margin"). — [growwstacks: sell AI receptionists to local businesses](https://growwstacks.com/blog/sell-ai-receptionists-local-businesses/); [superdupr cost guide](https://superdupr.com/blog/how-much-does-an-ai-receptionist-cost.md)
- Buldrr: lead reactivation agent $5,000–12,000 setup + $300–800/mo; general setup $2,000–4,000. Upper-end, guru-adjacent. — [buldrr](https://buldrr.com/7-ai-agents-businesses-are-paying-for-in-2026/)
- SaaS price anchors clients may compare against (US/English): Trillet $49/mo for 150 min + $0.20/min overage; My AI Front Desk $99 ($79 annual) for 200 min; Goodcall Starter $79 unlimited; Aira $24.95 (30 calls) to $159.95 (500 calls); NextPhone $199/mo unlimited. Speechify's RO-language blog: AI receptionist $200–500/mo vs a human receptionist at $35–50k/yr (US). — [trillet pricing](https://trillet.ai/receptionist/pricing); [getaira](https://www.getaira.io/ai-receptionist-faq/how-much-does-an-ai-receptionist-cost); [getnextphone](https://www.getnextphone.com/blog/ai-receptionist-cost); [speechify RO blog](https://speechify.com/ro/blog/ai-receptionist-how-small-businesses-are-replacing-phone-answering-services-in-2026/)
- Underpricing signal: a community member with a first lead considered "a maximum of $1 per call". — [skool learn-ai](https://www.skool.com/learn-ai/just-created-my-ai-receptionist-and-got-a-lead-dont-know-how-to-price-it)
- Per-minute rebilling: HighLevel fixed-rate example $0.10/Voice-AI minute, or a 1.5–2× markup. Assistable example pays $0.07 base and charges $0.10. "Most agencies bill $1–3 per voice minute" is an anecdotal, unverified blog claim. — [HighLevel fixed-rate rebilling](https://help.gohighlevel.com/support/solutions/articles/155000008422-fixed-rate-rebilling-for-ai-products); [Assistable rebilling docs](https://docs.assistable.ai/platform/rebilling.md); [optimizesmart](https://optimizesmart.com/blog/how-to-bill-your-voice-ai-clients-like-a-pro/)
- **White-label:**
  - Synthflow: white-label + custom domain add-on **$2,000/mo**, or Enterprise (custom per-minute, minimum 10,000 min/mo; ~$30k/yr per competitor Trillet). The legacy Agency plan (~$1,250–1,400/mo, 6,000 min) is disputed or likely retired. — [frontdeskreview Synthflow](https://frontdeskreview.com/software/ai-voice-agents/synthflow/); [trillet](https://trillet.ai/blogs/synthflow-alternative-for-agencies)
  - Autocalls: White Label plan $419/mo (third-party), with minute rollover. — [dailyaifixs Autocalls](https://dailyaifixs.com/blog/autocalls-ai-pricing-2026-the-120-minute-start)
  - HighLevel: rebilling with markup/fixed rate per sub-account. Voice AI $0.045/min engine + TTS. — [netpartners](https://netpartners.marketing/gohighlevel-voice-ai-conversation-ai-pricing-2026/)
  - Romanian price lists: none found in lei for AI receptionists. Edesy (Indian vendor with RO pages) lists Pro $18/mo for 300 min (unclear Romanian quality). — [edesy RO](https://edesy.in/ai-voice-agent/use-cases/customer-support/in/romanian)

### Inferences
- Unit economics example (overflow salon, ~400 min/mo): COGS ≈ $45–60 (section 3). At a hypothetical €149/mo retainer, gross margin is ~60–70% before labor. At €249/mo it is ~80%.
  - Labor at 1.5 h/month is the real cost. Price so that (retainer − COGS) / maintenance hours ≥ the founder's target hourly rate.
  - These euro price points are illustrative only. US $300–650 benchmarks likely overstate what Bucharest micro-businesses pay, so the market researcher's Romanian data should set the price.
- Recommended structure, drawn from the patterns above:
  - Setup fee (covers 4–8 h; could be waived for a pilot), plus a monthly retainer with a minute allowance (e.g., 300–600 min), plus per-minute overage at 2–3× cost (≈$0.20–0.30/min).
  - Do not sell "unlimited", because COGS scales with minutes.
- Do not white-label at the start: Synthflow's $2,000/mo is uneconomic for <10 clients. Running directly on ElevenLabs/Vapi with your own branding, and a WordPress/APEX dashboard for reports, gives the same client-facing result.

### Gaps
- No verified Romanian market pricing (lei) for AI receptionist services.
- HighLevel plan subscription costs (Agency/SaaS tiers) were not captured by search. Vapi and Retell have no formal reseller or white-label programs in the sources found.
- No independent margin data after labor and churn.

---

## 7. Validating demand fast and selling; common mistakes

### Takeaway
Practitioner/vendor advice converges on a few steps:
- Pick one niche you know.
- Let prospects **talk to a live demo number** (not a screen recording).
- Prove the pain with a **missed-call audit**: call them after hours, or log calls for 2 weeks.
- Run a short free or paid pilot in exchange for a testimonial.
- Report results early, because most churn happens in the first 90 days.

Much of this content comes from vendors and course-sellers, so treat it as hype-prone.

### Cited Findings
- Top niche-selection mistake: picking from a spreadsheet. Industry familiarity matters more than revenue projections ("familiarity is what gets you in the door"). — [growwstacks: best AI voice agency niches](https://growwstacks.com/blog/best-ai-voice-agency-niches-for-beginners/); [trillet: choosing a first niche](https://trillet.ai/blogs/how-to-choose-your-first-niche-as-an-ai-voice-agency)
- Demo format: "the demo has to be the conversation". Prospects should talk to it live or via a link. A polished demo does not prove it survives real callers, noise or anger. — [growwstacks niches](https://growwstacks.com/blog/best-ai-voice-agency-niches-for-beginners/); [ciela: demo software for agencies (Aug 2026)](https://ciela.ai/blogs/ai-voice-agent-demo-software-for-agencies)
- Missed-call audit: log every inbound call for ~2 weeks (time, duration, outcome) and watch abandonment patterns. Call target businesses after hours; if they don't answer, they need inbound coverage. Free pilots in exchange for testimonials and referrals. — [growwstacks: how to start a profitable AI agency 2026](https://growwstacks.com/blog/how-to-start-profitable-ai-agency-2026); [callin.io missing-call](https://callin.io/missing-call)
- Pitch statistic: 411 Locals' 62% "unanswered" (n=85; voicemail counted as unanswered). Use it carefully. — [alliancevirtualoffices](https://www.alliancevirtualoffices.com/virtual-office-blog/shocking-research-finds-small-businesses-miss-almost-half-of-incoming-calls/). Zadarma (a telephony provider active in Romania) also published missed-call cost research. — [Zadarma missed calls research](https://zadarma.com/en/blog/missed-calls-cost-research/)
- Churn: ~70% of churn in the first 90 days (ciela). SMB monthly churn commonly 3–5%. New voice-AI agencies often see **double-digit monthly churn** in year one before adding a retention system (Trillet). Fixes: early visible wins, scheduled reports, act when usage drops. — [ciela churn](https://ciela.ai/blogs/why-ai-automation-clients-churn-and-how-to-keep-them); [trillet retention](https://trillet.ai/blogs/voice-agent-client-retention-strategies); [DEV playbook](https://dev.to/scalelogix_ai/how-to-retain-ai-agency-clients-a-playbook-for-long-term-operator-success-521a)
- Unverified vendor claim: ~30% of AI receptionist customers abandon within 6 months (attributed to a "Customer Service Institute" study that could not be found). — [myaifrontdesk reseller blog](https://www.myaifrontdesk.com/reseller-blogs/how-to-prevent-ai-receptionist-churn-and-boost-your-client-retention)
- Hype flags:
  - "Voice AI agency $60k MRR in 17 days" (growwstacks headline). — [growwstacks](https://growwstacks.com/blog/voice-ai-agency-60k-mrr-17-days/)
  - Autocalls' "$0 → $50K MRR playbook" banner. — [autocalls](https://autocalls.ai/country/romania)
  - Course promising $10k/month in 60–90 days (superdupr summary). — [superdupr](https://superdupr.com/blog/how-much-does-an-ai-receptionist-cost.md)

### Inferences
- Fast validation plan for Bucharest:
  - **Week 1:** mystery-call 30–50 businesses in one niche (e.g., dental clinics or salons in one sector) at lunch, after 18:00 and on Saturday. Record answer rate. This produces a local "missed-call audit" you can show prospects.
  - **Week 2:** call back the non-answering ones and offer a free 14-day overflow pilot (conditional forwarding only, so no forwarding-cost risk). Give each a Romanian demo number tuned to their niche, and send a weekly WhatsApp report: calls answered, bookings, messages.
  - **Convert:** offer a paid plan with a modest setup fee. Results-based pricing (per booked appointment) is possible but hard to measure without calendar access.
- Common mistakes to avoid as a part-timer:
  1. Too broad (many niches means many templates).
  2. Underpricing (per-call pricing near $1 or "unlimited minutes").
  3. Taking on clients whose software has no API.
  4. Promising full replacement of the receptionist instead of overflow/after-hours.
  5. No contractual SLA limits. Platform outages happen (section 8).

### Gaps
- Reddit (r/AI_Agents, r/n8n, r/smallbusiness) threads were not indexed by the search tool. No first-hand Romanian practitioner reports were found.
- No data on conversion rates of demo-number or missed-call-audit outreach.

---

## 8. Reliability risks: EU latency, outages, hallucinations, noise/accents, human fallback, monitoring

### Takeaway
The main risks are:
- **Platform outages**: Vapi logged multiple 2026 incidents, including ~38k dropped calls in under an hour on 23 Feb.
- **Latency** if any component runs in the US. Transatlantic adds 75–160 ms, and users have reported 840 ms+.
- **Hallucinated confirmations**: the agent "books" without the tool succeeding.
- **Romanian STT errors** on names, numbers and noisy calls.

The mitigations are architectural: EU region + EU providers, tool-gated confirmations with readback, warm transfer or take-a-message fallback, and monitoring based on system state rather than transcripts.

### Cited Findings
- **Vapi 2026 incidents** (third-party trackers IsDown/Pingoru):
  - 23 Feb: 37,806 calls dropped (9:10–10:05 AM) due to call-worker failures.
  - 24–25 Feb: ~22 h disruption on the weekly channel.
  - 19 Mar: cluster + Deepgram transcriber issues for 1 h 19 m.
  - 14 Apr: SIP failures and transfer problems for ~1 h 55 m.
  - 16 Apr: inbound calls dropped after a DB query change.
  - 21 May: major incident of ~2 h, or 3.7 h per another entry.
  - 26/28 May: call-failure spikes of 38/54 min.
  - 2–3 Jun: dashboard errors and call-creation failures.
  - — [pingoru Vapi outage history](https://pingoru.io/providers/vapi-ai/outage-history); [isdown Vapi](https://isdown.app/status/vapi/outage-history)
- **Latency:** human turn-taking gaps ≈200 ms. TTS time-to-first-audio budget is typically 200–300 ms, and Coval treats >400 ms as noticeable. — [Coval TTS/STT benchmark](https://www.coval.ai/blog/voice-ai-tts-stt-benchmark/)
  - Transatlantic inference adds ~75–160 ms of fiber latency. — [lyceum: jurisdiction proof](https://lyceum.technology/magazine/inference/data-residency/jurisdiction-proof/)
  - Vapi forum: a user reported a Twilio call landing on a US websocket with >840 ms latency. User-reported round trips range 340–1,040 ms (hosted) vs 500–1,300 ms (on-prem). Vapi provides per-call latency reports. — [Vapi forum: EU endpoint](https://support.vapi.ai/t/23111245/vapi-endpoint-in-europe); [Vapi forum: EU latency](https://support.vapi.ai/t/32982063/eu-latency)
- **Hallucinations / false confirmations:**
  - SIVARO Q2 2026 production data: top models hallucinate in 3–7% of agent responses, domain-dependent. Softcery: real-world misfire rate closer to 20%. These measure different things. — [sivaro: 47 production incidents](https://sivaro.in/articles/ai-agent-deployment-failure-causes-what-i-learned-from-47/); [softcery: demos vs production](https://softcery.com/lab/why-voice-agents-sound-great-in-demos-but-fail-in-production)
  - VAmoS Bench (arXiv, 2026, research harness): phone-call task completion 65.8% (simple) vs 52.2% (complex). Calls can sound successful while the backend state change never happened, e.g., an agent said "I've updated your address" without calling the tool. — [arXiv VAmoS Bench](https://arxiv.org/pdf/2607.27453)
  - Controls: readback and confirmation; validation at the tool; confirm only on success responses. STT can turn "B3172" into "B3712". — [softwareseni failure modes](https://www.softwareseni.com/when-voice-agents-go-wrong-production-failure-modes-and-how-to-prevent-them/)
- **STT/noise:** WER <5% is good, and >8% typically triggers cascade failures (vendor rule of thumb). — [webfuse](https://www.webfuse.com/blog/top-5-voice-ai-agent-failures-and-how-to-fix-them). GPT-4o Transcribe led on accents and noise in Coval's July 2026 STT analysis (third-party summary). — [Coval benchmarks](https://www.coval.ai/blog/benchmarks). Krisp noise cancellation is included in Pipecat Cloud up to 10k min. — [Daily](https://www.daily.co/pricing/pipecat-cloud)
- **Human fallback:**
  - Handoff is the most frequent failure point (Haptik). Escalation defaults to cold unless designed. Define rule-, sentiment- and policy-based triggers. An explicit request for a human should transfer immediately (Famulor). Confidence threshold ~0.6–0.7 is a rule of thumb (Webfuse). Pass intent, identity and transcript to the human. An ineffective AI wastes ~81 s per interaction before escalating (Twilio-cited research). — [haptik warm transfer](https://www.haptik.ai/blog/warm-transfer-escalation-design-between-ai-human-agents); [famulor transfer guide 2026](https://www.famulor.io/es/blog/ai-voice-agent-call-transfer-to-a-human-the-2026-guide); [Twilio AI-to-human handoff](https://www.twilio.com/en-us/blog/insights/ai-to-human-handoff-context); [Retell warm transfer](https://www.retellai.com/blog/how-ai-voice-agents-are-perfecting-the-warm-transfer)
  - Bland bills transfers at $0.03–0.05/min. — [layer3labs Bland](https://www.layer3labs.io/guides/bland-ai-pricing)
- **EU data residency:** Vapi EU region exists; bring your own EU-hosted provider keys to avoid US routing (forum). — [Vapi docs EU](https://docs.vapi.ai/security-and-privacy/eu-region). A single non-EU logging service in the chain re-introduces transfers. — [regolo.ai](https://regolo.ai/eu-data-residency-and-gdpr-for-ai-vendors-from-checkbox-to-product-feature/)

### Inferences
- For Bucharest callers: use the Vapi EU region (Frankfurt), or a platform with EU media servers. Pick EU-hosted or low-latency STT/TTS (ElevenLabs Flash ~75 ms). Avoid big reasoning LLMs on the hot path.
- Test latency from a Romanian mobile, through the actual forwarding path, before go-live.
- Design rules for SMB receptionists:
  1. Never let the LLM confirm a booking unless the n8n tool returned success. Read back the date, time and phone number in Romanian.
  2. Default fallback is "take a message + WhatsApp to the owner within 1 min". Warm transfer to the owner's mobile only during set hours (transfer minutes cost money, and the owner may not answer).
  3. Use a platform-outage fallback. With conditional forwarding, calls ring the owner first, so an AI outage degrades to the status quo. With full forwarding, configure a failover number at the telephony layer (Twilio fallback URL / SIP failover; specifics not researched).
  4. Monitoring: a daily n8n job flags calls with failed tool calls, short duration (<15 s), "transfer requested" or negative sentiment. Weekly review of 10–20 flagged transcripts. Alert on webhook errors.
- Contract: no uptime guarantee beyond the platform's own; specify response times (e.g., next business day) to keep support load compatible with a part-time schedule.

### Gaps
- No outage history found for ElevenLabs Agents, Retell or Autocalls in this pass (only Vapi was searched).
- No measured EU latency figures for ElevenLabs/Retell/Autocalls from Romania.
- Romanian-specific accent/noise performance data (e.g., Moldovan accents, older callers, street noise): none found.
- Legal requirements (GDPR call recording consent, EU AI Act disclosure that the caller is talking to an AI) were not researched here; presumably covered by another workstream.
