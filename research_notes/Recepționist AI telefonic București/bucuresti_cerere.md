# Demand side for an AI phone receptionist among Bucharest SMBs (as of October 2026)

Method note: direct page fetches to termene.ro, topfirme.com, snapcert.ro, capital.ro, dotro.ro, ec.europa.eu and romania-insider.com were all blocked by the egress proxy (EGRESS_BLOCKED). **Every fact below comes from search-result snippets/summaries, not from reading the full pages.** Treat exact figures as "per search snippet" and re-verify the critical ones (firm counts, Eurostat values) before publishing. Firm-count aggregators (termene, topfirme, listafirme, snapcert, certificatul) use different definitions (main vs. any CAEN code, active vs. all, "agenți economici" vs. SRLs), so counts conflict. I flag those conflicts wherever they show up.

Context for every count: Romania is moving from CAEN Rev.2 to Rev.3. Only 37.24% of the firms concerned had updated their codes by 25 Sep 2026, and the deadline has been extended to 25 Mar 2027 (HG 788/2026). Rev.2 and Rev.3 codes run in parallel until then, and some codes split (9602 becomes 9621 hair/barber + 9622 beauty treatments), so code-based counts are in flux — [ProTV](https://stirileprotv.ro/stiri/financiar/firmele-isi-pot-actualiza-codurile-caen-pana-la-25-martie-2027-termenul-de-tranzitie-a-fost-prelungit.html); [CCINA Constanța](https://www.ccina.ro/2026/10/05/actualizarea-caen-rev-3/); [ONRC CAEN Rev3 explanations](https://www.onrc.ro/index.php/ro/caen-rev3-explicatii?CLASA_REV2=9602&DENUMIRE_REV2=Coafur%C4%83+%C5%9Fi+alte+activit%C4%83%C5%A3i+de+%C3%AEnfrumuse%C5%A3are)

## 1. How many firms are in Bucharest (and Ilfov) in phone-heavy verticals?

### Takeaway
Summing the best available Bucharest figures for the core verticals gives roughly **19,000–20,000 firm-level entities**: dental ~2,400, specialist medical ~2,300, beauty ~2,500, auto repair ~1,900, restaurants ~5,100, real estate ~2,500, plumbing/HVAC ~2,000, vets ~370, private kindergartens 185. That excludes ~10,000 lawyers and ~500 notaries. Ilfov adds a meaningful but smaller pool, for example 318 dental firms. Many of these firms are inactive or have no employees, so the realistically addressable base is likely around half of the headline number (see Inferences).

### Cited Findings
**General Bucharest firm base**
- Bucharest had the most new registrations in the country: 22,550 between Jan and Aug 2026 (ONRC), and 20,276 by end-July, +6.4% y/y — [business24](https://business24.ro/firme-noi-romania/94-078-de-firme-inmatriculate-in-primele-opt-luni-din-2026-1667562); [Economica.net](https://www.economica.net/cate-firme-s-au-infiintat-in-romania-in-primele-sapte-luni-din-2026-lista-pe-zone-date-onrc_969297.html)
- Churn is also high: Bucharest had 3,782 struck-off firms (radieri) in Q1 2026 (+8.68% y/y) and 6,402 dissolutions in H1 2026 (+23.81%) — [StartupCafe](https://startupcafe.ro/cate-firme-din-romania-au-fost-radiate-la-inceput-de-2026-date-onrc-95798); [Economica.net](https://www.economica.net/firme-dizolvate-onrc-semestrul-unu_965482.html)
- Stock of firms "active and in operation" in Bucharest: 273,441 (clientsolutions.ro, table only runs to Jan 2024, so stale). Firme-on-line.ro shows 365,616 firms registered, incl. struck-off and suspended, as of 27 May 2026 — [clientsolutions.ro](https://www.clientsolutions.ro/lista-firme/); [firme-on-line.ro](https://www.firme-on-line.ro/cities/bucuresti/bucuresti.html)
- SMEs are 99.8% of Romanian firms (EU average 95%) — [Termene.ro](https://termene.ro/articole/romaniei-ii-lipsesc-companiile-mari-998-dintre-firmele-romanesti-sunt-imm-uri-media-europeana-este-de-95)

**Dental (CAEN 8623)**
- Termene.ro analysis of 2023 financial reports: Bucharest has **2,405** dental companies, about a quarter of the country's dental practices. Nationally, 10,068 economic agents are active (12,874 registered "in activity" per Punctul.ro). The snippet doesn't say whether 2,405 is out of the active or the registered total — [Termene.ro article](https://termene.ro/articole/afacerile-stomatologice-din-romania); [Punctul.ro](https://punctul.ro/afacerile-stomatologice-din-romania-au-crescut-cu-un-miliard-de-euro-in-ultimul-deceniu/)
- Ziarul Financiar data via Statista: in 2020 Bucharest had "nearly 3.2 thousand" dental offices (cabinete, not firms), far ahead of Timiș (842) — [Statista (ZF data)](https://www-statista-com.ezproxy.canberra.edu.au/statistics/1258620/romania-number-of-dental-offices-by-county)
- Older figure: more than 1,300 dental firms in Bucharest in 2016 — [Wall-Street.ro](https://www.wall-street.ro/articol/Social/211963/romania-tara-paradoxurilor-romanii-nu-se-duc-la-dentist-cu-anii-dar-piata-serviciilor-stamatologice-a-ajuns-la-un-mld-lei.html)
- National counts conflict: demoanaf ~15,602 active in the ONRC register; listafirme.eu 11,996; targetare 9,712; termene's code page lists ~17,400 incl. struck-off firms and in body text says ~8,250 with 8623 as main activity — [demoanaf](https://demoanaf.ro/caen/8623); [listafirme.eu](https://listafirme.eu/8623/d1.htm); [targetare](https://targetare.ro/top-firme-cod-caen/8623/activitati-de-asistenta-stomatologica); [termene.ro list](https://termene.ro/cod_caen/8623-activitati%2Bde%2Basistenta%2Bstomatologica/0)
- **Ilfov 8623: 318 economic agents** (0.31% of the county total), 147.3M lei turnover, 463 employees. Largest are Integra Medical Services (Balotești, 38.4M lei) and HOB Clinic Group (Voluntari, 14.7M lei) — [topfirme Ilfov 8623](https://www.topfirme.com/judet/ilfov/caen/8623/)

**Medical outpatient/specialist (CAEN 8622, 8621, 8690)**
- Bucharest 8622: **2,293 economic agents** (~0.47% of the city total), ~6.3bn lei turnover, 17,954 employees. Undated. Includes dialysis operators (Fresenius Nephrocare, Diaverum) and large networks, so the code is broader than small clinics — [topfirme Bucharest 8622](https://www.topfirme.com/judet/bucuresti/caen/8622/)
- National 8622 counts conflict: 8,881 or ~8,400 main activity (termene), 6,351 (caen.ro), 11,361 active per 2024 balance sheets (contabss), 22,044 incl. secondary codes (termene list) — [termene.ro 8622](https://termene.ro/cod_caen/8622-activitati-de-asistenta-medicala-specializata); [contabss](https://contabss.ro/caen/8622/); [caen.ro](https://caen.ro/clase/caen-8622-activitati-de-asistenta-medicala-specializata)
- 8621 (general practice): 1,686 firms nationally with it as main activity. No Bucharest figure found — [termene.ro 8621](https://termene.ro/cod_caen/8621-activitati-de-asistenta-medicala-generala)

**Beauty (CAEN 9602)**
- Bucharest: **2,488 economic agents**, first among counties, out of 13,401 nationally (topfirme county ranking). One snippet misattributed this figure to Ilfov; a separate snippet assigns 2,488 to "MUNICIPIUL BUCURESTI", which fits the ~21% Bucharest share below — [topfirme 9602](https://www.topfirme.com/caen/9602/)
- Snapcert (ANAF-based): 12,618 firms with 9602 as main activity, of which **7,266 (58%) are active**. Bucharest holds about 21% of firms — [Snapcert](https://snapcert.ro/caen/9602)
- Termene's 9602 list shows 53,862 entries (incl. struck-off and secondary codes) and estimates ~12,800 firms with main code 9602 — [termene.ro 9602](https://termene.ro/cod_caen/9602-coafura+si+alte+activitati+de+infrumusetare/)

**Auto repair (CAEN 4520; 9531 not found)**
- Bucharest: **1,918 economic agents** (topfirme). An older Sierra Quadrant analysis (5+ years old) had 1,682. The code includes car washes and tyre shops. Nationally, 20,514 firms have 4520 as main activity; contera counts 25,669 in operation out of 42,925 registered — [topfirme via search](https://www.topfirme.com/caen/4520/); [contera](https://contera.ro/caen/4520); [termene.ro 4520](https://termene.ro/cod_caen/4520-intretinerea+si+repararea+autovehiculelor/)
- Ilfov ranks 2nd nationally for 4520 by number of agents and turnover (843.2M lei). No exact count in the snippet — [topfirme 4520](https://www.topfirme.com/caen/4520/)

**Restaurants (CAEN 5610)**
- Bucharest: **5,083 firms** with 5610 as main activity, first among counties. Nationally 29,571 registered, 17,598 in operation. The snippet doesn't say whether 5,083 counts only those in operation — [certificatul.ro](https://certificatul.ro/firme/caen/5610)
- Sector context: HoReCa turnover was 58.44bn lei in 2025 (+12%) but net profit fell from 4.17bn to 3.54bn lei. Restaurant margins are ~6%. VAT on restaurant services rose from 5% to 11% on 1 Aug 2025 — [StartupCafe (HORA/Iancu Guda)](https://startupcafe.ro/romanii-au-lasat-bacsisuri-de-116-miliarde-eur-la-restaurant-in-2025-afacerile-horeca-au-crescut-dar-profitabilitatea-a-scazut-104545); [ZF](https://www.zf.ro/zf-24/realitate-anul-2025-horeca-vanzarile-restaurante-hoteluri-au-crescut-12-peste-inflatie-profitul-net-scazut-15-horeca-iese-usor-sifonata-dupa-aceasta-perioada-merge-departe-23209776)

**Real estate agencies (CAEN 6831)**
- Bucharest: **2,527 economic agents** (0.52% of Bucharest economic agents). National figures range from 5,929 (2024 balance sheets) to 18,120 — [topfirme Bucharest 6831](https://www.topfirme.com/judet/bucuresti/caen/6831/); [targetare](https://targetare.ro/top-firme-cod-caen/6831/agentii-imobiliare)

**Lawyers and notaries**
- Baroul București: **10,045 active lawyers** and 9,483 "definitivi" (counter, May–Sep 2025), "almost half the country's lawyers". By Sep 2026 the counter reads 16,779 "members", label changed, unexplained — [Baroul București](https://www.baroul-bucuresti.ro/stire/adunarea-generala-ordinara); [Baroul București – Ziua Baroului 2026](https://www.baroul-bucuresti.ro/stire/ziua-baroului-bucuresti-28-septembrie)
- Notaries: a 2014 Ministry of Justice order lists 519 posts for București, 506 occupied (stale). The bucuresteni.ro directory lists 201 notary offices in Bucharest+Ilfov (incomplete) — [legeaz.net (Ordin MJ 3591/2014)](https://legeaz.net/monitorul-oficial-752-2014/ordinul-mj-3591-c-2014); [bucuresteni.ro](https://www.bucuresteni.ro/info/birouri_notariale/o--nume/)

**Veterinary (CAEN 7500)**
- **374 active firms** with main CAEN 7500 in Bucharest (termene firm pages). National: 3,458 active in one place, 6,756 in another — [termene.ro (Sanita Vet page)](https://termene.ro/firma/11845027-SANITA-VET-SRL)
- Directories: yably.ro lists 112 vet clinics in Bucharest. bucuresteni.ro lists 37 with hospitalisation (Bucharest+Ilfov) — [yably](https://yably.ro/veterinari-si-clinici-veterinare/bucuresti); [bucuresteni.ro](https://www.bucuresteni.ro/info/cabinete_veterinare/with--internari/)

**Trades, cleaning, fitness**
- Plumbing/heating/AC (CAEN 4322), Bucharest: **2,043 economic agents** (0.42%). The top of the list is large contractors such as Energomontaj (279.4M lei) — [topfirme Bucharest 4322](https://www.topfirme.com/judet/bucuresti/caen/4322/)
- Electricians (4321): no Bucharest figure found.
- Cleaning (8121): ~3,363 companies nationally with main activity 8121 (caen.ro) vs 7,696 (firme.info). No Bucharest figure — [caen.ro 8121](https://caen.ro/clase/caen-8121-activitati-generale-de-curatenie-a-cladirilor)
- Fitness (9313), Bucharest: topfirme shows 954 employees and 26.1M lei profit for the segment. No firm count in the snippet. Termene lists 7,181 nationally incl. struck-off — [topfirme Bucharest 9313](https://www.topfirme.com/judet/bucuresti/caen/9313/)

**Private kindergartens / after-schools**
- Bucharest had **185 authorized/accredited private kindergartens in 2025** (192 in 2024) vs 124 state ones. Private units average 67.5 children vs 285 per state unit (ISMB data) — [Edupedu](https://www.edupedu.ro/zero-gradinite-de-stat-noi-in-bucuresti-in-ultimii-7-ani-perioada-in-care-numarul-gradinitelor-private-le-a-depasit-pe-cele-de-stat-cu-aproape-50-analiza-lista-gradinite-private-2025-bucuresti/)
- After-schools: "hundreds" of private after-schools operate in Bucharest (Digi24, probably 2022). There is no official count. Full packages reach 2,000 lei/month — [Digi24](https://www.digi24.ro/stiri/actualitate/social/ministerul-educatiei-recomanda-parintilor-sa-evite-inscrierea-copiilor-la-afterschool-uri-private-nu-sunt-centre-de-invatamant-2744021); [Bugetul.ro](https://www.bugetul.ro/cat-te-costa-sa-iti-inscrii-copilul-la-un-afterschool-din-bucuresti/)

### Inferences
- Headline sum for Bucharest (dental 2,405 + 8622 2,293 + beauty 2,488 + auto 1,918 + restaurants 5,083 + real estate 2,527 + plumbing/HVAC 2,043 + vets 374 + private kindergartens 185) is ≈ **19,300 entities**. Law offices (thousands of firms behind 10,000+ lawyers) and ~500 notaries come on top. Some counts include inactive firms. In beauty, for example, Snapcert shows only 58% of 9602 firms active nationally, so a **realistic active, addressable pool is likely ~10,000–12,000 Bucharest firms** across these verticals. This is my estimate, not a sourced figure.
- topfirme's percentages (2,527 = 0.52%; 2,293 = 0.47%) both imply a base of ~486,000–488,000 "economic agents" in Bucharest. That base probably includes PFAs/IIs and inactive entities, so topfirme counts are likely inclusive (over-counting) rather than active-only.
- Many beauty, dental and vet practitioners operate as PFA/II or individual medical practices (cabinete medicale individuale) rather than SRLs, and lawyers as cabinete individuale. SRL-based CAEN counts may undercount the number of *locations* that answer phones, as the ZF 2020 "3,200 dental offices" vs the 2,405 firms suggests.
- Most promising by density + phone dependence: dental (~2,400 firms + ~3,200 offices; high ticket per booking), private clinics (~2,300), beauty (~2,500, but low ticket and fragmented), auto service (~1,900), vets (~370, small but phone-heavy, with emergencies). Restaurants are numerous (5,000+), but reservations are a smaller share of their revenue.

### Gaps
- No ONRC/INS official Bucharest count by CAEN code was obtainable (pages blocked; INS TEMPO not reachable). Counts for 8621, 8690, 4321, 8121, 9313, 9531 in Bucharest were not found.
- Ilfov counts beyond dental (318) were not found as exact numbers.
- Notary count is from 2014. No current count of after-schools.
- No size distribution (employees per firm) for Bucharest by vertical. That would be needed to separate firms with a front desk from solo practitioners.

## 2. How do Romanians book services: phone vs online vs WhatsApp? Platform penetration

### Takeaway
I found no independent, representative Romanian survey on booking channels for private services (clinics, salons, auto). The evidence points indirectly to the phone still dominating private-sector booking. Online booking is growing, mainly through clinic-network portals, Docbook and Fresha, but their penetration among small Bucharest businesses looks low. WhatsApp is near-universal among consumers, but there is no data on WhatsApp Business use by SMBs.

### Cited Findings
- **Docplanner (ZnanyLekarz/Doctoralia) does not appear to operate in Romania.** Its group lists 13 countries and brands (Doctoralia, ZnanyLekarz, MioDottore, Jameda), none Romanian — [Docplanner Group](https://www.docplanner.com/)
- **Docbook** (local market leader): 500,000+ online bookings cumulatively from its 2018 launch to mid-2023. Online bookings +20% in 2023 vs 2022. ~7,500 doctors in 225+ cities (Aug 2024). The site now claims 8,500+ doctors (undated). 77% of users read reviews. ~90% book paid services. 55%+ found a slot within 96 hours in 2024 — [Forbes.ro](https://www.forbes.ro/peste-500-000-de-programari-online-la-medici-prin-platforma-docbook-77-dintre-pacienti-sunt-atenti-la-recenzii-405930); [Ziarul News, Aug 2024](https://ziarulnews.ro/2024/08/28/docbook-depaseste-500-000-de-programari-online-77-dintre-pacienti-verifica-recenziile-inainte-de-a-alege-un-medic/); [docbook.ro](https://www.docbook.ro/)
- Regina Maria reported 1 million online bookings on its telemedicine platform (older article, telemedicine only) — [Economica.net](https://www.economica.net/reteaua-privata-de-sanatate-regina-maria-a-inregistrat-un-milion-de-programari-online-in-platforma-sa-de-telemedicina_666911.html). No 2025 online vs call-centre split was found for Regina Maria, MedLife or Sanador. MedLife's online booking reportedly excludes complex investigations, e.g. MRI with contrast, which go through the call centre (third-party guide) — [medlife.contact-telefon.ro](https://medlife.contact-telefon.ro/)
- MedOcean analysed **100,000+ phone calls** between prospective patients and private-clinic operators (Jan 2025–Jan 2026). This shows phone volume remains substantial in private healthcare (vendor data) — [AGERPRES press release](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680)
- Ipsos (July 2021, online, urban 18–60): for remote consultations, the phone was used by 20% and WhatsApp by 12%. Ipsos describes Romanian telemedicine as dominated by phone and WhatsApp depending on the doctor's availability (dated) — [Ipsos Romania](https://www.ipsos.com/ro-ro/retrospectiva-privind-accesarea-serviciilor-medicale-pandemie)
- Public health: AtlasIntel (March 2026, n=2,325) found 32.6% had made online appointments in the public health system. AtlasIntel (June 2026, n=2,002) found ~88% would choose online booking for state hospitals — [StartupCafe](https://startupcafe.ro/romanii-si-serviciile-digitale-de-stat-plata-taxelor-pe-primul-loc-ce-vor-ei-in-2026-studiu-96599); [Go4it](https://www.go4it.ro/content/internet/romanii-vor-mai-putine-ghisee-si-mai-multe-servicii-online-ce-arata-noul-studiu-atlasintel-19277915)
- Older INSCOP: 17.4% would not use online public services, preferring direct contact with an official — [Biziday](https://www.biziday.ro/331048-2/)
- National e-SănătateaMea portal: CNAS-contracted providers must use it from Q4 2026. Patients can still book by phone, and patient organisations want phone booking kept (rural, low digital skills) — [Digi24](https://www.digi24.ro/stiri/actualitate/social/romanii-ar-putea-consulta-online-retetele-trimiterile-si-istoricul-medical-cum-va-functiona-platforma-e-sanatateamea-din-septembrie-3906571); [medic24](https://medic24.ro/portalul-esanatateamea-ajunge-la-promulgare-programari-online-din-trimestrul-iv/)
- **Beauty:** RoBeauty (pandemic-era article) puts 15–30% of Bucharest salon bookings through online platforms/social/chat/email/phone. The figure is ambiguous and doesn't separate phone from online — [Business Magazin](https://www.businessmagazin.ro/actualitate/afaceri/industria-pe-care-pandemia-a-afectat-o-semnificativ-scaderile-sunt-20064605). Fresha lists 103 venues in București on its "best salons" page, 35 verified beauty salons, 20+ hair salons and 29 nail salons (2026 snapshots) — [Fresha București](https://www.fresha.com/lp/en/ro-bucure%C8%99ti). A sponsored a1.ro piece "(P)" claims big-city salons are digitising fast while small towns use phone + social-media messages — [a1.ro (advertorial)](https://a1.ro/news/social/p-bookingul-de-beauty-sa-mutat-online-iar-romania-prinde-din-urma-un-trend-care-in-vest-e-deja-norma-id1160486.html). Vendor blog claim: "67% of beauty clients prefer digital booking", unsourced — [salononline.ro (vendor)](https://salononline.ro/blog/ghid-practic-cum-sa-implementezi-corect-sistemul-perfect-de-programari/)
- **Booksy, Stailer, RevMy:** no Romanian partner counts or penetration data were found.
- **Auto service:** a Romanian auto-shop software vendor argues online self-booking works poorly in auto repair because duration, cost and parts availability can't be promised upfront. Its tool is an internal calendar, not client-facing (vendor opinion) — [ServiceProX](https://www.serviceprox.ro/)
- **WhatsApp:** 15M+ active WhatsApp Messenger users in Romania in Q2 2025 (Sensor Tower). An older Digital 2023 report had 86.9% of Romanian internet users on WhatsApp monthly. There is no data on SMB WhatsApp Business adoption for bookings. One API vendor claims 200+ Romanian business clients — [Sensor Tower](https://sensortower.com/blog/2025-q2-unified-top-5-communication%20apps-units-ro-6070aae1241bc16eb81f5bab); [whapi.ro (vendor)](https://whapi.ro/ghid-whatsapp-business-romania.html)
- Vendor (unsourced): "73% of patients prefer to book online; 59% frustrated by hold times/office hours on phone booking" — [amed.md (vendor, Moldova)](https://amed.md/programare-online-la-medic/)

### Inferences
- Fresha's ~103 Bucharest venues vs ~2,500 beauty firms implies **<5% Fresha penetration** among Bucharest salons. Docbook's 8,500 doctors nationally is a fraction of private practitioners. Online-booking marketplaces have not displaced phone/WhatsApp/Instagram DM booking for small operators. This is an estimate from the counts above.
- Phone-heavy segments: private clinics (MedOcean's 100k+ calls; complex investigations routed to the call centre), auto service (non-standard jobs), and older/less digital customers (see Section 5 on digital skills). Younger urban consumers in Bucharest are shifting to online and messaging, so an AI receptionist offering both voice and WhatsApp/SMS fits the hybrid behaviour.
- The public e-SănătateaMea portal may raise consumers' expectation of 24/7 booking, which could spill over to private providers. This is speculative.

### Gaps
- No independent Romanian survey of booking channels (phone/online/WhatsApp/walk-in) for clinics, salons or auto service.
- No Booksy/Stailer/RevMy Romania data. No WhatsApp Business SMB adoption data. No Bucharest-specific splits.

## 3. Evidence of unanswered or missed calls in Romanian SMBs

### Takeaway
The only quantitative Romanian evidence comes from vendors. The main one is MedOcean (100k+ private-clinic calls), which finds **39.6% of callers seeking a new appointment end the first call without one**. It measures failed conversion, not strictly unanswered calls. I found no independent Romanian study of unanswered-call rates or mystery-calling response rates (the only mystery-calling study is from 2012).

### Cited Findings
- MedOcean (AI call analytics start-up), subset of 100,000+ calls, Jan 2025–Jan 2026, private clinics: **39.6% of people calling for a new appointment leave without one** at the first interaction. Booking rate is 83.77% when the operator shows empathy vs 21.88% with cold or rushed operators. Conversion drops to 5.84% when no clear appointment proposal is made. Price is "not the main reason" for drop-off. **Conflict of interest:** MedOcean sells call analytics to clinics — [AGERPRES](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680); [Economica.net](https://www.economica.net/foto-studiu-in-premiera-in-sistemul-medical-de-ce-pierd-clinicile-4-din-10-pacienti-romani-de-la-primul-apel_908536.html); [Capital.ro](https://www.capital.ro/inteligenta-artificiala-intra-in-call-centerul-medical-cum-pierd-clinicile-aproape-40-dintre-pacienti-inca-de-la-primul-apel.html)
- Another MedOcean-related piece cites ~1 in 4 patients lost at first call for empathy/interaction reasons. It's unclear whether this is the same metric — [Romania Pozitiva](https://www.romaniapozitiva.ro/romania-pozitiva/cum-se-schimba-comportamentul-pacientilor-in-2026-concluziile-medocean-din-analizarea-cu-ajutorul-unei-tehnologii-proprii-cu-ai-a-peste-100-000-de-conversatii-telefonice/)
- MedOcean targets 100 clients in 2026 and a €1M pre-seed round — [start-up.ro](https://start-up.ro/medocean-duce-analiza-apelurilor-medicale-pe-doua-piete-noi-si-pregateste-runda-pre-seed-in-2026-vrea-100-de-clienti-si-finantare-de-1-mil-euro/)
- Mystery calling by VBS-Business Solutions at 11 major private clinics in Bucharest, 3–9 Jan 2012: only in half of cases were "mystery patients" greeted in an upbeat tone. It measured etiquette, not answer rates (dated 2012) — [Customer Service Excellence Club blog](http://fidelizareclienti.blogspot.com/2012/01/empatie-sau-indiferenta-realitatea-din.html)
- Vendor claims (unsourced): clinics lose "up to 20%" of potential appointments to unanswered calls — [centraletelefonice.ro (vendor)](https://centraletelefonice.ro/blog/centrala-telefonica-clinici-medicale/). Dotro publishes a "how many calls does a firm lose per month" calculator article (content not readable) — [dotro.ro (vendor)](https://www.dotro.ro/blog/cate-apeluri-pierde-o-firma)
- Consumer frustration with phone queues and IVR: a bill capping call-centre wait times at 5 minutes has been stuck in Parliament for nearly three years. Complaints mention 55-minute waits and repetitive robots before reaching a human — [RomaniaTV](https://www.romaniatv.net/legea-prin-care-este-limitat-timpul-de-asteptare-in-call-center-la-cinci-minute-blocata-in-parlament-de-aproape-trei-ani-romanii-tot-mai-furiosi-am-avut-cazuri-de-sesizari-si-reclamatii-d_9410698.html)
- The often-quoted Health Minister line "Am primit «n» telefoane… nu am răspuns" is about the **minister not answering lobbying calls from clinics**, not clinics failing to answer patients. Don't use it as evidence — [Digi24](https://www.digi24.ro/stiri/actualitate/social/ministrul-sanatatii-despre-controalele-din-clinicile-private-am-primit-n-telefoane-nu-am-raspuns-3504297)
- ANPC received nearly 800 dental-patient complaints in a year, about treatment not matching advertising, not phone access — [Observator](https://observatornews.ro/sanatate/promisiunile-clinicilor-stomatologice-care-pot-pacali-pacientii-nu-exista-garantii-in-domeniul-medical-656537.html)

### Inferences
- The MedOcean data (call volume, ~40% first-call failure, empathy-driven conversion gap) supports the problem thesis for clinics. An AI receptionist would have to *convert* as well as *answer* (clear slot proposals, empathetic tone). It is the only large Romanian dataset, and it comes from a vendor.
- The evidence base is thin for salons, auto service, trades and vets. A pitch to these verticals would need the company's own mystery-calling study, e.g. calling ~200 Bucharest businesses after hours and at lunchtime. That would also double as a lead-generation asset.

### Gaps
- No independent mystery-shopping or response-rate study (2020–2026) for Romanian SMBs. No ANPC data on unanswered calls. No data on share of calls arriving after hours.

## 4. Cost of a human receptionist in Bucharest (2026) and of virtual-secretary or call-answering outsourcing

### Takeaway
A Bucharest clinic or salon receptionist is advertised at roughly **3,000–5,000 lei net/month** in 2026. That is ~5,100–8,700 lei gross and **~5,200–8,900 lei total employer cost, ≈ €1,000–1,750**. Covering 10–12 hours a day, six days a week needs ~2 FTE. Human outsourced alternatives start at ~€100–250/month for limited hours. Romanian AI-voice vendors list ~€19–260/month plus setup, so AI undercuts a human receptionist roughly 5–10x on headline price.

### Cited Findings
**Statutory base (2026)**
- Minimum gross wage: 4,050 lei (Jan–Jun 2026), **4,325 lei from 1 July 2026** (HG 146/2026). Net ≈ 2,699 lei (with 200 lei untaxed). Employer cost ≈ 4,418–4,422 lei incl. CAM 2.25%, the employer's work-insurance contribution. Sources differ (93 vs 97 lei CAM) depending on the base — [StartupCafe](https://startupcafe.ro/salariul-minim-2026-a-crescut-inclusiv-in-firmele-private-cat-primeste-net-angajatul-si-ce-cost-suporta-patronul-102626); [Profit.ro](https://profit.ro/taxe-si-consultanta/vin-bani-mai-multi-pentru-unii-angajati-bani-in-plus-in-mana-dupa-cresterea-salariului-minim-din-vara-calcul-concret-cat-primeste-angajatul-cat-ia-statul-22286563); [infocontact.ro](https://www.infocontact.ro/salariul-minim-pe-economie-2026/)
- Employee contributions: CAS 25%, CASS 10%, income tax 10% — [salariucalculator.ro](https://salariucalculator.ro/)
- Bucharest average net wage (INS): **7,631 lei net / 12,737 lei gross in April 2026** (8,039 net in March 2026). The national average is 5,843 lei net. The average is skewed upward by IT, finance and management — [Forbes.ro via search](https://www.forbes.ro/?p=511211); [logos-pres.md](https://logos-pres.md/noutati/unde-se-inregistreaza-cele-mai-mari-si-cele-mai-mici-salarii-in-romania/)

**Receptionist pay, Bucharest (job ads 2026)**
- OLX (June 2026): physiotherapy clinic front desk, Sector 2, 3,000–3,500 lei; medical receptionist, Sector 2, 3,800–4,300 lei; aesthetics clinic, Sector 3, 3,000–4,500 lei. Net/gross not stated — [OLX](https://www.olx.ro/locuri-de-munca/bucuresti/q-receptionera-clinica/)
- Romedic (Sep 2026): Eurosanity medical centre 4,000–5,000 lei (negotiable); SuperDiet nutrition clinic, Sector 1, 3,000–3,500 lei — [Romedic](https://www.romedic.ro/joburi/receptie-secretariat)
- Jooble salary estimate (29 Jul 2026): clinic receptionist in Bucharest ~€844/month; generic receptionist €655; clinic secretary-reception €900 — [Jooble](https://ro.jooble.org/salary/receptionera+clinica/Bucure%C5%9Fti)
- BestJobs: hospital (Sf. Sava) medical receptionist €690–700. City Dent receptionist market estimate €900–995 (not employer-posted) — [BestJobs](https://www.bestjobs.eu/locuri-de-munca-in-bucuresti/receptie+clinica)
- Beauty-clinic receptionist ad: 4,500–5,500 lei (one listing says 4,500–5,000 net; may be old) — [Jooble](https://ro.jooble.org/locuri-de-munca-receptioner+hotel/Bucure%C5%9Fti)
- Hotel-receptionist benchmark: Bucharest average 3,810 lei net (meseriile.ro). Ghidsalariu shows 5,914 lei gross (INS 2024), but the same figure also appears as the national P90, so it may be a data error — [meseriile.ro](https://meseriile.ro/salariu/receptioner-hotel/); [ghidsalariu.ro](https://ghidsalariu.ro/salariu/receptioner-hotel)

**Human outsourcing / virtual secretary (Romania)**
- TransTel Services: human virtual secretary **from €250/month + VAT**, minimum 6-month contract. Includes answering machine, fax server, IVR (page likely old) — [tts.ro](http://www.tts.ro/secretariat-virtual.html)
- StartHUB: 10 hours/month secretariat subscription, €600 for 6 months, **≈€100/month**, premium hours €52 — [StartHUB](https://www.starthub.ro/servicii/servicii-de-secretariat)
- Regus call answering in Bucharest **from 6 RON/day** (~180 RON/month). It is an address+call package, not a dedicated secretary — [Regus](https://www.regus.com/ro/ro/bucuresti/bucharest/virtual-offices)
- Teasist: secretariat services incl. monthly subscription, price not published — [Teasist](https://teasist.ro/servicii-de-secretariat/)
- Call-centre outsourcing in Romania: **$12–22/hour** fully loaded (TDS Global Solutions). GoodFirms median $25/hour across 13 Romanian firms (Oct 2026). Rocurier from €1/call (order confirmations) — [TDS](https://www.tdsgs.com/call-center-outsourcing/romania); [GoodFirms](https://www.goodfirms.co/bpo-services/call-center-services/romania); [Rocurier](https://www.rocurier.com/call-center)
- Virtual PBX (no human) price anchors: centraletelefonice.ro €9/€39/€69/month; Mediasat €35/€49 + VAT — [centraletelefonice.ro](https://centraletelefonice.ro/); [Mediasat](https://www.mediasat.ro/ro/telefonie#mdst-telefonie-numere-premium)

**AI-receptionist price points in Romania (vendor marketing; for willingness-to-pay context)**
- receptie-clinica.ai: setup from €1,200 one-off + support from €150/month + ~€0.19/minute usage. Example: small clinic (1–5 doctors) ~€104/month for ~400 calls; medium (6–15 doctors) ~€261/month for ~1,000 calls, excl. VAT. Integrations with iStoma, icMED, iClinic — [receptie-clinica.ai](https://receptie-clinica.ai/)
- AllAI: Starter €24/month (web chat + booking), Professional €59/month (adds WhatsApp, voice AI, calendar), 14-day trial — [allai.ro](https://allai.ro/industrii/medical)
- Dotro SmartPBX: virtual PBX from €14/month, AI voice assistant from €19/month, €79 package with 5 simultaneous AI calls and 3 agents, no minimum term — [dotro.ro](https://www.dotro.ro/asistent-vocal-ai-smartpbx/)
- VoiceFleet: from €99/month (Ireland/EU-focused) — [VoiceFleet](https://voicefleet.ai/blog/ai-receptionist-cabinet-stomatologic-romania-2026)
- Clinova: custom pricing by call volume, first week free, no long-term contract — [clinova.ro](https://clinova.ro/)

### Inferences
- Net→gross conversion (my calculation, ignoring the personal deduction, so slightly conservative). Net ≈ gross × 0.65 × 0.90 = 0.585 × gross:
  - 3,500 lei net ≈ 5,980 gross ≈ 6,120 lei employer cost
  - 4,000 net ≈ 6,840 gross ≈ 6,990 lei employer cost
  - 5,000 net ≈ 8,550 gross ≈ 8,740 lei employer cost
  - At an assumed ~5.1 RON/EUR, that is **≈ €1,200 / €1,370 / €1,710 per month** per receptionist.
- A clinic open 08:00–20:00 Mon–Sat (72 h/week), with 40-h FTEs and ~21 days of annual leave, needs ~2 receptionists ≈ 12,000–14,000 lei (~€2,400–2,750) per month. That still leaves nights and Sundays uncovered.
- Willingness-to-pay anchors: AI at ~€100–260/month (receptie-clinica.ai examples) is roughly **8–20% of one receptionist's cost**. The cheapest human alternative (StartHUB, €100 for 10 h) covers only ~2.5 h/week. Plausible price bands: ~€50–150/month for micro businesses (salons, auto, trades, vets) and ~€150–400/month for clinics. Both are consistent with vendor list prices. These are inferences, not survey data.
- Note the minimum-wage reference: many small salons and auto shops pay staff near the minimum (employer cost ~4,420 lei ≈ €870). For them, the AI's value is extra coverage (calls missed while the owner works on a client), not replacing a receptionist.

### Gaps
- No Paylab, eJobs (Salario) or Undelucram figure specific to "recepționer/ă clinică București 2026" with net/gross clearly stated.
- No current, verified Romanian price list for human virtual-receptionist services (TransTel page probably dated). No survey of SMB willingness to pay for call answering.

## 5. Romanian consumer attitudes toward chatbots, voicebots and AI; digital skills; robocalls

### Takeaway
Romanians are **rapidly adopting AI tools (68% daily use in 2026, up from 47%) but trust is falling.** Trust in AI output dropped from 65% to 55%, and 7 in 10 distrust AI working without human oversight. Romania has the **lowest basic digital skills in the EU (31.8% in 2025)**. A surge of robot-voice fraud calls may have primed suspicion of automated voices. An AI receptionist should identify itself, offer a human fallback, and stay especially careful in medical contexts. There is no Romanian survey specifically on willingness to talk to an AI phone agent.

### Cited Findings
**AI use and trust**
- Reveal Marketing Research (Feb 2026): AI use in daily life went from 47% (2025) to **68% (2026)**. "Useful but risky" rose from 49% to 53%. High/very high confidence in AI output fell from **65% to 55%**. Top use is information search (83%), then work (44%) and learning (39%) — [Romania Insider](https://www.romania-insider.com/study-romanians-artificial-intelligence-use-feb-2026)
- Reveal (2025 wave, n=1,000, ±3.1%): 47% use AI daily, women 51% vs men 42%, 18–24-year-olds 70%. ChatGPT 60%, Gemini 29%, Siri 21% — [CECCAR Business Magazine](https://www.ceccarbusinessmagazine.ro/romanii-folosesc-tot-mai-mult-inteligenta-artificiala-in-activitatile-lor-zilnice/a/k85NKT9MVfb048GOitqF)
- RoCoach + Novel Research (May–June 2025, n=800 urban working people, not nationally representative): **7 in 10 don't trust AI working without human intervention.** Only 20% would accept fully autonomous AI professional evaluations; ~40% want a human to validate; 27% reject fully automated decisions. 68% are very or moderately worried about AI's use of their personal data — [Termene.ro](https://termene.ro/articole/romanii-nu-prea-au-incredere-in-inteligenta-artificiala); [Romania Insider](https://www.romania-insider.com/most-romanians-do-not-trust-ai-without-human-intervention-survey-shows)
- MKOR "AI Adoption Report România 2026" (n=1,000, national, ages 18–65, fieldwork May & Aug 2026): 52% thought an AI-written text was human-written. **32% would feel betrayed if explanations of their medical tests were AI-generated** — [StartupCafe](https://startupcafe.ro/jumatate-romani-nu-recunosc-text-inteligenta-artificiala-studiu-107187); [Cotidianul](https://www.cotidianul.ro/romanii-folosesc-masiv-ai-dar-jumatate-nu-o-pot-recunoaste-ruptura-periculoasa-intre-utilizare-si-incredere/)
- eJobs (Jan 2026): nearly half said they intentionally use AI tools, customer-service chatbots or image generators. **4 in 10 would be uncomfortable sharing personal info with AI** even for more personalised service — [Romania Insider](https://www.romania-insider.com/ejobs-romania-artificial-intelligence-use-jan-2026)
- AtlasIntel for Edge Institute (July 2026): 83% use AI in at least one context; workplace adoption still limited — [Romania Insider](https://www.romania-insider.com/romanian-ai-use-survey-july-2026)
- Study (June 2026, sponsor not identified in snippet): ~8 in 10 Romanians would trust AI to make online purchases — [Romania Insider](https://www.romania-insider.com/romanians-trust-ai-online-purchases-study-june-2026)
- Ipsos (31-country survey, date not shown in snippet): 77% of Romanians say they understand what AI is (4th place). 50% are nervous about AI; 62% are excited — [Ipsos Romania](https://www.ipsos.com/ro-ro/romanii-si-inteligenta-artificiala-intre-ignoranta-si-fascinatie)
- Special Eurobarometer 557 (fieldwork Sep–Oct 2024, published Feb 2025): Romania is one of three EU states where distrust of AI-based research (34%) exceeds trust (25%) (Verian secondary analysis) — [Verian](https://www.veriangroup.com/news-and-insights/artificial-intelligence-and-the-future-of-work); [Eurobarometer 3227](https://europa.eu/eurobarometer/surveys/detail/3227)
- Older Eurobarometer 95.2-based paper: Romanians are slightly more pessimistic than the EU average and more worried about AI and jobs — [Unibuc CMP journal](https://journals.unibuc.ro/index.php/cmp/article/view/937)

**Human vs bot in customer service**
- No Romanian survey with a clear "prefer human vs bot" percentage was found. Revista Cariere notes no market research exists on Romanians and robot-assisted shopping — [Revista Cariere](https://www.revistacariere.ro/noutati/tehnologie/studiu-95-dintre-millennials-nu-vor-sa-fie-asistati-la-cumparaturi-de-roboti)
- Regional comparator (Daktela, Czech contact-centre vendor, May 2025; sample country not confirmed): 60.9% prefer a human operator, 28.2% indifferent, 11% prefer a robot. **~80% would prefer a bot answer within 3 minutes over a human answer after 3 days** — [Daktela](https://daktela.com/press-releases/customers-would-rather-talk-to-a-robot-now-than-a-human-in-five-minutes)
- International: 71% of customers prefer a human agent over a chatbot, and 60% say chatbots often fail to understand their issue — [The Conversation](https://theconversation.com/chatbots-are-on-the-rise-but-customers-still-trust-human-agents-more-259980)
- Observator ran a poll "Preferați operatorii reali sau pe cei cu AI?" (result not in snippet) — [Observator](https://observatornews.ro/sondaj/sondaj-preferati-operatorii-reali-sau-pe-cei-cu-inteligenta-artificiala-644667.html)

**Digital skills**
- Eurostat 2025: **31.8% of Romanians have at least basic digital skills, last in the EU** (Bulgaria 38.3%; EU avg 60.4%; target 80% by 2030). Ages 16–24: 53.3%. All 4 Romanian macro-regions are below 40% — [Romania Insider](https://www.romania-insider.com/eurostat-basic-digital-skills-ro-ranks-last-apr-2026); [Eurostat regional](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_society_statistics_at_regional_level); [bne IntelliNews](https://www.intellinews.com/bulgaria-romania-lag-eu-peers-on-digital-skills-eurostat-data-shows-439818/)
- DESI 2025 (2023 data): 27.7% basic digital skills vs EU 54%. The EC recommends upskilling of private-sector employees and older people — [CRPE](https://www.crpe.ro/en/inclusive-digitalisation-in-romania-between-targets-and-reality/); [EC Romania 2025 Digital Decade report](https://digital-strategy.ec.europa.eu/en/factpages/romania-2025-digital-decade-country-report)
- Romania exceeds the EU average for household internet access but ranks last on digital skills (Aug 2026) — [Romania Insider](https://www.romania-insider.com/social-monitor-digital-skills-romania-august-2026)

**Robocalls and phone fraud**
- Romania saw an "alarming" rise in fraudulent calls using **robotic voices** and spoofed national numbers. From **7 July 2025**, ANCOM requires operators to block calls from abroad that spoof Romanian numbers — [Antena 3](https://www.antena3.ro/actualitate/apelurile-false-care-ii-dispera-pe-romani-de-cateva-luni-vor-fi-blocate-ancom-ia-masuri-impotriva-fraudei-telefonice-748391.html); [Mobilissimo](https://www.mobilissimo.ro/stiri-telefoane/ancom-trece-la-blocaje-automate-apelurile-frauduloase-din-afara-tarii-vor-fi-filtrate-de-operatori)
- 60%+ (about two-thirds) of Romanians have been targeted by a phone-fraud attempt (study cited by ProTV) — [Știrile ProTV](https://stirileprotv.ro/stiri/actualitate/apelurile-tip-zspoofing-blocate-automat-de-operatorii-de-telefonie-peste-60-dintre-romani-pica-in-plasa-escrocilor.html)
- Law 506/2004 bans automated commercial calls without prior express consent. That matters for outbound reminders and campaigns, not inbound answering (commercial guide) — [infocontact.ro](https://www.infocontact.ro/blocare-apeluri-spam-telemarketing-gdpr/)
- ANCOM complaints rose 27% to 5,244 in 2025, mostly number portability. Telemarketing is not named among the top categories — [Techrider](https://techrider.ro/tehnologie/telecom/ancom-reclamatii-comunicatii-electronice-servicii-digitale-2025/)

### Inferences
- Consumers are not hostile to AI per se: adoption is high, especially among the young and urban, and Bucharest has the best digital profile in Romania. They are wary of unsupervised AI and data use, and the medical context is sensitive (32% "betrayed"). Speed beats channel preference (Daktela: bot in 3 min > human in 3 days), so the strongest framing is "answers every call instantly and hands off to a human", not "replaces staff".
- Robot-voice fraud waves in 2025 likely make some callers, especially older ones, hang up on synthetic-sounding voices. Natural Romanian speech, quick self-identification and callback/SMS confirmation matter. Older patients are a large share of clinic callers, and low digital skills (31.8%) mean voice is often their *only* channel. That argues for voice AI over app/online-only booking.

### Gaps
- No Romanian survey on willingness to speak with an AI phone agent, or on acceptance by age group for voice specifically.
- No data on Romanian reactions to disclosed AI voice agents (vs fraud robocalls). No ANCOM data on robocall complaints.

## 6. SMB digital adoption and spending in Romania

### Takeaway
Romanian firms are at or near the bottom of the EU on every digital-adoption metric: **AI 5.2% (last), CRM 13.9%, any business software 32%, social media 48%, website <60%.** Micro firms, the bulk of the target market, are not even covered by Eurostat and are presumably lower. Typical small-business software budgets are modest: hundreds of euros a month for 10–30-employee firms, often ≤100 lei/month for online ads among micro-SMBs (older data). That points to price sensitivity and a need for done-for-you setup.

### Cited Findings
- **Eurostat 2025: 5.2% (5.21%) of Romanian enterprises with ≥10 employees used AI, the lowest in the EU.** EU 20.0%; Denmark 42.0%; Poland 8.4%; Bulgaria 8.5–8.6% — [Eurostat news 11 Dec 2025](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2); [Eurostat on X](https://x.com/EU_Eurostat/status/1999056570944983101)
- Romania rose from 3.1% (2024) to 5.2% (2025) while the EU grew 6.5 pp from 13.5%, so the gap widened. By size: small 4.1%, medium 7.8%, large 20.8% — [Business Forum](https://www.businessforum.ro/industry/20251211/romanian-companies-fall-behind-on-ai-usage-says-eurostat-2662); [RMCI ASE paper](https://www.rmci.ase.ro/no27vol1/09.pdf)
- Eurostat 2025: CRM used by **13.93%** of Romanian enterprises (EU 28.51%; small firms EU 24.69%). Any ERP/CRM/BI software: **Romania 32%** (2nd lowest; EU 53%). Social media: **48.07%** (EU 63.57%). Website: Romania is among the countries **below 60%** (with Bulgaria and Greece; EU ~79%). Eurostat notes some Romanian ICT data refer to 2023 — [Eurostat Statistics Explained](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_economy_and_society_statistics_-_enterprises); [Eurostat news 20 May 2026](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260520-1); [Eurostat social media](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Social_media_-_statistics_on_the_use_by_enterprises)
- Older: in 2016 fewer than half of Romanian firms (≥10 employees) had a website, last in the EU — [Romania Insider](https://www.romania-insider.com/romania-companies-websites)
- DESI 2025: Romania remains among the last EU states in business technology adoption, most visibly among SMEs. CRM is used by <18% of firms. Social-media presence is above the EU average but hasn't translated into practical digital services (secondary summary) — [webactiv.ro](https://webactiv.ro/digitalizarea-economiei-romaniei-raport-ce-desi-2025/)
- Basic digital intensity of SMEs: BT blog cites 44% of Romanian SMEs at the basic level; an older MKOR study says ~2 in 10 (EU 56%). These conflict — [BT blog](https://blog.bancatransilvania.ro/the-macro-zone/romania-digitala); [MKOR](https://mkor.eu/research/digitalization-report-smes/)
- LIFE IS HARD + Cult Research (400 Romanian SMEs): only 22% use basic digital tools. Another outlet attributes 22% to "advanced" solutions (Business Review, Feb 2025), so the wording is inconsistent — [Digitalio](https://digitalio.ro/2025/02/12/imm-urile-romanesti-raman-in-urma-doar-22-folosesc-solutii-digitale/)
- Cloud: 11% of Romanian firms vs EU 33%. AI among SMEs: 1% vs EU 8% (older DESI-derived figures in a commercial blog) — [Digitalio](https://digitalio.ro/2025/02/12/imm-urile-romanesti-raman-in-urma-doar-22-folosesc-solutii-digitale/)
- MKOR (1,464 SMEs): digitalisation averages 7.08% of a company's annual expenses — [Revista Cariere](https://www.revistacariere.ro/noutati/tehnologie/immurile-romanesti-se-digitalizeaza-sau-dispar-eficienta-provocari-si-solutii-reale)
- Spending anchors (vendor or agency sources): software and licences for a 10–30-employee firm run €200–700/month — [rifter.ro (vendor)](https://rifter.ro/blog/cat-costa-digitalizarea-imm-romania-2026/). Minimum ad budgets are €400–500/month for Google Ads and €300–400 for Meta, plus agency fees — [marvamarketing.ro (agency)](https://marvamarketing.ro/2026/04/16/cat-costa-sa-promovezi-o-afacere-in-online-in-romania-in-2025/). Agency packages for SMEs run €1,000–2,500/month — [awisee](https://awisee.com/ro/blog/agentii-marketing-digital-romania/)
- Older study (152 SMEs, 4+ years old): 26% do no online marketing at all. Of those who do, ~54% spend ≤100 RON/month — [revistabiz.ro](https://www.revistabiz.ro/imm-urile-trec-prin-perioade-tulburi-cu-scaderi-de-venituri-de-30-50/)
- Survey of 250 entrepreneurial firms (turnover €100k–€10M, Sep–Nov): 43% prioritise technology investment in 2025. Salaries (44%) and marketing (22%) are the top budget-increase categories — [ziuacargo.ro](https://www.ziuacargo.ro/consultanta/raportarea-financiara-la-antreprenori-editia-a-v-a-tendintele-anului-235147.html/)
- PNRR SME digitalisation: €5,000 vouchers for 100,000 firms, plus grants up to €100,000. Eligible spending includes websites and software — [StartupCafe](https://startupcafe.ro/rezultate-2025-program-digitalizare-imm-lista-5-firme-admise-finantarile-100000-30225); [EIB SME digitalisation Romania](https://www.eib.org/attachments/lucalli/20230198_digitalisation_of_smes_in_romania_ro.pdf)
- Conflicting signal: the EY Entrepreneurship Barometer 2025 says 71% of (surveyed) Romanian companies adopt AI. Its sample is likely larger or self-selected firms, which conflicts with Eurostat's 5.2% — [EY Romania](https://www.ey.com/en_ro/newsroom/2025/050/ey-entrepreneurship-barometer-study-)

### Inferences
- A self-serve SaaS motion will struggle with Bucharest micro-SMBs. A done-for-you setup with phone-number forwarding, no integrations required and SMS/WhatsApp confirmations fits better given 13.9% CRM and 32% business-software use. Integrations with local clinic software (iStoma, icMED) matter for dental and medical.
- If ~54% of SMBs that market online spend ≤100 lei/month on ads (old data), a micro-salon's willingness to pay is likely tens of euros a month. Clinics with paid receptionists are the segment with budget.
- Low AI adoption cuts both ways. Awareness and trust among owners are low, but competitors are few and "first AI in my niche" positioning is available.

### Gaps
- No 2025 Romania-specific website share (exact value) or Romanian data for micro firms (<10 employees).
- No reliable survey of SMB monthly software spend by vertical in Bucharest.

## 7. Signs of demand: vendors, ads, search interest

### Takeaway
Supply-side activity is a strong indirect demand signal. At least 15 Romanian or Romania-targeting AI-receptionist or voice-agent offers appeared in 2025–2026, many aimed at clinics and some at salons and restaurants. One early case study exists (Callio at a Timișoara dental clinic). I found no direct evidence of SMB owners publicly asking for a "robot care răspunde la telefon", and Google Trends could not be checked.

### Cited Findings
- **Callio** (bootstrapped): voice agent for dental and medical clinic reception, development since Dec 2025, pilot from Feb 2026. At Hub of Smiles (Timișoara) it handled 200+ calls and 100+ bookings. It aims to become "intelligent reception for any phone-dependent business" — [start-up.ro](https://start-up.ro/callio-agentul-vocal-ai-care-preia-telefonul-receptiei-din-clinicile-stomatologice)
- **Clinova**, "Recepționist AI pentru Clinici Medicale din România" — [clinova.ro](https://clinova.ro/); **receptie-clinica.ai** — [receptie-clinica.ai](https://receptie-clinica.ai/); **AllAI** (medical vertical) — [allai.ro](https://allai.ro/industrii/medical); **medical-ai.ro** — [medical-ai.ro](https://medical-ai.ro/)
- Multi-vertical: **aifrontdesk.ro** ("ideal for clinics, salons, restaurants") — [aifrontdesk.ro](https://aifrontdesk.ro/servicii/agent-vocal); **proiectideal.ro** ("AI virtual secretary for salons", custom demo) — [proiectideal.ro](https://proiectideal.ro/); **Voxbee** (AI receptionist books into the client's calendar + SMS) — [voxbee.ro](https://voxbee.ro/ai-agenti); **NexAi Agency** (10 simultaneous calls) — [nexaiagency.ro](https://nexaiagency.ro/agent-vocal-ai); **AgentVocal.ro** (claims "50+ firms automated", unverified) — [agentvocal.ro](https://agentvocal.ro/); **Aloro.ai** (Bucharest; voice + WhatsApp + SMS + CRM) — [aloro.ai](https://aloro.ai/en); **Dotro SmartPBX VoiceAI** — [dotro.ro](https://www.dotro.ro/asistent-vocal-ai-smartpbx/); **Zudu**, **STVN**, **robomarketing.ro** — [zudu.ai](https://zudu.ai/language/ro/asistent-vocal-ai-in-limba-romana/); [stvn.ro](https://stvn.ro/services/asistent-ai-vocal/); [robomarketing.ro](https://robomarketing.ro/servicii/agent-vocal-ai-voicebot/); **VoiceFleet** (Romanian-language blog content on dental receptionists) — [VoiceFleet](https://voicefleet.ai/blog/ai-receptionist-cabinet-stomatologic-romania-2026)
- Adjacent tools for auto service and salons: WhatsApp AI assistant for auto-shop bookings (up2date.ro), ClientDesk (free at launch), Oravo/SoftPrim online booking for salons — [up2date.ro](https://up2date.ro/solutii/programari-service-auto); [clientdesk.ro](https://clientdesk.ro/); [softprim.ro](https://softprim.ro/)
- Call-analytics demand: MedOcean targets 100 clinic clients in 2026, expanding to two new markets, with a €1M pre-seed. Clinics are paying for call-quality insight — [start-up.ro](https://start-up.ro/medocean-duce-analiza-apelurilor-medicale-pe-doua-piete-noi-si-pregateste-runda-pre-seed-in-2026-vrea-100-de-clienti-si-finantare-de-1-mil-euro/); [ZF](https://www.zf.ro/profesii/cum-arata-detectivul-ai-din-call-centerele-clinicilor-start-up-ul-23148357)
- Labour-substitution narrative in the press: AI could replace about half of Romanian call-centre employees in coming years — [Digi24](https://www.digi24.ro/digieconomic/digital/inteligenta-artificiala-transforma-industria-call-center-jumatate-dintre-angajatii-romani-ar-putea-fi-inlocuiti-in-urmatorii-ani-73331)

### Inferences
- The number of vendors (15+), most of them clinic-focused, suggests founders and agencies see demand in clinics first. It also means the **clinic segment in Bucharest is getting crowded**, while salons, auto service, vets and trades have mostly WhatsApp or online-booking tools and few voice-specific offers.
- Published prices clustered at €19–260/month plus setup suggest the market is converging on a price band, which is useful for willingness-to-pay estimates. These are list prices, not proof of paying customers. The only usage proof found is Callio's single-clinic numbers.

### Gaps
- Google Trends for "robot telefonic", "secretară virtuală", "recepționist AI", "agent vocal AI" could not be retrieved (no tool access). This needs a manual check.
- No evidence found of forum or social posts by Romanian SMB owners asking for a phone-answering robot. No Meta Ad Library or Google Ads observations.
- No vendor discloses customer counts beyond self-claims (AgentVocal "50+ firms", whapi "200+").
