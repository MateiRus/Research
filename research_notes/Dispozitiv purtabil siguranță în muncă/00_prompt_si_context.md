# 00 — Promptul de cercetare (copiat din branch claude/trusting-planck-3jm893, commit 5187f0c) și contextul din repo

**Instrucțiune pentru redactor:** răspunsul final trebuie să urmeze exact secțiunea „Ce vreau la final” (9 livrabile), în română simplă, cu prescurtările explicate în paranteză, cu liste cu puncte simple (nu tabele), și cu marcaje clare: fapt cu sursă / estimare / de verificat.

**Legături în repo (branch claude/amazing-turing-nucje7):** planul PREVENT-NV v2 e în `proiect-STEP-PREVENT-NV-plan-v2.md` (centrul de coordonare poate deveni dispecerat de alarme); evaluarea lui în `evaluare-plan-PREVENT-NV.md`; regulile apelului STEP și actorii din Nord-Vest în `research_notes/Apel STEP Nord Vest oportunități/` (reguli_apel_step_obligatii.md, actori_nord_vest.md, apeluri_accesibile_microfirma.md) și în `reports/Apel STEP Nord Vest oportunități.md`. Corrigendum nr. 2 a mutat termenul apelului 961 la 02.11.2026; ILLUSTRUS nu poate fi solicitant direct (grant minim 5 mil. EUR, profit și salariat în anul anterior).

---

# Prompt de cercetare: dispozitiv purtabil pentru siguranța la locul de muncă (România)

**Ce e documentul:** promptul pentru o cercetare aprofundată a ideii de dispozitiv purtat în timpul lucrului, în locurile cu risc, ca să reducă accidentele și decesele de muncă. Se copiază întreg într-o sesiune nouă de cercetare.
**Data:** 12 octombrie 2026.
**Legătura cu restul repo-ului:** se poate combina cu `proiect-STEP-PREVENT-NV-plan.md` (centrul de coordonare devine dispecerat pentru alarme) și cu `reports/Oportunități software în sănătatea predictivă.md`.

---

## Promptul (de copiat)

Ești un analist de piață și de produs. Fă o cercetare aprofundată, cu surse citate, despre ideea de mai jos. Scrie în română simplă. Orice prescurtare sau cuvânt tehnic se explică în paranteză. Pentru liste folosește puncte simple, nu tabele, ca textul să poată fi copiat ușor.

### Cine sunt eu

- Firmă: ILLUSTRUS S.R.L., Bihor, CAEN 6310 (prelucrarea datelor, hosting, portaluri web).
- Competențe: Python, SQL, PL/SQL, Oracle APEX, n8n (automatizări), LLM-uri (modele mari de limbaj), WordPress.
- Nu construiesc hardware. Cumpăr dispozitive certificate existente și construiesc platforma, integrarea, regulile de alertă și dispeceratul.

### Ideea

Un dispozitiv purtat de muncitori (brățară, ceas, cutiuță prinsă de cască sau vestă), plus o platformă și un dispecerat (centru care primește alarmele), vândute ca abonament firmelor. Funcțiile avute în vedere:

- detectarea căderii și a imobilității („om la pământ”), cu locația;
- buton SOS pentru cine lucrează singur;
- avertizare la stres termic (supraîncălzirea corpului);
- detectarea gazelor toxice;
- avertizare la apropierea de utilaje;
- puls anormal (doar dacă nu transformă produsul în dispozitiv medical).

Ce aleg să promit: siguranță și ajutor rapid, nu diagnostic medical.

### Întrebările de cercetare

**1. Problema în România (cu cifre și surse)**
- Câte accidente de muncă și câte decese au fost în ultimii 5 ani? Sursele: Inspecția Muncii, INS (Institutul Național de Statistică), Eurostat.
- Pe ce cauze (căderi de la înălțime, striviri, electrocutări, utilaje, căldură, gaze, cauze medicale la locul de muncă)?
- Pe ce industrii și pe ce județe? Detaliază Bihor și Nord-Vest.
- Ce procent din decese putea fi evitat sau redus prin alarmă automată și intervenție rapidă (căderi, imobilitate, lucru singur)?
- Ce costă un accident grav pentru firmă: amenzi, anchetă, răspundere penală, asigurări, oprirea lucrului, imagine?

**2. Obligațiile legale care creează cererea**
- Legea 319/2006 (securitate și sănătate în muncă) și HG 1425/2006 (normele de aplicare): ce obligă angajatorul la evaluarea riscurilor, la lucrul singur, la lucrul la înălțime și la căldură extremă.
- Reguli pentru caniculă (OUG 99/2000 și altele actuale).
- Reguli speciale pe sectoare: construcții, energie, silvicultură, mine, chimie, utilități.
- Monitorizarea angajaților: Codul muncii, GDPR (regulamentul european de protecție a datelor), Legea 190/2018 art. 5. Ce trebuie făcut ca urmărirea locației și a pulsului să fie legală: informare, consultarea sindicatului, interes legitim, DPIA (evaluarea de impact asupra protecției datelor).
- Când devine produsul dispozitiv medical (MDR, regulamentul european pentru dispozitive medicale) și când e doar echipament de protecție sau de siguranță (Regulamentul UE 2016/425 pentru EIP, adică echipament individual de protecție)?
- Certificări cerute pentru zone cu pericol de explozie (ATEX, adică certificare că nu produce scântei).
- Ce se schimbă cu AI Act (legea europeană a inteligenței artificiale) dacă platforma folosește AI pentru alerte la angajați?

**3. Piața și concurenții**
- Cine vinde astfel de soluții în lume (de ex. Blackline Safety, Honeywell, Dräger, MSA, Kenzen, StrongArm, Soter Analytics, Twig, Tracker Systems etc.)?
  - Ce dispozitive au?
  - Ce prețuri au (dispozitiv plus abonament)?
  - Ce clienți au?
  - Ce venituri raportează?
- Cine vinde în România și în țările vecine (distribuitori, integratori, firme de SSM, adică securitate și sănătate în muncă)?
- Ce soluții pentru lucrul singur există deja ca aplicații de telefon și de ce nu ajung?
- Mărimea pieței: în lume, în UE, în România. Câți muncitori în industriile cu risc în Bihor și în Nord-Vest?

**4. Hardware-ul de cumpărat**
- Ce dispozitive certificate pot fi integrate printr-un API (interfață prin care programul meu citește datele dispozitivului) sau SDK (kit de programare pus la dispoziție de producător)?
  - Preț pe bucată.
  - Baterie.
  - Conectivitate (LTE-M, NB-IoT, LoRaWAN, satelit, adică tipuri de rețele pentru dispozitive mici).
  - Rezistență (IP67/IP68, adică rezistență la apă și praf).
  - ATEX.
- Ce acoperire de semnal e în zonele forestiere și montane din Bihor? Ce soluții există fără semnal (rețea proprie LoRaWAN, satelit, transmitere întârziată)?
- Ceasuri industriale rezistente și telefoane rezistente cu detectare de cădere: sunt suficiente pentru primul pilot?

**5. Clienții și prețul**
- Care sunt primele 3 industrii de atacat în Bihor și de ce: construcții, exploatare forestieră, producție, utilități, logistică, pază?
- Cine decide cumpărarea (șeful de SSM, directorul de producție, proprietarul) și cine plătește?
- Cât plătesc firmele acum pe SSM (servicii externe de SSM, echipamente de protecție, asigurări)?
- Ce preț ar accepta pe muncitor pe lună? Ce model merge: abonament, închiriere, pachet cu serviciul extern de SSM?
- Se poate vinde prin firmele de servicii externe SSM și de medicina muncii, ca partener de distribuție?
- Asigurătorii (de accidente și de răspundere civilă) ar da reduceri firmelor care folosesc dispozitivul?

**6. Riscurile ideii**
- Alarmele false și refuzul muncitorilor de a purta dispozitivul. Ce rate de adoptare raportează concurenții?
- Opoziția sindicatelor și teama de spionare. Cum au rezolvat-o alții?
- Răspunderea juridică: ce se întâmplă dacă dispozitivul nu alarmează și omul moare? Ce asigurare și ce contract trebuie?
- Dependența de un singur producător de hardware.
- Ce ar face un concurent mare dacă intră pe piața din România?

**7. Finanțare**
- Se potrivește ideea la STEP Nord-Vest (Platforma pentru Tehnologii Strategice a UE, apelul PR Nord-Vest), singură sau combinată cu proiectul PREVENT-NV din repo?
- Ce alte surse se potrivesc: POCIDIF (programul pentru digitalizare și inovare), EIT Health (rețeaua europeană de inovare în sănătate), Horizon Europe (programul UE de cercetare), programe de siguranță în muncă, granturi pentru IMM-uri (firme mici și mijlocii)?

**8. Planul de start**
- Cum arată un pilot cu 1 firmă și 20–50 de muncitori: ce cumpăr, cât costă, cât durează, ce măsor?
- Ce trebuie să existe în primele 3 luni: platforma, integrarea a 1–2 dispozitive, dispeceratul, contractele, documentele GDPR?
- Ce cifre ar dovedi că ideea merge: adoptare, alarme reale, alarme false, timp de răspuns, reînnoirea abonamentului?

### Ce vreau la final

1. Un verdict clar: merită sau nu, și pentru ce industrie să încep.
2. Cele mai importante cifre, fiecare cu sursa.
3. Lista concurenților, cu prețuri.
4. Lista dispozitivelor recomandate pentru pilot, cu prețuri.
5. Lista obligațiilor legale și ce documente îmi trebuie.
6. Planul de pilot pe 90 de zile.
7. Prețul recomandat și calculul simplu de profit pe 50, 200 și 1.000 de muncitori.
8. Cum se leagă de proiectul PREVENT-NV și de finanțarea STEP.
9. Ce nu se știe încă și cum aflu: oameni de sunat, întrebări de pus.

Marchează clar ce e fapt cu sursă, ce e estimare și ce e de verificat.
