# Runda 3: review-ul investitorului pentru planul v2

**Investitorul:** același partener de fond european de digital health (vezi `01_round_1_review.md`).
**Ce evaluează:** planul v2 din `04_round_2_plan.md`, ca ultimă rundă. Întrebarea se schimbă: nu mai e „e un plan coerent?”, ci „e un plan pe care l-aș urmări 7 ani și în care aș intra la un moment dat? Ce l-ar putea omorî oricum?”.

---

## Verdictul pe scurt

**Coerent. Nu investesc acum, dar aș urmări.** v2 a mutat valoarea și datele în locul potrivit: munca echipei MM în jurul examenului obligatoriu. Guvernanța pe trei niveluri, „dispeceratul echipei mobile” și modulul de prevenție „la examen, nu după” sunt mișcări bune și sprijinite de note. Ce lipsește acum e ce lipsește oricărei afaceri bootstrapped care vrea să devină companie de prevenție:
- o poziție clară despre finanțare (unde intră bani din afară, dacă intră);
- un responsabil medical;
- un design de măsurare a rezultatelor;
- reguli pentru momentele în care fondatorul trebuie să aleagă.

**Ce nu mai contest:**
- activul de date pe niveluri, cu bază legală pentru fiecare;
- etapa 3a (prognoză de capacitate pe sediu), legal curată;
- etapa 2 construită pe contactul care are loc oricum (ȘTI KQ1, ACCESS);
- argumentul de bani care nu depinde de angajator (un client păstrat ≈ 5 ani de abonament; calculul fondatorului);
- validarea care încape în ~150 h, cu trei porți;
- G înghețat în scris.

---

## Obiecțiile

### 1. Ca investiție de risc, cazul nu există încă; ca afacere, planul nu spune când ar exista
- **Probabilitatea de respingere dacă rămâne nerezolvată: 60%** (pentru bani de fond acum)
- **Logica:** Chiar dacă toate porțile ies, v2 ajunge la ~3k € MRR în luna 34. Asta e o afacere mică, bună pentru fondator, dar nu un caz de fond. Nu e o critică: e o clarificare pe care planul trebuie să o facă singur. Un fond intră doar dacă există o piață mai mare decât cabinetele independente din România. Notele nu arată cumpărători români activi de module healthtech, deci nici ieșirea prin vânzare nu e documentată.
- **Dovezi:**
  - v2 cu modulul: 3.185 € MRR în luna 36 (`model_36m.py`);
  - stratul de scadențe: cel mult ~0,4 mil. €/an la prețurile de azi (calculul din runda 1);
  - ecosistemul românesc trăiește din granturi, nu din VC: 356 de startup-uri healthtech, 45 finanțate, 15 Series A+; „experimenter” la EIT Health (RO §6);
  - „no evidence of active Romanian acquirers of healthtech modules” (CEE Q3, Inferences);
  - tiparul care a mers în CEE: un flux zilnic al furnizorului → încorporare → module adiacente pentru același cumpărător → abia apoi extindere geografică sau funcții reglementate (CEE Q3, Inferences).
- **Ce m-ar face să schimb votul:** o politică de finanțare scrisă (fără bani de fond până la dovezile etapei 2) și pragurile la care un caz de fond ar exista: de exemplu, modulul de prevenție vândut în ≥2 țări sau la ≥1 rețea medie.

### 2. Nu există un responsabil medical
- **Probabilitatea de respingere dacă rămâne nerezolvată: 50%**
- **Logica:** Din etapa 2, produsul poartă conținut definit de medici: clasele de termen ale recomandărilor, meniul testelor din ziua de prevenție, regulile de marcare a constatărilor. Un fondator tehnic fără un medic MM în guvernanță nu e credibil nici pentru cabinete, nici pentru un auditor, nici pentru mine. „Consilier la ~150 €/lună” e o linie de cost, nu un rol.
- **Dovezi:** „Acces inițial limitat la medici” (AF §0); intenția declarată și materialele de vânzare decid calificarea MDR (REG §2, Art. 2(12)); clinicile vor cere asigurare și responsabilitate (REG §6, §7); lentila Produs: „granița clinică e fragilă” (`board/product.md`, la G).
- **Ce m-ar face să schimb votul:** un medic de medicina muncii numit, cu rol scris (aprobă conținutul clinic, semnează notele de calificare, participă la designul măsurătorilor), plătit sau cu o mică participație.

### 3. Fondatorul va trebui să aleagă, iar planul nu spune după ce regulă
- **Probabilitatea de respingere dacă rămâne nerezolvată: 50%**
- **Logica:** În lunile 18–36, v2 pune în paralel: vânzarea a ~1,5 clienți/lună, modulul de prevenție (cu partener de laborator), dispeceratul echipei mobile, arhiva de expunere și coordonarea ajutorului part-time. La 10–12 h/săpt, asta nu încape. Fie fondatorul urcă la ~20 h/săpt, fie alege o singură direcție. Planul nu spune cum alege.
- **Dovezi:** scenariul „spre 3k” cere ~20 h/săpt (AF §D2, §E5.5); capacitatea ~52 h/lună (`cfo/cfo-sources.md`); MVP-ul singur a cerut 120–160 h (AF §B).
- **Ce m-ar face să schimb votul:** o regulă de alegere în luna 18, bazată pe metrici (de exemplu: prevenția înainte de dispecerat doar dacă ≥3 angajatori au cerut-o în scris), și o decizie scrisă despre orele fondatorului.

### 4. Nu există un design de măsurare a rezultatelor
- **Probabilitatea de respingere dacă rămâne nerezolvată: 45%**
- **Logica:** Când angajatorul plătește pentru prevenție, va întreba „ce am primit?”. Dovezile pe care se sprijină planul sunt din SUA sau din programe organizate (FUR §2), iar transferul spre România e nedovedit. Fără un grup de comparație de la început, „prevenție” rămâne un cuvânt de marketing, iar etapa 3b nu va avea niciodată dovada că bate „reminder pentru toți”. Mai mult, tablourile de risc fără acțiune pot crește consumul de servicii fără beneficiu.
- **Dovezi:** efectele sunt mai ales din SUA și din programe organizate; transferul spre clinicile românești e nedovedit (FUR §2, Inferences); țintirea nu s-a dovedit mai bună decât reminderul pentru toți (FUR §3); PRISMATIC: stratificarea riscului a crescut internările (ȘTI KQ1); nu există date românești despre urmare (FUR §1, Gaps).
- **Ce m-ar face să schimb votul:** auditul inițial ca bază la fiecare client, introducerea treptată cu grup de comparație (de exemplu, angajatori care încep în luni diferite) și un partener academic care publică rezultatele.

### 5. Etapele 3b–4 depind de calendare pe care nimeni din România nu le controlează
- **Probabilitatea de respingere dacă rămâne nerezolvată: 40%**
- **Logica:** Organismul de acces la date (HDAB) din România nu e verificat, reforma MDR poate întârzia până în 2028, iar obligațiile EHDS pentru rezultatele de laborator vin abia în 2031. Ambiția „predictivă” pe termen lung nu poate depinde de evenimente externe fără date.
- **Dovezi:** pregătirea României pentru EHDS (HDAB, autoritatea de sănătate digitală) nu a fost verificată (REG §4, Gaps); reforma MDR: vot SANT pe 3.12.2026, adoptare posibilă abia în 2027–2028 (REG §2; FUR §5); EHDS grupa 1 din 26.03.2029, grupa 2 (laborator) din 26.03.2031 (FUR §5); AI Act Anexa I din 2.08.2028 (REG §3).
- **Ce m-ar face să schimb votul:** un plan pe 3–7 ani care are valoare și în scenariul „nimic nu vine la timp”, plus momentele exacte în care se cheltuie bani pe conformitate (QMS, documentație AI Act).

### 6. Prețul stratului de bază va fi erodat
- **Probabilitatea de respingere dacă rămâne nerezolvată: 35%**
- **Logica:** Reminderele și portalurile devin, în timp, funcții incluse gratuit în programele MM, la fel cum reminderele SMS sunt deja incluse în programele de clinică. În luna 36, ~80% din venitul din v2 vine tot din stratul de bază.
- **Dovezi:** SMS-ul simplu e „commodity, evidence-backed functionality”, inclus în orice program (FUR §3, Inferences); MediNote include SMS la 50 lei/utilizator/lună (RO §2); ponderea modulului în MRR-ul din luna 36: ~620 € din 3.185 € (calculul meu din `model_36m.py`).
- **Ce m-ar face să schimb votul:** o țintă de mix de venit (de exemplu, modulele ≥40% din MRR în luna 48) și o regulă de preț pentru stratul de bază când apare un concurent gratuit.

### 7. O singură breșă de securitate omoară un furnizor mic
- **Probabilitatea de respingere dacă rămâne nerezolvată: 30%**
- **Logica:** Produsul ține date despre aptitudinea a zeci de mii de angajați, de la mai multe cabinete. Un incident face din „SRL necunoscut” un „SRL cu scurgere de date”. Cabinetele mai mari (sau clienții lor) vor cere dovezi conform NIS2.
- **Dovezi:** atacul ransomware Backmydata (februarie 2024) asupra RSC/Hipocrate a afectat 26 de spitale (RO §2); amenzi ANSPDCP în sectorul medical (RO §3); entitățile NIS2 cer securitate în lanțul de furnizori (REG §5); trust e principalul motiv de refuz în panelul v2 (`panels/A2/results.md`).
- **Ce m-ar face să schimb votul:** un plan de securitate cu trepte (aliniere la controale ISO 27001/NIS2, test de penetrare la un prag de clienți, plan de răspuns la incident, backup testat).

### 8. Argumentul „frica de ITM” și regulile MM nu sunt verificate pentru 2026
- **Probabilitatea de respingere dacă rămâne nerezolvată: 30%**
- **Logica:** Suma amenzii din art. 39 e din texte din 2006–2010. Frecvența controalelor ITM în Bihor e necunoscută. Periodicitatea exactă din Anexa 1 nu a fost citită. Dacă amenda e mai mică, controalele sunt rare sau periodicitatea se lungește, argumentul angajatorului slăbește și numărul de evenimente pe angajat scade.
- **Dovezi:** „Re-check the consolidated law for 2026” (RSMM §3); nicio statistică ITM Bihor (RSMM §3, Gaps); periodicitatea din Anexa 1 necitită (RSMM §3, Gaps); notele avertizează să nu se confunde cu proiectele din Republica Moldova, care trec la 24/36 de luni (RSMM §3); AF §E5.6.
- **Ce m-ar face să schimb votul:** verificarea legislației consolidate în primele 3 săptămâni și un argument de vânzare care nu stă pe amendă (cel din v2: timp și clienți păstrați).

---

## Tabelul obiecțiilor

| # | Obiecția | Probabilitate de respingere |
|---:|---|---:|
| 1 | Cazul de investiție nu există încă; nu e clar când ar exista | 60% |
| 2 | Niciun responsabil medical | 50% |
| 3 | Regula de alegere a fondatorului în luna 18 lipsește | 50% |
| 4 | Niciun design de măsurare a rezultatelor | 45% |
| 5 | Etapele 3b–4 depind de calendare externe | 40% |
| 6 | Prețul stratului de bază va fi erodat | 35% |
| 7 | O breșă de securitate omoară un furnizor mic | 30% |
| 8 | Amenda, controalele ITM și periodicitatea neverificate pentru 2026 | 30% |

**Ce aș vrea să văd în planul final:** orizonturile 0–6 luni, 6–18 luni, 18–36 de luni și 3–7 ani, fiecare cu ce se construiește, ce se validează, ce se licențiază sau se obține prin parteneriat și când se oprește; politica de finanțare; un medic responsabil; designul de măsurare; criteriile go / no-go într-un singur loc.
