# Runda 2: atacurile investitorului, răspunsurile și verdictul (planul v1 → v2)

**Investitorul:** același. Acum atacă planul v1 din `runda_1.md`, secțiunea B. Probabilitățile sunt tot „de respingere dacă rămâne nerezolvat”. Fără cercetare web nouă; prescurtările surselor sunt în `00_original_plan.md`.

---

## A. Atacurile

### Atacul 1. Încă nu ai vorbit cu niciun client
- **Probabilitatea de respingere: 75%**
- **Logica:** Toată runda 1 a reparat planul pe hârtie. Nu există niciun interviu, nicio scrisoare de intenție, niciun buget. „Utilitățile au dispecerat de avarii non-stop” e acum fundația planului v1 și e o presupunere. Dacă Compania de Apă spune „nu avem pe cine pune să răspundă la un om căzut”, v1 cade.
- **Dovezi:**
  - Lista de oameni de sunat există, dar niciunul nu a fost sunat [RAP §9].
  - Pentru Termoficare Oradea și DEER (Distribuție Energie Electrică Romania) nu există nici măcar efective [fapt: lipsă, N05 §1 Gaps].
  - Nu există niciun angajator român care să declare că folosește astfel de dispozitive [fapt: lipsă, N05 §7].
- **Ce m-ar face să schimb votul:** o poartă de validare înainte de orice cheltuială mare, cu un prag numeric.

### Atacul 2. Fără dispecerat, ce mai e al tău? Un panou Traccar cu logo
- **Probabilitatea de respingere: 60%**
- **Logica:** Traccar e gratuit. Firmele de GPS de flotă din România integrează deja dispozitive Teltonika și au vânzători la aceleași utilități, pentru mașini [estimare; prețul de flotă de 50 lei pe vehicul e fapt, RAP §7]. Pentru ele, „om la pământ” e o setare pe un tracker în plus. Dacă tu nu răspunzi la alarmă, avantajul tău e mic și ușor de copiat.
- **Dovezi:**
  - Traccar e open-source și discută deja dispozitivele Teltonika [fapt, N04 §1 și „Inferences”].
  - Teltonika publică singur cazul „Lone worker monitoring with GH5200” [fapt, N04 §1].
  - Firmele de pază „pot copia serviciul” [estimare, N05 §5].
- **Ce m-ar face să schimb votul:** să știu ce cumpără clientul de la tine și nu poate lua de la un integrator de flotă.

### Atacul 3. SMS-ul direct și monitorul extern reduc riscul, dar răspunderea de produs rămâne
- **Probabilitatea de respingere: 50%**
- **Logica:** Software-ul e produs după Directiva 2024/2853, pentru produsele puse pe piață după 9 decembrie 2026. Pilotul tău pornește după această dată. Dacă regula ta din n8n (sau din Traccar) a filtrat o alarmă reală ca falsă, defectul e al tău, indiferent cine răspunde la telefon. Iar asigurătorul poate refuza: nimeni nu știe dacă un asigurător român acceptă „platformă de alarmare pentru persoane”.
- **Dovezi:** RAP §5 (Directiva 2024/2853); N02 întrebarea 10 (Legea 240/2004 până la transpunere, de verificat); N05 §6 Gaps (niciun preț RC).
- **Ce m-ar face să schimb votul:** o regulă de produs care face imposibil ca software-ul tău să „înghită” o alarmă, și o poartă clară pe asigurare.

### Atacul 4. Bus factor: un tehnician cu abonament nu e o echipă
- **Probabilitatea de respingere: 50%**
- **Logica:** Un tehnician plătit 200 EUR pe lună nu va răspunde la 3 noaptea dacă nu e plătit și pentru gardă. APEX pe ce rulează? Dacă e Oracle Cloud „Always Free”, nu ai niciun SLA pentru un serviciu de alarmă [estimare]. Dacă fondatorul e la examene două săptămâni, cine face instruirea la al doilea client?
- **Dovezi:** N00 (10–12 h, 0–1 angajați); RAP §6 („Siguranța lanțului”), fără nicio mențiune despre găzduire și SLA.
- **Ce m-ar face să schimb votul:** găzduire plătită cu SLA, manual de intervenție, și o regulă scrisă care spune când angajezi.

### Atacul 5. Ciclul de vânzare la stat îți mănâncă primul an
- **Probabilitatea de respingere: 50%**
- **Logica:** Suntem în octombrie 2026. Bugetul pe 2027 al unei companii municipale se aprobă de obicei la început de an [estimare]. Cu pilotul cumpărat la jumătatea lui 2027, primul contract real vine spre toamnă. Plata la stat vine la 30–60 de zile [estimare]. Un an întreg cu un singur client posibil.
- **Dovezi:** N05 §2 (decizia la director general și SSM, prin SEAP; la corporații 6–12 luni); RAP §1 (pragul de achiziție directă de verificat).
- **Ce m-ar face să schimb votul:** un client privat care poate porni în paralel și un calendar care nu presupune că statul cumpără repede.

### Atacul 6. Mostrele pot pica toate
- **Probabilitatea de respingere: 40%**
- **Logica:** Dacă TMT250 e doar 2G și nu are SMS direct, iar GH5200 nu se mai găsește, rămâi cu Twig (793 EUR) sau cu un telefon robust (circa 330 EUR), care schimbă complet economia. Sau cu o aplicație Android proprie, de 20–40 de zile-om, pe care nu o ai.
- **Dovezi:** N04 §1 (prețuri Twig), N04 §3 (Cat S75), N04 „Integrarea” (aplicație Android 20–40 zile-om).
- **Ce m-ar face să schimb votul:** un plan B cu preț și o regulă de oprire dacă și planul B pică.

### Atacul 7. Sindicatul semnează, dar muncitorul tot nu poartă
- **Probabilitatea de respingere: 40%**
- **Logica:** Acordul cu sindicatul rezolvă legalitatea, nu purtarea. Un dispozitiv de 800 mAh care se descarcă la jumătatea turei e lăsat în mașină. Cine încarcă 30 de dispozitive în fiecare zi?
- **Dovezi:** RAP §4 (baterie 800 mAh, autonomie necunoscută); N05 §6 Gaps (nicio rată de purtare din teren).
- **Ce m-ar face să schimb votul:** o rutină de încărcare la client și cineva de la client care răspunde de ea.

### Atacul 8. 12 EUR pentru „platformă” e scump fără dispecerat
- **Probabilitatea de respingere: 35%**
- **Logica:** Ai scos dispeceratul, dar prețul a rămas 12 EUR. Clientul compară cu GPS-ul de flotă de 50 lei (10 EUR) pe vehicul, care vine cu om de suport. Diferența trebuie justificată.
- **Dovezi:** RAP §7 („Cum argumentezi prețul”), N05 §3.
- **Ce m-ar face să schimb votul:** ce primește clientul pentru acești bani, enumerat.

---

## B. Răspunsurile (planul v2)

### La atacul 1 (75%) → Poarta 0: nicio cheltuială peste 1.000 EUR fără dovezi de cerere
- **În lunile 1–2 (noiembrie–decembrie 2026), doar interviuri**, circa 35 h pe lună: 3 utilități (Compania de Apă Oradea, Termoficare Oradea, RER Vest), 2 servicii externe SSM, 2 firme de pază (ca clienți pentru paznicii lor de noapte și ca dispecerat de rezervă), 2 firme private (o firmă de exploatare forestieră, un antreprenor), 1 broker de asigurări, 1 avocat, ITM Bihor (lista e în RAP §9).
- **Pragul de trecere (toate trei):**
  - cel puțin 2 organizații confirmă în scris că au lucrători singuri peste o oră, un dispecerat non-stop care poate prelua alarma și un buget pentru un pilot plătit;
  - un broker confirmă că activitatea se poate asigura și dă un ordin de mărime al primei;
  - avocatul nu găsește un obstacol de licență (Legea 333/2003) sau de răspundere care să blocheze modelul.
- **Dacă nu trece:** stop, cu circa 2.000 EUR cheltuiți [estimare]. Vezi condițiile de oprire din `hardened_plan.md`.

### La atacul 2 (60%) → Clientul cumpără un „sistem de lucru izolat la cheie”, nu un panou
- **Ce nu ia de la un integrator de flotă [estimare]:**
  - pachetul de conformitate: evaluarea riscului „lucru izolat”, procedura de salvare, DPIA, acordul-șablon cu sindicatul, nota de informare, regimurile de păstrare (RAP §5, documentele A–F);
  - regulile de alarmă reglate în mod umbră pe lucrătorii lui, cu raportul de alarme false;
  - testul lunar al procedurii, cronometrat, și raportul lunar pentru SSM și pentru ITM;
  - ecranul de dispecerat cu pașii scriși și ora fiecărui pas, gândit pentru dispecerul de avarii al clientului, nu pentru un operator de pază.
- **Integratorul de flotă e partener, nu doar concurent.** Dacă unul vinde deja Teltonika la aceeași utilitate, i se oferă comision pentru a recomanda (sau licențiere a platformei). Plan scris pentru „ziua copierii”: prețul coboară la nivelul pachetului de conformitate, iar platforma rămâne ca serviciu.
- **Spus cinstit:** avantajul nu e tehnologic. E o afacere locală de servicii, cu o barieră mică de intrare. Nu e un caz de fond de risc.

### La atacul 3 (50%) → „Platforma nu are voie să tacă”
- **Regula de produs:** nicio regulă din software nu șterge o alarmă. Filtrul de alarme false e doar pe dispozitiv (pre-alarma pe care lucrătorul o anulează). Orice eveniment care ajunge la server merge la dispecer; „falsă” o declară un om, după apel.
- **SMS-ul direct din dispozitiv** rămâne calea de rezervă, testată zilnic.
- **Poarta de asigurare:** fără poliță semnată (nu doar ofertă), nu se pornește modul real după modul umbră.

### La atacul 4 (50%) → Găzduire cu SLA, gardă plătită și regula de angajare
- **Găzduire:** server administrat plătit, în UE, cu copie de rezervă și un al doilea nod pentru partea de primire a alarmelor (circa 80 EUR pe lună [estimare]). Nu Oracle „Always Free” pentru calea de alarmă; APEX poate rămâne pentru rapoarte.
- **Gardă:** tehnicianul de rezervă are abonament lunar plus tarif pe intervenție; manualul de intervenție e scris înainte de pilot.
- **Regula de angajare:** la 150 de lucrători activi sau la 3 luni la rând cu peste 50 h de muncă pe lună, se angajează suport cu jumătate de normă (circa 600 EUR pe lună [estimare, RAP §7: 1.200 EUR pe normă]).
- **Calendar academic:** nicio pornire de client în sesiunea de examene.

### La atacul 5 (50%) → Două drumuri în paralel, cu cel privat ca plasă
- **Drumul public:** pilotul plătit, cumpărat direct, cu oferta în catalogul SEAP. Calendarul presupune bugetul 2027 și pornirea în primăvară.
- **Drumul privat:** în același timp, un client privat cu dispecerat propriu. Primul candidat: firmele de pază, care au paznici de noapte singuri și dispecerat non-stop [estimare]. Al doilea: un antreprenor mare cu șantier în Bihor.
- **Regula:** primul care semnează pilotul plătit devine pilotul. Celălalt e al doilea client.

### La atacul 6 (40%) → Planul B cu preț și regula de oprire
- **Ordinea testului pe mostre:** TMT250 (sau înlocuitorul indicat de distribuitor) → telefon robust cu om la pământ (Sonim XP10 sau Cat S75 cu aplicație existentă) → Twig One pentru clienți care plătesc mai mult.
- **Efectul pe preț [estimare]:** cu telefon de circa 330 EUR cumpărat de client, abonamentul rămâne 12 EUR, dar investiția clientului crește de circa 3–4 ori.
- **Oprire:** dacă niciun dispozitiv sub 350 EUR nu trece testul de teren (rețea, SMS direct, o tură de 12 ore, cădere și nemișcare), proiectul se oprește sau așteaptă.

### La atacul 7 (40%) → Încărcarea e a clientului, scrisă
- **Rutina:** un suport de încărcare la punctul de început de tură; șeful de tură verifică pe ecran „pornit și conectat” la începutul turei. Raportul săptămânal arată cine nu a purtat.
- **Purtarea sub 60% două săptămâni la rând** = pilotul se oprește (ținta originală, păstrată).

### La atacul 8 (35%) → Ce cumpără clientul cu 12 EUR, enumerat
- platforma și regulile; SMS-urile și SIM-ul; mod umbră și reglajul; pachetul de conformitate și actualizarea lui; testul lunar al procedurii; raportul lunar; suport în orele de lucru; un număr de alarme false incluse.
- **Opțional, 16 EUR:** dispecerat de pază ca linie de rezervă, la firma aleasă de client.

---

## C. Verdictul rundei 2

- **Ce s-a rupt:** presupunerea că statul cumpără repede, „tehnicianul de rezervă” ca soluție de continuitate, ideea că platforma e greu de copiat.
- **Ce s-a schimbat:** o poartă de validare înaintea banilor, două drumuri de vânzare, produsul definit ca „sistem de lucru izolat la cheie”, regula „platforma nu înghite alarme”, regula de angajare.
- **Investitorul după răspunsuri:** „Acum e o afacere mică, onestă, care se poate opri ieftin. Nu e o investiție pentru mine. Dar pot spune ce trebuie să se întâmple ca să devină interesantă. Runda 3.”
