# Oferta refăcută (founder-offer)

## Problemele cumpărătorului (din panel și board, în cuvintele lor)

Înainte de a cumpăra: (1) „un student cu job: cine răspunde la telefon peste un an?”; (2) „prețul de lansare pentru primii 2 = nimeni nu îl folosește”; (3) „4.000 EUR în primul an pentru un site care nu promite clienți”; (4) „12 luni blocat cu un om care lucrează 10 h pe săptămână”; (5) „arată-mi un consultant din România care îl folosește”; (6) „site-ul meu vechi funcționează”; (7) „toți clienții vin din recomandări”; (8) „plătesc automatizări și ore pe care nu le folosesc”.
În timpul folosirii: (9) „fermierii mei nu folosesc linkuri; aduc hârtii”; (10) „AI-ul spune greșit «neeligibil» și pierd un client”; (11) „se strică cu o zi înainte de termen și el e la job”; (12) „suport într-o zi lucrătoare e prea lent lângă un termen”; (13) „regulile apelurilor se schimbă; cine ține pre-check-ul la zi?”.
După: (14) „dacă dispare, portalul meu moare”; (15) „datele clienților mei pe un sistem al unui om”; (16) „ce primesc concret în fiecare lună pentru abonament?”.

## Soluții păstrate (valoare mare, cost mic)

| problemă | soluție | valoare 1–5 | cost 1–5 |
|---|---|---|---|
| 1, 4, 14, 15 | **Instalare pe conturile clientului** (domeniu, găzduire, n8n, stocare în contul lui) + **predare scrisă** + **persoană de rezervă numită** în contract; fără blocare: lunar, preaviz 30 zile | 5 | 2 |
| 3, 6, 7, 8 | **Fără site în ofertă.** Automatizarea de documente se vinde singură, se leagă de site-ul/WhatsApp-ul existent | 5 | 1 |
| 9 | Clientul final primește linkul **pe WhatsApp, în numele consultantului**, poate trimite și poze; consultantul vede lista de lipsuri; reminderele pleacă automat | 4 | 2 |
| 10, 13 | Pre-check-ul **nu dă verdicte**: semnalează date lipsă și criterii evidente (județ, CAEN, mărime); verdictul rămâne la consultant; **test pe 20–50 de cereri reale** înainte de activare | 4 | 2 |
| 11, 12 | Automatizările au **fallback manual** (dacă pică, linkul duce la un formular simplu + e-mail); suport **în aceeași zi lucrătoare până la 18** în săptămâna unui termen anunțat | 3 | 2 |
| 2, 5 | **Pilot la primul client cunoscut** (consultantul fondatorului) 60 de zile, apoi referință telefonică; prețul de lansare dispare după 2 clienți | 5 | 2 |
| 16 | Raport lunar de o pagină: documente colectate, remindere trimise, zile economisite, incidente | 3 | 1 |

Eliminate: site-ul ca produs principal; radarul din ofertă; abonamentul de 12 luni; promisiunea „verificare AI a eligibilității”.

## Stiva

- **Produsul**: „Dosarul complet la timp” — clienții consultantului primesc link și remindere, consultantul vede ce lipsește, nimeni nu mai conduce 60 km după o hârtie.
- **Bonusuri**: (a) pre-check de date lipsă pe cererile noi (+400 EUR dacă vrea verdicte structurate; semnalarea simplă e inclusă); (b) șablon de pagină „Documente necesare” pe site-ul existent; (c) predarea scrisă + persoana de rezervă.
- **Garanția**: dacă în 60 de zile timpul de urmărit documente nu scade (măsurat: zile între cerere și dosar complet, înainte vs după), instalarea se returnează. Cost la o rată de reclamații de 1 din 5: 180 EUR pe contract mediu — acoperit de contribuția de ~700 EUR.
- **Urgență reală**: 2 locuri la preț de lansare până la 31 ianuarie 2027, pentru că fondatorul nu poate livra mai mult de un client la 6 săptămâni.
- **Numele**: „Dosar Complet”.

## Scor pe ecuația valorii (1–10), înainte → după

- Rezultat dorit: 5 → 7 (de la „site” la „dosare complete la timp”)
- Probabilitate percepută: 2 → 5 (pilot cu referință, test pe cereri reale, continuitate; rămâne 5 fără un client real)
- Timp până la rezultat: 4 → 7 (7 săptămâni → 2 săptămâni)
- Efort și sacrificiu: 4 → 7 (fără site, fără 12 luni, pe conturile lui)

## Re-test

`founder/pitch-v1.md` = oferta inițială (0 din 20). `founder/pitch.md` = oferta nouă; panel „quick”, același seed (7), în `founder/panel/ (oferta v2; panelul ofertei inițiale e în founder/panel-v1/)`. Rezultatul: vezi `founder/panel/results.md` și `founder/summary.md`.
