# Runda 2: review-ul investitorului pentru planul v1

**Investitorul:** același partener de fond european de digital health (vezi `01_round_1_review.md`).
**Ce evaluează:** planul v1 din `02_round_1_plan.md`. Probabilitatea de respingere e dată pentru fiecare obiecție nouă sau rămasă, dacă rămâne nerezolvată.

---

## Verdictul pe scurt

**Mai aproape, dar încă nu.** v1 a reparat ce era ușor de reparat: dovezile vin înainte de cod, vendorii se verifică primii, modelul are churn, datele sunt minime, iar drumul are porți. Asta mută planul de la „poveste” la „experiment bine construit”. Dar un experiment bine construit nu e încă o companie. Rămân trei probleme de fond:
1. activul de date pe care se sprijină tot drumul spre predictiv **nu e al fondatorului**;
2. avantajul competitiv e în continuare „suntem mai rapizi”;
3. modelul se oprește la ~1,6k € MRR, iar planul nu spune cum trece mai departe.

**Ce s-a îmbunătățit și nu mai contest:**
- validarea măsoară cerere reală (pre-vânzări, audit pe exportul real, pilot concierge);
- verificarea vendorilor în 2 săptămâni, cu arbore de decizie;
- modelul cu churn, retururi și buget de ore;
- modelul de date fără CNP și fără diagnostice; registrul recomandărilor vizibil doar cabinetului până la opinia juridică;
- regulile pentru datele învechite (statusuri cu grație, banner de prospețime);
- scopul declarat și cuvintele interzise.

---

## Obiecțiile

### 1. Activul de date nu e al tău, iar etapele 3–4 depind de el
- **Probabilitatea de respingere dacă rămâne nerezolvată: 65%**
- **Logica:** Tot drumul spre predictiv stă pe „istoricul buclelor”. Dar:
  - ca persoană împuternicită, istoricul e al fiecărui cabinet. Orice analiză peste mai mulți clienți, făcută în scopul tău, te face operator (REG §1, Art. 28(10));
  - o clauză în DPA care îți permite „statistici anonimizate” e contestabilă: anonimizarea trebuie să treacă testul din Recital 26, iar pseudonimizarea nu ajunge (REG §1);
  - **consimțământul angajatului** nu e o soluție simplă: într-o relație de muncă, consimțământul dat prin angajator riscă să nu fie considerat liber (principiu GDPR general, **BK, de verificat cu avocatul**; notele nu acoperă acest punct);
  - datele MM sunt subțiri (categorie, dată, termen). Un cabinet cu 3.000 de angajați produce ~3.000 de examene pe an și o fracțiune de recomandări. Un model pe un singur cabinet are puține evenimente (calculul meu, ordin de mărime);
  - profilarea cu date de sănătate cere consimțământ explicit sau o bază legală expresă (Legea 190/2018 art. 3; REG §1). Simplul fapt că un angajat are o recomandare deschisă e o dată de sănătate indirectă (REG §1, Inferences).
- **Dovezi:** REG §1 (Takeaway, Inferences: rutele (a)–(e) pentru antrenarea unui model); REG §4 (permisele HDAB abia din ~2029, dacă România are organism funcțional); LAT O25 („baza legală e dificilă”).
- **Ce m-ar face să schimb votul:** o guvernanță a datelor pe niveluri, cu baza legală pentru fiecare, și o etapă 3 care are valoare chiar dacă avocatul spune „nu” la profilare.

### 2. Avantajul competitiv e tot „suntem mai rapizi”
- **Probabilitatea de respingere dacă rămâne nerezolvată: 60%**
- **Logica:** „Adaptoare pentru mai mulți vendori” și „istoric care devine cost de schimbare” sunt reale, dar slabe. Un vendor are deja datele în propriul program și nu are nevoie de adaptor. Istoricul de 12 luni al unui cabinet se poate exporta (chiar promiți asta). Și nu ai pârghie în negocierea cu vendorii: cu 5–10 cabinete, nu ești un partener interesant pentru Setrio. Un OEM la cel mai slab vendor înseamnă un canal mic. Ce se întâmplă cu clienții tăi în luna în care BizMedica lansează un portal gratuit?
- **Dovezi:** BizMedica importă deja Excel și are COR, posturi, definiții de loc de muncă (RSMM §1); lentila Monopol: „What do you build that stays yours if BizMedica adds a portal?” (`board/monopoly.md`); „Apărarea fondatorului e viteza de onboarding, relația locală și un parteneriat cu un vendor, nu tehnologia” (`plan/A/business-plan.md`, §Concurența).
- **Ce m-ar face să schimb votul:** un plan explicit pentru ziua în care un vendor lansează portalul, plus valoare care nu stă în portal și nici în import.

### 3. Plafonul de ~1,6k € MRR nu are o ieșire
- **Probabilitatea de respingere dacă rămâne nerezolvată: 55%**
- **Logica:** v1 spune cinstit că 3.000 € MRR nu vine la 10–12 h/săpt. Dar ținta fondatorului e 1.000–3.000 € MRR înainte de echipă, iar orice investitor vrea să vadă motorul care trece de plafon. Cele trei variante (mai mult timp, un canal, un al doilea modul) au fiecare un cost care nu e în plan: ore, comision, dezvoltare.
- **Dovezi:** plafonul de ~25 de clienți (AF §D2); scenariul „spre 3k” cere ~20 h/săpt din luna 13 și ajunge la 50 de cabinete, ~10% din cele 508 (AF §D2); canalul de +50% volum e o ipoteză (AF §D3); v1 la ~1,6k € în luna 36 (`model_36m.py`).
- **Ce m-ar face să schimb votul:** un al doilea motor cu cifre, cu momentul în care pornește și cu poarta care îl declanșează.

### 4. Cabinetul plătește tot din marjă; kitul de refacturare contrazice dovezile
- **Probabilitatea de respingere dacă rămâne nerezolvată: 55%**
- **Logica:** Kitul de refacturare presupune că angajatorul acceptă +2–4 lei/angajat/an. Toate semnalele pe care le ai spun contrariul: cabinetele sunt negociate la 80 de lei, iar HR-ul simulat a respins scadențarul în proporție de 18/20 și a spus că „ar trebui inclus în prețul MM”. Dacă refacturarea nu merge, abonamentul rămâne un cost pe care cabinetul îl taie „la prima revizuire de costuri”.
- **Dovezi:** „mă negociază la 80 de lei” (`panels/A`, P004, P005; `panels/A2`, P004); panelul B: 2/20, „ar trebui să primesc scadențarul de la furnizorul MM, în prețul pe care îl plătesc deja” (`plan/A/business-plan.md`, §Pricing B); „tai abonamentele care nu aduc bani imediat” (`panels/A2`, P001, P015).
- **Ce m-ar face să schimb votul:** un argument de bani care nu depinde de angajator: costul unei ore de asistentă sau valoarea unui client păstrat, comparate cu abonamentul.

### 5. Etapa 2 presupune că urmarea o face cineva pe care nu-l controlezi
- **Probabilitatea de respingere dacă rămâne nerezolvată: 50%**
- **Logica:** „Scrisoare către medicul de familie + remindere + dovadă” mută bucla în afara cabinetului MM: angajatul trebuie să meargă la medicul de familie, iar acesta trebuie să răspundă. Medicul MM are rol de aptitudine, nu de tratament. Angajatul nu e clientul tău și, statistic, nu e digital. Dovezile spun că bucla se închide cel mai bine **în locul unde omul e deja prezent**, nu prin urmărire după.
- **Dovezi:**
  - „the OH doctor does not own the referral loop”; treatment follow-up belongs to family doctors (RSMM §3, Inferences, Against);
  - prevenția publică trece prin medicul de familie și pachetul CNAS (RO §5, Inferences);
  - ACCESS: 22% finalizare cu trimitere vs 100% cu testul în aceeași vizită; 22% vs 64% follow-through după rezultate anormale (ȘTI KQ1);
  - e-mailul a făcut ~11% dintre medici să acționeze, telefonul peste două treimi (FUR §2);
  - 31,8% competențe digitale de bază; ~10% programări online (RO §8).
- **Ce m-ar face să schimb votul:** o etapă 2 proiectată în jurul contactului care are loc oricum (examenul periodic), cu un om care acționează.

### 6. Consolidarea îți mănâncă clienții
- **Probabilitatea de respingere dacă rămâne nerezolvată: 45%**
- **Logica:** Clienții tăi cei mai buni („sub presiunea rețelelor”) sunt exact cei care fie pierd angajatori, fie sunt cumpărați. Când o rețea cumpără un cabinet, IT-ul se decide central, iar contractul tău se termină. Churn-ul de 1,5%/lună din model nu include acest eveniment.
- **Dovezi:** Medicris cumpărat de MedLife (2022), Pelican 80% Medicover (2018), Regina Maria vândută către Mehiläinen (2025) (RSMM §5; RO §1, §7); „Network-owned sites decide IT centrally” (RO §7).
- **Ce m-ar face să schimb votul:** diversificare geografică, contracte anuale și un plan pentru momentul în care un client e cumpărat.

### 7. Validarea de 90 de zile nu încape în 10–12 h/săpt
- **Probabilitatea de respingere dacă rămâne nerezolvată: 40%**
- **Logica (calculul meu):**
  - 15 conversații × 3–4 h (cu drumul) = 45–60 h;
  - ~8 audituri pe exporturi × ~2 h = ~16 h;
  - pilot concierge la 2–3 cabinete × ~4 h/săpt × 5 săpt = 40–60 h;
  - prototip APEX + n8n = 20–30 h;
  - vendori și juridic = ~10 h.
  - **Total: ~130–175 h**, față de ~150 h disponibile în 13 săptămâni. Nu rămâne rezervă pentru drumuri în Cluj sau Satu Mare și nici pentru construcția MVP-ului după.
- **Dovezi:** capacitatea de ~52 h/lună (`cfo/cfo-sources.md`); MVP 120–160 h (AF §B #1); 15 conversații, ≥8 în afara Oradei (AF §E6).
- **Ce m-ar face să schimb votul:** o validare secvențiată, care taie ce nu e necesar pentru decizia din ziua 90.

### 8. Răspunderea contractuală și asigurarea sunt estimate, nu cotate
- **Probabilitatea de respingere dacă rămâne nerezolvată: 30%**
- **Logica:** PLD acoperă moarte, vătămare, bunuri și date neprofesionale, nu pierderile economice (REG §7). O amendă ITM pentru un examen ratat e o pierdere economică a angajatorului, deci riscul tău e contractual, față de cabinet și, prin el, față de angajator. La etapa 2, o constatare anormală neurmată poate deveni vătămare. Asigurarea de 600 €/an e o estimare fără ofertă.
- **Dovezi:** REG §7 (daunele acoperite; răspunderea față de persoana vătămată nu se exclude prin contract); `cfo/cfo-sources.md` („Nicio ofertă reală”); Legea 95/2006 Titlul XV leagă răspunderea furnizorului medical de asigurarea subcontractorilor (REG §6, PBU).
- **Ce m-ar face să schimb votul:** o ofertă de asigurare reală și un contract-tip cu plafon și responsabilități clare.

### 9. Focusul: G stă în așteptare, dar concurează pentru aceleași ore
- **Probabilitatea de respingere dacă rămâne nerezolvată: 25%**
- **Logica:** Board-ul preferă G, iar planul o ține „a doua ușă”. Fără o regulă clară, fondatorul va fi tentat să facă un audit G „doar pentru că a cerut o clinică”, din aceleași 10–12 ore.
- **Dovezi:** board: G media 6,0 față de A 5,7 (`board/board.md`); AF §E6 (zilele 61–90 includ „un singur audit G, dacă o clinică acceptă”).
- **Ce m-ar face să schimb votul:** G înghețat până la porți, scris.

---

## Tabelul obiecțiilor

| # | Obiecția | Probabilitate de respingere |
|---:|---|---:|
| 1 | Activul de date nu e al fondatorului; etapele 3–4 depind de el | 65% |
| 2 | Avantajul competitiv e „suntem mai rapizi” | 60% |
| 3 | Plafonul ~1,6k € MRR fără ieșire | 55% |
| 4 | Cabinetul plătește din marjă; refacturarea contrazice dovezile | 55% |
| 5 | Etapa 2 depinde de medicul de familie și de angajat | 50% |
| 6 | Consolidarea mănâncă clienții | 45% |
| 7 | Validarea nu încape în 10–12 h/săpt | 40% |
| 8 | Răspunderea contractuală și asigurarea necotate | 30% |
| 9 | Focusul: G concurează pentru aceleași ore | 25% |

**Ce cer înainte de runda 3:** o guvernanță a datelor cu bază legală pe niveluri, o etapă 2 construită pe examenul care are loc oricum, un al doilea motor de venit cu cifre și un plan pentru ziua în care un vendor copiază portalul.
