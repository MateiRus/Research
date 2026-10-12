#!/usr/bin/env python3
"""Construiește intrările pentru unit_economics.py (founder-cfo), le rulează și leagă rulările anuale în 36 de luni.

Tot ce e aici e ESTIMARE (sursele și raționamentul: cfo-sources.md). Unitatea: un lucrător echipat pe o lună
("lucrător-lună"); days_per_month = 1, deci "per day" înseamnă lucrători plătitori activi în luna respectivă.

Două structuri de preț:
- C "clientul cumpără dispozitivul" (~130 EUR, cost 88,50) + abonament lunar (recomandarea cercetării pentru primii clienți);
- B "dispozitiv inclus" în abonament (dispozitivul e al ILLUSTRUS).

Două vederi:
- amortizat (scale_*.json): la B dispozitivul intră în costul variabil, amortizat pe 36 de luni; răspunde la
  „cât lasă un lucrător” la 50 / 200 / 1.000 de lucrători;
- numerar (<scenariu>_y1/y2/y3.json): la B dispozitivele cumpărate în an intră ca cheltuială de pornire a anului
  (prudent: la începutul anului); răspunde la „de câți bani am nevoie”.

Rampa pe 36 de luni e limitată de ORELE fondatorului: un client nou se acceptă doar dacă orele lunare necesare
nu depășesc orele disponibile (model de ore mai jos) și dacă a trecut ciclul minim de vânzare de la clientul anterior.

    python3 -I build_model.py
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = "/tmp/claude-0/-home-user-Research/443ae51e-6356-5470-b8f1-0cb21e6eb50e/scratchpad/ext/founder-skill/skills/founder-cfo/unit_economics.py"

# ---- modelul de ore (estimare) ----
H_PLATFORM, H_SALES = 8, 10   # întreținere platformă + test zilnic; vânzare și descoperire, pe lună
H_PILOT_FIRST, H_PILOT = 45, 20  # primul pilot (include construirea modelelor de documente) / următorii; pe 3 luni (pregătire + 60 de zile)
H_CLIENT, H_WORKER = 3, 0.05  # suport lunar pe client (raport, alarme de test, întrebări) și pe lucrător (dispozitive, baterii)
DEVICE_COST, DEVICE_SALE = 88.50, 130.0


def variable(price, structure, dispatch, channel_share, amortized, device=DEVICE_COST):
    v = []
    if structure == "B":
        if amortized:
            v.append({"label": "Dispozitiv %.2f EUR amortizat pe 36 de luni" % device, "cost": round(device / 36, 2)})
        v.append({"label": "Pierderi și defecte (10%/an din valoarea dispozitivului)", "cost": round(device * 0.10 / 12, 2)})
    else:
        v.append({"label": "Logistică garanție și schimb (dispozitivul e al clientului)", "cost": 0.25})
    v += [
        {"label": "SIM IoT multi-rețea", "cost": 1.50},
        {"label": "Dispecerat externalizat (firmă de pază), pe lucrător", "cost": dispatch},
        {"label": "Comision serviciu extern SSM (15%% x %d%% din venit)" % round(channel_share * 100), "cost": round(price * 0.15 * channel_share, 2)},
        {"label": "Garanția „luna gratuită dacă alarma nu e preluată în 60 s” (3% din venit)", "cost": round(price * 0.03, 2)},
        {"label": "Facturare și încasare (0,5%)", "cost": round(price * 0.005, 2)},
    ]
    return v


FIXED_SOLO = [
    {"label": "Găzduire UE: VM + bază de date + backup + monitorizare", "cost": 60},
    {"label": "Gateway SMS/voce pentru escaladare și test zilnic", "cost": 20},
    {"label": "Asigurare RC profesională + cyber (~1.800 EUR/an, fără ofertă reală)", "cost": 150},
    {"label": "Minim lunar la firma de pază (dispecerat), peste tariful pe lucrător", "cost": 150},
    {"label": "Contabilitate suplimentară", "cost": 30},
    {"label": "Deplasări în Bihor (teste de semnal, instruiri, schimb de dispozitive)", "cost": 100},
    {"label": "SIM-uri de test și de rezervă", "cost": 15},
]
BACKUP = {"label": "Inginer de rezervă la apel pentru platformă (retainer)", "cost": 150}

STARTUP_Y1 = [
    {"label": "Avocat: contract abonament + subcontract dispecerat, art. 28 GDPR, clauze de răspundere, opinie L333/2003", "cost": 2500},
    {"label": "Revizia modelelor de documente SSM/DPIA de un consultant SSM", "cost": 500},
    {"label": "Parc de pilot: 23 x Teltonika TMT250 (88,50 EUR), refolosit de la un pilot la altul", "cost": 2036},
    {"label": "3 dispozitive LTE alternative de test (riscul 2G / End of life, ~177 EUR)", "cost": 530},
    {"label": "Test end-to-end cu firma de pază: 50 de alarme simulate, zi și noapte", "cost": 300},
    {"label": "Găzduire în cele 3 luni de construcție", "cost": 180},
    {"label": "Materiale de vânzare: ghidul „Lucru izolat după HG 1091/2006”, pagină web", "cost": 300},
    {"label": "Deplasări de descoperire și teste de semnal gratuite", "cost": 200},
]

SCENARIOS = {
    "base": dict(structure="C", price=12, dispatch=2.50, start_size=20, step=10, cap=40, first=6, gap=3,
                 churn=None, failed_pilot_ratio=0.5, hours_y1=48, hours_later=48,
                 label="Bază: clientul cumpără dispozitivul + 12 EUR/lună; 10–12 h/săpt; client nou la ≥3 luni, 20 → 40 de lucrători"),
    "baseB": dict(structure="B", price=14, dispatch=2.50, start_size=20, step=10, cap=40, first=6, gap=3,
                  churn=None, failed_pilot_ratio=0.5, hours_y1=48, hours_later=48,
                  label="Varianta B: dispozitiv inclus, 14 EUR/lună (pitch-ul v2); aceleași ore și aceeași rampă"),
    "pess": dict(structure="C", price=10, dispatch=4.00, start_size=15, step=5, cap=25, first=8, gap=6,
                 churn=(1, 20), failed_pilot_ratio=1.0, hours_y1=48, hours_later=48,
                 label="Pesimist: 10 EUR/lună, dispecerat 4 EUR, client nou la ≥6 luni, 15 → 25 de lucrători, jumătate din piloți pică, primul client pleacă în luna 20"),
    "h20": dict(structure="C", price=12, dispatch=2.50, start_size=20, step=10, cap=40, first=6, gap=3, gap_later=2,
                churn=None, failed_pilot_ratio=0.5, hours_y1=48, hours_later=87,
                label="20 h/săpt din luna 13: clientul cumpără dispozitivul + 12 EUR/lună, client nou la ≥2 luni"),
}


def workers(sc, starts, m):
    n = clients = 0
    for k, s in enumerate(starts):
        if m < s:
            continue
        if sc["churn"] and k == sc["churn"][0] - 1 and m >= sc["churn"][1]:
            continue
        n += min(sc["cap"], sc["start_size"] + sc["step"] * ((m - s) // 6))
        clients += 1
    return n, clients


def hours(sc, starts, m):
    n, clients = workers(sc, starts, m)
    pilot_h = 0.0
    for k, s in enumerate(starts):
        if s - 3 <= m < s:
            pilot_h += ((H_PILOT_FIRST if k == 0 else H_PILOT) + sc["failed_pilot_ratio"] * H_PILOT) / 3
    return H_PLATFORM + H_SALES + pilot_h + clients * H_CLIENT + n * H_WORKER


def avail(sc, m):
    return sc["hours_y1"] if m <= 12 else sc["hours_later"]


def schedule(sc):
    starts = []
    for s in range(sc["first"], 37):
        gap = sc["gap"] if s <= 12 else sc.get("gap_later", sc["gap"])
        if starts and s - starts[-1] < gap:
            continue
        trial = starts + [s]
        if all(hours(sc, trial, m) <= avail(sc, m) + 1e-9 for m in range(1, 37)):
            starts = trial
    return starts


def numbers(sc, starts, year):
    rng = range((year - 1) * 12 + 1, year * 12 + 1)
    ramp = [workers(sc, starts, m)[0] for m in rng]
    channel = 0.0 if year == 1 else 0.30
    fixed = list(FIXED_SOLO) + ([BACKUP] if year > 1 else [])
    if sc["hours_later"] > 48 and year > 1:
        fixed.append({"label": "Deplasări suplimentare (ritm dublu de vânzare)", "cost": 100})
    startup = list(STARTUP_Y1) if year == 1 else []
    if sc["structure"] == "B":
        prev_end = workers(sc, starts, (year - 1) * 12)[0] if year > 1 else 0
        new = max(0, max(ramp) - prev_end)
        startup.append({"label": "Dispozitive cumpărate pentru lucrătorii noi din anul %d (%d x %.2f EUR + 10%% rezervă)" % (year, new, DEVICE_COST),
                        "cost": round(new * DEVICE_COST * 1.10, 2)})
    if not startup:
        startup = [{"label": "Nicio cheltuială de pornire nouă în anul %d" % year, "cost": 0}]
    return {
        "business": "Lucru izolat conform, la cheie (ILLUSTRUS) · %s · anul %d · vedere numerar" % (sc["label"], year),
        "unit": "lucrător-lună", "price": sc["price"],
        "variable": variable(sc["price"], sc["structure"], sc["dispatch"], channel, amortized=False),
        "fixed_monthly": fixed, "startup": startup, "days_per_month": 1,
        "plan_per_day": max(ramp) or 1, "ramp_per_day": ramp,
    }


def scale(n, fixed, structure, price):
    return {
        "business": "Lucru izolat conform, la cheie (ILLUSTRUS) · stare stabilă la %d de lucrători · structura %s · vedere amortizată" % (n, structure),
        "unit": "lucrător-lună", "price": price,
        "variable": variable(price, structure, 2.50, 0.30, amortized=True),
        "fixed_monthly": fixed, "startup": [STARTUP_Y1[i] for i in (0, 1, 4, 5, 6, 7)], "days_per_month": 1,
        "plan_per_day": n,
    }


def run_tool(path, md=None, extra=()):
    if md:
        subprocess.run([sys.executable, "-I", TOOL, path, "--out", md] + list(extra), check=True, capture_output=True)
    r = subprocess.run([sys.executable, "-I", TOOL, path, "--json"] + list(extra), check=True, capture_output=True, text=True)
    return json.loads(r.stdout)


def main():
    out = {"scale": {}}
    staff200 = FIXED_SOLO + [BACKUP, {"label": "Ajutor part-time 0,25 normă (instalări, schimb dispozitive)", "cost": 300}]
    staff1000 = [{"label": "2 angajați (suport, instalare, vânzare) x 1.200 EUR cost complet", "cost": 2400},
                 {"label": "Găzduire UE la scară + monitorizare", "cost": 150},
                 {"label": "Asigurare RC profesională + cyber la scară", "cost": 300},
                 {"label": "Contabilitate și salarizare", "cost": 80},
                 {"label": "Deplasări", "cost": 200}]
    # prețurile se schimbă prin fișiere separate (nu prin --price), ca procentele din costul variabil să urmeze prețul
    for n, fx in ((50, FIXED_SOLO), (200, staff200), (1000, staff1000)):
        for structure, price in (("C", 12), ("C", 10), ("B", 14), ("B", 20)):
            tag = "scale_%d_%s%d" % (n, structure, price)
            p = os.path.join(HERE, tag + ".json")
            json.dump(scale(n, fx, structure, price), open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            a = run_tool(p, os.path.join(HERE, tag + "_cfo.md"))
            be = a["breakeven_per_day"]
            out["scale"][tag] = {"contribution": round(a["contribution"], 2), "contribution_pct": round(a["contribution_pct"], 3),
                                 "fixed": a["fixed_monthly"], "monthly_result": round(a["months"][0]["profit"]),
                                 "margin": round(a["margin_at_plan"], 3), "breakeven_workers": None if be is None else round(be, 1),
                                 "device_capital_if_B": round(n * DEVICE_COST) if structure == "B" else 0}
    lines = ["# Modelul pe 36 de luni (calculul meu peste ieșirile `unit_economics.py`)", "",
             "Toate cifrele sunt **estimări**. Unealta calculează abonamentele. Două încasări unice sunt adunate de mine, nu de unealtă: taxele de pilot (500 EUR/pilot, inclusiv piloții care nu se convertesc) și, la structura C, marja de ~41,50 EUR pe dispozitivul vândut clientului (130 − 88,50). La structura B, dispozitivele cumpărate într-un an sunt scăzute la începutul anului (prudent).", ""]
    for name, sc in SCENARIOS.items():
        starts = schedule(sc)
        yrs = []
        for y in (1, 2, 3):
            p = os.path.join(HERE, "%s_y%d.json" % (name, y))
            json.dump(numbers(sc, starts, y), open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            yrs.append(run_tool(p, os.path.join(HERE, "%s_y%d_cfo.md" % (name, y))))
        fee_per_conv = 500 * (1 + sc["failed_pilot_ratio"])
        cum, rows, prev_n = 0.0, [], 0
        for y, a in enumerate(yrs):
            cum -= a["startup"]
            for mm in a["months"]:
                m = y * 12 + mm["month"]
                n, clients = workers(sc, starts, m)
                once = (fee_per_conv if (m + 3) in starts else 0)
                if sc["structure"] == "C":
                    once += max(0, n - prev_n) * (DEVICE_SALE - DEVICE_COST)
                prev_n = n
                cum += mm["profit"] + once
                rows.append((m, n, clients, mm["revenue"], mm["profit"] + once, cum, round(hours(sc, starts, m), 1), avail(sc, m)))
        first = lambda f: next((r[0] for r in rows if f(r)), None)
        res = {
            "label": sc["label"], "structure": sc["structure"], "price": sc["price"], "client_starts": starts,
            "contribution_y1": round(yrs[0]["contribution"], 2), "contribution_y2": round(yrs[1]["contribution"], 2),
            "startup_y1": yrs[0]["startup"], "startup_y2": yrs[1]["startup"], "startup_y3": yrs[2]["startup"],
            "cash_needed_36m": round(-min([r[5] for r in rows] + [0])),
            "year1_result_all_in": round(rows[11][5]), "year2_result": round(sum(r[4] for r in rows[12:24]) - yrs[1]["startup"]),
            "year3_result": round(sum(r[4] for r in rows[24:36]) - yrs[2]["startup"]),
            "mrr_m12": rows[11][3], "mrr_m24": rows[23][3], "mrr_m36": rows[35][3],
            "workers_m12": rows[11][1], "workers_m24": rows[23][1], "workers_m36": rows[35][1],
            "clients_m36": rows[35][2],
            "month_mrr_1000": first(lambda r: r[3] >= 1000), "month_mrr_3000": first(lambda r: r[3] >= 3000),
            "month_cumulative_back_to_zero": first(lambda r: r[0] > 1 and r[5] >= 0),
            "cumulative_36m": round(rows[35][5]), "peak_hours": max(r[6] for r in rows),
        }
        out[name] = res
        lines += ["## %s" % sc["label"], "", "Clienți noi (luna în care încep să plătească abonamentul): %s." % starts, "",
                  "| luna | lucrători plătitori | clienți | MRR (EUR) | rezultat lunar cu încasări unice (EUR) | cumulat după toate cheltuielile (EUR) | ore necesare / disponibile |",
                  "|---:|---:|---:|---:|---:|---:|---:|"]
        for r in rows:
            lines.append("| %d | %d | %d | %s | %s | %s | %s / %s |" % (r[0], r[1], r[2], "{:,.0f}".format(r[3]), "{:,.0f}".format(r[4]), "{:,.0f}".format(r[5]), r[6], r[7]))
        lines += [""] + ["- %s: %s" % (k, v) for k, v in res.items()] + [""]
    open(os.path.join(HERE, "model_36m.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump(out, open(os.path.join(HERE, "model_36m.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
