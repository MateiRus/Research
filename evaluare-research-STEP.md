# Evaluarea research-ului „Apel STEP Nord-Vest”

**Ce am evaluat:** branch-ul `claude/amazing-turing-nucje7` (commit `d97b081`), 9 octombrie 2026. Conține:
- 3 rapoarte:
  - `Apel STEP Nord Vest oportunități.md`
  - `Idee proiect STEP Nord Vest.md` (baterii: pașaport + telemetrie + a doua viață)
  - `Idee proiect STEP Nord Vest - varianta software.md` (platformă DPP cu extragere AI)
- 5 notițe de cercetare: context, reguli, piața de implementare, actori, apeluri accesibile.

**Cum am evaluat:** am citit toate rapoartele și notițele (cele lungi parțial, plus concluziile fiecărei secțiuni). Am verificat pe web 5 afirmații-cheie și am comparat totul cu ce exista deja în repo.
**Data:** 10 octombrie 2026.

---

## Verdict pe scurt

- **Ca research, e bun (7/10).**
  - E cel mai riguros din repo pe partea de reguli: prinde Corrigendum nr. 2, care mută termenul la 02.11.2026 și schimbă grila.
  - Separă ce e verificat de ce e estimat și are o listă clară cu ce trebuie recitit în documentele originale.
  - Se încheie cu decizii pentru săptămâna asta.
- **Ca plan pentru tine, e împărțit în două:**
  - **Raportul 1** („ocolește apelul și vinde implementarea”) e realist și se potrivește cu constrângerile tale (8/10).
  - **Rapoartele 2 și 3** (un proiect STEP de 5–10 mil. EUR) sunt exerciții „ce-ar fi dacă”. Presupunerile lor schimbă totul: 2–3 mil. EUR cofinanțare, partener industrial, echipă de 6–7 oameni, raport CTT, dosar în 3 săptămâni. Pentru tine, așa cum ești azi, sunt o hartă, nu un plan (3/10).
- **Partea cea mai utilă din rapoartele 2–3 e „versiunea fără grant”** (pașaportul bateriei ca serviciu). Are însă o problemă de calendar și una de cumpărător, pe care raportul nu le vede (punctul 1 de mai jos).

## Notare pe criterii (1–10)

| Criteriu | Notă | De ce |
|---|---:|---|
| Transparența surselor | 8 | Fiecare fapt are link și etichetă, iar lipsurile sunt scrise. Dar totul vine din rezumatele căutărilor: niciun ghid sau regulament nu a fost citit integral. |
| Corectitudine (cât am putut verifica) | 7 | Data de 18.02.2027 pentru pașaportul bateriei și standardele EN 18216–18223 (publicate pe 27.05.2026) se confirmă. Corrigendum nr. 2 nu l-am putut confirma independent (căutarea mea nu l-a găsit), dar e citat cu link precis. |
| Logică și coerență între rapoarte | 6 | Două contradicții nerezolvate (punctele 3 și 6). |
| Potrivire cu situația ta | R1: 8 / R2–R3: 3 | R1 respectă 10–12 h/săpt și regula „fără e-mail rece”. R2–R3 cer o altă firmă și alt capital. |
| Utilitate practică | 8 | Decizii, plan pe 4 săptămâni, criterii de continuare. |
| Noutate față de repo | 6 | Confirmă direcții vechi (pagina de proiect, monitorul de indicatori, simulatorul de punctaj). Adaugă calendarul cumpărătorului STEP, linia de cost art. 28, intermediarii (CECCAR, CTT, Goodwill) și ideea DPP. |

## Ce face bine

1. **Prinde schimbările recente ale apelului.** Corrigendum nr. 2 (termen 02.11.2026; grila de evaluare, grila de eligibilitate și macheta modificate) face transcrierea ta parțial depășită. Raportul spune asta clar și nu construiește pe cifre vechi fără avertisment.
2. **Pune întrebarea corectă.** Nu „cum aplic la STEP”, ci „ce vând în jurul lui și când apare cumpărătorul”. Calendarul (contracte în T2–T3 2027, achiziții din a doua jumătate a lui 2027, durabilitate până în 2033) e logic și marcat ca estimare.
3. **Leagă regulile de bani expuși.** Indicatorii ratați întrerup plățile, AM PR NV cere plan de recuperare la simplul risc, iar o pagină de vizibilitate lipsă aduce notificare. E același tipar „banii expuși” din sesiunile laterale, acum confirmat de documentele AM.
4. **Spune ce nu va merge.** Nu vinzi solicitanților 961 înainte de 2.11. Nu vinzi software ca activ necorporal art. 14 dintr-o microfirmă. Nu faci radarul de apeluri ca produs. Nu ești și consultant, și furnizor în același proiect.
5. **Respectă lecțiile din repo:** etichetele [VERIFICAT]/[ESTIMARE], panelurile simulate tratate ca limită superioară și nicio unealtă construită înainte de interviuri.

## Probleme importante (și cum se repară)

### 1. Pașaportul bateriei: calendarul și cumpărătorul sunt greșit legate de Casa Verde
- **Ce spune raportul:** valul de ~27.000 de baterii Casa Verde e o piață pentru pașaport, iar instalatorii AFM sunt canalul principal.
- **Ce spun regulile:** obligația de pașaport se aplică bateriilor **introduse pe piață sau puse în funcțiune din 18.02.2027** ([S-GE](https://www.s-ge.com/export/en/articles/spotlight/introduction-eu-battery-passport-february-2027); [Osapiens](https://osapiens.com/en/regulations/eu-batteries-regulation-eubr)). Bateriile introduse pe piață înainte de această dată nu au nevoie de pașaport. Obligația cade pe **operatorul care pune bateria pe piață** (producător sau importator), nu pe instalator (de verificat pe textul art. 77 și pe obligațiile operatorilor economici).
- **De ce contează:**
  - O mare parte din bateriile Casa Verde intră în țară și se instalează înainte de februarie 2027, deci nu cer pașaport.
  - Instalatorii nu au obligația, deci nu au motiv să plătească.
  - Marii producători (cei care vând majoritatea bateriilor rezidențiale) își vor face pașaportul singuri sau prin reprezentantul din UE.
  - Cumpărătorii reali rămân: importatorii direcți de mărci mici, Rombat (producător, bateriile industriale de peste 2 kWh) și operatorii de „a doua viață”.
- **Efectul:** piața versiunii fără grant e mult mai mică decât sugerează raportul, iar prețul de 15–25 EUR/baterie/an nu are nicio ancoră.
- **Reparația:** cele trei telefoane din plan se schimbă. În loc de instalatori: Rombat, 2 importatori direcți și 1 distribuitor. Prima întrebare: „Cine vă face pașaportul pentru ce importați după februarie 2027? Vi-l dă producătorul?”

### 2. Încadrarea STEP a unei platforme DPP e mai fragilă decât pare
- STEP finanțează **tehnologii critice**. O platformă de conformitate care folosește modele de limbaj existente poate fi văzută de evaluatori ca o aplicație, nu ca o tehnologie critică.
- Asta lovește criteriile 5.1/5.2, unde 0 puncte înseamnă respingere.
- Raportul folosește doar nota de ghidare C/2024/3209. Există o notă mai nouă, **C/2025/6798 (22.12.2025)**, care ține cont de lecțiile de implementare ([EUR-Lex](https://eur-lex.europa.eu/eli/C/2024/3209/oj/eng); [nota 2025](https://umwelt-online.de/recht/eu/25d/25d_c_2025_6798_leitl.htm)). Trebuie citită înainte de orice fișă de proiect.
- **Reparația:** în e-mailul către ADR NV, pe lângă întrebarea despre art. 14, întreabă dacă o platformă DPP cu componentă de cercetare (extragere verificabilă, credențiale) se încadrează la „tehnologii digitale critice”.

### 3. Contradicție despre art. 14 și calculul în cloud
- Raportul 1 spune că „software ca activ necorporal art. 14 nu merge” pentru o microfirmă.
- Raportul 3 pune **4,5 mil. EUR pe art. 14** pentru servere GPU și sală de servere, ca „infrastructură de producție”. Asta e presupunerea P3, pe care raportul o numește „cel mai mare risc”, dar construiește totuși bugetul detaliat pe ea.
- Raportul 2 respinge ideea C (nod de calcul AI) pentru că „GPU-urile sunt non-UE, argumentul de dependență se întoarce împotriva ta”. Raportul 3 folosește exact GPU-urile ca argument pentru reducerea dependenței.
- **Reparația:** nu se scrie niciun buget până nu vine răspunsul în scris de la ADR NV la P3. Contradicția trebuie rezolvată explicit: fie infrastructura e de producție și argumentul GPU e slab, fie invers.

### 4. Relația cu obligațiile tale DR-36 lipsește
- ILLUSTRUS are un plan de afaceri DR-36 monitorizat: servicii web, CAEN 6310, rural, venit minim de 10.000 EUR.
- Rapoartele 2–3 propun ILLUSTRUS sau „un vehicul nou” ca solicitant pentru un proiect de producție de milioane. Nu discută:
  - dacă asta e compatibil cu angajamentele DR-36 pe perioada de monitorizare;
  - cumulul de minimis: dacă sprijinul DR-36 (70.000 EUR sumă forfetară ([StartupCafe](https://startupcafe.ro/fonduri-ue-2025-granturi-imm-70-000-eur-afaceri-startup-neagricole-rural-ghid-finantare-leader-82280))) e acordat ca de minimis, plafonul de 300.000 EUR pe 3 ani pentru „întreprindere unică” se împarte cu componenta de minimis din STEP. Regimul DR-36 nu l-am putut confirma.
- **Reparația:** o întrebare la GAL/OJFIR, pusă împreună cu cea despre cum se numără cei 10.000 EUR: „pot fi partener sau furnizor într-un proiect STEP și ce ajutor de minimis mi-a fost înregistrat?”

### 5. Punctajul estimat (~70–82) e prea precis pentru ce se știe
- Estimarea e făcută pe o grilă pe care Corrigendum nr. 2 a modificat-o, fără criteriile 4.1, 4.2 și 4.4 (aproximativ 20 de puncte, necunoscute).
- În plus, regula de respingere la abaterea față de autoevaluare (5 puncte în transcriere, 2 puncte la apelul 121) face o supraestimare periculoasă.
- **Reparația:** păstrează doar concluzia calitativă: criteriul 3 e probabil 0, iar criteriul 2.1 depinde de echipa partenerului. Scoate totalul până nu există grila consolidată.

### 6. Produsul „recomandat acum” din raportul 1 e același cu cel din plan v4
- „Pagina de proiect conformă MIV + pachet de dovezi” e produsul B din plan v4. Riscurile cunoscute rămân:
  - ADR NV dă gratuit machete și generator de design;
  - beneficiarii aflați la mijlocul implementării pot avea deja pagina;
  - cele 800 EUR vin dintr-un panel simulat;
  - plafonul de publicitate de 15.000 lei e regula apelului 961 (proiecte mari), nu a apelurilor micro.
- Valoarea reală e pentru **obligația ta DR-36** (venit din servicii legate de site-uri), nu ca afacere în sine. Raportul o spune, dar o prezintă tot ca „singurul produs care are cerere azi”.
- **Reparația:** tratează-l ca venit de bază pentru DR-36, cu efort minim (șablon), nu ca direcție de creștere.

### 7. Probleme mai mici
- Eticheta [VERIFICAT] e pusă și pe surse ale vânzătorilor (Codibly, Scantrust, Renoon). Corect ar fi „sursă secundară”.
- „16 GAL-uri cu teritoriu în Bihor” vine dintr-o lucrare universitară. Notele mai vechi din repo listau 8 GAL-uri în Bihor. Probabil diferența vine de la GAL-urile care acoperă doar parțial județul, dar trebuie verificat.
- Lista de „câștigători probabili” (Celestica, Plexus, Zollner etc.) e construită din semnale indirecte. Raportul o marchează corect, dar o tabelă de nume poate fi citită ca listă de clienți. Nu e.

## Ce am verificat eu, independent

| Afirmație | Rezultat |
|---|---|
| Pașaportul bateriei e obligatoriu din 18.02.2027 (LMT, EV, industriale > 2 kWh, inclusiv stocare staționară) | **Confirmat**, din mai multe surse secundare; o sursă spune că data a fost reconfirmată la deschiderea registrului, pe 20.07.2026 ([S-GE](https://www.s-ge.com/export/en/articles/spotlight/introduction-eu-battery-passport-february-2027); [Battery-tech](https://battery-tech.net/why-the-eu-is-about-to-miss-its-own-battery-passport-deadline-while-industrys-stays-fixed/)) |
| Primele standarde europene DPP (EN 18216 și pachetul EN 18219–18223) publicate în 2026 | **Confirmat**: 27.05.2026, CEN-CLC/JTC 24; citarea în Jurnalul Oficial e neclară ([CDX](https://public.cdxsystem.com/en/web/cdx/w/first-european-standards-for-the-digital-product-passport-published); [Genorma](https://genorma.com/en/standards/en-18216-2026)) |
| Corrigendum nr. 2 la GS 961, termen 02.11.2026 | **Neconfirmat de mine** (căutarea nu l-a găsit). Raportul citează un URL precis de pe regionordvest.ro. De deschis pagina apelului |
| Nota de ghidare STEP folosită e cea mai recentă | **Nu**: există C/2025/6798 din 22.12.2025 |
| DR-36: 70.000 EUR sumă forfetară per plan | **Confirmat**; regimul de minimis și cumulul nu le-am putut confirma |

## Cum se leagă de restul repo-ului

- **Confirmă tiparul vechi.** Valoarea stă în faza de implementare, unde regulile pun bani în risc, nu în faza de depunere.
- **Seamănă cu concluzia din research-ul de sănătate.** Și acolo, produsul recomandat („biroul de continuitate” pentru medicina muncii) vinde un termen legal pe care nu-l urmărește nimeni.
- **DPP e singura idee nouă, cu un calendar legal real.** Ca „versiune fără grant”, e mai mică decât pare, din cauza punctului 1.
- **Pentru un om cu 10–12 h/săpt, diferența practică:**
  - Medicina muncii are cumpărători la care mergi fizic, în Oradea.
  - DPP are cumpărători în altă parte (importatori, Rombat în Bistrița) și concurenți mari care coboară spre IMM-uri.

## Ce aș face cu el

1. **Păstrează din raportul 1:** Decizia 1 (nu urmări 961 până la lista câștigătorilor) și Decizia 3 (nicio unealtă înainte de 3 interviuri).
2. **Fă testul ieftin pe DPP, corectat:** 3 telefoane la Rombat, un importator direct și un distribuitor (nu la instalatori), cu întrebarea despre cine le face pașaportul după 18.02.2027. Cere în scris de la ADR NV răspuns la P3 (art. 14 pe calcul) și la încadrarea „tehnologie critică”. Te costă cam 5 ore.
3. **Nu face buget și fișă de proiect STEP** până nu ai trei lucruri: răspunsul ADR NV, un partener industrial care pune cofinanțarea și răspunsul GAL/OJFIR despre DR-36 și de minimis.
4. **Pagina de proiect MIV rămâne venit de bază pentru DR-36,** făcută din șablon, fără să-ți ia timpul de creștere.
5. **Alege o singură direcție după primele răspunsuri:** medicina muncii (poarta din ziua 21) sau DPP (cele 3 telefoane), după care primește primul „cât costă?”.
