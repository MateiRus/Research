#!/usr/bin/env python3
"""Leagă cele trei rulări anuale ale unit_economics.py (--json) într-un orizont de 36 de luni.
Calculul meu peste ieșirile uneltei: luna în care MRR trece de 1.000 și 3.000 EUR, luna în care
se recuperează cheltuiala de pornire și luna în care profitul cumulat recuperează 25.000 EUR.
    python3 -I combine_36m.py A     # citește A_numbers.out.json, A_numbers_y2.out.json, A_numbers_y3.out.json
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def run(prefix, extra=""):
    yrs = [json.load(open(os.path.join(HERE, f"{prefix}_numbers{s}{extra}.out.json"))) for s in ("", "_y2", "_y3")]
    startup = yrs[0]["startup"]
    months, cum = [], -startup
    for y, a in enumerate(yrs):
        for m in a["months"]:
            cum += m["profit"]
            months.append((y * 12 + m["month"], m["per_day"], m["revenue"], m["profit"], cum))
    first = lambda cond: next((mm for mm, *_ in months if cond(_)), None)
    mrr1k = next((mm for mm, n, rev, p, c in months if rev >= 1000), None)
    mrr3k = next((mm for mm, n, rev, p, c in months if rev >= 3000), None)
    payback = next((mm for mm, n, rev, p, c in months if c >= 0), None)
    rec25 = next((mm for mm, n, rev, p, c in months if c + startup >= 25000), None)
    out = {"startup": startup, "cash_needed": -min(c for *_, c in months + [(0, 0, 0, 0, -startup)]),
           "mrr_m12": months[11][2], "mrr_m24": months[23][2], "mrr_m36": months[35][2],
           "clients_m36": months[35][1], "month_mrr_1k": mrr1k, "month_mrr_3k": mrr3k,
           "month_startup_payback": payback, "month_cum_profit_25k": rec25,
           "cum_profit_36m_after_startup": months[35][4], "capacity": yrs[0]["capacity_per_day"],
           "max_mrr_at_capacity": (yrs[0]["capacity_per_day"] or 0) * yrs[0]["price"]}
    return out, months
if __name__ == "__main__":
    p = sys.argv[1]
    out, months = run(p)
    print(json.dumps(out, indent=1))
    with open(os.path.join(HERE, f"{p}_36m.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# {p}: 36 de luni (calculul meu peste ieșirile unit_economics.py)\n\n| luna | clienți activi | MRR (€) | profit lunar (€) | cumulat după pornire (€) |\n|---:|---:|---:|---:|---:|\n")
        for mm, n, rev, pr, c in months:
            fh.write(f"| {mm} | {n:.0f} | {rev:,.0f} | {pr:,.0f} | {c:,.0f} |\n")
        fh.write("\n" + "\n".join(f"- {k}: {v}" for k, v in out.items()) + "\n")
