# Verificarea planului PREVENT-NV v2 și a evaluării lui

**Ce am verificat:** commit-ul `22055d0` de pe branch-ul `claude/amazing-turing-nucje7` (12.10.2026). Conține trei documente:
- `evaluare-plan-PREVENT-NV.md`
- `proiect-STEP-PREVENT-NV-plan-v2.md`
- `proiect-STEP-PREVENT-NV-conformitate-ghid.md`

**Cu ce am comparat:** transcrierea celor 36 de slide-uri ale ghidului (`Transcriere_Regio_Nord_Vest_Primele_36_slideuri.docx`).
**Data:** 12 octombrie 2026.

## Verdict

**v2 e mult mai bun decât v1** și evaluarea e în mare parte corectă:
- un singur produs clinic;
- fără hardware propriu;
- plătitor numit (angajatorul, prin medicina muncii), cum recomandase research-ul din repo;
- director de proiect din domeniu;
- porți cu criterii de oprire;
- flux de numerar cu TVA;
- matrice de conformitate pe fiecare cerință din ghid.

**Mai are 6 probleme de corectat înainte să fie folosit pentru dosar.** Două dintre ele ar putea respinge proiectul.

## Problemele

### 1. Unitățile mobile s-ar putea să nu fie „producție STEP” (risc mare)
- **Ce spune transcrierea (slide-urile 4–6):**
  - art. 14 finanțează „capacitatea fizică de producție necesară punerii în producție a tehnologiilor critice STEP”;
  - pe P9, rezultatul trebuie să fie chiar tehnologia critică;
  - pe P1, doar ce e „necesar producției de tehnologii critice din cadrul aceluiași proiect”.
- **Ce face v2:** numește tehnologia critică „infrastructură suverană de date de sănătate, învățare federată, extragere RO/HU”. Apoi pune grosul investiției (1,6–1,8 mil. EUR) pe vehicule cu ECG și spirometru pentru zile de prevenție.
- **Problema:** vehiculele sunt capacitate de prestare a unui serviciu medical, nu de producție a tehnologiei digitale. Ironic, centrul de date, pe care v2 l-a micșorat ca „umflat”, se potrivea mai bine definiției.
- **Ce faci:** întrebarea 2 către ADR NV trebuie pusă exact pe acest punct, cu lista activelor. Dacă răspunsul e „nu”, investiția trebuie mutată pe infrastructura de date și calcul, dimensionată pe cerere reală.

### 2. Minimul de 3 mil. EUR pe art. 14 e tot ratat (aceeași greșeală ca în v1)
- Transcrierea (slide 1) confirmă: ajutorul regional pe proiect are **minim 3.000.000 EUR**.
- v2 scrie 4.600.000 × 65% ≈ „3.000.000”. Calculul exact e **2.990.000 EUR**, sub prag.
- **Inconsistență:** secțiunea 4 a planului însumează activele la 3,6–4,1 mil. EUR, dar tabelul de buget pune 4,6 mil. EUR.
- **Ce faci:** ai nevoie de ~4,62 mil. EUR la 65% sau de ~4,29 mil. EUR la 70%, plus marjă de 5–10% pentru cheltuieli tăiate la evaluare. Intensitatea reală se ia din cap. 3.4 al ghidului.

### 3. Art. 28 nu e 100% pe tot (aceeași greșeală ca în v1)
- Transcrierea (machetă, slide 15) dă două procente diferite:
  - „Art. 28 – Inovare IMM” (brevete, active necorporale, detașare): **50%**;
  - „Consultanță pentru inovare”: **100%**.
- v2 pune la 100% și „protecție marcă/IP”. Aceea e la 50%.
- **Ce faci:** imparți linia. Consultanța (MDR, organismul notificat, studiul de piață) merge la 100%, IP-ul la 50%. Verifică și dacă raportul CTT poate fi decontat: e făcut înainte de depunere, iar condiția EG7 nu permite investiții demarate înainte.

### 4. TVA-ul e calculat la 19%; cota standard în România e 21% din 1.08.2025
- În notele din repo apare deja creșterea TVA la HoReCa de la 1 august 2025. Cota standard a urcat atunci la 21%, de verificat pe produsele medicale, care pot avea cotă redusă.
- **Efectul:** pe ~8 mil. EUR eligibili, TVA-ul de finanțat temporar crește cu ~160.000 EUR.

### 5. ESO4 și ESO2 se pot rezolva pentru o fereastră din 2027
- Ambele documente tratează salariatul mediu (ESO4) și profitul din exploatare (ESO2) ca „ipoteze asumate”.
- **Nuanța practică:** ESO4 se verifică pe anul fiscal anterior depunerii.
  - La o depunere în 2026, anul verificat e 2025, deci nu se mai repară.
  - La o depunere în 2027, anul verificat e 2026. Dacă ILLUSTRUS are în medie ≥1 salariat în 2026 și profit din exploatare în 2025 sau 2026, condițiile sunt îndeplinite.
- **Ce faci:** dacă ținta e o fereastră din 2027, decizia de angajare și profitul din 2026 trebuie luate acum, nu după.

### 6. Calendarul nu lasă timp pentru plata finală
- EG11: implementare **și plăți** până la 31.12.2029.
- 30 de luni de la un contract din T2–T3 2027 se termină în T4 2029–T1 2030, iar cererea finală de rambursare are nevoie de 2–3 luni pentru verificare.
- **Ce faci:** implementarea trebuie să fie de cel mult 24–26 de luni, cu terminare în jur de septembrie 2029. Asta înseamnă scop mai mic sau certificarea pe planul B din start.

## Lucruri corecte pe care le confirm din transcriere

| Afirmația din v2 | Ce spune transcrierea |
|---|---|
| Grant 5–10 mil. EUR; art. 25 max. 7 mil.; art. 28 max. 220 k; minimis max. 300 k; publicitate max. 15.000 lei | slide-urile 1 și 9 |
| Peste 4 ENI pentru 6 puncte la un grant de 5–7 mil. EUR | slide 23 |
| Directorul de proiect trebuie să aibă 5 ani experiență „în domeniul proiectului” | slide 28 (2.1.a), deci mutarea directorului pe omul de reglementare e corectă |
| Criteriul de buget: activitatea de bază trebuie să fie ≥50% din bugetul eligibil | slide 33. 4,6 din 8,17 mil. = 56% dacă activitatea de bază e producția (definiția e de verificat în ghid) |
| Cercetarea la 80% / 60% e pe varianta cu diseminare (coloana „Difuzare: DA”) | slide 15. v2 are publicare (benchmark, protocol, profil FHIR), deci condiția poate fi îndeplinită; trebuie scris explicit în cerere |
| Depunerea integrală în apelul 1, bugetul complet în Macheta STEP | slide 15 |

## Ce lipsește în continuare

- Grila consolidată după Corrigendum 2 (criteriile 4.1, 4.2, 4.4 și pragul de toleranță).
- Intensitatea regională exactă (cap. 3.4 din ghid).
- Definiția „activității de bază”.

## Recomandare

Folosește **v2 ca bază**, cu cele 6 corecturi. Primul pas rămâne e-mailul către ADR NV. Formulează întrebarea 2 pe fiecare activ (unități mobile, centru de coordonare, mediul de date, licențe) și cere confirmarea că se încadrează la P9 sau P1. De răspunsul acesta depinde dacă proiectul mai are sens în STEP.
