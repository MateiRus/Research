# Ideea de proiect STEP, varianta software + cercetare: platformă de pașaport digital al produsului cu extragere verificabilă a datelor prin AI

**Data:** 9 octombrie 2026. **Cerința:** aceeași idee STEP, mutată pe serviciu/produs software cu componentă reală de cercetare, cu hardware-ul redus la minimul pe care îl cere apelul. Presupunerile sunt scrise explicit. Varianta anterioară (cu linie de telemetrie și a doua viață) rămâne în `Idee proiect STEP Nord Vest.md`.

---

## 0. Presupunerile (și ce se întâmplă dacă pică)

| # | Presupunere | Dacă nu e adevărată |
|---|---|---|
| P1 | Eligibilitatea solicitantului (ESO1–ESO6) e rezolvată: an fiscal cu profit din exploatare, salariat mediu ≥ 1, cofinanțare, sediu în NV. | Vehicul nou cu partener industrial sau universitar ca acționar; ILLUSTRUS aduce produsul și echipa de date. |
| P2 | Cofinanțare de **~2,5–3 mil. EUR** [ESTIMARE] și capital de lucru pentru prefinanțare și TVA. | Varianta „minimă” de mai jos (grant ~5,1 mil., cofinanțare ~2 mil.). |
| P3 | **Art. 14 acceptă ca „infrastructură de producție” o capacitate de calcul și date găzduită în UE** (servere GPU pentru antrenare/inferență, stocare, securitate, amenajare sală de servere, licențe și know-how ca active necorporale), în valoare eligibilă de ~4,5 mil. EUR pentru a atinge minimul de 3 mil. grant. Precedent: România finanțează deja AI prin STEP (HRIA, POCIDIF P4, grant 324,8 mil. lei, 2025–2029 ([HRIA](https://hria.upb.ro/en/2026/04/20/)) [VERIFICAT, dar e universitate și alt program]. | Dacă ADR NV cere linie fizică de producție, se adaugă un laborator de test pentru baterii (bancuri, ciclatoare) ca în varianta anterioară, ~1 mil. EUR. **Aceasta e presupunerea cu cel mai mare risc de reglementare; întreab-o în scris la regio@nord-vest.ro înainte de orice.** |
| P4 | Echipă nominală: director de proiect cu ≥ 5 ani în software/date sau conformitate industrială; 2 cercetători de la UTCN/UBB/INCDTIM ca membri; tu, lead pe arhitectura de date și AI. | Pierzi 6–10 puncte la 2.1; rămâi peste 65–75, nu peste 85. |
| P5 | Un cercetător științific gradul I sau un CTT (UTCN, UBB, Universitatea din Oradea CNCG-CTT, INCDTIM) semnează raportul pentru 1.2 / 5.1 / 5.2. | Fără raport, 5.1/5.2 pot fi 0 și proiectul e respins. |
| P6 | Fereastra: 961 până la 02.11.2026 doar cu consultant și partener intrați săptămâna aceasta; altfel o fereastră STEP ulterioară în PR Nord-Vest. | Produsul se construiește fără grant (secțiunea 9); cheltuielile proprii devin „maturizare” pentru criteriul 3. |
| P7 | Regulile din notele de research (din rezumate de căutare, nu din ghid): art. 25 până la 7 mil. grant, 80%/60%; art. 14 min 3 mil., intensitate NV 40% + 20 pp mică + 10 pp STEP [de verificat]; art. 28 100% până la 220.000 EUR; minimis 300.000 EUR; 31.12.2029. | Intensități mai mici → cofinanțare mai mare cu 0,5–1 mil.; structura nu se schimbă. |
| P8 | Faptele de piață de mai jos sunt corecte conform surselor citate (majoritatea furnizori și bloguri de conformitate; textele oficiale nu au fost citite pe EUR-Lex). | Dacă termenele ESPR alunecă, piața se mută cu 1–2 ani; bateriile (18.02.2027) rămân prima piață. |

---

## 1. Ideea într-un paragraf

**O platformă de pașaport digital al produsului (DPP) pentru IMM-uri producătoare și importatori din România și Europa Centrală, al cărei nucleu de cercetare este extragerea verificabilă a datelor de produs din documentele furnizorilor cu AI (cu proveniență, grad de încredere și validare umană), un strat de credențiale verificabile cu divulgare selectivă pe niveluri de acces, și, pentru primul vertical (baterii), modele de stare de sănătate antrenate pe date de exploatare.** Calendarul e dat de lege, nu de marketing: pașaportul bateriei e obligatoriu din **18.02.2027** pentru baterii industriale > 2 kWh, EV și mobilitate ușoară ([Codibly](https://codibly.com/blog/articles/eu-battery-regulation-passport-bess-operators); [Scantrust](https://www.scantrust.com/eu-battery-regulation-eu-battery-passport-requirements/)) [VERIFICAT, surse de furnizori]; primele șase standarde europene pentru DPP (EN 18216–18223: identificatori, purtători de date, API, interoperabilitate) au fost publicate de CEN-CENELEC JTC 24 în mai–iunie 2026, iar standardul de drepturi de acces și securitate (FprEN 18239) era așteptat în septembrie 2026 ([CDX](https://public.cdxsystem.com/en/web/cdx/w/first-european-standards-for-the-digital-product-passport-published); [Recycling Magazine](https://www.recycling-magazine.com/27342/digital-product-passport-european-technical-standards-now-in-place)) [VERIFICAT]; **registrul UE al pașapoartelor** e lansat, cu mediu de test și API, iar vama va putea verifica electronic existența unui pașaport înregistrat ([CMS](https://cms.law/en/int/legal-updates/key-development-in-the-eu-digital-product-passport-launch-of-the-dpp-registry); [GS1 UK](https://www.gs1uk.org/insights/news/EU-Digital-Product-Passport-Registry-goes-live)) [VERIFICAT]. Planul de lucru ESPR 2025–2030 aduce apoi oțelul și aluminiul, textilele, anvelopele, mobila și saltelele, cu acte delegate indicativ în 2026–2029 și ferestre de pregătire de ~18 luni ([Renoon](https://www.renoon.com/blog/the-timeline-of-digital-product-passport-regulation-in-eu-espr-from-product-groups-to-rollout-schedule); [PSQR](https://psqr.eu/publications-resources/espr-updates-april25/)) [VERIFICAT că sunt prioritare; datele exacte diferă între surse].

Toate acestea sunt industrii din Nord-Vest: baterii (Rombat, Bistrița), aluminiu aerospațial (Universal Alloy Corporation Europe, Maramureș), mobilă (Cluster Mobilier Transilvan, Cluj), textile și încălțăminte în lohn (Bihor, Satu Mare, Maramureș), electronică (Plexus, Celestica, Connectronics, Oradea). Niciuna nu are azi, public, un furnizor regional de DPP [absență în căutare, 9.10.2026].

## 2. De ce e STEP și de ce e cercetare

- **Sector:** tehnologii digitale (AI, spații de date, identitate și securitate digitală) cu aplicare directă în lanțurile valorice ale tehnologiilor curate (baterii, materiale). Dubla încadrare contează la 5.1 și RCO125/126.
- **Condiția (b), dependențe strategice:** datele de produs ale industriei europene stau azi în platformele furnizorilor asiatici de celule/BMS și în cloud-uri non-UE; extragerea de date cu AI se face prin API-uri americane unde documentele părăsesc UE. O platformă găzduită în UE, cu modele rulate pe infrastructură proprie, e exact „reducerea dependenței” pe care o cere art. 2(2)(b) din Reg. 2024/795.
- **Condiția (a), element inovator cu potențial economic:** piața DPP e estimată comercial la 0,15 mld. USD (2025) → 2,35 mld. USD (2035) ([MarketsandMarkets](https://www.marketsandmarkets.com/ResearchInsight/battery-passport-market.asp)) [ESTIMARE comercială]; furnizorii existenți (Kezzler, Circularise, iPoint, Protokol, Siemens, SAP) vând la întreprinderi mari cu prețuri de 15.000–100.000 EUR/an și peste, iar uneltele self-service pentru IMM-uri (de la ~9–25 EUR/lună) nu au extragere AI, nici date verificabile ([Renoon](https://renoon.com/blog/how-much-does-a-digital-product-passport-solution-cost); [DPP-Tool](https://dpp-tool.com/en/blog/dpp-cost/); [Gartner/Kezzler](https://www.gartner.com/reviews/product/kezzler-1408029466)) [VERIFICAT, surse de furnizori]. Golul e IMM-ul producător și importatorul din CEE, cu documente în română/maghiară/germană, fără echipă de conformitate.
- **De ce e cercetare, nu doar dezvoltare:** cele patru întrebări de mai jos nu au răspuns standard în literatură sau în produsele existente, pornesc de la TRL 3–4 și ajung la TRL 7–8 prin pilotare în mediu operațional la membrii clusterelor.

## 3. Pachetele de cercetare (art. 25) și produsul

| WP | Întrebarea de cercetare | De la → la | Rezultat | Linia |
|---|---|---|---|---|
| **WP1. Extragere verificabilă** | Cum extragi câmpurile unui pașaport (compoziție, conținut reciclat, amprentă de carbon, teste, due diligence) din fișe tehnice, rapoarte de încercări și declarații eterogene, în RO/HU/EN/DE, cu proveniență la nivel de propoziție, grad de încredere calibrat și validare umană minimă? | TRL 3 → 7 | Benchmark deschis de documente de produs RO/HU (spillover), model de extragere cu citare, interfață de validare | Cercetare industrială 80% |
| **WP2. Încredere și divulgare selectivă** | Cum emiți atestări verificabile (W3C Verifiable Credentials, compatibile cu portofelul european de identitate pentru organizații) pentru fiecare dată din pașaport, cu divulgare pe niveluri de acces (public / autorități / reciclatori), conform FprEN 18239? | TRL 4 → 7 | Strat de credențiale, model de autorizare, audit criptografic | Cercetare industrială 80% |
| **WP3. Interoperabilitate** | Cum implementezi EN 18216–18223 și API-ul registrului UE cu conectori spre spații de date (Asset Administration Shell, Catena-X) astfel încât un IMM să nu știe că există? Suită de teste de conformitate publicată deschis (spillover). | TRL 4 → 8 | Motor DPP conform, conectori, suită de conformitate | Dezvoltare experimentală 60% |
| **WP4. Vertical baterii: stare de sănătate** | Cum estimezi SoH și durata rămasă pentru stocare staționară din date de exploatare rare și zgomotoase (telemetrie de invertor, nu de laborator), cu învățare federată între instalatori, ca să nu centralizezi datele clienților? | TRL 3 → 6 | Modele SoH/RUL, pașaport „viu” actualizat din exploatare, bază pentru a doua viață | Cercetare industrială 80% |
| **WP5. Amprentă de mediu asistată** | Cum calculezi amprenta de carbon pe produs (reguli PEF) din lista de materiale și datele furnizorilor, cu incertitudine explicită, când jumătate din date lipsesc? | TRL 3 → 6 | Modul de calcul cu intervale de incertitudine, mapare asistată de LLM la baze LCA | Cercetare industrială 80% |
| **WP6. Modele de limbă suverane** | Pot modele mici de limbă, rulate pe infrastructura proprie din Bihor, să atingă precizia API-urilor mari pe documentele de produs RO/HU, la o zecime din cost și fără ca datele să iasă din UE? | TRL 4 → 7 | Modele fine-tuned, pipeline de evaluare, costuri per document | Dezvoltare experimentală 60% |

**Produsul care iese:** „Pașaport digital ca serviciu” pentru IMM-uri și importatori: încarci documentele furnizorilor, platforma extrage și citează, tu validezi, pașaportul e emis, înregistrat în registrul UE, servit prin QR pe niveluri de acces, actualizat din exploatare (baterii). Verticalele în ordinea legii: baterii (2027), oțel/aluminiu și textile (2027–2028), mobilă (2028–2029), electronică (cerințe orizontale de reparabilitate).

## 4. Infrastructura (art. 14) redusă la ce justifică cercetarea și producția de serviciu

| Element | De ce e necesar | Valoare eligibilă [ESTIMARE] |
|---|---|---|
| Noduri GPU pentru antrenare și inferență (WP1, WP4, WP6), găzduite în Oradea sau Cluj | modelele trebuie să ruleze pe infrastructură UE: e argumentul de dependență | 2.000.000–2.500.000 |
| Stocare, rețea, securitate (HSM pentru chei de semnare, WP2), redundanță | pașapoartele au termen de păstrare de 10 ani în registru; semnăturile cer chei protejate | 600.000–800.000 |
| Amenajare sală de servere / colocare, alimentare, răcire | | 500.000–700.000 |
| Active necorporale: licențe baze LCA, standarde, know-how achiziționat, licențe software | cumpărate la preț de piață de la terți nelegați, amortizabile, păstrate 3 ani | 500.000–700.000 |
| Laborator mic de validare pentru baterii (bancuri de test pentru adevărul de teren al WP4) și stații de lucru | | 300.000–500.000 |
| **Total art. 14** | | **~4.500.000** → grant ~3.000.000 la 65–70% |

Dacă ADR NV respinge calculul ca „infrastructură de producție” (P3), laboratorul de baterii crește la ~1 mil. și proiectul devine varianta anterioară.

## 5. Schiță de buget (varianta software) [ESTIMARE]

| Linie | Eligibil | Intensitate (P7) | Grant | Cofinanțare |
|---|---|---|---|---|
| Art. 25 cercetare industrială (WP1, WP2, WP4, WP5: personal 6–8 cercetători/dezvoltatori × 3 ani, cercetare contractată UTCN/UBB/INCDTIM, date, calcul) | 2.400.000 | 80% | 1.920.000 | 480.000 |
| Art. 25 dezvoltare experimentală (WP3, WP6, piloți la membrii clusterelor) | 1.500.000 | 60% | 900.000 | 600.000 |
| Art. 14 infrastructură de calcul, date, securitate, active necorporale, laborator | 4.500.000 | 65–70% | 3.000.000 | 1.350.000–1.575.000 |
| Art. 28 inovare IMM: raport CTT, studiu de piață, consultanță inovare, protecție IP (marcă, eventual brevet pe WP2/WP4) | 220.000 | 100% | 220.000 | 0 |
| Minimis: consultanță scriere/implementare, publicitate (15.000 lei fără TVA) | 300.000 | 100% | 300.000 | 0 |
| **Total** | **~8.900.000** | | **~6.300.000** | **~2.400.000–2.700.000** |

Grant între 5 și 7 mil. → criteriul 1.1 cere **> 4 locuri de muncă**: planifică **7 ENI** (3 cercetători/ingineri ML, 2 dezvoltatori platformă, 1 specialist conformitate/standarde, 1 vânzări). Varianta „minimă”: art. 25 la 2,0 mil. grant, art. 14 la 3,0 mil., total 5,5 mil., cofinanțare ~2 mil.

## 6. Cum ar puncta pe grila din transcriere [ESTIMARE; grila modificată prin Corrigendum 2]

| Criteriu | Max | Estimare | De ce |
|---|---|---|---|
| 1.1 locuri de muncă | 6 | 6 | 7 ENI |
| 1.2 inovație | 5 | 3–4 | b (produs), c (proces: conformitate automatizată), d (emergentă: credențiale verificabile, învățare federată); e (de vârf) posibil pe WP6 |
| 2.1 echipă | 12 | 6–10 | director 5 ani (4), 2 cercetători universitari (2+2), management operațional de la partener (2); experiența UE (2) doar cu un membru care a implementat 2 proiecte |
| 2.2 solvabilitate | 4 | 2–4 | bilanțul vehiculului |
| 2.3 cash-flow | 4 | 4 | abonamente recurente din 2027 |
| 3 maturizare ≥ 10% | 8 | **0–4** | 0 la o depunere acum; 4 (≥ 1%) dacă până la următoarea fereastră cheltui 90.000+ EUR proprii pe produsul fără grant și pe un voucher UEFISCDI (secțiunea 9) |
| 4.3 scalare | 3 | 3 | regulament identic în toată UE; scrisori de la un cluster maghiar/polonez și de la un distribuitor |
| 4.4 spillover | ? | bun | benchmark deschis, suită de conformitate deschisă, contribuție la comitetul tehnic ASRO |
| Secțiunea II | 11 | 11 | obligatorii, cu raport CTT și buget corelat |
| **Total orientativ** | 100 | **~72–82** | peste 65/75, sub 85/90; autoevaluează conservator (regula de 5 puncte) |

## 7. Clienți, canale, scrisori de intenție

| Cumpărător | Ce cumpără | De ce acum | Rol în dosar |
|---|---|---|---|
| **Rombat** (Bistrița) | DPP pentru baterii industriale > 2 kWh, SoH pentru flote | obligație 18.02.2027 | scrisoare de intenție; pilot WP4 |
| **Importatori și instalatori de baterii rezidențiale** (NV, național) | pașaport per baterie + telemetrie de garanție | Casa Verde Baterii: ~27.000 de baterii ≥ 10 kWh, 400 mil. lei, lansare octombrie 2026 ([Economedia](https://economedia.ro/prosumatorii-cer-sa-fie-consultati-inainte-de-lansarea-programului-casa-verde-baterii-2026.html)) [VERIFICAT] | 3–5 scrisori; primul venit |
| **Cluster Mobilier Transilvan** (Cluj) și membrii lui | pregătire DPP mobilă (acte delegate indicativ 2028) | ferestre de pregătire ~18 luni | scrisoare de la cluster; piloți WP1/WP5 |
| **Producători textile/încălțăminte în lohn** (Bihor, Satu Mare) | DPP textile (acte delegate indicativ 2027/28) | clienții lor din Vest le vor cere datele | 2–3 scrisori prin CCI Bihor |
| **Universal Alloy Corporation Europe** (Maramureș) | DPP aluminiu/oțel (primele acte delegate) | lanț aerospațial cu cerințe de trasabilitate | scrisoare pentru 4.3 (grup internațional) |
| **EMS Oradea** (Plexus, Celestica) | cerințe orizontale electronică (reparabilitate, reciclabilitate) | cerere din partea clienților OEM | piloți WP3 (conectori AAS/Catena-X) |
| **Extern:** cluster din Ungaria/Polonia, distribuitor CEE | aceeași lege, aceleași limbi lipsă la furnizorii mari | | 4.3 |

Canal fără e-mail rece: clusterele (Cluj IT Cluster, Transilvania IT Cluster/TEDIHT 2.0, Cluster Mobilier Transilvan), CCI Bihor, instalatorii validați AFM (listă publică, telefon), GS1 România ca furnizor de identificatori.

## 8. Ce poate ucide ideea

1. **P3 (art. 14 pe calcul)**: dacă ADR NV nu acceptă infrastructura de calcul ca producție, proiectul redevine unul cu laborator fizic. Întreabă în scris înainte de a scrie o pagină.
2. **Furnizorii consacrați coboară spre IMM-uri** (Kezzler, Circularise au deja modele pe volum); răspunsul tău e limba, documentele reale ale furnizorilor din CEE și prețul per SKU, nu platforma enterprise.
3. **Actele delegate ESPR alunecă** (sursele deja se contrazic cu un an); bateriile rămân singura piață cu dată fermă în 2027; restul e 2028–2030, adică exact perioada de implementare, ceea ce e un argument în plus la 5.3, dar un risc de venit.
4. **Cercetarea fără universitate nu e credibilă**: WP1/WP2/WP4 cer un grup de NLP sau de sisteme energetice ca partener contractat (UTCN, UBB, INCDTIM). Fără ei, raportul CTT nu se semnează.
5. **Răspunderea pentru conținutul pașaportului** rămâne la operatorul economic; platforma trebuie să fie „unealtă cu validare umană”, nu „garant al datelor”, altfel asigurarea de răspundere devine costul principal.
6. **Cofinanțarea** de 2–3 mil. nu vine dintr-un SRL cu un angajat; vine de la un partener industrial sau un investitor; dacă e majoritar, proiectul e al lui și tu ești CTO cu părți sociale.

## 9. Versiunea fără grant, care începe acum și construiește dosarul

1. **Pașaportul bateriei ca serviciu** (Q4 2026 – Q1 2027): extragere din fișa tehnică cu LLM + validare umană, QR, pagină publică per baterie, înregistrare în registrul UE (mediul de test e disponibil), 15–25 EUR/baterie/an [ESTIMARE, fără ancoră în RO], vândut instalatorilor AFM și importatorilor. E portal web (CAEN 6310), deci alimentează obligația DR-36.
2. **Voucher de inovare UEFISCDI** (max 50.000 lei, depunere continuă din 08.01.2026, buget 2026 mic, stare de verificat) cu UTCN sau UBB pe WP1 (benchmark de extragere RO/HU): creează relația cu cercetătorul gradul I și prima dovadă de maturizare pentru criteriul 3.
3. **TEDIHT 2.0 / DIH4Society**: servicii gratuite de testare și acces la infrastructură de calcul pentru prototipul WP6.
4. **„Audit de pregătire DPP”** pentru membrii Clusterului Mobilier Transilvan și pentru textile (serviciu de consultanță, 1–2 zile): aduce scrisorile de intenție și datele reale pentru WP1/WP5.

Fiecare din cele patru produce o piesă de dosar: client, partener de cercetare, infrastructură, scrisori. La următoarea fereastră, criteriul 3 nu mai e 0.

## 10. Alternativele software cântărite

| Idee | De ce e mai jos |
|---|---|
| **Model de limbă suveran RO/HU pentru industrie**, ca produs de sine stătător | e cercetare bună, dar fără obligație legală care să creeze cumpărători; intră aici ca WP6, nu ca produs |
| **Geamăn digital / mentenanță predictivă pentru EMS** | concurează cu Siemens/PTC/Rockwell; fabricile cumpără la nivel de grup; fără dată de piață |
| **Software medical predictiv (MDSW)** din notele de sănătate | MDR: 9–18 luni și 32–110 k EUR înainte de venit; încadrare STEP incertă; acces la date clinice limitat |
| **Analitică SoH pentru baterii, singură** | piață reală dar îngustă; intră aici ca WP4 și prim vertical |

DPP câștigă pentru că **legea creează cumpărătorii pe un calendar scris, standardele tocmai au apărut, registrul UE e deschis, industriile vizate sunt în Nord-Vest, iar nucleul tehnic (extragere din documente, date, API, automatizări) e exact ce știi deja să faci.**

## 11. Următoarele 10 zile

1. E-mail la regio@nord-vest.ro: „infrastructura de calcul și activele necorporale pentru o platformă de date sunt acceptate ca investiție inițială pe art. 14 în apelul 961 / într-o fereastră viitoare?” (30 min; răspunsul decide P3).
2. Citește EN 18216–18223 (rezumatele publice) și documentația API a registrului UE; fă contul în mediul de test (3 h).
3. Demo în APEX: pașaport de baterie generat dintr-o fișă tehnică reală, cu citarea sursei pentru fiecare câmp, QR și pagină publică (10 h). E demo-ul pentru toate discuțiile de mai jos.
4. Trei telefoane: Rombat (conformitate), un importator de baterii din Cluj/Oradea, un instalator AFM din Bihor (3 h).
5. O vizită la UTCN sau UBB (grup NLP / sisteme energetice) și la Universitatea din Oradea CNCG-CTT: cine semnează raportul și cine ar fi partener pe WP1/WP4 (3 h).
6. O discuție cu Clusterul Mobilier Transilvan și cu CCI Bihor despre un „audit de pregătire DPP” pentru membri (1 h).

Dacă răspunsul de la ADR NV e „da” la P3 și două din cele trei telefoane se termină cu „cât costă?”, ideea trece de la ipoteză la dosar. Dacă P3 e „nu”, revii la varianta cu laborator din documentul anterior, cu același nucleu software.
