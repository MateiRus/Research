# Model simplu de numerar pe 24 de luni (luna 1 = noiembrie 2026) pentru planul intarit.
# TOATE intrarile sunt estimari ale evaluatorului, nu oferte reale. Rulare: python3 -I model_24m.py
# Reperele de unde pornesc estimarile: raportul, sectiunile 6 si 7; nota 05, sectiunea 4.

CAPACITATE_ORE = 11 * 4.3          # 10-12 h/saptamana -> ~47 h/luna
CASH_START = 25000.0

def run(nume, pilot_start, pilot_conv, nou_pe_luna, churn, prob_pilot_ok=True, pret=12.0,
        pret_rezerva=16.0, pondere_rezerva=0.3, luni=24, salariu_fondator=0.0):
    cash = CASH_START
    lucr = 0.0
    rows = []
    min_cash = cash
    angajat = False
    for m in range(1, luni + 1):
        cost = 0.0
        venit = 0.0
        ore = 0.0
        if not prob_pilot_ok and m > pilot_conv:
            rows.append((m, 0, 0, 0, 0, round(cash), 0, 0))
            continue  # afacerea se opreste: nu mai cheltuim nimic
        if m >= pilot_conv and prob_pilot_ok: cost += salariu_fondator
        # --- unice (estimare) ---
        if m == 1: cost += 300            # materiale de vanzare, deplasari interviuri
        if m == 2: cost += 1500 + 450 + 100  # aviz avocat + contract-tip; 3 dispozitive mostra + SIM; zi de masurare semnal
        if m == pilot_start - 1: cost += 900  # asigurare RC profesionala, prima anuala (pret necunoscut)
        if m == pilot_start + 11: cost += 900
        # --- fixe lunare ---
        if m >= 3: cost += 80 + 20 + 30   # gazduire administrata pe 2 noduri + monitorizare, poarta SMS, unelte
        if m >= pilot_start - 1: cost += 200  # tehnician de rezerva cu abonament (bus factor)
        # --- ore fondator ---
        if m <= 2: ore += 35              # interviuri si calificare
        if 3 <= m < pilot_start: ore += 45  # constructie (120-160 h in total) + documente
        ore += 8                          # administrare de baza
        # --- pilot ---
        if pilot_start <= m < pilot_start + 3:
            lucr = 30.0
            venit += 30 * pret * 0.5      # pilot platit la jumatate de pret, cumparat direct
            ore += 20                     # insotire pilot, rapoarte saptamanale
            if m == pilot_start: venit += 30 * 20  # marja pe dispozitivele cumparate de client (20 EUR/buc)
        elif m >= pilot_conv:
            if not prob_pilot_ok:
                lucr = 0.0
            else:
                if m > pilot_conv: lucr = lucr * (1 - churn)
                nou = nou_pe_luna if m > pilot_conv else 0
                lucr += nou
                venit += nou * 20         # marja dispozitiv
                ore += nou * 0.5          # instruire si configurare
                ore += 15 + (nou / 25.0) * 20  # prospectare + ciclu de vanzare (~20 h pe client nou de ~25 lucratori)
                pret_mediu = pret * (1 - pondere_rezerva) + pret_rezerva * pondere_rezerva
                venit += lucr * pret_mediu
                cost += lucr * (1.5 + 0.3)            # SIM IoT + SMS/apeluri
                cost += lucr * pondere_rezerva * 3.0  # dispecerat de rezerva la firma de paza
                if lucr * pondere_rezerva > 0: cost += 150  # minim lunar presupus la dispeceratul de rezerva
                cost += nou * pret * 0.15 * 12 * 0.4  # comision 15% pe 1 an, pe 40% din clientii adusi de parteneri
                cost += venit * 0.03                  # diverse
                ore += lucr * 0.04
        elif pilot_start + 3 <= m < pilot_conv:
            ore += 6                      # pauza de decizie/achizitie, lucratorii raman la 0 venit
            lucr = 30.0 if prob_pilot_ok else 0.0
        if lucr >= 150 and not angajat:  # regula din plan: suport part-time la 150 de lucratori
            angajat = True
        if angajat:
            cost += 600                   # 0,5 norma suport (1.200 EUR/norma, raport sectiunea 7)
            ore -= 25                     # suportul preia instruirea si o parte din administrare
        cash += venit - cost
        min_cash = min(min_cash, cash)
        rows.append((m, round(lucr), round(venit), round(cost), round(venit - cost), round(cash), round(max(ore, 0)), round(max(ore, 0) - CAPACITATE_ORE)))
    print(f"\n=== Scenariul: {nume} ===")
    print("luna | lucratori | venit EUR | cost EUR | rezultat | numerar | ore fondator | peste capacitate")
    for r in rows:
        print(" | ".join(str(x) for x in r))
    dep = sum(1 for r in rows if r[7] > 0)
    print(f"Numerar minim: {round(min_cash)} EUR; numerar la luna 24: {rows[-1][5]} EUR; "
          f"lucratori la luna 24: {rows[-1][1]}; MRR la luna 24: ~{rows[-1][2]} EUR (include marja dispozitiv); "
          f"luni cu ore peste capacitate (~{round(CAPACITATE_ORE)} h): {dep}")

if __name__ == "__main__":
    run("de baza: pilot platit lunile 6-8, contract din luna 10, +20 lucratori/luna", 6, 10, 20, 0.01)
    run("pesimist: pilot amanat (lunile 10-12), contract din luna 15, +8/luna, churn 2%", 10, 15, 8, 0.02)
    run("optimist: pilot lunile 5-7, contract din luna 9, +35/luna", 5, 9, 35, 0.01)
    run("de baza + fondatorul isi plateste 800 EUR/luna din luna 10", 6, 10, 20, 0.01, salariu_fondator=800)
    run("esec: pilotul nu se transforma in contract (oprire)", 6, 10, 0, 0.0, prob_pilot_ok=False)
