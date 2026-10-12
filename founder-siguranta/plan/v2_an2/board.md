# Board-ul (simulat): rezumatul președintelui

**Cum a rulat.** Trei sub-agenți separați (`claude -p`, model opus, fără unelte), câte unul pe lentilă: Ofertă, Monopol, Produs (`founder-board/lenses.md`). Fiecare a primit doar `brief.md`, care conține faptele din cercetare, fără opinia mea. Prompturile sunt în `prompt_*.md`, iar memoriile neschimbate în `offers.md`, `monopoly.md`, `product.md`. Lentilele sunt rezumate ale unor cadre publicate; membrii board-ului **nu sunt** acele persoane și nu vorbesc în numele lor.

## 1. Votul

- **Ofertă: 4/10, FUND IF.**
- **Monopol: 3/10, PASS.**
- **Produs: 5/10, FUND IF.**
- **Rezultat: 2 × FUND IF, 1 × PASS; media 4,0.** Pentru comparație, Scadențarul MM din analiza anterioară a avut 3 × FUND IF, media 5,7.

## 2. Riscurile ridicate de mai mulți membri (acestea primele)

1. **Încrederea și dovada lipsesc** (toți trei):
   - nu există dovezi că dispozitivele salvează vieți;
   - rata de alarme false e necunoscută;
   - 46–59% dintre muncitori ar refuza dispozitivul;
   - TMT250 poate fi doar 2G, iar GH5200 e „End of life”.
2. **Firma de pază este cusătura critică** (Monopol și Produs):
   - momentul în care un om răspunde nu aparține fondatorului;
   - partenerul care vede toate alarmele și procedurile e cel mai probabil să copieze serviciul.
3. **Cererea nu e formată** (Ofertă și Monopol):
   - amenzile sunt mici, CAM nu are bonus-malus, nu există licitații și nici vocabular comercial;
   - nu există un „de ce acum”;
   - durerea (dosarul penal) e rară și vine târziu.
4. **Distribuția și primii 10 clienți sunt nedovediți** (Ofertă și Monopol):
   - cicluri de 6–12 luni sau SEAP;
   - pilotul gratuit nu testează cererea.

## 3. Condițiile, unite (lista de bifat pentru restul pachetului)

- [ ] **Un pilot plătit din prima zi** (taxă de setup), nu gratuit, sau o scrisoare de intenție plătită (Ofertă; Monopol, pentru a schimba votul). Oferta v2/v3 îl conține (2.500 lei); **nu e vândut**.
- [ ] **Confirmarea rețelei TMT250 (4G/LTE-M) și a disponibilității în 2026–2029**, plus un dispozitiv de rezervă (Produs, Ofertă). Bugetul e în CFO (530 EUR pentru dispozitive alternative).
- [ ] **Test end-to-end cu 50 de alarme simulate, zi, noapte și weekend, prin operatorii reali ai pazei:** 100% să ajungă, ≥95% în sub 60 s, **înainte de orice client** (Produs). Bugetul e în CFO (300 EUR).
- [ ] **SLA scris cu firma de pază,** cu timp de preluare, penalități și **neconcurență pe segment** (Produs, Monopol).
- [ ] **Bench test de purtare cu lucrători reali,** cu rata de alarme false măsurată și pre-alarma reglată (Produs, Ofertă).
- [ ] **Ofertă reală de RC** pentru garanția de preluare (Ofertă). CFO-ul o estimează la ~150 EUR/lună; **nu există ofertă**.
- [ ] **Banii riscați plafonați la ~6.600 EUR până la prima plată** (Ofertă). La structura C, CFO-ul ajunge la 8.421 EUR în luna 5, adică **puțin peste plafon**.
- [ ] **Un singur segment în V1;** satelitul și pădurea ies (Produs). Aplicat în ofertă.
- [ ] **Scanarea concurenței regionale** (distribuitori SSM, Blackline sau Peoplesafe în Ardeal), care să confirme golul (Monopol). Făcută doar din note, fără cercetare nouă (`../competitors/`); golul de ofertă e confirmat, cel de cerere nu.

## 4. Cea mai puternică versiune pe care o vede board-ul

Membrii nu sunt de acord asupra formei, și dezacordul e util:
- **Ofertă:** **„lucru izolat conform, la cheie”**, adică setup plătit (documente, sindicat, instruire) + abonament + raport lunar + garanția de preluare în 60 s. Primul client: Compania de Apă Oradea. Pădurea vine în faza 2, pentru că acolo doborârea de unul singur e oricum interzisă.
- **Produs:** **„60 de secunde până la un om, garantat și dovedit”**, pentru echipele de utilități din cămine și stații. Trei lucruri lucrate perfect: dispozitivul, operatorul, raportul. Primul client: tot Compania de Apă.
- **Monopol (PASS pe ideea propusă):** fondatorul **nu ar trebui să devină firmă de alarme**. Ar trebui să vândă **stratul de software și conformitate firmelor de pază**, sub marca lor, cu licență pe lucrător. Amenințarea nr. 1 devine astfel canal. Primul client: firma de pază din Oradea, ca licențiat plătitor.

**Sinteza mea (judecată proprie, nu a board-ului).** Cea mai puternică versiune e un **singur motor** (ecran de dispecerat + reguli + jurnal + pachet de documente) vândut prin **două uși**:
- **ușa „la cheie”** (cu dispecerul partenerului) pentru angajatorii fără dispecerat;
- **ușa „dispeceratul vostru”**, licență pentru firmele de pază și pentru fabricile cu pază internă.

Panelul simulat a mutat apoi primul client de la utilitate (0/6 la v1) la **managerul HSE al unei fabrici mari** (2/6 → 3/6); vezi `../panel/rezultate_panel.md`. Board-ul nu a văzut panelul.

## 5. Dezacordurile, păstrate

- **Ofertă și Produs** cred că ideea se poate finanța cu condiții. **Monopolul** spune PASS: fără tehnologie proprie, fără efect de rețea, cu un stack copiabil (Teltonika + Traccar + n8n) și cu partenerul ca primul copiator.
- **Primul client:** Ofertă și Produs aleg Compania de Apă Oradea. Monopolul alege firma de pază, ca licențiat.
- **Pachetul de documente:** pentru Ofertă e nucleul valorii („reduce efortul cumpărătorului”). Produsul l-ar tăia din V1 ca să nu dilueze „lucrul unic”.
