# De unde vine fiecare număr din `*_numbers.json`

Ordinea preferată de skill: (1) ofertele și facturile fondatorului (nu există încă), (2) prețuri publice verificabile, (3) estimarea mea, marcată. **Aproape tot e la nivelul (3).** Înainte să se cheltuiască bani, fiecare cifră trebuie verificată cu o ofertă reală.

| Intrare | Valoare | Sursă / raționament |
|---|---:|---|
| Preț A | 65 €/client-lună | Media scării 39/79/149 € la un mix estimat de 50/40/10% (calculul meu). Scara vine din panelul simulat (`../pricing/pricing.md`). |
| Preț G | 89 €/locație-lună | Între IPP (40–69 €) și pragul „scump” al clinicilor (120–150 €) din panelul simulat. Estimare. |
| SMS | refacturat la cost, exclus din preț și din cost | ~0,06–0,074 USD/SMS prin API-uri internaționale (FUR §4 ← Sent.dm). Tariful agregatorilor români e necunoscut (FUR §4, Gaps). |
| API LLM | 2 €/client-lună | Estimare: maparea coloanelor la importuri săptămânale, câteva mii de tokeni pe import. De verificat pe facturi reale. |
| Găzduire și stocare incrementală | 1–1,5 €/client-lună | Estimare. |
| E-mail tranzacțional, comisioane | 0,5 + 0,5 € | Estimare. |
| Găzduire fixă în UE | 45 €/lună | Estimare: o VM mică cu backup și monitorizare. Prețul exact depinde de furnizor (OCI, Hetzner etc.); nu e în note. |
| Unelte, domeniu, e-mail | 25 €/lună | Estimare. |
| Asigurare RC profesională + cyber | 50 €/lună (600 €/an) | Estimare. Clinicile vor cere asigurare de la furnizori (REG §6, Inferences; REG §7). Nicio ofertă reală. |
| Contabilitate suplimentară | 30 €/lună | Estimare (SRL-ul există deja). |
| Deplasări de vânzare | 80 €/lună (+80 în scenariul „spre 3k”) | Estimare: 2–3 drumuri/lună în Nord-Vest. |
| Avocat (DPA, termeni, DPIA, consimțământ) | 1.200 € | Estimare. Kitul minim e descris în REG §1, Inferences. |
| Opinie de calificare MDR (doar G) | 800 € | Estimare. REG §8 recomandă o notă scrisă de calificare pentru zona de graniță. |
| Revizie de securitate | 800 € | Estimare. REG §5: clinicile cer dovezi de securitate. |
| Capacitate | 25 de clienți (A), 13 (G) | Estimare: ~52 h/lună disponibile. A: ~1 h suport/client-lună și ~25 h/lună vânzare și dezvoltare. G: ~2 h suport/client-lună, plus integrare grea. |
| Rampa A | +1 client/lună din luna 4 | Estimare. Panelul simulat: 35% (v1) și 15% (v2) cumpără; skill-ul spune să fie tratat ca limită superioară, deci ~10–15% conversie reală din vizite calificate. La ~4–6 vizite/lună: ~1 client nou pe lună. |
| Rampa G | primul client în luna 5, ~0,5 clienți/lună în anul 1 | Estimare. Panelul simulat: 0% (v1), 10% (v2; 2 din 9 clinici). Integrarea per clinică e de 10–15 h. |
| Costul timpului fondatorului | 20 €/h (doar în varianta „cost complet”) | Cost de oportunitate ales de mine. Nu e cheltuială în numerar. |
| CAC | ~25–40 h de vânzare per client câștigat, plus 50–100 € deplasări | Estimare: 4–8 vizite de ~3–4 h la o conversie de ~12–15%. În numerar: ~75–150 €. Cu timpul la 20 €/h: ~600–900 €. |
