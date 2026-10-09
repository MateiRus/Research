# Concurența pentru primele trei idei (A, G, B)

**Limita acestui pas.** Skill-ul `founder-competitors` cere surse publice citite acum, cu link, inclusiv recenziile clienților. Sarcina interzice cercetarea web nouă, așa că **toate rândurile vin din notele de cercetare** (coloana `note_source` din `competitors.csv`), cu link-urile citate acolo. **Pasul 3 (recenziile, 1–3 stele) nu s-a putut face:** notele nu conțin recenzii pentru niciunul dintre acești concurenți. În locul lor folosesc obiecțiile din panelul de cumpărători, marcate ca simulate. Nu am inventat niciun concurent, preț sau rating.

## 1. Tabelul, după cât de direct concurează

### A · Scadențar MM + portal angajator (prin cabinete independente)

| Concurent | Tip | Preț comparabil | Ce vinde | Sursa |
|---|---|---|---|---|
| BizMedica MM (Setrio) | direct | nepublicat (versiunea pentru medicina de familie: 159–199 RON/lună, preț vechi) | fișa de aptitudine, dosarul, **import Excel** al angajaților | RSMM §1; RO §2 |
| MedExam (DMV Consult) | direct | nepublicat | cabinet MM fără hârtie, rapoarte | RSMM §1 |
| Qmedical | direct | nepublicat | firmele-client, posturile pe risc, rapoarte | RSMM §1 |
| Charisma (modul MM) | direct | nepublicat | fișa, evoluția angajatului | RSMM §1 |
| MedSoft (modul MM) | direct | ofertă la cerere | modul MM | RSMM §1 |
| **MedLife Self-Service + MM Express** | indirect (rețea) | inclus | **portal angajator** cu statusul MM în timp real; fișa în 24h | RSMM §1 |
| Regina Maria MM Oradea | indirect (rețea) | nepublicat | MM cu programare online | RSMM §5 |
| Urmărirea scadențelor ca serviciu (One Medicina Muncii, HARDMED, M Hospital) | indirect | inclus în 80–110 lei/angajat/an | evidență digitală, urmărirea scadențelor | RO §5 |
| Excel + telefonul asistentei | substitut | 0 € | — | panel A |

### G · Bucle deschise (clinici cronice)

| Concurent | Tip | Preț comparabil | Ce vinde | Sursa |
|---|---|---|---|---|
| MediNote | indirect | 50 lei/utilizator/lună, cu SMS inclus | program de clinică cu remindere | RO §2 |
| icMED + icMED.Mobile | indirect | nepublicat | program de clinică cu aplicație pentru pacient | RSMM §1 |
| Zarina CRM Medical | indirect | 2.990 € + TVA, licență unică (licența CRM generală) | CRM cu WhatsApp/SMS și automatizări | RSMM §1 |
| VAstoma, DentAIM, AI Frontdesk | indirect | nepublicat (agenți vocali români ~299–499 €/lună) | remindere WhatsApp și apeluri AI | EMG §L, Q3 |
| Callio | indirect | 139/189/299 €/lună | agent vocal la recepție | RO §2 |
| receptie-clinica.ai | indirect | 1.200 € setup + 150 €/lună | recepționist AI | RO §2 |
| Asistentul AI MedLife, Synevo Decoder, aplicația Regina Maria | indirect (rețele, nu se vând independenților) | inclus | interpretarea rezultatelor, la inițiativa pacientului | RSMM §2 |
| e-SănătateaMea | substitut (stat) | gratuit | programări obligatorii pentru furnizorii CNAS din T4 2026 | RO §4; RSMM §6 |
| Lighthouse 360 (SUA) | doar ancoră de preț | 329 $/lună + 299 $ setup | rechemare dentară legată de PMS | B2B Q4 |
| Asistenta cu telefonul / pacientul revine singur | substitut | 0 € | — | panel G |

### B · Scadențar MM direct la HR

| Concurent | Tip | Preț | Sursa |
|---|---|---|---|
| Excel + furnizorul MM care anunță scadențele | substitut | 0 € | panel B; RO §5 |
| MedLife Self-Service (pentru clienții MedLife) | indirect | inclus | RSMM §1 |
| Platforme HR/salarizare cu evidența fișelor | indirect | **neverificat**: notele nu le documentează | — |

## 2. Intervalul de preț pentru produsul comparabil

- **A:** **niciun preț publicat pentru software de medicina muncii** (RSMM §1, Gaps). Cele mai apropiate ancore sunt programele de clinică:
  - MediNote, ~10 €/utilizator/lună (50 lei);
  - BizMedica pentru medicina de familie, ~31–39 €/lună (preț vechi);
  - Zarina, 2.990 € licență unică, adică ~83 €/lună pe 3 ani (calculul meu).
  - **Cel mai mic ~10 €, median ~35 €, cel mai mare necunoscut.**
- **G:** de la ~10 € (reminder inclus în MediNote) la 24–59 € (AllAI; RO §2), 139–299 € (Callio), 150 € plus setup (receptie-clinica.ai) și 299–499 € (agenți vocali; EMG Q3). **Mediana ancorelor românești e ~150 €/lună**, dar acestea sunt agenți vocali la recepție, nu liste de rechemare.
- **B:** 0 € (Excel, serviciul inclus de furnizorul MM).

## 3. Harta de poziționare (în text)

**A:** axa X = cine deține relația cu angajatorul (rețea ↔ cabinet independent); axa Y = ce vede angajatorul (doar fișa pe hârtie sau PDF ↔ portal de status la zi).
- **Sus-stânga:** MedLife (rețea, cu portal).
- **Jos-dreapta:** cabinetele independente cu BizMedica MM, MedExam, Qmedical, Charisma sau MedSoft. Notele nu documentează un portal pentru angajator la niciunul dintre aceste programe; **trebuie verificat** la vendori.
- **Mijloc:** furnizorii care vând urmărirea scadențelor ca serviciu.
- **Golul:** sus-dreapta, adică un cabinet independent cu portal pentru angajator.

**G:** axa X = reactiv (reminder la o programare care există deja) ↔ proactiv (găsește pacientul care n-a programat nimic); axa Y = integrat în programul clinicii ↔ separat.
- MediNote și icMED: integrat, reactiv.
- VAstoma, DentAIM, Callio, AI Frontdesk: separat, reactiv (recepție, apeluri).
- Rețelele: proactiv, dar doar pentru pacienții lor și la inițiativa pacientului.
- **Golul:** proactiv, pentru clinici independente, pe termene stabilite de medic.

## 4. Plângerile (în locul recenziilor)

Notele n-au recenzii pentru acești concurenți. Obiecțiile din panelurile simulate (`panels/*/results.md`) sunt cel mai apropiat substitut. **Nu sunt recenzii reale.** Ordonate după frecvență:
- **A:** „programul MM/Excel-ul îmi arată deja scadențele” (6/13 refuzuri); încrederea în date și teama de amenzi ANSPDCP (4/13); prețul și „nu aduce bani imediat” (2/13).
- **G:** încrederea în date și teama de amenzi GDPR (7/20); „programul trimite deja SMS” (6/20); prețul față de capitație la medicii de familie (3/20); exportul zilnic pe care nimeni nu știe să-l facă (2/20).
- **B:** „Excel și furnizorul MM ne anunță” (10/18); „nu e o problemă reală” (5/18).

## 5. Golul

- **A:** un **portal pentru angajator cu marca cabinetului independent**, alimentat din programul MM existent. E legat de dovezi: MedLife vinde exact asta (RSMM §1), iar cabinetele independente concurează fără echivalent (RSMM §3, Inferences). **Condiție:** să fie confirmat că BizMedica MM, MedExam și ceilalți nu-l au deja. Altfel golul nu există.
- **G:** **găsirea pacienților care n-au mai programat controlul** stabilit de medic. N-a fost documentat niciun produs românesc (RSMM §2, Inferences). Golul există ca produs, dar **cererea pentru el nu e demonstrată**: în panelul v1, 0/20.
- **B:** **nu există un gol vizibil**. Substitutul gratuit (Excel plus furnizorul MM) e suficient pentru 18 din 20 de cumpărători simulați.

## 6. Cine ar copia cel mai repede

- **A:** **Setrio (BizMedica MM)** și **DMV Consult (MedExam)**. Au deja datele și clienții. Un portal de status e pentru ei o funcție, nu un produs. Apărarea fondatorului e viteza de onboarding, relația locală și un parteneriat cu un vendor (vânzarea prin el), nu tehnologia.
- **G:** **MediNote sau icMED** pot adăuga un raport „controale scadente” peste datele pe care le au deja. Vendorii de recepție AI (Callio, VAstoma) pot adăuga apeluri de rechemare.
