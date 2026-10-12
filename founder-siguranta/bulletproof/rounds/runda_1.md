# Runda 1: atacurile investitorului, răspunsurile și verdictul (planul v0 → v1)

**Investitorul (persona):** business angel care a investit în telematică de flotă și în servicii de pază din Europa Centrală și de Est. Știe cum arată un dispecerat la 3 dimineața și cine e chemat în judecată când o alarmă se pierde. Pentru fiecare obiecție dă o **probabilitate de respingere dacă obiecția rămâne nerezolvată**. Nu e o statistică: arată cât cântărește obiecția în decizia lui.

**Regula de lucru:** fără cercetare web nouă. Faptele vin din raport și din note (prescurtările din `00_original_plan.md`). Ce e judecata evaluatorului e marcat **[estimare]**. Ce e din memoria evaluatorului, necitit în surse, e marcat **[de verificat]**.

---

## A. Atacurile

### Atacul 1. Vinzi o promisiune de viață, cu răspunderea unei firme de o persoană
- **Probabilitatea de respingere: 90%**
- **Logica:** Dacă un om moare și alarma lui nu a ajuns, prima întrebare la cercetare va fi „unde s-a pierdut”. Planul pune ILLUSTRUS în mijlocul lanțului: serverul, regulile, ecranul și contractul cu dispeceratul sunt ale tale. Clauza „răspunderea mea se limitează la abonamentul pe 12 luni” e scrisă ca estimare, nevalidată de avocat. Din memoria evaluatorului, Codul civil (art. 1355 alin. 2) nu permite limitarea răspunderii pentru vătămarea integrității corporale sau a sănătății decât în condițiile legii [de verificat]. Dacă e așa, clauza ta nu te apără exact în cazul care contează.
- **Dovezi:**
  - Directiva 2024/2853 tratează software-ul ca produs și se transpune până la 9 decembrie 2026; România nu avea proiect de lege [fapt, RAP §5; N02 întrebarea 10].
  - Contractul, asigurarea RC (răspundere civilă) și opinia pe Legea 333/2003 sunt toate „estimare, de validat cu avocat” [RAP §5, „Contractul și asigurarea”].
  - Nu s-a găsit niciun preț de asigurare RC profesională pentru dispecerat de alarme în România [fapt: lipsă, N05 §6 Gaps; N02 linia „Nu am găsit oferte”].
  - Procesele penale durează 4–8 ani, cu condamnări cu suspendare pentru administrator [fapt, RAP §1 și §2, cazurile Aleșd și Strugari].
- **Ce m-ar face să schimb votul:** un aviz scris de avocat pe structura de răspundere și o ofertă scrisă de asigurare care numește activitatea, înainte de primul lucrător echipat.

### Atacul 2. Firma de pază e punctul unic de eșec, iar stimulentul ei e aproape zero
- **Probabilitatea de respingere: 85%**
- **Logica:** Planul presupune că o firmă de pază va pune operatori să stea în ecranul tău APEX „pe toată durata turelor clientului” pentru 30 × 2,50 = 75 EUR pe lună. Asta e sub costul unei singure ore de operator pe zi [estimare]. Operatorii lor sunt instruiți pentru efracție, nu pentru un om căzut într-o stație de pompare. Al doilea ecran, într-o aplicație străină, e ușor de ignorat la ora 3. Dacă firma de pază are o pană de curent, schimbă personalul sau pierde contractul de pază al clientului, lanțul tău se rupe fără ca tu să știi.
- **Dovezi:**
  - Tariful de 2,50 EUR e ancorat pe un supliment britanic, fără nicio ofertă românească [fapt pentru reper, estimare pentru valoare, N05 §4 și §4 Gaps].
  - „Poate exista un minim lunar” [RAP §6, „Ce cumperi”].
  - Firmele de pază „pot copia serviciul”, recomandarea e o clauză de neconcurență [estimare, N05 §5].
  - Încadrarea dispeceratului în Legea 333/2003 e necunoscută [de verificat, N02 linia 266].
- **Ce m-ar face să schimb votul:** cine răspunde la alarmă când firma de pază nu răspunde, scris în procedura clientului, și cel puțin o ofertă reală de dispecerat cu timp de preluare garantat.

### Atacul 3. 10–12 ore pe săptămână nu acoperă un serviciu care nu are voie să se oprească
- **Probabilitatea de respingere: 85%**
- **Logica:** Lanțul are cinci piese care pot cădea (dispozitiv, rețea, Traccar, n8n, APEX), toate administrate de un student cu sesiune de examene. Cine repară serverul sâmbătă la 2 noaptea? Construcția singură ia 7–16 săptămâni la ritmul tău, iar în aceeași perioadă trebuie vândut pilotul, negociat cu firma de pază, scris contractul și pregătite cele circa 15 documente A–F. Bus factor 1 (afacerea depinde de un singur om).
- **Dovezi:**
  - 80–160 de ore de construcție, 7–16 săptămâni [estimare, RAP §6].
  - Pachetul de documente A–F, circa 15 documente [RAP §5; N02 secțiunea finală].
  - „Alarma cere răspuns non-stop: dispeceratul externalizat e obligatoriu” [estimare, RAP §1].
- **Calculul evaluatorului [estimare]:** 10–12 h/săpt × 4,3 ≈ 43–52 h pe lună. Construcția (120 h la mijloc) plus documentele (circa 30 h) plus vânzarea (circa 30 h) ≈ 180 h, adică 4 luni de capacitate completă înainte de ziua 1, fără nicio rezervă pentru incidente.
- **Ce m-ar face să schimb votul:** o arhitectură în care o pană a serverului tău nu pierde alarma, plus un om de rezervă plătit.

### Atacul 4. Utilitatea de stat nu poate cumpăra așa cum ai scris pilotul
- **Probabilitatea de respingere: 80%**
- **Logica:** „Clientul cumpără 30 de dispozitive, primește 90 de zile gratis, iar contractul prevede trecerea la 12 EUR dacă pilotul reușește” e un model de vânzare privată. O companie de apă a municipiului cumpără prin SEAP/SICAP (sistemul electronic de achiziții publice). Promisiunea unui contract viitor către același furnizor, fără procedură, e greu de apărat [estimare]. Din memorie, operatorii de apă pot intra și sub regulile achizițiilor sectoriale (Legea 99/2016), nu doar sub Legea 98/2016 [de verificat]. Pragul de achiziție directă de circa 270.000 lei e „din memorie” chiar în raport. Și nimeni de la Compania de Apă nu a spus încă nimic: toată cererea e dedusă.
- **Dovezi:**
  - Pragul de achiziție directă: „din memorie, de verificat” [RAP §1; N05 §2].
  - Utilitățile publice decid prin director general și șef SSM, prin SEAP [estimare, N05 §2].
  - Statutul RER Vest (privat sau al municipiului) e neclar [de verificat, N05 §1 Gaps].
  - Achizițiile publice de monitorizare existente sunt pentru pază, nu pentru persoane [fapt, N05 §7].
  - „Nu am găsit angajatori români care declară că folosesc dispozitive lone worker; nici licitații SEAP” [fapt: lipsă, N05 §7 Gaps].
- **Ce m-ar face să schimb votul:** o discuție cu șeful SSM și cu achizițiile de la cel puțin două utilități, și un pilot care se poate cumpăra legal, cu bani, din bugetul lor.

### Atacul 5. Cazul de folosire ales e locul cu cel mai prost semnal și cu cel mai mare risc de gaze
- **Probabilitatea de respingere: 75%**
- **Logica:** Pilotul vizează „cămine și stații de pompare”. Acolo semnalul mobil e cel mai slab (sub pământ, beton, metal), iar raportul nu are nicio măsurătoare din cămine. Germania spune explicit că sistemele prin rețele publice „depind de disponibilitatea rețelei” și cer echipament suplimentar pentru lucrul singur periculos. Iar moartea tipică în cămin e prin gaze: un tracker care alarmează după ce omul a leșinat poate trimite colegul în aceeași capcană.
- **Dovezi:**
  - DGUV (asigurătorul public german pentru accidente de muncă), sistemele PNA-11 prin rețele mobile publice [fapt, N02, întrebarea despre lucrul izolat].
  - ANCOM măsoară de pe drumuri, nu din pădure sau cămine [fapt, RAP §4].
  - Săveni, muncitor mort la o stație de pompare [fapt, RAP §1].
  - Gazele: „doar cu detectoare certificate existente” [RAP §1]; detectoarele conectate costă 1.300–1.900 EUR [fapt, N04 §4].
  - Pentru spații închise nu există HG dedicată; detectorul de gaz plus om la pământ e „practic standardul de piață” [estimare, N02 întrebarea 5].
- **Ce m-ar face să schimb votul:** o zi de măsurare în cămine cu dispozitivul real înainte de orice contract, și o definiție îngustă a lucrătorului țintă care nu depinde de gaze.

### Atacul 6. Hardware-ul nu e verificat, iar unul dintre cele două modele e scos din producție
- **Probabilitatea de respingere: 70%**
- **Logica:** GH5200 apare „End of life” la Teltonika și „indisponibil” la distribuitor. TMT250 „pare să fie doar 2G”, iar protocolul Codec 8 pentru el nu e confirmat. Gradul IP (rezistența la apă și praf) e necunoscut pentru ambele. Tot produsul tău stă pe un producător fără distribuitor în România, care își retrage modelele. Dacă operatorii închid 2G, flota ta de pilot devine deșeu [de verificat: datele de închidere 2G în România nu sunt în note].
- **Dovezi:**
  - GH5200 „End of life”, indisponibil la Ascend, stoc epuizat la Novatel [fapt, N04 §1; RAP §4].
  - TMT250: 2G posibil, Codec 8 neconfirmat, autonomia necunoscută [de verificat, N04 §1].
  - Familiile TAT100/TAT140 „End of life” [fapt, N04 §1].
  - Niciun distribuitor Teltonika în România găsit [fapt: lipsă, RAP §3].
  - Calitatea algoritmului om la pământ nu e documentată public de niciun producător [estimare, N04 §1].
- **Ce m-ar face să schimb votul:** 3 mostre testate pe birou și în teren, confirmarea scrisă a rețelei și a protocolului, și un al doilea tip de dispozitiv integrat.

### Atacul 7. Muncitorii și sindicatul pot opri totul în prima lună
- **Probabilitatea de respingere: 70%**
- **Logica:** 59% nu ar folosi dispozitive de urmărire. La o utilitate cu sindicat, consultarea e obligatorie înainte de pornire. Dacă sindicatul vede un GPS pe om, pilotul nu pornește sau pornește cu dispozitivele lăsate în vestiar. Ținta de 85% purtare nu are niciun reper real de purtare, doar un reper de înscriere voluntară (70–80%).
- **Dovezi:**
  - 46% / 59% refuz [fapt, studiu văzut prin rezumat, RAP §1; N05 §6].
  - Legea 190/2018 art. 5, condiții cumulative, inclusiv consultarea sindicatului [fapt, RAP §5].
  - Amenzi ANSPDCP (autoritatea pentru protecția datelor) de 2.000–4.000 EUR pentru GPS în afara programului [fapt, N05 §6].
  - Nu există rate de purtare din implementări reale [fapt: lipsă, N05 §6 Gaps].
  - Great River Energy: 70–80% înscriși într-un program voluntar [fapt, RAP §6].
- **Ce m-ar face să schimb votul:** un produs care nu urmărește continuu, un acord scris cu sindicatul înainte de pilot și o măsură automată a purtării.

### Atacul 8. Alarmele false vor obosi dispecerul exact înainte de alarma reală
- **Probabilitatea de respingere: 65%**
- **Logica:** Nimeni nu publică rate de alarme false din teren. Un om care îngenunchează într-un cămin 5 minute arată ca un om căzut. Ținta „sub 2 la 100 de ture-om” e inventată. Dacă primele două săptămâni aduc 20 de alarme false, dispecerul de pază va învăța să le închidă fără să sune. Cine plătește deplasările inutile?
- **Dovezi:**
  - Temporizatorul de imobilitate e „un instrument brut” [fapt, sursă de furnizor, RAP §1].
  - Singura rată măsurată (1,1%) e academică, offline [fapt, N05 §6].
  - Caietele de sarcini românești pentru pază includ un număr de alarme false în tarif [fapt, N05 §2].
  - Lucrătorii din Alabama „se tem că alarmele false le vor perturba munca” [fapt, N05 §6].
- **Ce m-ar face să schimb votul:** o fază de măsurare a alarmelor false fără dispecerizare, înainte de pornirea reală.

### Atacul 9. Economia nu ține la scara Bihorului, iar costurile fixe presupun oameni pe care nu îi ai
- **Probabilitatea de respingere: 60%**
- **Logica:** Pragul de rentabilitate e 160–700 de lucrători. Piața realistă în Bihor e 1.100–3.400 de abonamente în 3–5 ani, ±50%. Prețul pentru primii clienți (12 EUR) dă aproape zero la 200 de lucrători. Costurile fixe din calcul includ 0,5–2,5 norme de personal care nu există. Dispeceratul de 2,50 EUR nu are ofertă.
- **Dovezi:** RAP §2 („Muncitori la risc”), RAP §7; N05 §4 Gaps (fără tarife de dispecerat și SIM în România).
- **Ce m-ar face să schimb votul:** un model în care costul cel mai mare (dispeceratul) nu crește cu fiecare lucrător, și un prag de rentabilitate pe care un singur om îl poate atinge.

### Atacul 10. Nu poți dovedi valoarea în pilot, deci reînnoirea e o loterie
- **Probabilitatea de respingere: 55%**
- **Logica:** Planul spune cinstit că în 60 de zile probabil nu va exista nicio alarmă reală gravă. Atunci de ce ar plăti clientul în luna 4? ITM (inspectoratul teritorial de muncă) nu cere dispozitivul. CAM nu scade. Amenzile sunt mici. Singurul argument rămas e frica de penal, care e abstractă până la primul mort.
- **Dovezi:** RAP §1 („Ce nu va funcționa”), RAP §6 („Spus cinstit”), N06 §1 (CNPP, Casa Națională de Pensii Publice, nu finanțează prevenirea; CAM fără bonus-malus).
- **Ce m-ar face să schimb votul:** un livrabil pe care șeful SSM îl poate pune pe masă la control ITM sau la cercetarea unui accident, independent de existența unei alarme reale.

### Atacul 11. Regula de 30 de zile se bate cap în cap cu jurnalul de probe
- **Probabilitatea de respingere: 40%**
- **Logica:** Planul vinde jurnalul de alarme „ca probă la ITM”, dar PL/SQL șterge pozițiile după 30 de zile. Cercetarea penală durează ani. Dacă jurnalul dispare, proba dispare; dacă rămâne cu tot cu pozițiile, încalci Legea 190/2018.
- **Dovezi:** RAP §5 (Legea 190/2018, max. 30 de zile „cu excepții justificate” în N05 §2); RAP §6 (ștergere la 30 de zile, jurnal ca probă); RAP §2 (procese de 4–8 ani).
- **Ce m-ar face să schimb votul:** două regimuri de păstrare scrise în DPIA (evaluarea de impact asupra protecției datelor).

**Verdictul investitorului în runda 1: NU.** Ideea are o obligație legală reală în spate și un loc gol pe piață. Dar planul pune un om cu 10 ore pe săptămână la mijlocul unui lanț de viață și moarte, cu un partener nemotivat, la un client care nu poate cumpăra așa, într-un loc fără semnal, pe un dispozitiv neverificat.

---

## B. Răspunsurile (planul v1)

### La atacul 1 (90%) → ILLUSTRUS iese din rolul de „cel care răspunde la alarmă”
- **Schimbarea:** produsul devine o **platformă de alarmare pe care o operează dispeceratul non-stop al clientului**. Majoritatea utilităților au deja un dispecerat de avarii pe toate turele [estimare, de verificat la fiecare client]. ILLUSTRUS livrează platforma, regulile, testele și pachetul de conformitate; răspunsul la alarmă rămâne la angajator, unde stă deja răspunderea SSM („direct și exclusiv angajatorului”, N06 §1).
- **Modelul de referință:** Vatix (UK) oferă exact varianta de „auto-monitorizare”, în care alarma merge la respondenții clientului [fapt, N05 §6]. INRS (Franța) cere ca alarma să fie folosită doar într-o procedură de salvare validată de angajator [fapt, RAP §5].
- **Contractul:** obiectul e „serviciu de transmitere a alertelor și platformă”, cu SLA (nivel de serviciu garantat) pe disponibilitatea platformei și pe timpul de livrare a alertei, nu pe salvare.
- **Poartă înainte de primul lucrător:** aviz scris de avocat pe (a) Codul civil art. 1355 și limitarea răspunderii la vătămări corporale, (b) Legea 333/2003, (c) Directiva 2024/2853; plus ofertă scrisă de asigurare RC care numește „platformă de alarmare pentru persoane”. Fără ofertă de asigurare, nu se pornește.

### La atacul 2 (85%) → Dispeceratul extern devine rezervă, nu fundație
- **Schimbarea:** primul răspuns e dispeceratul clientului. Dacă alarma nu e preluată în 60 de secunde, escaladează automat la telefoanele șefului de tură și ale responsabilului SSM, apoi la un dispecerat de pază ca a treia linie, doar dacă clientul alege și plătește opțiunea.
- **Fără dependența unei singure firme:** firma de pază e opțională și se cere ofertă de la cel puțin 3, cu timp de preluare scris. Clientul fără dispecerat propriu nu e client în anul 1.
- **Legea 333/2003:** intră în avizul de la atacul 1.

### La atacul 3 (85%) → O pană a platformei nu are voie să piardă alarma
- **Calea independentă de server:** fiecare dispozitiv se configurează să trimită SMS de alarmă direct la 2 numere ale clientului (dispecerat și șef de tură). Dacă dispozitivul ales nu poate face asta, nu e ales [de verificat pe mostre: funcția nu e confirmată în note].
- **Supravegherea platformei:** un monitor extern verifică serverul la fiecare minut și trimite SMS la client și la fondator dacă tace; clientul are procedura scrisă „platforma e oprită → treceți pe apel de verificare la 30 de minute”.
- **Om de rezervă:** un tehnician plătit cu abonament (circa 200 EUR pe lună [estimare]) cu manualul de intervenție și acces la server.
- **Construcție mai mică:** Traccar plus reguli plus un ecran APEX simplu; fără funcții „nice to have”. Ținta: 120 h.

### La atacul 4 (80%) → Pilot plătit, cumpărat legal, și un al doilea client privat în paralel
- **Pilotul:** clientul cumpără un serviciu de 3 luni la jumătate de preț (30 × 6 EUR × 3 = 540 EUR) plus dispozitivele (circa 2.700–3.300 EUR). Total mult sub orice prag de achiziție directă [estimare; pragul exact de verificat]. Nu se promite contractul următor; după pilot, clientul cumpără din nou, normal.
- **Înregistrarea în SEAP/SICAP:** ILLUSTRUS își face cont și oferta în catalog înainte de prima discuție cu achizițiile.
- **Al doilea drum:** în paralel, se califică un client privat cu dispecerat propriu (o firmă de pază pentru proprii paznici de noapte, o firmă de exploatare forestieră cu zonă cu semnal, un antreprenor mare) [estimare].

### La atacul 5 (75%) → Ținta se îngustează la lucrătorul singur la suprafață
- **Lucrătorul țintă:** cel care lucrează singur peste o oră, la suprafață, în zonă cu semnal: operatorul de noapte al stației de pompare, echipa de o persoană la avarii, cititorul de contoare, paznicul de noapte [estimare].
- **Căminele și spațiile închise ies din pilot.** Acolo rămâne regula clientului (om la suprafață, detector de gaz). Produsul nu se vinde pentru gaze. Procedura de alarmă scrie: „nu intrați după colegul căzut într-un spațiu închis fără detector și echipament”.
- **Ziua de semnal:** înainte de contract, o zi pe traseele reale cu mostrele.

### La atacul 6 (70%) → Mostre întâi, adaptor de dispozitiv și un al doilea model
- **Nu se cumpără 30 de bucăți** până nu trec 3 mostre (circa 450 EUR cu SIM-uri [estimare]) un test de birou și unul de teren: rețea (2G sau LTE-M), protocol, autonomie pe o tură de 12 ore, SMS direct, cădere și nemișcare.
- **Arhitectura:** un strat de adaptare, astfel încât un al doilea dispozitiv (alt model Teltonika, un telefon robust cu om la pământ ca Sonim XP10, sau Twig pentru clienți mai bogați) să intre fără rescrierea regulilor (RAP §4).
- **GH5200** iese din plan (scos din producție). Se întreabă distribuitorul ce îl înlocuiește.

### La atacul 7 (70%) → Produs „fără urmărire” și sindicatul la masă înainte de pilot
- **Locația pleacă doar la alarmă, pre-alarmă sau la test.** Nimic în afara programului; lucrătorul poate opri dispozitivul la ieșirea din tură. Fără puls, fără productivitate (N05 §6, „Design de produs anti-refuz”).
- **Acordul scris cu sindicatul** e condiție de pornire, nu document de după.
- **Purtarea se măsoară automat:** „dispozitiv pornit și conectat în tură” vine din jurnalul de conectare, nu din chestionar.

### La atacul 8 (65%) → Două săptămâni în „mod umbră”
- **Mod umbră:** în primele 14 zile, alarmele ajung doar în platformă și la fondator, nu la dispecer. Se numără, se reglează pragurile, apoi se pornește dispecerizarea reală. SOS-ul manual merge din ziua 1 la dispecer.
- **Alarmele false au preț:** un număr inclus pe lună și pe lucrător, ca în caietele de sarcini de pază (N05 §2).

### La atacul 9 (60%) → Dispeceratul iese din costul pe lucrător
- **Cu dispeceratul clientului**, costul variabil scade la SIM și mesaje (circa 1,8 EUR pe lucrător [estimare]). Prețul de bază rămâne 12 EUR pe lucrător pe lună cu dispozitivul cumpărat de client; 16 EUR cu dispecerat de pază ca rezervă.
- **Rezultatul pe bani** e în modelul `model_24m.py` (runda 3 și `hardened_plan.md`).

### La atacul 10 (55%) → Livrabilul e dosarul „lucrător izolat”, nu alarma
- **Raportul lunar** pentru șeful SSM: cine a lucrat izolat, câte ture au fost acoperite, câte teste au trecut, în cât timp s-a răspuns. E proba că angajatorul a organizat „supravegherea și legătura cu exteriorul” pentru lucrătorul izolat (HG 1091/2006; formula din N02, „Formula de vânzare”).
- **Testul lunar al procedurii de salvare** (alarmă de test, cronometrată) intră în abonament.

### La atacul 11 (40%) → Două regimuri de păstrare
- **Pozițiile de rutină** nu se păstrează deloc (nu se trimit). **Evenimentele de alarmă** (ora, tipul, pașii, poziția la alarmă) se păstrează pe durata prevăzută de avizul juridic, ca obligație legală a angajatorului de a cerceta evenimentele (Legea 319/2006 art. 26–27, de verificat în N02). Scris în DPIA.

---

## C. Verdictul rundei 1

- **Ce s-a rupt:** rolul de dispecerat (răspundere, cost, timp), pilotul gratuit la o instituție publică, căminele ca loc de pilot, GH5200.
- **Ce a rezistat:** obligația legală (HG 1091/2006), golul de pe piață, ideea de a nu construi hardware, ieșirea pulsului și a gazelor.
- **Investitorul după răspunsuri:** „Mai bine. Acum am o platformă de alarmare cu reguli de siguranță. Dar m-ai mutat de la un risc de răspundere la un risc de diferențiere. Revin în runda 2.”
