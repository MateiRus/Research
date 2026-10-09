# Planul întărit v2: „Scadențar MM”, biroul de continuitate și de prevenție al cabinetului MM independent

**Persona:** fondator strategic / consultant. Răspunde obiecțiilor din `03_round_2_review.md`, în ordinea gravității. Tot ce era în v1 și nu e atins aici rămâne valabil (`02_round_1_plan.md`).

**Ideea centrală a rundei:** valoarea și activul de date trebuie mutate în locul pe care fondatorul îl poate deține legal și operațional: **munca echipei MM în jurul examenului obligatoriu** (programarea, deplasările, recomandările, ziua de prevenție). Nu în portal, nu în import și nu într-un set de date strâns în numele altora.

Cifrele vin din `bulletproof/model_36m.py` (calculul meu; intrările sunt estimări).

---

## Ce s-a schimbat, pe obiecții

### Obiecția 1 (65%) → Guvernanța datelor pe trei niveluri, iar etapa 3 are valoare și fără profilare

**Trei niveluri de date, fiecare cu baza lui legală:**

| Nivel | Ce conține | Cine e operator | Baza legală | Ce se poate face cu el |
|---|---|---|---|---|
| **A. Operațional** | angajați, scadențe, concluzii, recomandări, contacte | cabinetul | Art. 9(2)(h) al cabinetului; fondatorul e persoană împuternicită (REG §1) | doar serviciul pentru acel cabinet |
| **B. Indicatori agregați** | rata de închidere, timpul până la programare, umplerea zilelor de examen; celule de minimum 10 persoane | cabinetul, pentru tabloul lui; pentru comparații între cabinete, doar după opinie juridică | aceeași; comparațiile între cabinete doar dacă ieșirea e anonimă după testul din Recital 26 și cabinetul a optat în scris | tabloul cabinetului; raportul către angajator; comparații anonime, dacă avocatul confirmă |
| **C. Cercetare și modele** | date pseudonimizate pentru antrenare sau evaluare | depinde de rută | (a) studiu cu partener academic și comisie de etică (Art. 9(2)(j); baza românească trebuie verificată, REG §1 Gaps); (b) permis HDAB prin EHDS, de la ~2029 (REG §4); (c) model al cabinetului, comandat de el, cu DPIA (REG §1, ruta b, contestată) | etapele 3b și 4 |

Reguli:
- **Produsul nu se bazează pe consimțământul angajatului pentru dezvoltarea produsului.** În relația de muncă, consimțământul riscă să nu fie liber (BK, de verificat cu avocatul). Consimțământul se folosește doar pentru remindere SMS (Legea 506/2004).
- **Nicio dată de nivel A nu iese din tenantul cabinetului**, nici spre LLM (doar capete de coloană).

**Etapa 3 se rupe în două:**
- **3a. Predicție operațională fără profilare** (lunile 18–36): **„dispeceratul echipei mobile”**. Din scadențele tuturor angajaților, pe sediile angajatorilor, produsul propune zilele de deplasare și numărul de examene pe zi, ca echipa mobilă să facă mai multe examene pe drum. E prognoză de volum la nivel de angajator și sediu, nu scor pe persoană.
  - nu e dispozitiv medical (prognoza de capacitate e categoria 1; REG §8);
  - nu e profilare individuală, pentru că lucrează pe număr de scadențe pe sediu;
  - se sprijină pe un fapt din note: firmele medii și cabinete ca Carimed fac examene la sediul angajatorilor, cu programare (RSMM §5). Analogia „dispeceratului” vine din LAT §C.
- **3b. Predicția individuală „pe cine suni primul”** (după luna 30): doar dacă avocatul confirmă o bază legală (consimțământ explicit sau model al cabinetului cu DPIA) și doar dacă bate „reminder pentru toți” cu grup de control (FUR §3 ← JAMIA 2022: nedovedit). Dacă nu, 3b nu se face, iar planul nu se rupe.

**Efect:** drumul spre predictiv nu mai depinde de un activ care nu e al fondatorului. Primul strat „predictiv” (3a) e legal curat și are un cumpărător clar.

### Obiecția 2 (60%) → Valoarea iese din portal și din import; plan scris pentru ziua copierii
**Unde stă valoarea în v2 (în ordinea în care se construiește):**
1. **munca spre exterior:** remindere către HR, urmărirea până la programare (din v1);
2. **registrul recomandărilor**, cu termen pus de medic, dovadă și escaladare (din v1);
3. **planul de deplasări al echipei mobile** (3a, de mai sus): miezul operațional al firmelor medii, pe care programele MM, construite pentru cabinet, nu-l au documentat (RSMM §1 nu menționează așa ceva la niciun vendor; de verificat la discuțiile cu vendorii);
4. **modulul de prevenție la examen** (obiecția 5);
5. portalul și raportul de renegociere, ca vederi.

**Planul pentru ziua în care un vendor lansează portalul:**
- produsul citește în continuare exportul vendorului; cabinetul păstrează reminderele, registrul, planul de deplasări și modulul de prevenție;
- portalul nostru se oprește pentru acel cabinet, iar prețul scade pe treapta „Birou” (fără portal), ca să nu plătească de două ori;
- vendorului i se propune o integrare (listare în ofertă, comision de recomandare).

**Parteneriatul cu vendorii, cu pârghie:** nu se cere în luna 1, ci după **10 cabinete plătitoare**, cu date proprii (ore economisite, examene în plus pe deplasare, clienți păstrați). Propunerea e de complement, nu de concurent: comision de 20–30% pe revânzare (estimare) sau vânzarea modulului către vendor (o opțiune de ieșire).

**Spus cinstit:** în anii 1–2, apărarea e adâncimea fluxului (patru lucruri pe care cabinetul le folosește zilnic) și distribuția locală, nu tehnologia. Costul de a încerca rămâne mic (~4k € numerar).

### Obiecția 3 (55%) → Un al doilea motor, cu cifre și cu poartă
**Motorul 2: un ajutor operațional part-time, din luna 13.**
- **Cine:** o asistentă de medicina muncii sau un administrator, colaborator, ~20 h/lună, la ~20 €/h, deci ~400 €/lună (estimare).
- **Ce face:** onboarding-ul exporturilor, suportul de prim nivel, rapoartele lunare.
- **Efect:** fondatorul rămâne la 10–12 h/săpt, dar orele lui se mută pe vânzare și produs. Plafonul crește de la 25 la ~40 de cabinete.
- **Poarta:** ≥12 clienți plătitori **și** CAC măsurat ≤20 h/client **și** churn sub 2%/lună în ultimele 6 luni.

**Motorul 3: canalul.** Referințe de la primii clienți, demo-uri la distanță, eventual un vendor (după 10 cabinete). Ținta: CAC ≤15 h/client până în luna 12, măsurat. Permite ~1,5 clienți noi pe lună din luna 13.

**Motorul 4: modulul de prevenție** (obiecția 5). Se adaugă din luna 19 la o parte din clienți.

| Indicator (calculul meu) | v1 | **v2 fără modul** | **v2 cu modulul de prevenție** (ipoteză) |
|---|---:|---:|---:|
| MRR luna 12 | 758 € | 758 € | 758 € |
| MRR luna 18 | 996 € | 1.280 € | 1.280 € |
| MRR luna 24 | 1.218 € | 1.747 € | 2.171 € |
| MRR luna 36 | 1.605 € | 2.562 € | 3.185 € |
| Luna cu 1.000 € MRR | 19 | 15 | 15 |
| Luna cu 3.000 € MRR | niciodată | niciodată | **34** |
| Clienți în luna 36 | ~22 | ~35 | ~35 |
| Cel mai adânc punct al numerarului | −4.060 € | −4.060 € | −4.060 € |

Ipotezele modulului (de testat, nu fapte): 60 €/lună în medie pe clientul care îl ia; adopție de la 5% la 30% din clienți între lunile 19 și 24; plus un consilier medical MM la ~150 €/lună din luna 13 (detalii în runda 3).

**Efect:** plafonul are trei ieșiri, fiecare cu un cost scris și o poartă. 3.000 € MRR devine posibil în ~luna 34, fără ca fondatorul să treacă de 10–12 h/săpt, dar doar dacă porțile ies.

### Obiecția 4 (55%) → Argumentul de bani nu mai depinde de angajator
- **Un client păstrat:** un angajator de 300 de persoane × 80 lei = **24.000 lei/an ≈ 4.700 €/an** (calculul meu, la ~5,1 lei/€; prețul din RO §5, cursul din RSMM §4). Treapta standard costă 79 € × 12 = 948 €/an. **Un singur angajator mediu păstrat la renegociere plătește ~5 ani de abonament.**
- **Ore de asistentă economisite:** măsurate în pilot, înmulțite cu costul orei pe care îl știe cabinetul. Fondatorul nu inventează salarii.
- **Examene în plus pe deplasare** (din planul de deplasări): măsurate față de luna dinaintea pilotului.
- **Refacturarea devine un bonus, nu o premisă.** Kitul rămâne, dar nu intră în model.
- **Plata anuală în avans:** 12 luni la prețul a 10 (estimare), opțională. Reduce churn-ul și aduce numerar.
- **Treapta pentru angajatori „speriați de ITM”** rămâne doar ca sursă de clienți pentru cabinete (AF §C4), nu ca venit.

### Obiecția 5 (50%) → Etapa 2 se mută „la examen, nu după”
**Modulul de prevenție la examenul periodic** (succesorul lui O9 + O2 din LAT):
1. **În aceeași zi, în același loc:** când echipa MM face examenele periodice la sediul angajatorului, angajatorul poate cumpăra pentru angajații lui un set de teste suplimentare, din meniul definit de medicul MM (și de laboratorul partener, unde e nevoie). Lecția ACCESS: testul în aceeași vizită a dus finalizarea de la 22% la 100% (ȘTI KQ1).
2. **Pe ce se sprijină:** pentru grupele de risc, echipa MM face deja glicemie, EKG, spirometrie, audiometrie (RSMM §3 ← caietul de sarcini ONRC). Acestea sunt „declanșatori naturali de prevenție” (RSMM §3, Inferences).
3. **Constatările anormale:** **medicul** le marchează și pune clasa de termen. Produsul pune omul pe lista asistentei (un om care sună, nu un e-mail: FUR §2), generează scrisoarea către medicul de familie și verifică închiderea **la următorul examen periodic**, care oricum are loc.
4. **Ce vede angajatorul:** doar raportul agregat (celule de minimum 10): câți au participat, câte recomandări s-au închis. Nimic individual medical.
5. **Cine plătește:** angajatorul, prin cabinet, per participant sau per eveniment. Tratamentul fiscal (serviciu MM sau beneficiu în plafonul de 400 €; RSMM §4) se verifică cu un contabil.
6. **Partenerul de laborator:** Humanamed e singurul laborator independent găsit în Oradea, cu contract CAS (RSMM §5); celelalte sunt ale rețelelor, adică ale concurenței. Alternativa e să rămână doar testele pe care echipa MM le face deja.
7. **Reglementarea:** medicul decide și interpretează; software-ul programează și ține termenele puse de medic. Categoria 1. Notă scrisă de calificare MDR (~800 €, estimare) înainte de lansare.

**Efect:** bucla se închide acolo unde omul e deja prezent, iar urmarea depinde de un om al cabinetului, nu de medicul de familie.

### Obiecția 6 (45%) → Consolidarea, tratată ca risc cu reguli
- **Nicio regiune peste 40% din MRR** până în luna 24 (vânzare la distanță).
- **Contracte anuale**, cu predare a datelor în 3 luni dacă un cabinet e cumpărat. Cumpărătorul primește o ofertă (poate păstra fluxul).
- **Motivul fiecărei plecări** se notează; „cumpărat de o rețea” e o categorie separată în raportul lunar.
- **Segmentul se lărgește** spre firmele medii care nu sunt sub presiune imediată (50% în panelul simulat v1).
- Consolidarea ca **ieșire** (vânzarea către o rețea sau un vendor) e posibilă, dar nu se planifică pe ea: notele n-au găsit cumpărători români activi de module healthtech (CEE Q3, Inferences).

### Obiecția 7 (40%) → Validarea secvențiată în ~150 h

| Faza | Săptămânile | Ce se face | Ore |
|---|---|---|---:|
| A | 1–3 | 5 vendori (6 h); lista de 20 de cabinete (6 h); întrebări la avocat și cererea de ofertă de asigurare (3 h); 6 conversații în Oradea (18 h) | ~35 |
| **Poarta A (ziua 21)** | | **≥2 vendori cu portal pentru angajator → stop sau OEM; <3 din 6 cabinete confirmă durerea → oprire sau lărgire** | |
| B | 4–8 | 9 conversații (6 pe video, 3 fizic; ~25 h); ≤5 audituri pe exporturi (10 h); prototip APEX + n8n (25 h) | ~60 |
| **Poarta B (ziua 60)** | | **≥3 pre-vânzări plătite** | |
| C | 9–13 | pilot concierge la 2–3 cabinete plătitoare (~35 h); începutul MVP (20 h) | ~55 |
| **Poarta C (ziua 90)** | | **GO / PIVOT / NO-GO** (v1, neschimbat) | |

Ce s-a tăiat: drumurile fizice în afara Oradei (înlocuite cu video) și auditul G din primele 90 de zile.

### Obiecția 8 (30%) → Ofertă reală de asigurare și contract-tip
- **Oferta de asigurare** (RC profesională + cyber) se cere în săptămâna 3; dacă trece de ~1.200 €/an, se refac numerele.
- **Contractul-tip:**
  - plafon de răspundere = taxele din ultimele 12 luni;
  - cabinetul rămâne responsabil de programare și de informarea angajatorului;
  - termeni separați pentru utilizatorii din partea angajatorului;
  - jurnal de incidente.
- **Etapa 2:** medicul pune marcajele; produsul nu trimite conținut clinic către angajator sau angajat.

### Obiecția 9 (25%) → G înghețat, în scris
Nicio muncă pe G înainte de luna 12 și de 10 cabinete A plătitoare. După aceea, cel mult un audit G, doar la cererea unei clinici și doar dacă metricile A sunt verzi. Porțile G din AF §E3 rămân.

---

## Etapele, în versiunea v2

| Etapa | Lunile | Ce se construiește | Activul de date (nivel) | Poarta de intrare | Condiția de oprire |
|---|---|---|---|---|---|
| 0. Validare | 0–3 | prototip + pilot concierge | A | — | poarta A, B sau C picată |
| 1. Biroul de continuitate | 3–18 | remindere, registru, portal, raport | A, B (pentru cabinet) | GO în ziua 90 | <8 clienți în luna 12 sau churn >3%/lună |
| 2. Prevenție la examen | 18–36 | modulul de prevenție; arhiva de expunere (afișare fidelă) | A, B | ≥12 clienți, notă MDR, 1 partener de test | modulul la <15% din clienți după 12 luni |
| 3a. Dispecerat echipă mobilă | 18–36 | prognoza de volum pe sediu, planul de deplasări | B | ≥5 firme medii cu echipă mobilă | nu crește examenele pe deplasare |
| 3b. „Pe cine suni primul” | 30+ | model per cabinet, cu grup de control | C (rută b) | opinie juridică + DPIA | nu bate reminderul pentru toți |
| 4. Era EHDS | 2029+ | export conform, modele CE ale altora, permise HDAB | C (rutele a, b) | HDAB funcțional în România | HDAB absent; nicio rută legală |

## Verificarea constrângerilor

| Constrângere | Ține în v2? |
|---|---|
| Fondator solo, SRL Bihor, rețele Oradea/București | Da; ajutorul din luna 13 e colaborator part-time, nu co-fondator |
| Stack | Da |
| ~25k € | Da; vârful de numerar ~4,1k €; ajutorul și consilierul se plătesc din venit după luna 13 |
| 10–12 h/săpt | Da, inclusiv în motorul 2 |
| B2B recurent | Da |
| Fără date clinice la început | Da; în etapa 2, valorile rămân în programul MM, produsul ține doar marcajul și termenul puse de medic |
| Administrativ, în afara MDR | Da; 3a e prognoză de capacitate; 3b și 4 au porți juridice |
| Drum spre preventiv/predictiv | Da, cu active de date pe niveluri și baze legale |
