# Runda 3: atacurile investitorului, răspunsurile și verdictul (planul v2 → planul final)

**Investitorul:** același. Atacă planul v2 din `runda_2.md`, secțiunea B, și modelul de numerar `model_24m.py` (ieșirea în `model_24m.out.txt`). Toate cifrele modelului sunt **[estimare]** a evaluatorului; reperele de pornire sunt în RAP §6–7 și N05 §4. Fără cercetare web nouă.

**Ce spune modelul, pe scurt [estimare]:**
- **De bază** (pilot plătit în lunile 6–8, adică aprilie–iunie 2027; contract din luna 10; +20 de lucrători pe lună): 289 de lucrători și circa 4.200 EUR venit lunar în luna 24; numerarul minim 20.800 EUR; fondatorul nu e plătit.
- **Pesimist** (pilot amânat cu 4 luni, +8 pe lună, 2% pierderi lunare de clienți): 92 de lucrători, circa 1.370 EUR pe lună în luna 24.
- **Optimist** (+35 pe lună): 516 lucrători, circa 7.500 EUR pe lună.
- **De bază, cu 800 EUR pe lună pentru fondator din luna 10:** numerarul rămâne aproape de cel de pornire (23.700 EUR în luna 24).
- **Eșec la pilot:** oprire în luna 10, cu circa 4.350 EUR cheltuiți.
- **Orele:** în scenariul de bază, fondatorul trece de circa 47 h pe lună în 9 din 24 de luni, chiar cu suportul angajat la 150 de lucrători.

---

## A. Atacurile

### Atacul 1. Banii nu sunt problema; timpul tău e
- **Probabilitatea de respingere: 45%**
- **Logica:** Cea mai mare pierdere de numerar e circa 5.000–6.000 EUR. Ai 25.000. Dar în scenariul de bază depășești capacitatea în 9 luni, iar creșterea de 20 de lucrători pe lună cere circa un client nou la fiecare 1–2 luni, cu ciclu de vânzare, instruire și documente. Creșterea e limitată de ore, nu de capital. Și planul nu spune ce faci cu banii nefolosiți.
- **Dovezi:** `model_24m.out.txt`, coloana „peste capacitate”; N00 (10–12 h pe săptămână).
- **Ce m-ar face să schimb votul:** o regulă care transformă banii în ore (cine preia ce) și o listă de lucruri pe care fondatorul nu le face.

### Atacul 2. La 24 de luni ai o afacere de buzunar, nu o companie
- **Probabilitatea de respingere: 45%**
- **Logica:** 4.200 EUR pe lună în scenariul de bază, fără salariu pentru fondator. Pragul de rentabilitate din raport (160–700) se atinge, dar plafonul Bihorului (1.100–3.400 de abonamente în 3–5 ani, ±50%) rămâne mic. Ce te duce mai departe de Bihor?
- **Dovezi:** RAP §2 („Muncitori la risc în Bihor”); RAP §7.
- **Ce m-ar face să schimb votul:** un drum spre Nord-Vest care nu cere un vânzător pe teren în fiecare județ.

### Atacul 3. Un singur client mare te ține ostatic
- **Probabilitatea de respingere: 40%**
- **Logica:** Primul client are la început 100% din venit. Dacă e o utilitate de stat și schimbă conducerea, sau organizează la anul o procedură câștigată de un integrator de flotă, pierzi tot.
- **Dovezi:** N05 §2 (decizia la directorul general); RAP §1 (Romsilva în reorganizare, ca exemplu de instituție instabilă).
- **Ce m-ar face să schimb votul:** o țintă de diversificare cu termen.

### Atacul 4. Prima alarmă reală gravă nu are plan
- **Probabilitatea de respingere: 35%**
- **Logica:** Mai devreme sau mai târziu, un lucrător echipat va muri sau va fi grav rănit, cu sau fără alarmă. În aceeași zi vor suna ITM, poliția, presa și familia. Ce face ILLUSTRUS în primele 24 de ore? Dacă jurnalul e modificat după eveniment, chiar și din greșeală, ai pierdut.
- **Dovezi:** RAP §5 (jurnalul devine probă la cercetare; anunțarea „de îndată” a ITM); RAP §2 (procese penale de 4–8 ani).
- **Ce m-ar face să schimb votul:** o procedură de incident scrisă înainte de pilot.

### Atacul 5. Firma de pază e, pe rând, client, partener și concurent
- **Probabilitatea de respingere: 25%**
- **Logica:** Planul v2 vrea firmele de pază ca prim client privat și ca dispecerat de rezervă. Ele vând la aceiași clienți. Odată ce au învățat procedura, nu mai au nevoie de tine.
- **Dovezi:** N05 §5 („pot copia serviciul”).
- **Ce m-ar face să schimb votul:** o clauză de neconcurență pe segment și o regulă despre ce date și ce proceduri rămân ale ILLUSTRUS.

### Atacul 6. Tentația LLM-ului
- **Probabilitatea de respingere: 15%**
- **Logica:** Fondatorul știe LLM-uri. Dacă un model de limbaj ajunge în lanțul de alarmă (rezumat, clasificare, „triere inteligentă”), apar AI Act (legea europeană a inteligenței artificiale) din 2 decembrie 2027 pentru sistemele cu risc ridicat din domeniul muncii, întrebarea „cine a decis că alarma e falsă” și un punct nou de eșec.
- **Dovezi:** RAP §5 (AI Act, Reg. 2026/1744; „LLM-urile stau în afara lanțului de alarmă”).
- **Ce m-ar face să schimb votul:** interdicție scrisă.

### Atacul 7. Finanțarea publică te poate încurca mai mult decât te ajută
- **Probabilitatea de respingere: 15%**
- **Logica:** Voucherul UEFISCDI (Unitatea Executivă pentru Finanțarea Învățământului Superior, a Cercetării, Dezvoltării și Inovării) e de minimis, iar cumulul cu ajutorul DR-36 primit anterior e neverificat. O aplicație costă ore de care nu dispui.
- **Dovezi:** N06 §3 și §7 (voucher, de minimis, cumul DR-36 de verificat).
- **Ce m-ar face să schimb votul:** o regulă: aplici doar dacă finanțarea plătește ceva ce oricum faci.

---

## B. Răspunsurile (planul final)

### La atacul 1 (45%) → Banii cumpără ore, după o listă
- **Fondatorul nu face:** instruirea lucrătorilor (o face responsabilul SSM al clientului, după kitul ILLUSTRUS, sau serviciul extern SSM, plătit din comision); încărcarea și distribuirea dispozitivelor (clientul); dispecerizarea (clientul).
- **Suportul cu jumătate de normă** se angajează la 150 de lucrători activi sau la 3 luni la rând peste 50 h, oricare vine primul (regula din v2, păstrată).
- **Ritmul maxim:** cel mult un client nou pe lună până la angajare.
- **Banii nefolosiți** rămân rezervă pentru gardă, asigurare și o eventuală schimbare de dispozitiv. Nu se cheltuie pe funcții noi până la 250 de lucrători.

### La atacul 2 (45%) → Drumul spre Nord-Vest prin canale, nu prin vânzători
- **Canalele:** serviciile externe SSM (comision de recomandare, N05 §5) și integratorii de flotă care vând deja Teltonika (licențiere a platformei, cu marca lor sau a ta).
- **Poarta pentru extindere:** 250 de lucrători, cel puțin 4 clienți și alarme false măsurate sub ținta reglată, în luna 24.
- **Spus cinstit:** asta e o afacere de servicii de nișă cu venit lunar recurent. Cazul de investiție apare doar dacă o rețea de canale aduce sute de lucrători pe lună.

### La atacul 3 (40%) → Diversificare cu termen
- **Ținta:** din luna 18, niciun client peste 40% din venit; cel puțin un client privat și unul public.
- **Contractele publice** se semnează pe 12 luni, cu reînnoire prin achiziție directă cât valoarea anuală rămâne sub prag (de verificat pragul exact).

### La atacul 4 (35%) → Procedura de incident, scrisă înainte de pilot
- **În prima oră:** se îngheață jurnalul (copie semnată cu amprentă digitală și oră), se anunță clientul, asigurătorul și avocatul.
- **În primele 24 de ore:** ILLUSTRUS dă clientului și ITM raportul tehnic al evenimentului, din jurnal, fără interpretări. Nicio declarație publică fără avocat.
- **După:** analiza cauzei, scrisă, și testul tuturor dispozitivelor clientului.

### La atacul 5 (25%) → Regula firmei de pază
- **Ca dispecerat de rezervă:** contract cu timp de preluare, fără drept de a vinde același serviciu clienților ILLUSTRUS pe durata contractului și 12 luni după (de validat cu avocatul).
- **Ca client:** e un client ca oricare altul, fără acces la regulile sau la platforma altor clienți.

### La atacul 6 (15%) → Interdicție scrisă
- **Nicio componentă LLM sau ML (învățare automată) în calea alarmei.** Regulile sunt fixe și documentate; în DPIA scrie „nu este sistem AI”. LLM-ul poate ajuta doar la redactarea internă a documentelor, nu la decizii despre alarme.

### La atacul 7 (15%) → Regula de finanțare
- **Se aplică doar** la voucherul UEFISCDI, cu Universitatea din Oradea, pentru validarea regulilor de cădere și nemișcare pe datele din modul umbră (ceva ce oricum faci), după ce cumulul de minimis cu DR-36 e verificat (N06 §3). STEP rămâne în afara planului (RAP §8).

---

## C. Verdictul rundei 3 (final)

- **Verdictul investitorului:** „Nu investesc, pentru că nu e o afacere pentru fond. Dar dacă aș fi tu, aș face-o așa: cu poarta 0 înainte de bani, fără rolul de dispecerat, la lucrătorul singur de la suprafață, cu mod umbră și cu regulile de oprire scrise. Pierderea maximă e de circa 4.000–6.000 EUR și câteva sute de ore. Câștigul posibil e o afacere locală recurentă și o poziție bună dacă piața românească a lucrului izolat se trezește.”
- **Ce nu poate repara nicio rundă pe hârtie:** cererea (nimeni nu a fost sunat), comportamentul real al dispozitivului în teren și existența unei asigurări. Toate trei se află în primele 8–10 săptămâni de lucru, nu în documente.
