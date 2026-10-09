# Vinde închiderea buclei înainte de predicție

## 1. Rezumat executiv: valoarea rară e urmărirea, nu predicția

**Recomandarea: din Bihor, cu ~25.000 € și 10–12 ore pe săptămână, construiește întâi un „birou de continuitate” pentru cabinetele independente de medicina muncii, nu un model predictiv.** E un produs administrativ, deci în afara MDR. Face patru lucruri: ține scadențele examenelor periodice obligatorii, face în locul asistentei munca de reamintire către angajatori, ține registrul recomandărilor cu termen pus de medic și produce raportul de renegociere pentru fiecare angajator. Motivul e o regulă care se repetă în dovezile din ultimii zece ani: beneficiul în prevenție vine din acțiunea care urmează semnalului, nu din precizia semnalului. După un AI-ECG pozitiv, doar **49,6%** dintre pacienți au făcut ecografia de confirmare ([TCTMD](https://www.tctmd.com/news/ai-ecg-allows-early-diagnosis-low-ef)). Când testul s-a făcut în aceeași vizită, finalizarea a urcat de la **22% la 100%** ([UW Ophthalmology](https://www.ophth.wisc.edu/blog/2024/01/11/autonomous-artificial-intelligence-increases-screening-and-follow-up-for-diabetic-retinopathy-in-youth-the-access-randomized-control-trial)). Stratificarea riscului fără o intervenție atașată a **crescut** internările de urgență ([PMC6820297](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820297/)). Medicina muncii e singurul contact preventiv obligatoriu, recurent și plătit de angajator pentru toți cei **5,76 milioane** de salariați ([Profit.ro/INS](https://profit.ro/taxe-si-consultanta/romania-avea-anul-trecut-5-76-milioane-salariati-botosani-si-teleorman-cele-mai-mici-salarii-la-polul-opus-bucuresti-22784743)). Lipsa examenului se amendează cu **4.000–8.000 lei pe abatere**; suma vine din texte vechi și trebuie reverificată pentru 2026 ([Inspecția Muncii](https://www.inspectiamuncii.ro/documents/547298/82715837/comunicat-examen+medical.doc/eeaa2a89-0633-4c02-b070-c7901ad81a43)). MedLife vinde deja angajatorilor exact stratul de coordonare pe care cabinetele independente nu-l au ([MedLife Self-Service](https://www.medlife.ro/self-service)). Economia e modestă și trebuie spusă direct. În scenariul de bază corectat, **1.000 € MRR vine în luna ~15–19** (luna ~19 fără niciun ajutor, luna ~15 cu un colaborator part-time din luna 13). Fără ajutor, plafonul e **~1.600 € MRR**. **3.000 € MRR apare abia în luna ~34**, și numai cu un ajutor part-time și un modul de prevenție. În scenariul pesimist, 1.000 € MRR vine abia în luna 32. Capitalul nu e problema: vârful de numerar e ~4–4,7k € din 25k €. Constrângerile sunt timpul fondatorului și conversia reală. Tot ce susține azi cererea e simulat, deci primele 21–60 de zile trebuie fie să omoare ideea, fie să o confirme. Te oprești dacă două programe de medicina muncii au deja portal pentru angajator sau dacă după 15 conversații calificate nu ai 3 pre-vânzări plătite.

**Ce arată viitorul.** Până în 2030, „normal” devine AI-ul care intră în fluxuri deja finanțate, nu produsele de predicție de sine stătătoare. Exemplele sunt citirea asistată a mamografiilor în programele organizate, screeningul autonom al retinopatiei acolo unde e rambursat, scribii ambientali și schimbul de rezumate de pacient și rețete prin EHDS din 26 martie 2029 ([EUR-Lex 2025/327](https://eur-lex.europa.eu/eli/reg/2025/327/oj)). Rămân speculative chiar și pentru 2040: gemenii digitali de corp întreg, prognozele individuale pe 20 de ani care să conducă prevenția și scanările de corp întreg cu beneficiu dovedit. Modelele fundaționale pe dosare (Delphi-2M, Foresight) au doar acuratețe retrospectivă ([UK Biobank](https://www.ukbiobank.ac.uk/publications/learning-the-natural-history-of-human-disease-with-generative-transformers/)). Primul RCT de test multi-cancer din sânge (NHS-Galleri) și-a ratat criteriul principal ([BioSpace/GRAIL](https://www.biospace.com/press-releases/grail-reports-full-results-from-nhs-galleri-trial-demonstrating-substantial-reduction-in-stage-iv-cancer-diagnoses-at-2026-asco-annual-meeting)).

**Ce arată România.**
- **Sistemul e digital întârziat, dar recuperează.** Doar ~10% dintre români și-au făcut programări online sau și-au accesat dosarul în 2024 ([OECD](https://www.oecd.org/en/publications/oecd-reviews-of-health-systems-romania-2025_f52e4a98-en/full-report/access-and-quality-of-care-in-romania-s-healthcare-system_31f62789.html)). Competențele digitale de bază sunt cele mai slabe din UE (31,8%) ([Romania Insider](https://www.romania-insider.com/eurostat-basic-digital-skills-ro-ranks-last-apr-2026)).
- **Portalul național nu e o sursă de date pentru terți.** Statul a lansat e-SănătateaMea pe 1 septembrie 2026, dar nu are un API public pentru aplicații terțe ([Tele7abc](https://tele7abc.ro/e-sanatatea-mea-portalul-cnas-pentru-dosarul-medical-digital-lansat-pe-1-septembrie-2026/)).
- **Banii de prevenție stau la angajatori și în buzunarul oamenilor, nu la CNAS.** Nu există o cale de rambursare pentru produse digitale.
- **Clienții accesibili sunt independenții.** Marile rețele (MedLife, Regina Maria, Medicover) își construiesc software-ul în casă. Clinicile și cabinetele independente din Oradea sunt numărabile și se poate ajunge fizic la ele.

**Ce arată concurența globală.** Afacerile B2B care au crescut din puțin au pornit dintr-un singur mesaj frecvent, lipit de sistemul de evidență existent, și s-au extins pe același flux. Accurx a pornit de la SMS-ul trimis de medicul de familie din desktop ([Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b)). Lifen a pornit de la trimiterea documentelor și a ajuns profitabilă la peste 20 mil. € ARR ([FrenchWeb](https://www.frenchweb.fr/lifen-la-startup-qui-digitalise-lhopital-sans-jamais-apparaitre-a-lecran/454591)). Kaiku a fost cumpărată de Elekta la doar 1,3 mil. € venit ([ArcticStartup](https://arcticstartup.com/kaiku-health-exits-elekta/?amp=1)). Eșecurile au alt tipar: livrare fizică intensivă în capital (Forward), rambursare care n-a venit (Pear), volume mici direct la consumator în Europa (Aware).

**Drumul spre predictiv** e în etape, fiecare cu o poartă de trecere:
- **Prevenția la examen:** teste făcute în aceeași vizită, cu constatările marcate de medic și un om care sună pacientul.
- **Prognoza de capacitate pentru echipa mobilă:** pe sediu de angajator, fără profilarea persoanelor.
- **„Pe cine suni primul”:** doar cu bază legală și doar dacă bate „reminder pentru toți” cu grup de control.
- **După 2029:** produsul devine locul în care modelele certificate CE ale altora produc acțiuni, iar datele pot fi folosite secundar prin EHDS.

**De evitat ca prim produs:** modelele proprii de risc, calculatoarele de scor (SCORE2/QRISK) puse în fluxul medicului, chatbot-urile de triaj, RPM-ul cu alerte, aplicațiile și PHR-urile pentru consumator, abonamentele de analize direct la consumator și scribul AI general. Cele care fac afirmații clinice cad în MDR clasa IIa (~32–110k €, 9–18 luni). Celelalte cer un plătitor care nu există.

| Decizia | Ce anume | De ce | Ce trebuie dovedit întâi |
|---|---|---|---|
| **Construiește** | Birou de continuitate pentru cabinetele independente de medicina muncii (39 / 79 / 149 €/lună, SMS la cost) | Contact obligatoriu, recurent, plătit de angajator; cumpărători numărabili; administrativ | 0–1 vendori de software MM cu portal pentru angajator (ziua 21); ≥3 pre-vânzări plătite (ziua 60) |
| **A doua ușă, înghețată** | „Controale pierdute” la clinicile independente de boli cronice | Cea mai valoroasă strategic; dovezi internaționale solide pentru gol | ≥10 cabinete MM plătitoare; 2 audituri cu ≥30 de controale depășite fiecare; opinie MDR scrisă |
| **Opțiune pentru 2027–2029** | Componente EHDS (fațadă FHIR, rezumat IPS, jurnal de acces) pentru vendorii locali | Termene legale; avantaj pe Oracle/PL-SQL | Reguli românești de aplicare; un vendor care plătește |
| **Evită** | Model propriu, scoruri de risc individuale, RPM cu alerte, aplicații B2C, scrib AI general | MDR IIa+ sau lipsa plătitorului | — |

### Cum să citești raportul

**Etichetele de dovezi** apar în paranteze drepte după afirmațiile-cheie:
- **[Stabilit]**: mai multe surse independente, RCT-uri sau meta-analize, ori text de lege.
- **[Emergent puternic]**: un RCT bun, date prospective consistente, sau o sursă credibilă dar unică ori raportată de companie.
- **[Plauzibil]**: inferență cu sprijin parțial, încă nedovedită.
- **[Speculativ]**: ipoteză.

**Calitatea datelor despre companii** se marchează așa:
- **(V)**: dezvăluit într-un raport financiar, de un regulator, într-un contract public sau într-un comunicat cu cifre auditate, așa cum l-a preluat presa;
- **(C)**: afirmația companiei;
- **(E)**: estimarea unui agregator (Latka, Sacra, Dealroom și alții).

**Limita surselor, spusă o dată și valabilă peste tot.** În sesiunile de cercetare, proxy-ul a blocat descărcarea paginilor pentru aproape toate domeniile încercate: EUR-Lex, PMC, site-urile companiilor, presa. **Aproape toate faptele vin din rezumatele motorului de căutare, nu din pagini citite integral.** Linkurile duc la pagina din care provine rezumatul și trebuie verificate înainte de citare. Unele afirmații vin din cunoștințele de fond ale cercetătorilor, nu din surse redeschise în sesiune. Notele le marchează **BK** (background knowledge) sau **PK** (prior knowledge), iar eu le marchez la fel.

**Ce e analiză, nu dovadă.** Analiza laterală, scorarea ponderată, board-ul de trei membri, panelurile de câte 20 de cumpărători și cele trei runde de review „investitor” **au fost simulate cu modele de limbaj**: niciun client real nu a fost întrebat. Le folosesc ca să aleg ce trebuie testat și ca să arăt cum s-a întărit planul, niciodată ca dovadă a cererii. Ratele de cumpărare din paneluri sunt o limită superioară. Fișierele sunt în `founder-sanatate/` (scoring, board, panels, pricing, cfo, plan, bulletproof) și în `analiza_laterala.md` și `analiza_founder.md`. Unde rundele „bulletproof” au corectat analiza founder (churn și retururi care scad cifrele, produsul redefinit din „portal” în „birou de continuitate”, drumul predictiv cu porți), raportul folosește versiunea corectată.

**Previziunile nu sunt dovezi.** Tabelele cu orizonturi de timp (2030, 2035, 2040) sunt judecata cercetătorilor, ancorată în dovezi și termene legale; nu provin din previziuni publicate. Calculele mele sunt marcate „calculul meu”.

## 2. Viitorul sănătății 2026–2040: acțiunea bate acuratețea

### Trei niveluri de dovadă care nu trebuie confundate

Orice afirmație despre sănătatea predictivă trebuie pusă pe una din trei trepte:
- **acuratețea:** cât de bine prezice modelul (AUC, sensibilitate);
- **schimbarea de proces:** mai multe teste făcute, mai multe diagnostice puse;
- **rezultatul pentru pacient:** mai puține cancere în stadiu avansat, mai puține internări sau decese.

Marketingul sare de obicei de pe prima treaptă direct pe a treia. Dovezile din octombrie 2026 arată că saltul reușește rar.

**Puține tehnologii au RCT-uri cu efect apropiat de rezultat:**
- **Mamografia citită cu sprijinul AI.** Studiul MASAI a randomizat peste 100.000 de femei. A raportat **12% mai puține cancere de interval** și **27% mai puține cancere de interval agresive**, cu sensibilitate de 80,5% față de 73,8% ([Lund University](https://www.lunduniversity.lu.se/article/ai-support-breast-cancer-screening-fewer-missed-cancer-cases); [ScreenPoint](https://screenpoint-medical.com/insights/final-results-masai-trial)) [Emergent puternic]. Cifrele vin mai ales prin vânzător și presă, iar mortalitatea nu a fost măsurată.
- **Programul de prevenție a diabetului prin stil de viață:** −58% incidență în RCT-ul original (PK; [Knowler, NEJM 2002](https://doi.org/10.1056/NEJMoa012512)) [Stabilit].
- **Screeningul autonom al retinopatiei diabetice.** Efectul e de închidere a golului de îngrijire, nu de acuratețe: examen finalizat la 100% față de 22%, urmare după un rezultat anormal la 64% față de 22% ([UW Ophthalmology](https://www.ophth.wisc.edu/blog/2024/01/11/autonomous-artificial-intelligence-increases-screening-and-follow-up-for-diabetic-retinopathy-in-youth-the-access-randomized-control-trial)) [Emergent puternic].
- **Un geamăn digital folosit într-o singură procedură:** ablația fibrilației atriale. Pacienții fără aritmie la 18 luni au fost 77,9% față de 59,5% ([ESC](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Digital-twin-technology-helps-reduce-the-recurrence-of-atrial-arrhythmias-after-catheter-ablation-for-persistent-atrial-fibrillation)) [Emergent puternic, date de congres].

**Alte RCT-uri arată doar schimbare de proces:**
- **AI-ECG (EAGLE):** 2,1% față de 1,6% diagnostice noi de fracție de ejecție scăzută, adică ~5 la 1.000 de pacienți scanați ([TCTMD](https://www.tctmd.com/news/ai-ecg-allows-early-diagnosis-low-ef)).
- **Programul de prevenție a diabetului livrat de AI:** non-inferior pe criterii intermediare, 31,7% față de 31,9% ([Patient Care](https://www.patientcareonline.com/view/ai-powered-diabetes-prevention-program-intervention-matches-human-coaching-daily-dose)).
- **Scribii ambientali:** au economisit secunde pe notă ([UCLA Health](https://www.uclahealth.org/news/release/ucla-study-finds-ai-scribes-may-reduce-documentation-time)).

**Un al treilea grup de RCT-uri a ieșit negativ pe criteriul principal:**
- **NHS-Galleri** (142.250 de participanți): de patru ori mai multe cancere găsite prin screening, dar fără reducerea stadiilor III–IV combinate ([BioSpace/GRAIL](https://www.biospace.com/press-releases/grail-reports-full-results-from-nhs-galleri-trial-demonstrating-substantial-reduction-in-stage-iv-cancer-diagnoses-at-2026-asco-annual-meeting)).
- **Controalele generale de sănătate:** risc relativ de mortalitate 1,00 în 17 studii ([AAFP/Cochrane](https://www.aafp.org/afp/2019/1201/p676)) [Stabilit].
- **PRISMATIC:** unealta de stratificare a riscului introdusă în 32 de cabinete din Țara Galilor a crescut internările de urgență cu ~1% și vizitele ambulatorii cu ~5% ([PMC6820297](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820297/)) [Stabilit în acel context].

**Restul are doar acuratețe retrospectivă:** modelele fundaționale pe dosare, scorurile poligenice, AI-ul pentru noduli pulmonari, panourile de biomarkeri pentru consumatori, RMN-ul de corp întreg.

Unde beneficiul apare, el are trei condiții:
- o acțiune specifică și eficientă;
- un flux cu oameni care acționează;
- finalizarea urmăririi.

Mortalitatea a fost asociată cu alertele de sepsis TREWS doar când alerta era confirmată de un clinician în 3 ore. E o asociere observațională, nu un RCT ([Scientific American](https://www.scientificamerican.com/article/algorithm-that-detects-sepsis-cut-deaths-by-nearly-20-percent/)). Modelul de sepsis Epic a avut AUC 0,63 la validarea externă, față de 0,76–0,83 în documentația internă, și valoare predictivă pozitivă de 12% ([JAMA Intern Med](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781313)). Când s-a schimbat mixul de cazuri în pandemie, proporția pacienților cu alertă a urcat de la 9% la 21% pe zi ([Healthcare IT News](https://www.healthcareitnews.com/news/epic-generated-sepsis-alerts-increased-during-covid-19-study-shows)).

Notele sintetizează **șase puncte în care se pierde beneficiul între model și pacient**:
1. performanța locală e sub cea promisă;
2. modelul derapează după schimbări de populație sau de IT;
3. alertele sunt prea multe;
4. nimeni nu deține alerta;
5. pozitivul nu e urmărit;
6. apar cascade de investigații.

**Cinci dintre ele sunt probleme de software și operațiuni, nu de construcție a modelului.** Aceasta e inferența cea mai importantă pentru un fondator care știe SQL, APEX și n8n, dar nu are un model medical propriu [Plauzibil].

### Ce e dovedit, ce e doar acuratețe și ce e marketing, pe 14 domenii

| Domeniu | Tehnologia | Beneficiu dovedit pe rezultate | Doar acuratețe sau proces | Afirmații fără dovadă | Barierele principale |
|---|---|---|---|---|---|
| Detecție timpurie cu AI și stratificarea riscului | rețele neuronale pe imagini și ECG; modele de deteriorare din dosar | MASAI: −12% cancere de interval [Emergent puternic]; screening autonom al retinopatiei: închiderea golului [Emergent puternic]; TREWS: asociere cu mortalitatea doar cu răspuns confirmat [Emergent puternic, observațional] | EAGLE: mai multe diagnostice, efect pe termen lung necunoscut; noduli pulmonari: doar retrospectiv ([RSNA](https://www.rsna.org/news/2025/september/ai-estimates-lung-cancer-risk)); dermatologie: NICE recomandă DERM doar condiționat, pe 3 ani ([PharmaTimes](https://pharmatimes.com/news/nice-recommends-first-ai-medical-device-for-skin-cancer-diagnosis-in-the-nhs/)) | acuratețea declarată de vânzător scade la validarea externă (Epic) | validare locală, derapaj, oboseala de alerte, MDR IIa–III, echipă de răspuns |
| Monitorizare continuă și pasivă | PPG, ECG cu o derivație, accelerometrie, CGM | anticoagularea fibrilației atriale detectate de dispozitiv: AVC ischemic RR 0,68, dar sângerări majore RR 1,62 ([meta-analiză McIntyre](https://openaccess.sgul.ac.uk/id/eprint/115979/1/mcintyre-et-al-2023-direct-oral-anticoagulants-for-stroke-prevention-in-patients-with-device-detected-atrial.pdf)) [Stabilit] | notificările de fibrilație: VPP 0,84–0,98 (BK; [Apple Heart Study](https://doi.org/10.1056/NEJMoa1901183)); EQUAL: 9,6% față de 2,3% fibrilație nouă ([JACC](https://www.jacc.org/doi/10.1016/j.jacc.2025.11.032)); LOOP: fără reducere semnificativă a AVC (BK) | CGM fără prescripție la nediabetici: nicio dovadă de beneficiu ([Clinical Correlations](https://www.clinicalcorrelations.org/2025/05/22/could-adults-without-diabetes-benefit-from-continuous-glucose-monitoring/)) | VPP mic la populații tinere; nimeni nu e plătit să revizuiască datele; răspunderea pentru ce s-a văzut și nu s-a făcut |
| Wearables de consum față de senzori clinici | ceas sau inel (PPG) față de patch ECG, implant, manșetă validată | doar senzorii clinici cu flux: senzorul de presiune pulmonară implantat reduce internările pentru insuficiență cardiacă cu ~30%, fără efect pe mortalitate ([ACC](https://www.acc.org/latest-in-cardiology/journal-scans/2023/10/10/16/38/efficacy-of-pulmonary-artery)) [Stabilit] | notificarea Apple de hipertensiune: sensibilitate 41,2%, specificitate 92,3% ([AAFP](https://www.aafp.org/pubs/afp/afp-community-blog/entry/smartwatch-screening-for-hypertension.html)) | „scoruri” de recuperare și stres nevalidate; tensiunea fără manșetă „validată” după protocoale făcute pentru manșete | standarde de validare în formare (ISO 81060-3); FDA a relaxat regulile pentru wellness în ian. 2026, doar în SUA ([Covington](https://www.cov.com/news-and-insights/insights/2026/01/fda-issues-revised-guidance-on-general-wellness-products)) |
| Predicție din dosarul longitudinal | transformere pe coduri ICD-10 și pe text; scoruri clasice | niciunul | Delphi-2M: peste 1.000 de boli, „comparabil cu modelele pentru o singură boală”, cu biasuri UK Biobank ([Scientific American](https://www.scientificamerican.com/article/new-ai-tool-predicts-which-of-1-000-diseases-someone-may-develop-in-20-years/)); scor poligenic: +0,02 la statistica C ([JAMA 2020](https://jamanetwork.com/journals/jama/article-abstract/2761088)) | „prezicem bolile cu 20 de ani înainte” | acces la date, calitatea codării, MDR (definiția include explicit „predicția”), Legea 190/2018 art. 3 |
| Biomarkeri din sânge și testare preventivă | test multi-cancer din sânge, panouri largi, RMN de corp întreg; screening organizat | screeningul organizat de sân, col uterin și colorectal din ghiduri [Stabilit] ([recomandarea UE 2022](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_22_7548/IP_22_7548_EN.pdf)) | NHS-Galleri a ratat criteriul principal; stadiul IV, rata de incidență 0,86 (nominal); PATHFINDER 2: VPP 61,6%, studiu cu un singur braț ([GRAIL](https://grail.com/press-releases/grail-pathfinder-2-results-show-galleri-multi-cancer-early-detection-blood-test-increased-cancer-detection-more-than-seven-fold-when-added-to-uspstf-a-and-b-recommended-screenings/)) | RMN de corp întreg: 94% cu o anomalie, până la 30% trimiși la investigații, 1,1–1,6% cu cancer confirmat, fără RCT ([CFPC](https://cfpclearn.ca/wp-content/uploads/2026/03/TFP-410-English.pdf)); panouri de tip Function fără studiu de rezultat | supra-diagnostic, cascade, lipsa recomandării în ghiduri |
| Recomandări personalizate | coaching cu AI, nutriție personalizată | prevenția diabetului prin stil de viață (PK) [Stabilit] | prevenția diabetului livrată de AI: non-inferioară pe criterii intermediare [Emergent puternic]; ZOE: doar trigliceridele, studiu făcut de companie ([FoodNavigator](https://www.foodnavigator.com/Article/2024/05/10/Zoe-hails-personalized-nutrition-trial-success-results-come-under-scrutiny/)) | „vârsta biologică”, dietele „personalizate” cu efect clinic | efectul scade în timp; implicarea pacienților |
| Fluxuri asistate de AI și suport decizional | scribi, copiloți LLM, suport decizional clasic | suport decizional clasic: îmbunătățire mediană de **0,3%** în 30 de studii cu criterii clinice ([BMJ 2020](https://www.bmj.com/content/370/bmj.m3216)) [Stabilit: efect mic] | scribi: −0,36 h/zi de documentare ([UW Health](https://uwclinicaltrials.org/2025/12/12/studies-find-ai-technology-for-clinical-documentation-aids-efficiency-and-reduces-burnout/)); GPT-4 nu a îmbunătățit raționamentul medicilor (76% față de 74%) ([Medical Dialogues](https://medicaldialogues.in/amp/mdtv/medicine/videos/can-gpt-4-improve-diagnosis-study-provides-insights-137499)); doar 19 RCT-uri din 4.609 studii despre LLM-uri ([cancer.fr](https://www.cancer.fr/professionnels-de-sante/veille/nota-bene-cancer/bulletin-n-677-du-12-mars-2026/llm-assisted-systematic-review-of-large-language-models-in-clinical-medicine)) | „AI-ul diagnostichează mai bine decât medicul” | MDR IIa pentru codare și suport decizional (Tandem); răspundere; dovezi rare |
| Monitorizare la distanță și boli cronice | transmitere zilnică, centru de telemedicină | TIM-HF2, cu centru 24/7: mortalitate HR ~0,70 (BK; [Lancet 2018](https://doi.org/10.1016/S0140-6736(18)31880-4)); auto-monitorizarea tensiunii cu ajustarea tratamentului: −3,4 până la −4,7 mmHg (BK) [Stabilit] | Tele-HF și BEAT-HF, fără răspuns clinic puternic: fără efect (BK); monitorizarea tensiunii fără ajustarea medicației: efect marginal ([PHTI](https://phti.org/wp-content/uploads/sites/3/2024/10/PHTI-Digital-Hypertension-Mgmt-Assessment-Report.pdf)) | SUA: 43% dintre pacienții Medicare cu RPM n-au primit toate cele trei componente ale serviciului ([Healthcare Dive](https://www.healthcaredive.com/news/remote-patient-monitoring-medicare-oversight-oig/728039/)) | personal, rambursare (EBM în Germania, CPT în SUA), oboseala de alerte, MDR IIa/IIb |
| Analitica de sănătate a populației | liste de risc, tablouri | niciunul fără intervenție finanțată | PRISMATIC: a crescut utilizarea; Camden: fără efect asupra reinternărilor (PK) | „tabloul reduce internările” | lipsa capacității de intervenție |
| Îmbătrânire și îngrijire la domiciliu | detecția căderilor, senzori ambientali, teleasistență | niciunul solid; telecare în Whole System Demonstrator: fără reducerea serviciilor (BK) | 98,5% dintre studiile de detecție a căderilor folosesc căderi simulate ([Catania](https://www.iris.unict.it/handle/20.500.11769/705569)) | „prevenim căderile” | alarme false, intimitate, bugete mici |
| Biomarkeri digitali | mers, voce, tastare, HRV | calificări de reglementare doar pentru studii clinice: SV95C la EMA, AFib History la FDA (BK; [FDA MDDT](https://www.fda.gov/medical-devices/medical-device-development-tools-mddt)) | asocieri pentru voce, tastare, HRV | „detectăm depresia din voce” | cost de validare, derapaj de firmware, bias |
| Interoperabilitate și date controlate de pacient | FHIR, IPS, EHDS | Estonia: 99% rețete electronice ([PSN](https://cdn.publicsectornetwork.com/insight/pdfs/Birgit_Lao_PSN_Toronto_26092024_Lao_send_522142.pdf)) | — | „portofelul de sănătate al pacientului” (Google Health, HealthVault, închise) | lipsa fluxului clinic; termenele EHDS 2029/2031 |
| Agenți AI care coordonează îngrijirea | agenți vocali și text, orchestrare | reminderele simple cresc prezența (SMS: RR 1,06–1,23) [Stabilit] | răspunsurile la mesaje redactate de LLM: mai puțină epuizare, fără timp economisit (BK); Platform24: 3 din 10 pacienți triați greșit ([SVT](https://www.svt.se/nyheter/lokalt/skane/svt-avslojar-hemlig-rapport-underkanner-1177-s-digitala-losning-platform24)) | „asistentă virtuală autonomă” | AI Act Art. 50 din 2.08.2026; triajul intră în Anexa III din 2.12.2027 |
| Gemeni digitali | modele de organ derivate din imagistică | CUVIA-PRR: un RCT, o procedură [Emergent puternic] | — | „geamănul tău digital” | capital, calcul, validare; platforma UE VHT nu are încă dată de lansare ([EC](https://digital-strategy.ec.europa.eu/en/news/virtual-human-twins-launch-european-virtual-human-twins-initiative)) |

### Ce devine normal și când

Tabelul de mai jos e **judecata cercetătorilor**, ancorată în dovezile de mai sus și în termene legale. Nu am găsit nicio previziune instituțională (OMS, OCDE, Comisia Europeană) cu rate de adopție pe ani. Planurile instituționale, cum e planul NHS pe 10 ani („de la boală la prevenție”, scoruri de risc care combină scorul poligenic cu factorii clinici), sunt pariuri de politică, nu dovezi ([NHS 10-Year Plan](https://assets.publishing.service.gov.uk/media/6888a0996478525675738f3a/fit-for-the-future-10-year-health-plan-for-england-executive-summary.pdf)).

| Domeniu | 2026–2030 | 2030–2035 | 2035–2040 |
|---|---|---|---|
| Detecție timpurie cu AI | AI la citirea mamografiilor în multe programe UE; screening autonom al retinopatiei unde e rambursat [Emergent puternic] | AI ca cititor standard în screeningul imagistic; primele date de mortalitate [Plauzibil] | citirea autonomă a majorității examenelor normale [Speculativ] |
| Monitorizare și wearables | notificările ceasului devin declanșatori obișnuiți de trimitere, cu confirmare pe ECG sau prin monitorizarea ambulatorie a tensiunii [Emergent puternic] | tensiunea fără manșetă, validată, acceptată în unele trasee clinice [Plauzibil] | glicemie neinvazivă fără calibrare [Speculativ] |
| Predicție din dosar | scoruri clasice în fluxul medicului; modelele fundaționale doar în cercetare [Plauzibil] | semnale de risc din modele fundaționale livrate de vendori, cu validare locală obligatorie [Plauzibil] | prognoze individuale pe 20 de ani care conduc prevenția [Speculativ] |
| Biomarkeri și testare | screeningul organizat se extinde; panourile și scanările pentru consumatori cresc fără dovezi | datele pe termen lung din NHS-Galleri decid politica [Plauzibil] | screening multi-cancer din sânge, cu beneficiu dovedit [Speculativ] |
| Recomandări personalizate | programele digitale de prevenție a diabetului devin alternativă rambursabilă în unele sisteme [Emergent puternic] | dovezi de durabilitate pe 5 ani [Plauzibil] | prevenție multi-omică cu beneficiu dovedit [Speculativ] |
| Fluxuri și suport decizional | scribii devin rutină în Marea Britanie și SUA [Emergent puternic] | suport decizional LLM cu RCT-uri pe sarcini precise [Plauzibil] | panouri de boli cronice gestionate semi-autonom de agenți [Speculativ] |
| RPM și boli cronice | RPM rambursat pentru insuficiență cardiacă și hipertensiune în Germania, SUA și câteva alte țări [Emergent puternic] | triajul cu AI reduce timpul de revizie [Plauzibil] | monitorizarea devine implicită în orice plan de îngrijire cronică [Speculativ] |
| Analitica populației | tablouri peste tot, cu dovezi slabe | analitică legată de intervenții finanțate [Plauzibil] | contractare predictivă cu internări reduse demonstrat [Speculativ] |
| Îmbătrânire și îngrijire la domiciliu | detecția căderilor pe ceas; kituri vândute prin agenții [Emergent puternic pentru folosire, Plauzibil pentru rezultate] | monitorizare radar în căminele noi [Plauzibil] | „gemeni” ai locuinței la scara populației [Speculativ] |
| Biomarkeri digitali | mai multe criterii digitale în studiile clinice [Emergent puternic] | câțiva biomarkeri în trasee clinice de rutină [Plauzibil] | screening multimodal pentru sănătatea mintală [Speculativ] |
| Interoperabilitate | EHDS grupa 1 (rezumate, rețete) din 26.03.2029; România în urmă [Emergent puternic legal, Plauzibil ca termen] | grupa 2 (analize, imagini, externări) din 26.03.2031; folosirea secundară prin organismele de acces la date [Emergent puternic legal] | fluxuri de date dirijate de pacient spre orice serviciu [Speculativ] |
| Agenți AI | agenți administrativi (programări, remindere, rechemări) normali în clinicile private [Emergent puternic] | agenți clinici protocolizați, certificați CE, supravegheați de asistente [Plauzibil] | coordonatori autonomi ai planului de îngrijire [Speculativ] |
| Gemeni digitali | gemeni de organ în proceduri înguste [Plauzibil] | gemeni multi-organ în centre de specialitate [Plauzibil–Speculativ] | geamăn de corp întreg în îngrijirea de rutină [Speculativ] |

### Ce înseamnă asta pentru un fondator de software

Fiecare exemplu cu rezultat pozitiv depinde de o infrastructură care nu e AI:
- mamografia, de un program de screening cu invitații și flux de citire;
- retinopatia, de testul la punctul de îngrijire și de urmărirea trimiterii;
- EAGLE, de alerta din dosar și de comanda testului de confirmare;
- TREWS, de echipe care răspund la alerte;
- prevenția diabetului, de urmărirea implicării pacienților.

**„Ultimul kilometru”** (acționarea, urmărirea și măsurarea rezultatului) e locul unde se câștigă sau se pierde beneficiul, și are puține unelte. Asta e pentru fondator cea mai solidă inferență din cercetare [Plauzibil].

**Calendarul de reglementare aduce cererea pentru această infrastructură înainte de 2030:**
- **directiva de răspundere pentru produse (PLD)** face din software produs cu răspundere strictă pentru versiunile lansate după 9 decembrie 2026 ([Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive));
- **AI Act, după Omnibus** (Regulamentul 2026/1744): AI-ul din dispozitivele medicale devine cu risc ridicat din 2 august 2028, iar sistemele din Anexa III, inclusiv triajul de urgență, din 2 decembrie 2027 ([Orrick](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes));
- **EHDS** se aplică general din 26 martie 2027, cu termenele pe categorii de date din 2029 și 2031 ([Comisia Europeană, Q&A EHDS](https://health.ec.europa.eu/document/download/4dd47ec2-71dd-49fc-b036-ad7c14f6ed68_en?filename=ehealth_ehds_qa_en.pdf)).

**Beneficiile modelelor predictive înseși vor rămâne inegale.** Chiar și pentru fondatorul cel mai ambițios tehnic, drumul realist trece prin a deveni locul în care predicțiile altora produc acțiuni.

## 3. Harta tehnologică: unde se câștigă valoare fără dispozitiv medical

### Unde e granița de reglementare

Harta are sens doar dacă se vede de la început granița de reglementare. În UE, software-ul e dispozitiv medical în funcție de **scopul declarat de producător, inclusiv în materialele de vânzare și promovare**. Definiția din MDR include explicit „predicția” și „prognosticul”. Regula 11 împinge aproape orice informație folosită pentru decizii de diagnostic sau tratament în **clasa IIa sau mai sus**, cu organism notificat (BK; [MDR, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj)) [Stabilit].

**Spre deosebire de SUA, UE nu are o excepție pentru suportul decizional transparent.** „E doar o formulă publicată” nu scoate un calculator SCORE2 de sub MDR. Ghidul MDCG 2019-11 a fost revizuit pe 17 iunie 2025, cu exemple noi despre prevenția bolilor ([Comisia Europeană](https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en)). Software-ul care doar stochează, comunică, face căutări simple sau programează administrativ nu e dispozitiv [Emergent puternic].

**Costul clasei IIa** e estimat la **32.000–110.000 € și 9–18 luni**, fără investigații clinice. Estimarea vine de pe blogul unui furnizor, deci e doar un ordin de mărime ([meddeviceguide](https://meddeviceguide.com/blog/ce-marking-cost-medical-devices-guide)). Asta e peste buget pentru un prim produs.

**Aceeași funcție își schimbă clasa după formulare:**

| Formularea funcției | Încadrarea |
|---|---|
| „Îi amintește pacientului data de control stabilită de medic” | administrativ |
| „Identifică pacienții restanți la screening după ghid” | zonă de graniță |
| „Identifică pacienții cu risc mare care trebuie văzuți mai devreme” | dispozitiv |
| „Arată buletinul de analize” | administrativ |
| „Evidențiază valorile anormale și prezice deteriorarea” | dispozitiv, posibil sub IVDR |

[Emergent puternic, după notele de reglementare]

### Straturile de software de care are nevoie sănătatea predictivă

| Strat | Ce face | Cine îl cumpără sau îl construiește azi | Încadrarea tipică | Potrivirea cu fondatorul |
|---|---|---|---|---|
| **1. Ingestie și normalizare** | citește CSV, Excel, PDF, HL7 v2, FHIR; mapează pe ICD-10, LOINC, ATC; preia date de la wearables prin API-uri agregate (Terra, Thryve) | vendori de integrare (Redox în SUA), laboratoare, companii digitale; în România, exporturi fără API la aproape toți vendorii | administrativ, dacă afișează fidel | **foarte bună**: Python, SQL, LLM doar pentru maparea coloanelor |
| **2. Identitate, consimțământ, jurnal de acces** | registru de consimțământ granular; jurnal „cine a deschis dosarul”; componenta de jurnalizare cerută de EHDS | clinici sub presiunea amenzilor ANSPDCP; vendori care se pregătesc pentru EHDS | administrativ; parte dintr-un „sistem EHR” din 2029/2031 | bună |
| **3. Cronologia longitudinală** | istoricul pe persoană: examene, rezultate, recomandări, expuneri | rețelele mari (aplicațiile MedLife și Regina Maria, cu 10+ ani de istoric) | administrativ dacă afișează fidel; „sistem EHR” dacă stochează date din categoriile prioritare | bună (Oracle/APEX) |
| **4. Motorul de termene și listele de lucru (stratul de buclă)** | termene puse de medic sau de program; cine acționează și până când; escaladare; închiderea jurnalizată | aproape nimeni în România pentru independenți; în SUA, uneltele de rechemare dentară și de urmărire a rezultatelor | administrativ, cât timp ceasul e al medicului | **foarte bună**: miezul recomandării |
| **5. Comunicare și coordonare** | SMS, WhatsApp, e-mail, agent vocal; link de programare; urmărirea trimiterilor | foarte aglomerat la nivelul reminderelor (MediNote, Callio, VAstoma, DentAIM) | administrativ; AI Act Art. 50 dacă e chatbot; triajul e dispozitiv | bună ca strat al motorului, slabă ca produs separat |
| **6. Capacitate și dispecerat** | invitații în valuri după capacitate, umplerea anulărilor, planul de deplasări al echipelor mobile | programe de screening, clinici de endoscopie și imagistică, firme de medicina muncii cu echipă mobilă | administrativ (prognoză de volum, nu de persoană) | bună: prima formă legal curată de „predicție” |
| **7. Măsurarea rezultatelor și generarea de dovezi** | audit de bază, grupuri de comparație, registre de rezultate, rapoarte pentru plătitori | programe UE, NICE (DERM, cu dovezi colectate 3 ani), plătitori | administrativ sau analiză la nivel de populație | **subevaluată**: transformă „prevenția” din vorbă în dovadă |
| **8. Monitorizarea modelelor terților** | validare locală, derapaj, povara alertelor, performanța pe subgrupuri | spitale care cumpără AI marcat CE; obligațiile utilizatorului din AI Act Art. 26, din 2 august 2028 | administrativ sau de calitate | slabă acum în România (n-a fost găsit niciun utilizator); opțiune pentru 2028+ |
| **9. Interoperabilitate reglementată** | fațadă FHIR R4 peste baze vechi; rezumat IPS; MyHealth@EU; interfețele CNAS SIUI/PIAS | vendorii de software medical (autocertificare EHDS); furnizorii cu contract CNAS | componentă de „sistem EHR”, nu MDR | **foarte bună** pe PL/SQL, dar cererea vine în 2027–2029 |
| **10. Modele predictive și diagnostice** | scoruri de risc, interpretare de imagini și semnale | vendori certificați CE (ScreenPoint, Vara, Skin Analytics, Cardiomatics) | clasa IIa–III; AI cu risc ridicat din 2028 | **nu** ca prim produs; mai târziu, doar găzduirea modelelor altora |
| **11. Stratul pentru consumator** | aplicații, wearables, PHR, abonamente de analize | Oura, Whoop, Function, Neko | wellness sau dispozitiv, după afirmații | slabă: plătitorul lipsește, capital mare |
| **12. Software pentru furnizorii existenți** | add-on-uri peste programele de cabinet, portaluri cu marca furnizorului, livrarea rezultatelor, componente pentru vendori | cabinete de medicina muncii, laboratoare, clinici independente, vendori locali | administrativ | **foarte bună**: aici e primul produs |

### Straturile trecute cu vederea

Trei straturi lipsesc din aproape orice pitch de „sănătate predictivă” și sunt exact cele pe care dovezile le arată drept decisive.

**Stratul de buclă (4), adică proprietarul plătit al drumului de la semnal la acțiune.** Analiza laterală a ajuns la el pe patru drumuri independente:
- concept fan;
- inversarea presupunerilor;
- analogia cu organizația de continuitate a navigabilității din aviație (CAMO), care deține defectele amânate și termenele lor fără să repare nimic;
- random stimulus.

Toate au produs aceeași concluzie: **resursa rară nu e informația, ci responsabilitatea pentru acțiune și un buget care există deja** (analiză, `analiza_laterala.md` §F1).

**Stratul de capacitate (6).** O campanie de invitații fără capacitate în aval creează liste de așteptare. Un calcul pe ROCCAS 4 Nord-Vest, cu pozitivitatea FIT din Oltenia, dă **~1.614 pozitivi față de 1.328 de colonoscopii țintă** (calculul din analiza laterală, cu ipoteza că pozitivitatea se transferă între regiuni; [ARPS](https://arps.ro/proiecte/roccas-4-nv); [Gazeta de Sud](https://www.gds.ro/Sanatate/2026-04-23/screeningul-pentru-cancer-colorectal-in-oltenia-prinde-amploare-peste-2000-de-persoane-incluse-in-programul-roccas-4-svo/)).

**Stratul de măsurare (7).** Fără el, PRISMATIC se repetă.

Alte două straturi rare au propriul plătitor:
- **curatoriatul sau „dez-implementarea”:** scoaterea testelor fără valoare din pachetele plătite de asigurători, în contextul în care daunele de sănătate au crescut cu ~30% în T1 2025, față de prime în creștere cu 12–13% ([ZF](https://www.zf.ro/banci-si-asigurari/piata-de-asigurari-in-t1-2025-asigurarile-de-sanatate-au-ajuns-la-22845837));
- **arhiva longitudinală de expunere profesională:** pentru cancerigeni, evidențele se păstrează 40 de ani (BK; [Directiva 2004/37/CE](https://eur-lex.europa.eu/eli/dir/2004/37/oj)).

### Unde se capturează valoarea

Valoarea se capturează în instalațiile plictisitoare, nu în strălucirea predicției. Aeon a cumpărat din insolvența Aware **integrările cu laboratoarele, rețeaua de recoltare și ~10.000 de clienți activi**, nu marca ([IT Brief UK](https://itbrief.co.uk/story/aeon-buys-aware-health-assets-in-eur-expansion-push)). Lifen a devenit profitabilă din rutarea documentelor. Junction a strâns 18 mil. $ pentru un API de comandă de analize ([Junction docs](https://docs.junction.com/lab/overview/introduction)). Pentru fondator, straturile 1, 4, 6, 7 și 12 sunt cele în care competențele lui (SQL, PL/SQL, APEX, n8n, LLM pentru mapare) contează mai mult decât capitalul.

## 4. Peisajul competitiv global: penele înguste câștigă, consumatorul arde capital

Tabelele de mai jos acoperă peste 50 de companii și sisteme. Fiecare rând distinge datele dezvăluite (V) de afirmațiile companiei (C) și de estimările agregatorilor (E). Câmpurile lipsă înseamnă că nu s-a găsit nimic verificabil, nu că lipsesc din realitate. Prețurile și cifrele vin din rezumatele motorului de căutare. Paginile de preț ale vendorilor nu au putut fi deschise.

### 4.1 Vânzători B2B înguști: povești „îngust, apoi extins”

| Companie | Produs și problemă | Plătitor și model | Preț (calitate) | Tracțiune (calitate) | Tehnologie, dovezi, reglementare | Lecția și oportunitatea pentru România |
|---|---|---|---|---|---|---|
| **Accurx** (UK, 2016) | SMS trimis din desktopul medicului de familie → mesagerie, video, programare, rechemare | comisariatele NHS și cabinetele; per pacient înregistrat pe an | £0,20–0,97/pacient/an, SMS separat (V, documente G-Cloud 2026, posibil promoțional) ([G-Cloud](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/708675/281422867192066-pricing-document-2026-08-10-1029.pdf)) | contract regional de £1,41M (V) ([Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/52859b24-dfb2-431d-adfd-2bfdfe794d6b)); „98% din cabinetele din Anglia” (C); €39,1M venit 2023 (E) | administrativ; distribuie scribul Tandem către 200k+ angajați NHS (C) | **se lipește de sistemul de evidență, iar distribuția devine șanțul de apărare**; plata per pacient se potrivește cu rechemarea |
| **Lifen** (FR, 2015) | trimiterea documentelor medicale → integrare automată în dosarul electronic al spitalului → platformă de date | spitale și medici privați | nepublicat | „Lifen Care” profitabil, >€20M ARR în 2025 (C); 800+ spitale (C); ~€77M strânși (V, presă) ([FrenchWeb](https://www.frenchweb.fr/lifen-la-startup-qui-digitalise-lhopital-sans-jamais-apparaitre-a-lecran/454591)) | administrativ | instalația plictisitoare devine afacere, dar după 10 ani și cu capital |
| **Lighthouse 360 / Solutionreach** (SUA) | rechemare dentară legată de programul cabinetului | cabinet; tarif fix pe locație | LH360: $329/lună + $299 configurare (E) ([SoftwarePundit](https://www.softwarepundit.com/node/40)); Solutionreach: $199–249 (E) ([Spendbase](https://www.spendbase.co/?p=36425)) | nepublicat | administrativ | ancoră de preț: rechemarea se vinde la ~$200–350 pe locație în SUA; în România, o fracțiune |
| **Weave** (SUA, listată) | telefon + SMS pentru stomatologie → plăți, recenzii, AI | cabinet; abonament + plăți | ~$499/lună (E, articol vechi) | FY2025: $239,0M venit (+17%), cash-flow liber $12,9M, pierdere netă $28,1M (V) ([BusinessWire](https://www.businesswire.com/news/home/20260218591820/en/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/)) | administrativ | o pană de comunicare devine companie listată, dar tot pe pierdere contabilă |
| **Cliniko** (AU, 2010) | program de cabinet pentru kinetoterapie și alte specialități conexe; a rămas îngust | cabinet; tarif pe intervale de număr de practicieni | $45–395/lună (E, surse în conflict) ([CostBench](https://costbench.com/software/scheduling/cliniko/)) | ~$1,5M venit 2025, ~14 oameni, fără VC (E, încredere mică) ([Latka](https://getlatka.com/companies/cliniko.com)) | administrativ | bootstrapping posibil, dar lent: ~15 ani |
| **Jane App** (CA) | program de cabinet pentru specialități conexe | per practician | nepublicat | ~404–420 angajați (E) ([Built In](https://builtin.com/company/jane-app)); run-rate de $4,7M în 2018 (E) | administrativ | modelul de cabinet merge, dar cere un produs mare |
| **Semble** (UK) | dosar electronic pentru clinici private → plăți → Franța | per utilizator | de la ~£119/utilizator/lună (E, sursă: un concurent) | 1.700+ organizații (C); Series C de £30M (V) ([Semble](https://www.semble.io/articles/sembles-ps30m-series-c-funding-explained)) | — | plafon de preț pentru programele de clinică din vest |
| **Kaiku Health** (FI) | monitorizarea simptomelor raportate de pacienții oncologici | spitale | nepublicat | €1,3M venit și 35 de oameni (2019); cumpărată 100% de Elekta în 2020 (V) ([ArcticStartup](https://arcticstartup.com/kaiku-health-exits-elekta/?amp=1)) | statutul de dispozitiv neverificat | **o nișă îngustă, vândută unui incumbent care are distribuție în aceeași nișă**, la sub 2 mil. € venit |
| **Lindera** (DE, 2017) | riscul de cădere din mersul filmat cu camera telefonului | cămine, asigurători | nepublicat | 350+ unități în 2021 (C) ([Presseportal](https://www.presseportal.de/pm/156286/5083103)); Series A de ~€6M (V) | statutul DiGA/DiPA neverificat | căminele cumpără documentare și siguranță, nu dovezi |
| **Thryve** (DE) | un singur API pentru 100+ API-uri de wearables (500+ dispozitive) | asigurători, producători DiGA, farma | nepublicat | Series A de €4M (V) ([Tech.eu](https://tech.eu/2024/08/30/german-thryve-secures-4m-series-a-to-accelerate-international-growth/)) | „conform GDPR, certificat ISO” (C) | **cumpără API-ul, nu-l construi** |
| **Terra** (UK/SUA) | API pentru 500+ surse de wearables și laboratoare | dezvoltatori; plată după consum | „de la $399–499/lună” (E/C) ([Terra](https://tryterra.co/pricing)) | seed de $2,8M (V) ([TechCrunch](https://techcrunch.com/2021/06/09/terra-raises-2-8m-to-build-the-plaid-for-fitness-data)) | — | aceeași lecție: stratul de agregare e deja marfă |
| **Medplum** (SUA) | server FHIR open-source (Apache 2.0) + găzduire | dezvoltatori | oferte private | finanțări raportate între $125k și $6,5M (E, conflict) ([Medplum](https://www.medplum.com/open-source)) | — | **unealtă** pentru fondator, nu concurent |
| **Healthie** (SUA) | dosar electronic pentru practici de wellness și virtuale → API | per furnizor | $19,99–149/lună, după numărul de clienți activi (E) ([SoftwareFinder](https://softwarefinder.com/emr-software/healthie/pricing)) | Series B condusă de TCV (sumă necunoscută) | — | intrare ieftină prin plafonul de clienți activi |

### 4.2 Platforme, scribi AI și interoperabilitate

| Companie | Produs și problemă | Plătitor și model | Preț (calitate) | Tracțiune (calitate) | Tehnologie, dovezi, reglementare | Lecția și oportunitatea pentru România |
|---|---|---|---|---|---|---|
| **Doctolib** (FR) | programare online → program de cabinet → teleconsultații → AI | per practician pe lună | ~€139/lună în Germania, cu remindere incluse (E) ([GIGA](https://www.giga.de/tech/was-kostet-doctolib-diese-preise-und-tarife-gibt-es-aktuell--01KPN5Y6VMKWGMSGVS4BDCZ046)); asistentul AI €79/lună la lansarea din 2024 ([Maddyness](https://www.maddyness.com/2024/10/15/intelligence-artificielle-doctolib-lance-son-assistant-de-consultation/)) | ARR €348M în 2024, pierdere €53,8M (V) ([Sifted](https://sifted.eu/articles/doctolib-results-2024)) | administrativ + AI | o pană de programare devine suită; nu e prezent în România |
| **Docplanner** (PL) | marketplace gratuit pentru pacienți + SaaS pentru medici + AI Noa (note, programare vocală) | medici și clinici | nepublicat | EBITDA pozitiv în 2025 (C) ([LinkedIn CEO](https://pl.linkedin.com/in/peterbialo)); ~20–22M programări/lună, 13 țări (C) ([Twilio](https://www.twilio.com/en-us/press/releases/docplanner-expands-patient-access-with-voice-ai-agent-powered-by)) | administrativ; Noa Evidence e la graniță | **a decis încă din ~2016 să nu intre în România cu echipă locală** ([StartupCafe](https://www.startupcafe.ro/stiri-idei-21426385-docplanner-booking-com-tripadvisor-com-medici-peter-bialo.htm)); stratul pentru clinicile mici rămâne local |
| **Tandem Health** (SE) | scrib → asistent de codare și suport decizional → „sistem de operare pentru clinică” | organizații medicale | nepublicat | $160M strânși în total; Series B de $100M (V) ([TheNextWeb](https://thenextweb.com/news/tandem-health-100m-series-b-scaleup-europe-fund)); 10.000 de organizații (C) | **scribul, codarea și suportul decizional certificate MDR IIa** | scribii alunecă în zona reglementată pe măsură ce cresc |
| **Heidi Health** (AU) | scrib gratuit → planuri plătite pe clinician → practică | clinician și practică | gratuit; $90–150/utilizator/lună (C/E) | Series B de $65M la ~$465M evaluare (V) ([TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72)); ~$340M strânși în 2026 (V, presă) ([Startbase](https://www.startbase.com/news/heidi-erhaelt-340-millionen-dollar-fuer-ki-im-gesundheitswesen/)) | — | prețul scribului coboară spre zero în partea de jos a pieței |
| **Nabla** (FR) | scrib | clinician și companii mari | gratuit ~30 de consultații/lună; Pro ~$119 (E, neoficial) | Series C de $70M (V) ([Dealroom](https://dealroom.co/companies/nabla/)); 85.000 de clinicieni (C) | RCT UCLA: −41 s/notă față de −18 s în grupul de control | nu concura frontal |
| **Abridge** (SUA) | scrib pentru spitale, integrat în Epic | sisteme de spitale | ~$2.500/clinician/an (E) | ARR ~$100M în mai 2025 (E) ([Sacra](https://sacra.com/research/abridge)); $300M la $5,3B (V) ([Maginative](https://www.maginative.com/article/abridge-raises-300m-series-e-at-5-3b-valuation/)) | dependent de Epic | nu se transferă |
| **Microsoft Dragon Copilot** (UK/UE) | scrib ambiental | NHS, spitale | nepublic | lansat în NHS pe 4.09.2025 (V) ([Digital Health](https://www.digitalhealth.net/2025/09/microsoft-launches-ambient-ai-assistant-to-the-nhs)) | MHRA clasa I | incumbent global |
| **Redox** (SUA) | motor de integrare cu dosarele electronice | vendori de software | taxă de platformă + de conexiune + de tranzacție | ~$181M venit 2024 (E) ([Latka](https://www.getlatka.com/companies/redoxengineredox)) | piața de EHR din SUA | modelul de taxe pe conexiune e util, piața nu |
| **Health Gorilla** (SUA) | comandă de teste → rețea de date clinice | companii digitale, laboratoare | nepublicat | $80M strânși (V); dat în judecată de Epic și 4 furnizori (V) ([Healthcare IT News](https://www.healthcareitnews.com/news/epic-and-health-systems-sue-health-gorilla-and-data-companies)) | HIPAA, TEFCA | **extragerea dosarelor în numele altora are risc juridic mare** |
| **Junction** (SUA/UK) | API de comandă și rezultate de laborator | companii digitale | nepublicat | Series A de $18M (V) ([Junction](https://docs.junction.com/lab/overview/introduction)) | laboratoare CLIA/CAP | integrarea cu laboratoarele e un strat finanțabil separat |
| **Kaia Health** (DE) | terapie digitală pentru durerea de spate | asigurările statutare (DiGA), pe rețetă | prețul mediu provizoriu al unei DiGA: €645 (2023) ([ISPOR](https://www.ispor.org/heor-resources/presentations-database/presentation/euro2024-4013/144119)) | listată permanent în 2023 pe baza unui RCT (V); cumpărată de Sword, ~$285M raportat (Plauzibil) | MDR + RCT | calea DiGA cere marcaj CE și RCT; România nu are echivalent |
| **Ada Health** (DE) | verificator de simptome pentru consumatori → licențe pentru asigurători și spitale | asigurători (Groupe Mutuel, Santéclair), sisteme de spitale | nepublicat | „50M+ utilizatori” și „profitabil” (C, nedovedit) ([MedCity News](https://medcitynews.com/tag/ada-health/)) | triaj = dispozitiv | B2B2C prin asigurător; triajul e zonă interzisă la început |

### 4.3 Monitorizare, RPM și prevenție pentru consumator

| Companie | Produs și problemă | Plătitor și model | Preț (calitate) | Tracțiune (calitate) | Tehnologie, dovezi, reglementare | Lecția și oportunitatea pentru România |
|---|---|---|---|---|---|---|
| **Luscii** (NL, 2018) | măsurători acasă pentru boli cronice → secții virtuale NHS | spitale, NHS | listată pe G-Cloud | cumpărată de OMRON în 2024 (V) ([CB Insights](https://www.cbinsights.com/company/luscii)); grant SBRI de £211.333 (V); Leeds: 47% cu mai puține vizite la urgențe (C, evaluare a vânzătorului) | statut neverificat | RPM merge doar unde există plătitor public |
| **Validic** (SUA) | agregarea datelor de la dispozitive pentru RPM | sisteme de spitale | nepublicat | cumpărată în 2026 de ChartSpan, o firmă de servicii de îngrijire cronică (V) ([HIT Consultant](https://hitconsultant.net/2026/06/22/chartspan-acquires-validic-remote-patient-monitoring/)) | rambursare CCM/RPM în SUA | un API de dispozitive a fost absorbit de un serviciu rambursat |
| **Medicalgorithmics** (PL) | dispozitive + AI pentru ECG | parteneri, lanțul rambursat din SUA | nepublicat | PLN 31,0M în 2025 (+29%), SUA +140%, EBITDA pozitiv în T4 (V) ([Biznesradar](https://www.biznesradar.pl/a/146488,medicalgorithmics-podsumowuje-2025-r-kwartalna-ebitda-na-plusie)) | dispozitiv medical | **produsul reglementat trăiește din piața rambursată din străinătate** |
| **Cardiomatics** (PL) | analiză ECG/Holter cu AI în cloud | clinici | nepublicat | 700+ clienți (C, 2021); seed de $3,2M (V) ([TechCrunch](https://techcrunch.com/2021/08/20/cardiomatics-bags-3-2m-for-its-ecg-reading-ai)) | marcaj CE din 2018 | un produs CE poate trăi din clinici, dar cere certificare |
| **Function Health** (SUA) | abonament cu 160+ analize, plus RMN Ezra | consumator | $365/an (V, presă) ([MedCity News](https://medcitynews.com/2025/11/function-health-startup-testing-imaging/)) | ~$100M run-rate, ~200k abonați în feb. 2025 (E) ([Sacra](https://sacra.com/research/function-health-at-100m-year/)); finanțare de creștere de $450M, rambursată din valoarea cohortelor (V, presă) ([MobiHealthNews](https://www.mobihealthnews.com/news/function-health-secures-450m-growth-financing)) | **niciun studiu de rezultat**; laboratoare Quest | nu se transferă: în România, laboratoarele sunt chiar mărcile de consum |
| **Superpower** (SUA) | abonament de analize | consumator, subvenționat de parteneri | $199/an; $49 prin partener (V, presă) ([Athletech](https://athletechnews.com/superpower-199-membership-preventive-care/)) | niciun număr de membri publicat | — | prețul accesului la panouri se prăbușește |
| **Oura** (FI/SUA) | inel + abonament | consumator | — | venit LTM $1,4B; 5,0M membri plătitori; retenție la 12 luni ~85%; profit net $60,8M pe 9 luni (V, S-1) ([Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/News/121786/smart-ring-maker-oura-sets-terms-for-2-1-billion-ipo)); IPO amânat pe 29.09.2026 (V) | wellness | consumatorii plătesc când produsul e un dispozitiv purtat zilnic |
| **Whoop** (SUA) | abonament cu hardware inclus | consumator | $199–359/an; €199–399 în UE (V) | 2,5M+ membri; cash-flow pozitiv în 2025 (C) ([Yahoo Finance](https://finance.yahoo.com/sectors/healthcare/articles/whoop-raises-575-million-10-204207038.html)) | scrisoare de avertizare FDA în 2025 pentru funcția de tensiune ([FDA](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-07142025)) | afirmațiile medicale atrag regulatorul |
| **Withings** (FR) | dispozitive + Withings+ (4 revizii de cardiolog în 24 h) | consumator | €99,95/an (V, comunicat) ([Withings](https://media.withings.com/press/press-releases/bpm-vision-cardio-check-up-ces/CES-2025_Withings_BPM-Vision-Cardio-Check-Up_PR_Final.pdf)) | profitabil în 2025; ~2/3 din venit din dispozitive medicale (C) | FDA / CE-MDR | **revizia umană vândută ca produs**: un model pentru stratul de buclă |
| **Dexcom Stelo** (SUA) | CGM fără prescripție | consumator | $89/lună | ~$130M în 2025, față de o prognoză de $190M (V față de previziune) ([MarketBeat](https://www.marketbeat.com/instant-alerts/dexcom-q4-earnings-call-highlights-2026-02-12/)) | autorizare FDA OTC; fără beneficiu dovedit la nediabetici | adoptarea reală e sub hype |
| **Neko Health** (SE/UK) | scanare de corp întreg + consultație | consumator | £299 în UK; $499 în New York | >100k scanări; ~75% își plătesc anticipat scanarea următoare (C) ([Pulse2](https://pulse2.com/neko-health-raises-700-million-series-c-ahead-of-u-s-launch/)); $700M la ~$7B (V, presă, din surse) | date proprii, fără grup de control ([Neko](https://www.nekohealth.com/neko-data-story-year-two)) | integrat vertical și foarte scump; de copiat doar mecanismul de reprogramare |
| **Prenuvo** (SUA) | RMN de corp întreg | consumator, angajatori care își asigură singuri angajații | $2.500; pachet de $3.999 | ~$100M în 2024, „profitabil” (CEO, Plauzibil) ([NBC](https://www.nbcsandiego.com/news/business/money-report/prenuvo-adds-new-health-tests-to-flagship-full-body-scan-raises-120-million-in-fresh-funding/3753868/)) | colegiile americane de radiologie (ACR) și de medicină preventivă (ACPM) recomandă împotriva lor | marketing înaintea dovezilor |
| **Irish Life Health / Inuvi** (IE) | test de sânge acasă + raport revizuit de clinician | asigurătorul, ca beneficiu pentru membri | €50 (V) ([Irish Life](https://www.irishlife.ie/health-insurance/health-benefits/essential-health-check/)) | — | revizie clinică | **B2B2C prin asigurător** e calea europeană viabilă |

### 4.4 Eșecuri și cazuri de avertizare

| Companie | Ce a fost | Ce s-a întâmplat (calitate) | Mecanismul eșecului | Lecția |
|---|---|---|---|---|
| **Forward** (SUA) | abonament de medicină primară + CarePods | închisă în nov. 2024; $400–657M strânși, sub $100M venit cumulat (V, presă) ([Fierce Healthcare](https://www.fiercehealthcare.com/health-tech/primary-care-player-forward-shutters-after-raising-400m-rolling-out-carepods?utm_id=74)) | livrare fizică intensivă în capital; ~5 CarePods la ~$1M fiecare (foști angajați) | nu construi hardware și nici clinici |
| **Babylon** (UK/SUA) | telemedicină + contracte de risc | pierdere de $221M în 2022; administrare specială în 2023; active vândute către eMed (V, presă) ([Fierce Healthcare](https://www.fiercehealthcare.com/digital-health/babylon-closes-us-business-lays-employees-after-mindmaze-take-private-deal-collapses)) | îngrijire cu risc asumat, pe pierdere, plus o fuziune ratată | evaluarea nu e afacere |
| **Pear Therapeutics** (SUA) | terapii digitale pe rețetă, autorizate FDA | $12,7M venit față de $75,5M pierdere în 2022; faliment (Chapter 11) în 2023 (V) ([In Vivo](https://invivo.pharmaintelligence.informa.com/IV147722/Pear-Bankruptcy-Filing-Highlights-Reimbursement-Barriers-for-Digital-Therapeutics)) | Medicare nu le acoperea | autorizarea nu garantează plătitorul |
| **Aware Health** (DE) | teste de sânge prin lanțul de drogherii dm | insolvență în iunie 2026; active cumpărate de Aeon (V, presă) ([Apotheke Adhoc](https://www.apotheke-adhoc.de/nachrichten/detail/markt/blutanalysen-dm-partner-ist-pleite/print.html)) | volume mici direct la consumator în Europa | valoarea a rămas în integrări, nu în marcă |
| **ZOE** (UK) | nutriție personalizată, CGM | venit £29M și pierdere ~£20M în FY23, marjă brută 28%; concedieri în 2024 (V, conturi preluate de presă) ([The Grocer](https://thegrocer.co.uk/health/can-zoe-app-trim-enough-of-its-own-fat-to-fight-fit-again/690316.article)) | testare costisitoare, valoare oferită o singură dată | retenția vine din bucle recurente |
| **Huma** (UK) | aplicații de spital → RPM clasa IIb | concedieri (~45 de oameni) la încetinirea veniturilor (V) ([Sifted](https://sifted.eu/articles/uk-healthtech-huma-layoffs)) | certificarea nu aduce singură clienți | clasa IIb nu înseamnă venit |
| **Biofourmis** (SG/SUA) | RPM, spitalizare la domiciliu | 120 de concedieri; CEO-ul a plecat (V) ([MobiHealthNews](https://www.mobihealthnews.com/news/biofourmis-confirms-layoffs-120-employees-globally)) | dependență de rambursarea din SUA | — |
| **Amazon Halo** | wearable + abonament | oprit în 2023 (V) ([Amazon](https://www.aboutamazon.com/news/company-news/amazon-halo-discontinued)) | segment aglomerat, critici legate de intimitate | — |
| **Google Health, Microsoft HealthVault** | dosare personale de sănătate (PHR) | închise în 2011 și 2019 (V/BK) ([InformationWeek](https://www.informationweek.com/it-sectors/5-reasons-why-google-health-failed)) | fără date care să curgă singure, fără flux clinic | consumatorii plătesc doar ca „membri captivi” |
| **Comarch Healthcare** (PL) | HIS, telemedicină, clinică proprie | veniturile din sănătate −40% în 2024; HIS vândut către Sygnity; clinica vândută (V, presă) ([ITwiz](https://itwiz.pl/comarch-sprzedaje-segment-his-firmie-sygnity/)) | portofoliu larg vândut statului prin licitații | nu intra pe software de spital prin achiziții publice |
| **Platform24** (SE) | triaj pentru serviciul național 1177 | 3 din 10 pacienți triați greșit (raport confidențial); supraveghere din partea agenției suedeze a medicamentului pentru că nu era înregistrat ca dispozitiv (V, presă) ([SVT](https://www.svt.se/nyheter/lokalt/skane/svt-avslojar-hemlig-rapport-underkanner-1177-s-digitala-losning-platform24)) | triaj lansat la scară fără certificare | triajul e dispozitiv medical |

### 4.5 România și Europa Centrală și de Est

| Companie | Ce face | Tracțiune sau preț (calitate) | Relevanța pentru fondator |
|---|---|---|---|
| **MedLife** | lider privat; portal self-service pentru angajatori cu statusul MM; MM Express; asistent AI în aplicație | €630M venit pro-forma 2025 (V) ([MedLife](https://www.medlife.ro/comunicat-de-presa/medlife-atinge-630-milioane-eur-cifra-de-afaceri-pro-forma-2025-si-continua)); ~800k angajați abonați (C); a cumpărat Medicris Oradea (22k+ abonați) și SanoPass | **concurentul direct** al cabinetelor MM independente; nu e client |
| **Regina Maria** (Mehiläinen) | rețea; aplicație cu 10+ ani de istoric; laborator cu autoverificare AI | ~3,0 mld lei în 2025 (V, presă) ([Economedia](https://economedia.ro/piata-serviciilor-medicale-private-continua-sa-creasca.html)); 780–850k abonamente (C) | IT centralizat; posibil partener mai târziu |
| **Medicover / Synevo** | clinici, Spitalul Pelican (80%), laboratoare; Medicover Tech SRL | >1,6 mld lei în 2025 (V, presă) ([ZF](https://www.zf.ro/companii/primele-rezultate-serviciile-medicale-private-grupul-suedez-23059255)) | IT în casă |
| **Docbook** | marketplace de programări | ~7.500 de medici; 500k+ programări între 2018 și mijlocul lui 2023 (C) ([Forbes.ro](https://www.forbes.ro/peste-500-000-de-programari-online-la-medici-prin-platforma-docbook-77-dintre-pacienti-sunt-atenti-la-recenzii-405930)) | fără API public |
| **Medicai** (Cluj) | PACS în cloud, API REST + SDK | 70 de clienți (C) ([Business Forum](https://www.businessforum.ro/industry/20250807/medicai-a-romanian-health-tech-startup-expands-in-the-us-2164)) | **reperul realist pentru o firmă românească mică de software medical B2B** |
| **MedOcean** | analiza apelurilor din clinici | 100k+ apeluri analizate; țintă de 100 de clienți (C) ([AGERPRES](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680)) | clinicile plătesc pentru unelte de front-office |
| **Callio** (Timișoara) | agent vocal la recepția clinicilor dentare | €139/189/299 pe lună (C); pilotul Hub of Smiles ([start-up.ro](https://start-up.ro/callio-agentul-vocal-ai-care-preia-telefonul-receptiei-din-clinicile-stomatologice)) | ancoră de preț |
| **iStoma** (iDava) | program pentru clinici dentare | 5.300 de stomatologi (C) ([ZF](https://www.zf.ro/zf-it-generation/zf-it-generation-ionut-botorogeanu-fondator-ceo-idava-solutions-22322427)) | posibilă țintă de integrare |
| **BizMedica** (Setrio) | medicină de familie și modul MM (fișa de aptitudine, import Excel) | 159–199 RON/lună pentru medicina de familie (C, preț vechi) ([Setrio](https://setrio.ro/medicina-muncii/)) | **cel care ar copia primul** |
| **MedExam, Qmedical, Charisma, MedSoft** | software pentru medicina muncii | fără prețuri publicate | de verificat dacă au portal pentru angajator |
| **SanoPass** | platformă de acces la prevenție | seed €400k + €850k; preluată majoritar de MedLife (V, presă) ([The Diplomat](https://www.thediplomat.ro/?p=21719)) | **singura ieșire românească documentată** |
| **Heymedica** (Alba Iulia) | marketplace european de furnizori | ~500k indexări (C); finanțare raportată contradictoriu | — |

### Ce se transferă și ce nu

**Primul tipar: penele care au crescut se lipesc de sistemul de evidență existent.** Accurx a pornit de pe desktopul medicului de familie, Lifen intră direct în dosarul electronic al spitalului, Lighthouse se leagă de programul cabinetului dentar. Fiecare deține un tip de mesaj frecvent și adaugă module pe același flux, pentru același cumpărător. Distribuția devine șanțul de apărare: Accurx revinde azi AI-ul altora [Emergent puternic].

**Al doilea tipar: ieșirile mici, documentate, au mers către cumpărători cu distribuție în aceeași nișă.** Kaiku a fost cumpărată de Elekta (radioterapie), Luscii de OMRON (tensiometre), Validic de ChartSpan (servicii de îngrijire cronică). Pentru un fondator român, ieșirea realistă e vânzarea către un vendor regional de software, o rețea medie sau un distribuitor care vinde deja acelorași clinici. Notele nu au găsit însă cumpărători români activi de module healthtech, în afară de MedLife cu SanoPass [Plauzibil].

**Al treilea tipar: finanțarea nu e dovadă de succes.** Huma a obținut clasa IIb și a strâns peste $80M, apoi a concediat. Biofourmis a fost unicorn și a concediat 120 de oameni. Weave e pe pierdere la $239M venit, Doctolib pierdea €54M în 2024 [Stabilit].

**Ce nu se transferă în România:**
- afacerile RPM din SUA construite pe codurile Medicare (~$26–52 pe cod, pe pacient, pe lună);
- extragerea de dosare în rețelele americane;
- scribii vânduți prin Epic;
- abonamentele de analize direct la consumator, pentru că în România laboratoarele sunt chiar mărcile de consum.

**Ce se transferă, la prețuri mai mici:**
- rechemarea și mesajele plătite de clinică;
- rutarea documentelor și a rezultatelor;
- B2B2C prin asigurător sau angajator.

**Ancorele de preț pentru România:**
- MediNote, ~50 lei pe utilizator pe lună ([MediNote](https://medinote.ro/soft-medical));
- agenții vocali, 139–499 €;
- ipoteza de lucru din note pentru rechemare: **20–60 € pe locație pe lună, plus SMS la cost** [Plauzibil].

## 5. Piața românească: plătitorul e angajatorul, nu statul

### Trei grupuri mari și o coadă lungă de independenți

**Piața privată e consolidată în jurul a trei grupuri:**
- **MedLife:** ~3,17 mld lei (≈ €630M) venit pro-forma în 2025, +17% ([MedLife](https://www.medlife.ro/comunicat-de-presa/medlife-atinge-630-milioane-eur-cifra-de-afaceri-pro-forma-2025-si-continua));
- **Regina Maria:** ~3,0 mld lei în 2025 (alte surse dau peste 2 mld lei în 2023) ([Economedia](https://economedia.ro/piata-serviciilor-medicale-private-continua-sa-creasca.html)). E cumpărată acum de finlandezii de la Mehiläinen, tranzacție încheiată în decembrie 2025 ([Profit.ro](https://www.profit.ro/povesti-cu-profit/ultima-ora-regina-maria-vanduta-finlandezii-s-au-obligat-sa-plafoneze-preturile-din-bucuresti-brasov-si-constanta-la-unele-servicii-in-anumite-conditii-tranzactie-finalizata-22282893));
- **Medicover cu Synevo:** peste 1,6 mld lei în 2025 ([ZF](https://www.zf.ro/companii/primele-rezultate-serviciile-medicale-private-grupul-suedez-23059255)) [Stabilit].

Medicover are chiar o filială tehnică românească, Medicover Tech SRL ([Risco](https://www.risco.ro/en/verifica-firma/medicover-tech-cui-42402275)). **Marile rețele își construiesc software-ul în casă și decid IT-ul central.** Sunt parteneri sau cumpărători mai târziu, nu primii clienți [Plauzibil].

**Contextul de finanțare:**
- România cheltuie **5,8% din PIB** pe sănătate, față de 10% în UE.
- Cheltuiala pe locuitor e cea mai mică din UE.
- Partea privată (23%) e aproape toată plătită din buzunar.
- Asistența primară primea doar **10%** din cheltuială în 2022 ([Romania Insider/State of Health 2025](https://www.romania-insider.com/eu-state-of-health-ro-dec-2025)) [Stabilit].
- Asigurările private de sănătate sunt mici, dar cresc: **756 mil. lei prime brute în S1 2026** (+10%), cu Groupama lider ([1asig](https://www.1asig.ro/TOP-asigurari-de-sanatate-in-S1-2026-GROUPAMA-devine-lider-iar-piata-urca-la-756-mil-lei-articol-100-75256.htm)).

### Digitalizarea e în urmă, iar procesele sunt pe telefon și WhatsApp

**Pacienții folosesc puțin canalele digitale.** Doar **~10%** dintre români și-au făcut o programare online sau și-au accesat dosarul în 2024 ([OECD](https://www.oecd.org/en/publications/oecd-reviews-of-health-systems-romania-2025_f52e4a98-en/full-report/access-and-quality-of-care-in-romania-s-healthcare-system_31f62789.html)). Competențele digitale de bază sunt de **31,8%**, ultimul loc în UE ([Romania Insider](https://www.romania-insider.com/eurostat-basic-digital-skills-ro-ranks-last-apr-2026)).

**Sistemul public recuperează repede.** Indicatorul eHealth din Digital Decade a fost **75 față de 83 media UE**, cu +17 puncte, una dintre cele mai mari creșteri ([Euronews](https://www.euronews.com/health/2026/02/23/digital-health-across-europe-which-country-leads-acess-to-electronic-health-records-and-li)) [Emergent puternic].

**Firmele adoptă puțină tehnologie.** Doar 5,2% dintre firmele cu peste 10 angajați folosesc AI, ultimul loc în UE, iar 13,93% folosesc un CRM ([Eurostat](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2)).

**În clinici, telefonul domină.** Datele unui vânzător (MedOcean), pe 100.000+ apeluri, arată că **39,6%** dintre cei care sună pentru o programare nouă închid fără ea ([AGERPRES](https://agerpres.ro/comunicate/2026/01/30/comunicat-de-presa---medocean--1523680)). Clinicile au primit amenzi ANSPDCP pentru că au trimis date ale pacienților pe WhatsApp sau pe e-mail ([e-juridic](https://e-juridic.manager.ro/articole/centre-medicale-private-amendate-pentru-incalcarea-gdpr-datele-pacientilor-divulgate-fara-drept-pe-whatsapp-sau-prin-e-mail-29342.html)). Managerii de spital descriu dosarul electronic drept „închis” și nefuncțional ([PMC12563242](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563242/)).

**Ce nu s-a găsit în România:** nicio măsurătoare a ratelor de neprezentare, a rechemărilor sau a urmării rezultatelor anormale. Acestea sunt goluri de proces **plauzibile, dar nemăsurate**.

### Vendorii: mulți, mici și fără API public

**Software de clinică:**
- **MediNote:** program de cabinet în cloud, cu SMS inclus, la 50 lei pe utilizator pe lună ([MediNote](https://medinote.ro/soft-medical)).
- **BizMedica** (Setrio): 159–199 RON pe lună, preț vechi ([Setrio](https://setrio.ro/en/family-medicine/)).
- **iStoma:** 5.300 de stomatologi declarați ([ZF](https://www.zf.ro/zf-it-generation/zf-it-generation-ionut-botorogeanu-fondator-ceo-idava-solutions-22322427)).
- **icMED:** integrări cu SIUI, rețeta electronică și e-Factura ([icMED](https://icmed.ro/indexen.html)).
- **Zarina CRM:** licență unică de €2.990, preț de pe blogul pentru CRM-ul general ([Zarina](https://www.zarinacrm.ro/cel-mai-bun-crm-2026/)).

**Software de spital:** Hipocrate (RSC), InfoWorld și Softeh, după un sondaj din 2016. Atacul ransomware din februarie 2024 asupra RSC/Hipocrate a afectat **26 de spitale** ([DNSC](https://www.dnsc.ro/citeste/alert-backmydata-ransomware-spitale-romania)).

**În afară de Medicai (imagistică), niciun vendor nu are un API public documentat** [Stabilit pentru ce s-a găsit]. Integrarea înseamnă în practică exporturi CSV/Excel, PDF, e-mail și parteneriate negociate cu fiecare vendor. Documentul tehnic de la Fundeni (aprilie 2026) acceptă trei căi de transmitere a rezultatelor de laborator: **CSV, introducere manuală sau API** ([ICF Fundeni](https://icfundeni.ro/wp-content/uploads/2026/04/Anexa-nr.-2_Transmiterea-datelor_signed.pdf)). Asta arată cum se specifică proiectele reale.

**Medicina muncii nu e teren gol.** Cel puțin șase produse emit fișa de aptitudine:
- BizMedica MM, care importă și listele de angajați din Excel ([Setrio](https://setrio.ro/medicina-muncii/));
- MedExam ([DMV Consult](https://dmvconsult.ro/medicina-muncii));
- Qmedical;
- modulul Charisma;
- modulul MedSoft;
- Tempomed.

**Nimeni nu publică prețuri sau API-uri.** Golul nu e programul care tipărește fișa, ci partea angajatorului: cine e scadent, cine îi sună pe oameni, cine urmărește recomandările. MedLife vinde exact asta prin portalul self-service ([MedLife](https://www.medlife.ro/self-service)) [Plauzibil].

### Interoperabilitatea: CNAS publică specificații, dar nu oferă date terților

**Raportarea și rețeta electronică.** CNAS publică specificațiile de interfațare PIAS pentru producătorii de software, ultima versiune fiind **v3.7.32 din 7.04.2026** ([CNAS PIAS](https://portal.cnas.ro/cnas/pias/specificatii)). Accesul se face cu certificatele digitale ale furnizorului medical. Aplicația de rețetă trebuie „înregistrată în sistemul CNAS”. Integrarea nu dă vendorului niciun drept asupra datelor.

**Portalul e-SănătateaMea**, lansat pe **1 septembrie 2026** cu ~€100M din PNRR, arată pacientului istoricul, rețetele, trimiterile și serviciile decontate. **Programarea online prin el devine obligatorie pentru furnizorii cu contract CNAS din T4 2026** ([Tele7abc](https://tele7abc.ro/e-sanatatea-mea-portalul-cnas-pentru-dosarul-medical-digital-lansat-pe-1-septembrie-2026/); [medic24](https://medic24.ro/portalul-esanatateamea-ajunge-la-promulgare-programari-online-din-trimestrul-iv/)). Din aceeași dată, biletele de trimitere și scrisorile medicale emise în programe terțe trebuie să ajungă în portal prin specificațiile SIUI ([Alba24](https://alba24.ro/cnas-de-la-1-septembrie-formularele-medicale-vor-fi-disponibile-in-esanatateamea-ce-trebuie-sa-faca-furnizorii-de-servicii-1155597.html)).

**Nu s-a găsit niciun API care să permită citirea datelor de către terți.** Consultațiile private plătite din buzunar probabil nu ajung în dosarul național [Plauzibil]. Concluzia: e-SănătateaMea e o **suprafață de conformitate** pentru clienții cu contract CNAS, nu o sursă de date pentru predicție.

**Spitalele publice** se digitalizează prin investiția PNRR I3.3, cu maximum €1M per spital județean ([europenefonduri.eu](https://europenefonduri.eu/finantari/digitalizarea-spitalelor-pnrr-investitia-specifica-i3-3-investitii-in-sistemele-informatice-si-in-infrastructura-digitala-a-unitatilor-sanitare-publice/)).

**Pregătirea României pentru EHDS nu a putut fi verificată:** autoritatea de sănătate digitală, organismul de acces la date (HDAB), profilurile FHIR naționale.

**Lecția din Finlanda.** Conectarea obligatorie la Kanta, plus un lanț de certificare (testare gratuită la Kela, audit de securitate plătit, registrul public al sistemelor), a creat o piață pentru vendori și pentru intermediarii care conectează lanțuri întregi de clinici ([Kanta](https://www.kanta.fi/en/system-developers/certification-and-key-requirements)). România nu are încă nici API-ul, nici lanțul de certificare care ar face posibil un astfel de intermediar [Plauzibil].

### Plătitorii: cine plătește azi pentru prevenție

| Plătitor | Ce plătește | Cifre | Ce înseamnă pentru software |
|---|---|---|---|
| **Angajatorii, prin medicina muncii** | examene obligatorii la angajare, periodice și la reluarea muncii (HG 355/2007) | 80 lei/angajat/an, 110 lei pentru șoferi ([Medworks](https://medworks.ro/medicina-muncii-bucuresti/)); 5,76M salariați; cheltuială teoretică de **460–630 mil. lei/an la nivel național** și **15–21 mil. lei/an în Bihor** (calculul cercetătorului, presupunând respectarea integrală) | **cel mai accesibil contact preventiv recurent**; marje mici la furnizor |
| **Angajatorii, prin abonamente** | abonamente medicale scutite de taxe până la **€400/persoană/an**, în limita a 33% din salariul de bază ([Fiscalitatea.ro](https://www.fiscalitatea.ro/abonamentul-medical-incheiat-direct-de-salariat-cu-centrul-medical-cum-il-poate-deconta-angajatorul-si-ce-taxe-se-aplica-24930/)) | „2,2M beneficiari, piață de peste €250M”, dintr-un advertorial, sursă slabă ([Wall-Street.ro](https://www.wall-street.ro/articol/sanatate/enayati-medical-city-lanseaza-abonamentele-aniversare-corporate.html)); MedLife ~800k, Regina Maria 780–850k (C) | dominat de rețele; software-ul trebuie să coste o fracțiune dintr-un abonament |
| **Asigurătorii privați** | polițe de sănătate, pachete de analize (NN la Regina Maria) ([NN](https://www.nn.ro/sites/default/files/2025-03/GhidRM_EnergieSiVitalitate_mar2025.pdf)) | 756 mil. lei în S1 2026 | piață mică; acces greu fără rețea |
| **CNAS: pachetul de prevenție** | din februarie 2026, serviciile de prevenție sunt gratuite pentru oricine e înscris la un medic de familie; la 40+, până la 3 consultații în 6 luni; la 60+, și evaluarea osteoporozei, a incontinenței și a demenței ([Capital](https://www.capital.ro/cnas-actualizeaza-ghidul-asiguratului-si-detaliaza-serviciile-medicale-gratuite-de-preventie-consultatiile-pot-fi-accesate-si-de-persoanele-neasigurate.html)) | plata pe serviciu pentru medic **necunoscută**; medicul de familie e plătit pe listă | cumpărătorul (medicul de familie) are buget mic |
| **Programele de screening finanțate de UE** | ROCCAS 4 Nord-Vest, inclusiv Bihor: 2025–2029, 35,6 mil. lei, 24.156 de teste FIT, 1.328 de colonoscopii ([Digenio](https://digenio.ro/proiect-regional-de-screening-al-cancerului-de-colon-lansat-la-cluj-prof-dr-marcel-tantau-exista-tot-mai-mult-cancer-care-coboara-sub-50-de-ani/)) | bugete fixate în 2025, cu reguli UE de achiziție | doar ca subcontractor, cu un singur cumpărător |
| **Statul, pentru produse digitale** | — | nicio cale de rambursare digitală (de tip DiGA) găsită | nu există plătitor pentru RPM sau pentru aplicații |

**Golul de screening e real, dar nu e o piață de software.** Doar **6,2%** dintre femeile eligibile au făcut screening cervical, cel mai puțin din UE ([TVR Info](https://tvrinfo.ro/romania-fara-niciun-program-national/)). CNAS a decontat în anul raportat doar **263** de servicii de screening cervical prin spitalizare de zi, iar 36 de județe n-au avut niciunul ([PressOne](https://pressone.ro/exclusiv-in-zeci-de-judete-din-romania-statul-nu-deconteaza-servicii-esentiale-pentru-sanatatea-femeilor-lista-oraselor-mari-unde-nu-s-a-facut-nicio-investigatie-pentru-depistarea-cancerelor-de-san)). Golul vine din finanțarea publică și din capacitate, nu din lipsa software-ului [Plauzibil].

**Ecosistemul de startup-uri trăiește din granturi.** Tracxn numără 356 de startup-uri healthtech în România, dintre care 45 finanțate și 15 ajunse la Series A sau mai departe ([Tracxn](https://tracxn.com/d/explore/healthtech-startups-in-romania/__BuNQoA9qXCPoTqXX3KpFNfbIizmugJvffBGl20WNRPs/companies)). EIT Health clasează România ca ecosistem „experimentator”: bun la granturi, slab la capital privat ([Startups n the City](https://startupsnthecity.com/seven-years-of-eit-health-presence-in-the-romanian-healthtech-ecosystem/)).

**Încrederea în AI e o constrângere reală.** 32% dintre români s-ar simți trădați dacă explicațiile analizelor ar fi scrise de AI ([StartupCafe/MKOR](https://startupcafe.ro/jumatate-romani-nu-recunosc-text-inteligenta-artificiala-studiu-107187)).

### București, Cluj, Timișoara: centrele de decizie și reperele

**București** e locul unde se decide IT-ul rețelelor (MedLife, Regina Maria, Medicover) și unde lucrează vendorii de software de clinică și de spital. E și reperul de preț pentru medicina muncii: Medworks cere 80 lei pe angajat pe an. Rețeaua fondatorului de aici contează pentru Q (componentele EHDS vândute vendorilor) și pentru vânzarea la distanță către firmele MM mai mari.

**Cluj:**
- Medexpert declară peste 15.000 de angajați evaluați pe an și peste 500 de firme ([Medexpert](https://mcmedexpert.ro/medicina-muncii/));
- Medicai e reperul unui vendor românesc mic de software medical;
- ROCCAS 4 Nord-Vest a fost lansat de la Cluj.

**Timișoara:**
- Bioclinica a fost fondată aici;
- Callio și-a făcut pilotul la Hub of Smiles;
- icMED are prefix telefonic de Timiș;
- Consiliul Județean Timiș publică anual caiete de sarcini pentru serviciile MM ([CJ Timiș 2026](https://www.cjtimis.ro/wp-content/uploads/2020/07/Caiet-de-sarcini-MM-2026.pdf)). Acestea arată regulile examenului de reluare: după cel puțin 90 de zile de absență medicală sau 6 luni din alt motiv, în 7 zile de la reluare.

### Oradea și Bihor: organizațiile verificabile public

**Despre proprietate.** Proprietatea organizațiilor „aparent independente” **n-a fost verificată** în registre (ONRC, Termene); trebuie verificată înainte de vizită. Bihor are **187,3k salariați** ([INS](https://bistrita.insse.ro/wp-content/uploads/2025/09/28_Forta-de-munca_iunie_25.pdf)), al doilea județ din Nord-Vest după Cluj.

| Organizație | Ce este | Cine decide IT-ul | Relevanța pentru fondator |
|---|---|---|---|
| Spitalul Clinic Pelican (Medicover 80% din 2018; 244 de paturi; contract CAS; secție MM) ([ZF](https://www.zf.ro/companii/medicover-cumpara-spitalul-pelican-din-oradea-intr-o-tranzactie-de-23-mil-euro-17216243)) | spital privat | grupul Medicover | referință, nu client |
| Medicris Oradea (cumpărat de MedLife în 2022; 22k+ abonați MM) ([MedLife](https://www.medlife.ro/comunicat-de-presa/medlife-bifeaza-o-noua-tranzactie-la-oradea)); MedLife Ronald Reagan (MM, examene pentru șoferi) ([MedLife](https://www.medlife.ro/clinica-medlife-ronald-reagan)); MedLife Hyperclinica; laboratorul MedLife Genesys (ISO 15189) | rețea | central | **concurentul direct** pe MM |
| Regina Maria Oradea: centru MM, clinică dentară, punct de recoltare ([Regina Maria](https://www.reginamaria.ro/clinici/centru-de-medicina-muncii-oradea)) | rețea | central | concurent |
| Affidea Hiperdia Oradea (RMN); Medima Oradea (RMN și CT, 2025, €1,6M) ([ZF](https://www.zf.ro/zf-24/reteaua-de-clinici-de-imagistica-medima-a-deschis-o-noua-unitate-la-22798460)) | imagistică în rețea | central | nu |
| **Medimun SRL** ([medimun.ro](https://www.medimun.ro/)), **Carimed Center** (examene la sediul angajatorilor) ([Carimed](https://carimedcenter.ro/despre-noi/)), **Clinica Endodigest** ([Sfatul Medicului](https://www.sfatulmedicului.ro/clinici/medicina_muncii-oradea)), Alfa Medica, Gecoprosana ([Pagini Aurii](https://www.paginiaurii.ro/firmy/ORADEA/q_medicina+muncii/1/)), Neoklinik | cabinete și firme MM aparent independente | local, de verificat | **primii clienți țintă pentru produsul recomandat** |
| **GrandMed** (diabet, cardiologie, endocrinologie; contract CAS) ([GrandMed](https://www.grandmed.ro/)), **NewMedics** ([NewMedics](https://oradea.clinica-newmedics.ro/)), Medena, Spitalul Ovidius | clinici aparent independente | local, de verificat | candidați pentru „controale pierdute” |
| **Humanamed** (laborator din 2003, contract CAS) ([Sfatul Medicului](https://www.sfatulmedicului.ro/arhiva-medicala/laboratoare-de-analize-medicale-oradea-pagina_5)) | singurul laborator independent găsit | local | partener posibil pentru „ziua de prevenție” |
| Dental-Art, MaxiloMED, LifeDent, Estetical Dentis, German Dental (își fac reclamă la pacienți străini) ([Dental-Art](https://dental-art.ro/en/dental-tourism/)); Dr. Leahu (rețea) | clinici dentare | local / rețea | turism dentar (K) |
| Spitalul Clinic Județean de Urgență Bihor: proiect PNRR (7 clădiri, termen august 2026) ([Oradea.ro](https://oradea.ro/stiri/spitalul-clinic-judetean-de-urgenta-bihor-va-implementa-un-sistem-informatic-de-nivel-inalt)); investiții de 73 mil. lei în 2025 ([Agerpres](https://agerpres.ro/sanatate/2026/03/16/bihor-investitii-de-peste-73-de-milioane-de-lei-la-spitalul-clinic-judetean-din-oradea-in-anul-2025--1537848)); programări pentru screeningul cervical | spital public | achiziții publice | nu ca prim client |
| „Spitalul Clinic Avram Iancu Oradea” (pe lista PNRR) | identitate neconfirmată | — | de verificat |
| ROCCAS 4 Nord-Vest (Bihor inclus) | consorțiu de screening colorectal | consorțiu | doar subcontractare oportunistă |
| Caritas Eparhial Oradea (îngrijire la domiciliu, pe o listă din 2015); DASO Oradea | social | — | căminele private nu sunt verificate |
| ADLO/CRESC Oradea Mare (preincubare; apelul nr. 8 a expirat pe 04.10.2026); Oradea Tech Hub; Universitatea din Oradea (DIH4Society) ([UO](https://www.uoradea.ro/wp-content/uploads/2026/05/Comunicat_de_Presa_Partener-UO_-DIH4Society_Conferinta-finala-28-Mai-2026.pdf)) | ecosistem | — | granturi și parteneriate; Facultatea de Medicină n-a fost verificată |

**Alte cifre locale, de tratat cu prudență:**
- **Turismul dentar** din Oradea se sprijină pe un preț al implantului de ~€400–450, față de €560–600 în Ungaria. Metodologia comparației nu e clară ([Stomatologo](https://stomatologo.ro/articole/cum-se-situeaza-romania-pe-harta-turismului-stomatologic-european-in-2026)).
- **Firmele dentare din Bihor** ar fi 732, conform unei note anterioare care nu a fost reverificată ([Termene.ro](https://termene.ro/articole/afacerile-stomatologice-din-romania)).
- **Bioclinica** are o prezență în Oradea care rămâne neconfirmată.

### Golurile vizibile și cauza lor

Un gol de piață nu e automat o oportunitate. Tabelul de mai jos atribuie fiecărui gol cauza cea mai probabilă, după note.

| Golul observat | Concurență slabă? | Cerere scăzută? | Lipsă de date? | Rambursare? | Reglementare? | Concluzie |
|---|---|---|---|---|---|---|
| Programele de clinică n-au API public | da (vendori mici) | da (clinicile nu cer) | informații lipsă | — | — | nu e o oportunitate în sine; integrarea se face prin exporturi |
| Portalul pentru angajator al cabinetelor MM independente | **da, dacă vendorii nu-l au (de verificat)** | parțial (MedLife arată cerere la rețele) | — | — | mică (ce vede angajatorul) | **oportunitatea A**, condiționată de verificare |
| Urmarea rezultatelor anormale și a controalelor („bucla laborator → medic → rechemare”) | da pentru independenți | **nedovedită** în România | **nemăsurat** | CNAS nu plătește coordonarea | graniță MDR/IVDR dacă interpretează | oportunitatea G, cu audit înainte |
| Acoperirea screeningului (6,2% cervical) | — | da (participare mică) | parțial | **da: finanțare publică slabă** | — | nu e piață de software; doar subcontractare |
| Rechemarea pentru pachetul CNAS 40+/60+ | da | cumpărătorul n-are motiv financiar | — | **da: plata pe listă, nu pe serviciu** | — | H, slabă până se clarifică plata |
| RPM și telemonitorizare | da | — | — | **da: nicio rambursare** | **da: alertele sunt IIa** | de evitat |
| Aplicații și PHR pentru consumator | — | **da (10% online, 31,8% competențe)** | — | — | — | de evitat |
| Acces terț la e-SănătateaMea | — | — | **da: niciun API** | — | infrastructura statului | de evitat până apare API |
| Modele predictive pe date românești | — | — | **da: fără acces, fără HDAB înainte de ~2029** | — | **da: profilare, MDR** | etapa 4, cu parteneri |
| Software pentru cămine și îngrijire la domiciliu | da | bugete mici (îngrijirea de lungă durată = 5,6% din cheltuiala curentă) ([INSSE](https://insse.ro/cms/sites/default/files/com_presa/com_pdf/scs2023e.pdf)) | piață neverificată | da | mică | slabă |
| Rezultate livrate de laboratoarele independente | — | — | — | — | — | **structural: laboratoarele sunt ale rețelelor**; în Oradea, doar unul independent |
| Componente EHDS pentru vendori | da | **amânată până în 2027–2028** | — | — | da (termene 2029/2031; reguli românești lipsă) | Q, opțiune cu termen |
| Scrib AI în română | **nu: concurență globală finanțată** | — | — | — | alunecare spre IIa | de evitat |
| Rechemare dentară | **nu: VAstoma, DentAIM, Callio, iStoma** | — | — | — | — | marfă |

## 6. Baza de oportunități: 29 de idei scorate și filtrate după dependențele fatale

Baza vine din `analiza_founder.md` și `founder-sanatate/scoring/`. Cele 26 de idei din analiza laterală au fost completate cu 4 variante noi. Mai jos sunt 29 de rânduri, fiindcă O24 (auditul „bani expuși”) e o unealtă de vânzare, nu o afacere. **Notele 1–5 sunt estimări sprijinite pe note, nu măsurători.** Rundele „bulletproof” au corectat ulterior cifrele financiare ale lui A, nu scorurile. Scorarea rămâne un filtru de prioritate, nu o dovadă.

### Ponderile și de ce așa

Fiecare criteriu e notat de la 1 la 5, cu 5 = favorabil fondatorului. La criteriile negative, 5 înseamnă „puțin” sau „ușor”. Scorul total = Σ(pondere × notă) / 5, deci variază între 20 și 100. Ponderile urmează obiectivul declarat: **bani recurenți repede, cu 10–12 ore pe săptămână, și abia apoi drumul strategic**.

| Criteriu | Pondere | De ce |
|---|---:|---|
| Urgența reală la client | 10 | fără o durere urgentă nu se cumpără în 90 de zile |
| Capacitatea de plată | 10 | România are cea mai mică cheltuială de sănătate pe locuitor din UE; toate fundăturile cer un plătitor nou |
| Achiziția clienților (5 = ușoară) | 10 | la 10–12 h/săpt, un canal scump omoară produsul |
| Accesul la date | 8 | ucigașul cel mai frecvent: fondatorul poate fi doar persoană împuternicită, iar programele n-au API |
| Potențialul de venit recurent | 8 | preferința explicită pentru B2B SaaS |
| Relevanța strategică pentru sănătatea predictivă | 8 | al doilea obiectiv; contează după „bani acum” |
| Oportunitatea în România și Bihor | 6 | primii clienți trebuie să fie la distanță de mers cu mașina |
| Complexitatea de reglementare (5 = mică) | 6 | clasa IIa costă ~32–110k € (cazurile extreme le prinde și flagul) |
| Fezabilitatea ca dezvoltator solo | 6 | fondator singur, cu timp limitat |
| Forța diferențierii | 6 | altfel concurezi cu funcții incluse gratuit în programele existente |
| Concurența (5 = puțină) | 5 | o piață goală poate însemna lipsă de cerere |
| Nevoia de parteneriate clinice (5 = deloc) | 4 | accesul la medici e limitat |
| Efortul pentru MVP (5 = mic) | 4 | MVP-ul trebuie să încapă în ~2–3 luni |
| Dependența de platforme terțe (5 = mică) | 3 | exporturile și WhatsApp sunt riscuri, dar se pot ocoli |
| Potențialul internațional | 2 | o întrebare pentru anul 3+ |
| Dificultatea tehnică (5 = ușor) | 2 | fondatorul e puternic tehnic |
| Capitalul de pornire (5 = mic) | 2 | 25k € ajung pentru un produs administrativ |

**Flagul de dependență fatală** exclude ideea ca prim produs, oricât de mare ar fi scorul (⛔), dacă e prezentă cel puțin una dintre condiții:
- **date:** datele nu sunt accesibile fondatorului;
- **validare:** e nevoie de MDR IIa+ (inaccesibil ca bani și timp);
- **plătitor:** nu există unul;
- **integrare:** depinde de un API care nu există;
- **cumpărător unic:** există un singur cumpărător sau un canal blocat de un singur actor.

Avertismentul (⚠) marchează o condiție care trebuie verificată în validare. Dacă testul iese negativ, devine fatal.

### Clasamentul

| Loc | Cod | Oportunitate | Cine plătește | Scor /100 | Flag | Ce o ridică / ce o coboară |
|---:|---|---|---|---:|---|---|
| 1 | A | Scadențar MM + partea angajatorului + registrul recomandărilor (după corectură: **birou de continuitate**) | cabinete MM independente | **73,4** | ⚠ plata și exportul neverificate | serviciu obligatoriu, recurent, plătit de angajator; categoria 1 / programul MM există deja, plafon local mic |
| 2 | G | Bucle deschise la clinicile cronice independente: controale scadente, rezultate anormale, trimiteri | clinici cronice | 68,4 | ⚠ export fără API; consimțământ pentru SMS | cel mai aproape de prevenție / încredere, integrare |
| 3 | B | Scadențar MM vândut direct HR-ului | angajatori | 67,2 | ⚠ plata HR-ului nedovedită; Excel gratuit | nu cere nimic de la nimeni / Excel e substitutul gratuit; slab strategic |
| 4 | K | Urmărirea pacienților de turism dentar (Oradea) | clinici dentare | 64,6 | ⚠ volum necunoscut | pacienți străini / rechemarea dentară e aglomerată; nu duce spre predictiv |
| 5 | H | Rechemarea pentru pachetul CNAS 40+/60+ | medici de familie | 63,2 | ⚠ plata CNAS pe serviciu necunoscută | program național din 2026 / cumpărătorul n-are bani |
| 6 | J | Navigator după o notificare de la ceas | clinici de cardiologie | 63,2 | ⚠ penetrarea wearable-urilor necunoscută | nimeni nu face asta / probabil doar un modul |
| 7 | Q | Componente EHDS (fațadă FHIR, IPS, jurnal) pentru vendorii locali | vendori de software medical | 63,2 | ⚠ venit realist abia în 2027–2028 | date sintetice, fără parteneri clinici / cumpărătorii amână |
| 8 | L | Remindere și reducerea absențelor, cu grup de control | clinici private, stomatologie | 62,8 | — | efect dovedit / marfă, piață aglomerată |
| 9 | R | Jurnal de acces și cereri de acces la dosar | clinici private | 60,0 | — | amenzi reale / se cumpără doar după amendă |
| 10 | D | Arhiva longitudinală de expunere profesională | furnizori MM, angajatori industriali | 59,8 | ⚠ numărul de lucrători expuși necunoscut | singurul activ de date longitudinal cu bază legală clară / piață mică |
| 11 | Z | Dispecerat de capacitate pentru campanii de invitații | clinici de endoscopie și imagistică | 59,2 | ⚠ campanii rare | mai bun ca modul |
| 12 | C | „Ziua de prevenție” la locul de muncă | furnizor MM / angajator | 58,8 | ⚠ apetit neverificat; laborator partener | dovada ACCESS / depinde de parteneri |
| 13 | M | Raport de finalizare a prevenției pentru abonamentele corporate | clinici medii | 58,8 | ⚠ cererea angajatorilor negăsită | — |
| 14 | F | Inbox pentru rezultatele în afara intervalului | laboratoare independente | 58,4 | ⚠ un singur laborator independent în Bihor | strategic / fără clienți locali |
| 15 | S | PDF-uri vechi → tabel de valori pentru medic | clinici cu check-up | 57,6 | ⚠ răspundere sub PLD pentru erorile de extracție | — |
| 16 | AB | Jurnal de evenimente și escaladare pentru cămine | cămine, agenții de îngrijire | 57,0 | ⚠ piață neverificată | bugete mici |
| 17 | N | Meniu fix de prevenție bazată pe dovezi, în bugetul de €400 | angajator, prin clinici | 56,8 | ⚠ laborator și medic partener; regim fiscal | axa „curatoriat” |
| 18 | I | Urmărirea biletelor de trimitere | medici de familie | 55,4 | ⚠ plata incertă | — |
| 19 | W | Check-in administrativ după chirurgia de zi | clinici de chirurgie de zi | 52,0 | ⚠ la granița triajului | — |
| 20 | AD | Coordonator pentru părinții familiilor din diaspora (B2C) | familia | 50,8 | ⚠ B2C, serviciu cu om | — |
| excl. | E | Navigator FIT pozitiv → colonoscopie pentru ROCCAS 4 NV | consorțiu (subcontract) | 57,0 | ⛔ un singur cumpărător, achiziții UE | cea mai bună dovadă de efect; doar oportunist |
| excl. | U | Predicția buclelor care nu se închid, ca prim produs | clienții A, G, H | 54,2 | ⛔ istoricul nu există; profilare | etapa a doua |
| excl. | O | Auditul „pauza” (dez-implementare) pentru asigurători | asigurători | 51,4 | ⛔ fără date de daune și fără rețea | axă nouă, dar inaccesibilă |
| excl. | AC | Predarea la pensionare: ultimul examen MM → medicul de familie | neclar | 51,2 | ⛔ niciun plătitor | — |
| excl. | AA | Monitorizarea locală a AI-ului marcat CE | rețele de imagistică | 51,0 | ⛔ niciun utilizator român găsit | opțiune pentru 2028+ |
| excl. | Y | Platformă pentru programe de prevenție a diabetului | angajatori, clinici de nutriție | 50,8 | ⛔ niciun plătitor găsit | — |
| excl. | P | Punte spre e-SănătateaMea pentru furnizorii mici cu contract CNAS | furnizori CNAS | 49,0 | ⛔ niciun API public | — |
| excl. | T | RPM pentru un program privat de hipertensiune, cu alerte | clinici | 45,4 | ⛔ alertele = IIa; nicio rambursare | — |
| excl. | V | Scor de risc individual (SCORE2/FINDRISC) sau model propriu | medici | 45,4 | ⛔ MDSW IIa, fără excepție de suport decizional în UE | — |

### Lanțul de valoare al primelor idei: de la problemă la extindere

| Cod | Problema → cumpărătorul | Datele care se pot folosi | Software-ul → valoarea măsurabilă | Achiziția → venitul | Apărarea → extinderea |
|---|---|---|---|---|---|
| A | fișe expirate, asistenta la telefon, recomandări neurmărite; clienți pierduți în fața rețelelor → cabinetul MM independent | export din programul MM sau Excel; lista HR; cabinetul e operatorul (Art. 9(2)(h)) | remindere, registru, raport de renegociere → % examene la termen, ore de asistentă economisite, angajatori păstrați | vizite fizice în Oradea + audit gratuit → 39/79/149 €/lună | adâncimea fluxului, istoricul buclelor, relația locală → prevenția la examen, dispecerat, arhiva de expunere |
| G | controale stabilite de medic și neprogramate → clinica cronică independentă | export din programul clinicii; marcajele laboratorului | listă de lucru + om care sună → controale programate, consultații facturate | audit pe 6 luni de date → 89 €/locație | know-how-ul de parsare a exporturilor fără API → alte bucle, după opinia MDR |
| B | amenda ITM, Excel → HR-ul angajatorului | doar datele HR, fără date medicale | calendar și remindere → zero fișe expirate | rețeaua de angajatori → 19–79 € | slabă → devine partea de angajator a lui A |
| K | pacientul pleacă acasă între faze → clinica dentară de turism | planul de tratament, fotografiile pacientului | check-in-uri multilingve → faza 2 făcută, mai puține complicații tratate de alții | rețeaua locală → 99–249 €/lună | relația → slabă spre predictiv |
| H | nimeni nu invită la pachetul 40+ → medicul de familie | exportul listei de pacienți | listă de eligibili + invitații → pași finalizați | asociația județeană → 15–30 €/lună | statul poate prelua funcția → depinde de plata CNAS |
| J | notificări neconfirmate → clinica de cardiologie | formularul pacientului | intrare + programarea testului de confirmare → teste ECG/Holter facturate | site-ul clinicii → 39–79 €/lună, ca modul | modul al lui G |
| Q | termenele EHDS, lipsa expertizei FHIR → vendorul local | date sintetice + schemele vendorului | fațadă FHIR, IPS, jurnal → conformitate | rețeaua din București → 5–15k € per vendor (estimare fără ancoră) | PL/SQL + FHIR → intermediar de conectare, ca în Finlanda |
| L | neprezentări → clinica privată | calendarul clinicii | remindere + grup de control → prezență măsurată | vizite → 49–99 €/lună | marfă |
| R | amenzi pentru WhatsApp/e-mail, cereri de acces → clinica privată | jurnale, documente | ceas de 30 de zile, link securizat → conformitate | consultanți GDPR → 19–49 €/lună | componentă „sistem EHR” din 2029/2031 |
| D | istoric rupt la schimbarea furnizorului, păstrare 40 de ani → furnizorul MM cu lucrători expuși | audiograme și spirometrii în PDF, extrase cu LLM și verificate de om | afișare fidelă în timp → nivel de bază, predare către furnizorul următor | treapta a doua a lui A | activ de date longitudinal → baza unei predicții viitoare |
| E | pozitivi FIT pierduți înainte de colonoscopie → consorțiul ROCCAS | lista participanților, rezultatele FIT, prin contract | listă de lucru + valuri după capacitate → colonoscopii făcute | subcontract UE → pe proiect | referință publică → celelalte proiecte regionale |
| C | angajații nu merg singuri la controale → furnizorul MM și angajatorul | lista HR + examenele | planificator pentru ziua de prevenție, într-un singur loc → participare | același cumpărător ca A → pe eveniment | modulul de prevenție al lui A |

### Cât de robust e clasamentul

Scorarea a fost refăcută cu trei seturi alternative de ponderi:
- **egale:** toate cele 17 criterii cântăresc la fel;
- **fezabilitate întâi:** datele, reglementarea, munca solo și MVP-ul cântăresc mai mult;
- **strategic întâi:** relevanța strategică are pondere 15.

**A și G rămân în primele trei la orice set de ponderi** (A: locurile 1, 1, 2, 1). B urcă pe primul loc când contează doar fezabilitatea și coboară pe locul 7 când contează strategia. Q (EHDS) urcă pe locul 3, iar D (arhiva) pe 5, când strategia cântărește mai mult: sunt opțiuni de anul 2, nu de start (`scoring/sensitivity.md`). Locurile 5–7 (H, J, Q) sunt la egalitate, deci ordinea dintre ele nu spune nimic.

### Ce au schimbat board-ul și panelurile simulate, și cât valorează

Board-ul de trei membri (lentile: Ofertă, Monopol, Produs) a pus **A pe primele două locuri la toți trei membrii**: media 5,7, 3 × „FUND IF”. **G a avut media cea mai mare (6,0)**, dar cu riscuri de integrare și de graniță MDR. B a primit 2 PASS, K 2 PASS, iar H 3 PASS (`board/board.md`).

Panelurile de câte 20 de cumpărători simulați au dat:

| Ideea | Prima ofertă | Oferta refăcută |
|---|---|---|
| A | 7/20 (35%) | 3/20 (15%) |
| G | **0/20** | 2/20, ambii fiind clinici cronice |
| B | 2/20 | — |

Motivele de refuz s-au repetat la toate ideile:
- obișnuința: „programul MM și Excel-ul îmi arată deja scadențele”;
- încrederea: „nu dau datele unui SRL necunoscut”;
- prețul: „îl plătesc din marjă” (`panels/*/results.md`).

**Toate acestea sunt simulări cu modele de limbaj.** Răspunsurile sunt corelate (același model), ratele sunt o limită superioară, iar la n=20 diferența dintre 7 și 3 nu e semnificativă statistic. Le folosesc doar ca să știu ce trebuie testat cu oameni reali.

## 7. Cinci analize în profunzime

Le-am ales pe cele mai bune patru produse distincte din clasament: A, G, K și H. B nu mai e produs separat: a devenit partea de angajator a lui A. A cincea e Q, aleasă din egalitatea H–J–Q de la 63,2 pentru că e cea mai puternică opțiune strategică (locul 3 când strategia cântărește mai mult) și folosește direct avantajul fondatorului pe Oracle/PL-SQL. J devine un modul al lui G.

**Nucleul tehnic comun tuturor celor cinci** (estimare):
- **Bază de date:** Oracle APEX + PL/SQL pe o instanță în UE, cu mai mulți clienți pe aceeași instalare, fiecare văzându-și doar datele lui, și jurnal de audit pe fiecare acțiune.
- **Automatizare:** n8n găzduit în UE pentru importuri programate (e-mail, folder, SFTP), trimiteri, escaladări și rapoarte.
- **Citirea fișierelor:** Python pentru Excel, CSV și PDF.
- **LLM:** API în regiune UE, fără păstrarea datelor, folosit **doar** pentru maparea coloanelor din fișiere dezordonate. Niciodată pentru interpretare clinică.
- **Statutul juridic:** fondatorul e persoană împuternicită (Art. 28 GDPR), clientul e operatorul. Kitul minim: DPA, listă de sub-procesatori, găzduire în UE, ajutor la DPIA (BK; [GDPR, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).
- **Răspundere:** jurnalul de audit e și apărarea sub PLD pentru versiunile lansate după 9 decembrie 2026.

### 7.1 A · Biroul de continuitate al cabinetului independent de medicina muncii (versiunea corectată)

În analiza founder, A era un „scadențar cu portal”. Rundele „bulletproof” l-au mutat de pe portal pe **munca din jurul examenului obligatoriu**. Portalul era ușor de copiat de cele șase programe MM existente. Munca spre exterior, registrul recomandărilor și planificarea echipei mobile nu sunt documentate la niciun vendor.

| Element | Conținut |
|---|---|
| **Conceptul** | Un „CAMO pentru oameni”: biroul care deține termenele, fără să facă examenul. (1) **Munca spre exterior:** remindere către HR-ul fiecărui angajator-client și urmărire până la programare. (2) **Registrul recomandărilor:** fiecare recomandare „apt condiționat” are termen pus de medic, dovadă încărcată și escaladare; e vizibil doar cabinetului până la opinia juridică. (3) **Raportul de renegociere** pe angajator. (4) **Portalul de status cu marca cabinetului:** doar o vedere peste celelalte, și doar cât permite opinia juridică. În lunile 18–36 se adaugă **un singur modul**, ales după o regulă: prevenția la examen sau dispeceratul echipei mobile (§8). |
| **Primul client plătitor** | O firmă MM medie (2–5 medici, echipă mobilă, 3.000–10.000 de angajați urmăriți) sau un cabinet aflat sub presiunea rețelelor. În Oradea: **Medimun, Carimed, Endodigest** (proprietatea de verificat) ([Medimun](https://www.medimun.ro/); [Carimed](https://carimedcenter.ro/despre-noi/)). |
| **MVP** | Import cu raport de calitate (rânduri, erori, dubluri). Calendarul scadențelor la 30/60/90 de zile, inclusiv regula examenului de reluare (după cel puțin 90 de zile de absență medicală sau 6 luni din alt motiv, în 7 zile). Remindere pe e-mail către HR. Registrul. Statusuri cu perioadă de grație: „programat” → „în curs de confirmare” → abia apoi „depășit”. Bannerul „actualizat la [data]”. Jurnal de audit. Export lunar automat către cabinet (dacă firma dispare, cabinetul are datele). **120–160 h.** |
| **Arhitectura** | Nucleul comun. Portalul angajatorului e o aplicație APEX separată, doar cu status. Cel mult **două adaptoare** de export în v1. LLM-ul vede doar capetele de coloană și rânduri sintetice. |
| **Datele și integrarea** | Excel-ul cabinetului sau exportul programului MM, plus lista HR. **Fără CNP** (se folosește numărul de dosar al cabinetului), fără diagnostice, fără textul recomandărilor. Concluzia (apt / apt condiționat / inapt) e cea scrisă deja pe exemplarul angajatorului din fișa de aptitudine ([HG 355/2007](https://www.avocatnet.ro/articol_8477/Hotarare-nr-355-2007-privind-supravegherea-sanatatii-lucratorilor.html)). Nu există niciun API. |
| **Concurenți și substitute** | Programele MM: BizMedica MM, cu import Excel ([Setrio](https://setrio.ro/medicina-muncii/)), MedExam, Qmedical, Charisma, MedSoft, Tempomed. Portalul MedLife Self-Service și MM Express ([MedLife](https://www.medlife.ro/medicina-muncii-express)). Regina Maria MM Oradea. Urmărirea scadențelor vândută ca serviciu inclus. Excel-ul și telefonul asistentei (0 €). **Cine ar copia primul:** Setrio și DMV Consult. |
| **Prețul** | **39 / 79 / 149 €/lună** (până la 1.500 / 6.000 / nelimitat de angajați urmăriți), SMS refacturat la cost și scris în contract, plată anuală opțională (12 luni la prețul a 10). Garanție de 90 de zile doar pentru cabinetele calificate. „Pilot fondator” pentru primele 5 cabinete, cu preț blocat 24 de luni. Prețul mediu de lucru e **~74 €**, cu un mix de 30% cabinete mici, 60% firme medii, 10% regionale (estimare). Ancora: 2–4 lei pe angajat pe an, adică ~2,5–5% din prețul MM de 80–110 lei. Dacă un vendor oferă gratuit portalul, treapta trece pe „Birou fără portal”, cu ~20 € mai ieftin. |
| **Reglementarea și poziționarea** | **Administrativ (categoria 1): „logistica medicinei muncii”.** Scopul declarat, scris: „software administrativ pentru planificarea examenelor de medicina muncii și urmărirea termenelor stabilite de medic; nu interpretează date medicale”. Cuvinte interzise în marketing: „prezice”, „risc”, „diagnostic”, „detectează”, „previne boala”. **Ce schimbă clasa:** „identifică angajații cu risc care trebuie examinați mai devreme” → dispozitiv (MDSW); „evidențiază valori anormale” → dispozitiv, posibil sub IVDR. GDPR: angajatorul vede doar statusul și concluzia până la opinia juridică (o listă de recomandări deschise poate dezvălui indirect date de sănătate). SMS-urile către angajați doar cu consimțământ (Legea 506/2004) ([Avocatnet](https://www.avocatnet.ro/articol_15269/Orange-amendata-cu-5000-lei-pentru-mesaje-comerciale-nesolicitate.html)). Sub PLD: jurnal de versiuni și disciplină de patch-uri. Pentru clienții NIS2: chestionarele de securitate. |
| **Ruta spre primii 3 clienți** | 6 vizite la cabinete din Oradea, plus discuții directe cu cei 5 vendori, în primele 3 săptămâni. **Audit gratuit pe exportul real:** câte fișe sunt expirate azi și câte expiră în 30/60 de zile, câte recomandări n-au dovadă de închidere, plus jurnalul de o săptămână al telefoanelor asistentei. Apoi **pilot concierge plătit**: 3 luni în avans, rambursabile prin garanție. 2–3 angajatori din rețeaua fondatorului servesc drept argument. Se testează două mesaje de deschidere: „asistenta nu mai sună angajatorii” față de „portal ca la rețele”. |
| **Costuri și efort** | Pornire în numerar **~3.580 €**: avocat ~1.200 €, opinie juridică ~600 €, revizie de securitate ~800 €, găzduire, deplasări, SMS. Costuri fixe 230 €/lună; din luna 13, 780 €/lună (ajutor part-time 400 € + responsabil medical 150 €). Vârful de numerar **~4.060 €** (bază) sau **~4.675 €** (pesimist). Onboarding 6–10 h pe client; suport ~1 h pe client pe lună. Capacitate ~25 de clienți la 10–12 h/săpt. CAC estimat la 25–40 h, cu țintele ≤20 h în luna 12 și ≤15 h în luna 18. Toate sunt estimări (`cfo/cfo-sources.md`; `bulletproof/model_36m.py`). |
| **Dovezile de cerere** | Examenul periodic e obligatoriu pentru toți lucrătorii (HG 355/2007 art. 20); amenzi de 4.000–8.000 lei, sumă de reverificat ([avocatnet](https://www.avocatnet.ro/articol_68935)). ITM găsește frecvent muncă fără examen. MedLife vinde exact stratul pentru angajator. Romedic listează 508 cabinete MM la nivel național, ca director, nu ca recensământ ([Romedic](https://www.romedic.ro/cabinete/medicina-muncii/4)). În Oradea sunt ~6 cabinete aparent independente. **Lipsesc:** orice dovadă că un cabinet independent plătește și orice sondaj printre angajatori. Simulat: panel 7/20, apoi 3/20; board 3 × FUND IF. |
| **De ce ar eșua** | Vendorii au deja portalul sau îl adaugă. „Excel-ul merge.” Încrederea. Piața locală mică și consolidarea (Medicris → MedLife). Marja mică a cabinetului (80 lei pe angajat). Exporturile dezordonate. Timpul fondatorului. O regulă juridică strictă despre ce vede angajatorul. |
| **Numerele, după corecturile bulletproof** | Planul original, fără churn: +534 € în anul 1, 1.000 € MRR în luna 18, plafon 1.625 €. **Cu churn de 1,5%/lună și 20% retururi la garanție:** −198 € în anul 1 și 1.000 € MRR abia în luna 24. **Cu o rampă realistă ca timp:** 984 € MRR în luna 36, adică 1.000 € nu mai vine. Planul final (v3), bază fără modul: +1.747 € în anul 1, MRR 758 / 1.280 / 1.747 / 2.562 € în lunile 12 / 18 / 24 / 36, 1.000 € MRR în luna 15. Cu modulul: 2.171 € în luna 24, 3.185 € în luna 36, **3.000 € în luna 34**. Pesimist: −1.031 € în anul 1, 1.000 € MRR în **luna 32**, 1.111 € în luna 36. Îmbunătățirea dintre original și v3 vine din **ipoteze** (preț mediu 74 €, 3 piloți plătiți în luna 3, retururi de 10%, ajutor din luna 13, CAC ≤15 h, adoptarea modulului), nu din dovezi (`bulletproof/model_36m.out.txt`). |

### 7.2 G · „Controale pierdute” la clinicile independente de boli cronice

| Element | Conținut |
|---|---|
| **Conceptul** | După panel, a rămas **o singură buclă în v1**: lista săptămânală a pacienților cu control stabilit de medic și neprogramat. Asistenta sună (un om, nu un e-mail), pacientul primește un mesaj neutru cu link de programare, iar închiderea buclei se jurnalizează. Raportul lunar arată bucle închise → consultații facturate. Un grup de control e opțional. Buclele pentru rezultatele în afara intervalului și pentru trimiterile neînchise vin abia după o opinie MDR. Navigatorul pentru notificările de la ceas (J) devine un modul. |
| **Primul client plătitor** | O clinică independentă multi-specialitate (diabet, cardiologie, endocrinologie), cu contract CAS și laborator propriu sau partener: **GrandMed, NewMedics, Medena** (Oradea) ([GrandMed](https://www.grandmed.ro/)). Apoi clinici independente din Cluj și Timișoara. **Nu medicii de familie** (0/7 în panel, plătiți pe listă) și **nu laboratoarele**. |
| **MVP** | Import CSV zilnic sau săptămânal din programul clinicii; reguli deterministe (termenele puse de medic); lista asistentei; SMS/e-mail cu consimțământ; registrul de consimțământ; raport lunar; grup de control. **140–180 h.** |
| **Arhitectura** | Nucleul comun; regulile în PL/SQL; Python mapează exporturile, care diferă de la un program la altul; LLM doar pentru maparea coloanelor, confirmată de om. |
| **Datele și integrarea** | Exportul programului clinicii (icMED, MediNote, Zarina și altele, fără API public). Rezultatele vin adesea ca PDF sau pe e-mail, deci la început se citesc doar marcajele laboratorului. Vizitele la o clinică de specialitate sunt **date de sănătate indirecte** (BK; CJUE C-184/20, C-21/23). |
| **Concurenți și substitute** | Reminderele incluse în programele de clinică (MediNote, cu SMS). Agenții vocali și pe WhatsApp: VAstoma, DentAIM, AI Frontdesk, Callio, receptie-clinica.ai ([receptie-clinica.ai](https://receptie-clinica.ai/)). Rețelele interpretează rezultatele doar pentru pacienții lor (asistentul AI MedLife, Synevo Decoder) ([MedLife](https://www.medlife.ro/comunicat-de-presa/medlife-lanseaza-primul-asistent-ai-care-ofera-ghidaj-medical-personalizat); [Synevo Decoder](https://synevo.hilio.com/)). e-SănătateaMea, pentru programările furnizorilor CNAS din T4 2026. Asistenta cu telefonul. |
| **Prețul** | **89 €/locație/lună**, după un audit gratuit, cu garanția „sub 15 controale programate în primele 3 luni → nu plătiți”. Se testează 69 € față de 99 €. Intervalul simulat acceptabil: 30–130 € (v1). |
| **Reglementarea și poziționarea** | Administrativ **doar** dacă termenele sunt ale medicului și marcajele ale laboratorului. **Ce schimbă clasa:** „evidențiază valori anormale și prezice deteriorarea” → dispozitiv, posibil IVDR; „ordonează pacienții după risc” → dispozitiv; ordonarea după un model individual devine profilare (Legea 190/2018 art. 3: consimțământ explicit sau bază legală expresă) ([ANSPDCP](https://www.dataprotection.ro/servlet/ViewDocument?id=1520)). SMS doar cu consimțământ. Din 2031 poate deveni „sistem EHR” sub EHDS, dacă tratează rezultate de laborator. **Opinie MDR scrisă (~800 €) înainte de orice buclă de laborator.** |
| **Ruta spre primii 3 clienți** | Doar după ce sunt îndeplinite porțile lui A (§8, §11). Audit pe un export pseudonimizat de 6 luni la GrandMed, NewMedics, Medena: „câte controale sunt depășite acum”. Pragul: ≥30 pe clinică. Referințe de la clienții A, pentru încredere. |
| **Costuri și efort** | MVP 140–180 h; numerar ~3,9–5,2k €; onboarding 10–15 h; suport 2–3 h pe client pe lună; capacitate ~13 clinici la 10–12 h/săpt. |
| **Dovezile de cerere** | Internaționale și solide: între **6,8% și 62%** dintre rezultatele de laborator nu sunt urmărite ([Callen, JGIM](https://link.springer.com/doi/10.1007/s11606-011-1949-5)). **18,1%** dintre alertele pentru imagistică n-au fost niciodată confirmate ([ScienceDaily](https://www.sciencedaily.com/releases/2009/09/090928172349.htm)). Urmărirea cu un om care acționează: **73,4% față de 52,2%** au primit evaluarea diagnostică ([ecancer](https://ecancer.org/en/news/7664-electronic-trigger-reduces-delays-in-evaluation-for-cancer-diagnosis)). Un e-mail a făcut ~11% dintre medici să acționeze, telefonul peste două treimi ([PMC4613876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4613876)) [Stabilit/Emergent puternic]. **În România:** nicio măsurătoare și niciun proces „laborator → medic → rechemare” găsit. Simulat: panel 0/20, apoi 2/20; board, media cea mai mare (6,0). |
| **De ce ar eșua** | Încrederea și GDPR („nu dau datele pacienților diabetici unui SRL necunoscut”). „Programul trimite deja SMS.” Exporturile fac din fiecare clinică un proiect separat. Consimțământul pentru SMS lipsește din fișele vechi. Venitul recuperat nu justifică prețul. Mandatul e-SănătateaMea. |
| **Numerele** | La 89 €: contribuție 84,5 € pe client pe lună; anul 1 **−1.070 €** (pe pierdere la orice preț testat); 1.000 € MRR în **luna 27**; plafon **~1.157 €** la 10–12 h/săpt (`cfo/cfo.md`). |
| **Statutul** | **Înghețat în scris** până în luna 12 și până la ≥10 cabinete A plătitoare. Atunci, cel mult un audit G, doar la cererea unei clinici. |

### 7.3 K · Urmărirea pacienților de turism dentar (Oradea)

| Element | Conținut |
|---|---|
| **Conceptul** | După faza 1 a unui implant, pacientul pleacă acasă. Instrumentul programează protocolul de după tratament, face check-in-uri în germană, italiană, engleză și maghiară (fotografii și chestionar trimise medicului, **fără evaluare automată**) și planifică fereastra de călătorie pentru faza 2. |
| **Primul client plătitor** | O clinică din Oradea care își face reclamă la pacienți străini: **Dental-Art, MaxiloMED, LifeDent, Estetical Dentis, German Dental** ([MaxiloMED](https://www.maxilomed.ro/turism-medical-oradea-medical-and-travel/)). |
| **MVP** | Planul pe pacient; mesaje programate în mai multe limbi; încărcarea fotografiilor în UE; tabloul medicului; reminderul pentru faza 2. **120–160 h.** |
| **Arhitectura** | Nucleul comun plus stocare de fișiere în UE; LLM doar pentru traducerea șabloanelor, verificată de om. |
| **Datele și integrarea** | Planul de tratament din programul clinicii (iStoma, icMED, fără API) și fotografiile pacientului (date de sănătate: DPA, găzduire în UE). |
| **Concurenți și substitute** | Reminderele dentare existente (VAstoma, DentAIM), iStoma (5.300 de stomatologi), Callio, WhatsApp-ul coordonatorului clinicii. |
| **Prețul** | 99–249 €/lună pe clinică (ancoră: Callio, 139–299 €). |
| **Reglementarea și poziționarea** | Administrativ cât timp doar transmite. **Ce schimbă clasa:** „evaluează automat vindecarea din fotografii” sau „detectează complicațiile” → dispozitiv. GDPR e același pentru pacienții din UE, dar reclamațiile pot veni în altă jurisdicție și altă limbă. |
| **Ruta spre primii 3 clienți** | Vizite la clinicile de turism dentar din Oradea, prin rețeaua locală; condiția board-ului: volumul de pacienți străini pe clinică și 2 pre-vânzări. |
| **Costuri și efort** | 120–160 h; ~2.000–3.000 € (traduceri, stocare). |
| **Dovezile de cerere** | Clinicile își declară pacienți din Italia, Marea Britanie, Austria, Germania (marketing) ([Dental-Art](https://dental-art.ro/en/dental-tourism/)). Peste 30.000 de turiști medicali străini într-un an, an neclar ([Economica.net](https://www.economica.net/peste-30-000-de-turisti-straini-au-venit-in-scop-medical-in-romania-anul-trecut_823250.html)). Implanturi la ~€400–450 față de €560–600 în Ungaria, metodologie neclară. **Lipsește volumul pentru Bihor.** |
| **De ce ar eșua** | Volum prea mic pe clinică; coordonatorul face deja asta gratuit pe WhatsApp; rechemarea dentară e aglomerată; **nu duce spre predictiv** (strategic 2/5). Board: 2 PASS, media 4,0. |
| **Numerele** | Fără model CFO. Calculul meu: la 99–249 €, 1.000 € MRR cere **4–10 clinici**. Fezabil doar dacă volumul pe clinică justifică prețul, lucru nedovedit. |

### 7.4 H · Rechemarea pentru pachetul CNAS de prevenție 40+/60+ (medici de familie)

| Element | Conținut |
|---|---|
| **Conceptul** | Lista cabinetului, filtrată după **vârstă și data ultimei prevenții** (nu după risc). Invitații prin SMS, telefon sau scrisoare; programare; urmărirea celor 3 pași ai pachetului 40+; ajutor la raportare. |
| **Primul client plătitor** | Un cabinet de medicină de familie din Oradea, cu contract CNAS, listă mare și asistentă. |
| **MVP** | Import din exportul programului de cabinet; lista eligibililor; invitații; programare; urmărirea pașilor; export pentru raportare. **100–140 h.** |
| **Arhitectura** | Nucleul comun. |
| **Datele și integrarea** | Exportul programului de cabinet (fără API); medicul e operatorul. |
| **Concurenți și substitute** | Vendorii de program de cabinet (BizMedica/Setrio); e-SănătateaMea, cu programare obligatorie pentru furnizorii CNAS din T4 2026; asistenta cu telefonul. |
| **Prețul** | 15–30 €/lună pe cabinet sau un modul vândut prin vendor, cu împărțirea venitului (ancoră: BizMedica, 159–199 RON/lună). |
| **Reglementarea și poziționarea** | Administrativ cât timp eligibilitatea e regula de calendar a CNAS. **Ce schimbă clasa:** „prioritizează pacienții cu risc mare” → zonă de graniță sau dispozitiv; exemplele noi despre prevenție din MDCG 2019-11 Rev.1 fac granița mai sensibilă. Apelurile automate cer consimțământ; prioritizarea după date de sănătate e profilare. |
| **Ruta spre primii 3 clienți** | Medicii de familie din rețeaua fondatorului, apoi asociația județeană a medicilor de familie. |
| **Costuri și efort** | 100–140 h; ~1.500–2.500 €. |
| **Dovezile de cerere** | Din februarie 2026, prevenția e gratuită pentru oricine e înscris la un medic de familie: la 40+, până la 3 consultații în 6 luni; la 60+ se adaugă osteoporoza, incontinența și demența ([Arhiepiscopia Aradului / ghidul CNAS](https://www.arhiepiscopiaaradului.ro/2026/02/atat-asiguratii-cat-si-neasiguratii-beneficiaza-de-servicii-medicale-de-preventie-a-aparut-noul-ghid-cnas/)). Invitațiile funcționează: scrisorile de invitație cresc participarea la screeningul cervical de 1,71 ori ([Cochrane](https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD002834.pub3/pdf/CDSR/CD002834/CD002834_abstract.pdf)). **Lipsește suma pe care CNAS o plătește medicului pe serviciu de prevenție.** Asistența primară primește 10% din cheltuială. |
| **De ce ar eșua** | Medicul n-are motiv financiar să invite mai mulți pacienți și n-are timp pentru vizite în plus. Vendorul adaugă funcția gratuit. e-SănătateaMea devine canalul de programare. Board: **3 × PASS**. |
| **Când ar redeveni interesantă** | Dacă CNAS plătește o sumă semnificativă pe serviciu de prevenție (ipoteza 8 din `analiza_founder.md` §E5). Atunci devine cea mai mare pârghie de prevenție la nivel de populație, pe bani publici. |

### 7.5 Q · Componente EHDS pentru vendorii locali de software medical

| Element | Conținut |
|---|---|
| **Conceptul** | O fațadă FHIR R4 peste bazele vechi Oracle/PL-SQL, un generator de rezumat IPS, tabele de mapare LOINC/ATC, componenta de jurnalizare și o evaluare de pregătire. Fondatorul livrează o **componentă**; vendorul își autocertifică „sistemul EHR”. |
| **Primul client plătitor** | Un vendor român de software pentru clinici sau laboratoare, fără echipă FHIR. Candidați din note: MediNote, BizMedica/Setrio, icMED, iStoma; la HIS, Hipocrate (RSC) și InfoWorld. **Nu s-a verificat** ce tehnologie folosește fiecare. |
| **MVP** | Fațadă FHIR pentru 5–8 resurse (Patient, Observation, DiagnosticReport, Composition…); IPS generat pe date sintetice; jurnal de acces. **250–400 h**, inclusiv învățarea FHIR și IPS. |
| **Arhitectura** | PL/SQL + ORDS (REST) sau o fațadă în Python; HAPI și Medplum ca referință ([Medplum](https://www.medplum.com/open-source)); ghidurile HL7 FHIR IPS. |
| **Datele și integrarea** | **Nu e nevoie de date de pacient pentru dezvoltare** (date sintetice); schemele vin de la vendor. |
| **Concurenți și substitute** | Open-source (HAPI, Medplum); integratori; echipa internă a vendorului. Asseco, Comarch și CompuGroup n-au o prezență vizibilă în România în domeniul sănătății. |
| **Prețul** | Licență plus integrare, de ordinul 5.000–15.000 € per vendor, plus mentenanță anuală (**estimare fără ancoră în note**). |
| **Reglementarea și poziționarea** | Nu e MDR. Sub EHDS, „sistemul EHR” se **autocertifică**: cerințe esențiale, componentele armonizate de interoperabilitate și de jurnalizare, marcaj, înregistrare în baza de date a UE, fără organism notificat. **Termenele:** aplicare generală pe 26.03.2027; din 26.03.2029 pot fi puse pe piață doar sisteme conforme pentru rezumate și rețete (Q&A-ul Comisiei); grupa 2 (analize, imagini, externări) pe 26.03.2031 ([Q&A EHDS](https://health.ec.europa.eu/document/download/4dd47ec2-71dd-49fc-b036-ad7c14f6ed68_en?filename=ehealth_ehds_qa_en.pdf)). Primele acte de punere în aplicare (MyHealth@EU, HealthDCAT-AP) au fost raportate în septembrie 2026 ([Produktkanzlei](https://www.produktkanzlei.com/en/2026/09/23/myhealtheu-and-healthdcat-ap/)). **Ce schimbă clasa:** dacă componenta începe să „semnaleze” sau să „interpreteze” date, iese din EHDS și intră în MDR. |
| **Ruta spre primii 3 clienți** | Rețeaua din București; contact direct cu ~10–20 de vendori; argumentul finlandez: obligația plus certificarea au creat o piață pentru intermediari ([Kanta](https://kanta.fi/en/professionals/preparatory-tasks-and-joining)). |
| **Costuri și efort** | 250–400 h; ~2.000–5.000 €. |
| **Dovezile de cerere** | Termene legale datate; vendori fragmentați, fără API. **Contra:** cumpărătorii vor amâna până în 2027–2028; regulile românești de aplicare lipsesc; open-source-ul e „suficient”. |
| **De ce ar eșua** | Nimeni nu cumpără înainte de 2028; România întârzie aplicarea; venitul vine pe proiect, nu recurent; nimic nu intră în fereastra de 90 de zile. |
| **Rolul corect** | O **opțiune pentru anii 2027–2029**, alimentată din competența construită cu A, nu un start. Q e și calea prin care stratul de buclă devine „conform EHDS” când va trebui. |

## 8. Trei strategii de intrare: venit întâi, SaaS specializat, platformă predictivă

Cele trei strategii nu sunt complet separate. Ele diferă prin ce optimizează în primii doi ani:
- **A (venit întâi)** optimizează numerarul rapid;
- **B (SaaS specializat)** optimizează venitul recurent pe un singur flux;
- **C (platformă predictivă)** optimizează activul de date și dovezile.

Fiecare are aceleași patru orizonturi și aceleași rubrici: ce construiești, dependențele, achiziția, finanțarea, reperele, pivotul și condiția de oprire. Strategiile A și C sunt designul meu, construit din note și din rundele bulletproof. Strategia B e planul final întărit (`bulletproof/rounds/06_final_plan.md`).

### 8.1 Strategia A · Venit întâi: servicii care devin produs

Ideea vine din inversarea nr. 7 a analizei laterale: întâi faci bucla **manual, ca serviciu, pentru un plătitor**, apoi o automatizezi. Seamănă cu Cera (servicii cu software) și cu centrele germane de telemedicină, care sunt centre cu oameni (`analiza_laterala.md` §B.7).

| Rubrica | 0–6 luni | 6–18 luni | 18–36 luni | 3–7 ani |
|---|---|---|---|---|
| **Ce construiești sau vinzi** | servicii plătite unde fondatorul e rar: audit de scadențe și bucle deschise pe exportul clientului (întâi gratuit, ca unealtă de vânzare, apoi plătit); „birou de continuitate” operat manual pentru 2–3 cabinete MM (fondatorul rulează reminderele cu APEX + n8n); mici proiecte de curățare și raportare a datelor pentru clinici | serviciul cel mai repetat devine produs (taxă de configurare + abonament); din 2027, 1–2 evaluări de pregătire EHDS pentru vendori locali | nucleu recurent + proiecte FHIR/IPS pentru vendori pe măsură ce apar regulile românești; fațada FHIR devine produs | intermediar de conectare și conformitate, ca în Finlanda, peste stratul de buclă |
| **Dependențe** | kitul juridic (DPA, sub-procesatori), asigurare | un serviciu care se repetă la ≥3 clienți | actele de punere în aplicare EHDS (din 2027); reguli românești | România desemnează autoritatea și profilurile FHIR |
| **Achiziție** | vizite fizice în Oradea, rețeaua locală | referințe, vânzare la distanță | rețeaua din București pentru vendori | parteneriate cu vendori |
| **Finanțare** | capital propriu, sub ~2k € | din venit | din venit + granturi pentru interoperabilitate | din venit; capital extern doar pentru o extindere regională |
| **Repere** | ≥2 clienți plătitori de servicii; ≥1 care cere același lucru lunar | ≥50% din venit recurent în luna 18 | ≥2 contracte cu vendori | venit recurent majoritar |
| **Pivot** | spre B, când un serviciu se repetă | spre B complet dacă proiectele nu se repetă | spre Q ca linie principală | — |
| **Oprire** | niciun serviciu repetat în 6 luni; >70% din ore nefacturabile | proiectele trec de 60% din venit în luna 18: ai devenit agenție, nu produs (decizie explicită) | — | — |

**Drumul spre predictiv** e cel mai slab dintre cele trei. Trece prin transportul datelor și al predicțiilor altora (FHIR, IPS), nu printr-un activ propriu. **Riscul principal** e capcana agenției: proiectele mănâncă cele 10–12 ore, iar produsul nu apare. **Nu există ancore de preț în note pentru servicii.** Singura estimare e cea pentru componentele EHDS: 5–15k € per vendor, fără ancoră.

### 8.2 Strategia B · SaaS specializat: biroul de continuitate MM

E planul final întărit după trei runde de review „investitor”, cu porți numerotate și condiții de oprire. **Luna 1 = noiembrie 2026.**

| Rubrica | 0–6 luni (nov. 2026 – apr. 2027) | 6–18 luni (mai 2027 – apr. 2028) | 18–36 luni (mai 2028 – oct. 2029) | 3–7 ani (nov. 2029 – 2033) |
|---|---|---|---|---|
| **Ce construiești** | prototip pentru pilotul concierge; apoi MVP: import cu raport de calitate, calendar, remindere către HR, registru, statusuri cu grație, jurnal, export lunar | portalul cu marca cabinetului (doar ce permite opinia juridică); raportul de renegociere; cel mult două adaptoare; plata anuală; tabloul indicatorilor | **un singur modul, ales după regulă**: prevenția la examen **sau** dispeceratul echipei mobile | al doilea modul; arhiva de expunere; „pe cine suni primul” (cu bază legală); componente EHDS; găzduirea modelelor CE ale altora |
| **Dependențe** | 0–1 vendori cu portal; exporturi obținute în <30 min; opinie juridică pe „ce vede angajatorul” | responsabilul medical numit până în luna 12; ajutor part-time din luna 13 (dacă poarta e trecută) | notă scrisă de calificare MDR; partener de laborator sau doar testele pe care echipa MM le face deja; partener academic | baza legală pentru profilare; HDAB în România; reforma MDR |
| **Achiziție** | 6 vizite în Oradea + 9 conversații (6 pe video); audit gratuit; pilot concierge plătit | referințe; vânzare la distanță către firmele MM medii; nicio regiune peste 40% din MRR | ~1,5 clienți noi pe lună (CAC ≤15 h); discuții cu un vendor MM după 10 clienți | rețea medie sau vendor MM ca distribuitor; alte țări doar după rezultate publicate |
| **Finanțare** | capital propriu; pornire ~3.580 €; vârf de numerar ~4.060 € | din venit | din venit + un grant nediluant pentru evaluare | angel sau fond **doar** la un declanșator (mai jos) |
| **Repere (porți)** | ziua 21: vendorii; ziua 60: ≥3 pre-vânzări; ziua 90: efect măsurat în pilot; luna 6: ≥5 cabinete plătitoare | luna 12: ≥8 clienți, CAC ≤20 h, churn <2%/lună; luna 18: ≥12 clienți și MRR ≥1.000 € | luna 24: modulul la ≥15% din clienți, MRR ≥1.700 €; luna 36: MRR ≥2.500 €, modulele ~20% din MRR | modulele ≥40% din MRR și MRR ≥5.000 €; un rezultat publicat; un contract cu o rețea medie, un vendor sau clienți din altă țară |
| **Pivot** | ≥2 vendori au portal → OEM la vendorul care nu-l are, sau doar registrul | <8 clienți în luna 12 → OEM sau vânzarea bazei de clienți | modulul la <15% după 12 luni → se încearcă celălalt o singură dată | niciun declanșator până în luna 48 → nișă profitabilă sau vânzare către un vendor MM |
| **Oprire** | ≤1 pre-vânzare până în ziua 75; <10 cabinete accesibile; curățarea datelor >20 h | churn >3%/lună timp de 3 luni | niciun efect măsurat → modulul nu se vinde ca „prevenție” | 3b nu bate reminderul pentru toți → nu se vinde |

**Regula de alegere din luna 18.** Prevenția la examen are prioritate dacă ≥3 angajatori au cerut-o în scris, prin cabinetele lor, și există un partener de test. Altfel se face dispeceratul, dacă ≥5 clienți au echipă mobilă. Altfel nu se face niciun modul și se încearcă vânzarea prin vendor. Fondatorul urcă la ~20 h/săpt **doar** dacă MRR ≥1.500 € și ajutorul part-time funcționează. În acel caz se fac ambele module, la 6 luni distanță.

### 8.3 Strategia C · Platformă predictivă pe termen lung, în etape cu porți

Strategia C nu e o alternativă la B. E **B construit de la prima zi pentru ca activul de date și dovezile să fie legale și utilizabile**. Pornește din obiecțiile rundei a doua: „activul de date nu e al tău” și „etapa 2 depinde de cineva pe care nu-l controlezi”. Răspunsul e guvernanța datelor pe trei niveluri, fiecare cu baza lui legală:
- **nivelul A, operațional:** cabinetul e operatorul, fondatorul e persoană împuternicită, datele servesc doar acel cabinet;
- **nivelul B, indicatori agregați:** celule de minimum 10 persoane; comparațiile între cabinete doar dacă ieșirea e anonimă după testul din Recitalul 26 și cabinetul a optat în scris;
- **nivelul C, cercetare și modele:** prin studii cu partener academic și comisie de etică (Art. 9(2)(j)), prin permise HDAB de la ~2029 sau prin modelul comandat chiar de cabinet, cu DPIA (`bulletproof/rounds/04_round_2_plan.md`).

**Produsul nu se sprijină pe consimțământul angajatului** pentru dezvoltarea produsului. În relația de muncă, consimțământul riscă să nu fie liber (BK, de verificat cu avocatul).

| Rubrica | 0–6 luni | 6–18 luni | 18–36 luni | 3–7 ani |
|---|---|---|---|---|
| **Ce construiești** | ce construiește B + designul pe trei niveluri, scris cu avocatul; nicio dată nu iese din tenantul cabinetului (nici spre LLM) | **măsurarea ca parte din produs**: auditul de pornire e linia de bază; angajatorii sunt porniți în valuri lunare, iar cei care încep mai târziu sunt comparația naturală pentru primii | **3a: prognoza de volum pe sediu** pentru echipele mobile (zile de deplasare, examene pe zi): predicție operațională fără profilare individuală; **modulul de prevenție la examen** (testul în aceeași vizită; constatarea marcată de medic; un om care sună; verificarea la examenul următor) | **3b: „pe cine suni primul”**, ca model al fiecărui cabinet, cu grup de control; **găzduirea modelelor CE ale altor vendori** (vendorul poartă MDR, tu urmărirea); folosirea secundară prin HDAB; un dispozitiv propriu (clasa I/IIa) **doar** cu finanțare externă și partener clinic |
| **Dovezile pe care se sprijină** | regula „date fără beneficiu”: benefic = riscul de bază × cât de acționabil e semnalul × cât de sigur e răspunsul | urmărirea cu om care acționează bate alerta pasivă (73,4% față de 52,2%) | testul în aceeași vizită: 22% → 100% (ACCESS); stratificarea fără acțiune crește utilizarea (PRISMATIC) | țintirea nu e dovedită superioară reminderului pentru toți ([recenzia JAMIA](https://eprints.gla.ac.uk/287844/1/287844.pdf)); EAGLE: 49,6% urmare după semnal |
| **Dependențe** | avocat; căutarea unui medic MM responsabil | responsabil medical numit; partener academic identificat (Facultatea de Medicină din Oradea e neverificată) | notă MDR; laborator partener (Humanamed e singurul independent găsit) sau doar testele MM existente; grant | Legea 190/2018 art. 3 (consimțământ explicit sau bază legală expresă) și DPIA; HDAB în România; AI Act Anexa I (2.08.2028); reforma MDR |
| **Achiziție** | ca B | ca B | angajatorii plătesc modulul prin cabinet | parteneriate cu vendori de modele CE; rețele medii |
| **Finanțare** | capital propriu | din venit | **granturi nediluante** pentru evaluare (EIT Health; ADLO/CRESC, după expirarea apelului nr. 8) | angel sau fond **doar** la un declanșator; dispozitivul propriu niciodată din cei 25k € |
| **Repere** | design scris; DPIA-model | prima linie de bază la ≥5 cabinete | +10 puncte procentuale la recomandările închise în 90 de zile față de comparație, sau mai multe examene pe deplasare | un rezultat publicat; 3b bate reminderul pentru toți |
| **Pivot** | — | fără partener academic → măsurare internă, nepublicată | fără efect → modulul rămâne serviciu de organizare, nu „prevenție” | fără HDAB → etapa 4 se reduce la găzduirea modelelor altora și la export conform EHDS |
| **Oprire** | ca B | ca B | ca B | 3b nu bate reminderul → nu se vinde; nicio rută legală → nu se construiește |

**Declanșatorii pentru un „caz de fond”** sunt scriși dinainte. Oricare dintre ei deschide discuția cu un angel sau un fond:
- modulele aduc ≥40% din MRR, iar MRR-ul total e de cel puțin 5.000 €;
- un rezultat măsurat și publicat, cu grup de comparație;
- un contract cu o rețea medie, cu un vendor MM sau cu clienți din altă țară.

**Scenariul „nimic nu vine la timp”** înseamnă: fără HDAB, fără reforma MDR, EHDS întârziat. Și în acest caz rămâne o afacere cu valoare: biroul de continuitate, plus un modul, plus prognoza de capacitate fără profilare.

**Capătul drumului, spus cinstit.** C nu duce la „un model propriu de risc clinic”. Duce la **stratul care face ca prevenția plătită de angajator să se termine cu o acțiune**, iar mai târziu la locul în care modelele certificate ale altora produc acțiuni, nu doar alerte.

### 8.4 Ce alegi și cum le combini

| Strategia | Primul venit | MRR realist la 10–12 h/săpt | Credibilitatea drumului predictiv | Riscul principal | Când o alegi |
|---|---|---|---|---|---|
| A · Venit întâi | cel mai rapid (luna 1–3), pe proiect | mic și neregulat; venit, nu MRR | slabă | capcana agenției | dacă ai nevoie de numerar imediat sau dacă porțile lui B pică, dar clienții cer servicii |
| B · SaaS specializat | luna 3 (piloți plătiți) | bază: 1.000 € în luna 15–19, ~1.600 € plafon fără ajutor; pesimist: 1.000 € în luna 32 | medie, prin module | golul nu există; copierea de către vendori | **implicit** |
| C · Platformă predictivă | ca B | ca B; 3.000 € în luna ~34 doar cu ajutor și modul | **cea mai bună dintre cele trei** | etapele 3b–4 depind de calendare externe și de baze legale | ca B, cu guvernanța și măsurarea construite de la început |

**Recomandarea: B ca șira spinării, cu C încorporat de la prima zi** (guvernanța pe niveluri, linia de bază, valurile de pornire, responsabilul medical). Din A se păstrează doar două mecanisme, folosite pentru vânzare și onboarding, nu ca linie de afaceri: auditul gratuit și pilotul concierge plătit.

**Ce s-a întărit în cele trei runde de review simulat.** Probabilitatea maximă de respingere a scăzut de la **85%** („nicio dovadă reală de cerere”) la **60%** („cazul de investiție nu există încă; nu e clar când ar exista”). Obiecțiile care au rămas nu mai sunt despre coerență, ci despre dovezi pe care doar piața reală le poate da (`bulletproof/rounds/01–05`).

## 9. Conceptul recomandat: biroul de continuitate al cabinetului independent de medicina muncii

**În două fraze:** un add-on administrativ prin care cabinetul independent de medicina muncii deține tot ce se întâmplă între două examene obligatorii: cine e scadent, cine trebuie sunat, ce recomandare a rămas deschisă și ce a primit angajatorul. Angajatorul plătește deja examenul. Cabinetul plătește biroul, pentru că îi economisește timpul asistentei și îi păstrează clienții la renegociere.

**Cui îl vinzi și de ce acum.** Cumpărătorii țintă sunt firmele MM medii cu echipă mobilă și cabinetele care pierd clienți în fața rețelelor. Primii sunt în Oradea; apoi vânzarea merge la distanță. Momentul e acum din trei motive:
- MedLife a cumpărat cel mai mare furnizor MM din Bihor ([MedLife](https://www.medlife.ro/comunicat-de-presa/medlife-bifeaza-o-noua-tranzactie-la-oradea)) și le oferă angajatorilor un portal cu statusul în timp real ([MedLife Self-Service](https://www.medlife.ro/self-service));
- independenții concurează fără un echivalent;
- nimeni nu a documentat public pentru ei munca spre angajator.

**De ce e cea mai puternică opțiune inițială în aceste constrângeri:**
- **Cel mai bine documentat plătitor dintre toate opțiunile.** Obligația e legală și recurentă, plătită de angajator, cu amenzi, pentru întreaga populație salariată.
- **Fără dispozitiv medical.** E categoria 1, fără MDR, fără date clinice stocate și fără CNP.
- **Cumpărători accesibili.** Sunt numărabili și se poate ajunge fizic la ei.
- **Bani puțini.** Cere cel mai puțin numerar (~3,6k € la pornire, vârf ~4,1k €).
- **Clasare robustă.** E singura idee pusă pe primele două locuri de toate cele trei lentile ale board-ului simulat și pe primele două locuri la orice set de ponderi.
- **E pe drumul spre prevenție.** Același cumpărător, cu același contact obligatoriu, poate vinde mai târziu testul în aceeași vizită: mecanismul cu cea mai bună dovadă din note (ACCESS: 22% → 100%).

**Ce nu face, niciodată, în etapele 0–3a:**
- interpretare clinică;
- scoruri de risc individuale;
- afirmații „predictive” în marketing;
- date clinice stocate în afara programului MM al cabinetului.

**Un motor, două uși.** Board-ul simulat a observat că A și G sunt **același motor**: termene puse de un profesionist, ținute la zi din exporturile programelor existente, cu un om care acționează și cu un jurnal. Diferă doar ușa:
- **A** e ușa rapidă la bani;
- **G** (controalele pierdute la clinicile cronice) e ușa strategică. Se deschide doar după referințe și audituri.

Motorul se construiește o singură dată, iar know-how-ul de citire a exporturilor fără API devine, în timp, singura barieră tehnică reală [Plauzibil].

**Ce trebuie să fie adevărat** (și se verifică în 90 de zile):
1. golul există: cel mult un vendor MM are portal sau remindere pentru angajator;
2. cabinetele plătesc: ≥3 pre-vânzări plătite;
3. piața accesibilă are ≥20 de cabinete independente;
4. exporturile se obțin în mai puțin de 30 de minute.

Dacă oricare dintre aceste condiții pică, conceptul se reduce (doar registrul și reminderele), se pivotează (OEM prin vendor) sau se oprește.

**Cum a evoluat conceptul sub review-urile simulate:**

| Runda | Cea mai grea obiecție | Probabilitatea de respingere | Ce s-a schimbat |
|---|---|---:|---|
| 1 | nicio dovadă reală de cerere; semnal simulat fragil | 85% | validare prin pilot concierge plătit și pre-vânzări; vendorii verificați primii; produsul redefinit din „portal” în „birou de continuitate”; model cu churn și retururi |
| 2 | activul de date nu e al fondatorului | 65% | guvernanța pe trei niveluri; etapa 3 ruptă în 3a (prognoză de capacitate, fără profilare) și 3b (doar cu bază legală); prevenția mutată „la examen, nu după”; un al doilea motor (ajutor part-time) cu poartă |
| 3 | cazul de investiție nu există încă | 60% | politică de finanțare scrisă; responsabil medical cu rol definit; regula de alegere din luna 18; măsurarea încorporată în produs; trepte de securitate |

## 10. Planul de validare în 90 de zile

**Principiul:** dovadă înainte de cod. Validarea măsoară plata și efectul, nu opiniile. Încape în **~150 h în 13 săptămâni**, la 10–12 h/săpt, pentru că taie drumurile fizice în afara Oradei (le înlocuiește cu video) și îngheață G.

### Cele trei faze

| Faza | Săptămânile | Ce se face | Ore |
|---|---|---|---:|
| **A** | 1–3 | discuții cu 5 vendori MM (6 h); lista nominală de 20 de cabinete independente, cu proprietarul verificat la ONRC/Termene și programul folosit (6 h); întrebările pentru avocat și cererea de ofertă de asigurare RC + cyber (3 h); 6 conversații fizice în Oradea (18 h); verificarea legislației consolidate: amenda din art. 39 al Legii 319/2006, periodicitatea din Anexa 1 a HG 355/2007, ce scrie pe exemplarul angajatorului | ~35 |
| **Poarta A (ziua 21)** | | **≥2 vendori au portal sau remindere pentru angajator → nu se construiește portalul** (OEM, doar registrul, sau stop). **Mai puțin de 3 din 6 cabinete confirmă durerea → oprire sau lărgirea segmentului** | |
| **B** | 4–8 | 9 conversații (6 pe video, 3 fizic, Cluj, Satu Mare, Arad, Timișoara, București; ~25 h); cel mult 5 audituri pe exporturi reale (10 h); prototip APEX + n8n pe date sintetice (25 h); oferta „pilot fondator” | ~60 |
| **Poarta B (ziua 60)** | | **≥3 pre-vânzări plătite** (≥39 €/lună, 3 luni în avans); ≥2 exporturi funcționale obținute în sub 30 de minute; ≥20 de cabinete independente pe listă | |
| **C** | 9–13 | pilot concierge la 2–3 cabinete plătitoare (~35 h); începutul MVP (20 h) | ~55 |
| **Poarta C (ziua 90)** | | **GO / PIVOT / NO-GO** (mai jos) | |

### Pe cine întrebi

| Ținta | Câți | Ce afli |
|---|---:|---|
| Cabinete MM independente din Oradea: Medimun, Carimed, Endodigest, Alfa Medica, Gecoprosana, Neoklinik | 6 | durerea, programul folosit, cum țin scadențele, orele asistentei, exportul |
| Firme MM din afara Oradei (Cluj, Satu Mare, Arad, Timișoara, București) | 9 | dacă vânzarea la distanță funcționează; segmentul firmelor medii |
| Vendori MM: Setrio (BizMedica MM), DMV Consult (MedExam), Qmedical, Charisma, MedSoft | 5 | au portal sau remindere pentru angajator? ce export permit? ar accepta un parteneriat (integrare, revânzare, OEM)? |
| Angajatori din rețeaua fondatorului (HR în parcurile industriale) | 3–5 | ar folosi accesul la status? cum programează azi examenele? au avut controale ITM? |
| Avocat (GDPR și sănătate) | 1 | ce vede angajatorul; dacă reminderele sunt comunicare comercială (Legea 506/2004); DPA; sub-procesatori |
| Broker de asigurări | 1 | o ofertă reală RC profesională + cyber; dacă trece de ~1.200 €/an, se refac numerele |
| Medic MM, posibil responsabil medical | 1–2 | dacă ar accepta rolul; clasele de termen ale recomandărilor |

**G nu se auditează în aceste 90 de zile.** Dacă o clinică cronică cere un audit, se notează și se răspunde după luna 12.

### Întrebările de descoperire

| Întrebarea | De ce o pui |
|---|---|
| Ce program MM folosiți și cum exportați lista de angajați, cu data ultimului examen? Puteți face exportul acum? | testează golul de integrare și metrica „export în <30 min” |
| Cum aflați azi ce fișe expiră luna viitoare? Cine sună angajatorii și cât durează asta pe săptămână? | cuantifică durerea în ore; se cere jurnalul de o săptămână, nu o estimare din memorie |
| Câte fișe sunt acum expirate sau expiră în 30 de zile? (răspunsul vine din auditul pe export) | produce primul număr local real |
| Ce se întâmplă cu recomandările „apt condiționat” după examen? Cine verifică închiderea lor? | testează valoarea registrului |
| Ați pierdut în ultimii 2 ani un angajator în favoarea unei rețele? De ce a plecat? | testează argumentul „client păstrat” (un angajator de 300 de oameni ≈ 4.700 €/an, calculul din v2) |
| Ce cer angajatorii la renegociere? Le trimiteți vreun raport? | testează raportul de renegociere |
| Ce date ați accepta să încărcați pe o platformă externă și ce v-ar liniști (DPA, găzduire în UE, export oricând)? | testează obiecția de încredere |
| Programul MM are un portal sau remindere pentru angajator? L-ați cere vendorului? | verifică golul de la client, nu doar de la vendor |
| Ați plăti 79 €/lună ca asistenta să nu mai sune angajatorii? Și 3 luni în avans, cu garanție? | prețul și plata reală; se compară 69 € cu 89 € pe treapta standard |
| Ați refactura angajatorilor un „serviciu digital de conformitate”? | ipoteza de refacturare, tratată ca bonus, nu ca premisă |
| Faceți examene la sediul angajatorilor? Cum planificați zilele de deplasare? | deschide modulul de dispecerat |
| Ar cumpăra angajatorii voștri teste suplimentare făcute în aceeași vizită? | deschide modulul de prevenție |

### Designul pilotului concierge

**Participanți:** 2–3 cabinete plătitoare, cu garanție doar pentru cele calificate (export funcțional și cel puțin un angajator care vrea acces).

**Linia de bază:** auditul inițial, cu fișele expirate, zilele medii de întârziere, recomandările închise la 90 de zile și orele asistentei pe săptămână, măsurate printr-un jurnal de o săptămână.

**Ce face fondatorul:** rulează reminderele pe e-mail către HR cu prototipul APEX + n8n și trimite angajatorilor un PDF de status săptămânal.

**Comparația:** angajatorii fiecărui cabinet sunt porniți în valuri, iar cei care încep mai târziu servesc drept comparație.

**Ce se măsoară:**
- procentul de examene programate înainte de expirare, față de linia de bază;
- orele de asistentă economisite;
- câți HR răspund și câți cer acces;
- timpul de curățare a datelor.

### Scopul MVP-ului

**Intră în MVP:** import cu raport de calitate, calendar cu regula examenului de reluare, remindere pe e-mail, registru vizibil doar cabinetului, statusuri cu grație, banner de prospețime, jurnal de audit, export lunar.

**Rămâne pe dinafară** până la porțile ulterioare: portalul angajatorului (doar după opinia juridică), SMS-ul (doar cu consimțământ înregistrat), orice modul de prevenție, orice predicție, G.

### Bugetul

**Numerar pentru validare: ~1.000 €.** Acoperă întrebările juridice inițiale, deplasările, găzduirea prototipului și creditele de e-mail/SMS.

**Pornirea completă: ~3.580 €.** Include avocat ~1.200 €, opinie juridică ~600 €, revizie de securitate ~800 €, găzduire, deplasări și SMS. **Vârful de numerar: ~4.060 €.** Toate sunt estimări, fără oferte reale.

**Ore: ~150.**

### Metricile de GO / NO-GO

| Metrica | GO | NO-GO |
|---|---|---|
| Vendori MM cu portal sau remindere pentru angajator | 0–1 | ≥2 (golul nu există) |
| Cabinete din Oradea care confirmă durerea | ≥3 din 6 (ziua 21); ≥6 din 15 în total | ≤3 din 15 |
| Cabinete independente accesibile pe listă | ≥20 | <10 |
| **Pre-vânzări plătite la ≥39 €/lună** | **≥3 până în ziua 60** | **≤1 până în ziua 75**; conversie <10% din conversațiile calificate |
| Exporturi funcționale în <30 min | ≥2 cabinete | 0 |
| Timpul de curățare a datelor la primul pilot | ≤10 h | >20 h |
| Efectul în pilot | examene programate înainte de expirare peste linia de bază **sau** ore de asistentă economisite | niciun efect măsurabil |
| Angajatori care ar folosi accesul | ≥3 | 0 |
| Opinia juridică | permite cel puțin statusul pentru angajator | interzice și statusul → produsul se reduce la registru și remindere |
| Orele fondatorului | ≤12 h/săpt | >15 h/săpt timp de 2 luni → se taie din funcții, nu se adaugă ore |

**Decizia din ziua 90:**
- **GO** dacă există ≥3 pre-vânzări plătite **și** ≥2 exporturi funcționale **și** golul e confirmat **și** pilotul arată un efect măsurat.
- **PIVOT** dacă golul există, dar cabinetele nu plătesc. Variante: parteneriat de revânzare cu un vendor MM, sau un nivel de autoservire la ~19 € pentru angajatorii „speriați de ITM”, folosit ca sursă de clienți pentru cabinete.
- **NO-GO** dacă sunt <2 pre-vânzări după ≥15 conversații **sau** dacă ≥2 vendori au deja portalul. Atunci scorarea se reface cu date reale. G trece în față doar dacă un audit G ulterior iese puternic.

## 11. Foaia de parcurs pe trei ani

Luna 1 = noiembrie 2026. Cifrele de MRR sunt din `bulletproof/model_36m.py`: scenariul de bază și, între paranteze, cel pesimist. Toate sunt **estimări**. Porțile decid dacă se trece la etapa următoare, nu calendarul.

| Perioada | Produsul | Clienți și MRR (bază / pesimist) | Echipa și banii | Calendarul extern |
|---|---|---|---|---|
| **Lunile 0–3** (nov. 2026 – ian. 2027) | validare: vendori, audituri, prototip, pilot concierge; începutul MVP | 3 piloți plătitori în luna 3; ~222 € MRR | fondator 10–12 h/săpt; pornire ~3.580 €; opinie juridică; ofertă de asigurare | 3.12.2026: votul SANT pe reforma MDR (programat); **9.12.2026: PLD**, software-ul devine produs; T4 2026: e-SănătateaMea obligatoriu pentru programările furnizorilor CNAS |
| **Lunile 4–6** (feb. – apr. 2027) | MVP în producție: import, calendar, remindere, registru, jurnal, export lunar | ≥5 cabinete plătitoare în luna 6; ~409 € MRR | treapta 1 de securitate; contract-tip cu plafon de răspundere | **26.03.2027: EHDS se aplică general**; acte de punere în aplicare |
| **Lunile 7–12** (mai – oct. 2027) | portalul angajatorului (cât permite opinia juridică); raportul de renegociere; al doilea adaptor; plata anuală | **luna 12: ≥8 clienți** (bază ~10, ~758 €; pesimist ~5, ~304 €) | căutarea responsabilului medical; numit până în luna 12 (poartă) | — |
| **Lunile 13–18** (nov. 2027 – apr. 2028) | tabloul indicatorilor (nivelul B, linia de bază); treapta 2 de securitate la 10 clienți; prima discuție cu un vendor MM | **luna 18: ≥12 clienți și MRR ≥1.000 €** (bază ~17, ~1.280 €; pesimist ~518 €) | ajutor part-time (~20 h/lună, ~400 €) dacă: ≥12 clienți, CAC ≤20 h, churn <2%/lună | **2.12.2027: AI Act Anexa III** (triaj, prețuri de asigurare); 11.12.2027: obligațiile CRA pentru produsele descărcabile |
| **Lunile 19–24** (mai – oct. 2028) | **un singur modul, după regula din luna 18**: prevenția la examen sau dispeceratul; notă de calificare MDR; prima măsurătoare cu comparație | **luna 24: MRR ≥1.700 €** (bază 1.747 € fără modul / 2.171 € cu modul; pesimist ~791 €); modulul la ≥15% din clienți | grant nediluant pentru evaluare; partener academic | **2.08.2028: AI Act Anexa I** (AI în dispozitive medicale); adoptarea reformei MDR posibil în 2027–2028 |
| **Lunile 25–36** (nov. 2028 – oct. 2029) | modulul se maturizează; al doilea modul doar la ~20 h/săpt; G se deschide doar la porți | **luna 36: MRR ≥2.500 €** (bază 2.562 € fără modul / **3.185 €** cu modul, 3.000 € în luna 34; pesimist ~1.111 €); ~35 de clienți (pesimist ~15) | decizia din luna 36: normă întreagă sau nu; primul angajat din venit sau din grant | **26.03.2029: EHDS grupa 1** (rezumate, rețete; sisteme EHR conforme); folosirea secundară a datelor de la ~2029 |

**Numerele de ansamblu** (calculul din `bulletproof/model_36m.py`):

| Indicator | Pesimist | Bază, fără modul | Bază, cu modul (ipoteză) |
|---|---:|---:|---:|
| Profit operațional anul 1 | −1.031 € | +1.747 € | +1.747 € |
| Luna cu 1.000 € MRR | 32 | 15 | 15 |
| Luna cu 3.000 € MRR | niciodată | niciodată | 34 |
| Clienți în luna 36 | ~15 | ~35 | ~35 |
| Cel mai adânc punct al numerarului | −4.675 € | −4.060 € | −4.060 € |
| Profit cumulat la 36 de luni, după pornire | −781 € | +18.556 € | +26.358 € |

**Cum se citesc numerele.** Scenariul pesimist e exact cel pe care îl prinde poarta din luna 12 (<8 clienți). Dacă se întâmplă, planul pivotează sau se oprește înainte să piardă bani. Scenariul de bază depinde de patru ipoteze nedovedite:
- 3 piloți plătiți în luna 3;
- un preț mediu de ~74 €;
- un ajutor part-time din luna 13, cu un CAC ≤15 h;
- un modul adoptat de 30% dintre clienți, la ~60 €.

Fiecare are o poartă care o testează.

**Ce se urmărește, dar nu se așteaptă:**
- pregătirea României pentru EHDS (autoritatea de sănătate digitală, HDAB, profilurile FHIR);
- un eventual API e-SănătateaMea pentru terți;
- apelul la CJUE privind cadrul UE–SUA de transfer de date (DPF), cu Microsoft admis ca intervenient pe 4.06.2026 ([DataGuidance](https://www.dataguidance.com/news/eu-cjeu-admits-microsoft-intervener-appeal-concerning)), care contează pentru alegerea furnizorului de LLM;
- transpunerea PLD în România, la care s-au raportat doar „măsuri pregătitoare” ([Howden Re](https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-04/Howden%20Re%20Casualty%20in%20focus%20%234%20-%20%20the%20new%20EU%20product%20liability%20directive%20%26%20AI%20April212026.pdf)).

**Extinderea în Europa** e o întrebare pentru anii 3–7 și **n-a fost cercetată** pentru medicina muncii din alte țări. Tiparul care a mers în regiune spune: întâi rezultate publicate pe același cumpărător, abia apoi alte țări. O nișă de limbă maghiară, transfrontalieră, din Bihor e doar o ipoteză [Speculativ].

## 12. Lacune și incertitudini: ce trebuie încă aflat

| Lacuna | De ce contează | Cum se închide | Tipul | Când |
|---|---|---|---|---|
| Au programele MM (BizMedica MM, MedExam, Qmedical, Charisma, MedSoft) portal sau remindere pentru angajator? | dacă da, golul lui A dispare | discuție sau demo cu fiecare vendor | interviu | ziua 21 |
| Câte cabinete MM independente sunt accesibile în Nord-Vest, cine le deține, ce program folosesc | plafonul pieței și rampa | ONRC/Termene + telefoane | cercetare de piață | ziua 21–60 |
| Plătesc cabinetele independente? Cât timp pierde asistenta? Câte fișe sunt expirate? | toată cererea e azi simulată | pre-vânzări, audituri pe exporturi, jurnal de o săptămână | interviu + test plătit | ziua 60–90 |
| Suma actuală a amenzii din art. 39 (Legea 319/2006), periodicitatea din Anexa 1 (HG 355/2007), conținutul exemplarului angajatorului | argumentul de vânzare și volumul de evenimente | legislația consolidată | juridic | ziua 21 |
| Ce are voie să vadă angajatorul; dacă recomandările deschise sunt date de sănătate indirecte | forma portalului | opinie juridică | juridic | ziua 90 |
| Sunt reminderele către angajați comunicare comercială (Legea 506/2004)? | canalul SMS | opinie juridică | juridic | ziua 90 |
| Validitatea consimțământului angajatului; clauza din DPA pentru indicatori anonimizați (Recitalul 26) | nivelurile B și C de date | opinie juridică | juridic | luna 12 |
| Baza legală pentru „pe cine suni primul” (Legea 190/2018 art. 3; DPIA) | etapa 3b | opinie juridică + DPIA | juridic | luna 30 |
| Calificarea MDR a modulului de prevenție și a buclelor G (exemplele din MDCG 2019-11 Rev.1) | granița categoriei 1 | notă scrisă cu un consultant MDR (~800 €, estimare) | juridic / reglementare | înainte de luna 19 |
| Regimul fiscal al prevenției plătite de angajator (serviciu MM sau beneficiu în plafonul de €400) | cine plătește modulul și cum | contabil | fiscal | luna 18 |
| Transpunerea PLD în România; anexele OUG 155/2024 și termenele de notificare NIS2; termenele de păstrare a dosarelor; înregistrarea software-ului la CNAS | răspundere și contracte | avocat | juridic | lunile 3–12 |
| Formatele de export ale programelor MM; timpul de curățare; acuratețea mapării coloanelor cu LLM | costul onboarding-ului | primele 2 piloți | tehnic | ziua 60–90 |
| Tarifele agregatorilor români de SMS; costul WhatsApp Business | marja (SMS-ul absorbit de fondator trece anul 1 pe pierdere) | oferte de la agregatori | tehnic / comercial | ziua 60 |
| Costul testului de penetrare și al certificării ISO 27001 pentru o firmă micro | treptele de securitate | oferte | tehnic | luna 12 |
| Clasele de termen ale recomandărilor; meniul de teste din aceeași vizită; protocolul pentru constatări anormale | conținutul clinic al modulului | responsabilul medical (medic MM) | clinic | lunile 6–18 |
| Designul de măsurare (pornire în valuri), etică, publicare | dovada care deschide „cazul de fond” | partener academic (Facultatea de Medicină din Oradea, neverificată) | clinic / cercetare | lunile 12–24 |
| Datele românești despre urmarea rezultatelor, pozitivitatea FIT în Nord-Vest, acoperirea screeningului | dimensiunea golului pentru G și E | audituri G; datele ROCCAS | cercetare | după luna 12 |
| Plata CNAS pe serviciu de prevenție pentru medicul de familie | ar redeschide H | normele CNAS | cercetare | oricând |
| Volumul turismului dentar în Bihor | viabilitatea lui K | interviuri cu clinicile | interviu | opțional |
| Pregătirea României pentru EHDS (HDAB, autoritate, profiluri FHIR); API e-SănătateaMea | etapa 4 și Q | monitorizare | cercetare | anual |
| Dovezile științifice deschise: rezultatele Heartline; cifrele exacte din Lancet pentru MASAI; articolul revizuit NHS-Galleri | calibrarea viziunii 2030–2040 | literatură | cercetare | anual |
| Prețurile vendorilor europeni de rechemare; plățile reale ale clinicilor românești | ancorele de preț | interviuri, oferte | comercial | pe parcurs |

**Limitele metodei, spuse încă o dată.** Faptele vin din rezumate de căutare. Unele afirmații sunt cunoștințe de fond marcate (BK/PK). Board-ul, panelurile și review-urile au fost simulate. Prețurile, rampele și costurile sunt estimări fără oferte reale. Niciun cumpărător nu a fost întrebat. Cea mai mare incertitudine nu e tehnică și nici juridică: e **dacă un cabinet independent de medicina muncii plătește 39–149 € pe lună** pentru munca pe care azi o face asistenta cu Excel-ul și telefonul.

## Răspunsuri directe

### a) Dacă aș fi în locul tău, în România, în 2026, ce afacere de software medical aș construi întâi și de ce?

**Biroul de continuitate pentru cabinetele independente de medicina muncii.** Motivele, în ordinea importanței:
1. **Are un plătitor cu obligație legală.** Angajatorul plătește examenul periodic pentru fiecare salariat, de regulă anual, sub amenințarea amenzii. Nu trebuie să inventezi un buget.
2. **E administrativ.** Ceasul e al medicului sau al legii, nu al software-ului. Asta te ține în afara MDR, a scorurilor de risc și a profilării.
3. **Cumpărătorii sunt la distanță de mers cu mașina.** Medimun, Carimed și Endodigest sunt în Oradea.
4. **Te costă puțin.** ~3,6k € la pornire și un vârf de numerar de ~4,1k € din cei 25k €.
5. **Construiește exact activele de care are nevoie o afacere de prevenție.** Relația cu contactul obligatoriu, istoricul buclelor, know-how-ul de citire a exporturilor fără API, un responsabil medical și o metodă de măsurare.

**Ce înseamnă concret.** Aș începe săptămâna aceasta cu 6 vizite în Oradea și 5 telefoane la vendori, nu cu cod. Aș trata rezultatul ca pe un test cu dată de expirare: dacă în ziua 21 sau în ziua 60 porțile pică, mă opresc sau pivotez. Aș accepta de la început că e **o afacere de nișă înainte de a fi o platformă**: în scenariul de bază, 1.000 € MRR vine în luna ~15–19 și doar dacă porțile ies.

### b) Ce oportunități să eviți explicit, deși par futuriste?

Evită ca prim produs (și, la bugetul acesta, ca produs propriu în general):
- **Un model predictiv propriu sau un model fundațional pe dosare.** Doar acuratețe retrospectivă (Delphi-2M, Foresight); date inaccesibile; MDR include explicit „predicția”.
- **Calculatoarele SCORE2/QRISK/FINDRISC în fluxul medicului.** Clasa IIa; UE nu are excepție pentru suportul decizional.
- **Chatbot-urile de triaj și verificatoarele de simptome.** Clasa IIa+; Anexa III din AI Act de pe 2.12.2027; Platform24 a ajuns sub supravegherea regulatorului.
- **RPM-ul cu alerte automate.** IIa/IIb; nicio rambursare în România; în SUA, 43% dintre pacienții Medicare cu RPM n-au primit serviciul complet.
- **PHR-ul sau „portofelul de sănătate” pentru consumator.** Google Health și HealthVault au închis.
- **Abonamentele de analize direct la consumator, de tip Function.** În România, laboratoarele sunt chiar mărcile de consum; Aware a intrat în insolvență.
- **Clinicile de scanare de corp întreg, de tip Neko, și interpretarea RMN de corp întreg.** Capital de ordinul sutelor de milioane; ACR recomandă împotrivă; 94% dintre scanați au o anomalie.
- **Testele multi-cancer din sânge ca produs.** Primul RCT și-a ratat criteriul principal.
- **Tablourile de stratificare a riscului vândute ca „reduc internările”.** PRISMATIC le-a crescut.
- **Scribul AI general în română.** Tandem a strâns $160M, Heidi ~$340M, iar funcțiile avansate alunecă în IIa.
- **Gemenii digitali** (cercetare, capital) și **platformele de federated learning** (problemă de guvernanță, nu de cod).
- **Exportul prin căile germană (DiGA) sau franceză (PECAN).** Cer marcaj CE și RCT.

Evită ca **prim** produs, chiar dacă sunt mai puțin futuriste:
- puntea spre e-SănătateaMea, până apare un API;
- navigatorul FIT pentru ROCCAS (un singur cumpărător, achiziții UE);
- reminderele generice, care sunt deja marfă.

### c) Care e cel mai ieftin mod de a obține dovada că cineva plătește?

**Pasul 1, aproape gratuit: poarta din ziua 21.** Discuții cu cei 5 vendori MM și 6 conversații în Oradea, cu întrebarea „puteți face exportul acum?”. Cere ~35 h și practic 0 €. Poate omorî ideea înainte să scrii o linie de cod: dacă doi vendori au deja portalul pentru angajator, te oprești.

**Pasul 2: pre-vânzarea plătită.** Primele 3 luni plătite în avans, la prețul de listă, rambursabile prin garanție, oferite **după** un audit gratuit pe exportul real al cabinetului. Auditul arată câte fișe sunt expirate și câte recomandări n-au fost închise. Toată validarea de 90 de zile costă **~1.000 € numerar și ~150 h**.

**Ce nu contează ca dovadă:**
- scrisorile de intenție;
- „da, ar fi util”;
- panelurile simulate.

Contează doar banii și un efect măsurat în pilot: examene programate înainte de expirare peste linia de bază, sau ore de asistentă economisite, măsurate cu un jurnal de o săptămână.

### d) Ce oportunități pot aduce realist 1.000–3.000 € MRR înainte să ai nevoie de echipă?

**A (biroul de continuitate) ajunge la 1.000 € MRR:**
- fără niciun ajutor (planul v1), în luna ~19;
- cu un colaborator part-time din luna 13 (planul final), în luna ~15;
- în scenariul pesimist, abia în luna 32.

**Plafonul lui A la 10–12 h/săpt e ~1.600 € MRR**, la ~25 de clienți. **3.000 € MRR apare în luna ~34**, dar cere un colaborator part-time din luna 13 (~20 h/lună, ~400 €) și un modul de prevenție adoptat de ~30% dintre clienți. Strict vorbind, asta e o „echipă” minimă.

**G (controalele pierdute)** are un plafon de ~1.150 € MRR la 10–12 h/săpt și atinge 1.000 € abia în luna ~27. Anul 1 e pe pierdere.

**K (turismul dentar)** ar avea nevoie de 4–10 clinici la 99–249 € pentru 1.000 € MRR (calculul meu), dar volumul pe clinică e nedovedit.

**Celelalte:**
- **L (remindere)** poate ajunge aritmetic la cifre similare, dar e marfă, cu prețuri în scădere.
- **Q (componente EHDS)** aduce venit pe proiect (estimare: 5–15k € per vendor), nu MRR, și nu înainte de 2027–2028.
- **Serviciile din strategia A** aduc bani mai repede, dar ca venit pe proiect, nu ca MRR.

**Concluzia:** 1.000 € MRR e realist doar pentru A, și numai dacă trec porțile. 3.000 € MRR nu e realist la 10–12 h/săpt fără un colaborator sau un canal (un vendor MM care revinde).

### e) Ce produs de start are cel mai plauzibil drum spre o afacere mult mai mare de prevenție sau predicție?

**Tot A, citit corect.** Motivul principal: stă pe **singurul contact preventiv universal, obligatoriu, recurent și finanțat de angajator** pentru populația activă (5,76 milioane de salariați). Pe acel contact, produsul poate deveni **proprietarul buclei de răspuns**, adică exact locul în care dovezile arată că se creează beneficiul (EAGLE, ACCESS, TIM-HF2).

Drumul plauzibil are pași mici și verificabili:
1. **Prevenția la examen:** teste în aceeași vizită, constatări marcate de medic, un om care sună. Mecanismul ACCESS: 22% → 100%.
2. **Prognoza de capacitate pentru echipele mobile:** predicție operațională fără profilare.
3. **„Pe cine suni primul”:** doar cu bază legală și doar dacă bate „reminder pentru toți” cu grup de control.
4. **Din 2029:** găzduirea modelelor certificate CE ale altora, unde vendorul poartă MDR-ul, iar tu urmărirea, plus folosirea secundară a datelor prin EHDS.

**Alternativele:**
- **G** e mai aproape de prevenția clinică, dar are cea mai slabă dovadă de cerere (0/20 la prima ofertă simulată).
- **Q** e un drum de infrastructură, nu de predicție.

**Spus cinstit:** „mult mai mare” înseamnă aici un strat de prevenție plătit de angajatori, apoi găzduirea predicțiilor altora. Nu înseamnă o companie cu model propriu. Iar trecerea la scară cere declanșatori dovediți:
- modulele aduc ≥40% din MRR, cu MRR de cel puțin 5.000 €;
- un rezultat publicat;
- un contract cu o rețea medie, un vendor sau clienți din altă țară.

### f) Ce te-ar face să concluzionezi că nu ar trebui să intri deloc în tehnologia medicală?

**Semnale din piață:**
- **Golul nu există la cumpărătorii accesibili.** Cel puțin doi vendori MM au deja portal sau remindere pentru angajator, iar, mai târziu, auditurile la clinicile cronice arată sub 10 controale depășite pe clinică.
- **Nimeni nu plătește.** Cel mult o pre-vânzare după 15 conversații calificate, iar pivoturile (revânzarea prin vendor, nivelul de autoservire pentru angajatori) pică și ele.
- **Încrederea nu se poate câștiga.** Cabinetele și clinicile refuză să dea date unui SRL mic, chiar cu DPA, găzduire în UE, revizie de securitate și export garantat. Asta a fost primul motiv de refuz în panelurile simulate și trebuie testat real.

**Semnale despre tine:**
- **Economia timpului nu ține.** Nu poți susține constant 10–12 h/săpt, sau CAC-ul rămâne peste ~40 h pe client câștigat.
- **Nu vrei să porți obligațiile nenegociabile ale domeniului:** un medic responsabil, disciplina scopului declarat și a cuvintelor interzise, asigurarea RC + cyber, jurnalul de versiuni și patch-urile cerute de PLD, chestionarele de securitate NIS2, obligațiile de persoană împuternicită sub GDPR.
- **Singurele idei care te motivează sunt cele cu afirmații clinice** (model propriu, scoruri de risc, triaj). La 25k € și 10–12 h/săpt, acestea nu sunt fezabile.
- **Ai nevoie de un rezultat de tip fond de risc într-un orizont scurt.** Ecosistemul românesc trăiește din granturi, iar notele n-au găsit cumpărători activi de module healthtech, în afară de MedLife cu SanoPass.

**Ce faci atunci.** Competențele tale (date, integrare, APEX, automatizare) se vând mai repede și cu mai puțină răspundere în alte domenii reglementate, dar nemedicale.
