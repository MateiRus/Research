# Runda 0: planul original „Scadențar MM” (concept A), așa cum a ieșit din analiza founder

**Data:** 9 octombrie 2026
**Ce e acest fișier:** arhiva planului de la care pornește procesul „bulletproof”. Nu conține nimic nou. E o comprimare fidelă a ce scrie în:
- `research_notes/Oportunități software în sănătatea predictivă/analiza_founder.md` (§„Pe scurt”, §B #1, §C, §D, §E2, §E3, §E6);
- `founder-sanatate/plan/A/` (`idea.md`, `summary.md`, `one-pager.md`, `offer.md`, `business-plan.md`, `pricing.md`);
- `founder-sanatate/board/`, `founder-sanatate/panels/A`, `A2`, `founder-sanatate/cfo/`.

**Abrevieri pentru citări** (toate în `research_notes/Oportunități software în sănătatea predictivă/`):

| Abreviere | Fișier |
|---|---|
| RSMM | `romania_software_medicina_muncii.md` |
| RO | `romania_piata.md` |
| REG | `reglementare_ue_ro.md` |
| FUR | `follow_up_recall_dovezi.md` |
| LAT | `analiza_laterala.md` |
| AF | `analiza_founder.md` |
| EMG | `emergente_si_platitori.md` |
| ȘTI | `stiinta_predictie_preventie.md` |
| CEE | `cee_nordice.md` |

Artefactele din `founder-sanatate/` sunt citate cu calea lor (de ex. `board/monopoly.md`, `panels/A2/results.md`, `cfo/A_36m.md`).

**Cum s-a rulat procesul (abateri de la skill, spuse o dată):**
- Skill-ul cere ca obiecțiile investitorului să fie susținute cu date căutate pe web. **Sarcina interzice cercetarea web nouă**, așa că fiecare obiecție citează notele de cercetare existente. Ce e calcul sau judecată proprie e marcat „calculul meu” sau „estimare”. Ce vine din cunoștințe generale, nu din note, e marcat „BK, de verificat”.
- Skill-ul întreabă câte runde. Utilizatorul a fixat **maximum 3 runde**. Skill-ul nu are altă regulă de oprire, așa că s-au rulat toate 3.
- Numele fișierelor urmează exemplul lucrat din skill (`00_original_plan.md`, `rounds/01_round_1_review.md` … `rounds/06_final_plan.md`, `summary.md`).

---

## 1. Fondatorul și constrângerile (rămân adevărate în orice versiune)

- Fondator tehnic solo, SRL în Bihor (Oradea), rețele în Oradea și București.
- Python, SQL, PL/SQL, Oracle APEX, n8n, API-uri LLM.
- ~25.000 € capital; 10–12 h/săptămână la început.
- B2B, venit recurent.
- Fără acces la date clinice la început.
- Produsul rămâne **administrativ** (în afara MDR) la început.
- Ambiția pe termen lung: un drum credibil spre sănătate preventivă/predictivă (programe de prevenție plătite de angajatori, urmarea constatărilor anormale, date din era EHDS).

## 2. Produsul

**Ce este** (`plan/A/idea.md`): un add-on pentru **cabinetele și firmele independente de medicina muncii (MM)**, care:
- ține scadențele fișelor de aptitudine pentru toți angajații fiecărui angajator-client, alimentat din exportul programului MM existent sau din Excel;
- trimite remindere către HR-ul clienților (e-mail) și SMS către angajat (doar cu consimțământ), ca asistenta să nu mai sune;
- dă fiecărui angajator un **portal cu marca cabinetului**: în termen / expiră / depășit, plus recomandările „apt condiționat” deschise sau închise, **fără diagnostice și fără CNP**;
- trimite un raport lunar pe angajator, folosit la renegocierea anuală.

**MVP** (AF §B #1): import Excel; calendarul la 30/60/90 de zile și regula examenului de reluare (după 90 de zile de absență medicală sau 6 luni din alt motiv, în 7 zile; RSMM §3); remindere e-mail/SMS; portal de status; raport lunar PDF; lista recomandărilor cu termen pus de medic și încărcarea dovezii; jurnal de audit. Estimare: 120–160 h, adică ~3–4 luni la 10–12 h/săpt.

**Arhitectura** (AF §B, nucleul comun): Oracle APEX + PL/SQL pe o instanță în UE, multi-tenant, jurnal de audit pe fiecare acțiune; n8n pentru importuri, trimiteri și rapoarte; Python pentru citirea fișierelor; API-uri LLM (regiune UE, fără retenție) doar pentru maparea coloanelor, niciodată pentru interpretare clinică. Fondatorul e persoană împuternicită (Art. 28 GDPR), cabinetul e operator pe baza Art. 9(2)(h) (REG §1).

**Cine e clientul:** cabinete independente cu 1–5 medici, 1.000–10.000 de angajați urmăriți, mai ales cele care fac examene la sediul angajatorilor și au pierdut clienți în fața rețelelor. Primele vizate: Medimun, Carimed, Endodigest (Oradea), apoi Nord-Vest (RSMM §5).

## 3. Prețul și oferta

- **39 / 79 / 149 €/lună** (până la 1.500 / 6.000 / nelimitat angajați urmăriți), SMS la cost, fără TVA (`pricing/pricing.md`).
- Media țintă ~65 €/client-lună, la un mix estimat de 50% cabinete mici, 40% firme medii, 10% furnizori regionali (calculul din `cfo/cfo-sources.md`).
- Ofertă de lansare: „pilot fondator” pentru primele 5 cabinete, preț blocat 24 de luni, configurare la sediu, **garanție de 90 de zile** cu returnarea banilor (`plan/A/offer.md`).
- Mesajul principal (v3, netestat): „Asistenta dumneavoastră nu mai sună angajatorii: fiecare client își vede singur scadențele, cu marca cabinetului, și primește remindere la timp.”

## 4. De ce A (dovezile invocate)

- Examen periodic obligatoriu pentru toți lucrătorii, de regulă anual, plătit de angajator; amenzi de 4.000–8.000 lei pe abatere (Legea 319/2006 art. 39(4); suma de reverificat pentru 2026) (RSMM §3).
- MedLife vinde deja angajatorilor un portal self-service cu statusul MM în timp real (RSMM §1) și a cumpărat cel mai mare furnizor MM din Bihor, Medicris, 22.000+ abonați (RSMM §5).
- Scorare: locul 1 din 29 (73,4/100), robust la 4 seturi de ponderi (AF §A).
- Board simulat: singura idee pusă de toate trei lentilele în primele două (3 × FUND IF, media 5,7) (`board/board.md`).
- Panel simulat: 7/20 cumpără la pitch-ul v1 (35%, limită superioară); 3/20 (15%) la pitch-ul v2 (`panels/A`, `panels/A2`).
- Categoria 1, administrativ: „logistica medicinei muncii” (REG §8).

## 5. Numerele (estimări, `cfo/`)

| Indicator | Valoare |
|---|---:|
| Contribuție / client-lună | 61 € (94%) |
| Costuri fixe | 230 €/lună |
| Prag de rentabilitate | 4 clienți |
| Pornire în numerar | 2.980 € |
| Numerar necesar până se autofinanțează | 3.825 € |
| Profit operațional anul 1 | +534 € |
| MRR luna 12 / 24 / 36 | 650 / 1.430 / 1.625 € |
| 1.000 € MRR | ~luna 18 |
| 3.000 € MRR | niciodată la 10–12 h/săpt (plafon ~25 de clienți ≈ 1.625 €); luna 31 doar cu ~20 h/săpt din anul 2 |
| Verdict `compile.py` | „Profitable”, dar fragil: se răstoarnă la −20% volum, la SMS absorbit sau cu panelul v2 |

Rampa: +1 client/lună din luna 4, după 3 pre-vânzări (`cfo/A_numbers.json`). Modelul **nu are churn** (`cfo/A_36m.md`).

## 6. Validarea de 90 de zile (AF §E6)

- **Zilele 1–30:** 15 conversații calificate cu cabinete MM (Oradea, apoi Cluj, Satu Mare, Arad) + 5 angajatori; verificarea programului MM folosit și dacă are portal pentru angajator; întrebări directe la Setrio și DMV Consult; partea juridică (amenda 2026, „ce vede angajatorul”, consimțământul SMS, DPA).
- **Zilele 31–60:** machetă APEX pe date sintetice, oferta „pilot fondator”, scrisori de intenție plus o plată.
- **Zilele 61–90:** MVP minim la 1–3 piloți pe exporturi reale.
- **GO:** ≥3 pre-vânzări plătite până în ziua 60 **și** ≥2 exporturi funcționale **și** golul confirmat (0–1 programe MM cu portal).
- **NO-GO:** <2 pre-vânzări după ≥15 conversații **sau** ≥2 programe MM au deja portalul.

## 7. Drumul spre preventiv/predictiv (AF §E2, marcat acolo „inferență, nu plan”)

1. **Anul 1, A:** fiecare examen și fiecare recomandare „apt condiționat” e o buclă cu termen; se adună istoricul buclelor (LAT §F1.3).
2. **Anii 1–2, același cumpărător:** D, arhiva de expunere (audiograme, spirometrii afișate fidel); C, ziua de prevenție la locul de muncă, cu un laborator partener (ȘTI KQ1 ← ACCESS: 22% → 100%).
3. **Anul 2:** G, controalele pierdute la clinicile cronice, după referințe de la A.
4. **Anii 2–3:** predicție operațională „cine nu-și va închide bucla” (O25), cu grup de control și consimțământ explicit (Legea 190/2018 art. 3); fără scoruri clinice individuale.
5. **2028–2031:** stratul de buclă găzduiește modele de risc ale unor vendori cu marcaj CE; componente EHDS; folosirea secundară prin EHDS după ~2029 (REG §4).

## 8. Locul 2: G „Controale pierdute” (AF §E3)

O listă săptămânală de pacienți cu control stabilit de medic și neprogramat, la clinicile independente de boli cronice; 89 €/locație după un audit gratuit. Panel simulat: 0/20 la v1, 2/20 la v2; anul 1 pe pierdere (−1.070 €). Se deschide doar după: ≥2 clienți A plătitori, 2 audituri cu ≥30 de controale depășite fiecare, o opinie MDR scrisă, ≥1 clinică plătitoare la ≥69 €.

## 9. Riscurile pe care planul le recunoaște singur

- Cabinetele consideră că programul MM sau Excel-ul „face deja asta”.
- Un vendor MM (Setrio, DMV Consult) adaugă portalul.
- Plafonul local e mic (~6 cabinete independente identificate în Oradea; RSMM §5).
- Timpul fondatorului, nu capitalul, e constrângerea.
- Board-ul și panelul sunt **simulate**; niciun om real n-a fost întrebat; prețurile și rampele sunt estimări; faptele vin mai ales din rezumate de căutare.
