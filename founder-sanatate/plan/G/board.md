# Rezumatul președintelui de board

**Cum a rulat.** Trei membri de board, fiecare un sub-agent separat (`claude -p`, model opus, fără unelte). Fiecare a primit doar `brief.md` și o singură lentilă din `founder-board/lenses.md`. Lentilele sunt rezumate ale unor cadre publicate; membrii nu vorbesc în numele autorilor. Memoriile complete sunt în `offers.md`, `monopoly.md` și `product.md` (lentila „Monopol” a răspuns în engleză, deși i s-a cerut româna; textul e păstrat neschimbat). Board-ul **nu** a văzut rezultatele panelului de cumpărători (au rulat în paralel).

## 1. Votul

| Idee | Ofertă | Monopol | Produs | Media | Voturi |
|---|---:|---:|---:|---:|---|
| **A** Scadențar MM + portal angajator (prin cabinete) | 6 FUND IF | 5 FUND IF | 6 FUND IF | **5,7** | 3 × FUND IF |
| **G** Bucle deschise (clinici cronice, laboratoare, MF) | 7 FUND IF | 6 FUND IF | 5 FUND IF | **6,0** | 3 × FUND IF |
| **B** Scadențar MM direct la HR | 4 PASS | 3 PASS | 7 FUND IF | 4,7 | 2 PASS, 1 FUND IF |
| **K** Turism dentar | 5 FUND IF | 3 PASS | 4 PASS | 4,0 | 2 PASS, 1 FUND IF |
| **H** Rechemare CNAS 40+/60+ | 3 PASS | 3 PASS | 3 PASS | 3,0 | 3 × PASS |

**Recomandarea fiecărei lentile pentru primul produs:**
- **Ofertă:** G, apoi A.
- **Monopol:** G, apoi A.
- **Produs:** B, apoi A. A e „același nucleu, cu datele venite de la cine emite fișa”.

**A e singura idee pe care toți trei o pun în primele două.**

## 2. Riscurile ridicate de mai mulți membri (primele)

1. **Piața locală e prea mică pentru ținta de MRR** (A, G, B; toți trei). În Oradea sunt ~6 cabinete MM independente, ~3 clinici cronice și 1 laborator. La 59–129 EUR, pentru 1–3k EUR MRR sunt necesari 8–50 de clienți, deci vânzare în tot Nord-Vestul sau la nivel național din primul an.
2. **Copierea în luna 6 / funcția devine o bifă** (A: toți trei; B: Ofertă și Monopol). Cele 6 programe MM existente (BizMedica importă deja Excel) și portalul MedLife pot închide golul.
3. **Lipsa dovezilor locale de plată și de durere** (A, G; toți trei). Nu există sondaj, măsurătoare sau pre-vânzare.
4. **Cusătura de date: fără API, totul depinde de exporturi** (A: Produs și Monopol; G: Ofertă și Produs). Un portal care arată „depășit” pentru cineva deja examinat distruge încrederea.
5. **Granița MDR la bucla „rezultat în afara intervalului”** (G: Monopol și Produs). Cere o opinie scrisă de reglementare înainte de a fi construită.
6. **H: cumpărătorul n-are bani și statul poate absorbi funcția** (toți trei).

## 3. Condițiile, unite într-o listă de verificat

- [ ] **A:** 3 cabinete independente semnează pre-vânzări plătite **înainte** de construcție (toți trei). → verificat parțial în panel (simulat); confirmare reală în validarea de 90 de zile.
- [ ] **A:** o listă verificată cu ≥20 de cabinete independente accesibile în Nord-Vest (Monopol). → validarea de 90 de zile.
- [ ] **A:** confirmarea că BizMedica MM, MedExam etc. **nu** au deja un portal pentru angajator (Ofertă). → nu se poate din note; de întrebat vendorii și cabinetele.
- [ ] **A:** v1 face un singur lucru: statusul în termen / depășit, actualizat cel puțin săptămânal (Produs). → integrat în oferta v2.
- [ ] **A:** oferta reformulată în jurul păstrării și câștigării angajatorilor, cu o garanție (Ofertă). → integrat în oferta v2 (garanție de 90 de zile).
- [ ] **G:** 2 audituri reale pe 6 luni de date, cu recuperări de cel puțin 5 ori prețul, și o conversie la plată (Ofertă, Monopol, Produs).
- [ ] **G:** importul demonstrat fără muncă manuală zilnică (Ofertă). → integrat în oferta v2 (export automat configurat de fondator).
- [ ] **G:** v1 tăiat la o singură buclă, „controale scadente neprogramate”, pentru un singur tip de client (Produs). → oferta v2.
- [ ] **G:** opinie de reglementare scrisă înainte de bucla de laborator (Monopol, Produs).
- [ ] **B:** cel mult canalul angajatorului pentru A, nu produs separat (Ofertă, Monopol). Dacă e testat: 5 pre-vânzări și un flux de actualizare de un clic după examen (Produs).
- [ ] **K:** volumul de pacienți străini pe clinică și 2 pre-vânzări (Ofertă). Altfel PASS.
- [ ] **H:** niciuna; PASS unanim.

## 4. Cea mai puternică versiune pe care o vede board-ul

Board-ul nu vede cinci afaceri, ci **un singur motor**: o listă de termene stabilite de un profesionist (medicul MM, medicul curant), ținută la zi din exporturile programelor existente, cu un om care acționează și un jurnal. Motorul are **două uși de intrare**:

- **Ușa A** (cabinetele MM independente, cu portal pentru angajator) e cea mai rapidă la bani. Cumpărătorul e numărabil și accesibil fizic, iar motivul de cumpărare e concret: paritatea cu portalul MedLife. Datele nu sunt clinice, iar riscul de reglementare e minim.
- **Ușa G** (controalele scadente la clinicile de boli cronice) e cea mai valoroasă strategic. Duce direct spre prevenție, iar know-how-ul de integrare cu programe fără API devine o barieră. Dar golul e nedemonstrat în România, iar oferta inițială n-a convins pe nimeni din panel.

B nu e o afacere separată, ci partea de angajator a lui A. K și H nu trec.

**Dezacordul real:** lentilele Ofertă și Monopol ar începe cu G pentru valoare și secret. Lentila Produs ar începe cu forma cea mai simplă (B, apoi A). Panelul de cumpărători (§C3 în `analiza_founder.md`) înclină balanța spre A ca prim produs. Și varianta propusă aici diferă de ce a fost propus: nu „un produs de medicina muncii” și nici „un produs de rechemare”, ci un motor comun, cu A ca primă ușă și G ca a doua, deschisă doar după un audit real.
