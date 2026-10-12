# Planul: 90 de zile, 12 luni și condițiile de oprire

Toate termenele pornesc de luni, **19 octombrie 2026**, cu ~11 h/săptămână (~48 h/lună; ~140 h în 90 de zile). Țintele numerice sunt **estimări** (modelul de ore și rampa din `../cfo/`). Comparația cu Scadențarul MM și recomandarea de secvență sunt în analiza finală.

## Primele 90 de zile (19.10.2026 – 17.01.2027)

**Săptămânile 1–4: descoperire, fără cod (~40 h)**
- **10–12 conversații calificate**, în ordinea din panel:
  - 5 manageri HSE la fabrici din Oradea (Plexus, Celestica, Connect Group, Emerson; lista din N05 §1);
  - 3 utilități (Compania de Apă Oradea, RER Vest, Termoficare Oradea);
  - 2 firme de pază cu dispecerat;
  - 2 firme forestiere private (Aleșd–Beiuș).
  - **Faist Mekatronic** e evitată: e în concordat (N05 §1).
- **Întrebările** (din R §9): câți oameni lucrează izolat și unde; ce folosesc acum; cine semnează și până la ce sumă fără licitație; ce a cerut ITM-ul sau auditul ISO 45001 pe lucrul izolat; cine e reprezentantul lucrătorilor.
- **ITM Bihor:** cum aplică HG 1091/2006 și dacă un sistem de alarmă cu procedură contează ca „legătură cu exteriorul”.
- **3 oferte scrise de la firme de pază pentru dispecerat:** tarif pe persoană conectată, minim lunar, timp de preluare garantat, penalități, autorizare după Legea 333/2003, acceptarea neconcurenței pe segment.
- **Distribuitorul Teltonika:** TMT250 merge pe 2G sau pe LTE-M/4G? Ce înlocuiește GH5200? Documentația Codec 8; preț la 30 și 200 de bucăți. Se cumpără 3 TMT250 + 1 alternativă LTE.
- **2 oferte de asigurare RC** profesională, care să acopere explicit dispeceratul de alarme pentru persoane (prin broker).
- **O oră de consultanță la un avocat** (dreptul muncii + GDPR) pe răspundere, clauzele de limitare și Legea 333/2003.

**Săptămânile 5–10: lanțul minim (~70 h)**
- **Traccar** primește Codec 8 de la cele 3–4 dispozitive și trimite webhook la **n8n** (pre-alarmă de 30 s; escaladare la 60 s; SMS direct din Traccar ca a doua cale).
- **Ecranul APEX de dispecerat:** coadă cu cronometru, hartă, fișa lucrătorului, butoane pe pași cu ora salvată, ștergere automată după 30 de zile prin PL/SQL. Test automat zilnic. Fără satelit, gaze sau puls.
- **Bench test:** 3 dispozitive purtate 10 ture reale (prieteni, colegi, un client prietenos). Se notează alarmele false și bateria.
- **Testul end-to-end:** 50 de alarme simulate, zi, noapte și weekend, prin operatorii reali ai pazei alese.

**Săptămânile 9–13: primele vânzări (~30 h)**
- **3 teste de semnal gratuite** la cei mai calzi 3 prospecți. Ținta: cel puțin 2 manageri HSE.
- **Trimiterea ofertei de pilot** (`../offer/offer.md` §6) după fiecare test.
- **Metrici go / no-go în ziua 90:**
  - conversații calificate: **GO ≥10**, din care ≥5 HSE sau utilități; **NO-GO <6**;
  - oferte de dispecerat: **GO ≥2**, cu tarif ≤3 EUR/lucrător, minim ≤150 EUR/lună, preluare ≤60 s cu penalități; **NO-GO**: niciuna acceptă SLA cu penalități;
  - dispozitiv confirmat pe LTE-M/4G: **GO da**, cu un al doilea model testat; **NO-GO**: doar 2G și fără înlocuitor;
  - asigurarea RC care acoperă dispeceratul: **GO ofertă ≤2.500 EUR/an**; **NO-GO**: niciun asigurător sau >3.500 EUR/an;
  - testul de 50 de alarme: **GO** 50/50 ajung și ≥95% preluate sub 60 s; **NO-GO**: sub 100% după a doua încercare;
  - alarme false la bench test, după reglaj: **GO <2 la 100 de ture-om**; **NO-GO >5 la 100**;
  - teste de semnal acceptate: **GO ≥3**; **NO-GO ≤1**;
  - **piloți plătiți semnați (2.500 lei): GO ≥1 până în ziua 90** (sau o comandă fermă pentru ianuarie); **NO-GO: 0 după 3 teste de semnal**;
  - orele fondatorului: **GO ≤12 h/săpt**; **NO-GO >15 h/săpt, susținut**;
  - numerarul cheltuit: **GO ≤6.600 EUR**; **NO-GO >9.000 EUR fără niciun pilot plătit**.
- **Decizia din ziua 90:**
  - **GO:** toate cele de mai sus;
  - **PIVOT spre „dispeceratul vostru”:** cumpărătorii vor, dar nicio pază nu acceptă SLA-ul și nicio asigurare nu acoperă. Atunci se vinde doar software-ul (licență de 6 EUR/lucrător) unei firme de pază sau unei fabrici cu dispecerat propriu, iar răspunderea dispeceratului rămâne la ele;
  - **STOP:** oricare dintre NO-GO-urile marcate cu „STOP” de mai jos.

## Primele 12 luni (după cele 90 de zile)

- **Luna 4–5 (feb.–mar. 2027):** primul pilot de 60 de zile, la o fabrică (mentenanță sau tura de noapte, 20 de lucrători). Raport săptămânal; interviuri cu lucrătorii în ziua 55. În paralel, al doilea test de semnal.
- **Luna 6 (apr. 2027):** prima conversie, cu 20 de lucrători × 12 EUR = **240 EUR MRR**, plus vânzarea dispozitivelor (~650 lei bucata). Începe al doilea pilot. Cu acordul clientului, se scrie un **studiu de caz** (timpi de preluare, purtare, alarme false), anonimizat.
- **Luna 7–9:** a doua conversie în luna 9 (~480 EUR MRR). Abia acum, cu o referință, se semnează **acordul de recomandare cu 1–2 servicii externe SSM** (comision de 15%, cu răspunderea furnizorului scrisă). Se oferă licența „dispeceratul vostru” unei singure firme de pază.
- **Luna 10–12:** al treilea client în luna 12. **~70 de lucrători, ~840 EUR MRR** (CFO, scenariul de bază). Primul client crește spre 30 de lucrători.
  - **Decizia din luna 12:** cu ≥3 clienți plătitori și ≥700 EUR MRR, fie se trece la ~20 h/săpt (atunci 3.000 EUR MRR vine în ~luna 24, CFO `h20`), fie se plătește un ajutor part-time. Altfel, vezi condițiile de oprire.
- **Finanțare opțională, fără să depindă de ea:**
  - voucherul de inovare UEFISCDI (≤50.000 lei), cu Universitatea din Oradea, pentru validarea alarmelor false pe datele pilotului;
  - servicii gratuite EDIH (R §8; N06 §7).
- **Ce nu se face în anul 1:** pădurea și satelitul, gazele, stresul termic, pulsul, ML-ul în lanțul de alarmă (AI Act; R §5), dispeceratul propriu 24/7 (care se plătește abia peste ~2.400 de lucrători; R §7) și licitațiile SEAP mari.

## Condițiile de oprire (kill criteria)

Oprești proiectul, nu îl „mai împingi o lună”, dacă se întâmplă oricare dintre următoarele:
1. **Ziua 90:** 0 piloți plătiți după ≥10 conversații calificate și ≥3 teste de semnal. Asta înseamnă că cererea nu există la acest preț și sub această formă.
2. **Nicio firmă de pază** nu acceptă în scris preluarea în ≤60 s cu penalități, la ≤3 EUR/lucrător, **și** niciun prospect nu are dispecerat propriu. Fără acest om care răspunde, nu există produs.
3. **Nicio asigurare RC** nu acoperă dispeceratul de alarme pentru persoane, sau costă peste 3.500 EUR/an. Garanția și răspunderea din ofertă nu se pot susține.
4. **Testul end-to-end** nu ajunge la 100% alarme livrate după două iterații, sau alarmele false rămân peste 5 la 100 de ture-om după reglaj.
5. **În pilot:** purtarea scade sub 60% din ture sau alarmele de test ajung sub 95% (pragurile de oprire din R §6). Se oprește pilotul la acel client. La doi piloți eșuați la rând, se oprește proiectul.
6. **Luna 9:** niciun client plătitor de abonament. **Luna 12:** sub 2 clienți plătitori sau sub 500 EUR MRR.
7. **Timpul:** peste 15 h/săpt timp de două luni la rând, **sau** o alarmă reală (sau de test) care n-a fost preluată pentru că lanțul a depins de fondator (examen, noapte, telefon închis) și nu există încă rezervă plătită.
8. **Banii:** peste 9.000 EUR cheltuiți înainte de primul abonament încasat. Peste o treime din capital s-ar duce înainte de prima dovadă.
9. **Un incident real grav** în care lanțul a eșuat. Se oprește vânzarea până la analiza cauzei și opinia avocatului și a asigurătorului.
