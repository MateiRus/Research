# „Busola” — monitor de implementare pentru proiecte finanțate (fișa produsului, ciornă)

**Din:** `lateral/03-random-stimulus.md`, stimulul Sextant. **Stare:** ipoteză, netestată cu clienți reali. Livrat ca aplicație web (APEX), deci rămâne în zona serviciilor web.

## Într-o frază
Busola îi spune unui consultant, pentru fiecare client aflat în implementare, cât de departe e de pragurile din planul de afaceri, câți bani riscă și până când trebuie să recupereze, calculat automat din facturile emise.

## Problema
- Beneficiarii de start-up (DR36/LEADER, sM 6.2, tineri fermieri, Diaspora ReSTART, Start-Up Nation) au în plan praguri obligatorii: venituri minime (de ex. 30% din prima tranșă), locuri de muncă, termene. Nerespectarea înseamnă tranșa a doua pierdută și recuperare proporțională sau integrală [VERIFICAT – sursă secundară].
- Azi, nimeni nu vede traiectoria până la cererea tranșei a doua. Consultantul află când e prea târziu; beneficiarul nu știe să calculeze.
- Pierderea tipică: zeci de mii de euro per proiect. Produsul costă o fracțiune.

## Ce face (MVP)
1. **Configurare proiect** (15 minute, din contract): valoarea primei tranșe, pragul (%), termenul, alte repere (angajați, investiții).
2. **Date** — trei căi, de la cea mai simplă: (a) ping lunar pe WhatsApp cu 3 întrebări; (b) import lunar al jurnalului de vânzări exportat din programul de facturare; (c) conectare la SPV / e-Factura prin API ANAF, acces doar de citire, revocabil din SPV, autorizat de firmă sau de contabil.
3. **Calcul**: realizat vs prag, ritm pe ultimele 3 luni, luna estimată de atingere, suma lipsă, „suma expusă” la recuperare.
4. **Alerte**: verde / galben / roșu; mesaj către consultant și beneficiar când traiectoria ratează termenul.
5. **Tablou de portofoliu** pentru consultant: toți clienții în implementare, sortați după risc.

## Demonstrația care vinde (5 minute)
Proiectul ILLUSTRUS, cu facturile reale: „sunt la X% din pragul meu, termenul e luna Y, la ritmul ăsta ajung în luna Z”. Apoi: „dați-mi 3 clienți în implementare și în 10 minute vedeți același lucru pentru ei.”

## Cine plătește și cât [ESTIMARE, de testat]
| Cumpărător | Preț | Logica |
|---|---|---|
| Consultant cu 10–50 de proiecte în implementare | 10 EUR / proiect / lună, minim 100 EUR/lună | își protejează onorariul de succes și reputația; o tranșă pierdută la un client costă mai mult decât un an de Busola |
| Beneficiar direct | 149 EUR / an | „nu-ți pierde tranșa a doua” |
| GAL | pachet pe tot teritoriul | monitorizarea indicatorilor strategiei; de verificat dacă are nevoie și buget |

## De ce ar fi „atât de bun”
- **Rezultat dorit mare:** nu pierzi banii grantului.
- **Probabilitate percepută mare:** cifrele vin din facturile reale, nu din estimări; fondatorul îl folosește pe propriul proiect.
- **Timp scurt:** valoarea apare la prima rulare.
- **Efort mic:** fără documente încărcate, fără conturi noi pentru beneficiar; acces doar de citire.
- **Încredere cerută mică:** nu ține dosare, nu decide eligibilitate, nu operează nimic critic.

## Riscuri
- Pragurile și baza de calcul diferă pe program și pe GAL; configurarea per proiect trebuie validată de consultant.
- Autorizarea SPV e legată de certificatul celui care semnează; expiră sau se revocă (reautorizare anuală).
- Consultanții pot spune „țin asta în Excel”; testul trebuie să arate un client real la risc pe care nu-l știau.
- Concurență posibilă din programele de facturare sau contabilitate dacă piața se dovedește bună.

## Cum se testează, în ordine
1. Busola pentru ILLUSTRUS: configurare + import facturi + tablou (8–12 h).
2. Arăți consultantului tău; ceri 3 clienți în implementare, anonimizați.
3. 5 discuții cu consultanți care fac și implementare; întrebarea-cheie: „câți dintre clienții tăi în implementare știi azi exact unde sunt față de prag?”
4. Prag: 2 consultanți acceptă un pilot plătit pe 3 luni.
