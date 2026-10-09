# Prețul pentru primele trei idei (A, G, B)

**Sursele prețului:** (1) răspunsurile la cele patru întrebări de preț din panelurile **simulate** (`van_westendorp.py`; tabelele `*-curve.md` din acest folder; unealta afișează „$”, dar toate răspunsurile sunt în **EUR pe lună, fără TVA**); (2) prețurile concurenților din `../competitors.md`; (3) marjele din unealta CFO (`../cfo/`). Răspunsurile simulate aleg ce să testezi. Nu dovedesc ce se va plăti.

## A · Scadențar MM + portal angajator (prin cabinete)

**1. Ce au spus cumpărătorii** (20 simulați; v1 = primul pitch, v2 = oferta refăcută):

| Panel | PMC | OPP | IPP | PME | Interval acceptabil |
|---|---:|---:|---:|---:|---|
| v1 (59/99 €) | 24 € | 25 € | 59 € | 120 € | 24–120 € |
| v2 (35/69/129 €) | 15 € | 30 € | 40 € | 99 € | 15–99 € |

Mediana pragului „începe să fie scump”, pe segment (v1/v2): **cabinet mic 60/40 €, firmă medie 120/95 €, furnizor regional 250/250 €.** Cei care cumpără au în v1 o mediană de 130 € la „scump” și 250 € la „prea scump”.

**2. Ce cer concurenții:** niciun preț publicat pentru software de medicina muncii. Ancore apropiate: MediNote ~10 €/utilizator/lună; BizMedica pentru medicina de familie ~31–39 €/lună (preț vechi) (RO §2).

**3. Ce cere afacerea** (`unit_economics.py --price`, rampa de bază din anul 1):

| Preț mediu | Contribuție/client | Prag de rentabilitate (clienți) | Profit operațional anul 1 |
|---:|---:|---:|---:|
| 39 € | 35 € | 7 | −870 € |
| 49 € | 45 € | 6 | −330 € |
| **65 €** | **61 €** | **4** | **+534 €** |
| 79 € | 75 € | 4 | +1.290 € |
| 99 € | 95 € | 3 | +2.370 € |

**4. Decizia:**
- **Prețul: o scară pe trei trepte, cu o medie țintă de ~65 €/client-lună.** Media e calculul meu, la un mix estimat de 50% cabinete mici, 40% firme medii, 10% furnizori regionali.
  - **Mic: 39 €/lună** (până la 1.500 de angajați urmăriți). Stă sub pragul „scump” al cabinetelor mici (40–60 €).
  - **Standard: 79 €/lună** (până la 6.000). Firmele medii sunt segmentul care a cumpărat cel mai mult (50% în v1), iar pragul lor „scump” e 95–120 €.
  - **Regional: 149 €/lună** (nelimitat, mai multe locații). Pragul lor „scump” e 250 €.
  - SMS-urile se refacturează la cost, separat.
- **De ce nu 25–30 € (OPP):** OPP e prețul cu cea mai mică rezistență, dar la 39 € sau mai puțin primul an e pe pierdere (tabelul de mai sus), iar la plafonul de timp al fondatorului (~25 de clienți) MRR-ul maxim ar fi sub 1.000 €.
- **Oferta de lansare:** „pilot fondator” pentru primele 5 cabinete:
  - preț blocat 24 de luni;
  - configurarea inițială făcută de fondator la sediu;
  - garanție de 90 de zile cu returnarea banilor.
  - **Fără reduceri procentuale**, ca să nu-i înveți pe cumpărători să aștepte promoții. Raritatea e reală: la 10–12 h/săpt fondatorul poate integra ~1 client pe lună.
- **Ce se testează cu cumpărători reali:**
  - Standard la **69 € față de 89 €** (pre-vânzare la firmele medii);
  - Mic la **35 € față de 49 €**;
  - întrebarea „ați refactura portalul angajatorilor?”.
- **Obiecțiile de preț, citate din panel (simulat):**
  1. „Costul de 59–99 € pe lună îl iau din marjă, iar clientul nu-mi dă un leu în plus pentru portal sau remindere.” (A/P015)
  2. „Încă un abonament lunar pe care îl plătesc eu, iar clienții nu vor plăti în plus pentru el.” (A/P001)
  3. „Cu 3.000–10.000 de angajați aș ajunge pe treapta de 69 sau 129 € pe lună, bani scoși din marja mea.” (A2/P007)
  - **Răspunsul de marketing:** argumentul nu e „portal”. E „asistenta nu mai sună angajatorii” plus „nu mai pierzi clientul la renegociere”. Testul A/B simulat sugerează că economia de timp (reminderele) convinge mai mult decât portalul.

## G · Controale pierdute (clinici de boli cronice)

**1. Ce au spus cumpărătorii:**

| Panel | PMC | OPP | IPP | PME | Interval |
|---|---:|---:|---:|---:|---|
| v1 (129 €) | 30 € | 30 € | 69 € | 130 € | 30–130 € |
| v2 (69 €) | 15 € | 15 € | 40 € | 120 € | 15–120 € |

Pragul „scump” pe segment (v1/v2): **clinici cronice 150/120 €**, laboratoare 110/80 €, medici de familie 70/59 €.

**2. Ce cer concurenții:** de la ~10 € (reminder inclus în MediNote) la 139–299 € (Callio) și 299–499 € (agenți vocali; EMG Q3).

**3. Ce cere afacerea:**

| Preț | Contribuție | Prag de rentabilitate (clienți) | Profit operațional anul 1 |
|---:|---:|---:|---:|
| 49 € | 44,5 € | 6 | −1.870 € |
| 69 € | 64,5 € | 4 | −1.470 € |
| **89 €** | **84,5 €** | **3** | **−1.070 €** |
| 119 € | 114,5 € | 2 | −470 € |

Anul 1 e pe pierdere la orice preț. Motivul e rampa lentă: audit, integrare per clinică, prima plată abia în luna 5.

**4. Decizia:**
- **Prețul: 89 €/lună pe locație, doar pentru clinicile de boli cronice**, după un audit gratuit.
- **Nu se vinde medicilor de familie** (0 cumpărători din 7 în ambele paneluri; „sunt plătită pe listă, nu pe consultație”, G/P017) și **nici laboratoarelor** în v1.
- **Garanția** „în lunile din primele 3 cu mai puțin de 15 controale programate din listă, nu plătiți” costă cel mult 3 × 89 € pe client. Se acordă doar dacă auditul arată cel puțin 30 de controale depășite.
- **Ce se testează:** 69 € față de 99 €, la primele 4–6 clinici auditate.
- **Obiecțiile de preț (simulate):**
  1. „Plătesc 129 € pe lună, adică aproape 1.550 € pe an, și nu am nicio garanție că vin pacienți în plus.” (G/P014)
  2. „Nu sunt convinsă că ar aduce suficiente consultații în plus cât să acopere 129 € pe lună.” (G/P016)
  3. „69 € pe lună plus TVA pentru o listă pe care asistenta o poate scoate și din programul actual.” (G2/P016)

## B · Scadențar MM direct la HR

**1. Ce au spus cumpărătorii:** PMC 10 €, OPP 10 €, IPP 25 €, PME 60 €. Intervalul acceptabil e 10–60 €. Pragul „scump” median e 37–57 €, după mărimea angajatorului.

**2. Ce cer concurenții:** 0 € (Excel, furnizorul MM).

**3. Ce cere afacerea:** la ~25 € (IPP), 1.000 € MRR cere ~40 de angajatori, fiecare cu vânzare separată. La 10–12 h/săpt e nefezabil ca produs separat (calculul meu; CFO nu a rulat pentru B, care nu e în primele 2).

**4. Decizia:** **niciun preț separat pentru B ca produs.** Partea de angajator intră în A, prin portalul cabinetului. Singura excepție testabilă: un nivel de autoservire la **19 €/lună** pentru angajatorii „speriați de ITM” (singurul segment care a cumpărat, 2 din 3). Rolul lui e de **sursă de clienți pentru cabinete**, nu de linie de venit.
- **Obiecțiile de preț (simulate):**
  1. „Ar trebui să primesc scadențarul de la furnizorul de medicina muncii, în prețul pe care îl plătesc deja.” (B/P017)
  2. „39 € pe lună mi se pare mult pentru un tabel cu date.” (B/P007)
  3. „39 € pe lună plus SMS-uri pentru ceva ce fac gratis nu mi se pare justificat.” (B/P020)
