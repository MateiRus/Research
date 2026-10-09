# Oferta: Scadențar MM (founder-offer)

Metoda e lentila „Ofertă” din `founder-board/lenses.md`: un rezumat al unui cadru publicat, nu cuvintele autorului. Problemele vin din obiecțiile panelului simulat (`panels/A/results.md`, `panels/A2/results.md`) și din riscurile ridicate de board.

## Problemele, în cuvintele cumpărătorului (din panel și board)
1. „Programul meu MM îmi arată deja scadențele.”
2. „Asistenta ține un Excel care merge.”
3. „Angajatorii nu plătesc în plus; mă negociază la 80 de lei.”
4. „Îl plătesc din marjă.”
5. „Nu am timp să importăm și să curățăm datele.”
6. „Datele angajaților la un SRL necunoscut? Amenzi ANSPDCP.”
7. „Ce fac dacă firma dispare?”
8. „Angajatorul nu are voie să vadă nimic medical.”
9. „SMS-urile cer consimțământ.”
10. „Cine răspunde dacă scapă o scadență?”
11. „Nu-mi aduce clienți noi.”
12. „Vreau să-l văd la un cabinet pe care îl cunosc.”
13. „Vreau integrare directă, nu Excel.”
14. „Portalul arată «depășit» pentru cineva deja examinat?” (board, lentila Produs)
15. „Copiază BizMedica funcția în 6 luni.” (board, lentila Monopol)
16. „Nu-i convinge pe angajatorii mici, care nu cer portal.”

## Soluțiile (valoare pentru cumpărător / cost de livrare, 1–5)

| Soluție | Răspunde la | Valoare | Cost | Păstrată |
|---|---|---:|---:|---|
| Remindere automate către HR-ul clienților: asistenta nu mai sună | 2, 5, 11 | 5 | 1 | ✔ nucleu |
| Configurare la sediu, din exportul programului MM existent; actualizare săptămânală | 1, 5, 13, 14 | 5 | 3 | ✔ |
| Portal cu marca cabinetului: status în termen / expiră / depășit | 3, 11 | 4 | 2 | ✔ |
| Raport lunar de scadențe pe angajator (argument la renegociere) | 3, 11 | 4 | 1 | ✔ |
| Fără CNP, fără diagnostice; DPA și model de consimțământ gata făcute | 6, 8, 9 | 4 | 1 | ✔ într-o frază |
| Export complet oricând; date returnate la închidere | 7 | 3 | 1 | ✔ |
| Jurnal „cine a văzut ce”; marcarea manuală „examinat azi” | 10, 14 | 3 | 2 | ✔ |
| Garanție de 90 de zile cu returnarea banilor | 4, 12 | 4 | 2 | ✔ |
| Refacturarea portalului către angajatori (opțional) | 3, 4 | 3 | 1 | ✔ ca opțiune |
| Integrare API cu fiecare program MM | 13 | 5 | 5 | ✘ (nu există API; doar parteneriat ulterior) |
| Audit de securitate certificat | 6 | 3 | 5 | ✘ deocamdată (aliniere la controale, certificare mai târziu; REG §5) |

## Pachetul recomandat (v3, de testat cu oameni reali)
- **Nucleul (rezultatul, nu ingredientele):** „Asistenta dumneavoastră nu mai sună angajatorii: fiecare client își vede singur scadențele, cu marca cabinetului, și primește remindere la timp.”
- **Bonusuri:**
  - (1) configurarea la sediu, din exportul existent;
  - (2) raportul lunar pentru renegocierea anuală;
  - (3) modelele de DPA și consimțământ, gata făcute.
- **Garanția:** 90 de zile, cu returnarea banilor. Costul la o rată estimată de 1 din 5 clienți care cer banii înapoi e de ~3 × 65 € / 5 ≈ 39 € pe client. Acceptabil la o contribuție de 61 €/lună (calculul meu, pe cifrele din `cfo/`).
- **Urgența (reală):** doar 5 cabinete pilot în primul semestru, pentru că fondatorul poate integra ~1 cabinet pe lună. Pilotii păstrează prețul 24 de luni.
- **Numele:** „Scadențar MM”, cu „portal pentru angajatori” ca subtitlu.
- **Prețul:** 39 / 79 / 149 € (`pricing/pricing.md`).

## Ecuația valorii (1–10, estimarea mea): v1 → v3
- **Rezultatul dorit:** 6 → 7, prin raportul pentru renegociere și portalul cu marca proprie.
- **Probabilitatea percepută:** 4 → 6, prin garanție și configurarea la sediu. Va urca la 8 doar cu o referință reală.
- **Timpul până la rezultat:** 6 → 8, prin configurarea făcută de fondator.
- **Efortul cerut:** 5 → 8. Asistenta nu mai exportă și nu mai sună.

## Retestarea (panel simulat, aceleași cărți, seed 2026)
- **v1** (remindere + portal, 59/99 €): **7/20 (35%)**.
- **v2** (paritate cu rețelele, paragraf lung despre date, 35/69/129 €, garanție): **3/20 (15%)**. Au plecat 2 dintre cei cu „Excel și hârtie”, medicul ocupat și cel care caută noutăți, mai ales pe încredere.
- **Lecția:** reminderele care economisesc timpul asistentei vând mai bine decât portalul. Datele se spun într-o frază sigură, nu într-un paragraf care sperie. **v3 combină nucleul din v1 cu configurarea și garanția din v2.** N-a fost retestată în panel, pentru că următorul test trebuie făcut cu cabinete reale.
