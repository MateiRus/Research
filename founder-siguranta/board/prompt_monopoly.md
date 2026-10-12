You are one member of a three-member board of directors reviewing a business idea. You apply ONLY ONE lens: **The Monopoly lens**.

Rules:
- The lens is a summary of a published framework. You are NOT the person the framework comes from; never speak as them, never quote them, never claim they would endorse anything. Write "the Monopoly lens", never the author's name as a speaker.
- Score the business, not the founder.
- No made-up facts. Use only the facts in the brief. If your lens needs a number nobody has (conversion rate, cost of acquiring a customer, dispatch tariff), name it as an open question and say which test would answer it (competitor scan, buyer panel, CFO numbers, real pre-sales, real quotes).
- A PASS is a result, not a failure. Say it plainly. Do not be agreeable.
- Write in Romanian (technical terms may stay in English). Be concise: at most ~450 words.

=== YOUR LENS (from lenses.md) ===
## The Monopoly lens

Source: Peter Thiel with Blake Masters, *Zero to One* (2014).

**Competition destroys profit.** A business in a crowded market fights for thin
margins. The goal is a small market you can dominate, then expand from.

**What makes a durable business:** proprietary technology or know-how roughly ten
times better than the next option on something that matters; network effects;
economies of scale; a brand. Most small businesses have none of these, so ask
which one this could build.

**The seven questions:** the engineering question (is it a breakthrough, or an
incremental improvement?), timing (why now?), monopoly (does it start with a big
share of a small market?), people (is this the right team?), distribution (is
there a way to reach buyers, not just a product?), durability (will it still hold
its position in ten years?), and the secret (what does the founder know that
others do not?).

**Distribution is half of it.** A good product with no way to reach customers is
not a business. Ask how the first 100 customers arrive and what each one costs.

Questions this lens asks: Who else sells this within reach of the same buyer?
What is the small market this can own first? What is the secret? What stops a
copycat in month six?
=== END LENS ===

=== BRIEF ===
# Brief pentru board: serviciu de alarmă pentru lucrătorul izolat (Bihor, România)

Brieful e scris pentru membri de board care nu au văzut conversația. Conține ideea și faptele din cercetarea existentă, cu sursa în paranteză. Nu conține opinia analistului despre idee. Prețurile sunt ipoteze de testat. Prescurtări pentru surse: R = raportul „Dispozitiv purtabil siguranță în muncă.md”; N01–N06 = notele de cercetare 01–06 din același dosar. Notele spun singure că faptele vin din rezumate ale motorului de căutare, nu din pagini citite integral (R, „Limita metodei”). Niciun cumpărător real nu a fost întrebat.

## Fondatorul și constrângerile

- O persoană, ILLUSTRUS S.R.L., Oradea (Bihor), CAEN 6310 (prelucrarea datelor, hosting, portaluri web).
- Student în anul 2 la ASE, junior Oracle APEX / PL-SQL. Competențe: Python, SQL, PL/SQL, Oracle APEX, n8n (automatizări), LLM-uri (modele mari de limbaj), WordPress.
- Capital: ~25.000 EUR. Timp: 10–12 ore pe săptămână la început. 0–1 angajați.
- Nu construiește hardware. Cumpără dispozitive certificate existente și construiește platforma, integrarea, regulile de alertă și organizarea dispeceratului.
- Preferă B2B cu venit recurent. Ținta: un prim produs care ajunge la 1.000–3.000 EUR MRR (venit lunar recurent).

## Ideea

- **Ce este:** un serviciu pe abonament pentru lucrătorul izolat: cădere și imobilitate („om la pământ”), buton SOS și locația trimisă doar la alarmă; dispecerat externalizat (operatorii unei firme de pază din Oradea lucrează în ecranul fondatorului) care preia alarma, sună lucrătorul, clientul și 112; jurnal de alarme cu oră exactă, ca probă la ITM (inspectoratul teritorial de muncă); pachet de documente SSM (securitate și sănătate în muncă) și GDPR (protecția datelor) pentru client (R §1, §5, §6).
- **Ce iese din prima versiune:** pulsul (risc de dispozitiv medical, MDR clasa IIa/IIb), temperatura corpului (stresul termic devine doar indice din meteo), gazele (doar cu detectoarele certificate ale clientului), apropierea de utilaje (faza 2) (R §1).
- **Tehnic:** Traccar (server open-source) primește datele trackerelor Teltonika prin SIM-uri IoT; n8n aplică reguli fixe (pre-alarmă de 20–30 s, escaladare la 60 s); Oracle APEX e ecranul de dispecerat; un SMS direct din Traccar ca a doua cale; test automat zilnic (R §6). Construcția: ~80–160 de ore, adică 7–16 săptămâni la 10–12 h/săpt (R §6, estimare).
- **Dispozitive:** Teltonika TMT250, om la pământ + SOS, 88,50 EUR fără TVA (R §4; posibil doar 2G, de verificat). Teltonika GH5200, 176,53 EUR, marcat „End of life” pe o pagină Teltonika (R §4). Garmin inReach Mini 2 (satelit, fără om la pământ automat), 349,99 USD + 24,99–64,99 USD/lună, pentru 3–5 șefi de echipă din pădure (R §4). Nu se știe rata de alarme false; niciun furnizor nu publică rate din teren (R §1; N05 §6).
- **Preț ipotetic:** 20 EUR (~100 lei) pe lucrător pe lună cu dispozitiv inclus, contract 24–36 luni; sau 12 EUR (~60 lei) pe lună dacă clientul cumpără dispozitivul (~130 EUR) (R §7, estimare).
- **Pilot propus de cercetare:** 1 client din utilități, 30 de lucrători, 90 de zile; clientul cumpără dispozitivele, fără abonament 90 de zile, apoi 12 EUR/lucrător/lună dacă se ating țintele (purtare ≥85% din ture, 100% din alarmele de test ajung la dispecer, ≥95% în sub 60 s, alarme false <2 la 100 de ture-om). Fondatorul plătește platforma și dispeceratul. Total în bani, fără gaze și satelit: ~3.600–6.600 EUR (R §6, estimare).

## Cererea și piața

- **Bază legală:** HG 1091/2006 definește lucrul izolat (fără contact vizual și verbal, de regulă peste o oră, fără ajutor imediat) și cere informarea despre sistemul de supraveghere și legătură cu exteriorul (N02 Î2). Legea 319/2006 cere evaluarea riscurilor, primul ajutor și legătura cu urgențele (N02 Î1; art. 10 nevăzut direct, de verificat). Nu există normă românească dedicată dispozitivelor de alarmă (N02 Î2).
- **Decese:** 99 / 90 / 108 / 96 de decese la muncă în 2022–2025 în România (R §2). Bihor: 5 decese în 2025 (5,2% din țară), 6 în 2024 (R §2). Silvicultura a avut cele mai multe decese în 2024 (16) (R §2). Nu există studii independente că dispozitivele salvează vieți (R §1; N01 §6). Estimarea cercetării: 10–25% din decese sunt cazuri în care minutele contează (încredere scăzută) (R §2).
- **Costul pentru angajator:** amenzile SSM sunt mici (2.000–10.000 lei pe faptă). Un deces aduce dosar penal: la Aleșd (Bihor), administratorul unei firme forestiere a primit 2 ani cu suspendare, iar firma 18.000 lei amendă penală, la 8 ani de la faptă; daunele civile pot depăși 100.000 EUR (R §2; N01 §7). CAM (contribuția de asigurare pentru muncă) e 2,25% fixă, fără bonus-malus: „vă scade asigurarea” nu ține; niciun asigurător român nu dă reduceri (R §1; N05 §5; N06 §1).
- **Ce plătesc azi:** serviciu extern SSM 8–25 lei/angajat/lună (birouri, risc mic); GPS de flotă ~50 lei/vehicul/lună; deci 75–100 lei/lucrător/lună e de 3–10 ori onorariul SSM și se vinde doar pentru lucrătorii expuși (N05 §3).
- **Cine decide:** firmă < 50 angajați: patronul; 50–249: lucrătorul desemnat SSM + directorul de producție propun, administratorul aprobă; > 250: managerul HSE propune, achiziția trece prin procurement, ciclu 6–12 luni, adesea cu furnizori globali; utilități publice: director general + șef SSM, prin SEAP, probabil sub pragul de achiziție directă (80 lucrători × 75 lei × 12 = 72.000 lei/an; pragul ~270.000 lei din memorie, de verificat) (N05 §2).
- **Ținte în Bihor:** Compania de Apă Oradea (496 angajați), RER Vest (salubritate, ~720), Termoficare Oradea; Direcția Silvică Bihor (9 ocoale, Romsilva în reorganizare) și firme private de exploatare; fabricile mari (Plexus >2.400, Celestica 1.446, Connect Group 1.223), unde doar 5–15% lucrează izolat (estimare) (N05 §1).
- **Mărimea pieței:** Europa: 145 mil. EUR și 1,2 mil. utilizatori în 2024, ~10 EUR/utilizator/lună în medie (Berg Insight, raport comercial) (N03 §5). Bihor: 11–17 mii de lucrători izolați sau la risc înalt; 1.100–3.400 de abonamente realiste în 3–5 ani (estimare ±50%) (R §2).
- **Acceptarea de către muncitori:** într-un studiu din 2025, 46% din muncitorii din construcții n-ar purta purtabile biometrice și 59% n-ar folosi dispozitive de urmărire (văzut prin rezumat) (N05 §6). Legea 190/2018 art. 5 cere: interes legitim, informare prealabilă, consultarea sindicatului înainte de pornire, dovada că metodele mai blânde nu ajung, păstrarea datelor ≤ 30 de zile. ANSPDCP a amendat angajatori cu 2.000–5.000 EUR pentru GPS în afara programului (N05 §6; N02 Î6).
- **Vocabular și semnale:** căutările „om la pământ” / „lucrător izolat” dau doar butoane de panică pentru vârstnici; nicio licitație SEAP găsită pentru dispozitive de lucrător izolat; niciun blog SSM românesc pe temă (N05 §7). Romsilva a anunțat GPS pe utilaje și bodycam-uri pentru pădurari, nu alarmă personală; 157 de angajați Romsilva agresați în 5 ani (N03 §7).

## Concurența

- **În România:** niciun distribuitor Blackline, MSA, Twig sau Teltonika găsit, nicio firmă SSM cu acest serviciu, niciun startup local; doar aplicația gratuită „Safe Alone” din Cluj (SMS la un coleg, nu la dispecerat) (N03 §3). Lipsa din căutări nu dovedește lipsa din piață (R §1).
- **UK (piața cea mai dezvoltată):** StaySafe, aplicație 9,50 → 3,30 GBP/utilizator/lună, ARC (dispecerat 24/7) +1,85 GBP, satelit +1,50 GBP (listă publică G-Cloud, dec. 2025); Peoplesafe, 22,6 mil. GBP venit, >350.000 de lucrători, ~5,4 GBP realizat pe lucrător/lună; dispozitiv MySOS 14,99–16,49 GBP/lună (sursă terță) (N03 §2; N05 §4).
- **Liderii la gaze:** Blackline G7c ~56 EUR/lună cu dispecerat (1.512 USD/36 luni + 792 USD), API doar prin formular; MSA ALTAIR io 4 1.402,90 EUR; Twig One 793 EUR, Twig One Ex (ATEX) 1.701 EUR (R §3). Blackline intră pe piețe noi prin distribuitori locali (Italia 2015) (N03 §3, N05 §6).
- **Aplicațiile de telefon** costă 0–10 GBP/lună, dar chiar vânzătorii lor spun că la gaze, ATEX și industrie grea e nevoie de dispozitiv dedicat; telefonul stă în buzunar, bateria ține o zi; mulți muncitori nu au telefon de serviciu (de verificat) (N03 §4).
- **Dispecerate existente:** firmele de pază au deja operatori 24/7; caietele de sarcini publice (ONRC) cer monitorizare 24/7, alarme false incluse în tarif, teste lunare (N05 §5). Ele ar putea copia serviciul, pentru că au canal la aceiași clienți (N05 §5, estimare).

## Economia (calculul cercetării, toate estimări)

- Cost variabil pe lucrător/lună cu dispozitiv inclus: dispozitiv 90 EUR amortizat 36 luni 2,50 + pierderi 0,75 + SIM 1,50 + dispecerat externalizat 2,50 + comision canal 15% + asigurare/diverse 3% (R §7).
- La 20 EUR/lună: contribuție ~9,15 EUR/lucrător; rezultat lunar −290 EUR la 50 de lucrători, +380 EUR la 200, +5.650 EUR la 1.000 (cu 0,5 / 1 / 2,5 norme de personal la ~1.200 EUR). La 15 EUR: prag 290–700 de lucrători. Clientul cumpără dispozitivul + 12 EUR: aproape zero la 200. Dispecerat propriu 24/7: ~6.000 EUR/lună, se plătește abia peste ~2.400 de lucrători (R §7).
- Nu există tarife românești găsite pentru dispecerat „pe persoană conectată”, SIM IoT sau asigurare RC (răspundere civilă) pentru un dispecerat de alarme; costurile avocatului și asigurării sunt necunoscute (N05 §4; R §6).
- Finanțare: STEP nu finanțează produsul direct; realist doar voucherul de inovare UEFISCDI (≤50.000 lei) și servicii gratuite EDIH; pilotul îl plătesc clientul și fondatorul (R §8; N06 §7).

## Răspundere și reglementare

- Dispozitivul nu e EIP (echipament individual de protecție) și nu e dispozitiv medical dacă scopul declarat e „alarmare pentru securitatea în muncă”, fără puls „anormal” (N02 Î7).
- Contractul trebuie să promită un timp de preluare a alarmei, nu salvarea; răspunderea SSM rămâne la angajator; asigurare RC profesională pentru dispecerat; opinie despre Legea 333/2003 (pază) (R §5, estimare). Software-ul devine „produs” cu răspundere strictă după Directiva 2024/2853, de transpus până la 9.12.2026 (N02 Î10).
- În pădure, ghidul Inspecției Muncii interzice doborârea arborilor de unul singur; dispozitivul e a doua plasă, nu permisiune de lucru singur (R §5).
- Înainte de pilot e nevoie de ~15 documente (evaluarea riscurilor, procedura de răspuns, DPIA, consultarea sindicatului, contractul art. 28 GDPR, procedurile dispeceratului etc.) (R §5; N02 Î11).

## Ce se cere de la board

O notă 1–10, un vot (FUND / FUND IF / PASS), ce e puternic, ce ar ucide ideea (top 3, cel mai periculos întâi), întrebările pentru fondator și condițiile, dacă e FUND IF. La final: care e cea mai puternică versiune a acestui business pe care o vezi din lentila ta (poate diferi de ce s-a propus) și care ar trebui să fie primul client.

=== END BRIEF ===

Write your memo in exactly this shape:

# Monopoly lens
Score: <1-10> | Vote: FUND / FUND IF / PASS
## What is strong
## What would kill it (the top 3, most dangerous first)
## The questions I would ask the founder
## If FUND IF: the conditions
## Cea mai puternică versiune pe care o văd (și primul client)

Do not use any tools. Reply with the memo only (markdown).
