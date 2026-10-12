# Planul întărit: sistem de lucru izolat la cheie, pentru angajatorii din Bihor care au deja un dispecerat non-stop

**Ce e documentul:** planul de afaceri al ILLUSTRUS S.R.L. după trei runde de atac (metoda „bullet-proof business plan”). Rundele sunt în `rounds/runda_1.md`, `runda_2.md`, `runda_3.md`; planul inițial e în `00_original_plan.md`; modelul de numerar în `model_24m.py` și `model_24m.out.txt`.

**Data:** 12 octombrie 2026. Fără cercetare web nouă. Faptele trimit la raport (**RAP §n**) și la note (**N01–N06**), cu prescurtările din `00_original_plan.md`. **[estimare]** = judecata evaluatorului sau a cercetării. **[de verificat]** = sursă lipsă, slabă sau din memoria evaluatorului.

---

## 1. Planul pe o pagină

- **Ce vinzi:** un sistem de alarmă pentru lucrătorul care lucrează singur peste o oră, la suprafață, în zonă cu semnal: dispozitiv cu buton SOS și „om la pământ” (cădere și nemișcare), platforma care trimite alarma, regulile reglate pe lucrătorii clientului, testul lunar al procedurii de salvare, raportul lunar pentru SSM (securitate și sănătate în muncă) și pachetul de documente legale.
- **Cine răspunde la alarmă:** dispeceratul non-stop al clientului (de exemplu, dispeceratul de avarii al unei utilități), apoi telefoanele șefului de tură și ale responsabilului SSM. Un dispecerat de pază poate fi a treia linie, la cerere. **ILLUSTRUS nu este dispecerat.**
- **Cui vinzi întâi:** angajatorilor care au deja un dispecerat non-stop și lucrători singuri: utilitățile din Oradea (Compania de Apă, Termoficare, RER Vest) și, în paralel, un client privat (o firmă de pază pentru paznicii ei de noapte sau un antreprenor mare) [estimare; nicio organizație nu a confirmat încă].
- **Ce nu vinzi în anul 1:** cămine și alte spații închise, gaze, puls, stres termic măsurat pe corp, apropiere de utilaje, pădure fără semnal, zone ATEX (cu pericol de explozie).
- **Prețul:** 12 EUR pe lucrător pe lună, cu dispozitivul cumpărat de client; 16 EUR cu dispecerat de pază ca rezervă. Pilot de 3 luni plătit la jumătate de preț [estimare].
- **Primul pas nu e codul, ci poarta 0:** 8 săptămâni de interviuri (noiembrie–decembrie 2026). Nicio cheltuială peste 1.000 EUR până nu trece poarta.
- **Pierderea maximă dacă totul pică:** circa 2.000 EUR la poarta 0, circa 4.350 EUR dacă pică pilotul [estimare, `model_24m.out.txt`, scenariul „eșec”].
- **Ce e, spus cinstit:** o afacere locală de servicii, cu venit lunar recurent, nu un caz pentru un fond de risc. În scenariul de bază ajunge la circa 290 de lucrători și circa 4.200 EUR venit lunar în luna 24, fără salariu pentru fondator [estimare].

---

## 2. Ce s-a rupt în runde

- **Rolul de dispecerat al ILLUSTRUS.** O firmă de o persoană, la mijlocul unui lanț de viață și de moarte, cu o clauză de limitare a răspunderii care s-ar putea să nu țină la vătămări corporale (din memoria evaluatorului, Codul civil art. 1355 alin. 2, [de verificat]) (runda 1, atacul 1).
- **Firma de pază ca fundație.** Pentru 75 EUR pe lună (30 × 2,50 EUR, tarif fără ofertă reală, N05 §4), nimeni nu ține un operator în ecranul tău la 3 noaptea (runda 1, atacul 2).
- **Pilotul gratuit cu promisiune de contract la o companie municipală.** Nu se potrivește cu achizițiile publice; pragul de achiziție directă e „din memorie” chiar în raport (RAP §1; runda 1, atacul 4).
- **Căminele ca loc de pilot.** Cel mai slab semnal și cel mai mare risc de gaze; Germania spune că alarmele prin rețele publice depind de rețea (N02; runda 1, atacul 5).
- **GH5200.** Scos din producție (RAP §4).
- **„Platforma e greu de copiat”.** Traccar e gratuit, Teltonika e deja la integratorii de flotă (runda 2, atacul 2).
- **„Statul cumpără repede”.** Bugetul pe 2027 abia se aprobă (runda 2, atacul 5) [estimare].

---

## 3. Ce s-a schimbat, pe temele cerute

### 3.1. Răspunderea juridică dacă alarma nu ajunge
- **Mecanismul riscului:** un lucrător moare; cercetarea caută unde s-a pierdut alarma; dacă s-a pierdut în software-ul tău, ești în discuție pentru daune (sumele pentru decesul unei rude pot depăși 100.000 EUR, RAP §2) și, după 9 decembrie 2026, ca producător de software după Directiva 2024/2853 (RAP §5).
- **Ce s-a schimbat:**
  - ILLUSTRUS livrează platforma și regulile; răspunsul la alarmă e al angajatorului, unde e deja răspunderea SSM (N06 §1, CNPP: răspunderea „revine în mod direct și exclusiv angajatorului”). Modelul are precedent: auto-monitorizarea la Vatix (N05 §6) și „procedura de salvare validată” cerută de INRS în Franța (RAP §5).
  - **Regula „platforma nu înghite alarme”:** niciun filtru software nu șterge o alarmă; filtrul e doar pre-alarma de pe dispozitiv, anulată de lucrător. „Falsă” o declară un om, după apel.
  - **O cale independentă de server:** dispozitivul trimite SMS direct la 2 numere ale clientului [de verificat pe mostre].
  - **Poartă juridică:** aviz scris de avocat pe Codul civil (limitarea răspunderii la vătămări), Legea 333/2003 (dispecerate de pază) și Directiva 2024/2853, înainte de primul lucrător echipat.
  - **Poartă de asigurare:** poliță RC (răspundere civilă) profesională semnată, care numește activitatea, înainte de ieșirea din modul umbră. Fără poliță, nu se pornește.
  - **Procedura de incident** scrisă înainte de pilot: jurnal înghețat și semnat în prima oră, raport tehnic în 24 de ore, nicio declarație fără avocat.

### 3.2. Dispeceratul de pază ca punct unic de eșec
- **Mecanismul riscului:** o singură firmă, operatori instruiți pentru efracție, un al doilea ecran, un stimulent de câțiva zeci de euro pe lună.
- **Ce s-a schimbat:** trei linii, în ordine: dispeceratul clientului → telefoanele șefului de tură și ale responsabilului SSM, după 60 de secunde fără preluare → dispecerat de pază, doar la cerere și plătit (16 EUR). Pentru opțiunea de pază se cer 3 oferte cu timp de preluare scris. **Un client fără dispecerat propriu nu e client în anul 1.**

### 3.3. Timpul fondatorului (10–12 h pe săptămână) față de o alarmă non-stop
- **Mecanismul riscului:** un student, un server, o noapte de sâmbătă.
- **Ce s-a schimbat:**
  - fondatorul nu răspunde la alarme (le preia clientul), răspunde doar de platformă;
  - o pană a platformei nu pierde alarma (SMS direct), iar un monitor extern anunță clientul în cel mult un minut; clientul are procedura „platforma e oprită → apel de verificare la 30 de minute”;
  - găzduire plătită, în UE, cu SLA (nivel de serviciu garantat) și un al doilea nod pentru primirea alarmelor; nu Oracle „Always Free” pe calea de alarmă;
  - tehnician de rezervă cu abonament și tarif de intervenție, cu manual scris;
  - suport cu jumătate de normă la 150 de lucrători sau la 3 luni la rând peste 50 h, oricare vine primul; cel mult un client nou pe lună până atunci; nicio pornire în sesiunea de examene;
  - instruirea lucrătorilor o face clientul sau serviciul extern SSM, după kitul ILLUSTRUS.
- **Ce rămâne:** modelul arată că, și așa, fondatorul trece de circa 47 h pe lună în 9 din 24 de luni în scenariul de bază [estimare]. Timpul, nu banii, limitează creșterea.

### 3.4. Cererea reală la utilitățile de stat (achiziții publice)
- **Mecanismul riscului:** nimeni nu a spus „da”; cumpărarea trece prin SEAP/SICAP (sistemul electronic de achiziții publice); bugetul și ciclul sunt lente; operatorii de apă pot fi și sub regulile achizițiilor sectoriale (Legea 99/2016, din memorie, [de verificat]).
- **Ce s-a schimbat:**
  - **poarta 0** (secțiunea 6) cere confirmări scrise de la cel puțin 2 organizații înainte de cheltuieli;
  - pilotul e **un serviciu plătit, cumpărat direct**: 30 × 6 EUR × 3 luni = 540 EUR plus dispozitivele (circa 2.700–3.300 EUR), mult sub orice prag plauzibil [estimare]; nu se promite contractul următor;
  - ILLUSTRUS își face cont și ofertă în catalogul SEAP înainte de discuția cu achizițiile;
  - un drum privat în paralel; primul care semnează un pilot plătit devine pilotul.

### 3.5. Adoptarea de către muncitori
- **Mecanismul riscului:** 59% nu ar purta dispozitive de urmărire (RAP §1, studiu văzut prin rezumat); sindicatul trebuie consultat înainte (Legea 190/2018); dispozitivul descărcat rămâne în mașină.
- **Ce s-a schimbat:**
  - locația pleacă doar la alarmă, la pre-alarmă și la test; nimic în afara programului; dispozitivul se poate opri la sfârșitul turei; fără puls, fără productivitate (N05 §6);
  - acordul scris cu sindicatul e condiție de pornire;
  - încărcarea e a clientului: suport de încărcare la începutul turei, verificare „pornit și conectat” de șeful de tură;
  - purtarea se măsoară automat din jurnalul de conectare.

### 3.6. Alarmele false
- **Mecanismul riscului:** un om care îngenunchează arată ca un om căzut; după 20 de alarme false, dispecerul nu mai sună; nicio rată de teren nu e publicată (N05 §6).
- **Ce s-a schimbat:**
  - **14 zile de mod umbră:** cădere și nemișcare ajung doar în platformă, nu la dispecer; se numără și se reglează pragurile; SOS-ul manual merge la dispecer din ziua 1;
  - un număr de alarme false inclus în preț, ca în caietele de sarcini de pază (N05 §2);
  - datele din modul umbră pot susține un voucher UEFISCDI cu Universitatea din Oradea, dacă cumulul de minimis cu DR-36 e în regulă (N06 §3).

### 3.7. Dependența de Teltonika (GH5200 scos din producție)
- **Mecanismul riscului:** un singur producător, fără distribuitor în România (RAP §3), cu modele retrase; TMT250 poate fi doar 2G, cu protocol neconfirmat (N04 §1).
- **Ce s-a schimbat:**
  - GH5200 iese din plan; se cer 3 mostre (circa 450 EUR cu SIM-uri) și se testează pe birou și pe teren înainte de orice comandă;
  - un strat de adaptare în platformă, ca un al doilea dispozitiv să intre fără rescrierea regulilor;
  - ordinea planului B: TMT250 sau înlocuitorul indicat de distribuitor → telefon robust cu om la pământ (Sonim XP10, Cat S75 la circa 330 EUR) → Twig One (793 EUR) pentru clienți care plătesc mai mult (RAP §4).

### 3.8. GDPR și Legea 190/2018
- **Mecanismul riscului:** ANSPDCP (autoritatea pentru protecția datelor) a amendat deja GPS-ul folosit în afara programului sau păstrat peste 30 de zile (2.000–4.000 EUR, N05 §6); jurnalul de probe și regula de 30 de zile se contrazic.
- **Ce s-a schimbat:**
  - **două regimuri de păstrare, scrise în DPIA (evaluarea de impact asupra protecției datelor):** pozițiile de rutină nu există (nu se trimit); evenimentele de alarmă (ora, tipul, pașii, poziția la alarmă) se păstrează cât spune avizul juridic, ca parte din obligația angajatorului de a cerceta evenimentele (Legea 319/2006 art. 26–27, [de verificat], N02);
  - angajatorul e operator, ILLUSTRUS e împuternicit, cu contract după art. 28 GDPR; dispeceratul de pază și găzduirea sunt sub-împuterniciți (RAP §5);
  - nicio componentă LLM sau ML (învățare automată) în calea alarmei; în DPIA scrie „nu este sistem AI” (RAP §5, AI Act).

---

## 4. Calendarul

- **Lunile 1–2 (noiembrie–decembrie 2026): poarta 0.** Interviuri (lista din secțiunea 6), aviz juridic, ofertă de asigurare, 3 mostre, o zi de măsurare a semnalului pe traseele reale. Circa 35 h pe lună.
- **Lunile 3–5 (ianuarie–martie 2027): construcția și documentele.** Traccar, regulile, SMS direct, monitor extern, ecran de dispecerat, raport lunar; pachetul de documente A–F (RAP §5). Circa 120–160 h. Achiziția pilotului la client.
- **Lunile 6–8 (aprilie–iunie 2027): pilotul plătit.** 14 zile mod umbră, apoi funcționare reală, test săptămânal pe echipă, raport săptămânal.
- **Luna 9–10: decizia** clientului și contractul pe 12 luni.
- **Lunile 10–24: creștere** de circa 20 de lucrători pe lună în scenariul de bază, cel mult un client nou pe lună până la angajarea suportului.

---

## 5. Numerele (modelul pe 24 de luni) [estimare]

- **Ipoteze principale:** 12 EUR pe lucrător (16 EUR pentru 30% care iau dispecerat de pază, cost 3 EUR plus minim 150 EUR pe lună); marjă de 20 EUR pe fiecare dispozitiv vândut; SIM și mesaje 1,8 EUR pe lucrător; găzduire și unelte 130 EUR pe lună; tehnician de rezervă 200 EUR pe lună; asigurare 900 EUR pe an (preț necunoscut); aviz juridic 1.500 EUR; comision 15% pe un an pentru 40% din clienți; suport cu jumătate de normă 600 EUR pe lună de la 150 de lucrători.
- **De bază:** 289 de lucrători în luna 24, venit lunar circa 4.200 EUR, rezultat lunar circa +2.000 EUR, numerar minim 20.800 EUR, numerar în luna 24 circa 35.700 EUR. Fondatorul nu e plătit.
- **De bază, cu 800 EUR pe lună pentru fondator din luna 10:** numerar în luna 24 circa 23.700 EUR.
- **Pesimist:** 92 de lucrători, venit lunar circa 1.370 EUR, numerar în luna 24 circa 21.400 EUR.
- **Optimist:** 516 lucrători, venit lunar circa 7.500 EUR; orele fondatorului depășesc capacitatea în 17 din 24 de luni, deci creșterea asta cere mai mult personal decât presupune modelul.
- **Eșec la pilot:** oprire în luna 10, circa 4.350 EUR cheltuiți.
- **Concluzia:** capitalul de 25.000 EUR ajunge cu mult. Riscurile reale sunt cererea, comportamentul dispozitivului și orele.

---

## 6. Poarta 0 și cele 5 întrebări pentru clienți reali, înainte de a cheltui bani

**Pe cine întrebi:** 3 utilități (Compania de Apă Oradea, Termoficare Oradea, RER Vest), 2 servicii externe SSM, 2 firme de pază, o firmă privată de exploatare forestieră și un antreprenor mare, plus un broker de asigurări, un avocat și ITM Bihor (RAP §9).

**Cele 5 întrebări:**
1. **Câți oameni lucrează la voi singuri mai mult de o oră, în ce ture și unde, și ce folosiți acum ca să aflați că unul dintre ei a căzut?** (Ne spune dacă lucrătorul țintă există și cât de mult; răspunsul „au telefon” e concurentul real.)
2. **Dacă o alarmă de „om căzut” sosește la 3 noaptea, cine din organizația voastră o preia în 60 de secunde și ce face apoi? Puteți scrie asta într-o procedură?** (Fără un dispecerat non-stop al clientului, modelul nu merge.)
3. **Cine ar aproba și din ce buget ar plăti un pilot de 3 luni pentru 30 de oameni, de circa 3.800 EUR cu tot cu dispozitive, și cât durează de la „da” până la comanda fermă?** (Testează bugetul, procedura de achiziție și calendarul.)
4. **Ce ar spune sindicatul sau reprezentanții lucrătorilor despre un dispozitiv care trimite locația doar la alarmă, și cine ar trebui să fie la masă de la început?** (Testează adoptarea și Legea 190/2018 înainte de cod.)
5. **Ce ar trebui să vă arate pilotul, în cifre, ca să plătiți 12 EUR pe lucrător pe lună un an întreg?** (Arată dacă valoarea e conformitatea, liniștea șefului SSM sau altceva; fără o alarmă reală gravă, pilotul nu poate dovedi vieți salvate, RAP §6.)

**Pragul de trecere (toate trei):**
- cel puțin 2 organizații confirmă în scris lucrători singuri, un dispecerat care poate prelua alarma și un buget pentru pilot;
- un broker confirmă că activitatea se poate asigura și dă ordinul de mărime al primei;
- avocatul nu găsește un obstacol de licență sau de răspundere care blochează modelul.

---

## 7. Riscurile care rămân (probabilitate, impact, mecanism) [estimare]

- **Nicio organizație nu are lucrători singuri și dispecerat dispus să preia alarma.** Probabilitate: medie (circa 40%). Impact: fatal. Mecanism: lucrul izolat e rar organizat ca atare în România, piața nu are vocabular (RAP §1), iar dispecerii de avarii refuză o sarcină nouă. Se află la poarta 0.
- **Asigurătorul refuză sau cere o primă prea mare.** Probabilitate: medie (circa 30%). Impact: fatal pentru modul real. Mecanism: activitate nouă, fără istoric de daune, încadrată ca pază (N02 întrebarea 10). Se află la poarta 0.
- **Avizul juridic spune că limitarea răspunderii nu ține și că o pierdere de alarmă din vina software-ului e pe ILLUSTRUS fără plafon.** Probabilitate: medie-mare (circa 50%). Impact: mare. Mecanism: Codul civil la vătămări corporale [de verificat] și Directiva 2024/2853. Se atenuează prin calea SMS independentă, regula „nu înghite alarme” și asigurare; nu dispare.
- **Dispozitivul ales nu trece testul de teren (rețea, SMS direct, autonomie pe 12 ore).** Probabilitate: medie (circa 35%). Impact: mare (planul B costă de 3–4 ori mai mult pentru client). Mecanism: TMT250 posibil doar 2G, GH5200 retras (N04 §1).
- **Purtarea scade sub 60% după primele săptămâni.** Probabilitate: medie (circa 30%). Impact: mare. Mecanism: baterie, incomoditate, frica de urmărire (RAP §1).
- **Alarmele false rămân mari după reglaj.** Probabilitate: medie (circa 30%). Impact: mediu-mare. Mecanism: munca în genunchi sau statul pe loc arată ca o cădere; nicio rată publicată (N05 §6).
- **Achiziția publică întârzie pilotul cu 4–6 luni.** Probabilitate: mare (circa 50%). Impact: mediu (scenariul pesimist din model). Mecanism: buget anual, procedură, schimbări de conducere (N05 §2).
- **Un integrator de flotă sau o firmă de pază copiază serviciul.** Probabilitate: medie (circa 35% în 24 de luni). Impact: mediu. Mecanism: au deja Teltonika și relația cu clientul (N04; N05 §5).
- **Fondatorul nu poate ține ritmul.** Probabilitate: mare (circa 50%). Impact: mediu-mare. Mecanism: în model, depășire de ore în 9 din 24 de luni; sesiunile de examene (N00; `model_24m.out.txt`).
- **Un accident grav la un lucrător echipat, indiferent de cauză.** Probabilitate: mică în 24 de luni pe câteva sute de oameni, dar nu zero. Impact: foarte mare (reputație, proces). Mecanism: cercetarea ITM și cea penală trec prin jurnalul tău (RAP §5).

---

## 8. Pre-mortem: de ce a murit afacerea în 18 luni (aprilie 2028)

Povestea cea mai probabilă, spusă ca și cum s-ar fi întâmplat [estimare]:
- **Luna 2:** interviurile au fost entuziaste („foarte interesant”), dar nimeni nu a scris că are un dispecerat care preia alarma. Fondatorul a trecut poarta 0 pe „aproape”, în loc de prag.
- **Lunile 3–6:** construcția a durat de două ori mai mult, pentru că TMT250 nu trimitea SMS direct cum se credea și a trebuit integrat un telefon robust. Sesiunea din ianuarie–februarie a mâncat 6 săptămâni.
- **Lunile 6–10:** Compania de Apă a vrut pilotul, dar l-a putut cumpăra abia după aprobarea bugetului, în primăvară. Sindicatul a cerut încă o rundă de discuții. Pilotul a pornit în luna 10.
- **Lunile 10–13:** în modul umbră au fost 40 de alarme false pe săptămână de la operatorii de stație, care stau mult pe scaun. După reglaj, „om la pământ” abia mai detecta ceva. Purtarea a scăzut la 55%. Dispecerul de avarii a cerut să nu mai primească alarmele de nemișcare.
- **Lunile 14–16:** clientul a spus „interesant, dar nu acum”; noul director a avut alte priorități. Al doilea client (o firmă de pază) a preluat procedura și și-a făcut singur sistemul cu un integrator de flotă.
- **Luna 18:** fondatorul, cu 25 de lucrători plătitori și fără timp, a închis.

**Ce oprește această poveste în plan:** pragul numeric al porții 0 (nu „aproape”), testul de teren pe mostre înaintea construcției, nicio pornire în sesiune, modul umbră cu reguli de oprire, diversificarea din luna 18, clauza de neconcurență cu firma de pază.

---

## 9. Condițiile de oprire (scrise dinainte)

- **La poarta 0 (sfârșitul lunii 2):** mai puțin de 2 confirmări scrise (lucrători singuri, dispecerat, buget) → stop sau încă cel mult 4 săptămâni de interviuri, apoi stop.
- **Asigurare:** niciun asigurător nu acceptă activitatea până în luna 4 → nu se pornește modul real.
- **Aviz juridic:** licență obligatorie după Legea 333/2003 pe care ILLUSTRUS nu o poate obține, sau răspundere fără plafon neasigurabilă → stop sau schimbarea modelului (de exemplu, licențierea platformei unei firme de pază licențiate).
- **Dispozitive:** niciun dispozitiv sub 350 EUR nu trece testul de teren → stop sau pauză până apare unul.
- **În pilot:** alarmele de test ajung sub 95% sau purtarea sub 60% două săptămâni la rând → oprirea pilotului (ținta din RAP §6, păstrată).
- **Alarme false:** după 14 zile de mod umbră și reglaj, peste 2 la 100 de ture-om (ținta din RAP §6) fără ca „om la pământ” să-și piardă sensibilitatea la testele de cădere → doar SOS manual sau stop.
- **După pilot:** clientul nu semnează contract plătit în cel mult 3 luni → stop pe acest segment; se mai încearcă o singură dată cu clientul privat.
- **Luna 24:** sub 150 de lucrători plătitori sau un client peste 60% din venit → decizia scrisă: închidere, vânzarea platformei unui integrator de flotă, sau continuare ca proiect secundar fără investiții noi.

---

## 10. Ce nu se poate repara pe hârtie

- **Cererea:** nimeni nu a fost întrebat încă.
- **Dispozitivul în teren:** rețeaua, autonomia, SMS-ul direct și calitatea algoritmului om la pământ nu sunt publicate de niciun producător (N04 §1).
- **Asigurarea și avizul juridic:** nu există nicio ofertă sau opinie în note.

Toate trei se află în primele 8–10 săptămâni, cu sub 2.000 EUR. De acolo începe planul.
