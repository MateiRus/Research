# Plan v3: răspuns la review și corecții — doar partea de prestare servicii web

**Data:** 7 octombrie 2026. **Construit pe:** `plan-de-afaceri-v2.md`. **Scop:** aplic punctele din review-ul primit care țin de oferta comercială, de timp, de prețuri, de concurență și de calcule. **La cererea ta, nu am verificat și nu am modificat nimic legat de conformitate** (versiunea ghidului DR36, manualul citat, încadrarea CAEN, INS, GDPR). Acele observații din review sunt listate în §1 ca „în afara scopului”, ca să nu se piardă.

Legendă: **[VERIFICAT – sursă secundară]** = confirmat prin căutare web azi, fără a putea deschide pagina · **[ESTIMARE]** = judecata mea · **[DE VERIFICAT]** = nu am putut confirma.

---

## 1. Răspuns la review, punct cu punct

| Punctul din review | Verdict | Ce am făcut în v3 |
|---|---|---|
| Simplifică oferta; amână radarul până există un client care plătește | **Accept.** V2 cerea simultan vânzare, dezvoltare de produs și operare de serviciu. | Oferta devine START + PRO (2 automatizări definite) + RADAR doar ca pilot plătit, cu surse și responsabilități scrise (§2). Motorul complet (90 h) dispare din scenarii; rămâne un pilot de 30 h după acceptarea pilotului. |
| „Gol real — nimeni nu vinde așa” e prea ferm; IMFS One are calendar de termene și remindere pentru cabinete | **Accept.** IMFS One există și vinde un CRM pentru cabinete contabile (imfs.ro/ro/crm/industrii/cabinet-contabil/) [VERIFICAT – sursă secundară]; funcțiile exacte de remindere nu le-am putut citi. | „Gol real” devine „ipoteză de validat” (§4), cu un test de diferențiere măsurabil. |
| „Radar Finanțări” al Academiei de Finanțare, alternativă gratuită | **Accept parțial.** Academia de Finanțare există (platformă educațională pentru fonduri) [VERIFICAT – sursă secundară]; pagina „Radar Finanțări” nu a apărut în nicio căutare [DE VERIFICAT]. | Adăugat la comparația cumpărătorului, marcat ca neconfirmat (§4). |
| AFIR are listă publică de firme de consultanță, cu filtre pe județ; v2 spunea că nu există | **Accept. V2 era greșit.** Lista există: afir.ro/instrumente/nomenclator/firme-de-consultanta/ (și pe portalul vechi portal.afir.info), nu e exhaustivă, conține firme pe tipuri de servicii [VERIFICAT – sursă secundară]. | Devine sursa nr. 1 pentru lista de prospecți (§4.3). |
| Prețurile: compararea cu agențiile AEO nu dovedește disponibilitatea de plată; clientul vede costul total pe 12 luni | **Accept.** | Tabel cu cost total pe 12 luni în ofertă (§2.2); RADAR scos din oferta standard. |
| Bugetul de timp subestimează orele contractate (2/4/6 în ofertă vs 1,5/3/5 în scenarii) | **Accept.** | Scenariile folosesc orele contractate **la maxim** (§5). |
| Alerte validate în 24 h e greu lângă job și facultate; validarea ta nu confirmă eligibilitatea | **Accept.** | Promisiunea devine „următoarea zi lucrătoare, până la ora 18” (practic ≤ 48 h), cu responsabilitatea eligibilității atribuită explicit consultantului (§3.2). |
| 95% la extragerea termenelor = un termen greșit din 20 | **Accept.** | Câmpurile critice (termen limită, link sursă) se verifică în sursă, manual, înainte de orice trimitere; pragul de 95% rămâne doar ca indicator intern (§3.3). |
| APEX/ORDS public nu înseamnă API stabil | **Accept.** | Catalogul MySMIS devine sursă „de citit”, nu „de integrat”, până testezi 30 de zile stabilitatea (§3.3). |
| Erori de calcul: 40.000 × 83% × 30% = 9.960; prudent luna 20 = 12.920, luna 23 = 17.180; o lună de 50 h | **Accept, toate trei.** Am recalculat: review-ul are dreptate. | Exemplul devine 9.960 EUR; scenariile sunt refăcute integral (§5), cu plafon de 48 h respectat în fiecare lună. |
| Probabilitățile 25/50/25% nu au fundament | **Accept.** | Eliminate. Scenariile sunt „ipoteze de lucru”, nu probabilități. |
| Separă venit eligibil, încasări, profit; costurile nu includ timpul tău, contabilitatea, deplasările, licențele | **Accept.** | Model separat în §5.5. |
| Reducerea de pilot nu poate fi condiționată de o recenzie Google | **Accept.** | Reducerea se dă pentru studiu de caz + 2 introduceri; recenzia se cere separat, fără nicio recompensă (§6). |
| Scenariul de lucru: 2 PRO × 1.920 + 3 PRO × 2.400 = 11.040 EUR, fără dependență de radar | **Accept.** | Devine scenariul principal („de lucru”), §5.1. |
| Plan pe 30 de zile + criteriu de oprire (10 discuții, 3 oferte, 0 avans) | **Accept.** | §7. |
| Manualul citat e PS-DR-36F (pentru GAL-uri), nu pentru beneficiari; AFIR are Revizia 3 din 2 oct. 2026; elimină „alinierea” facturii la CAEN; INS; adăugarea unui CAEN la ONRC nu garantează recunoașterea | **În afara scopului, la cererea ta.** Nu am verificat, nu am modificat §A din v2. | Nimic. Observațiile rămân aici, pentru când vrei să le tratezi. |

---

## 2. Oferta simplificată

### 2.1 Trei produse, dintre care doar două se vând acum

| | **START** | **PRO** | **RADAR — pilot** (nu e în oferta standard) |
|---|---|---|---|
| Ce primește | Site 6–8 pagini cu texte scrise de tine din 2 interviuri, FAQ, date structurate, Google Business, Search Console, formular → cerere structurată + notificare | START + **exact 2 automatizări**: (1) formular → cerere structurată → calificare preliminară (eligibil probabil / nu, cu motiv) → notificare → programare; (2) colectare documente de la clienții consultantului prin link securizat, cu listă de lipsuri și remindere | Pentru **un singur consultant**: 3 surse (MIPE JSON, Regio NV, AFIR sesiuni), 5 profiluri de clienți finali, alerte până în următoarea zi lucrătoare, 30 de zile, cu drept de a nu continua |
| Preț instalare | 1.200 EUR (pilot primii 2 clienți: 960) | 2.400 EUR (pilot: 1.920) | 1.100 EUR pentru cele 30 de zile |
| Abonament | 60 EUR/lună, **2 h/lună incluse** | 140 EUR/lună, **4 h/lună incluse** | după pilot: de stabilit împreună (acoperire, surse, profiluri); reper 280 EUR/lună, 6 h/lună |
| Ore de livrare (ale tale) | 22 h | 45 h | 30 h |
| Ce **nu** include | Articole, campanii, poziții garantate | Portal cu OCR, integrare cu programe de contabilitate, mai mult de 2 automatizări | Acoperire „toate sursele”, verificarea eligibilității |

Ce s-a scos față de v2: RADAR ca pachet standard la 3.500 + 280; pachetele pentru contabili și SSM/brokeri ies din oferta activă până ai 3 clienți în nișa 1 (rămân în v2 ca rezervă).

### 2.2 Ce vede clientul: costul total pe 12 luni (fără TVA)

| Pachet | Instalare | Abonament lunar | Instalare + 12 luni | Cu preț de pilot |
|---|---|---|---|---|
| START | 1.200 EUR | 60 EUR | **1.920 EUR** | 1.680 EUR |
| PRO | 2.400 EUR | 140 EUR | **4.080 EUR** | 3.600 EUR |
| RADAR pilot (30 zile) | 1.100 EUR | — | 1.100 EUR | — |
| RADAR după pilot (reper) | — | 280 EUR | 3.360 EUR/an | — |

Pune tabelul ăsta în ofertă. Un consultant compară 4.080 EUR cu onorariul lui pe un proiect mediu; dacă nu poate spune în 10 secunde ce economisește sau ce câștigă, prețul e prea mare pentru el, nu pentru piață.

---

## 3. Timp, promisiuni, precizie

### 3.1 Orele contractate, la maxim [ESTIMARE]

| Clienți activi | Ore abonament/lună dacă toți folosesc tot | Ore abonament/lună (medie, ca în v2) |
|---|---|---|
| 1 START + 1 PRO | 6 | 4,5 |
| 2 START + 2 PRO | 12 | 9 |
| 2 START + 3 PRO | 16 | 12 |
| 2 START + 3 PRO + 1 RADAR | 22 | 17 |

Cu 10 h vânzare + 2 h administrare pe lună, la 5 clienți îți rămân **20 h/lună pentru livrări noi** în cazul maxim. Asta înseamnă un PRO la 2–3 luni, nu mai des. Regulă: orele neconsumate nu se reportează (scris în contract); peste ore, tarif orar de 35 EUR.

### 3.2 Promisiuni refăcute

| V2 promitea | V3 promite |
|---|---|
| Alerte validate în max 24 h | Alerte validate **până în următoarea zi lucrătoare, ora 18**; în sesiune (anunțată cu 30 de zile înainte): 2 zile lucrătoare |
| „Validate de om” | „Verificate de ILLUSTRUS pentru corectitudinea datelor (termen, link, sursă). **Verificarea eligibilității clientului final este responsabilitatea consultantului.**” — clauză în contract și text în fiecare alertă |
| 8 surse, 30 profiluri | Pilot: 3 surse, 5 profiluri; extinderea se negociază după pilot, cu ore și preț |

### 3.3 Precizie și dependențe tehnice

- **Câmpuri critice** (termen limită, link la sursă, program): verificate manual în sursă pentru fiecare alertă înainte de trimitere. Nu se trimite nimic doar pe baza extracției AI. Pragul de 95% rămâne indicator intern de calitate a extracției, nu promisiune.
- **Set de test** (din v2 §C.3) se păstrează, redus la 40 de elemente pentru pilot.
- **Catalogul MySMIS pe APEX/ORDS**: tratat ca pagină de consultat manual, nu ca API, până când 30 de zile de interogare zilnică arată structură stabilă și fără blocaje. Pilotul pornește de la API-ul JSON al MIPE (`oportunitati-ue.gov.ro/wp-json/wp/v2/apel`) și de la paginile HTML Regio NV și AFIR, cu diff pe listă.
- **Colectorul** rulează de pe o conexiune din România (constrângerea din v2 rămâne).

---

## 4. Concurența: de la „gol real” la ipoteze de validat

### 4.1 Ce știm acum

| Produs | Ce confirmă căutarea | Ce nu știm | Statut |
|---|---|---|---|
| **IMFS One** (imfs.ro) | Platformă românească ERP/CRM cu AI; are pagină dedicată „CRM pentru cabinet de contabilitate”; module financiar, e-Factura, SPV; „Predictive Accounting” în testare | Dacă reminderele către clienții finali sunt automate și personalizate per client; prețul pentru cabinete; adopția | [VERIFICAT – sursă secundară: wall-street.ro, imfs.ro] |
| **Academia de Finanțare** (academiadefinantare.ro) | Platformă educațională pentru fonduri nerambursabile, cursuri, prezentări video de programe | Existența unei pagini „Radar Finanțări” cu calendar și eligibilitate; nu a apărut în căutări | [DE VERIFICAT] |
| **Lista AFIR de firme de consultanță** | Există la afir.ro/instrumente/nomenclator/firme-de-consultanta/ (și portal.afir.info); conține firme pe tipuri de servicii (plan de afaceri, consultanță implementare, monitorizare); AFIR spune că nu e exhaustivă | Filtrele exacte (județ) — indicate de reviewer, neverificate de mine | [VERIFICAT – sursă secundară] |
| Agregatoare (fonduri-structurale.ro, finantare.ro, startupcafe.ro), buletine ADR/CJ, folositor.ro | Ca în v2 | — | [VERIFICAT – sursă secundară] |

### 4.2 Ipotezele de validat în discuțiile cu consultanții

1. „Consultanții află de corrigenda și de apeluri noi cu întârziere și pierd timp verificând manual.” → Întreabă: *Ultimele 3 apeluri relevante pentru clienții tăi, cum ai aflat de ele și când, față de data publicării?*
2. „Cererile neeligibile consumă ore.” → *Câte cereri ai primit luna trecută și câte au fost pierdere de timp? Cât a durat să le triezi?*
3. „Documentele lipsă blochează dosarele.” → *La ultimul dosar, câte zile ai așteptat acte de la client și cum le-ai cerut?*
4. „Ar plăti pentru asta.” → *Dacă ți-aș economisi X ore pe lună, cât ar valora? Ce folosești acum și cât plătești?*

Dacă 6 din 10 consultanți răspund „aflu la timp, din newslettere, gratuit”, radarul nu se construiește. Dacă 6 din 10 spun „pierd 5+ ore pe lună cu cereri și acte”, PRO e produsul.

### 4.3 Testul de diferențiere (ce arăți, nu ce afirmi) [ESTIMARE]

Pentru fiecare client-pilot, măsori și raportezi trei lucruri, în raportul lunar:
- **Timp economisit**: ore de triere a cererilor înainte vs după (clientul estimează la început; tu numeri cererile procesate automat).
- **Viteză**: timpul de la cerere la primul răspuns (ore) înainte vs după.
- **Oportunități relevante**: numărul de alerte aprobate de consultant ca relevante pentru portofoliul lui, pe lună, și câte dintre ele nu le știa deja.
Fără aceste cifre după 60 de zile, nu ai argument de vânzare pentru al doilea client.

### 4.4 Lista de prospecți, actualizată

Ordinea surselor: (1) lista AFIR de firme de consultanță, filtrată pe Bihor și București; (2) termene.ro / topfirme.com pe CAEN 7022; (3) Necesit.ro „Top 20 consultanță fonduri europene București 2026”; (4) ACRAFE (lista de membri [DE VERIFICAT]); (5) Google Maps. Restul metodei ca în v2 §E.1.

---

## 5. Scenariile financiare, refăcute

Ipoteze comune [ESTIMARE]: instalarea e contabilizată în luna livrării; abonamentul din luna următoare; primele 2 contracte la −20%; **orele contractate folosite integral** (2/4/6 h); 10 h vânzare + 2 h administrare pe lună; demo PRO de 20 h în lunile 1–2; livrări: START 22 h pe 2 luni, PRO 45 h pe 3 luni, pilot RADAR 30 h pe 2 luni + 40 h de motor întinse pe 6 luni înainte; **plafon 48 h/lună, verificat lună cu lună**. Fără probabilități.

### 5.1 Scenariul de lucru: 5 × PRO, fără radar → 10.000 EUR în luna 13

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 1–3 | demo, ~15 discuții | 0 | 0 | 0 | 22–37 |
| 4 | PRO (pilot) | 1.920 | 0 | 1.920 | 27 |
| 5–6 | — | 0 | 140 | 2.200 | 31 |
| 7 | PRO (pilot) | 1.920 | 140 | 4.260 | 31 |
| 8–9 | — | 0 | 280 | 4.820 | 35 |
| 10 | PRO | 2.400 | 280 | 7.500 | 35 |
| 11–12 | — | 0 | 420 | 8.340 | 39 |
| **13** | PRO | 2.400 | 420 | **11.160** | 39 |
| 16 | PRO | 2.400 | 560 | — | 43 |

Doar instalări: 11.040 EUR la al cincilea PRO (luna 16). Cu abonamente: luna 13. Ore maxime: 39–43. Nu depinde de radar.

### 5.2 Rapid → luna 13 (ore max 45)

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 3 | START (pilot) | 960 | 0 | 960 | 23 |
| 6 | PRO (pilot) | 1.920 | 60 | 3.060 | 36 |
| 9 | PRO | 2.400 | 200 | 6.060 | 40 |
| 11 | RADAR pilot | 1.100 | 340 | 7.840 | 37 |
| 12 | — | 0 | 620 | 8.460 | 39 |
| **13** | START | 1.200 | 620 | **10.280** | 39 |
| 16 | PRO | 2.400 | 680 | — | 45 |

Abonamente până în luna 13: 2.700 EUR (26%). Doar instalări: 10.980 EUR în luna 16.

### 5.3 Echilibrat → luna 15 (ore max 40)

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 4 | START (pilot) | 960 | 0 | 960 | 23 |
| 7 | PRO (pilot) | 1.920 | 60 | 3.060 | 29 |
| 10 | PRO | 2.400 | 200 | 6.060 | 40 |
| 13 | START | 1.200 | 340 | 8.280 | 40 |
| **15** | RADAR pilot | 1.100 | 400 | **10.180** | 39 |
| 18 | PRO | 2.400 | 680 | — | 45 |

Abonamente până în luna 15: 2.600 EUR (26%). Doar instalări: 10.380 EUR în luna 18.

### 5.4 Prudent → luna 19 (ore max 35)

| Luna | Contract livrat | Instalare | Abonamente în lună | Cumulat | Ore/lună |
|---|---|---|---|---|---|
| 5 | site local (fallback) | 800 | 0 | 800 | 26 |
| 7 | site local (fallback) | 800 | 40 | 1.680 | 27 |
| 9 | START (pilot) | 960 | 80 | 2.800 | 25 |
| 12 | PRO (pilot) | 1.920 | 140 | 5.140 | 31 |
| 16 | PRO | 2.400 | 280 | 8.660 | 35 |
| **19** | START | 1.200 | 420 | **11.120** | 35 |
| 22 | PRO | 2.400 | 480 | — | 41 |

Abonamente până în luna 19: 3.040 EUR (27%). Doar instalări: 10.480 EUR în luna 22. Nicio lună peste 41 h.

Toate scenariile presupun: contractele se semnează, se livrează, se plătesc integral și veniturile sunt recunoscute în proiect. Dacă abonamentele nu sunt recunoscute, coloana „doar instalări” dă luna: 16 / 16 / 18 / 22.

### 5.5 Venit eligibil, încasări, profit — separat [ESTIMARE]

| Element | Scenariul de lucru (13 luni) | Observație |
|---|---|---|
| Venit facturat (instalări + abonamente) | 11.160 EUR | ce se raportează în proiect, dacă e recunoscut |
| Încasări | ~10.700 EUR | ultimul PRO: a doua tranșă (1.200) vine la ~30 de zile după livrare |
| Costuri externe: infrastructură (VPS, API, găzduire) | 13 × 40 = 520 EUR | |
| Licențe (temă, plugin-uri premium, domenii) | 300 EUR | |
| Deplasări (2 drumuri/lună în medie, tren) | 13 × 80 = 1.040 EUR | dacă le combini cu drumurile acasă, costul real e mai mic |
| Contabilitate suplimentară generată de activitate | 13 × 30 = 390 EUR | contabilul SRL-ului există deja; aici e doar volumul în plus |
| **Marjă înainte de timpul tău** | **~8.900 EUR** | |
| Ore lucrate (medie 33 h/lună) | ~430 h | |
| **Marjă pe oră** | **~20 EUR/h** | sub tariful tău de piață ca dezvoltator; acceptabil doar pentru că obiectivul principal e obligația din proiect |

Dacă marja pe oră scade sub 12 EUR (de exemplu pentru că orele contractate sunt consumate integral și vânzarea durează dublu), oprești extinderea și livrezi doar ce ai contractat.

---

## 6. Pilotul, refăcut

Reducerea de 20% pentru primii 2 clienți se acordă **în schimbul a două lucruri, scrise în contract**: un studiu de caz cu nume și cifre (publicat după 60 de zile) și două introduceri către alți consultanți. **Recenzia Google se cere separat, tuturor clienților, fără nicio reducere sau serviciu în schimb.** Garanția de specificație pe START și cele 90 de zile de corectări rămân.

---

## 7. Următoarele 30 de zile și criteriul de oprire

| Săpt. | Ce faci | Ore |
|---|---|---|
| 1 | Trimiți scrisoarea către GAL/OJFIR (din v2 §A.2, neschimbată). Construiești lista de 50 din lista AFIR + termene.ro. Programezi prin telefon 4 discuții pentru drumul în Oradea. | 10 |
| 2 | **Demo PRO**: formular → cerere structurată → calificare → notificare → programare. Plafon propriu: **15–20 h**, fără radar. | 11 |
| 3 | Drumul 1 în Oradea: consultantul tău, 3 consultanți noi. Întrebările din §4.2, nu prezentare. | 12 |
| 4 | 4 discuții online cu consultanți din București; 3 oferte scrise (START sau PRO) cu tabelul de cost pe 12 luni. | 11 |

Ținta la 30 de zile: **10 discuții, 3 oferte, 1 avans** (480–960 EUR). Radarul intră în dezvoltare numai după ce un consultant semnează pilotul de 1.100 EUR cu surse, profiluri și responsabilități scrise.

**Criteriul de oprire:** după 10 discuții și 3 oferte concrete, zero avans → revizuiești, în ordinea asta, problema (ce spun ei că-i doare), oferta (ce automatizare o rezolvă), publicul (consultanți de fonduri vs. consultanți de afaceri vs. contabili). Nu mai construiești nicio funcționalitate până nu schimbi una dintre cele trei.

---

## 8. Ce rămâne valabil din v2

Fără modificări: registrul de surse (§C.1–C.2), schema de date și fluxurile n8n (§C.4–C.5), evenimentele și regulile de contactare (§E.2–E.3), scriptul de telefon și follow-up-ul (§E.4–E.5), structura contractului (§F.2), specificația demo-ului (§F.3, cu partea de radar devenită opțională), calendarul pe 12 săptămâni (§F.4; orele de construcție din săptămânile 3–5 se mută de pe radar pe demo-ul PRO). Secțiunea §A (finanțare) rămâne ca în v2, nerevizuită, la cererea ta.

## Surse noi față de v2

- IMFS One: https://imfs.ro/ro/crm/industrii/cabinet-contabil/ , https://www.wall-street.ro/articol/economie-and-finante/imfs-one-intra-in-testare-cu-primul-motor-predictiv-nativ-pentru-contabilitate.html
- Academia de Finanțare: https://academiadefinantare.ro/
- Lista AFIR de firme de consultanță: https://www.afir.ro/instrumente/nomenclator/firme-de-consultanta/ , https://portal.afir.info/informatii_generale_rapoarte_si_liste_lista_firme_de_consultanta , https://agrointel.ro/31712/lista-firme-de-consultanta-fonduri-europene-agricultura-fiecare-judet
