#!/usr/bin/env python3
"""Scorarea ponderată a oportunităților (sarcina A). Doar biblioteca standard.

Scara 1-5 pentru fiecare criteriu, ÎNTOTDEAUNA orientată „5 = favorabil fondatorului”:
pentru criteriile negative (concurență, dificultate tehnică, complexitate de reglementare,
nevoie de parteneriate clinice, efort MVP, capital, dificultatea achiziției, dependența de
platforme terțe) 5 înseamnă „puțin / ușor / mic”.

Scor total = suma(pondere x scor) / 5, deci pe o scară 0-100 (20 = totul 1, 100 = totul 5).

Notele (scorurile) sunt estimările mele, sprijinite pe notele de cercetare. Justificarea
ponderilor și a notelor-cheie e în analiza_founder.md, secțiunile A și B (motivul fiecărui
flag e în câmpul de după flag).

    python3 -I scoring.py            # scrie scoring.csv, scoring_table.md, sensitivity.md
"""
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# (cod, nume criteriu, pondere de bază)
CRITERII = [
    ("U", "Urgență reală la client", 10),
    ("P", "Capacitate și disponibilitate de plată", 10),
    ("C", "Concurență existentă (5 = puțină)", 5),
    ("RO", "Oportunitate în România / Bihor", 6),
    ("INT", "Potențial internațional", 2),
    ("T", "Dificultate tehnică (5 = ușor)", 2),
    ("D", "Acces la datele necesare (5 = ușor)", 8),
    ("R", "Complexitate de reglementare (5 = mică)", 6),
    ("CL", "Nevoie de parteneriate clinice (5 = deloc)", 4),
    ("S", "Fezabil ca dezvoltator solo", 6),
    ("M", "Efort MVP (5 = mic)", 4),
    ("K", "Capital de pornire (5 = mic)", 2),
    ("V", "Potențial de venit recurent", 8),
    ("A", "Achiziția clienților (5 = ușoară)", 10),
    ("DF", "Forța diferențierii", 6),
    ("PT", "Dependență de platforme terțe (5 = mică)", 3),
    ("ST", "Relevanță strategică pentru sănătatea predictivă", 8),
]
assert sum(w for _, _, w in CRITERII) == 100

# Seturi alternative de ponderi pentru testul de robustețe (nu schimbă scorurile, doar ponderile)
ALTERNATIVE = {
    "egale": {c: 100 / len(CRITERII) for c, _, _ in CRITERII},
    "fezabilitate-întâi": {"U": 7, "P": 7, "C": 4, "RO": 5, "INT": 1, "T": 5, "D": 12, "R": 10, "CL": 7,
                           "S": 10, "M": 7, "K": 4, "V": 6, "A": 7, "DF": 3, "PT": 3, "ST": 2},
    "strategic-întâi": {"U": 8, "P": 8, "C": 5, "RO": 5, "INT": 5, "T": 2, "D": 7, "R": 5, "CL": 3,
                        "S": 5, "M": 3, "K": 2, "V": 8, "A": 8, "DF": 8, "PT": 3, "ST": 15},
}
for k, v in ALTERNATIVE.items():
    assert abs(sum(v.values()) - 100) < 1e-6, k

ORDER = [c for c, _, _ in CRITERII]

# Flag de dependență fatală:
#   ""   = nimic
#   "W"  = avertisment: o condiție care trebuie verificată în validarea de 90 de zile
#   "X"  = fatal ca PRIM produs: date inaccesibile, validare/certificare inaccesibilă ca cost,
#          plătitor inexistent sau canal blocat de un singur actor. Exclus din top 10 indiferent de scor.
# Tipuri: D = date, V = validare/certificare, P = plătitor, I = integrare/API, C = canal cu un singur cumpărător
OPP = [
    # cod, origine, nume scurt, scoruri U P C RO INT T D R CL S M K V A DF PT ST, flag, motiv flag
    ("A", "O2 + RSMM §3", "Scadențar MM + portal angajator + registrul recomandărilor (cabinete MM independente)",
     [3, 3, 3, 4, 2, 5, 4, 4, 4, 4, 4, 5, 5, 3, 3, 4, 4], "W",
     "P/D: plata cabinetelor și exportul din softul MM existent sunt neverificate"),
    ("B", "variantă nouă (RSMM §3)", "Scadențar MM vândut direct angajatorilor (HR), indiferent de furnizor",
     [3, 2, 3, 3, 2, 5, 5, 4, 5, 5, 5, 5, 4, 2, 2, 5, 2], "W",
     "P: plata HR-ului nedovedită; substitut gratuit (Excel)"),
    ("C", "O9", "Ziua de prevenție la locul de muncă (treapta 2 a lui A)",
     [2, 3, 3, 3, 2, 4, 3, 4, 2, 2, 3, 4, 2, 3, 4, 3, 4], "W",
     "P + parteneri: apetitul angajatorilor neverificat; laborator partener necesar"),
    ("D", "O17 + CONS KQ3", "Arhiva longitudinală de expunere profesională (+ structurarea PDF-urilor de audiometrie/spirometrie)",
     [2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 2, 4, 4, 5], "W",
     "piață: numărul lucrătorilor expuși din Bihor necunoscut"),
    ("E", "O1 (+O18)", "Navigator FIT pozitiv -> colonoscopie pentru ROCCAS 4 NV, cu dispecerat de capacitate",
     [3, 3, 3, 3, 3, 4, 2, 4, 1, 3, 3, 4, 2, 1, 4, 2, 5], "X",
     "C/D: un singur cumpărător, achiziții UE; date doar prin contract cu consorțiul"),
    ("F", "O3", "Inbox de urmărire a rezultatelor în afara intervalului (laboratoare independente)",
     [3, 2, 3, 2, 3, 3, 2, 3, 3, 3, 3, 4, 4, 2, 3, 3, 5], "W",
     "D: un singur laborator independent găsit în Bihor; LIS necunoscut"),
    ("G", "nouă (FUR §2-3, RSMM §5)", "Bucle deschise în clinici independente de boli cronice: control scadent, rezultat anormal fără programare, trimitere neînchisă",
     [3, 3, 3, 3, 3, 4, 3, 4, 4, 4, 4, 5, 4, 3, 3, 3, 4], "W",
     "D: export din PMS fără API; consimțământ pentru SMS (Legea 506/2004)"),
    ("H", "O8", "Rechemarea pentru pachetul CNAS de prevenție 40+/60+ (medici de familie)",
     [2, 2, 3, 4, 2, 4, 3, 4, 4, 4, 4, 5, 4, 2, 3, 3, 4], "W",
     "P: cât plătește CNAS per serviciu de prevenție lipsește din note; dacă e ~0, devine fatal"),
    ("I", "O5", "Urmărirea biletelor de trimitere (medici de familie)",
     [2, 2, 3, 3, 2, 4, 2, 4, 4, 4, 4, 5, 3, 2, 2, 2, 3], "W",
     "P: nu știm dacă medicii de familie plătesc"),
    ("J", "O4", "Navigator după notificarea de la ceas (clinici de cardiologie)",
     [2, 3, 4, 2, 3, 4, 4, 3, 3, 4, 4, 5, 2, 3, 3, 4, 4], "W",
     "volum: penetrarea wearable-urilor în România necunoscută"),
    ("K", "O7 (L4)", "Urmărirea pacienților de turism dentar (Oradea)",
     [3, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 5, 4, 3, 3, 3, 2], "W",
     "volum: turismul dentar din Bihor necunoscut"),
    ("L", "nouă (EMG §L, FUR §3)", "Remindere și reducerea absențelor, cu grup de control (clinici private, stomatologie)",
     [3, 3, 1, 3, 3, 4, 3, 4, 5, 4, 4, 5, 4, 3, 2, 3, 2], "",
     ""),
    ("M", "O10", "Raport de finalizare a prevenției pentru abonamente corporate (clinici medii)",
     [2, 2, 2, 2, 2, 4, 3, 4, 4, 4, 4, 5, 4, 2, 3, 4, 3], "W",
     "P: cererea angajatorilor pentru analiză nu a fost găsită"),
    ("N", "O11", "Meniu fix de prevenție bazată pe dovezi în bugetul de 400 EUR",
     [2, 3, 2, 3, 2, 4, 4, 3, 2, 3, 3, 4, 3, 2, 4, 2, 3], "W",
     "parteneri: laborator + medic care semnează meniul; tratament fiscal de verificat"),
    ("O", "O12", "Auditul „pauza” (dez-implementare) pentru asigurători",
     [3, 3, 4, 2, 3, 4, 1, 4, 1, 2, 3, 4, 2, 1, 4, 3, 3], "X",
     "D: fără acces la datele de daune ale asigurătorilor și fără rețea în asigurări"),
    ("P", "O14", "Puntea e-SănătateaMea pentru furnizori mici cu contract CNAS",
     [3, 2, 2, 3, 1, 3, 1, 3, 4, 3, 2, 4, 4, 2, 2, 1, 2], "X",
     "I: niciun API public pentru terți găsit"),
    ("Q", "O15", "Componente EHDS (fațadă FHIR, IPS, jurnalizare) pentru vendori locali",
     [2, 3, 3, 3, 4, 2, 5, 3, 5, 3, 2, 4, 3, 2, 4, 3, 4], "W",
     "timp: venit realist abia 2027-2028; reguli românești de aplicare lipsă"),
    ("R", "O16", "Jurnal de acces și cereri de acces la dosar (clinici private)",
     [2, 2, 3, 3, 3, 4, 3, 4, 5, 4, 4, 5, 4, 2, 3, 3, 2], "",
     ""),
    ("S", "O21", "PDF-uri vechi -> tabel de valori pentru medic (check-up)",
     [2, 2, 3, 3, 3, 3, 4, 2, 3, 4, 4, 5, 3, 2, 2, 3, 4], "W",
     "răspundere: erorile de extracție intră sub PLD din 9.12.2026"),
    ("T", "O19 / MON §2", "Atelier RPM pentru un program privat de hipertensiune (cu alerte)",
     [2, 1, 3, 1, 3, 3, 3, 1, 1, 2, 2, 2, 4, 1, 3, 2, 5], "X",
     "V+P: alertele = MDSW IIa (32-110k EUR, 9-18 luni); nicio rambursare RPM în România"),
    ("U", "O25", "Predicția buclelor care nu se vor închide, ca PRIM produs",
     [2, 2, 3, 2, 3, 2, 1, 2, 3, 3, 2, 4, 4, 2, 4, 4, 5], "X",
     "D: istoricul buclelor nu există încă; profilare cu date de sănătate = consimțământ explicit"),
    ("V", "F4 fundături", "Scor de risc individual în fluxul medicului (SCORE2/FINDRISC) sau model propriu",
     [2, 2, 2, 2, 3, 3, 2, 1, 1, 2, 2, 1, 3, 2, 2, 3, 5], "X",
     "V: MDSW clasa IIa, fără excepție CDS în UE; validare clinică inaccesibilă"),
    # --- adăugate la reluare (9 oct 2026): restul oportunităților din analiza laterală, ca tabelul să le acopere pe toate
    #     (O24 nu e notat: e unealtă de vânzare, nu afacere; O18 apare și ca modul în E)
    ("W", "O6", "Check-in administrativ după chirurgia de zi (oftalmologie, ortopedie)",
     [2, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 4, 3, 2, 3, 3, 3], "W",
     "R: la granița triajului; răspundere pentru semnale ratate (PLD din 9.12.2026)"),
    ("Y", "O13", "Platformă de operare pentru programe de prevenție a diabetului (tip DPP), plătite de angajatori",
     [2, 1, 3, 1, 3, 4, 3, 3, 2, 3, 3, 4, 4, 1, 3, 3, 4], "X",
     "P: niciun program sau plătitor DPP găsit în România"),
    ("Z", "O18", "Dispecerat de capacitate pentru campanii de invitații (endoscopie, imagistică), ca produs separat",
     [2, 2, 3, 2, 3, 4, 3, 5, 4, 4, 4, 5, 3, 2, 3, 3, 3], "W",
     "volum: campaniile sunt rare; merge mai bine ca modul (în E sau G)"),
    ("AA", "O20", "Monitor local de performanță pentru AI marcat CE (imagistică, screening)",
     [1, 2, 4, 1, 4, 3, 1, 4, 2, 3, 3, 4, 4, 1, 4, 3, 4], "X",
     "D/P: niciun utilizator român de AI marcat CE găsit; fără acces la radiologie; obligațiile Art. 26 abia din 2028"),
    ("AB", "O22", "Jurnal de evenimente și escaladare pentru cămine și îngrijire la domiciliu",
     [2, 1, 3, 2, 2, 5, 4, 4, 4, 4, 4, 5, 4, 2, 2, 4, 2], "W",
     "piață: căminele din Bihor neverificate; bugete mici, piață fragmentată"),
    ("AC", "O23", "Predarea la pensionare: ultimul examen MM → medicul de familie",
     [1, 1, 4, 2, 2, 5, 3, 4, 3, 4, 4, 5, 2, 1, 3, 4, 3], "X",
     "P: niciun plătitor identificat"),
    ("AD", "O26", "Coordonator pentru părinții din România ai familiilor din diaspora (B2C)",
     [2, 2, 3, 3, 3, 4, 2, 4, 3, 1, 4, 4, 4, 1, 3, 3, 2], "W",
     "P/S: B2C (consumatorii plătesc doar ca „membri captivi”); serviciu cu om, nu scalează solo"),
]


def score(scores, weights):
    return sum(weights[c] * s for c, s in zip(ORDER, scores)) / 5.0


def main():
    base = {c: w for c, _, w in CRITERII}
    rows = []
    for code, origin, name, s, flag, why in OPP:
        assert len(s) == len(ORDER), code
        assert all(1 <= x <= 5 for x in s), code
        r = {"cod": code, "origine": origin, "oportunitate": name, "flag": flag, "motiv_flag": why}
        r.update({c: v for c, v in zip(ORDER, s)})
        r["scor"] = round(score(s, base), 1)
        for k, w in ALTERNATIVE.items():
            r["scor_" + k] = round(score(s, w), 1)
        rows.append(r)
    rows.sort(key=lambda r: -r["scor"])
    eligible = [r for r in rows if r["flag"] != "X"]
    for i, r in enumerate(rows, 1):
        r["loc_brut"] = i
    for i, r in enumerate(eligible, 1):
        r["loc_eligibil"] = i
    # ranks under alternatives (eligible only)
    for k in ALTERNATIVE:
        alt = sorted(eligible, key=lambda r: -r["scor_" + k])
        for i, r in enumerate(alt, 1):
            r["loc_" + k] = i

    with open(os.path.join(HERE, "scoring.csv"), "w", newline="", encoding="utf-8") as fh:
        cols = ["loc_brut", "loc_eligibil", "cod", "origine", "oportunitate"] + ORDER + \
               ["scor"] + ["scor_" + k for k in ALTERNATIVE] + ["flag", "motiv_flag"]
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    flagtxt = {"": "—", "W": "⚠", "X": "⛔"}
    L = ["| Loc | Cod | Origine | Oportunitate | " + " | ".join(ORDER) + " | **Scor /100** | Flag | Motivul flagului |",
         "|---:|---|---|---|" + "---:|" * len(ORDER) + "---:|---|---|",
         "| | | | **Pondere** | " + " | ".join(str(base[c]) for c in ORDER) + " | 100 | | |"]
    for r in rows:
        loc = str(r.get("loc_eligibil", "")) if r["flag"] != "X" else "excl."
        L.append("| %s | %s | %s | %s | %s | **%.1f** | %s | %s |" % (
            loc, r["cod"], r["origine"], r["oportunitate"], " | ".join(str(r[c]) for c in ORDER),
            r["scor"], flagtxt[r["flag"]], r["motiv_flag"] or "—"))
    with open(os.path.join(HERE, "scoring_table.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")

    S = ["| Cod | Oportunitate | Bază | Loc | Egale | Loc | Fezabilitate-întâi | Loc | Strategic-întâi | Loc |",
         "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in eligible:
        S.append("| %s | %s | %.1f | %d | %.1f | %d | %.1f | %d | %.1f | %d |" % (
            r["cod"], r["oportunitate"][:60], r["scor"], r["loc_eligibil"],
            r["scor_egale"], r["loc_egale"], r["scor_fezabilitate-întâi"], r["loc_fezabilitate-întâi"],
            r["scor_strategic-întâi"], r["loc_strategic-întâi"]))
    with open(os.path.join(HERE, "sensitivity.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(S) + "\n")
    with open(os.path.join(HERE, "weights.json"), "w", encoding="utf-8") as fh:
        json.dump({"baza": base, **ALTERNATIVE}, fh, indent=1, ensure_ascii=False)

    for r in rows:
        print("%-4s %-3s %5.1f  %s  %s" % (r.get("loc_eligibil", "x") if r["flag"] != "X" else "x",
                                         r["cod"], r["scor"], flagtxt[r["flag"]], r["oportunitate"][:70]))


if __name__ == "__main__":
    main()
