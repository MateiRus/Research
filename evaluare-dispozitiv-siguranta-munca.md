# Evaluarea ideii de dispozitiv de siguranță în muncă: sinteza celor trei analize

**Ce e documentul:** concluzia comună a trei analize făcute peste raportul `reports/Dispozitiv purtabil siguranță în muncă.md`:
- gândire laterală: `research_notes/Dispozitiv purtabil siguranță în muncă/analiza_laterala.md`;
- founder: `research_notes/Dispozitiv purtabil siguranță în muncă/analiza_founder.md`, cu artefactele în `founder-siguranta/` (board, competitors, panel, pricing, cfo, offer, plan);
- bulletproof (test adversarial în 3 runde): `founder-siguranta/bulletproof/`, cu `hardened_plan.md` și modelul pe 24 de luni.

**Data:** 12 octombrie 2026.

**Limita:** nicio persoană reală nu a fost întrebată. Board-ul (grupul de consilieri) și panelul de cumpărători sunt simulate de AI. Aproape toate costurile sunt estimări, iar cifrele din cercetare vin din rezumate de căutare.

## Verdict

- **Nu e primul produs.** Analiza founder dă „Not yet” (încă nu):
  - în anul 1, operațiunile pierd ~4.500 EUR;
  - doar 13% din panelul simulat cumpără, iar pragul e 25%;
  - la 10–12 ore pe săptămână, venitul lunar se oprește la ~2.400 EUR.
- **Scadențar MM rămâne primul produs** (urmărirea termenelor la medicina muncii).
- **Ideea de alarmă merită, dar îngustă și abia în anul 2**, vândută prin portalul pentru angajatori și prin cabinetele de medicina muncii, pe care le ai deja ca rețea.
- **Ce vinzi de fapt** (concluzia comună a celor trei analize): **dovada că firma a făcut tot ce trebuia** pentru lucrul izolat (HG 1091/2006, hotărârea despre locul de muncă) și **minute mai puține până la ajutor**. Nu vinzi brățara și nu promiți „salvăm vieți”.

## Unde se potrivesc și unde nu se potrivesc cele trei analize

**Se potrivesc:**
- **Nu fi tu dispecerul (cel care răspunde la alarme non-stop)**, din trei motive:
  - răspunderea juridică, pentru că limitarea răspunderii probabil nu ține la vătămări corporale (de verificat cu un avocat);
  - lipsa ta de timp;
  - punctul unic de eșec.
- **Argumentul asigurării nu merge**, pentru că CAM (contribuția de asigurare pentru muncă) e fixă.
- **Pentru patron contează riscul penal**, nu amenzile.
- **Pulsul, gazele, satelitul și pădurea rămân pe dinafară** la început.
- **Nu cheltui bani înainte de un semnal real de plată.**

**Nu se potrivesc, iar asta e o alegere de făcut:**
- **Primul client:**
  - cercetarea propune utilitățile (apă, salubritate);
  - founder propune managerul HSE (sănătate, securitate, mediu) al unei fabrici din Oradea, singurul tip de client care a „cumpărat” în panel;
  - bulletproof arată că utilitățile de stat cer achiziție publică, deci pilotul gratuit nu merge la ele.
  - **Concluzia:** fabrica privată e prima, iar utilitatea vine a doua, prin achiziție directă plătită.
- **Cine răspunde la alarmă:**
  - founder propune o firmă de pază parteneră;
  - bulletproof spune că o firmă de pază nu are motiv să țină un om pe ecranul tău pentru ~75 EUR pe lună;
  - **Concluzia:** alarma merge întâi la dispeceratul sau paznicul pe care clientul îl are deja, apoi la șeful de tură, iar firma de pază rămâne rezervă plătită.
  - Dispozitivul trimite și SMS direct, ca o pană a serverului să nu piardă alarma.

## Produsul, în forma întărită

- **Numele de lucru:** „Lucru izolat conform, la cheie”.
- **Ce face:**
  - cădere și lipsă de mișcare;
  - buton SOS;
  - locația trimisă doar la alarmă;
  - jurnal cu ora exactă, ca dovadă pentru ITM (Inspectoratul Teritorial de Muncă);
  - documentele SSM (securitate și sănătate în muncă) și GDPR (protecția datelor) gata făcute pentru client.
- **Varianta fără dispozitiv**, din analiza laterală: un „plan de lucru izolat”, ca planul de zbor.
  - Muncitorul anunță prin SMS unde intră și cât stă.
  - Dacă nu confirmă ieșirea, sistemul îl sună, apoi sună colegul, apoi dispecerul.
  - Se testează ieftin, cu n8n (unealta de automatizări).
- **Prețul:**
  - 12 EUR pe muncitor pe lună, cu dispozitivul cumpărat de client (~650 lei);
  - sau 16–20 EUR pe lună, cu dispozitivul inclus;
  - sau ~6 EUR pe lună, dacă alarmele merg la dispeceratul clientului;
  - pilotul costă ~2.500 lei.
- **Canalele de vânzare:**
  - firmele externe de SSM, cu comision;
  - cabinetele de medicina muncii, prin Scadențar MM;
  - white-label (produsul sub marca lor) pentru firmele de pază.

## Cifrele (estimări)

- **Ce rămâne pe un muncitor:** la 12 EUR pe lună, ~6,8 EUR.
- **Rezultatul lunar:**
  - −186 EUR la 50 de muncitori;
  - +383 EUR la 200;
  - +3.660 EUR la 1.000.
- **Numerarul necesar:**
  - ~8.400 EUR dacă dispozitivele le cumpără clientul;
  - ~25.400 EUR dacă le incluzi, adică tot capitalul.
- **Modelul bulletproof:**
  - ~290 de muncitori și ~4.200 EUR pe lună în luna 24 (scenariul pesimist: 92 de muncitori);
  - pierderea dacă pilotul eșuează: ~4.350 EUR;
  - în 9 din 24 de luni ai nevoie de mai mult de 10–12 ore pe săptămână.
- **Analiza founder:**
  - 1.000 EUR venit lunar recurent abia în luna 15;
  - 3.000 EUR doar dacă lucrezi ~20 de ore pe săptămână, în luna 24.

## Ce faci, în ordine

1. **Acum:** continui cu Scadențar MM ca prim produs.
2. **În paralel, ieftin (Poarta 0, lunile 1–2, maximum 1.000 EUR):**
   - ceri oferte scrise de dispecerat de la 3 firme de pază, cu SLA (timp de răspuns garantat);
   - arăți o machetă APEX a modulului „lucru izolat” la 5 firme SSM din Oradea și la 2–3 manageri HSE din fabrici;
   - ceri o ofertă de asigurare RC (răspundere civilă) pentru serviciul de alarmă;
   - ceri un aviz de la un avocat pe răspundere și pe Legea 190/2018 (monitorizarea angajaților).
3. **Mergi mai departe doar dacă:**
   - ai confirmări scrise de la 2 organizații;
   - ai o ofertă de asigurare;
   - avizul juridic e favorabil.
4. **Pilotul plătit**, după poartă:
   - 3 dispozitive de probă înainte de orice comandă;
   - 14 zile în „mod umbră” (alarmele se înregistrează, dar nu ajung la dispecer), ca să reglezi alarmele false;
   - o fabrică privată, cu muncitori singuri la suprafață, în zonă cu semnal.
5. **Te oprești dacă:**
   - nicio organizație nu confirmă în scris;
   - asigurarea nu se poate obține;
   - în pilot, alarmele de test ajung sub 95% sau purtarea scade sub 60%.
   - Detaliile sunt în `analiza_founder.md` §8 și în `hardened_plan.md`.
6. **Plasa de siguranță:** firmele SSM și fabricile pe care le-ai cunoscut devin clienți de servicii web. Asta te ajută la DR-36.
