# Brief pentru board: cinci variante de prim produs software în sănătatea preventivă (România, Bihor)

Brieful e scris pentru membri de board care nu au văzut conversația. Conține ideile și faptele din notele de cercetare, cu sursa (fișierul și secțiunea) în paranteză. Nu conține opinia analistului despre idei. Prețurile sunt ipoteze de testat.

## Fondatorul și constrângerile

- O persoană, cu un SRL în Bihor (Oradea). Rețele profesionale în Oradea și București.
- Competențe: Python, SQL, PL/SQL, Oracle APEX, backend web, arhitectură de date, AI/ML, API-uri LLM, agenți, n8n.
- Capital: ~25.000 EUR. Timp: 10–12 ore pe săptămână la început.
- Poate merge fizic la clienți. Preferă B2B SaaS cu venit recurent.
- Acces inițial limitat la medici, dosare medicale și seturi de date. Dispus la parteneriate cu organizații medicale.
- Ținta: un prim produs îngust care ajunge la **1.000–3.000 EUR venit recurent lunar (MRR)** înainte să fie nevoie de echipă, și care poate crește credibil spre sănătate preventivă/predictivă **fără** un model medical propriu care trebuie validat clinic.
- Software-ul care dă informații pentru decizii de diagnostic sau tratament la un pacient anume e dispozitiv medical clasa IIa sau mai mult în UE (Regula 11 MDR, fără excepție pentru „suport decizional transparent”). Clasa IIa costă aprox. 32–110k EUR și 9–18 luni (reglementare_ue_ro.md §2, estimare de pe blogul unui furnizor). Toate cele cinci idei de mai jos sunt gândite ca software administrativ (calendar, liste, mesaje, rapoarte), fără interpretare clinică.
- Pentru date de sănătate, fondatorul ar lucra ca persoană împuternicită (Art. 28 GDPR), clientul fiind operatorul (reglementare_ue_ro.md §1).

## Context de piață comun

- Programele românești de clinică și de cabinet nu publică API-uri; integrarea realistă e prin Excel/CSV, PDF, e-mail (romania_software_medicina_muncii.md §1).
- Clinicile mari (MedLife, Regina Maria, Medicover) își fac singure software-ul și decid IT-ul central (romania_piata.md §1, §7).
- România are cea mai mică cheltuială de sănătate pe locuitor din UE; partea privată (23%) e aproape toată din buzunar (romania_piata.md §5).
- Reminderele SMS cresc prezența la programări cu un efect mic dar sigur (RR 1,06–1,23) și sunt deja incluse în multe programe de cabinet; țintirea predictivă nu s-a dovedit mai bună decât reminderul pentru toți (follow_up_recall_dovezi.md §3).
- Apelurile automate pentru comunicări comerciale cer consimțământ prealabil (Legea 506/2004); profilarea cu date de sănătate cere consimțământ explicit sau o bază legală expresă (Legea 190/2018 art. 3) (romania_piata.md §3).
- Din 9 decembrie 2026, software-ul (inclusiv SaaS) e „produs” cu răspundere strictă după noua Directivă privind răspunderea pentru produse (reglementare_ue_ro.md §7).
- În Oradea s-au identificat cabinete independente de medicina muncii (Medimun, Carimed Center, Endodigest; plus Alfa Medica, Gecoprosana, Neoklinik doar în directoare), clinici independente cu boli cronice (GrandMed, NewMedics, Medena), un singur laborator independent (Humanamed) și ~527 de firme stomatologice; proprietatea și softul folosit nu au fost verificate (romania_software_medicina_muncii.md §5; romania_piata.md §7).

## Ideea A · Scadențar MM + portal pentru angajator (vândut cabinetelor independente de medicina muncii)

- **Ce este:** un add-on care importă din Excel sau din programul de medicina muncii (MM) lista angajaților fiecărui angajator-client și data ultimei fișe de aptitudine, arată ce expiră, trimite remindere (e-mail HR, SMS angajat cu consimțământ), și dă fiecărui angajator un portal cu marca cabinetului: în termen / depășit / recomandări „apt condiționat” deschise sau închise, fără diagnostice. Raport lunar.
- **Pentru cine:** cabinete și firme independente de medicina muncii din Oradea și Nord-Vest.
- **Preț ipotetic:** 59 EUR/lună (până la 2.000 de angajați urmăriți), 99 EUR/lună (până la 6.000), SMS la cost.
- **Fapte:**
  - Examenul periodic e obligatoriu pentru toți lucrătorii (HG 355/2007 art. 20), de regulă anual; angajatorul plătește tot; lipsa examenelor se amendează cu 4.000–8.000 lei pe abatere (Legea 319/2006 art. 39(4); suma trebuie reverificată pentru 2026) (romania_software_medicina_muncii.md §3).
  - Preț MM observat: 80 lei/angajat/an (110 pentru șoferi), Medworks București (romania_piata.md §5). Bihor: 187.300 de salariați (iunie 2025). Calculul analistului de cercetare: 15–21 mil. lei/an cheltuială teoretică pe examene periodice în Bihor (romania_software_medicina_muncii.md §3).
  - Cel puțin șase programe românești emit deja fișa de aptitudine (BizMedica MM/Setrio, MedExam, Qmedical, Charisma, MedSoft, Tempomed); BizMedica importă liste de angajați din Excel (romania_software_medicina_muncii.md §1).
  - MedLife oferă angajatorilor un portal self-service cu statusul examenelor MM în timp real și fișa în 24h (romania_software_medicina_muncii.md §1).
  - Cel mai mare furnizor MM din Bihor (Medicris, 22.000+ abonați) a fost cumpărat de MedLife în 2022 (romania_software_medicina_muncii.md §5).
  - Directorul Romedic listează 508 cabinete MM la nivel național (limită inferioară, nu recensământ) (romania_software_medicina_muncii.md §3).
  - Nu există niciun sondaj despre cum își urmăresc angajatorii scadențele și nicio dovadă că un cabinet independent plătește pentru un astfel de instrument (romania_software_medicina_muncii.md §3, Gaps).

## Ideea G · „Bucle deschise” (clinici independente de boli cronice, laboratoare, medici de familie)

- **Ce este:** din exportul zilnic al programului clinicii, o listă de lucru cu (1) controale scadente stabilite de medic și neprogramate, (2) rezultate marcate de laborator în afara intervalului fără consultație programată, (3) trimiteri emise fără răspuns. Mesaj neutru către pacient (cu consimțământ) cu link de programare, lista de sunat pentru asistentă, jurnal, raport lunar „bucle închise → consultații și analize”. Nu interpretează rezultate.
- **Pentru cine:** clinici independente multi-specialitate (diabet, cardiologie, endocrinologie), laboratoare independente, cabinete de medicină de familie.
- **Preț ipotetic:** 129 EUR/lună pe locație, SMS la cost; prima lună un audit gratuit pe 6 luni de date.
- **Fapte:**
  - În studii, rezultatele de laborator anormale nu sunt urmărite în 6,8–62% din cazuri, chiar și cu dosar electronic (Callen et al., JGIM) (follow_up_recall_dovezi.md §1).
  - Urmărirea cu un om care acționează funcționează mai bine decât alerta pasivă: 73,4% față de 52,2% pacienți evaluați într-un RCT (Murphy/Singh); e-mailul a determinat ~11% dintre medici să acționeze, telefonul peste două treimi (follow_up_recall_dovezi.md §2).
  - În România nu s-a găsit niciun proces documentat „laborator → medic → rechemare”; urmarea pare lăsată pe seama pacientului; rețelele mari construiesc interpretarea în aplicațiile proprii (romania_software_medicina_muncii.md §2).
  - Nu există măsurători românești ale golului de urmare și niciun preț românesc pentru unelte de rechemare (follow_up_recall_dovezi.md §1, §4, Gaps). Extrapolarea cercetătorului: 20–60 EUR/locație/lună plus SMS (follow_up_recall_dovezi.md §4). Unelte de rechemare dentară în SUA: 199–329 USD/locație/lună (competitori_b2b_infrastructura.md Q4).
  - Din T4 2026, furnizorii cu contract CNAS trebuie să folosească e-SănătateaMea pentru programări (romania_software_medicina_muncii.md §6).

## Ideea B · Scadențar MM vândut direct angajatorilor (HR)

- **Ce este:** același calendar de scadențe ca A, dar cumpărat de angajator, indiferent de furnizorul MM: import Excel, remindere angajați și șefi de tură, lista „de trimis la MM luna aceasta”, raport lunar, istoric. Fără date medicale: doar date de scadență și concluzia de pe fișă (pe care angajatorul o primește oricum, HG 355/2007 anexa 5).
- **Pentru cine:** HR, SSM sau director general la angajatori din Bihor cu 50–1.000 de angajați.
- **Preț ipotetic:** 39 EUR/lună până la 250 de angajați, 79 EUR/lună până la 1.000, SMS la cost.
- **Fapte:** obligația și amenzile sunt ale angajatorului (Legea 319/2006 art. 13 lit. j, art. 39(4)); amenzile sunt de ~40–100 de ori prețul MM pe angajat (calcul în romania_software_medicina_muncii.md §3). Constatări ITM frecvente: muncă fără examen, fișe lipsă (același §3). Nu există date despre cum programează angajatorii examenele (Excel, e-mail, telefon) (același §3, Gaps).

## Ideea K · Urmărirea pacienților de turism dentar (Oradea)

- **Ce este:** după faza 1 a unui implant, programarea protocolului post-tratament, check-in-uri în DE/IT/EN/HU (fotografii și chestionar trimise stomatologului, fără evaluare automată), planificarea ferestrei de călătorie pentru faza 2.
- **Pentru cine:** clinici dentare din Oradea care atrag pacienți străini.
- **Preț ipotetic:** 99–249 EUR/lună pe clinică.
- **Fapte:** clinicile din Oradea (Dental-Art, MaxiloMED, LifeDent, Estetical Dentis, German Dental) își fac reclamă la pacienți din IT, UK, AT, DE; peste 30.000 de turiști medicali străini în România într-un an; implanturi la 400–450 EUR în Oradea față de 560–600 EUR în Ungaria (metodologie neclară) (romania_piata.md §7). Volumul turismului dentar în Bihor e necunoscut (romania_piata.md §7, Gaps). Există deja vendori români de remindere dentare (VAstoma, DentAIM) (emergente_si_platitori.md §L) și iStoma declară 5.300 de stomatologi (romania_software_medicina_muncii.md §1).

## Ideea H · Rechemarea pentru pachetul CNAS de prevenție 40+/60+ (medici de familie)

- **Ce este:** din lista cabinetului, cine e eligibil după vârstă și data ultimei prevenții (nu după risc), invitații SMS/telefon/scrisoare, programare, urmărirea celor 3 consultații ale pachetului 40+, ajutor la raportare.
- **Pentru cine:** cabinete de medicină de familie cu contract CNAS.
- **Preț ipotetic:** 15–30 EUR/lună pe cabinet, sau modul vândut prin vendorul programului de cabinet.
- **Fapte:** din februarie 2026 serviciile de prevenție sunt gratuite pentru oricine e înscris la un medic de familie; 40+ are până la 3 consultații în 6 luni; 60+ adaugă evaluări pentru osteoporoză, incontinență, demență (romania_piata.md §5). Asistența primară primește doar 10% din cheltuiala de sănătate (romania_piata.md §5). Nu se știe cât plătește CNAS medicului per serviciu de prevenție (analiza_laterala.md O8). Programele de cabinet n-au API (romania_piata.md §2).

## Ce se cere de la board

Pentru **fiecare** dintre cele cinci idei: o notă 1–10, un vot (FUND / FUND IF / PASS), ce e puternic, ce ar ucide-o (top 3), întrebările pentru fondator, condițiile dacă e FUND IF. La final: care dintre cele cinci ar trebui să fie primul produs, din perspectiva lentilei tale.
