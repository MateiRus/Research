# Planul original (runda 0): alarmă pentru lucrătorul izolat, ILLUSTRUS S.R.L.

**Ce e documentul:** planul de testat, extras pe scurt din raportul de cercetare, secțiunile 1, 6, 7 și 8. Nu adaugă nimic nou. Rundele de atac sunt în `rounds/`, planul întărit în `hardened_plan.md`.

**Data:** 12 octombrie 2026. Fără cercetare web nouă.

**Prescurtări pentru surse (folosite în toate fișierele):**
- **RAP §n** = `reports/Dispozitiv purtabil siguranță în muncă.md`, secțiunea n.
- **N00 … N06** = notele din `research_notes/Dispozitiv purtabil siguranță în muncă/`: N00 prompt și context, N01 problemă și statistici, N02 cadru legal, N03 piață și concurenți, N04 hardware și conectivitate, N05 clienți, preț, canale, riscuri, N06 finanțare.
- **[fapt]** = scris în sursă; **[estimare]** = calcul sau judecată (a cercetării sau a evaluatorului); **[de verificat]** = sursă slabă, lipsă sau din memorie.

---

## Fondatorul și constrângerile

- ILLUSTRUS S.R.L., Oradea, CAEN 6310 (prelucrarea datelor, găzduire, portaluri web) (N00).
- Fondatorul: student în anul 2 la ASE (Academia de Studii Economice), junior Oracle APEX și PL/SQL (limbajul de programare al bazei de date Oracle); Python, SQL, n8n (instrument de automatizări), LLM-uri (modele mari de limbaj).
- 10–12 ore pe săptămână, circa 25.000 EUR, 0–1 angajați. Nu construiește hardware (N00).

## Ideea, pe scurt (RAP §1)

- **Produsul:** un serviciu de alarmă pentru lucrătorul izolat: detectarea căderii și a nemișcării („om la pământ”), buton SOS, locația trimisă odată cu alarma și un dispecerat care trimite ajutor. Se vinde „mai puține minute până la ajutor”, nu „salvăm vieți”.
- **Ce iese din prima versiune:** pulsul (risc de dispozitiv medical după MDR, regulamentul UE 2017/745), stresul termic măsurat pe corp (devine un indice din meteo), gazele (doar cu detectoarele clientului), apropierea de utilaje (faza 2).
- **Baza cererii:** HG 1091/2006 (hotărâre de guvern) definește lucrul izolat; Legea 319/2006 (legea SSM, securitate și sănătate în muncă) cere evaluarea riscurilor și primul ajutor [fapt, RAP §1].
- **Prima industrie:** utilitățile locale din Bihor: Compania de Apă Oradea (496 de angajați), RER Vest (circa 720), Termoficare Oradea [fapt, RAP §1]. Apoi firme private de exploatare forestieră, apoi marii antreprenori din construcții.

## Pilotul pe 90 de zile (RAP §6)

- 1 client din utilități, 30 de lucrători (echipe de noapte, cămine, stații de pompare), circa 60 de zile de funcționare reală.
- **Tehnic:** trackere Teltonika (TMT250 la 88,50 EUR sau GH5200 la 176,53 EUR) → SIM-uri IoT (pentru obiecte conectate) → Traccar (server open-source care citește protocolul Teltonika) → webhook (mesaj automat către o adresă web) → n8n cu reguli fixe (pre-alarmă 20–30 s, escaladare la 60 s) → ecran de dispecerat în Oracle APEX. SMS direct din Traccar ca a doua cale; test zilnic automat.
- **Dispeceratul:** operatorii unei firme de pază din Oradea lucrează în ecranul APEX pe durata turelor clientului.
- **Construcția:** 80–160 de ore, adică 7–16 săptămâni la 10–12 h pe săptămână; începe cu 8 săptămâni înainte de ziua 1.
- **Bani:** circa 3.600–6.600 EUR fără gaze și satelit; avocatul și asigurarea, necunoscute.
- **Cine plătește:** clientul cumpără cele 30 de dispozitive, fără abonament 90 de zile; contractul prevede trecerea la 12 EUR pe lucrător pe lună dacă pilotul atinge țintele. ILLUSTRUS plătește platforma și dispeceratul.
- **Ținte:** purtare ≥ 85% din ture; 100% din alarmele de test ajung, ≥ 95% în sub 60 s; alarme false < 2 la 100 de ture-om; ≥ 70% dintre lucrători „aș continua”; oprire dacă testele ajung sub 95% sau purtarea sub 60%.

## Prețul și profitul (RAP §7)

- Listă: 20 EUR pe lucrător pe lună, cu dispozitiv inclus, contract 24–36 de luni. Pentru pilot și primii clienți: 12 EUR, dispozitivul cumpărat de client.
- Costuri variabile presupuse: dispozitiv amortizat 2,50 + pierderi 0,75 + SIM 1,50 + dispecerat externalizat 2,50 EUR, comision de canal 15%, diverse 3% [estimare].
- Prag de rentabilitate: 160–380 de lucrători la 20 EUR, 290–700 la 15 EUR; la 12 EUR cu dispozitivul cumpărat de client, aproape zero la 200 de lucrători [estimare].
- Dispecerat propriu 24/7 abia peste circa 2.400 de lucrători [estimare].

## Finanțarea (RAP §8)

- Produsul nu e tehnologie STEP (programul UE pentru tehnologii strategice) de unul singur; ILLUSTRUS nu poate aplica direct (grant minim 5 mil. EUR, profit și salariat cerute) [fapt].
- Ca modul în PREVENT-NV: centrul de coordonare lucrează în orar de birou, alarmele cer acoperire pe ture [estimare].
- De urmărit: voucherul de inovare UEFISCDI (până la 50.000 lei), EDIH (centre de inovare digitală), furnizor art. 28 pentru câștigătorii STEP din 2027 [fapt].
- **Pilotul îl plătesc primul client și fondatorul.**

## Ce recunoaște deja planul ca slăbiciuni (RAP §1)

- Amenzile sunt mici, CAM (contribuția asiguratorie pentru muncă) e fixă, nu există dovezi independente că dispozitivele salvează vieți.
- 46–59% dintre muncitorii din construcții spun că nu le-ar purta [fapt, studiu văzut prin rezumat].
- Alarmele false nu au rate publicate; furnizorii numesc temporizatorul de nemișcare „un instrument brut”.
- Firma e mică, alarma cere răspuns non-stop: dispeceratul externalizat e „obligatoriu”.
