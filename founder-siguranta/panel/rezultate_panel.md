# Panelul de cumpărători B2B (simulat)

**Cum a rulat.**
- `founder-consumer/panel.py`, 30 de cumpărători, seed 2026, aceleași cărți la ambele variante (`v1/`, `v2/`).
- Fiecare cumpărător e un **sub-agent separat** (`claude -p`, model sonnet, fără unelte). A primit brieful scris de `panel.py` plus un sufix identic pentru toți (`uniform_suffix.txt`). Sufixul spune:
  - cifra de pe card e cifra de afaceri a organizației, în EUR;
  - prețurile sunt în EUR/lucrător/lună, fără TVA;
  - „cumpără” înseamnă că semnează ceva care îl obligă la bani în 3 luni;
  - la serviciul extern SSM, „cumpără” înseamnă că semnează un acord de recomandare și îl propune activ la 2 clienți.
- Răspunsul propriu al fiecărui cumpărător a fost salvat cu `panel.py save`. 60 de apeluri, toate valide. N-am scris niciun răspuns în locul unui cumpărător. **N-a fost întrebat niciun om real.**
- **Cele cinci tipuri cerute**, câte 6 cumpărători fiecare (`customer.json`):
  - șef SSM la o utilitate locală;
  - patron de firmă forestieră privată;
  - manager HSE (sănătate, securitate, mediu) la o fabrică mare;
  - director de firmă de pază;
  - administrator de serviciu extern SSM.
  - Comportamentele și obiecțiile vin din note (N05 §2, §6; R §1).
- **Limitele:**
  - modelele de limbaj tind să fie de acord, deci rata e o **limită superioară**;
  - toți cumpărătorii sunt același model, deci răspunsurile sunt corelate;
  - la n=6 pe segment, orice diferență e „subțire”;
  - citatele sunt simulate, nu mărturii de clienți.

## Rezultatele

- **v1** (pitch-ul din cercetare: 20 EUR cu dispozitiv sau 12 EUR + dispozitiv cumpărat, contract de 24 de luni, pilot gratuit de 90 de zile cu dispozitivele cumpărate de client): **4 / 30 (13%)**.
  - HSE fabrică: 2/6; serviciu extern SSM: 2/6.
  - Utilitate: 0/6; forestier: 0/6; pază: 0/6.
- **v2** (oferta refăcută din `../offer/`): **4 / 30 (13%)**, adică **aceeași rată, alți cumpărători**:
  - HSE fabrică: **3/6**; utilitate: **1/6** (cel „marcat de un accident”);
  - serviciu extern SSM: **0/6** (cere referințe; comisionul îl face „să pară interesat”);
  - forestier: 0/6; pază: 0/6.
- **Cine cumpără la ambele variante:** cei „marcați de un accident” și cei „deschiși la tehnologie”. Nu cumpără niciodată cei care „se mișcă doar la control”, „taie din costuri” sau „conservatori”.

## De ce refuză (citate simulate)

- **Nu pot semna singur / procedură** (v1: 10 pe „încredere”, v2: 11): „Nu pot semna singur nimic care mă obligă la bani: trebuie aprobarea directorului, discuția cu sindicatul și o procedură prin SEAP” (v1/P004, utilitate).
- **Fără o cerință ITM nu mă mișc**: „Eu mă mișc la SSM doar când vine ITM-ul sau un auditor și cere ceva scris” (v1/P003, forestier). ITM-ul apare în ce-ar schimba decizia la 9 din 26 de refuzuri în v1 și la 12 din 26 în v2.
- **Prețul pe cap de om** (v1: 6, v2: 4): „100 de lei pe om pe lună e mai mult decât plătesc pe tot serviciul SSM” (v1/P011, forestier).
- **Paza vrea alarma la ea, nu la un concurent:** „Nu dau alarmele agenților mei pe mâna unei alte firme de pază, care îmi e concurent” (v1/P008). Apare la 6 refuzuri în v1. În v2 apare o singură dată, după ce oferta a adăugat varianta „la dispeceratul vostru”, dar prețul a rămas obiecția (cer 4–7 EUR).
- **Răspunderea dacă alarma nu ajunge:** „Dacă omul meu cade la 3 noaptea și nimeni nu sună în 60 de secunde, dosarul penal e al nostru, nu al lor” (v1/P021, HSE).
- **Semnalul în pădure, cămine și subsoluri:** „La noi în pădure nu e semnal în multe locuri, iar ei nu spun nimic despre asta” (v1/P002).

## Ce i-ar face să semneze

- un control ITM sau un auditor care cere în scris măsuri pentru lucrul izolat (cel mai repetat);
- **o referință locală** (altă fabrică, altă utilitate, altă firmă forestieră din Bihor) cu jurnal real de alarme; în v2, 8 refuzuri o cer explicit;
- **testul gratuit de semnal** în locurile lor cele mai grele; în v2, 23 din 30 îl pomenesc și majoritatea l-ar accepta, dar spun că „nu e o cumpărare”;
- acordul scris al sindicatului și al directorului sau al grupului, înainte de pilot;
- contract cu răspunderea scrisă, cu penalități și cu polița RC arătată;
- **preț:** forestierii și paza cer 4–8 EUR; HSE și utilitățile acceptă până la ~16–20 EUR.
