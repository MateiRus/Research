# Evaluare cu „The Founder skill” (jakeschincariol/founder-skill)

**Data:** 7 octombrie 2026. **Ce am rulat:** founder-board (3 sub-agenți, câte o lentilă), founder-consumer în varianta rapidă (20 de cumpărători simulați, seed 7), founder-pricing (Van Westendorp pe răspunsuri), founder-offer (oferta refăcută + re-test pe aceiași 20), founder-cfo (unit_economics.py), founder-plan (compile.py → verdict). Nu am rulat marketing, brand, ops, launch (nu erau necesare pentru evaluare). Toate fișierele sunt în `founder/`. Total: 43 de sub-agenți.

**Ce e și ce nu e asta:** lentilele board-ului sunt rezumate ale unor cadre publicate (Offers, Monopoly, Product), nu opiniile autorilor lor. Cumpărătorii sunt agenți simulați: buni la a scoate obiecții și segmente, slabi la a prezice conversia; modelele de limbaj înclină spre amabilitate, deci rata de cumpărare e o **limită superioară**. Cifrele CFO vin din inputurile mele (`founder/numbers.json`, surse în `founder/cfo-sources.md`), în EUR fără TVA (tool-ul afișează „$”).

---

## 1. Verdictul compilat: **Not yet**

| Verificare | Rezultat |
|---|---|
| Fiecare unitate câștigă bani înainte de costurile fixe | ✓ contribuție 3.588 EUR pe contract PRO (88%) |
| Anul 1 are profit operațional | ✓ ~9.500 EUR pe 3 contracte (12.228 EUR venit) |
| Pragul de rentabilitate încape în capacitate | ✓ 0,03 contracte/lună (tool-ul afișează „1 pe zi” din rotunjire) |
| Destui cumpărători simulați cumpără (bara: 25%) | ✗ **0 din 20** pe oferta din plan v3 (PRO 2.400 + 140); **2 din 20 (10%)** pe oferta refăcută |

Economia e bună pe hârtie pentru că nu include timpul tău; cererea e problema.

## 2. Board-ul: 3 × FUND IF, scor mediu 4,3 / 10

| Lentilă | Scor | Ce ar omorî afacerea (primul motiv) | Condiția principală |
|---|---|---|---|
| Offers | 5 | Produsul principal (site 1.200 EUR) e o marfă peste plafonul local, fără nicio dovadă | 10 interviuri înainte de construcție; automatizarea de documente în față, site-ul bonus; garanție pe rezultat |
| Monopoly | 4 | Site + n8n nu e de 10 ori mai bun; radarul concurează cu gratuitul | Pană: doar Bihor 12 luni; radarul vândut devreme ca singur activ (dezacord cu ceilalți doi) |
| Product | 4 | Pre-check-ul AI de eligibilitate e cel mai riscant moment și e nemăsurat; trei produse, o persoană | Un singur produs 12 luni; pre-check măsurat pe 50 de cereri reale înainte de vânzare |

Toate trei: fără interviuri, fără client, fără set de test. Sinteza completă: `founder/board.md`.

## 3. Panelul: ce au spus 20 de „consultanți”

**Oferta v1 (PRO: site + 2 automatizări, 2.400 + 140/lună, 12 luni): 0 din 20.** Motive: încredere 10, preț 7, nevoie 3. Citate: „nu pun dosarele a 50 de clienți pe un contract de 12 luni cu un om care face asta după job” (firmă de 736k); „4.080 EUR în primul an e aproape o zecime din venitul meu, pentru un site care funcționează” (firmă de 43k); „singurul lucru care mă doare e colectarea documentelor și nu-l pot cumpăra fără site”.

**Oferta v2 („Dosar Complet”: doar colectarea documentelor, 900 + 50/lună, lunar, pe conturile clientului, persoană de rezervă, garanție 60 de zile): 2 din 20 (10%).** Motive: încredere 14, nevoie 5, preț 1. Cumpără doar firmele mari (2 din 3 cu 50+ clienți); 0 din 17 la firmele mici și mijlocii. Citate: „problema e reală și 900 e nimic față de ce facturăm, dar nu există un consultant în România pe care să-l pot suna azi”; „am 10–12 clienți pe an și le urmăresc eu pe WhatsApp în câteva ore pe lună”; „documentul pentru care am condus 60 km nu exista încă; un link nu rezolvă asta”.

**Ce ar întoarce un „nu”** (aproape unanim): un apel telefonic cu clientul-pilot din Bihor după 60 de zile, cu cifre înainte/după; persoana de rezervă cunoscută înainte de semnare; pentru firmele mici, preț de 400–500 EUR.

**Ce înseamnă pentru tine:**
1. **Site-ul nu e produsul.** Nimeni nu l-a vrut. Vinde-l doar celui care îl cere.
2. **Clientul e firma cu 20+ clienți activi.** Firmele cu 5–15 clienți/an fac asta de mână și nu plătesc 900 EUR. Lista ta de 50 de prospecți trebuie filtrată după numărul de clienți, nu după județ.
3. **Încrederea nu se cumpără cu clauze.** Garanția, continuitatea, lunar-fără-angajament au mutat rata de la 0% la 10%; restul vine doar dintr-un pilot real terminat și o referință apelabilă. Asta pune **pilotul la consultantul tău înaintea oricărei vânzări**, și îți interzice să menționezi „part-time” fără să spui în aceeași frază numele persoanei de rezervă.
4. **Pre-check-ul AI nu e argument de vânzare**; e risc. Vinde-l ca „semnalare de date lipsă”, după test pe cererile reale ale clientului.

## 4. Prețul

| | ofertă v1 (setup PRO) | ofertă v2 (setup Documente) |
|---|---:|---:|
| Interval acceptabil (PMC–PME) | ~790 – ~2.400 EUR | ~300 – ~1.500 EUR |
| Punct de indiferență (IPP) | ~1.500 | ~500 |
| Prețul tău | 2.400 (pe margine) | 900 (în interval, peste IPP) |

Recomandare (`founder/pricing.md`): preț pe volum — 500 EUR + 30/lună (≤ 15 clienți finali), 900 + 50 (≤ 50), 1.500 + 90 (peste 50); primii 2 la −20% până la 31 ianuarie 2027; de testat 900 vs 1.200 pe oferte reale, nu pe panel.

## 5. CFO

Contribuție 88% pe contract; costuri fixe 105 EUR/lună; startup 300 EUR; numerar necesar 615 EUR; recuperare în luna 4. Linia de urmărit: nu prețul (−10% ⇒ marja 80%) și nu costurile (+15% ⇒ 80%), ci **rampa**: 3 contracte în anul 1 dau 12.228 EUR, zero contracte dau −1.560 EUR. Timpul tău nu e în model: la ~430 h pe 13 luni, marja e ~20 EUR/h (plan v3). Un contabil trebuie să verifice structura și taxele înainte să mute bani.

## 6. Ce schimbă asta în plan v3

| Plan v3 spunea | Evaluarea spune |
|---|---|
| START + PRO, site în față | **„Dosar Complet” singur**, site add-on la cerere |
| 2.400 + 140/lună, 12 luni | 900 + 50/lună (sau pe volum), **lunar**, pe conturile clientului |
| Pilot −20% pentru primii 2 | Rămâne, dar **după** pilotul real la consultantul tău, nu în loc de el |
| Pre-check de eligibilitate ca automatizare 1 | Add-on, doar semnalare, doar după test pe cereri reale |
| Lista de 50: CAEN + județ | + filtru **20+ clienți activi** (firmele mici nu cumpără) |
| Scenariul „5 × PRO” = 11.040 EUR | Cu „Dosar Complet” la 900: **11 contracte** pentru 10.000 EUR doar din instalări; cu abonamente 50/lună, ~8–9 contracte în 15–18 luni. Obiectivul de 10.000 EUR devine **mai greu** cu produsul pe care îl vor, decât cu cel pe care nu-l vor. Soluția: vinde Documente ca intrare și **site-ul ca upsell** după 60 de zile de încredere, nu invers. |

Calcul rapid [ESTIMARE]: 6 × Documente (900) + 3 × site upsell (1.200) = 9.000 + abonamente (6 × 50 + 3 × 60 = 480/lună la final) → 10.000 EUR în ~luna 14–16, cu 6–9 clienți. Dacă clienții mari acceptă 1.500, mai repede.

## 7. Un singur lucru săptămâna asta

Semnezi pilotul „Dosar Complet” cu consultantul tău: 60 de zile, măsurătoarea „înainte” (zile de la cerere la dosar complet pe ultimele 10 dosare) luată acum, dreptul lui de a fi sunat de următorii clienți scris în contract, numele persoanei de rezervă scris lângă al tău.

## Fișiere

`founder/idea.md`, `founder/board/` (brief + 3 memorii), `founder/board.md`, `founder/customer.json`, `founder/pitch-v1.md` (oferta v1), `founder/pitch.md` (oferta v2), `founder/panel-v1/` (0/20), `founder/panel/` (2/20), `founder/pricing-curve-v1.md`, `founder/pricing-curve.md`, `founder/pricing.md`, `founder/offer.md`, `founder/numbers.json`, `founder/cfo.md`, `founder/cfo-sources.md`, `founder/summary.md`, `founder/business-plan.md`, `founder/one-pager.md`.
