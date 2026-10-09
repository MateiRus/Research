# Planul întărit v1: „Scadențar MM”, biroul de continuitate al cabinetului independent de medicina muncii

**Persona:** fondator strategic / consultant. Răspunde obiecțiilor din `01_round_1_review.md` una câte una, în ordinea gravității. Unde obiecția e critică (≥70%), ținta e ca ea să dispară sau să fie transformată într-o poartă de decizie verificabilă. Unde e medie, ținta e să scadă vizibil.

**Ce nu s-a schimbat:** fondatorul solo, SRL în Bihor, stack-ul (APEX, PL/SQL, Python, n8n, LLM doar pentru maparea coloanelor), ~25k €, 10–12 h/săpt, B2B recurent, fără date clinice, produs administrativ. Scara de preț 39 / 79 / 149 €/lună. G rămâne a doua ușă, condiționată.

Cifrele noi vin din `bulletproof/model_36m.py` (calculul meu; toate intrările sunt estimări).

---

## Ce s-a schimbat, pe obiecții

### Obiecția 1 (85%) → „Dovadă înainte de cod”: validarea măsoară cerere reală, nu păreri
Validarea de 90 de zile nu mai e „conversații + machetă”. E un **pilot concierge plătit**, în care fondatorul face manual serviciul pe exporturile reale, iar produsul se construiește doar pe ce se dovedește.
- **Săptămânile 1–2:** verificarea vendorilor (obiecția 2) și lista nominală a cabinetelor (obiecția 3).
- **Săptămânile 2–6:** 15 conversații calificate. Fiecare se încheie cu oferta unui **audit de scadențe gratuit** pe exportul cabinetului (O24 din LAT, folosit ca unealtă de vânzare):
  - câte fișe sunt azi expirate și câte expiră în 30/60 de zile;
  - câte recomandări „apt condiționat” au termen și nu au dovadă de închidere;
  - câte ore pe săptămână pierde asistenta cu telefoanele (jurnal de o săptămână, nu estimare din memorie).
- **Săptămânile 5–10:** **pilot concierge** la 2–3 cabinete. Fondatorul rulează reminderele (e-mail către HR) cu un prototip APEX + n8n și trimite angajatorilor un PDF de status săptămânal. Se măsoară:
  - procentul de examene programate înainte de expirare, față de auditul inițial;
  - orele de asistentă economisite;
  - câți HR răspund și câți cer acces la portal.
- **Pre-vânzarea** = primele 3 luni plătite în avans la prețul de listă, rambursabile prin garanție. Ținta: 3 până în ziua 60.
- **Testul de mesaj pe oameni reali:** jumătate din conversații încep cu „asistenta nu mai sună angajatorii”, jumătate cu „portal ca la rețele”. Lecția simulată (v1 35% față de v2 15%) devine o ipoteză verificată, nu o certitudine.
- **Verdictul se recalculează cu conversia reală.** Dacă din conversațiile calificate ies mai puțin de 10% pre-vânzări, planul se oprește.

**Efect:** obiecția nu dispare (nu poate dispărea fără clienți), dar devine o poartă cu cifre în ziua 60 și ziua 90, iar costul de a afla e de ~1.000 € și ~120 h.

### Obiecția 2 (80%) → Vendorii se verifică primii, iar produsul nu mai e „un portal”
- **Înainte de orice linie de cod**, discuție directă (sau demo cerut ca potențial partener) cu Setrio (BizMedica MM), DMV Consult (MedExam), Qmedical, Charisma și MedSoft. Întrebări:
  - au portal sau acces pentru angajator?
  - trimit remindere către HR-ul clientului?
  - țin recomandările „apt condiționat” cu termen și dovadă de închidere?
  - ce export programat permit (format, frecvență)?
  - ar accepta un parteneriat (integrare, revânzare, OEM)?
- **Arborele de decizie:**
  - **0–1 programe au portal pentru angajator** → se construiește A;
  - **≥2 îl au** → nu se construiește portalul. Se oferă un OEM vendorului care nu-l are, sau se păstrează doar registrul recomandărilor (mai jos), sau se trece la G dacă auditul G iese puternic;
  - **un vendor vrea parteneriat** → integrare prin el și vânzare prin baza lui de clienți (pârghia de +50% volum din AF §D3).
- **Repoziționarea.** Produsul nu e „portalul”, ci **biroul de continuitate** al cabinetului („CAMO pentru oameni”, LAT §C). Face trei lucruri pentru care programele MM nu sunt construite, pentru că ele sunt făcute să emită fișa în cabinet:
  1. **munca spre exterior:** remindere și urmărirea angajatorilor până la programare;
  2. **registrul recomandărilor deschise:** fiecare recomandare cu termen pus de medic, dovadă încărcată, escaladare;
  3. **raportul de renegociere** pe angajator.
  Portalul e doar o vedere peste acestea.
- **Ce rămâne al fondatorului dacă BizMedica adaugă un portal, spus cinstit:** în anul 1, niciun avantaj tehnic. Avantajele sunt viteza, serviciul local, faptul că produsul merge peste oricare dintre programe (adaptoare pentru mai mulți vendori) și **istoricul închiderii buclelor**, care devine cost de schimbare după 12 luni.

**Efect:** golul se verifică în 2 săptămâni, cu ~0 € cost. Dacă nu există, planul se oprește înainte de a cheltui 120–160 h pe MVP.

### Obiecția 3 (80%) → Piața se numără înainte, iar A e declarat „ușă”, nu „companie”
- **Lista nominală:** ≥20 de cabinete independente accesibile în Nord-Vest, cu proprietarul verificat (ONRC/Termene) și programul MM folosit. Sub 10 → NO-GO (rămâne din AF §E6).
- **Geografia vânzării:** primele 3–5 cabinete fizic, în Oradea. Apoi **vânzare la distanță** (demo video, onboarding pe exportul trimis securizat) către firmele medii și regionale din toată țara, unde tichetul e mai mare.
- **Mixul se mută spre firmele medii** (2–5 medici, echipă mobilă, 3.000–10.000 de angajați), segmentul cu cea mai mare rată simulată (50% în v1) și cu pragul „scump” la 95–120 €. La un mix de 30% mici / 60% medii / 10% regionale, prețul mediu devine **~74 €** (calculul meu, față de 65 €).
- **Ținta realistă:** 25 de cabinete = ~5% din cele 508 listate (RSMM §3).
- **Ce piață justifică o companie (spus cinstit):**
  - stratul de scadențe singur valorează cel mult ~0,4 mil. €/an la prețurile de azi, chiar cu toate cabinetele (calculul din review);
  - piața mare e **banul angajatorului pentru prevenție**: cheltuiala teoretică pe examene periodice e ~90–125 mil. €/an (RSMM §3, Inferences, calculul cercetătorului), iar abonamentele corporate sunt declarate la peste 250 mil. € (RSMM §4, sursă slabă: advertorial);
  - A e ușa spre acest buget, prin **același cumpărător** (cabinetul MM, care are deja contractul cu angajatorul). Drumul e la obiecția 4.

**Efect:** obiecția scade de la „piață nenumărată” la „piață numărată, mică, cu o ipoteză de extindere testabilă”.

### Obiecția 4 (70%) → Drumul spre predictiv, cu porți (prima versiune)

| Etapa | Ce se construiește | Activul de date și baza legală | Ce se validează | Partener / licență | Poarta spre etapa următoare | Condiția de oprire |
|---|---|---|---|---|---|---|
| **1. Administrativ** (lunile 0–18) | motorul de scadențe; remindere către HR; registrul recomandărilor; portal de status; raport lunar | istoricul buclelor (cine, ce termen, după câte contacte, închis sau nu), ca persoană împuternicită (Art. 28; baza cabinetului e Art. 9(2)(h)) | cabinetele plătesc; asistenta economisește timp; examene la termen mai multe decât la audit | avocat (DPA, opinie „ce vede angajatorul”) | ≥10 cabinete plătitoare, churn anual <25%, ≥2.000 de recomandări urmărite | <3 pre-vânzări în ziua 60; ≥2 vendori au deja portalul |
| **2. Prevenție la același cumpărător** (lunile 12–36) | închiderea recomandărilor medicului MM, inclusiv constatările anormale **marcate de medic**: scrisoare către medicul de familie, remindere, dovadă; arhiva de expunere (afișare fidelă); ziua de prevenție | același rol de împuternicit; nicio valoare calculată de software | rata de închidere crește față de audit, măsurată cu un grup de comparație | notă scrisă de calificare MDR; laborator partener pentru ziua de prevenție | ≥5 cabinete cu modulul plătit; creștere a ratei de închidere de ≥10 puncte procentuale | modulul nu se vinde la ≥30% din clienți în 12 luni |
| **3. Predicție operațională** (lunile 24–48) | ordonarea buclelor după probabilitatea de a nu se închide fără un apel | **de decis cu avocatul** (obiecția rămâne deschisă: profilare, Legea 190 art. 3) | bate „reminder pentru toți”, cu grup de control | DPIA; partener academic pentru evaluare | efect măsurat ≥ pragul stabilit | nu bate reminderul pentru toți (FUR §3 ← JAMIA 2022: nedovedit) |
| **4. Era EHDS** (2029+) | stratul de buclă găzduiește modele CE ale altor vendori; export conform EHDS | permise de la organismul de acces la date (HDAB), dacă România îl are | — | vendor CE (poartă MDR); HDAB | — | România nu are HDAB funcțional |

Reguli de la prima zi:
- **Nicio afirmație „predictivă” în marketing** (scopul declarat decide clasa MDR; REG §2, Art. 2(12)).
- Toate termenele sunt puse de medic sau de lege, niciunul de software.

**Efect:** obiecția scade (drumul are porți și opriri), dar rămâne deschisă la etapa 3: baza legală pentru date. Se reia în runda 2.

### Obiecția 5 (70%) → Valoare măsurată pentru cabinet, nu „paritate”
- **Oferta se vinde pe două lucruri măsurabile în pilot:** orele de asistentă economisite și angajatorii păstrați la renegociere (raportul lunar).
- **„Paritatea cu rețelele” nu mai e mesaj.** Panelul arată că a convins doar cabinetele care pierduseră deja clienți.
- **Kit de refacturare, opțional:** model de scrisoare și o linie „serviciu digital de conformitate” pe care cabinetul o poate adăuga în oferta către angajatori. Suma (de ex. +2–4 lei/angajat/an) e o **ipoteză de testat** cu ≥3 angajatori în validare, nu o promisiune.
- **Segmentele de început:** firme medii cu echipă mobilă și cabinetele „sub presiunea rețelelor” (au cumpărat 3/3 în ambele paneluri simulate).
- **Răspunsul real la pachetul rețelelor vine în etapa 2:** independentul nu poate vinde un abonament de 400 €, dar poate vinde **un modul de prevenție atașat de examenul obligatoriu** pe care îl face deja.

**Efect:** obiecția scade. Plătitorul rămâne cabinetul, dar cu un argument de bani, nu de imagine.

### Obiecția 6 (65%) → Modelul refăcut cu churn, retururi și timp
Schimbări față de CFO-ul original:
- **churn** 1,5%/lună după garanție (~17%/an; estimare);
- **retururi la garanție:** 10% din clienții noi, pentru că garanția se dă doar cabinetelor calificate (export funcțional, cel puțin un angajator care vrea acces);
- **rampa:** 3 piloți plătiți din luna 3 (chiar condiția GO), apoi +1 client/lună până în luna 12, apoi **0,8 clienți/lună** (limita de timp de la obiecția 6b);
- **preț mediu 74 €** (mixul spre firme medii);
- **pornire 3.580 €** (+600 € pentru opinia juridică);
- **CAC măsurat în ore** pe fiecare client câștigat, raportat lunar.

| Indicator (calculul meu) | R0 original | R0 cu churn și retururi | **Plan v1** |
|---|---:|---:|---:|
| Profit operațional anul 1 | +534 € | −198 € | **+1.747 €** |
| MRR luna 12 / 18 / 24 / 36 | 650 / 1.040 / 1.430 / 1.625 € | 522 / 777 / 1.010 / 1.417 € | **758 / 996 / 1.218 / 1.605 €** |
| Luna cu 1.000 € MRR | 18 | 24 | **19** |
| Luna cu 3.000 € MRR | niciodată | niciodată | **niciodată** (la 10–12 h/săpt) |
| Cel mai adânc punct al numerarului | −3.825 € | −3.853 € | **−4.060 €** |

**Ce spune tabelul:** v1 recuperează realismul (churn, retururi, timp) prin trei pârghii: prețul mediu, plata la începutul pilotului și garanția dată doar cabinetelor calificate. Plafonul rămâne ~1,6k € la 10–12 h/săpt. Asta e o constatare, nu o problemă ascunsă: **3.000 € MRR cere fie mai mult timp, fie un canal, fie un al doilea modul** (runda 2).

### Obiecția 7 (60%) → Modelul de date minim și opinia juridică înainte de portal
- **Ce se stochează, pe angajat:** nume, angajator, post/grupa de risc, data ultimului examen, tipul examenului, concluzia (apt / apt condiționat / inapt temporar / inapt permanent, adică ce scrie pe exemplarul angajatorului; RSMM §3 ← HG 355/2007 anexa 5), următoarea scadență. Telefonul sau e-mailul angajatului **doar** dacă și-a dat consimțământul pentru remindere.
- **Ce nu se stochează:** CNP (se folosește numărul de dosar al cabinetului), diagnostice, textul recomandărilor.
- **Ce vede angajatorul în v1:** statusul și concluzia pe angajat (ce are deja pe hârtie). **Registrul recomandărilor e vizibil doar cabinetului** până când opinia juridică spune ce poate vedea angajatorul.
- **Opinia juridică** (~600 €, estimare), înainte de portal: ce vede angajatorul; dacă reminderele către angajați sunt comunicare comercială (Legea 506/2004) sau administrativă; DPA; lista de sub-procesatori.
- **LLM-ul vede doar capetele de coloană** și rânduri sintetice, niciodată date personale.
- **Securitate pe care o înțelege un cabinet mic:** găzduire în UE, criptare, MFA, jurnal de acces, revizie externă de securitate (800 €), asigurare RC + cyber, export complet oricând, export lunar automat trimis cabinetului (dacă firma dispare, cabinetul are datele).
- **Primul pilot devine referința** pentru următoarele cabinete (condiția „să-l văd la un cabinet pe care îl cunosc” din panel).

### Obiecția 8 (55%) → Reguli de produs pentru datele învechite
- **Cel mult două adaptoare în v1**, pentru programele folosite de primii piloți.
- **Bannerul de prospețime:** „Actualizat la [data]” pe fiecare pagină a portalului.
- **Statusuri cu grație:** „examen programat” → „în curs de confirmare” (7 zile după data programată) → abia apoi „depășit”. Nimeni nu apare „depășit” a doua zi după examen.
- **Asistenta marchează „examinat azi” dintr-un clic.**
- **Import săptămânal automat** (n8n: e-mail sau folder) și un **raport de calitate** după fiecare import: rânduri, erori, dubluri.
- **Metrici:** export obținut în <30 min; curățare ≤10 h la primul pilot și ≤2 h/lună după aceea.

### Obiecția 9 (50%) → Un buget de ore și reguli de operare
- **Bugetul lunar (~52 h):**
  - lunile 1–3: 25 h descoperire și vânzare, 20 h construcție, 7 h juridic și administrativ;
  - lunile 4–12: 20 h vânzare, 15 h construcție, 10 h suport și onboarding, 7 h administrativ.
- **Plafon:** 25 de cabinete până la primul ajutor plătit.
- **Suport:** răspuns în următoarea zi lucrătoare; importurile ratate sunt detectate automat și semnalate; fără promisiune 24/7.
- **Continuitate:** proceduri scrise, parole într-un seif, export lunar la fiecare cabinet, un dezvoltator de rezervă din rețeaua fondatorului plătit la incident (estimare).
- **Pragul de ajutor:** suport + onboarding >15 h/lună sau >12 clienți → un ajutor part-time (detaliat în runda 2).

### Obiecția 10 (30%) → Scopul declarat și răspunderea, scrise de la început
- **Scopul declarat:** „software administrativ pentru planificarea examenelor de medicina muncii și urmărirea termenelor stabilite de medic; nu interpretează date medicale”.
- **Cuvinte interzise în marketing:** „prezice”, „risc”, „diagnostic”, „detectează”, „previne boala” (REG §2, §8).
- **Contracte:** plafon de răspundere; cabinetul răspunde de corectitudinea datelor introduse; asigurare RC + cyber.
- **SMS:** implicit e-mail către HR; SMS către angajați doar cu consimțământ înregistrat.
- **PLD:** jurnal de versiuni, note de lansare, disciplină de patch-uri (REG §7).
- **Orice funcție din etapele 2–4** cere o notă scrisă de calificare înainte de lansare.

---

## Planul v1, pe o pagină

- **Ce:** biroul de continuitate al cabinetului independent de medicina muncii: remindere către angajatori, registrul recomandărilor, raport de renegociere, portal de status cu marca cabinetului.
- **Cui:** firme MM medii cu echipă mobilă și cabinete sub presiunea rețelelor; Oradea fizic, apoi vânzare la distanță.
- **Preț:** 39 / 79 / 149 €/lună, SMS la cost scris în contract, garanție de 90 de zile doar pentru cabinetele calificate; kit de refacturare opțional.
- **Validarea (90 de zile):** verificarea vendorilor → lista de ≥20 → 15 conversații cu audit gratuit → pilot concierge plătit la 2–3 cabinete → MVP doar după 3 pre-vânzări.
- **GO (ziua 90):** ≥3 pre-vânzări plătite **și** 0–1 vendori cu portal **și** ≥2 exporturi funcționale **și** în pilot: ore de asistentă economisite sau examene la termen în creștere față de audit.
- **NO-GO:** <10% conversie din conversațiile calificate; ≥2 vendori cu portal; <10 cabinete independente accesibile.
- **Numerele (estimări):** 1.000 € MRR în ~luna 19; ~1,6k € MRR în luna 36 la 10–12 h/săpt; cel mai adânc punct de numerar ~−4,1k €.
- **Drumul:** 4 etape cu porți și condiții de oprire (tabelul de la obiecția 4).
- **G:** neschimbat, a doua ușă după referințe A și audituri.

## Verificarea constrângerilor

| Constrângere | Ține în v1? |
|---|---|
| Fondator solo, SRL în Bihor, rețele Oradea/București | Da |
| Stack: APEX, PL/SQL, Python, n8n, LLM | Da (LLM doar pe capete de coloană) |
| ~25k € | Da (vârf de numerar ~4,1k €) |
| 10–12 h/săpt | Da (buget de 52 h/lună, plafon de 25 de clienți) |
| B2B recurent | Da |
| Fără date clinice la început | Da (fără diagnostice, fără CNP) |
| Administrativ, în afara MDR | Da (scop declarat, cuvinte interzise) |
| Drum spre preventiv/predictiv | Da, cu porți (etapa 3 încă deschisă juridic) |
