# PREVENT-NV v2: prevenție cu buclă închisă la locul de muncă, cu un modul clinic certificat

**Ce e documentul:** planul de proiect STEP (PR Nord-Vest, apelul 961 sau o fereastră ulterioară), rescris după `evaluare-plan-PREVENT-NV.md`. Păstrează echipa de 6 ENI, partenerii și checklist-ul din v1; schimbă nucleul, investiția, calendarul și modelul de venit. **Cerințele de proiect** sunt cele din transcrierea ghidului (`Transcriere_Regio_Nord_Vest_Primele_36_slideuri.docx`); maparea criteriu cu criteriu e în `proiect-STEP-PREVENT-NV-conformitate-ghid.md`.
**Ipoteze de lucru** (aceleași ca în v1, plus una): cofinanțarea nu e o problemă; există partener clinic și de cercetare; platforma și datele le construiești tu, cu AI; **ADR NV confirmă în scris încadrarea STEP și compoziția investiției înainte de depunere**.
**Atenție:** regulile apelului vin din transcriere și din rezumate de căutare; Corrigendum nr. 2 (8.10.2026) a modificat grila, valorile și pragul de calitate. Totul se recitește în ghidul consolidat. Sumele sunt estimări fără oferte.
**Data:** 12 octombrie 2026.

---

## 1. Planul pe o pagină

- **Teza.** În prevenție, beneficiul apare doar când un semnal (rezultat anormal, scor de risc, examen scadent) ajunge la o acțiune făcută și confirmată; cinci din cele șase puncte unde se pierde beneficiul sunt probleme de software și operațiuni, nu de model (raportul de sănătate, §2). PREVENT-NV construiește și dovedește **stratul care închide bucla**, la singurul contact preventiv recurent și plătit din România: **examenul de medicina muncii și pachetul de prevenție al angajatorului**.
- **Ce livrează proiectul (trei lucruri, nu șase):**
  1. **Platforma PREVENT-NV**: dosar longitudinal FHIR/IPS (pregătit pentru EHDS), extragere verificabilă din documente RO/HU, motor de termene și liste de lucru cu proprietar, măsurarea rezultatelor; integrare cu dispozitive certificate cumpărate.
  2. **Modulul clinic PRIORITY** (dispozitiv medical software, clasa IIa țintă): profil de risc cardiometabolic din scoruri validate (SCORE2, CHA2DS2-VASc, FINDRISC) cu calibrare locală, plus prioritizarea listei de lucru a clinicianului. Modelele ML noi rămân în cercetare până au dovezi.
  3. **Capacitatea fizică de prevenție**: unități mobile pentru „ziua de prevenție” la angajator (testul în aceeași vizită: 22% → 100% finalizare în ACCESS) și un centru de coordonare operat cu partenerul clinic.
- **Cercetarea care justifică art. 25:** întrebarea centrală e **„pe cine suni primul?”**: prioritizarea prin model a urmăririi bate reminderul pentru toți? Nu e dovedit în literatură (recenzia JAMIA citată în repo), deci e cercetare industrială reală, cu studiu controlat.
- **Plătitorul:** angajatorul, prin cabinetele de medicina muncii partenere (Bihor: 187,3 k salariați [INS, via repo]); al doilea val: clinici independente de boli cronice, asigurători privați; extern: Ungaria (Bihor e bilingv, iar Debrecen e la 70 km).
- **Echipa:** 6 ENI noi; directorul de proiect e din domeniu (reglementare/dispozitive medicale), fondatorul e arhitect și lider tehnic.
- **Bani:** grant ~5,5 mil. EUR, eligibil ~8,0 mil., cofinanțare ~2,4 mil. + TVA și decalaj de rambursare (vârf de numerar 3,5–4,5 mil. [ESTIMARE]).
- **Porți:** luna 6, 12, 18, 24, cu criterii de oprire scrise; plan B pentru certificare.

## 2. Încadrarea STEP (cum o scrie raportul CTT)

- **Tehnologia critică** (nu domeniul): infrastructură suverană de date de sănătate conformă EHDS (FHIR/IPS, jurnalizare, componente armonizate), **învățare federată** între organizațiile partenere fără centralizarea datelor, **extragere verificabilă** din documente medicale în limbi cu resurse puține (română, maghiară) cu modele rulate în UE. Sectorul: digital și deep tech (AI, date, securitate). Sănătatea e domeniul de aplicare.
- **Condiția (b), dependențe:** datele de sănătate ale regiunii stau azi în exporturi PDF și în platforme fără API; extragerea și modelarea prin API-uri non-UE scot datele din Uniune; proiectul le ține în regiune, pe infrastructură proprie.
- **Condiția (a), element inovator:** nimeni nu a dovedit că prioritizarea urmăririi prin model bate reminderul pentru toți; proiectul produce dovada într-un studiu controlat și publică protocolul și benchmark-ul (spillover, criteriul 4.4).
- **Referințe de dovezi în dosar:** ACCESS (finalizare 22% → 100% la testul în aceeași vizită), EAGLE (49,6% urmare după semnal), PRISMATIC (stratificare fără acțiune a crescut utilizarea), TIM-HF2 (centru cu oameni, HR ~0,70 mortalitate) — toate din notele repo-ului, de citat cu sursele primare.
- **Întrebarea 1 pentru ADR NV** se pune exact așa, cu descrierea tehnologiei de mai sus, nu cu „platformă de prevenție”.

## 3. Pachetele de lucru (ce construiește fiecare și cu ce competență a ta)

| WP | Ce | Întrebarea de cercetare / rezultatul | TRL | Linia | Competența ta folosită |
|---|---|---|---|---|---|
| **WP0 Management** | achiziții (Ordin 1284), raportări, cereri de rambursare, vizibilitate MIV | — | — | minimis | n8n pentru calendarul de repere și dosarul de rambursare (același motor ca în ideile de implementare din repo) |
| **WP1 Dosarul longitudinal** | FHIR/IPS, identitate, consimțământ, jurnal de acces, calitatea datelor măsurată; conectori pentru exporturi CSV/PDF ale partenerilor | cum construiești dosar longitudinal din surse fără API, cu scor de calitate per înregistrare | 3→7 | cercetare industrială | **Oracle/APEX + ORDS** ca fațadă FHIR REST și tablou; **PL/SQL** pentru reguli de calitate și cohorte |
| **WP2 Extragere verificabilă** | valori, recomandări, diagnostice din PDF-uri RO/HU, cu sursa citată, grad de încredere, validare umană; benchmark deschis | precizia modelelor mici rulate în UE față de API-uri mari, pe documente reale | 3→7 | cercetare industrială | **Python + LLM** (extragere cu proveniență), evaluare, interfață de validare în APEX |
| **WP3 Motorul de buclă** | termene puse de medic/program, proprietar, escaladare, închidere jurnalizată; liste de lucru; mesaje RO/HU | care configurație de proprietar + termen + canal maximizează închiderea la 90 de zile | 4→8 | dezvoltare experimentală | **n8n** pentru fluxuri și escaladare, **APEX** pentru listele de lucru; e miezul competenței tale |
| **WP4 PRIORITY, modulul clinic** | scoruri validate cu calibrare locală; prioritizarea listei; monitor de drift și performanță | cât de bine se transferă SCORE2/FINDRISC pe cohorta regională; ce calibrare e necesară | 4→7 | dezvoltare experimentală + art. 28 (certificare) | **Python** (calibrare, monitorizare), QMS și IEC 62304 cu responsabilul de calitate |
| **WP5 „Pe cine suni primul”** | modelul de prioritizare a urmăririi vs. reminder pentru toți; studiu controlat (randomizare pe angajatori sau design în trepte); învățare federată între parteneri | prioritizarea prin model crește închiderea buclei și reduce timpul de personal? | 3→7 | cercetare industrială | **Python/ML**, design de studiu cu universitatea; datele rămân la fiecare partener |
| **WP6 Capacitate și dispecerat** | prognoza de volum pe sediu, planul deplasărilor unităților mobile, umplerea anulărilor | predicție operațională (volum, nu persoană) care crește examenele pe deplasare | 4→7 | dezvoltare experimentală | **SQL/Python** pe date operaționale; legal curată (nu profilează persoane) |
| **WP7 Pilot și măsurare** | 2–3 cabinete MM + 1 clinică + 1 laborator din Bihor; 150–300 de participanți; linia de bază la onboarding; rezultate la 90 de zile | efectul pe închiderea recomandărilor, examene la termen, teste finalizate | 5→8 | dezvoltare experimentală | tabloul de rezultate (APEX), export pentru publicare |
| **WP8 Calitate și reglementare** | ISO 13485, IEC 62304, ISO 14971, dosar tehnic MDR, DPIA, ISO 27001 sau echivalent, pregătire AI Act (2.08.2028) | — | — | art. 28 + dezvoltare experimentală | — (responsabilul de calitate conduce; tu furnizezi documentația tehnică generată din cod și pipeline) |

**Ce a ieșit față de v1:** WP6 hub hardware (înlocuit de dispozitive certificate cumpărate), modelele de risc proprii ca livrabil certificat (rămân cercetare în WP5), centrul de monitorizare 24/7 (devine centru de coordonare în orar de lucru, operat cu partenerul).

## 4. Investiția (art. 14): active cu utilitate evidentă

| Activ | De ce e necesar producției serviciului | Cantitate | Valoare eligibilă [ESTIMARE, de confirmat cu 3 oferte] |
|---|---|---|---|
| **Unități mobile de prevenție** (vehicul amenajat: ECG 12 derivații, spirometru, audiometru, analizor point-of-care, tensiometre validate, cântar/bioimpedanță, conectivitate) | „ziua de prevenție” la angajator; testul în aceeași vizită; sursa de date pentru WP4–WP6 | 4 (2 în anul 1, 2 în anul 2, după poarta din luna 12) | 1.600.000–1.800.000 |
| **Centrul de coordonare** (spațiu amenajat, stații, telefonie, ecrane, sistem) | locul unde listele de lucru devin apeluri și programări; operat cu partenerul clinic | 1 | 500.000–650.000 |
| **Mediul securizat de date** (servere, stocare criptată, HSM, redundanță, colocare în regiune) la dimensiunea pilotului + creștere | datele nu părăsesc UE; cerință pentru EHDS și pentru argumentul STEP | 1 | 500.000–650.000 |
| **Dispozitive certificate pentru pacienți** (tensiometre, ECG cu o derivație, cântare conectate) | monitorizare acasă pentru grupul cu risc, în pilot și în extindere | 600–900 buc. | 250.000–350.000 |
| **Active necorporale numite** (licență algoritm CE pentru fibrilație, terminologii, platformă QMS, instrumente de securitate) | cumpărate la preț de piață de la terți nelegați, amortizabile, păstrate 3 ani | — | 500.000–700.000 |
| **Total art. 14** | | | **~3.600.000–4.100.000** → grant ~2.350.000–2.700.000 la 65% |

**Atenție la minimul de 3 mil. grant pe art. 14** (din transcriere, de verificat după Corrigendum 2, care a modificat secțiunea 5.4). Dacă minimul rămâne 3 mil., investiția eligibilă trebuie să fie ~4,6 mil.: se adaugă a 5-a și a 6-a unitate mobilă (+800 k) sau se mărește stocul de dispozitive, **numai dacă planul de afaceri arată cerere** (angajatori cu scrisori de intenție pentru zilele de prevenție). Nu se umflă centrul de date.

## 5. Echipa (6 ENI) și guvernanța

| # | Rol | Normă | Ce face | Criteriul acoperit | Cost lunar [ESTIMARE] |
|---|---|---|---|---|---:|
| 1 | **Director de proiect = responsabil calitate și reglementare** (5+ ani dispozitive medicale) | 1,0 | QMS, dosar MDR, DPIA, relația cu organismul notificat; conduce proiectul | 2.1.a (director 5 ani în domeniu); PRRC (poate fi și extern, MDR art. 15(2)) | 4.500 € |
| 2 | **Arhitect și lider tehnic (tu)** | 1,0 | arhitectura, WP1–WP3, integrarea dispozitivelor, pipeline-ul de date, documentația tehnică | personal propriu de cercetare | 4.000 € |
| 3 | **Cercetător ML / date clinice** (doctorat sau doctorand) | 1,0 | WP4, WP5, calibrare, monitorizare, studiul | 2.1.b sau c; cercetare cu personal propriu | 4.500 € |
| 4 | **Inginer de date / NLP** | 1,0 | WP2, WP6, conectori, benchmark | 2.1.c | 3.800 € |
| 5 | **Dezvoltator software** (verificare independentă IEC 62304) | 1,0 | dezvoltare, teste, verificare, întreținere | separarea rolurilor | 3.500 € |
| 6 | **Manager de proiect** (5+ ani, ≥2 proiecte UE ≥100 k EUR) | 1,0 | achiziții, rambursări, raportări, coordonarea pilotului și a flotei | 2.1.e; 2.1.d dacă are management operațional | 3.500 € |
| **Total** | | **6 ENI** | | | **~23.800 €/lună** |

**De la parteneri (contract, nu angajați):** medic coordonator de medicina muncii și un cardiolog (protocoale, meniul testelor, textele mesajelor), asistente pentru centrul de coordonare și unitățile mobile, echipa de studiu, cercetători universitari (cercetare contractată), laborator partener, organism notificat, consultant de scriere/implementare (fără conflict de interese cu furnizorii).

**Guvernanță:** comitet de proiect lunar cu partenerul clinic și universitatea; comitet de etică și siguranță (medic, DPO, responsabil calitate) care aprobă orice listă, mesaj sau regulă înainte să ajungă la pacienți; regula anti-PRISMATIC scrisă: **nicio listă fără proprietar, termen și metrică de închidere**.

## 6. Datele și temeiul legal (ce se numește în dosar)

| Sursa | Cum intră | Temei |
|---|---|---|
| Fișele și examenele de medicina muncii ale cabinetelor partenere | export CSV/Excel/PDF → WP2 | cabinetul e operator (art. 9(2)(h)), tu ești persoană împuternicită (DPA) |
| Rezultatele laboratorului partener | export sau API dacă există | la fel |
| Dispozitivele din pilot și unitățile mobile | API/SDK al producătorilor | consimțământ explicit al participantului (pilot) |
| Modelele WP5 (profilare pe date de sănătate) | învățare federată; datele nu se centralizează | **Legea 190/2018 art. 3**: consimțământ explicit sau temei legal expres; cercetare cu partener academic (art. 9(2)(j)), comisie de etică, DPIA |
| Date naționale (SIUI, e-SănătateaMea, DES) | **nu** | nu există acces pentru terți; nicio promisiune în dosar |

## 7. Calendar cu porți (implementarea se termină la 31.12.2029)

| Perioadă | Ce se întâmplă | Poartă / criteriu de oprire |
|---|---|---|
| **Acum → depunere** | e-mail ADR NV (încadrare, art. 14, MDR eligibil, fereastră viitoare); GAL/OJFIR (cumul minimis DR-36, compatibilitate); prototip construit de tine cu AI (dosar FHIR de test, extragere din 3 PDF-uri reale, listă de lucru, tablou); partener clinic și universitate; director și manager găsiți; raport CTT, raport expert contabil, scrisori de intenție (≥5 angajatori, 2–3 cabinete MM, 1 partener din Ungaria), oferte | fără răspuns pozitiv la întrebarea 1 și 2 de la ADR NV → nu se depune în forma asta |
| **Contractare** | 961: realist T2–T3 2027; fereastră ulterioară: decalaj | — |
| **Lunile 1–6** | angajări; QMS pornit (ISO 13485); platforma v1 (WP1, WP3); acorduri de date și aviz de etică; contracte dispozitive; prefinanțare; prima unitate mobilă comandată | **Poarta 6:** acorduri de date semnate cu ≥2 cabinete MM + 1 clinică; aviz de etică obținut; ≥3 angajatori cu contract de zi de prevenție. Altfel: re-scope pe clinici și laborator, fără unități mobile suplimentare |
| **Lunile 7–12** | WP2 v1 (extragere RO/HU); WP4 v1 (scoruri + calibrare, în regim de cercetare); centrul de coordonare amenajat; 2 unități mobile operaționale; primele zile de prevenție; linia de bază măsurată | **Poarta 12:** ≥150 de participanți cu linie de bază; QMS auditabil; organism notificat contactat cu dosar preliminar. Altfel: a 3-a și a 4-a unitate nu se mai cumpără |
| **Lunile 13–18** | studiul WP5 pornește (randomizare pe angajatori); monitor de drift; dosarul tehnic MDR; ISO 27001 sau echivalent | **Poarta 18:** ≥300 de participanți; rata de închidere la 90 de zile măsurată față de linia de bază; dosar tehnic complet |
| **Lunile 19–24** | rezultatele intermediare WP5; auditul organismului notificat; extindere la clinici și asigurători; parteneriat Ungaria activat | **Poarta 24:** WP5 arată efect sau non-inferioritate cu mai puțin timp de personal; audit programat. Altfel: PRIORITY rămâne unealtă de organizare, fără afirmații predictive |
| **Lunile 25–30** | certificare (țintă); raport final; primii clienți plătitori în afara pilotului; publicare; cererea finală de rambursare | **Plan B certificare:** dacă organismul notificat nu închide până în luna 30, produsul se vinde ca unealtă administrativă (categoria 1), iar certificarea se termină în durabilitate din venituri + art. 28 rămas |
| **2030–2032** | durabilitate: 6 ENI menținute, flota și centrul în operare, raport anual; AI Act Anexa I (2.08.2028) deja acoperit în dosar | — |

## 8. Bugetul (estimare, de refăcut cu oferte)

| Linie | Ce include | Eligibil | Intensitate [P7] | Grant | Cofinanțare |
|---|---|---:|---:|---:|---:|
| **Cercetare industrială (art. 25)** | salarii WP1, WP2, WP5 (~55% din timpul echipei), cercetare contractată universitate (~350 k), date, calcul | 1.600.000 | 80% | 1.280.000 | 320.000 |
| **Dezvoltare experimentală (art. 25)** | salarii WP3, WP4, WP6, WP7, WP8 (~45%), studiul pilot la parteneri (~350 k), personal medical contractat pentru pilot (~250 k) | 1.450.000 | 60% | 870.000 | 580.000 |
| **Investiție (art. 14)** | unități mobile, centru de coordonare, mediu securizat de date, dispozitive, active necorporale numite (secțiunea 4) | 4.600.000 | ~65% (de verificat) | ~3.000.000 | ~1.600.000 |
| **Inovare (art. 28)** | consultanță MDR și organism notificat, studiu de piață, protecție marcă/IP, raport CTT | 220.000 | 100% | 220.000 | 0 |
| **De minimis** | consultanță scriere/implementare, proiectare, publicitate (max. 15.000 lei fără TVA) | 300.000 | 100% | 300.000 | 0 |
| **Total** | | **~8.170.000** | | **~5.670.000** | **~2.500.000** |

- Grantul e între 5 și 7 mil. → criteriul 1.1 cere **> 4 locuri de muncă**; avem 6.
- **TVA** (~19% din eligibil ≈ 1,5 mil. EUR) se plătește și se recuperează; e neeligibilă dacă e deductibilă. Intră în planul de numerar, nu în buget.
- **Flux de numerar:** vârf estimat **3,5–4,5 mil. EUR** (cofinanțare + TVA + decalaj de rambursare 3–6 luni), redus cu prefinanțarea de până la 40% (garanție bancară) și cu etapizarea flotei. Planul de afaceri trebuie să conțină tabelul trimestrial.
- **Costuri în durabilitate** (neeligibile, din venituri): ~120–180 k EUR/an pentru flotă, centru, hosting, personal medical contractat.

## 9. Indicatorii (conservator, cu scenariu pesimist scris)

| Indicator | Țintă | Pesimist |
|---|---|---|
| RCO01/02, RCO125 | 1 întreprindere sprijinită | — |
| RCR01 locuri de muncă | **6 ENI**, menținute 3 ani | 6 (2 posturi pot fi menținute prin contract cu partenerul dacă regulile permit; de verificat) |
| Produs nou | platforma + PRIORITY (certificat sau în regim administrativ, plan B) + serviciul de prevenție mobilă | platforma + serviciul |
| Participanți în pilot | ≥300 | ≥150 |
| Rezultat măsurat | +10 pp la recomandările închise la 90 de zile față de linia de bază; examene la termen | efect nul publicat (tot rezultat) |
| Venituri din activitatea sprijinită, durabilitate (anii 1–3) | 250 / 400 / 550 k EUR | 150 / 250 / 350 k EUR |
| Spillover | profil FHIR românesc publicat; benchmark deschis RO/HU; protocolul studiului publicat | la fel |

**Regula:** promite în cerere ținta pe care o atingi și în scenariul pesimist; restul e în planul de afaceri ca ambiție.

## 10. Cum face bani după proiect

| Plătitor | Ce cumpără | Preț [ESTIMARE] | De ce plătește |
|---|---|---|---|
| **Angajatori** (prin cabinetele MM partenere) | ziua de prevenție cu unitatea mobilă + urmărirea recomandărilor + raport de rezultate | 25–60 lei/angajat/lună în pachet, sau per zi de prevenție | examenul e obligatoriu oricum (80–110 lei/angajat/an); absenteismul și boala cronică costă; raportul e dovada pentru conducere |
| **Cabinete MM și clinici independente** | licență platformă (motor de buclă, dosar, PRIORITY) | 150–400 EUR/lună per locație | își păstrează clienții în fața rețelelor (MedLife vinde deja portal pentru angajator) |
| **Asigurători privați** | pachete de prevenție măsurate pentru asigurații corporativi | per asigurat/an | daunele de sănătate cresc mai repede decât primele (repo, §3) |
| **Ungaria și CEE** | aceeași platformă bilingvă; parteneriat cu un furnizor de medicina muncii din Debrecen | licență | criteriul 4.3; piața maghiară are aceleași obligații de medicina muncii |
| **Alți beneficiari STEP / cercetare** | servicii de date și extragere (art. 28 la ei) | per proiect | competența WP2 e refolosibilă |

Rețelele mari (MedLife, Regina Maria, Medicover) nu sunt clienți la început: își fac IT-ul în casă; sunt parteneri sau cumpărători mai târziu.

## 11. Partenerii și ce semnezi

| Partener | Ce aduce | Document |
|---|---|---|
| 2–3 cabinete / firme de medicina muncii din Bihor (independente; proprietatea de verificat în ONRC) | angajatorii-client, fișele, echipa mobilă existentă, medicul coordonator | acord de parteneriat, DPA, protocol de pilot |
| Clinică independentă de boli cronice + laborator independent din Oradea | pacienți cu risc, rezultate de laborator, controale pierdute | contract de servicii, DPA |
| Universitate (Oradea: Medicină + CNCG-CTT; UMF Cluj; UTCN pentru federated learning) | cercetare contractată, comisia de etică, raportul CTT / CS I, publicarea | contract de cercetare, raport |
| 2–3 producători de dispozitive certificate cu API | tensiometre, ECG, cântare; acces la date | oferte, contract de livrare, DPA |
| Furnizor de amenajare a unităților mobile + furnizori de echipamente medicale | vehicule echipate, ECG, spirometru, audiometru, POC | 3 oferte per lot |
| Organism notificat | evaluarea clasa IIa | ofertă, acord de evaluare |
| Partener din Ungaria (furnizor MM sau clinică din Debrecen) | scalare, criteriul 4.3 | scrisoare de intenție |
| Consultant | scrierea dosarului și implementarea | contract, fără conflict de interese cu furnizorii |
| Angajatori (≥5 din Bihor, 300+ salariați fiecare) | cererea pentru zilele de prevenție | scrisori de intenție |

## 12. Riscurile principale și mecanismele (criteriile 5.9 și 5.10)

| Risc | Probabilitate / impact | Mecanism |
|---|---|---|
| Încadrarea STEP respinsă (5.1/5.2) | medie / fatal | raport CTT pe tehnologie, nu pe domeniu; întrebarea scrisă la ADR NV înainte de depunere |
| Art. 14 neacceptat în forma propusă | medie / mare | confirmare scrisă; alternativă: mai multe unități mobile, nu centru de date |
| Certificarea MDR depășește luna 30 | mare / mediu | QMS din luna 1; scoruri validate, nu model nou; plan B administrativ; art. 28 rezervat |
| Date insuficiente pentru WP5 | medie / mare | ≥2 cabinete MM + clinică + laborator; design în trepte care funcționează și cu N mic; învățare federată |
| Partenerul clinic se retrage | mică / fatal | doi parteneri MM de la început; contract cu penalități simetrice |
| Numerar (TVA, decalaj rambursare) | medie / mare | prefinanțare 40%, linie de credit, flota în două valuri |
| Oboseala de alerte / nimeni nu deține alerta | medie / mediu | regula anti-PRISMATIC; proprietar și termen pe fiecare element; metrici de închidere în tablou |
| Furnizori de software MM copiază stratul de bază | medie / mediu | valoarea se mută în măsurare, PRIORITY și unitățile mobile, nu în remindere |
| Legea 190/2018 (profilare pe date de sănătate) | medie / mare | consimțământ explicit în pilot; cercetare prin universitate; DPIA; avocat în luna 1 |
| Durabilitate: costul flotei și al centrului | medie / mare | ținte de venit conservatoare; contracte multianuale cu angajatori; scenariu pesimist scris |

## 13. Dosarul de depunere: checklist (păstrat din v1, completat)

- [ ] Solicitant: sediu în NV; an fiscal cu profit din exploatare > 0; ≥1 salariat mediu; fără excludere; drept de folosință asupra spațiului (centrul de coordonare).
- [ ] **Răspuns scris ADR NV** la: încadrarea tehnologiei; compoziția art. 14; eligibilitatea certificării MDR; fereastră ulterioară.
- [ ] **Răspuns GAL/OJFIR**: cumulul de minimis cu DR-36; compatibilitatea cu planul de afaceri monitorizat.
- [ ] Dovada cofinanțării și a liniei de credit pentru TVA (~2,5 mil. + numerar de lucru).
- [ ] Cerere MySMIS2021+; plan de afaceri cu flux de numerar trimestrial și scenariu pesimist; studiu de piață (angajatori, cabinete MM, asigurători, Ungaria).
- [ ] Macheta financiară (Anexa III.5 corectată).
- [ ] Raport CTT / CS I (tehnologie critică, TRL, inovație); raport expert contabil CECCAR.
- [ ] CV-uri și dovezi: director (5 ani dispozitive medicale), cercetător, manager (2 proiecte UE).
- [ ] Scrisori de intenție: ≥5 angajatori, 2–3 cabinete MM, 1 clinică, 1 laborator, 1 partener din Ungaria.
- [ ] 3 oferte per lot (unități mobile, echipamente, dispozitive, servere, licențe) + centralizator.
- [ ] Deviz general HG 907/2016 pentru amenajarea centrului, dacă e cazul.
- [ ] Declarația Unică (versiunea nouă); declarații de ajutor de stat / minimis (inclusiv DR-36).
- [ ] Autoevaluare **conservatoare**.

## 14. Următoarele 4 săptămâni

1. **E-mail la regio@nord-vest.ro** cu cele 4 întrebări, formulate pe tehnologie (secțiunea 2), nu pe domeniu. Fără răspuns pozitiv la primele două, planul nu se depune în forma asta.
2. **GAL/OJFIR:** cumul de minimis și compatibilitatea cu DR-36.
3. **Prototipul tău cu AI (2–3 săptămâni, 25–30 h):** dosar FHIR de test în APEX/ORDS; extragere din 3 PDF-uri reale RO/HU cu sursa citată; motor de termene și listă de lucru în n8n + APEX; tablou de rezultate; un tensiometru certificat conectat prin API. Acesta e demo-ul pentru toți cei de mai jos.
4. **Doi parteneri de medicina muncii** din Oradea (de verificat proprietatea în ONRC înainte de vizită) și o clinică independentă: cererea e „un pilot plătit de 3 angajatori ai voștri, cu unitate mobilă și urmărire”.
5. **Universitatea:** cine semnează raportul CTT și cine conduce WP5 (design de studiu, comisie de etică).
6. **Directorul (reglementare, 5+ ani) și managerul (2 proiecte UE):** CV-urile intră în dosar; fără ei, 2.1 pierde 6–8 puncte.
7. **Oferte:** o firmă de amenajare a unităților mobile, 2 furnizori de echipamente medicale, 2 producători de dispozitive cu API, un organism notificat, o colocare din regiune.
8. **Consultantul:** decizia 961 (02.11.2026, foarte strâns) sau fereastra următoare, luată împreună după răspunsul ADR NV.

Dacă ADR NV răspunde „da” la încadrare și la art. 14, iar doi parteneri MM semnează intenția de pilot, planul trece de la ipoteză la dosar. Dacă „nu” la încadrare, nucleul (WP1–WP3, WP5) rămâne valabil pentru alte linii de finanțare (POCIDIF, PNCDI IV, EIT Health), fără investiția fizică.
