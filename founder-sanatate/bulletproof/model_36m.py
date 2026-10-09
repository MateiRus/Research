# Model simplu de 36 de luni pentru rundele bulletproof (calculul meu). Toate intrarile sunt estimari, nu oferte reale.
# Rulare: python3 -I model_36m.py
import json, sys

def run(name, price_fn, var=4.0, fixed_fn=lambda m: 230, startup=2980,
        new_fn=lambda m: 0, refund_share=0.2, churn=0.015, cap_fn=lambda m: 25,
        addon_fn=lambda m, n: 0.0, months=36):
    cohorts = []  # list of [start_month, count]
    active = 0.0
    rows = []
    cum = -startup
    first1k = first3k = None
    y1 = 0.0
    for m in range(1, months + 1):
        # churn on existing
        active *= (1 - churn)
        # guarantee refunds: share of cohort that started 3 months ago leaves
        for c in cohorts:
            if m - c[0] == 3:
                active -= c[1] * refund_share
        new = new_fn(m)
        room = max(0.0, cap_fn(m) - active)
        new = min(new, room)
        if new > 0:
            cohorts.append([m, new])
            active += new
        price = price_fn(m)
        mrr = active * price + addon_fn(m, active)
        contrib = active * (price - var) + addon_fn(m, active)
        # refunds cost: refunded clients get back 3 months
        refund_cost = sum(c[1] * refund_share * 3 * price for c in cohorts if m - c[0] == 3)
        profit = contrib - fixed_fn(m) - refund_cost
        cum += profit
        if m <= 12:
            y1 += profit
        if first1k is None and mrr >= 1000: first1k = m
        if first3k is None and mrr >= 3000: first3k = m
        rows.append((m, round(active, 1), round(mrr), round(profit), round(cum)))
    out = {
        "name": name,
        "mrr_m12": rows[11][2], "mrr_m18": rows[17][2], "mrr_m24": rows[23][2], "mrr_m36": rows[35][2],
        "clients_m12": rows[11][1], "clients_m24": rows[23][1], "clients_m36": rows[35][1],
        "y1_profit": round(y1), "month_1k": first1k, "month_3k": first3k,
        "min_cum": min(r[4] for r in rows), "cum_m36": rows[35][4],
    }
    return out, rows

scen = {}
# R0 replica (no churn, no refunds): +1/luna din luna 4 (2 in luna 4), plafon 25
def r0_new(m):
    if m < 4: return 0
    if m == 4: return 2
    return 1
scen['R0_replica'] = run('R0 (replica, fara churn)', lambda m: 65, new_fn=r0_new, refund_share=0.0, churn=0.0)

# R1 stress: same ramp, with refunds 20% at month 3 and churn 1.5%/luna
scen['R0_with_churn'] = run('R0 + churn 1,5%/luna + 20% refund garantie', lambda m: 65, new_fn=r0_new, refund_share=0.2, churn=0.015)

# R0 with time-consistent ramp: sales hours 30h/client, capacity 52h/luna -> after 10 clients slows to 0.5/luna
def r0_time(m, act_holder=[0]):
    return 0
# approximate: +1/luna din luna 4 pana la luna 12, apoi 0.6/luna
def ramp_time(m):
    if m < 4: return 0
    if m == 4: return 2
    if m <= 12: return 1
    return 0.6
scen['R0_time_churn'] = run('R0 cu timp realist + churn', lambda m: 65, new_fn=ramp_time, refund_share=0.2, churn=0.015)

# Plan v1 (runda 1): mix spre firme medii -> pret mediu 74; garantie doar dupa audit/calificare -> refund 10%;
# churn 1,5%; pilot concierge; prima plata luna 3 (3 piloti), +1/luna pana la 12, apoi +1/luna (referinte + adaptoare reduc CAC la ~15 h)
# costuri: fix 230 + 0 ; startup 2980 + 600 (opinie juridica) + 0
def v1_new(m):
    if m < 3: return 0
    if m == 3: return 3
    if m <= 12: return 1
    return 0.8
scen['v1'] = run('Plan v1', lambda m: 74, new_fn=v1_new, refund_share=0.10, churn=0.015, startup=3580, cap_fn=lambda m: 25)

# Plan v2: + plata anuala in avans (nu schimba MRR), + operator part-time din luna 13 (400 EUR/luna) -> plafon 40
# ramp: +1/luna m4-12, +1.5/luna m13-36 (canal: referinte, webinar asociatie, 1 vendor ca partener optional)
def v2_new(m):
    if m < 3: return 0
    if m == 3: return 3
    if m <= 12: return 1
    return 1.5
scen['v2'] = run('Plan v2', lambda m: 74, new_fn=v2_new, refund_share=0.10, churn=0.015, startup=3580,
                 fixed_fn=lambda m: 230 if m <= 12 else 630, cap_fn=lambda m: 25 if m <= 12 else 40)

# Plan v3 (final): ca v2 + modul Preventie (inchiderea recomandarilor + ziua de preventie) din luna 19
# la 30% din clienti, 60 EUR/luna/client in medie (ipoteza de testat); consilier medical MM 150 EUR/luna din luna 13
def v3_addon(m, n):
    if m < 19: return 0.0
    share = min(0.30, 0.05 * (m - 18))
    return n * share * 60
scen['v3'] = run('Plan v3', lambda m: 74, new_fn=v2_new, refund_share=0.10, churn=0.015, startup=3580,
                 fixed_fn=lambda m: 230 if m <= 12 else 780, cap_fn=lambda m: 25 if m <= 12 else 40, addon_fn=v3_addon)

# v3 fara modul: ca v3 (ajutor part-time + responsabil medical din luna 13), dar fara venitul din modul
scen['v3_nomod'] = run('Plan v3 fara modul', lambda m: 74, new_fn=v2_new, refund_share=0.10, churn=0.015, startup=3580,
                 fixed_fn=lambda m: 230 if m <= 12 else 780, cap_fn=lambda m: 25 if m <= 12 else 40)

# v3 pesimist: jumatate din ritm, churn 2,5%
def v3p_new(m):
    if m < 4: return 0
    if m == 4: return 2
    if m <= 12: return 0.5
    return 0.8
scen['v3_pess'] = run('Plan v3 pesimist', lambda m: 65, new_fn=v3p_new, refund_share=0.15, churn=0.025, startup=3580,
                 fixed_fn=lambda m: 230 if m <= 18 else 630, cap_fn=lambda m: 25 if m <= 18 else 40,
                 addon_fn=lambda m, n: 0.0 if m < 24 else n * 0.15 * 60)

for k, (o, rows) in scen.items():
    print(json.dumps(o, ensure_ascii=False))
print()
for k in ['R0_with_churn', 'v3']:
    print(k)
    for r in scen[k][1]:
        if r[0] in (3,4,6,9,12,15,18,21,24,30,36): print(r)
