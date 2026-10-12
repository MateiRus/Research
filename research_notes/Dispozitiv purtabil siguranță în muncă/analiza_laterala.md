# Analiză laterală: dispozitivul purtabil pentru siguranța în muncă

**Data:** 12 octombrie 2026
**Statut:** **ideație și deducție, nu dovezi.** N-am făcut cercetare web nouă. Faptele vin din raportul final și din cele 7 note ale cercetării și sunt citate ca atare. Orice idee, legătură sau cifră nouă de aici e o **[estimare]**, chiar și acolo unde nu repet eticheta la fiecare rând.

---

## 0. Cum să citești documentul

**Ce conține.** Am aplicat pachetul de gândire laterală „lateral-thinking” peste cercetarea existentă, ca treceri separate:
- **A. Concept fan** (evantaiul de concepte, Edward de Bono): urc de la soluție la scopul pe care îl servește, apoi cobor la alte soluții.
- **B. Inversarea presupunerilor**: răstorn presupunerile planului și caut unde varianta răsturnată e deja adevărată.
- **C. Provocarea („Po”)**: afirmații absurde făcute intenționat, din care scot „mișcare” (o idee nouă), nu judecată.
- **D. Analogia forțată**: mut mecanisme din domenii îndepărtate (aviație, biologie, transport rutier, viață socială).
- **E. Cea mai proastă idee** (brainstorming invers): proiectez dezastre, le găsesc mecanismul și răstorn mecanismul.
- **F. SCAMPER, pe scurt** (șapte transformări ale unei idei existente: înlocuiește, combină, adaptează, modifică, altă folosință, elimină, inversează), ca să generez variantele de produs.
- **G. Cele șase pălării** (șase perspective separate: fapte, emoții, riscuri, beneficii, alternative, sinteză) pe decizia „ce testez întâi”.
- Apoi secțiunile cerute: 1 Pe scurt, 3 Reformulări și plătitori, 4 Variante de produs, 5 Riscuri, 6 Recomandare. Secțiunea 2 este formată din trecerile A–G.

**Despre rutare.** Orchestratorul `lateral` recomandă o singură tehnică pe trecere. Cererea a fost pentru cel puțin cinci, deci le-am rulat ca treceri separate, fiecare cu pașii ei și cu mecanismele ei de onestitate: ramuri tăiate, inversări moarte, provocări fără mișcare, analogii abandonate, mecanisme moarte. Am sărit peste `random-stimulus` (stimul aleator), pentru că problema nu era că ideile seamănă între ele. Am sărit și peste `post` (postări pe rețele sociale), care nu se potrivește aici.

**Cum citez.** Formatul este `(fișier §secțiune)`. Prescurtările de fișiere:
- **RAP**: `reports/Dispozitiv purtabil siguranță în muncă.md` (raportul final);
- **N00**: `00_prompt_si_context.md`;
- **N01**: `01_problema_statistici_costuri.md`;
- **N02**: `02_cadru_legal_ssm_gdpr_mdr_atex_ai.md` (secțiunile sunt numerotate „Întrebarea 1…11”, citate ca Î1…Î11);
- **N03**: `03_piata_concurenti.md`;
- **N04**: `04_hardware_conectivitate.md`;
- **N05**: `05_clienti_pret_canale_riscuri.md`;
- **N06**: `06_finantare.md`;
- **PA2**: `plan-de-afaceri-v2.md` (din rădăcina repo-ului, pentru regula DR-36).

**Atenție la calitatea surselor.** Notele spun singure că toate faptele vin din rezumatele motorului de căutare, nu din pagini citite integral (RAP, „Limita metodei”). Citările de aici moștenesc aceeași limită.

**Prescurtări folosite des** (explicate și la prima apariție în text):
- SSM = securitate și sănătate în muncă;
- ITM = Inspectoratul Teritorial de Muncă;
- HG = hotărâre de guvern;
- ARC = Alarm Receiving Centre, adică dispecerat care primește alarmele 24/7;
- GDPR = regulamentul UE de protecție a datelor;
- DR-36 = finanțarea LEADER primită de ILLUSTRUS, cu obligația de venit din servicii.

**Fondatorul (constrângerile aplicate peste tot).**
- ILLUSTRUS S.R.L., Oradea, CAEN 6310 (prelucrarea datelor, hosting, portaluri web).
- Student în anul 2 la ASE, junior Oracle APEX/PL-SQL. Știe Python, SQL, n8n (automatizări), LLM-uri (modele mari de limbaj) și WordPress.
- Lucrează 10–12 ore pe săptămână și are circa 25.000 EUR.
- Nu construiește hardware.
- Are de făcut ≥10.000 EUR venit din servicii web pentru DR-36 (pragul e 30% din prima tranșă, verificat probabil pe CAEN-ul finanțat) (PA2 §A.1).

---

## 1. Pe scurt (cele mai bune idei noi)

1. **Pentru patron, partea cea mai valoroasă a produsului e dovada, nu brățara** [estimare]. Patronul cumpără protecție împotriva dosarului penal: administratorii primesc 1,5–2,7 ani cu suspendare după un deces, iar amenzile sunt mici (N01 §7). Un jurnal care arată cine a lucrat singur, unde, până la ce oră, ce verificări au avut loc și cât a durat răspunsul îi servește pe patron, pe auditor și pe ITM. Detectarea automată a căderii e doar unul dintre senzorii acestui jurnal. Patru tehnici au ajuns aici independent (A, B, C, D).
2. **„Planul de lucru izolat” cu termen, după modelul planului de zbor** [estimare]. Lucrătorul anunță prin SMS sau apel „intru în căminul 3, ies în 40 de minute”. Dacă nu confirmă ieșirea, sistemul îl sună, apoi sună șeful de echipă, apoi dispecerul. Nu cere niciun dispozitiv, merge pe orice telefon și răspunde exact definiției din HG 1091/2006: fără contact, de regulă peste o oră, fără ajutor imediat (N02 Î2).
3. **Colegul înaintea dispecerului.** În pădure, echipa e la 50–200 m (N02 Î2, deducții). Alarma merge întâi la cel mai apropiat coleg și abia apoi la dispecer. Modelul există deja: Vatix are „auto-monitorizare”, cu alarma trimisă direct la oamenii clientului (N05 §6), iar Safe Alone din Cluj trimite SMS unui coleg (N03 §3). Dispeceratul plătit (circa 2,50 EUR pe lucrător pe lună în calcul) devine treapta a doua [estimare].
4. **Vinde intermediarilor, nu fiecărui angajator** [estimare]. Serviciile externe SSM scriu evaluarea riscurilor și pot „prescrie” soluția (N05 §2). Un comision de 15% egalează onorariul lor întreg pe acel lucrător (N05 §5). Firmele de pază au deja dispecerat 24/7 și proceduri pentru alarme false (N05 §5). Ca produs white-label (sub marca lor), varianta pentru firmele de pază scoate fondatorul din lanțul de alarmă. Tot ea face din cel mai probabil copiator (N05 §5) un client.
5. **Un produs de software care contează probabil ca venit DR-36** [estimare, de confirmat cu GAL-ul (grupul de acțiune locală)]. Portalul de conformitate pentru lucrul izolat și consola de dispecerat vândute firmelor SSM sau de pază sunt servicii web și de hosting (CAEN 6310). Vânzarea de abonamente cu dispozitive și dispecerat amestecă în schimb hardware și servicii de monitorizare (PA2 §A.1: verificarea pare făcută pe CAEN-ul finanțat).
6. **GPS-ul de flotă ca dispozitiv deja plătit** [estimare, idee nouă, nevalidată]. Utilitățile și firmele forestiere plătesc deja circa 50 lei pe lună pe vehicul pentru GPS (N05 §3). Un modul „lucrător departe de mașină prea mult timp” vândut prin furnizorii de GPS de flotă ar avea un canal cu clienți existenți.
7. **Vinde în calendarul ITM.** Campaniile ITM pe sector (de exemplu ITM Sibiu, silvicultură 2026, N02 Î2) și momentele de după un accident din zonă sunt ferestrele de cumpărare. Materialul „lucrător izolat: ce cere HG 1091 și cum dovedești la ITM” (N05 §7, deducții) devine instrumentul de vânzare al firmelor SSM [estimare].
8. **Riscul principal s-a mutat.** Inversiunea și „cea mai proastă idee” arată același mecanism: varianta din raport îl pune pe fondator să poarte riscul (răspundere, capital în dispozitive, alarmă 24/7) înainte ca clientul să vadă valoarea. Testele recomandate (secțiunea 6) inversează ordinea: întâi canal și dovadă, apoi dispozitive [estimare].

---

## 2. Tehnicile aplicate

### A. Concept fan (evantaiul de concepte)

**Ce am făcut.** Am pornit de la soluția din raport și am întrebat de două ori „la ce servește asta?”. La fiecare treaptă am întins 3–4 concepte alternative, apoi am coborât la produse concrete.

**Ținta (soluția actuală).** Un tracker certificat cu detectare de cădere și imobilitate, buton SOS și locație, plus o platformă și un dispecerat externalizat, vândute ca abonament de 12–20 EUR pe lucrător pe lună, întâi utilităților din Bihor (RAP §1, §7).

**Urcarea.**
- **Treapta 1: la ce servește trackerul?** Să scurteze timpul până la ajutor pentru cineva pe care nu-l vede nimeni. Titlul raportului e chiar „Vinde timpul până la ajutor, nu brățara” (RAP).
- **Treapta 2: la ce servește scurtarea timpului?** Angajatorul să-și îndeplinească, **și să poată dovedi că și-a îndeplinit**, datoria de grijă față de lucrătorii nevăzuți. Legea 319/2006 cere evaluarea riscurilor, primul ajutor și legătura cu urgențele, iar HG 1091/2006 cere informarea despre „sistemul de supraveghere și de legătură cu exteriorul” (N02 Î1, Î2; textul exact al art. 10–11 e de verificat). Pentru patron, partea „dovedită” contează cel mai mult: costul dominant e penal și personal (N01 §7, deducții).
- M-am oprit aici. A treia treaptă („siguranță în general”) ar fi prea largă.

**Evantaiul la treapta 1: alte moduri de a scurta timpul până la ajutor.**
- a) **Eliminarea izolării prin organizare**: perechi, programarea lucrărilor cu risc, regula „niciodată singur” din ghidul forestier al Inspecției Muncii (N02 Î2). E ramură evidentă, dar validează harta, pentru că e soluția pe care o cere deja legea.
- b) **Verificare programată (check-in)**: lucrătorul confirmă la intervale sau la finalul unei sarcini, iar lipsa confirmării pornește escaladarea. Nu cere dispozitiv. Peoplesafe vinde „check-in” ca opțiune de 0,25 GBP pe lună (N05 §4), iar nota sugerează „check-in programat” pentru pădure (N05 §1, deducții).
- c) **Răspuns de la colegi** (alarma la cel mai apropiat coleg, nu la centru) (N05 §6 Vatix; N03 §3 Safe Alone).
- d) **Detectare automată pe corp** (soluția originală).
- *Tăiată:* „un tracker mai bun / cu baterie mai mare” e originalul vopsit altfel.

**Evantaiul la treapta 2: alte moduri de a îndeplini și dovedi datoria de grijă.**
- a) **Dosarul de diligență** (diligență = grija cerută de lege, care poate fi dovedită): evaluare, procedură de salvare, instruiri semnate, registrul turelor izolate, rapoarte de test. Lista A–F din raport (RAP §5) e deja un astfel de dosar, doar că acolo apare ca efort de implementare, nu ca produs.
- b) **Exercițiul de salvare ca serviciu**: o alarmă de test pe lună pe echipă, cu cronometru și raport semnat. Raportul are deja „o alarmă de test pe săptămână” ca măsurătoare de pilot (RAP §6); aici testul devine chiar livrabilul.
- c) **Transferul riscului**: asigurare sau garanție. În România nu există bonus-malus (prime mai mici pentru firmele fără accidente) la CAM (contribuția asiguratorie pentru muncă, de 2,25%) (N06 §1). Ramura e slabă azi.
- d) **Eticheta sau certificatul „lucru izolat controlat”** pentru antreprenorii care concurează la licitații sau lucrează pentru clienți cu audit ISO 45001 (standardul de management SSM). Notele nu au găsit cerințe de acest tip în România (N01 §7, lipsuri). Ramura e speculativă.

**Coborârea la produse (ramurile promițătoare).**
- **Din 1b (check-in):**
  - un SMS sau apel robotizat de tip IVR (răspuns vocal automat: „apasă 1 dacă ești bine”) la ora anunțată, cu escaladare;
  - un „plan de lucru izolat” deschis printr-un SMS cu cod („C3 40”);
  - o aplicație Android simplă, cu temporizator.
- **Din 1c (colegi):**
  - lanțul de alarmă coleg → șef de echipă → dispecer;
  - aceleași trackere, dar alarma merge întâi pe telefonul colegului.
- **Din 2a (dosar):**
  - un portal APEX pentru firmele SSM externe care generează lunar dosarul de lucru izolat al fiecărui client, cu textele redactate de un LLM în afara lanțului de alarmă;
  - un raport lunar pentru administrator: „X ture izolate, Y verificări, Z minute timp mediu de răspuns la test”.
- **Din 2b (exercițiu):** un pachet „test lunar de salvare”, vândut prin firma SSM, cu proces-verbal.

**Ramurile evidente.** 1a (organizarea) și 1d (originalul) le-ar fi găsit oricine. Ele validează evantaiul, dar nu sunt câștigul lui.

**Meta-tiparul.** Soluția originală optimizează **acuratețea detectării** (cădere, imobilitate, alarme false). Toate ramurile vii optimizează însă **cunoașterea programului**: cine e singur, unde, până când. Odată ce știi asta, „nu a confirmat la timp” e un semnal de alarmă la fel de bun ca „a căzut” pentru multe cazuri: cămin, stație de pompare, tură de noapte. Și e mult mai ieftin. Dispozitivul rămâne necesar unde omul își pierde cunoștința în câteva secunde și nimeni nu știe unde e: căderi, utilaj răsturnat, gaze. Au același răspuns și decesele din cauze medicale, de 11 la 4 în exemplul ITM Prahova (N01 §3).

**Clasament onest.**
- Cel mai puternic: 2a (dosarul de diligență) combinat cu 1b (check-in). Îl poate construi fondatorul, nu cere hardware și îl poate vinde un intermediar.
- Al doilea: 1c (colegii întâi), care scade costul dispeceratului, dar cere încredere în colegi. În Germania, sistemele pentru lucru singur periculos cer o centrală de recepție permanentă (N02 Î2, DGUV), deci clienții cu capital german pot respinge varianta.
- Slab: 2c (asigurarea), pentru că lipsește mecanismul în România. Speculativ: 2d (eticheta).

---

### B. Inversarea presupunerilor

**Ce am făcut.** Am listat opt presupuneri pe care stă planul din raport, am răsturnat fiecare în opusul ei plauzibil și am căutat unde opusul e **deja adevărat** și cine câștigă din el.

**1. Clientul e angajatorul final.**
- *Răsturnat:* clientul e un intermediar (firma SSM, firma de pază, antreprenorul general, furnizorul de GPS de flotă), care revinde sau include serviciul.
- *Unde e adevărat:*
  - Axpo (Elveția), o utilitate, vinde altora serviciul de lucrător singur cu centru de apel 24/7 (N03 §4);
  - Peoplesafe crește prin parteneriate cu asociații (Make UK, NFU, Safecontractor) (N03 §2; N05 §5);
  - Blackline intră pe piețe noi prin distribuitori (N05 §6).
- *Viu.*

**2. Valoarea e în detectarea automată.**
- *Răsturnat:* valoarea e în procedură și în dovadă, iar detectarea poate fi manuală (check-in).
- *Unde e adevărat:*
  - circa 20–25% din piața europeană e deja pe aplicații, în creștere (N05 §4);
  - INRS (institutul francez de securitate în muncă) spune că alarma pentru lucrătorul izolat se folosește doar într-o procedură de salvare validată și „nu răspunde singură” obligațiilor angajatorului (N02 Î2).
- *Viu.*

**3. Alarma o primește un dispecer profesionist 24/7.**
- *Răsturnat:* o primește întâi un coleg sau șeful de echipă.
- *Unde e adevărat:* Vatix, opțiunea de auto-monitorizare (N05 §6), și Safe Alone, cu SMS la coleg (N03 §3).
- *Limita:* DGUV (asigurătorul german de accidente) cere o centrală de recepție la lucrul singur periculos (N02 Î2).
- *Viu pentru riscul mediu*: cămine cu echipă la suprafață, ture de noapte în stații. *Mort pentru riscul înalt.*

**4. Lucrătorul e obstacolul (refuzul de 46–59%).**
- *Răsturnat:* lucrătorul sau sindicatul cer produsul și îl folosesc ca protecție proprie.
- *Unde e adevărat:*
  - NFU (uniunea fermierilor din UK) îl cumpără pentru membrii ei, care adesea lucrează pe cont propriu (N05 §5);
  - lucrătorii acceptă tehnologii „cu beneficiu direct de siguranță”, cum sunt alertele de pericol (N05 §6, USACE și Alabama);
  - pădurarii agresați (157 în 5 ani la Romsilva, N03 §7) au un motiv propriu să vrea un SOS.
- *Pe jumătate viu.* Nu am găsit nicio poziție a sindicatelor românești despre purtabile (N05 §6), deci varianta „sindicatul cere” nu are dovezi. Varianta „lucrătorul plătește” e *moartă*: nimic din note nu o susține.

**5. Plata e lunară, pe lucrător.**
- *Răsturnat:* plata e pe proiect sau pe șantier, pe tură izolată ori pe eveniment.
- *Unde e adevărat:*
  - raportul spune deja „vinzi pe șantier, nu pe firmă” (RAP §1);
  - în G-Cloud, Peoplesafe închiriază dispozitivele și le ia înapoi la final (N05 §4);
  - caietele de sarcini românești de pază includ un număr de alarme false în tarif (N05 §2).
- *Viu pentru construcții*, unde proiectele au termen.

**6. Asigurarea nu ajută.**
- *Răsturnat:* asigurătorul plătește sau reduce prima.
- *Unde e adevărat:* doar în Italia, prin INAIL OT23 (asigurătorul public italian, reducere de 5–28% pe punctaj) (N05 §5).
- *În România e mort:* CAM e fix, fără clase de risc (N06 §1), iar asigurătorii privați nu publică reduceri (N05 §3, §5). **Aceasta e presupunerea care supraviețuiește inversării.** Nu pierde timp pe argumentul „vă scade asigurarea” până nu se schimbă legea.

**7. Produsul se vinde pentru că salvează vieți.**
- *Răsturnat:* se vinde pentru că îl apără pe patron.
- *Unde e adevărat:* nota de costuri spune explicit că argumentul cel mai puternic este riscul penal personal al administratorului și dovada diligenței (N01 §7, deducții). Nu există nici dovezi independente că dispozitivele salvează vieți (N01 §6).
- *Viu, cu o condiție etică și juridică:* nu promiți salvarea (directiva de răspundere pentru produse 2024/2853, N02 Î10), ci „sistem și dovadă”.

**8. Întâi construiești platforma (80–160 de ore), apoi faci pilotul.**
- *Răsturnat:* întâi vinzi și operezi manual, apoi automatizezi.
- *Unde e adevărat:* un dispecer de pază poate suna lucrătorii după un tabel, fără nicio platformă. Infrastructura de dispecerat pentru butoane de panică există deja în România (N05 §7, deducții). Construcția cere 7–16 săptămâni la 10–12 ore pe săptămână (RAP §6).
- *Viu.*

**Dezvoltarea supraviețuitorilor.**
- **1 + 8 → „Lucrul izolat ca modul al firmei SSM”.** Firma SSM include modulul în evaluare. ILLUSTRUS dă portalul și dosarul lunar, iar în prima lună verificările se fac manual, de un dispecer partener.
- **2 + 7 → „Dosarul de diligență”.** Produsul vândut este jurnalul și procedura. Detectarea (check-in, tracker, GPS de flotă) e o sursă de evenimente care se conectează la el.
- **3 → „Scara de escaladare”** (lucrătorul → colegul → șeful → dispecerul → 112). Costul dispeceratului se plătește doar unde riscul îl cere.

**Meta-tiparul inversării.** Toate presupunerile vii depind de aceeași convingere ascunsă: *că ILLUSTRUS trebuie să opereze serviciul de siguranță*. Când o răstorni, ILLUSTRUS devine **furnizorul de software și dovadă al celor care operează deja** (firme SSM, firme de pază, echipele clientului). Pentru un fondator cu 10–12 ore pe săptămână, asta schimbă profilul de risc.

**Clasament onest.** Sunt puternice 1, 2, 7 și 8. Al 3-lea e util doar pentru riscul mediu, al 5-lea doar pentru construcții. Al 4-lea e pe jumătate mort, iar al 6-lea e mort.

---

### C. Provocarea („Po”)

**Ce am făcut.** Am scris regulile pe care toată lumea le ia ca fixe, apoi provocări absurde intenționat. Din fiecare am extras: (a) principiul ascuns, (b) ce s-ar întâmpla minut cu minut, (c) ce diferă față de azi.

**Regulile „fixe”:**
- R1: lucrătorul poartă un dispozitiv.
- R2: alarma merge la un dispecerat.
- R3: angajatorul plătește lunar.
- R4: produsul e pentru lucrătorul izolat.
- R5: întâi construiești, apoi vinzi.
- R6: detectarea e automată.

**Po 1 (eliminare): „Nu există niciun dispozitiv.”**
- (a) Principiul: orice obiect care știe deja unde e omul poate servi drept senzor.
- (b) Minut cu minut: echipa de la apă-canal pleacă cu duba, iar duba are GPS. Omul coboară în cămin, duba stă pe loc 50 de minute. Cine știe că omul e jos?
- (c) Diferența: azi GPS-ul de flotă urmărește vehiculul, nu omul.
- **Idee [estimare]:** „lucrătorul departe de dubă” sau „dubă oprită peste durata anunțată”, ca modul pentru furnizorii de GPS de flotă. Clienții plătesc deja circa 50 lei pe vehicul pe lună (N05 §3). E de verificat dacă furnizorii locali de flotă folosesc echipamente cu protocol deschis; notele nu au acest fapt.

**Po 2 (inversare): „Dispeceratul îl sună pe lucrător, nu lucrătorul dispeceratul.”**
- (a) Principiul: verificarea activă la momente cunoscute, nu așteptarea unei alarme.
- (b) Minut cu minut: „Intru în stația Episcopia, 45 de minute.” La minutul 45 sună un robot: „apasă 1”. Dacă omul nu răspunde, robotul mai încearcă o dată, apoi îl sună pe șef.
- (c) Diferența: alarma nu mai depinde de un senzor, ci de un termen.
- **Idee [estimare]:** planul de lucru izolat cu termen. E nucleul ideii 2 din „Pe scurt” și se leagă de analogia cu planul de zbor (D).

**Po 3 (exagerare): „Fiecare alarmă îl costă pe client 1.000 EUR.”**
- (a) Principiul: valoarea e în evenimentul rar, iar plata lunară „pentru nimic” e greu de apărat.
- (b) Minut cu minut: clientul ar vrea să vadă luna întâi că sistemul funcționează, nu să plătească orb.
- (c) Diferența: azi abonamentul nu produce nimic vizibil în lunile fără incident. Raportul recunoaște că în pilot probabil nu va exista nicio alarmă reală gravă (RAP §6).
- **Idee [estimare]:** livrabilul lunar vizibil e **exercițiul de salvare cronometrat**, cu proces-verbal: „alarma de test a ajuns în 41 de secunde, colegul a ajuns în 4 minute”. Patronul plătește pentru o probă lunară, nu pentru o promisiune.

**Po 4 (distorsiune): „Raportul către ITM se scrie înainte de accident.”**
- (a) Principiul: dovada se pregătește din timp.
- (b) Minut cu minut: în ziua accidentului, inspectorul cere evaluarea, instruirea și procedura. Firma scoate un dosar lunar deja semnat, cu jurnalul orelor.
- (c) Diferența: azi documentele SSM se fac o dată și se uită. Comunicarea „de îndată” a evenimentului la ITM e oricum obligatorie (N02 Î1), iar jurnalul de alarme devine probă la cercetare (RAP §5).
- **Idee [estimare]:** „dosarul de diligență” generat lunar, cu semnături.

**Po 5 (gândire dorită): „Lucrătorii se ceartă pe dispozitiv.”**
- (a) Principiul: dispozitivul trebuie să-i dea ceva lucrătorului.
- (b) Minut cu minut: pădurarul amenințat de hoți de lemne apasă discret SOS și știe că vine cineva, iar jurnalul arată unde era. Bodycam-urile pentru pădurari au fost justificate chiar ca „probe în instanță” (N03 §7).
- (c) Diferența: azi dispozitivul e „al patronului”.
- **Idee [estimare]:** jurnalul vizibil și lucrătorului, ca protecție proprie („am fost unde am spus, am cerut ajutor la ora X”), plus SOS contra agresiunii ca funcție principală pentru pădurari și pază, nu căderea. Așa se atacă refuzul de 59% pentru dispozitivele de urmărire (N05 §6).

**Po 6 (eliminare): „ISU plătește abonamentul.”** (ISU = Inspectoratul pentru Situații de Urgență)
- Prima încercare: ISU ar vrea alarme mai devreme. Notele nu spun nimic despre bugetele, mandatul sau timpii ISU/SMURD (serviciul mobil de urgență) în Bihor (N01 §6, lipsuri).
- A doua încercare: ISU ca partener de instruire pentru exercițiu. Nici aici nu am fapte.
- **Nicio mișcare. Abandonat.**

**Po 7 (distorsiune a ordinii): „Produsul se vinde doar după un accident.”**
- (a) Principiul: dorința de a cumpăra are vârfuri.
- (b) Minut cu minut: după decesul de la Leșu (RAP §1) sau după o campanie ITM pe silvicultură (N02 Î2), toți patronii din sector se uită la propriile riscuri.
- (c) Diferența: azi planul presupune o cerere constantă.
- **Idee [estimare]:** un calendar de vânzare legat de campaniile ITM și de cazurile publice, livrat prin firmele SSM. Atenție la ton: e informare, nu exploatarea tragediei.

**Meta-tiparul provocării.** Provocările care au dat mișcare (1, 2, 3, 4, 5) au mutat produsul **de la senzor la termen și la dovadă**. Ele au adus în față un lucru deja plătit (GPS de flotă), un termen (planul anunțat) sau un document (dosarul). Cele moarte (6) au cerut un plătitor nou, fără buget în note. E aceeași diagnoză ca la analiza laterală anterioară: fundăturile cer un plătitor nou.

**Clasament onest.** 2 și 4 sunt cele mai puternice și se completează. 3 e o idee bună de prezentare a valorii. 5 e utilă doar pentru pădure și pază. 1 e originală, dar complet neverificată. 7 e tactică de vânzare, nu produs.

---

### D. Analogia forțată

**Structura într-o frază, fără vocabularul domeniului:** „O persoană iese din câmpul vizual al grupului pentru un timp. Dacă pățește ceva, nimeni nu observă până nu e prea târziu. Cel responsabil de ea trebuie să poată dovedi după aceea că a avut grijă. Blocajul nu e detectarea, ci faptul că nimeni nu știe că persoana *ar trebui* să fi revenit.”

**Domeniile alese:** aviația ușoară (operațional), stolul de păsări (biologic), tahograful din transportul rutier (operațional și de reglementare), grupul de vecini sau echipa de cățărare (social).

**✈️ Aviația ușoară: planul de zbor și procedura „aeronavă întârziată”.**
- *Rolurile:* lucrătorul e pilotul, planul de lucru e planul de zbor, șeful de echipă și dispecerul sunt serviciul de trafic, iar căutarea e salvarea.
- *Ce face aviația cu blocajul:* pilotul depune un plan cu ora estimată de sosire. Dacă planul nu e închis la timp, se pornește automat o succesiune de faze (incertitudine, alertă, pericol), cu acțiuni tot mai mari. Mecanismul nu cere senzor, cere un **termen asumat** și o **escaladare în trepte**. *[Mecanismul aviatic e din cunoștințe generale, nu din note.]*
- *Transferul [estimare]:* „Deschide planul” (SMS cu codul locului și durata). Urmează o fază de incertitudine (robotul sună lucrătorul), o fază de alertă (colegul, șeful) și o fază de pericol (dispecerul, 112). Fazele se potrivesc cu escaladarea deja propusă în raport (RAP §6), dar sunt declanșate de termen, nu doar de senzor.
- **Transfer puternic.**

**🐦 Stolul de păsări: chemările de contact.**
- *Rolurile:* fiecare pasăre emite periodic un sunet, iar tăcerea unui membru pune stolul în alertă.
- *Transferul:* „tăcerea e alarma”. Trackerele trimit deja „legătură pierdută”, iar raportul are deja alarma de semnal pierdut (RAP §5, documentele F). Testul redundanței: am fi ajuns aici și fără păsări. **Abandonat: analogia de suprafață reformulează ținta.**

**🚚 Tahograful: registrul obligatoriu și industria care trăiește din el.**
- *Rolurile:* șoferul e lucrătorul, tahograful e jurnalul, inspectorul de transport e ITM-ul, iar firmele care descarcă și analizează datele de tahograf pentru transportatori sunt ILLUSTRUS.
- *Ce face domeniul:* un registru cerut de lege, verificat la control, a creat o piață de servicii care țin evidența și semnalează abaterile *înainte* de control. *[Mecanismul e din cunoștințe generale, nu din note.]*
- *Transferul [estimare]:* „registrul digital al lucrului izolat” ținut pentru client, cu semnalarea lunară a abaterilor: ture izolate fără plan, verificări ratate, instruiri expirate.
- *Limita:* tahograful e obligatoriu prin lege, dar dispozitivul de lucru izolat nu este. HG 1091 cere doar informarea despre un sistem de supraveghere și legătură, iar textul exact e de verificat (N02 Î2, lipsuri). Analogia ține pentru *registru și procedură*, nu pentru *dispozitiv*.
- **Transfer mediu.**

**🧗 Echipa de cățărare și grupul de vecini: primul ajutor vine de la cel mai apropiat.**
- *Rolurile:* coechipierul sau vecinul e colegul de la 50–200 m, iar salvamontul sau poliția e dispecerul cu 112.
- *Ce face domeniul:* primul răspuns e al celui aflat la distanță mică. Instituția intervine al doilea, iar fiecare știe dinainte cine răspunde pentru cine.
- *Transferul [estimare]:* fiecare tură izolată are un „responsabil de răspuns” numit: colegul cel mai apropiat, care primește primul alarma. HG 1091 cere deja un supraveghetor desemnat pentru lucrătorii izolați (N05 §1, citat din raportul României către Consiliul Europei; articolul exact e de verificat). Produsul numește supraveghetorul pe fiecare tură și îl face primul destinatar.
- **Transfer puternic, se suprapune cu inversarea 3.**

**Meta-tiparul analogiei.** Toate domeniile care au ajutat tratează blocajul ca **problemă de așteptare** (cine trebuia să revină și când), nu ca **problemă de detectare** (ce senzor a văzut căderea). Domeniul abandonat a eșuat exact pentru că era o analogie de detectare.

**Clasament onest.** Planul de zbor e cel mai puternic, urmat de primul răspuns de la cel mai apropiat. Tahograful e util ca poziționare („registru”), dar nu ca obligație. Stolul a fost abandonat.

---

### E. Cea mai proastă idee (brainstorming invers)

**Ce am făcut.** Am proiectat dezastre plauzibile, de tipul celor pe care o echipă reală le-ar putea apăra într-o ședință. Le-am găsit mecanismul și am răsturnat mecanismul, nu suprafața.

**W1. „Scriem pe site și în ofertă «Salvăm vieți».”**
- *Mecanismul:* creezi o așteptare de siguranță pe care n-o poți dovedi (nu există dovezi independente, N01 §6). Prin noua directivă de răspundere pentru produse, software-ul e produs, iar prezentarea definește siguranța „la care publicul se așteaptă” (N02 Î10).
- *Mecanismul răsturnat:* promiți doar ce controlezi și măsori, și publici lunar măsurătoarea.
- *Direcția:* un SLA (nivel de serviciu garantat) public în minute, cu raport lunar al testelor. Se leagă de Po 3.

**W2. „Patronul vede pe hartă, non-stop, unde e fiecare om, ca să știe cine stă la țigară.”**
- *Mecanismul:* transformă siguranța în supraveghere de productivitate. Asta aduce amenzile ANSPDCP (autoritatea pentru protecția datelor), de 2.000–4.000 EUR pentru GPS folosit în afara programului (N05 §6), refuzul de 59% (N05 §6) și conflictul cu sindicatul (Legea 190/2018, art. 5) (N02 Î6).
- *Mecanismul răsturnat:* datele sunt ale lucrătorului în mod implicit. Patronul vede locația doar la alarmă, iar lucrătorul vede tot jurnalul său.
- *Direcția:* „confidențialitatea ca funcție de vânzare către sindicat”. Nota propune deja aceste principii (N05 §6, deducții); nou e că ele devin argument de vânzare, nu doar conformitate.

**W3. „Dispecerul e fondatorul, noaptea, pe telefonul personal, până crește firma.”**
- *Mecanismul:* un singur om cu 10–12 ore pe săptămână devine punctul unic de eșec al unui lanț 24/7. Răspunderea lui e nelimitată, fără asigurare RC (răspundere civilă) găsită (N02 Î10).
- *Mecanismul răsturnat:* fondatorul nu stă niciodată în lanțul de alarmă. Stă în lanțul de **software și dovadă**.
- *Direcția:* white-label pentru firmele de pază (secțiunea 4, V5).

**W4. „Cumpărăm 1.000 de trackere acum, ca să avem preț bun.”**
- *Mecanismul:* capital blocat (circa 90.000 EUR la 1.000 de lucrători, N05 §4) la un buget de 25.000 EUR. În plus, modelul ales poate fi scos din producție: GH5200 apare „End of life” (RAP §4), iar TMT250 poate fi doar 2G (N04 §1).
- *Mecanismul răsturnat:* clientul sau distribuitorul deține hardware-ul, ILLUSTRUS doar se conectează.
- *Direcția:* platformă care acceptă mai mulți producători (V1) și scenariul C din raport (RAP §7).

**W5. „Începem cu Plexus și Petrom, că au bugete mari.”**
- *Mecanismul:* ciclul de achiziție de 6–12 luni și furnizorii globali impuși de grup (N05 §2, §6) depășesc răbdarea unui fondator part-time.
- *Mecanismul răsturnat:* vinzi acolo unde decide un singur om (patronul sub 50 de angajați, N05 §2) sau prin cineva care are deja relația.
- *Direcția:* canalul prin firmele SSM (V4).

**W6. „Orice alarmă sună direct la 112.”**
- *Mecanismul:* alarmele false consumă salvatori publici și încredere.
- *Mecanismul răsturnat:* lucrătorul confirmă întâi (pre-alarmă), apoi intervine omul.
- **Mecanism mort:** răsturnarea e deja în raport, cu pre-alarmă de 20–30 de secunde și escaladare (RAP §6). Nu aduce nimic nou.

**W7. „Primul pilot e în pădurea fără semnal din Apuseni, ca să arătăm ce putem.”**
- *Mecanismul:* pui cel mai greu caz tehnic la începutul curbei de încredere: LoRaWAN (rețea radio cu rază mare) are circa 300 m în pădure, iar satelitul direct pe telefon e doar în test (N04 §7). Prima referință devine un eșec.
- *Mecanismul răsturnat:* primul caz e cel în care succesul e ieftin de demonstrat.
- *Direcție parțial deja urmată:* raportul pornește de la utilități, nu de la pădure (RAP §1). Nou e că și dispozitivul poate lipsi în primul test (check-in), ca să izolezi riscul tehnic de riscul comercial.

**Descalificată ca „idee proastă”:** „Vindem doar hârtii: dosarul de conformitate, fără niciun dispozitiv.” Când am verificat mecanismul, n-am găsit unul prost. E un produs real, deghizat (V3). Am mutat-o în secțiunea 4.

**Meta-tiparul (păcatul comun).** W1, W3, W4 și W5 sunt același păcat sub forme diferite: **ILLUSTRUS își asumă riscul (juridic, operațional, de capital, de timp) înainte ca clientul să fi văzut valoarea, și în zone pe care nu le controlează** (semnalul, purtarea, salvarea). Harta a ce nu trebuie să facă niciodată produsul: să promită rezultatul, să țină fondatorul în lanțul 24/7, să dețină hardware și să depindă de ciclurile corporative.

---

### F. SCAMPER, pe scurt (pentru variantele de produs)

**Ținta:** „tracker + platformă + dispecerat, abonament lunar”.
- **Înlocuiește (S):**
  - trackerul cu un termen anunțat (check-in) sau cu GPS-ul de flotă existent;
  - dispecerul cu colegul ca prim răspuns.
  - Mușcă.
- **Combină (C):**
  - jurnalul de alarme cu dosarul SSM al firmei externe;
  - consola de dispecerat cu dispeceratul de pază existent.
  - Mușcă.
- **Adaptează (A):** planul de zbor (D) și „registrul” de tip tahograf (D). Le număr o singură dată: sunt deja la analogie.
- **Modifică (M):** mărirea frecvenței testului (exercițiu lunar ca livrabil) mușcă puțin. E deja la Po 3, deci nu o număr din nou.
- **Altă folosință (P):** același jurnal, pentru protecția lucrătorului (pădurar sau agent de pază agresat). Mușcă slab.
- **Elimină (E):**
  - dispozitivul (pentru riscul mediu);
  - dispeceratul propriu (deja eliminat în raport);
  - funcțiile de puls și stres termic (deja eliminate în raport).
  - Doar primul punct e nou.
- **Inversează (R):** cine operează (firma de pază) și cine furnizează (ILLUSTRUS). E deja la inversare.

**Meta-tiparul:** Înlocuiește și Elimină au mușcat cel mai mult, mereu pe același punct: **dispozitivul nu e necesar pentru un prim produs vândabil**. Acolo e ideea moale. Combină a mușcat pe canal. Operațiile fără conținut nou le-am arătat ca atare.

---

### G. Cele șase pălării, pe decizie

**Decizia:** primul lucru testat e pilotul din raport (utilitate, 30 de trackere, dispecerat de pază, 90 de zile, circa 3.600–6.600 EUR, construcție de 80–160 de ore) sau una dintre variantele de canal și software?

**⚪ Albă (doar fapte).**
- Bani și efort:
  - pilotul costă circa 3.600–6.600 EUR în bani, fără gaze și satelit (RAP §6);
  - construcția cere 7–16 săptămâni la 10–12 ore pe săptămână (RAP §6);
  - profitul vine abia la 160–700 de lucrători (RAP §7).
- Piața și concurența:
  - nu s-a găsit niciun concurent local, nicio firmă SSM cu acest serviciu și nicio licitație dedicată (N03 §3, §7; N05 §7);
  - piața nu are vocabular (N05 §7).
- Prețuri de referință:
  - onorariul SSM extern e de 8–25 lei pe angajat pe lună (N05 §3);
  - GPS-ul de flotă costă circa 50 lei pe vehicul (N05 §3);
  - un ARC în UK costă în plus 1,85 GBP (N05 §4).
- Cererea:
  - 46–59% din muncitorii din construcții nu ar purta astfel de dispozitive (N05 §6);
  - aplicațiile au 20–25% din piața europeană (N05 §4).
- Ce lipsește:
  - tariful de dispecerat în România;
  - numărul de firme SSM din Bihor;
  - dacă venitul din abonamente cu dispozitive contează la DR-36;
  - textul exact al HG 1091 art. 10–11;
  - statutul juridic după Legea 333/2003 (pază) (N05 §4, §5; N02 Î2, Î10; PA2 §A.1).

**🔴 Roșie (emoții, fără justificare).**
- Pilotul cu trackere e partea „adevărată” și captivantă. Varianta pe hârtie pare plictisitoare.
- Mă neliniștește ideea că un om moare într-un cămin, iar ILLUSTRUS apare în dosar.
- E o ușurare să nu fiu eu dispecerul.
- *Contra concluziei care se conturează:* mi-e teamă că varianta „doar software prin intermediari” e o fugă de partea grea și că fără dispozitive nu există produs diferit de un tabel Excel.

**⚫ Neagră (riscuri cu mecanism).**
- **Pilotul din raport:** blochează fondatorul circa 3 luni de construcție înainte de primul semnal de cumpărare. Pornește cu răspundere juridică nevalidată de avocat (N02 Î10), depinde de un model posibil scos din producție (RAP §4) și de un dispecer de pază fără tarif cunoscut (N05 §5).
- **Varianta prin firmele SSM:** se blochează dacă firmele se tem de răspunderea de a recomanda (N05 §5, deducții) sau dacă văd dosarul ca munca lor proprie, pe care n-o împart.
- **Check-in fără dispozitiv:** eșuează la riscul înalt (pierdere bruscă a cunoștinței, gaze), pentru că termenul de 40 de minute e prea lung. Dacă lucrătorii nu au telefon de serviciu, apare problema GDPR a telefonului personal (N03 §4).
- **White-label pentru pază:** cade dacă Legea 333/2003 cere licență pentru dispecerat de persoane (N02 Î10) sau dacă firma de pază vrea să plătească doar câțiva lei.

**🟡 Galbenă (beneficii cu mecanism).**
- **Varianta prin firmele SSM:** un singur contract de canal aduce zeci de clienți, pentru că firma SSM are deja relația și semnătura pe evaluare (N05 §2). Dosarul se construiește în APEX în câteva săptămâni, fără hardware [estimare].
- **Check-in-ul:** scade costul la zero hardware și coboară pragul de rentabilitate. Nota calculează un prag de circa 200 de lucrători la un amestec de 40% aplicație (N05 §4, sensibilități).
- **White-label-ul:** elimină cerința de 24/7 de la fondator și produce venit de software, probabil eligibil DR-36 [estimare].
- **Pilotul din raport:** este singura variantă care produce o probă tehnică reală (purtare, alarme false, semnal), pe care se sprijină ulterior toate celelalte.

**🟢 Verde (alternative; cel puțin una abandonează premisa).**
- G1. Testezi întâi canalul (firmele SSM) și check-in-ul manual, iar pilotul cu trackere vine în luna 3–4, numai dacă există un client care plătește.
- G2. Rulezi pilotul din raport, dar pe 10 lucrători în loc de 30, cu dispozitivele clientului și check-in în paralel, ca să compari cele două surse de alarmă.
- G3. Faci white-label numai pentru firma de pază, fără niciun client final direct.
- **G4 (abandonează premisa):** nu construiești un produs de siguranță acum. Folosești SSM-ul doar ca **nișă pentru serviciile web DR-36**: site-uri, automatizări n8n și portaluri pentru firmele SSM externe din Bihor. Ideea purtabilului revine după ce ai cei 10.000 EUR și o relație cu 2–3 firme SSM.

**🔵 Albastră (sinteză).**
- *Unde nu se înțeleg pălăriile:* Galbenă spune că dispozitivul nu e necesar pentru primul venit, dar e necesar pentru probă. Roșie spune că fără dispozitiv produsul nu e diferit.
- *Informația care schimbă răspunsul:* dacă 2 din 5 firme SSM din Oradea spun „da, includem modulul la un client” (secțiunea 6, testul 1). Fără asta, G4 devine opțiunea rațională.
- *Recomandarea:* G1, cu G4 ca plasă de siguranță. Testele de canal și de check-in în 2–4 săptămâni, iar pilotul cu trackere abia după un semnal de plată.
- *Încredere: medie-scăzută.* Se bazează pe deducții despre comportamentul firmelor SSM, fără niciun interviu în note.

---

## 3. Reformulări ale problemei și cine altcineva ar putea plăti

### 3.1 Ce vinde de fapt produsul (reformulări)

- **Minute până la ajutor.** E formularea raportului (RAP §1). E bună pentru marketing și contract (SLA), pentru că se poate măsura. Pentru patron nu e însă motivul principal de cumpărare: alarma reală e rară, iar în pilot probabil nu apare (RAP §6).
- **Dovadă pentru ITM și pentru procesul penal.** Jurnalul cu oră exactă devine probă la cercetare (RAP §5). Costul dominant al unui deces e penal și personal pentru administrator (N01 §7). **Cea mai puternică reformulare** [estimare]. Atenție: nu poate fi vândută ca „scăpați de pușcărie”, ci ca „aveți sistem și îl puteți arăta”.
- **Conformitate cu HG 1091/2006.** Hotărârea definește lucrul izolat și cere informarea despre sistemul de supraveghere și legătură cu exteriorul (N02 Î2). Ea nu cere însă explicit un *dispozitiv*, iar textul exact al art. 10–11 e de verificat. Conformitatea se vinde ca *procedură plus registru*, cu dispozitivul ca una dintre măsuri.
- **Liniștea patronului.** E reală, dar nu are preț în note. Se obține prin raportul lunar și prin exercițiul de salvare, nu prin hartă (Po 3) [estimare].
- **Asigurare.** În România nu ține azi: CAM e fix (N06 §1) și nu s-au găsit reduceri private (N05 §5). Ține doar ca co-marketing (o poliță de accidente de grup plus abonamentul) (N05 §5, deducții).
- **Organizarea lucrului izolat** (cine e singur, unde, până când). E reformularea venită din A și D. Rezolvă și ce nu rezolvă dispozitivul, adică știi pe cine să cauți [estimare].
- **Protecție împotriva agresiunii.** Pentru pădurari (157 agresați în 5 ani, N03 §7) și pentru pază, SOS-ul discret e funcția centrală, nu căderea [estimare].
- **Cerința clientului mare sau a auditului.** Antreprenorul care lucrează pentru o fabrică ISO 45001 sau pentru un beneficiar public poate fi obligat de clientul său. Notele nu au găsit astfel de cerințe în România (N01 §7, lipsuri). E o ipoteză de verificat.
- **Acceptarea de către lucrători și sindicat** (pachetul GDPR ca avantaj). Raportul o numește deja argument (RAP §1; N05 §2, deducții).

### 3.2 Cine altcineva ar putea plăti (sau vinde)

- **Serviciile externe SSM.** Lista lor e publică pe site-ul Inspecției Muncii (N05 §2). Ele recomandă, dar nu plătesc (N05 §5).
  - *Rol posibil:* revânzător sau white-label al modulului „lucru izolat” [estimare].
  - *Pentru:* scriu evaluarea, unde pot trece măsura (N05 §2), iar comisionul are greutate față de onorariul lor (N05 §5).
  - *Contra:* frica de răspundere (N05 §5).
- **Firmele de pază cu dispecerat.**
  - *Rol posibil:* operator al dispeceratului și cumpărător al consolei (white-label), revânzător către clienții lor de pază.
  - *Pentru:* au operatori 24/7 și proceduri de alarme false (N05 §5), iar caietele de sarcini includ deja alarme false și teste lunare (N05 §2).
  - *Contra:* Legea 333/2003 e neclară (N02 Î10), iar ele pot copia serviciul (N05 §5).
- **Asigurătorii** (NN, Omniasig, Grawe, Groupama).
  - *Rol posibil:* co-marketing pe polițele de accidente de grup (N05 §3, §5).
  - *Contra:* nu au reduceri dovedite, iar rolul de plătitor e mort azi (B6).
- **Antreprenorii generali ai marilor șantiere** (de exemplu Leșu).
  - *Rol posibil:* plătitor pe proiect pentru toți subcontractorii de pe șantier (RAP §1 „vinzi pe șantier”; B5) [estimare].
  - *Contra:* multe decese au loc cu colegi alături (RAP §1, Lunca).
- **Primăriile.** Nu au buget de SSM pentru firme private, deci nu sunt plătitor direct. Sunt însă acționari sau autorități pentru Compania de Apă Oradea și Termoficare (RAP §1), deci pot fi un sponsor politic al pilotului la utilități [estimare].
- **ISU.** *Mort ca plătitor:* notele nu au buget, mandat sau timpi (Po 6).
- **Romsilva / Direcția Silvică Bihor.**
  - *Pentru:* există deja un program de GPS pe utilaje și bodycam-uri pentru pădurari (N03 §7), deci și un buget de echipare.
  - *Contra:* decizia e centralizată și instituția e în reorganizare (N05 §1). E plătitor de anul 2, prin licitație.
- **Ocoalele silvice private** (6 în zonă) și firmele de exploatare care lucrează pe contracte (N05 §1). Patronul decide singur (N05 §2). Plătitor direct bun pentru SOS și satelit [estimare].
- **Furnizorii de GPS de flotă.**
  - *Rol posibil:* revânzători ai unui modul de lucru izolat pe aceeași factură (Po 1) [estimare, neverificat].
- **Medicina muncii.** Vede anual toți angajații și știe cine lucrează în ture, dar nu are stimulent financiar. Poate aduce clienți pentru un comision de 5–10% (N05 §5).
- **Distribuitorii de EIP** (echipament individual de protecție, de exemplu Safety Academy, distribuitor 3M) (N05 §5). Canal de revânzare pentru dispozitive [estimare].
- **Casa teritorială de pensii Bihor.** Canal de informare, nu finanțator (N06 §1).
- **Câștigătorii STEP 961** (programul UE pentru tehnologii strategice, apelul Nord-Vest), din trimestrul 3 al lui 2027. Pot cumpăra consultanță în inovare, acoperită 100% până la 220.000 EUR (N06 §7; RAP §8). Plătitor de servicii, nu de produs.
- **Poșta Română („Butonul Roșu”) și dispeceratele pentru vârstnici.** Infrastructura de dispecerat pentru butoane de panică există deja (N05 §7). Sunt partener posibil pentru dispecerat, nu plătitor [estimare].

---

## 4. Variante de produs mai ușor de vândut de un fondator singur

Fiecare variantă e o **[estimare]** construită pe faptele citate.

**V1. Doar software peste dispozitivele clientului (platformă care primește alarme de la mai mulți producători).**
- *Ce e:* ILLUSTRUS nu vinde hardware. Conectează trackerele Teltonika (prin Traccar, server open-source), Garmin inReach (prin webhook, adică Garmin trimite automat evenimentul la adresa ta) și, mai târziu, Twig sau MSA, și dă consola, regulile și jurnalul.
- *Pentru:*
  - nu are capital blocat (W4);
  - căile tehnice există: Traccar pentru Teltonika și webhook-ul Garmin (N04 §8);
  - un centru de alarmă din Italia leagă prin API peste 400 de dispozitive Twig (RAP §3);
  - scade dependența de un singur producător (N05 §6, deducții).
- *Contra:*
  - în România aproape nimeni nu are încă astfel de dispozitive (N05 §7; N03 §3), deci baza instalată e mică;
  - Blackline dă API doar prin formular (RAP §3).
- *Verdict:* e un strat bun pentru anul 2, nu un prim produs.

**V2. Check-in programat pentru lucrătorul izolat, pe telefon, cu escaladare (SMS, apel automat IVR sau aplicație).**
- *Ce e:* planul de lucru izolat cu termen (D, Po 2). Robotul sună la termen, apoi escaladează la coleg, la șef și la dispecer.
- *Pentru:*
  - aplicațiile au 20–25% din piața europeană (N05 §4);
  - costul hardware e zero și pragul de rentabilitate coboară (N05 §4, sensibilități);
  - se construiește cu n8n și APEX;
  - un apel vocal merge și pe telefon simplu, nu doar pe smartphone [estimare].
- *Contra:*
  - nu detectează căderea sau pierderea cunoștinței în câteva secunde;
  - telefonul nu e purtat pe corp, nu merge fără semnal și nu e ATEX (certificat pentru zone cu pericol de explozie);
  - mulți muncitori nu au telefon de serviciu, iar telefonul personal ridică probleme GDPR (N03 §4);
  - chiar vânzătorii de aplicații spun că la riscul înalt e nevoie de dispozitiv (N03 §4).
- *Unde merge:* ture de noapte la stații, mentenanță, pază, pădurari pentru check-in de seară. *Unde nu merge:* gaze și cădere de la înălțime.

**V3. Jurnalul sau dosarul de conformitate pentru lucrul izolat (portal fără dispecerat).**
- *Ce e:* evaluarea specifică lucrului izolat, procedura de salvare, instruirile cu semnătură, registrul turelor izolate (din V2 sau V1), raportul lunar și proces-verbalul exercițiului de salvare. Textele sunt redactate cu LLM, dar verificate de om și ținute în afara lanțului de alarmă (RAP §5, AI Act).
- *Pentru:*
  - lista de documente A–F e lungă și clientul are oricum nevoie de ea (RAP §5);
  - nu are răspundere 24/7;
  - e un serviciu web curat, deci probabil venit DR-36 [estimare, de confirmat cu GAL-ul; PA2 §A.1];
  - răspunde argumentului de vânzare cel mai puternic, dovada diligenței (N01 §7).
- *Contra:*
  - piața nu are vocabular (N05 §7);
  - firmele SSM pot considera dosarul munca lor;
  - prețul acceptabil e mic, raportat la onorariul SSM de 8–25 lei pe angajat (N05 §3);
  - singur, fără nicio verificare reală, riscă să fie „hârtie”, adică exact „gadgetul” criticat de INRS (N02 Î2).
- *Verdict:* bun numai legat de V2 sau de un exercițiu real.

**V4. Pachet vândut prin firmele de servicii externe SSM (comision sau white-label).**
- *Ce e:* V3 plus V2, livrate sub marca firmei SSM sau cu comision de recomandare.
- *Pentru:*
  - firma SSM e influențatorul care poate prescrie măsura în evaluare (N05 §2);
  - un comision de 15% egalează onorariul ei pe lucrător (N05 §5);
  - lista firmelor e publică (N05 §2);
  - un contract de canal înseamnă mulți clienți mici.
- *Contra:*
  - frica de răspundere când „recomandă” (N05 §5), de gestionat prin contract de recomandare, nu de revânzare (N05 §5, deducții);
  - numărul de firme din Bihor e necunoscut (N05 §5, lipsuri).
- *Verdict:* canalul cu cel mai bun raport între efort și reach pentru un fondator singur [estimare].

**V5. White-label pentru firmele de pază (ele operează, ILLUSTRUS dă software-ul).**
- *Ce e:* consola de dispecerat APEX, integrarea dispozitivelor și pachetul de conformitate, sub marca firmei de pază. Firma vinde „pază pentru oameni” clienților ei existenți.
- *Pentru:*
  - firma are operatori 24/7, proceduri de alarme false și relații cu aceiași clienți (N05 §5);
  - riscul de copiere devine relație de client;
  - fondatorul iese din lanțul 24/7 (W3);
  - venitul e din licență de software și hosting [estimare DR-36].
- *Contra:*
  - Legea 333/2003 e neclară (N02 Î10);
  - nu știm cât ar plăti (N05 §5, lipsuri);
  - firma de pază ar putea să nu vrea să-și asume răspunderea pentru alarmele de persoane (de verificat cu asigurătorul ei, RAP §9).

**V6. Modul de lucru izolat pentru furnizorii de GPS de flotă** (din Po 1).
- *Pentru:* clienții plătesc deja circa 50 lei pe vehicul pe lună (N05 §3), iar relația și factura există.
- *Contra:* complet neverificat. Notele nu spun ce echipamente folosesc furnizorii locali, iar aceștia îl pot construi singuri.
- *Verdict:* idee de explorat cu un singur telefon, nu direcție principală.

**V7. Serviciu pe proiect pentru antreprenorii generali** (închiriere pe șantier, B5).
- *Pentru:* „vinzi pe șantier” (RAP §1); Leșu e un caz local de operator singur.
- *Contra:* în construcții multe decese au loc cu colegi de față (RAP §1), proiectele sunt scurte, achizițiile trec prin antreprenor, iar dispozitivele sunt necesare (riscul e înalt).
- *Verdict:* faza 2.

**Varianta din raport, pentru comparație** (abonament cu dispozitiv și dispecerat la utilități).
- *Pentru:* singura care produce probă tehnică reală.
- *Contra:* capital, timp de construcție, răspundere și prag de profit la 160–700 de lucrători (RAP §6, §7).

---

## 5. Cele mai mari 5 riscuri, văzute din inversiune și din „cea mai proastă idee”

1. **Fondatorul își asumă riscul înaintea clientului** (păcatul comun din E: W1, W3, W4, W5).
   - *Mecanismul:* construiești 80–160 de ore, cumperi dispozitive și semnezi un SLA de alarmă înainte ca cineva să fi plătit. Profitul vine abia de la 160–700 de lucrători (RAP §7).
   - *Atenuare [estimare]:* întâi canal și check-in manual, apoi dispozitive (secțiunea 6).
2. **Promisiunea depășește dovada** (W1; inversarea 7).
   - *Mecanismul:* nu există dovezi independente că dispozitivele salvează vieți (N01 §6). Directiva 2024/2853 tratează software-ul ca produs, iar prezentarea definește siguranța așteptată (N02 Î10).
   - *Atenuare:* promiți minute și proceduri măsurate și publici rapoartele lunare.
3. **Supravegherea ucide adoptarea** (W2; inversarea 4).
   - *Mecanismul:* 59% refuză dispozitivele de urmărire (N05 §6). ANSPDCP amendează GPS-ul folosit în afara programului (N05 §6), iar Legea 190/2018 cere consultarea sindicatului (N02 Î6).
   - *Atenuare:* locație doar la alarmă, jurnal vizibil lucrătorului, SOS cu beneficiu direct (Po 5).
4. **Canalul nu vrea să-și asume răspunderea** (riscul nou al variantelor V4 și V5).
   - *Mecanismul:* firmele SSM se tem să „recomande” un dispozitiv care nu alarmează (N05 §5). Firmele de pază pot avea probleme de licență (Legea 333/2003) sau de asigurare (N02 Î10).
   - *Atenuare:* contract de recomandare, nu de revânzare, și opinie juridică înaintea primului contract (RAP §9).
5. **Cererea nu există încă și nu are cuvinte** (inversarea 1; Po 7).
   - *Mecanismul:* nu s-au găsit licitații, bloguri SSM sau angajatori care să folosească astfel de dispozitive (N05 §7). Lipsa din căutări nu dovedește lipsa din piață (RAP §1), dar nici nu arată o cerere.
   - *Atenuare:* educarea pieței prin firmele SSM și calendarul campaniilor ITM. Și G4 ca plasă de siguranță: dacă testele nu arată cerere în 4 săptămâni, revii la serviciile web DR-36.

**Riscul care NU s-a mișcat la inversiune:** argumentul asigurării (B6). Rămâne mort în România până la o reformă a CAM (N06 §1).

---

## 6. Recomandarea: trei direcții de testat întâi

Toate testele de mai jos sunt **[estimare]**: țintele de succes sunt propuneri, nu repere din note. Ordinea e gândită pentru 10–12 ore pe săptămână. Pilotul cu trackere din raport (RAP §6) rămâne **faza 2**, pornită numai dacă cel puțin un test de mai jos produce un semnal de plată.

### Direcția 1: Modulul „Lucru izolat” vândut prin firmele de servicii externe SSM (V4 + V3)

**Ipoteza:** firmele SSM din Oradea ar include în evaluarea riscurilor a cel puțin unui client un modul cu dosar lunar și check-in, dacă primesc comision și nu își asumă răspunderea de furnizor.

**Testul (3 săptămâni, circa 25 de ore):**
- **Săptămâna 1:**
  - descarci lista serviciilor externe SSM abilitate de pe site-ul Inspecției Muncii (N05 §2) și filtrezi Bihorul;
  - pregătești o pagină A4 „Lucrul izolat: ce cere HG 1091/2006 și cum dovedești la ITM” (N05 §7, deducții);
  - faci o machetă APEX cu 3 ecrane: lista turelor izolate, jurnalul de check-in și raportul lunar în PDF.
- **Săptămânile 2–3:**
  - suni 10 firme și obții 5 întâlniri de 30 de minute;
  - pui întrebările din RAP §9 („Vă cer clienții soluții pentru lucrul izolat? L-ați recomanda pentru 15%? Cine decide?”);
  - adaugi întrebarea nouă: „Ați include modulul sub numele dumneavoastră?”.

**Ce măsori:**
- câte firme spun că au clienți cu lucru izolat;
- câte acceptă să propună un pilot gratuit de 4 săptămâni unui client;
- ce preț ar cere clientului.

**Prag de continuare:** cel puțin 2 din 5 firme propun un client concret și cel puțin una semnează o scrisoare de intenție. **Prag de oprire:** nicio firmă nu propune un client. În acest caz cântărești G4 (folosești firmele SSM doar ca clienți de servicii web pentru DR-36).

### Direcția 2: Check-in programat cu escaladare, rulat întâi manual (V2, testul „vrăjitorul din Oz” = serviciu făcut de om înainte de automatizare)

**Ipoteza:** o echipă de noapte de la o utilitate, o firmă de pază sau o firmă forestieră mică folosește un plan de lucru izolat cu termen. Șeful ei ar plăti pentru jurnal și escaladare.

**Testul (4 săptămâni, circa 30 de ore):**
- **Săptămâna 1:**
  - alegi un client prietenos: o echipă din Direcția 2 sau un patron forestier din zona Aleșd–Beiuș (RAP §1);
  - 5–10 lucrători primesc instrucțiunea: „SMS cu codul locului și durata la intrare, «OK» la ieșire”;
  - faci în n8n fluxul: SMS primit → temporizator → SMS sau apel de verificare → escaladare la șef;
  - fondatorul ține doar jurnalul, nu e în lanț după ora 22. Escaladarea finală merge la șeful clientului (W3).
- **Săptămânile 2–4:** rulezi testul, faci un exercițiu de salvare pe săptămână (Po 3) și un interviu de 10 minute cu 5 lucrători și cu șeful.

**Ce măsori:**
- % din turele izolate cu plan anunțat;
- % din check-in-uri confirmate la timp;
- numărul de escaladări și câte au fost false;
- timpul până la contactul cu lucrătorul în exercițiu;
- câți lucrători spun „aș continua” (pragul de 70% din raport, RAP §6);
- dacă șeful acceptă să plătească 20–40 lei pe lucrător pe lună pentru continuare [estimare de preț].

**Prag de continuare:** cel puțin 80% din ture cu plan după săptămâna 2 și o ofertă de plată. **Prag de oprire:** sub 50% din ture cu plan, adică oamenii nu folosesc termenul.

### Direcția 3: White-label pentru o firmă de pază din Oradea (V5)

**Ipoteza:** o firmă de pază cu dispecerat ar plăti o licență de consolă și ar vinde „pază pentru oameni” clienților ei.

**Testul (2–3 săptămâni, circa 15 ore, în paralel cu Direcția 1):**
- **Săptămâna 1:**
  - ceri ofertele de dispecerat de la 3 firme, cum recomandă raportul (RAP §6, §9);
  - la fiecare întâlnire pui și a doua întrebare: „Dacă vă dăm consola, integrarea și dosarul, ați vinde serviciul clienților voștri sub marca voastră? Câți clienți aveți cu personal care lucrează singur?”
- **Săptămânile 2–3:**
  - arăți macheta APEX a consolei (coada de alarme cu cronometru, scriptul, butoanele pe pași, RAP §6);
  - ceri întrebarea despre Legea 333/2003 de la juristul firmei și de la asigurătorul ei.

**Ce măsori:**
- tariful pe persoană conectată (lipsă în note, N05 §4);
- interesul pentru licență și prețul acceptat;
- numărul de clienți ai firmei cu lucru izolat;
- răspunsul despre licență și asigurare.

**Prag de continuare:** o firmă acceptă să prezinte oferta la cel puțin 3 clienți ai ei. **Prag de oprire:** toate firmele cer exclusivitate fără plată sau refuză răspunderea pentru alarmele de persoane.

### Ce faci după cele 4 săptămâni

- **Dacă 1 sau 3 dau semnal:** construiești portalul (V3) și consola ca produs de software. Te ocupi și de întrebarea DR-36: scrisoarea către GAL și OJFIR din PA2 §A.2 trebuie să întrebe explicit dacă licențele de software vândute firmelor SSM și de pază contează ca activitate CAEN 6310.
- **Dacă 2 dă semnal:** check-in-ul devine treapta de intrare. Pilotul cu trackere din raport se face pe 10 lucrători, cu dispozitivele clientului, și compară cele două surse de alarmă (G2).
- **Dacă niciuna nu dă semnal:** păstrezi raportul ca analiză. Îți folosești timpul pe serviciile web DR-36, eventual cu firmele SSM ca clienți (G4), și revii la idee după campaniile ITM din 2027 sau după un caz care schimbă cererea.

**Ce n-am putut face și unde ar mai ajuta o trecere.**
- **Random-stimulus** (stimul aleator) ar putea arăta dacă toate tehnicile au ajuns la „dovadă și termen” pentru că ideea e bună sau pentru că s-a format un făgaș.
- **Six-hats pe G4** ar arăta separat cât costă amânarea ideii.
- Nicio idee de aici nu e validată pe teren. Cele mai fragile sunt V6 (GPS de flotă) și presupunerea că firmele SSM vor vinde un modul sub marca lor.
