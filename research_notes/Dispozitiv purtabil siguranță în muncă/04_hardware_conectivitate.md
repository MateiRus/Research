# Hardware purtabil și conectivitate pentru un serviciu de siguranță a lucrătorilor (pilot 20–50 lucrători, Bihor)

Data cercetării: 12 octombrie 2026. Prețurile sunt cele afișate de magazine/distribuitori la data căutării; se menționează dacă sunt cu sau fără TVA.

Legendă marcaje:
- [FAPT, sursă] = informație confirmată într-o sursă citată inline.
- [ESTIMARE] = deducție / ordin de mărime, bazată pe faptele citate, nu pe o sursă directă.
- [DE VERIFICAT] = informație incompletă sau neconfirmată; trebuie cerută de la producător/distribuitor.

Abrevieri folosite: API (Application Programming Interface – interfață software prin care două sisteme schimbă date), SDK (Software Development Kit – kit de dezvoltare pentru a scrie aplicații pe un dispozitiv), LTE-M / LTE Cat-M1 (rețea mobilă 4G pentru dispozitive IoT, consum mic, acoperire mai bună în interior), NB-IoT (Narrowband IoT – rețea mobilă de bandă foarte îngustă pentru senzori, consum foarte mic, nu suportă voce), LoRaWAN (rețea radio pe frecvență liberă 868 MHz, rază mare, consum mic, viteză foarte mică), IP67/IP68 (grad de protecție la praf și apă; 7 = scufundare 30 min la 1 m, 8 = mai mult), ATEX (certificare UE pentru echipamente folosite în atmosfere explozive, Zona 1/21 = gaze/prafuri frecvente), MQTT (protocol ușor de mesagerie pentru IoT), webhook (adresă web la care un serviciu trimite automat un mesaj când se întâmplă un eveniment), Codec 8 (protocolul binar Teltonika prin care trackerele trimit date către un server TCP/UDP), GNSS (GPS + alte sisteme de poziționare prin satelit), UWB (Ultra-Wideband – radio de precizie pentru măsurat distanțe de ordinul centimetrilor), RFID (identificare prin radio, folosită la etichete de proximitate), WBGT (indice de temperatură „wet bulb globe”, pentru stres termic), PHS (Predicted Heat Strain – modelul din standardul ISO 7933), D2C/D2D (direct-to-cell / direct-to-device – semnal de satelit direct pe telefon obișnuit).

Limitări ale acestei cercetări (important pentru cititor):
- Mediul de lucru a blocat complet accesul direct la paginile web (eroare DNS pentru toate site-urile încercate: wiki.teltonika-gps.com, teltonika-gps.com, aisemnal.ro, eshop.sectron.eu, arcobel.com). Toate constatările provin din rezumatele motorului de căutare, nu din citirea integrală a paginilor. Acolo unde rezumatul a fost ambiguu, am marcat [DE VERIFICAT].
- Bugetul de căutări web s-a epuizat înainte de ultima rundă (16 interogări planificate nu au mai putut rula: autonomie exactă TMT250, distribuitori Teltonika în România, API iNet Industrial Scientific, preț IS330.1, studii de acuratețe cădere, preț gateway LoRaWAN, wearable-uri LoRaWAN Milesight/Dragino/Browan, Zoleo, pagini IoT Orange Business România, prețuri inReach Professional în EUR, prețuri sisteme de proximitate 2025, data lansării NB-IoT Vodafone România, prețuri Sonim/Crosscall în EUR, prețuri aplicații lone-worker, preț Kenzen). Acestea apar explicit la „Gaps”.

---

## 1. Trackere personale cu man-down și SOS care expun date prin protocol deschis sau API

### Takeaway (Concluzie)
Singurele trackere personale confirmate cu detecție man-down (om căzut / imobil) și buton SOS la preț accesibil sunt cele două modele Teltonika (TMT250 și GH5200, ambele ~60–180 € fără TVA, în funcție de distribuitor); familiile Teltonika TAT/TFT sunt trackere de active, nu purtabile, și mai multe modele sunt „End of life”. Twig One este dispozitivul profesional de referință (protocol MPTP + Integrator Kit), dar costă ~800 € fără TVA, iar varianta ATEX ~1.700 €. Garmin inReach are un API documentat public (IPC Inbound/Outbound) și funcționează fără semnal mobil, dar nu are man-down și costă 25–65 USD/lună/dispozitiv. Queclink GL320MG și Abeeway Smart Badge au buton SOS, dar nu am găsit confirmarea unei funcții man-down.

### Cited Findings (Constatări cu sursă)

Teltonika TMT250 (Lituania; tracker personal autonom)
- Funcții listate de producător: detecție Man-Down, buton de alarmă (SOS), evenimente de mișcare / lipsă de mișcare. [FAPT] — [Teltonika TMT250](https://teltonika-gps.com/products/trackers/tmt250)
- Baterie: Li-ion 3,8 V, 800 mAh (listare distribuitor). [FAPT] — [Arcobel](https://arcobel.com/arcobel_fr/persoonlijke-tracker-met-800-mah-li-ion-batterij.html); fișa tehnică oficială (nu a putut fi deschisă): [DS-TMT250.pdf](https://wiki.teltonika-gps.com/images/8/8f/DS-TMT250.pdf)
- Preț: 88,50 € / bucată fără TVA la Sectron (Cehia). [FAPT] — [Sectron](https://eshop.sectron.eu/en/teltonika-tmt250-autonomni-osobni-tracker/p-15484/). Un distribuitor letonian afișa 34 € fără TVA, dar pe un subdomeniu de test – nesigur. [DE VERIFICAT] — [Trialine (dev)](https://jonys.dev2.trialine.lv/catalogue/teltonika-tmt250_401/)
- Configurare prin Teltonika Configurator și FOTA Web (actualizare firmware de la distanță). [FAPT] — [manual rapid Sectron](https://eshop.sectron.eu/UserFiles/File/Teltonika_tmt250_quick_manual.pdf)
- Niciun rezultat de căutare nu a confirmat explicit „Codec 8” pentru TMT250; documentația de protocol e pe wiki-ul Teltonika, care nu a putut fi accesat. [DE VERIFICAT]

Teltonika GH5200 (tracker personal „handheld”, cu ecran și buton)
- Funcții Man-Down și No-Movement listate; preț 176,53 € fără TVA (preț recomandat 224,99 €), marcat indisponibil la Ascend (Germania). [FAPT] — [Ascend GH5200](https://shop.ascend.de/en/products/teltonika-gh5200-personal-tracker-gh5200)
- 60,00 € fără TVA, 14 bucăți în stoc la Trialine (Letonia). [FAPT, sursă cu grad de încredere scăzut] — [Trialine GH5200](https://jonys.dev2.trialine.lv/catalogue/teltonika-gh5200-gps-tracker-personal_390/)
- 69 € pe eBay Germania (vânzător din Italia; nu e clar dacă nou). [FAPT] — [eBay DE](https://www.ebay.de/itm/236008912079)
- Novatel (Irlanda): stoc epuizat, livrare 5–7 zile la comandă. [FAPT] — [Novatel](https://www.novatel.ie/autonomous-trackers)
- Teltonika publică un caz de utilizare „Lone worker monitoring with GH5200”. [FAPT] — [Teltonika use case](https://www.teltonika-gps.com/ja/use-cases/assets-and-workforce/lone-worker-monitoring-with-gh5200-tracker)

Teltonika TAT100 / TAT140 / TAT141 / TFT100 (familiile TAT/TFT)
- TAT100 și TAT140 sunt marcate „End of life” pe paginile Teltonika. [FAPT] — [TAT100](https://www.teltonika-gps.com/ru/products/trackers/assets-workforce/tat100), [TAT140](https://www.teltonika-gps.com/ru/products/trackers/assets-workforce/tat140)
- TAT140 (4G LTE Cat 1): autonomie declarată „până la 3 ani” (condiții de test nespecificate), ~91 € cu TVA, în stoc la Voelkner (DE). [FAPT] — [Voelkner TAT140](https://www.voelkner.de/products/13666102/TAT140-4G-LTE-Cat-1-Asset-Tracker-mit-weltweiter-Abdeckung.html)
- TAT100 (2G, IP68): ~74,45 € cu TVA, livrare 3–4 săptămâni. [FAPT] — [Voelkner TAT100](https://www.voelkner.de/products/13666101/TAT100-2G-Tracker-mit-IP68-Gehaeuse-und-langer-Batterielaufzeit.html). Un utilizator Traccar relatează că suportul Teltonika a spus că TAT100 poate trimite ~1000 poziții cu o baterie. [FAPT, relatare forum] — [Traccar forum](https://www.traccar.org/forums/topic/lifestock-tracker-with-long-battery-life/)
- TAT141: tracker de active cu LTE Cat-M1 (modul Quectel BG95-M3, suportă și NB-IoT și GSM), IP68, raportare periodică – destinat uneltelor, containerelor, vehiculelor, nu purtării de persoane; unele pagini regionale îl listează „End of life”. [FAPT] — [Teltonika TAT141](https://www.teltonika-gps.com/products/trackers/assets-workforce/tat141), [wiki TAT141](https://wiki.teltonika-gps.com/view/TAT141_General_description)
- TFT100: tracker pentru e-mobilitate (stivuitoare electrice, trotinete), baterie 1800 mAh – nu e purtabil. [FAPT] — [wiki TFT100](https://wiki.teltonika-gps.com/view/TFT100_General_description)

Queclink GL320MG (China; tracker personal/active)
- LTE Cat-M1 / NB2 cu rezervă 2G; baterie Li-Po 2600 mAh; detecție mișcare, buton de urgență; NU apare detecție de cădere / man-down în broșură. [FAPT] — [broșură Queclink](https://pdf.directindustry.com/pdf/queclink/gl320mg/4568919-1090483.html)
- Clasa de protecție IPX5 (protecție doar la stropire); „IP67” se referă la husa accesoriu. [FAPT] — [Navixy](https://www.navixy.com/devices/?p=6219)
- Suportat de platforme terțe (Navixy, Wialon) – semn că protocolul este cunoscut integratorilor. [FAPT] — [Wialon](https://wialon.com/es/gps-hardware/queclink-gl320mg)
- Preț orientativ SUA: 89 USD (GL320M, Walmart), pachet cu baterie extinsă de la 155 USD; Embedded Works vinde pe bază de ofertă. [FAPT] — [Embedded Works](https://www.embeddedworks.net/tdev217/)

Twig One / Twig One Ex (Finlanda, Twig Com)
- Producătorul descrie protocolul TWIG MPTP pe care un furnizor de servicii îl poate integra în propriul sistem de monitorizare, plus un „TWIG Integrator Kit” cu resurse pentru dezvoltatori; TWIG Point Cloud listează „API integration”. [FAPT] — [Software and tools](https://navcom.futural.fi/software-and-tools), [Alarm monitoring system](https://twig.futural.fi/page/alarm-monitoring-system), [Twig One](https://twig.futural.fi/lone-worker-alarms/twig-one)
- Platforme terțe (flespi, GPS-Trace) decodează deja Twig One, inclusiv trimiterea de comenzi. [FAPT] — [flespi](https://flespi.com/devices/twig-one), [GPS-Trace](https://gps-trace.com/en/devices/twig-one)
- Exemplu real: centrul de alarmă Axitea (Italia) conectează 400+ dispozitive TWIG printr-o integrare pe baza API-ului furnizat de Irbema (distribuitor). [FAPT] — [Twig blog](https://navcom.futural.fi/blog/news-1/twig-responds-to-social-risks-132)
- Prețuri (retailer ezdirect.it, indisponibil la data căutării): Twig One 2G/3G/4G man-down GPS 793,31 € fără TVA (967,84 € cu TVA 22% IT); Twig One Ex (ATEX) 1.701,36 € fără TVA (2.075,66 € cu TVA); Twig One Ex cu SRD3 1.807,44 € fără TVA. [FAPT] — [ezdirect Twig One](https://www.ezdirect.it/gsm-umts-gateway-router/telefoni-gsm/394548-twig-one-man-down-gps-2g-3g-4g.html), [ezdirect Twig One Ex](https://www.ezdirect.it/gsm-umts-gateway-router/telefoni-gsm/387341-twig-one-ex-atex-con-man-down.html)
- Încărcător ATEX pentru Twig One: 160 €/buc; încărcarea în zona ATEX nu este permisă. [FAPT] — [Vandeputte](https://www.vdp.com/EN/product/view/1050440/2/detectie/twig-one-atex-lader.html)
- Twig One Ex este listat ca dispozitiv ATEX de Vatix (UK, G-Cloud 15) și Peoplesafe. [FAPT] — [Vatix](https://vatix.com/twig-one-ex), [Twig One Ex](https://twig.futural.fi/lone-worker-alarms/twig-one-ex)

Abeeway (Actility, Franța) – Smart Badge și Micro Tracker (LoRaWAN)
- Smart Badge: tracker multi-mod în format card, combină GNSS, „Wi-Fi sniffing”, BLE și geolocalizare LoRaWAN TDoA; buton unic configurabil ca Panic/SOS; buzzer pentru zonare locală; LoRaWAN Class A. Raportează început/durată/sfârșit de mișcare și intrare/ieșire din geofence; NU am găsit menționată o funcție man-down/cădere. [FAPT] — [Abeeway Smart Badge](https://www.abeeway.com/?p=1713), [MCCI store](https://store.mcci.com/products/abeeway-smart-badge), [docs ThingPark AT2](https://docs.thingpark.com/thingpark-location/firmware/AT2_v2.6/introduction/product-description)
- Preț Smart Badge: 140 USD (MCCI, SUA, stoc 0); în Australia 48,31 AUD + GST pentru varianta AS923. [FAPT] — [MCCI](https://store.mcci.com/products/abeeway-smart-badge), [PB Tech](https://www.pbtech.com/au/product/ABW1005/Abeeway-DEABE309-20-4AS-LoRaWAN-AS923-Smart-IoT-GP)
- Micro-Tracker V3 EU868: 89,67 € (Invibit, stoc epuizat). [FAPT] — [Invibit](https://invibitshop.com/products/abeeway-micro-tracker-v3-standard)
- Catalogul Abeeway: prețurile exclud livrarea și taxele vamale și variază pe țară. [FAPT] — [catalog DirectIndustry](https://pdf.directindustry.com/pdf/abeeway/smart-badge/243111-1022391.html)

Garmin inReach (satelit Iridium)
- API documentat public pentru clienți profesionali/enterprise: „IPC Outbound” = Garmin împinge evenimentele (poziții, mesaje, SOS) către URL-ul tău (webhook), cu scheme de evenimente V2–V4 și tabel de coduri de mesaj; „IPC Inbound” = serviciul tău trimite mesaje către dispozitiv (ghid v3.1.1, 10.10.2024, include secțiune „Costs” și autentificare). [FAPT] — [IPC Outbound PDF](https://developer.garmin.com/inReach/IPC_Outbound.pdf), [IPC Inbound PDF](https://developer.garmin.com/inReach/IPC_Inbound.pdf), [portal dezvoltatori](https://developer.garmin.com/inreach-portal/overview/)
- Abonamente „Professional Flex” (pagina regională Garmin, în USD): Basic 24,99 / Advanced 44,99 / Premier 64,99 USD pe lună, plus activare 49,99 USD; plan lunar, angajament 30 zile. [FAPT] — [Garmin Professional](https://garmin.com.my/minisite/inreach/professional); contact pentru enterprise: inReach.professional@garmin.com. [FAPT] — [broșură inReach Flight](https://www8.garmin.com/aviation/brochures/inReach_Flight.pdf)
- Preț inReach Mini 2: MSRP 349,99 USD (SHI) / ~400 USD (Advnture), oferte la 299 USD; în UK oferte la 249,99 £. [FAPT] — [SHI](https://www.shi.com/product/46469856/Garmin-inReach-Mini-2), [Advnture](https://www.advnture.com/news/garmin-inreach-mini-2-29-percent-amazon)
- Un revânzător listează „Garmin Enterprise Grouped Basic Plan” 181,23 USD cu minim 5 dispozitive și tracking la 30 min – denumire neconfirmată pe site-ul Garmin. [DE VERIFICAT] — [SatellitePhoneStore](https://satellitephonestore.com/catalog/sp/details/garmin-enterprise-grouped-basic-plan)
- Platforme terțe (EarthRanger, Traccar) descriu configurarea „Portal Connect” din Garmin Explore pentru a primi date. [FAPT] — [EarthRanger](https://earthranger-support.helpjuice.com/en_US/garmin-inreach), [Traccar forum](https://traccar.org/forums/reply/41003)

SPOT Gen4 / Bivy Stick (satelit Globalstar / Iridium)
- SPOT Gen4: ~145,53 € pe site-ul producătorului (ghid italian), 149,95 CAD în Canada; abonament SUA Basic 16,95 USD/lună (minim 12 luni) sau 193,40 USD/an; Extreme 21,90 USD/lună. SOS necesită abonament. [FAPT] — [Fastweb (IT)](https://www.fastweb.it/fastweb-plus/digital-magazine/comunicazione-satellitare-quali-sono-i-migliori-device/), [SatellitePhoneStore](https://satellitephonestore.com/catalog/sp/details/spot-gen4-monthly-satellite-service), [MEC](https://www.mec.ca/en/product/6013-434/spot-gen4-satellite-messenger)
- Bivy Stick Blue: ~290 €, Bluetooth cu telefonul, comunicare bidirecțională Iridium. [FAPT] — [Fastweb (IT)](https://www.fastweb.it/fastweb-plus/digital-magazine/comunicazione-satellitare-quali-sono-i-migliori-device/)

### Inferences (Deducții)
- [ESTIMARE] Pentru un integrator software mic, Teltonika este calea cea mai „deschisă”: protocolul este public (wiki), există server open-source (Traccar) care discută deja dispozitivele Teltonika, iar prețurile sunt sub 100 € pe unitate. Riscul principal: TMT250 pare să fie doar 2G [DE VERIFICAT] – trebuie verificat dacă operatorii din România mențin 2G în zonele rurale; GH5200 este alternativa cu ecran, mai scumpă.
- [ESTIMARE] Twig One este „standardul industriei” pentru lucrător izolat (robust, man-down testat, variantă ATEX), dar la ~800–1.700 € fără TVA costul pe 30 lucrători ar fi 24.000–51.000 € – nepotrivit pentru un pilot cu buget mic; integrarea cere Integrator Kit de la producător (nu e documentație publică).
- [ESTIMARE] Queclink GL320MG și Abeeway sunt bune pentru SOS + localizare, dar fără man-down confirmat; dacă man-down e cerință-cheie, nu sunt candidate principale fără confirmare scrisă de la producător.
- [ESTIMARE] Garmin inReach este singura opțiune cu API public care funcționează fără semnal mobil; dar fără man-down automat și cu cost lunar de ~25–65 USD/dispozitiv, se justifică doar pentru echipele mici din zone fără acoperire (forestier), nu pentru toți lucrătorii.
- [ESTIMARE] Calitatea algoritmului man-down nu este documentată public de niciun producător găsit (nu există cifre de sensibilitate/specificitate); pilotul trebuie să includă un protocol propriu de testare (căderi simulate, imobilitate, alarme false la aplecat/îngenuncheat).

### Gaps (Lacune)
- Autonomia TMT250 în ore/zile pe moduri (fișa tehnică nu a putut fi deschisă) și confirmarea protocolului Codec 8 / 2G-only – [DE VERIFICAT pe wiki.teltonika-gps.com].
- Distribuitori Teltonika în România și prețuri locale – căutarea nu a mai putut rula.
- Concox/Jimi – nu au fost cercetate (buget epuizat).
- Milesight / Dragino / Browan wearable-uri LoRaWAN cu SOS – căutarea nu a mai putut rula.
- Zoleo, Iridium Edge Solar – nu au fost găsite/cercetate prețuri și API.
- SPOT API (feed XML/JSON al paginii „shared page”) – nu a apărut în rezultate; [DE VERIFICAT].
- Prețuri inReach Professional în EUR și detaliile din secțiunea „Costs” a IPC Inbound – nu au putut fi citite.
- Confirmare scrisă că Twig MPTP / Integrator Kit se oferă unui integrator mic din România (condiții comerciale).

---

## 2. Smartwatch-uri utilizabile în industrie cu detecție cădere și cale de dezvoltare

### Takeaway (Concluzie)
Toate cele trei ecosisteme majore permit, în principiu, unei aplicații terțe să primească evenimente de cădere, dar cu bariere: Apple cere un „entitlement” special aprobat de Apple; Samsung oferă Health Services API pe Wear OS (cu un API avansat de cădere rezervat partenerilor „Privileged”); Garmin oferă SDK-uri doar partenerilor enterprise, iar funcția Incident Detection este una de consum, legată de aplicația Garmin Connect. Niciunul nu este certificat ATEX.

### Cited Findings (Constatări cu sursă)
- Apple Watch: clasa CMFallDetectionManager „necesită un entitlement de la Apple”, solicitat printr-un formular separat; aplicația trebuie să declare o cheie de utilizare în Info.plist (altfel se închide), iar utilizatorul trebuie să autorizeze primirea evenimentelor; alternativ se pot citi numărul de căderi din HealthKit; valabil pe Series 4 și mai noi. [FAPT] — [Apple CMFallDetectionManager](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager.md), [Fall Detection Entitlement Request](https://developer.apple.com/forums/thread/685761)
- Dezvoltatori raportează că formularul este restricționat (doar Account Holder al echipei poate cere) și că nu primesc răspuns clar. [FAPT, relatări forum] — [Apple forum](https://developer.apple.com/forums/thread/680898)
- Samsung Galaxy Watch (Wear OS): Health Services API permite aplicației de pe ceas să primească evenimente de cădere („dacă funcția încorporată nu răspunde nevoilor, Health Services API te lasă să detectezi evenimentul în propria aplicație”); funcția încorporată alimentează SOS-ul ceasului. [FAPT] — [Samsung Developer – Events Monitoring](https://developer.samsung.com/health/blog/en/events-monitoring)
- La SDC22 Samsung a anunțat un „Fall Detection API” cu sensibilitate reglabilă (accelerometru + giroscop), grupat cu programul „Privileged Health SDK” destinat partenerilor selectați. [FAPT] — [Samsung Newsroom (feed)](https://news.samsung.com/my/tag/fall-detection-api/feed)
- Garmin Incident Detection: funcție suplimentară disponibilă doar pentru anumite activități outdoor; trimite mesaj automat cu numele și locația către contactele de urgență configurate în Garmin Connect; „aplicația Garmin Connect nu contactează serviciile de urgență în numele tău”. [FAPT] — [manual Garmin](https://www8.garmin.com/manuals/webhelp/GUID-08ACA9FC-DEE6-4C8D-8A95-F62181C512E9/EN-GB/GUID-F109FB24-B55D-49D2-B388-D042E7FBA965.html)
- Garmin Health SDK / Companion SDK: „disponibile partenerilor enterprise Garmin Health”, acces prin formular, licențe de evaluare aranjate de echipa Garmin Health; Companion SDK dă acces la fluxuri în timp real (puls, accelerometru). [FAPT] — [Garmin Health SDK](https://developer.garmin.com/health-sdk/overview/)

### Inferences (Deducții)
- [ESTIMARE] Un smartwatch de consum nu înlocuiește un tracker dedicat într-un pilot industrial: autonomie 1–2 zile, lipsă ATEX, dependență de telefonul lucrătorului și de consimțământul individual pentru date de sănătate; totuși, poate fi util ca „senzor de puls opțional” via Companion SDK (Garmin) sau Health Services (Samsung).
- [ESTIMARE] Cea mai scurtă cale către un prototip de detecție cădere pe ceas este Samsung Wear OS (Health Services API public), nu Apple (entitlement greu de obținut).

### Gaps (Lacune)
- Google Pixel Watch (API cădere), Samsung Knox pentru flote de ceasuri, ceasuri industriale robuste (Honeywell/Zebra/Kyocera/Sonim/Mobvoi) – nu au fost cercetate.
- Nu am găsit studii de acuratețe (sensibilitate/specificitate, alarme false) pentru detecția căderii pe smartwatch – căutarea nu a mai putut rula.

---

## 3. Smartphone-uri robuste cu aplicații man-down și telefoane ATEX

### Takeaway (Concluzie)
Un telefon robust Android (Cat S75 ~330 €, Sonim XP10, Crosscall Core-X5) plus o aplicație de lucrător izolat (Peoplesafe, Nomadia eSafeMe) este cea mai flexibilă variantă software-first, dar aplicațiile comerciale vin cu propriul abonament și platformă. Telefoanele ATEX Zona 1 (i.safe MOBILE IS540.1) sunt o clasă aparte, cu prețuri de ordinul miilor de euro și vânzare pe ofertă.

### Cited Findings (Constatări cu sursă)
- Cat S75: preț recomandat la lansare în Germania 599 € (martie 2023). [FAPT] — [nextpit](https://www.nextpit.de/handys/caterpillar-cat-s75); listat acum la 329,90 € (128 GB, Estonia) și 274,99 £ în UK. [FAPT] — [Arvutitark](https://arvutitark.ee/en/smart-devices/phones/cat-s75-128gb-ds-black-66-5g-android-1255375), [PriceSpy UK](https://pricespy.co.uk/product.php?p=10020989)
- Aplicația Peoplesafe (UK) este disponibilă pe telefoanele Cat și include detecție de cădere care ridică automat alarma. [FAPT] — [Mobile News](https://mobilenewscwp.co.uk/news/article/cat-smartphones-offer-advanced-gps-tracking-lone-workers/)
- Sonim XP10: fișa de vânzare 2023 listează „emergency man-down și lone worker on-device alarm” și tracking GPS, garanție 3 ani. [FAPT] — [Sonim sell sheet](https://www.sonimtech.com/wp-content/uploads/2023/11/Sonim_Manufacturing_VerticalSellSheet_110923.pdf)
- Crosscall Core-X5: testat și aprobat cu aplicația Nomadia eSafeMe Pro; are 4 butoane programabile compatibile cu Nomadia Protect. [FAPT] — [Nomadia](https://www.nomadia.com/?p=41138)
- i.safe MOBILE IS540.1: smartphone ATEX/IECEx Zona 1/21 (descris ca primul din lume), Android 14, 8+128 GB, 5G, IP68, MIL-STD-810H, baterie 4400 mAh înlocuibilă. [FAPT] — [DACPOL (DE)](https://www.dacpol.eu/de/10268-telefone-fur-zonen-1-21/product/53154-is5401-smartphone-fur-die-zonen-1-21), [OfficeEasy (FR)](https://www.officeeasy.fr/isafe-is540-1.html), [Coal Age](https://www.coalage.com/product-news/explosion-proof-5g-smartphone/)
- Preț IS540.1: 5.764,94 NZD cu GST (Noua Zeelandă, stoc epuizat); în UK doar pe ofertă („Receive a quote within 2 hours”). [FAPT] — [Comsys NZ](https://comsys.co.nz/product/rugged-tab-i-safe-mobile-is-ip68-is5401-6in-6777752), [Rockall Safety](https://www.rockallsafety.co.uk/product/is540-1-atex-zone-1-21-certified-android-smartphone/)

### Inferences (Deducții)
- [ESTIMARE] Echivalentul în EUR al prețului NZ pentru IS540.1 este de ordinul 2.500–3.500 € fără TVA; prețul european real trebuie cerut distribuitorului (ex. DACPOL, Rockall).
- [ESTIMARE] Varianta „telefon robust + aplicație proprie Android” permite firmei să controleze complet algoritmul man-down (accelerometru) și transmisia (MQTT/HTTPS), dar algoritmul trebuie validat de firmă; dezavantaj: telefonul trebuie purtat pe corp (nu în rucsac) pentru ca detecția să funcționeze.

### Gaps (Lacune)
- Prețuri EUR actuale pentru Sonim XP10 și Crosscall Core-X5 – nu au apărut în rezultate.
- i.safe MOBILE IS330.1 (preț) – căutarea nu a mai putut rula.
- Doogee/Ulefone/Blackview – nu au fost cercetate.
- Prețuri pe utilizator/lună pentru aplicațiile lone-worker (StaySafe, Ok Alone, SoloProtect, Peoplesafe) – căutarea nu a mai putut rula.

---

## 4. Detectoare de gaze conectate cu posibilitate de integrare

### Takeaway (Concluzie)
Detectoarele multigaz conectate costă 1.300–1.900 € fără TVA pe unitate (MSA ALTAIR io4 ~1.403 € fără TVA în Germania); Dräger X-am 2800 este mai ieftin (~525 £ fără TVA, UK) dar nu are modem celular (doar Bluetooth către aplicație/gateway). Blackline G7c se vinde ca abonament SaaS (1.512 USD / 36 luni cu dispozitivul inclus) iar API-ul Blackline este accesibil doar prin formular de contact. Nu am găsit documentație publică de API pentru MSA Grid, Honeywell Safety Suite sau Dräger Gas Detection Connect.

### Cited Findings (Constatări cu sursă)
- MSA ALTAIR io4 (CO, H2S, metan, O2; celular integrat): 1.402,90 € fără TVA la RS Germania; 1.913,47 £ fără TVA (2.296,16 £ cu TVA) la RS UK; 1.338,05 USD la Airgas (SUA). [FAPT] — [RS DE](https://de.rs-online.com/web/p/gasmelder/0315978), [RS UK](https://uk.rs-online.com/web/p/gas-detectors/0315978?gb=s), [Airgas](https://www.airgas.com/product/Safety-Products/Monitors-%26-Calibration-Equipment/Gas-Monitors-%26-Sensors/p/MSA10245598)
- Dräger X-am 2800: fără modem celular; monitorizare live prin Bluetooth către aplicația Dräger Gas Detection Connect sau gateway ConHub; stația X-dock face bump-test, firmware și trimite date în cloud. [FAPT] — [Frontline Safety](https://www.frontline-safety.co.uk/blog/the-drager-x-am-2800-five-game-changing-features-for-modern-gas-detection)
- Preț X-am 2800: 524,99 £ fără TVA (UK); 1.526 USD „clearance” pentru set (SUA); Dräger nu publică listă oficială de prețuri. [FAPT] — [Sitebox UK](https://www.sitebox.ltd.uk/drager-xam-2800-multigas-detector-3703919-oXAM2800_3703919), [AllSafe Industries](https://allsafeindustries.com/x-am-2800-portable-gas-monitor.aspx), [Reliamag](https://reliamag.com/?p=266235)
- Honeywell BW Solo (monogaz, Bluetooth): 400–662 USD în SUA după variantă; 281,43–644,90 £ în UK; datele se descarcă pe PC și se gestionează în Honeywell Safety Suite (nu confirmă API public). [FAPT] — [Tequipment price list](https://www.tequipment.net/BWTechnologiesPriceList.html?pg=8), [Instrumart](https://www.instrumart.com/products/all-part-numbers/46039), [Rockall Safety](https://www.rockallsafety.co.uk/product/bw-solo-gas-detector-black/)
- Blackline G7c: pe AWS Marketplace, abonament SaaS „lone worker” 36 luni = 1.512 USD cu dispozitivul G7c inclus; monitorizare live 24/7 +792 USD; apel bidirecțional +396 USD; push-to-talk +612 USD; contractele SaaS sunt nerambursabile. [FAPT] — [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-wc7ixanpjyw3g)
- Revânzător european: G7c NH3 la 1.289,05 (+TVA) cu licență Blackline Live 2 ani inclusă, reînnoire bianuală neinclusă. [FAPT] — [333shop](https://www.3tres3.com/en-af/guide333/companies/333shop-en-af/detector-for-nh3-g7c-blackline_7331)
- Pagina „API” Blackline Safety duce la un formular de contact, nu la documentație publică. [FAPT] — [Blackline API](https://www.blacklinesafety.com/solutions/software/api); G7c este dispozitiv suportat în Blackline Live. [FAPT] — [Blackline Help Center](https://help.blacklinesafety.com/en/blackline-live/product-documentation/blackline-live-technical-user-manual/overview/supported-devices)
- Fișa G7c (versiune mai veche) menționează conectivitate celulară 3G și streaming automat de date. [FAPT] — [fișă G7c](https://assets.thermofisher.com/TFS-Assets/ANZ/Datasheets/blackline-g7c-gas-live-monitor.pdf)

### Inferences (Deducții)
- [ESTIMARE] Pentru un integrator mic, cea mai realistă cale de a primi alarme de gaz în platforma proprie este fie Blackline (API pe bază de parteneriat), fie un detector cu Bluetooth (Dräger X-am 2800, BW Solo) citit de o aplicație Android pe telefonul robust al lucrătorului – dar protocolul Bluetooth nu este public, deci [DE VERIFICAT] cu fiecare producător.
- [ESTIMARE] Toate detectoarele au certificare ATEX pentru atmosfere explozive (sunt destinate acestui scop), dar pilotul în construcții/forestier are nevoie de gaze rar (spații închise, cisterne, CO de la motoare în spații înguste); 2–4 unități partajate ar fi suficiente pentru pilot.

### Gaps (Lacune)
- MSA Grid (abonament și API), Honeywell Safety Suite API, Dräger Gas Detection Connect API – nicio documentație publică găsită.
- Industrial Scientific Ventis Pro / iNet (preț, API) – căutarea nu a mai putut rula.
- Honeywell BW RigRat – necercetat.
- Prețuri în România / distribuitori locali pentru detectoare – necercetate.

---

## 5. Wearable-uri pentru stres termic și validitatea abordării software-only

### Takeaway (Concluzie)
Singurul wearable cu validare publicată peer-reviewed este Kenzen (eroare medie absolută 0,25 °C față de temperatura rectală/pilulă, dar cu acuratețe scăzută peste ~38,5 °C conform unui studiu independent). SlateSafety BAND V2 (~805 CAD + abonament portal anual) nu are validare independentă găsită. Modelul PHS din ISO 7933 este validat în teren, dar nu este construit pentru monitorizare în timp real; există variante bazate pe puls (PHS-HR) validate în cameră climatică. O abordare software-only (meteo + rată de muncă + puls) este credibilă ca „indicator de risc / avertizare organizatorică”, nu ca măsurătoare medicală.

### Cited Findings (Constatări cu sursă)
- Kenzen – studiu Moyen et al. 2021 (IJERPH, autori majoritar Kenzen + cercetători universitari): 4 studii combinate, 52 teste, 27 subiecți; algoritm ML de temperatură centrală cu MAE 0,25 °C, RMSE 0,30 °C, r = 0,94, față de referințe rectale și pilulă ingerabilă. [FAPT] — [PMC8701050](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8701050/)
- Teză independentă (Waikato, triatloniști): acord bun între 37–38 °C, acordul scade de la ~38,5 °C; la ≥39 °C diferența medie 0,79 °C – autorul consideră dispozitivul nevalid pentru hipertermie moderată. [FAPT] — [Waikato](https://researchcommons.waikato.ac.nz/entities/publication/2fdc087c-9eb5-415c-9e1d-5e48a179f3d8)
- Kenzen (comunicat): algoritmul atinge MAE ≤0,3 °C pe intervalul 36–40 °C și 13–43 °C ambient; studiu cu 75 participanți în 3 universități; algoritmul include rata de transpirație, vârsta, sexul. [FAPT, sursă comercială] — [EHS Daily Advisor](https://ehsdailyadvisor.com/?p=28572), [PatSnap news](https://synapse.patsnap.com/news-detail/f59755bc-b6be-3712-abc5-2d94868b72fe-new-study-wearable-monitor-system-protects-workers-against-heat-stroke)
- SlateSafety BAND V2: monitor purtat pe braț, 24/7, puls, efort, temperatură centrală estimată; unitatea de bază (506-200) necesită achiziția „Annual Portal Access” (506-209); există kit cu 3 ani portal (506-200KP) și kit de 5 (506-200K5); SKC ascunde prețul după login. [FAPT] — [SKC BAND V2](https://skcinc.com/products/band-v2), [SKC kit 3 ani](https://skcinc.com/slatesafety-band-v2-kit-w-3-year-portal-access-506-200kp)
- Preț BAND V2: 804,95 $/buc la Levitt-Safety (Canada; probabil CAD), livrare 7–14 zile. [FAPT] — [Levitt-Safety](https://www.levitt-safety.com/Marques/Slate-Safety/Catalogue/Fast-Track/Heat-Stress)
- Safety+Health precizează că informațiile despre produs sunt furnizate de producător și nu au fost testate independent. [FAPT] — [Safety+Health](https://www.safetyandhealthmagazine.com/?p=38261)
- Epicore Connected Hydration: lansat comercial în aprilie 2024, patch de transpirație de unică folosință + electronică reutilizabilă, baterie buton 1.000+ ore; disponibil doar în SUA, doar pentru uz comercial. [FAPT] — [Notebookcheck](https://www.notebookcheck.net/Epicore-Biosystems-unveils-Connected-Hydration-wearable-to-monitor-worker-hydration-for-heat-safety.853288.0.html), [Archview](https://www.archviewservices.com/products/connected-worker-instruments/smartwearable/)
- Bodytrak (in-ear): monitorizează indice de strain fiziologic, puls, oboseală, alerte man-down; fără preț public. [FAPT] — [Australian Mining](https://www.australianmining.com.au/bodytrak-is-preventing-heat-stress-while-temperatures-rise/)
- ISO 7933 / PHS: model „PHS-HR” bazat pe puls (index temporal de puls) pentru rate metabolice variabile, validat în 8 combinații temperatură-umiditate în cameră climatică. [FAPT] — [Univ. Reading](https://centaur.reading.ac.uk/76546/)
- PHS nu este aplicabil pentru îmbrăcăminte de protecție cu izolație intrinsecă peste 1,0 clo. [FAPT] — [PolyU](https://research.polyu.edu.hk/en/publications/can-the-phs-model-iso7933-predict-reasonable-thermophysiological-/)
- Validare în mine subterane fierbinți: PHS „a dat rezultate fiabile în majoritatea cazurilor” față de alte metode. [FAPT] — [Univ. Arizona](https://experts.arizona.edu/en/publications/validation-of-the-predicted-heat-strain-model-in-hot-underground-/)
- Un index de strain în timp real bazat pe temperatura piciorului + puls (sub echipament de protecție, 32 °C) a corelat r = 0,756 cu indexul original; autorii notează că calculul ISO 7933 „e complicat de aplicat în monitorizare în timp real”. [FAPT] — [PMC4580874](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4580874/)
- Calculatorul PHS „FAME Lab” a fost verificat față de codul original ISO 7933:2018 și date de teren, cu rezultate în limitele de acuratețe din Anexa F. [FAPT] — [PMC6885605](https://pmc.ncbi.nlm.nih.gov/articles/PMC6885605), [CDC Stacks](https://stacks.cdc.gov/view/cdc/248710)

### Inferences (Deducții)
- [ESTIMARE] O abordare software-only este defendabilă dacă: (1) folosește WBGT/temperatura din date meteo + categoria de efort estimată (ISO 7933 / ISO 8996) pentru un „indice de risc al schimbului”, (2) opțional pulsul (din ceas sau bandă toracică) ca semnal de efort, (3) comunică explicit că este un instrument de prevenție organizatorică (pauze, hidratare), nu un dispozitiv medical și nu estimează temperatura centrală. Astfel se evită o pretenție medicală (regulamentul UE 2017/745 pentru dispozitive medicale) [DE VERIFICAT cu un consultant de reglementare].
- [ESTIMARE] Kenzen și SlateSafety sunt produse închise (dispozitiv + portal propriu); integrarea într-o platformă terță depinde de un acord comercial, iar prețul de ~800 CAD/unitate + portal face ca 30 unități să coste peste 20.000 € – nu pentru pilot.

### Gaps (Lacune)
- Preț Kenzen pe lucrător/abonament – căutarea nu a mai putut rula.
- Preț Bodytrak și Epicore – nu au fost găsite (vânzare pe ofertă).
- Nu am găsit un studiu care să valideze un wearable comercial față de ieșirile ISO 7933; posibil să nu existe.
- Garmin/Polar + senzori de mediu ca soluție de stres termic – necercetate.

---

## 6. Avertizare de proximitate om–utilaj

### Takeaway (Concluzie)
Sistemele de proximitate (ZoneSafe/Brigade pe RFID, Leica PA10 pe UWB, AWARE pe UWB) se vând ca pachete pe utilaj, de ordinul 3.500–5.000 £ per utilaj (cifră din 2011) sau ~5.300 SGD per pachet instalat (program Singapore); niciun producător găsit nu publică prețuri sau API deschis, iar integrarea de către un terț mic nu este documentată.

### Cited Findings (Constatări cu sursă)
- ZoneSafe (Brigade Electronics): un director OnGrade estima în 2011 costul la ~3.500–5.000 £ per utilaj, potrivit pentru excavatoare și utilaje peste 12 t. [FAPT, dată veche] — [KHL / International Rental News](https://www.khl.com/1065699.article)
- Document de co-finanțare Singapore: pachet ZoneSafe vehicul-pieton 5.300 SGD total (3.570 SGD cost eligibil), incluzând unitate de control, antenă, etichete, instalare și punere în funcțiune; varianta vehicul-vehicul la același total. [FAPT] — [GoBusiness SG (PDF)](https://www.gobusiness.gov.sg/images/psg/Desensitised_Automation_Support_ZoneSafe_Proximity_Part_1.pdf)
- Pagina Brigade listează coduri de produs (ex. ZS-1000-ECU unitate de control) fără prețuri; există etichetă reîncărcabilă. [FAPT] — [Brigade ZoneSafe](https://brigade-electronics.com/products/zonesafe/), [Agg-Net](https://www.agg-net.com/news/zonesafe-release-rechargeable-proximity-tag)
- Leica PA10: ancoră pe utilaj + etichetă pe pieton, UWB time-of-flight, rază până la 40 m, precizie ±20 cm, fără legătură radio separată, funcționează fără GNSS (ateliere, carieră). Fără preț/API în broșură. [FAPT] — [broșură Leica PA10](https://cdn.shopify.com/s/files/1/0364/1297/files/Leica-PA10-BRO.pdf)
- AWARE (Access Control Group): UWB, avertizează operatorul când o etichetă purtabilă sau alt echipament intră în rază; vândut ca add-on la pachetul de telematică „Advanced”; setările de rază se pot schimba din cloud. [FAPT] — [MHW Magazine](https://www.mhwmag.com/products/access-control-group-launches-aware/)
- Cercetare academică (Sensors, 2023): sistem UWB low-cost de detecție proximitate pentru firme mici de construcții, cu sau fără ancore fixe – prototip, nu produs. [FAPT] — [DOAJ / Sensors](https://doaj.org/article/30a6d28fd48d4804b017497df8c7cd9f)

### Inferences (Deducții)
- [ESTIMARE] Pentru pilot, proximitatea este modulul cel mai scump și cel mai greu de integrat; o alternativă „soft” este alerta de proximitate pe baza pozițiilor GNSS ale trackerelor (lucrător vs. utilaj cu tracker Teltonika) cu precizie de 5–10 m – suficientă pentru avertizare de zonă, nu pentru oprire de utilaj. Soluțiile UWB/RFID certificate rămân pentru faza 2, probabil prin parteneriat cu un distribuitor Brigade/Leica.

### Gaps (Lacune)
- Scan-Link Armour, Brickeye, SICK, Siemens UWB – nu au apărut în rezultate; prețuri 2025 pentru etichete/utilaj – căutarea nu a mai putut rula.
- Niciun producător nu a fost confirmat ca oferind API/protocol deschis unui integrator mic – [DE VERIFICAT direct cu Brigade (ZoneSafe) și Leica].

---

## 7. Conectivitate în Bihor (Apuseni, Pădurea Craiului, Codru-Moma) și ce funcționează fără semnal mobil

### Takeaway (Concluzie)
Oficial, toți operatorii acoperă ~98% din populația României (campania ANCOM 2024: Digi 98,6%, Orange 98,2%, Telekom 98,1%, Vodafone 98,1%), dar măsurătorile ANCOM se fac de pe drumuri accesibile, deci pădurile și crestele din Bihor nu sunt acoperite de date; harta oficială este aisemnal.ro (nu a putut fi accesată). LTE-M există la Orange România din 2018 (peste 3.000 localități) și Orange a fost singura filială Orange din Europa cu NB-IoT; Vodafone a anunțat NB-IoT național (dată neconfirmată). LoRaWAN public există doar în orașe (Orange: București, Iași + 6 localități; TTN are comunitate în Oradea), în pădure raza LoRa scade la sute de metri – 1–2 km. Satelitul direct pe telefon (D2C) nu este comercial în România: Orange testează în S2 2026, AST SpaceMobile integrează România din august 2026, primele servicii comerciale sunt estimate pentru 2027; Starlink D2C nu are operator în România. Singura soluție matură fără semnal este un comunicator satelit dedicat (Garmin inReach, SPOT).

### Cited Findings (Constatări cu sursă)

Acoperire mobilă și ANCOM
- Platforma ANCOM aisemnal.ro arată nivelul semnalului de voce pe localitate pentru 2G, 3G și 4G, pe fiecare punct de măsurare și operator, cu populația acoperită și data măsurătorii. [FAPT] — [Economedia](https://economedia.ro/?p=225374)
- Campania 2024 a măsurat acoperirea „din mers”, pe drumuri accesibile, bulevarde și străzi principale/secundare; rezultate: Digi 98,6%, Orange 98,2%, Telekom 98,1%, Vodafone 98,1% din populație. [FAPT] — [Economedia](https://economedia.ro/?p=225374), [HotNews](https://hotnews.ro/?p=463684)
- Campania 2022: RCS&RDS 98,8%, Orange 98,5%, Telekom 98,5%, Vodafone 98,4%. [FAPT] — [Capital](https://www.capital.ro/ancom-98-din-populatia-romaniei-are-acoperire-cu-semnal-pentru-serviciile-de-telefonie-mobila.html)
- Un răspuns ANCOM din 2023 (interpelare Senat) arată că autoritatea nu poate obliga operatorii să extindă rețeaua în zone din afara politicii lor comerciale; redirecționează plângerile către operatori. [FAPT] — [Senat.ro (PDF)](https://www.senat.ro/PDFIntrebari)
- Niciun rezultat nu a oferit date specifice pentru Apuseni, Pădurea Craiului sau Codru-Moma. [LACUNĂ]

Consolidarea pieței (relevant pentru alegerea SIM)
- Consiliul Concurenței a aprobat condiționat în iulie 2025 preluarea Telekom Romania Mobile de către Vodafone România și Digi România. [FAPT] — [Revista Biz](https://www.revistabiz.ro/consiliul-concurentei-aproba-conditionat-achizitia-telekom-romania-mobile-communications/)
- Vodafone preia clienții postpaid, business, retail și infrastructura de rețea (30 mil. € înainte de ajustări), Digi preia clienții prepaid; ambele primesc spectru și turnuri suplimentare. [FAPT] — [SEC filing Vodafone](https://www.sec.gov/Archives/edgar/data/0000839923/000165495425010931/a9683z.htm), [Business Forum](https://www.businessforum.ro/industry/20250729/vodafone-and-digi-to-finalize-telekom-romania-mobile-deal-2112)
- Fuziunea Vodafone–Telekom Romania Mobile a fost finalizată legal de la 1 iulie (anul nu e vizibil în rezumat), cu promisiuni de investiții accelerate în rețea. [FAPT] — [Economedia](https://economedia.ro/foto-vodafone-romania-finalizeaza-fuziunea-cu-telekom-romania-mobile-clientii-isi-pastreaza-serviciile-iar-compania-promite-investitii-accelerate-in-retea-si-digitalizare.html)
- Editorial: Digi conduce piața mobilă dar nu are încă partener de satelit; a cumpărat spectru și turnuri de la Telekom. [FAPT, opinie] — [Mobilissimo](https://mobilissimo.ro/editoriale-diverse/digi-conduce-piata-mobila-dar-ii-lipseste-inca-o-piesa-conexiunea-directa-la-satelit)

LTE-M și NB-IoT
- Orange România a lansat în noiembrie 2018 prima rețea națională LTE-M, cu acoperire inițială în peste 3.000 de localități. [FAPT] — [SAMENA](https://www.samenacouncil.org/samena_daily_news?news=70523), [Telecoms.com](https://www.telecoms.com/iot/orange-hits-green-button-on-lte-m-network)
- România era „singura filială Orange din Europa care oferă și NB-IoT” (Mobile Europe, 2018). [FAPT] — [Mobile Europe](https://www.mobileeurope.co.uk/?p=13201)
- Revista Biz: Vodafone România a lansat „prima rețea NB-IoT din România cu acoperire națională” (fragment nedatat; URL-ul indexat este despre 5G). [DE VERIFICAT] — [Revista Biz](https://www.revistabiz.ro/premiera-vodafone-romania-lanseaza-primele-servicii-5g/)
- Acoperire 4G Orange România la final de 2018: 96,9% populație, 100% urban. [FAPT] — [Forbes RO](https://www.forbes.ro/?p=88860)

LoRaWAN
- Orange Business Services (2020): acoperire LoRaWAN completă în București și Iași, rețea prezentă în alte 6 localități; funcționează pe banda liberă 868 MHz; „o singură stație poate acoperi 15–20 km” (afirmație a operatorului, valabilă în câmp deschis). [FAPT] — [Forbes RO](https://www.forbes.ro/orange-business-services-anunta-acoperirea-completa-lorawan-bucuresti-si-iasi-dedicata-aplicatiilor-smart-city-173239), [Mobilissimo](https://www.mobilissimo.ro/stiri-diverse/orange-romania-ofera-acum-acoperire-completa-lorawan-in-iasi-si-bucuresti)
- The Things Network: Oradea a devenit comunitate TTN în decembrie 2020 (număr de gateway-uri actual necunoscut). [FAPT] — [Interoperable Europe / OSOR](https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/new-communities-global-and-open-lorawan-network)
- Rază LoRaWAN în pădure: un studiu raportează propagare la 300 m în pădure cu recepție >80% la SF7. [FAPT] — [Future Internet 2021](https://doaj.org/article/9bf5ef3eb7e742078b3936154eeb1c33); „range extender” LoRaWAN (Ostfalia) a adăugat câte ~1 km în pădure densă. [FAPT] — [Uni Halle OpenData](https://www.opendata.uni-halle.de/handle/1981185920/113603); modelele de propagare subestimează pierderile vegetației la 200 m. [FAPT] — [Univ. Padova](https://research.unipd.it/handle/11577/3503746)
- Ridicarea antenei gateway-ului de la 12 m la 30 m aproape dublează raza (Kerlink / model Hata). [FAPT] — [Smartmakers](https://smartmakers.io/en/lorawan-range-part-2-range-and-coverage-of-lorawan-in-practice/); forum TTN: ~600 m în pădure realizabil cu antene ridicate; frunzișul de foioase blochează suplimentar primăvara. [FAPT, forum] — [TTN forum](https://www.thethingsnetwork.org/forum/t/coverage-in-forest/40832)

Mesh (Meshtastic, goTenna)
- Meshtastic folosește banda liberă 868 MHz în Europa; LoRa atinge ~16 km în condiții perfecte. [FAPT] — [IEEE Spectrum](https://spectrum.ieee.org/amp/build-iot-apps-with-meshtastic-2668335550)
- Relatări de utilizatori: 4–5 km prin pădure cu antene potrivite; 15 km cu antene standard în câmp; dar și rezultate „sub 50 m” din cauza antenelor/conexiunilor. [FAPT, anecdotic] — [rblind/Lemmy](https://rblind.com/post/3606659/2884139), [Meshtastic forum](https://meshtastic.discourse.group/t/meshtastic-range-test-dismal-results-50-meters/6299)
- goTenna Pro X: test în pădure densă (Michigan) prin vegetație moderată–densă la nivelul umărului, coronament și cu releu pe dronă (fără cifre km în rezumat); legătură de 88,45 km limitată de teren. [FAPT] — [Forterra – forest test](https://thelastmile.forterra.com/video-presentation-testing-gotenna-pro-x-mesh-networks-in-a-dense-forest/), [Forterra – Tech Rodeo](https://thelastmile.forterra.com/?p=2295)

Satelit direct pe telefon (D2C) și comunicatoare satelit
- Orange România va testa conectivitate prin satelit (SMS, voce, date) în a doua jumătate a lui 2026 – primul test de acest fel din grupul Orange. [FAPT] — [Romania Insider](https://www.romania-insider.com/orange-testing-satellite-connectivity-romania-2026), [Developing Telecoms](https://developingtelecoms.com/telecom-technology/satellite-communications-networks/19879-orange-and-partners-to-demo-d2d-satellite-connectivity-in-romania.html)
- AST SpaceMobile a confirmat pe 6 august 2026 că integrează rețelele din România și alte 7 țări europene; Orange a adăugat AST pe lista furnizorilor de satelit, cu teste europene la final de 2026. [FAPT] — [Finviz / Orange–AST](https://finviz.com/news/329825/orange-adds-ast-spacemobile-asts-to-its-satellite-roster-putting-europe-direct-to-cell-trials-on-the-calendar-for-late-2026)
- Vodafone lucrează prin Satellite Connect Europe (JV Vodafone + AST SpaceMobile) pentru D2D în Europa. [FAPT] — [Fierce Network](https://www.fierce-network.com/wireless/european-operators-scramble-keep-pace-satellite-initiatives)
- Un raport românesc estimează primele servicii comerciale în 2027. [FAPT, estimare presă] — [Gadget.ro](https://gadget.ro/?p=387495)
- Starlink Direct to Cell în Europa: Spania (MasOrange) anunțată ca prima țară UE cu lansare în 2026; Kyivstar (Ucraina) primul în Europa; Virgin Media O2 (UK) live; BICS (Proximus) furnizor IPX preferat pentru conectarea operatorilor europeni; Franța – serviciu de urgență în așteptarea aprobării. Niciun operator din România. [FAPT] — [Finviz / MasOrange](https://finviz.com/news/298652/starlinks-direct-to-cell-tech-gears-up-for-eu-debut-as-spains-masorange-to-begin-trial), [Capacity / BICS](https://capacityglobal.com/news/starlink-taps-proximus-d2c/), [Basenor – Franța](https://www.basenor.com/blogs/news/starlink-mobile-emergency-service-france-approval-explained)
- Comunicatoare satelit cu API: Garmin inReach (IPC Outbound/Inbound – vezi secțiunea 1), abonamente Professional Flex 24,99–64,99 USD/lună. [FAPT] — [Garmin Professional](https://garmin.com.my/minisite/inreach/professional)

### Inferences (Deducții)
- [ESTIMARE] În Bihor, pentru șantiere de construcții din localități și de pe drumuri principale, LTE/2G va fi aproape sigur disponibil (98% populație); pentru parchete forestiere din Apuseni și Pădurea Craiului, trebuie presupus că vor exista zone fără semnal. Recomandare: înainte de pilot, o zi de măsurare pe teren cu un telefon cu aplicație de măsurare (ex. Netograf/aisemnal, aplicații de „cell info”) pe fiecare SIM (Orange, Vodafone, Digi).
- [ESTIMARE] SIM multi-rețea (roaming IoT, de la furnizori precum 1NCE, Emnify, Things Mobile, sau oferta M2M a operatorilor locali) oferă cea mai bună șansă de acoperire, pentru că trackerul se conectează la oricare operator cu semnal; cost orientativ 1–3 € pe SIM pe lună la volum mic [DE VERIFICAT – nicio sursă citată].
- [ESTIMARE] Store-and-forward (dispozitivul memorează pozițiile/evenimentele și le trimite când revine semnalul) este standard la trackerele Teltonika (memorie internă), dar nu rezolvă alarma în timp real; o alarmă SOS din pădure fără semnal ajunge doar dacă (a) există comunicator satelit sau (b) o rețea privată (LoRaWAN/Meshtastic) cu gateway propriu, care în pădure densă acoperă realist 0,3–2 km de la gateway – deci gateway-ul trebuie mutat cu echipa (pe mașina de teren, antenă ridicată).
- [ESTIMARE] D2C (satelit pe telefon obișnuit) nu poate fi planificat pentru pilotul 2026–2027 în România; poate fi menționat ca evoluție viitoare în soluția completă.

### Gaps (Lacune)
- Date efective de acoperire pe localitățile și pădurile din Bihor (aisemnal.ro nu a putut fi accesat; Netograf necercetat).
- Starea actuală (2026) a rețelelor LTE-M/NB-IoT la Orange, Vodafone și Digi, prețuri SIM M2M/IoT – căutarea nu a mai putut rula.
- Număr de gateway-uri TTN active în Bihor; prețul unui gateway LoRaWAN outdoor (ESTIMARE neverificată: câteva sute de euro) – căutarea nu a mai putut rula.
- Test controlat de rază Meshtastic în pădure la 868 MHz – nu există în rezultate; doar relatări anecdotice.
- Prețuri în EUR pentru abonamente satelit (inReach, SPOT, Zoleo) în România/UE.

---

## 8. Intrări pentru recomandarea de pilot (20–50 lucrători, construcții sau forestier)

### Takeaway (Concluzie)
Un integrator experimentat ar alege pentru pilot un tracker Teltonika cu man-down (GH5200 sau TMT250) pentru toți lucrătorii, plus 3–5 comunicatoare Garmin inReach Mini 2 pentru șefii de echipă din zonele forestiere fără semnal, și ar primi alarmele în platforma proprie printr-un server Codec 8 (ex. Traccar open-source sau implementare proprie) și prin webhook-ul Garmin IPC Outbound. Hardware total pentru 30 lucrători: ~4.000–7.000 € fără TVA; conectivitate: ~50–100 €/lună pentru SIM-uri + ~120–300 €/lună pentru 5 inReach; efort de integrare: ~2–4 săptămâni de dezvoltator.

### Cited Findings (Constatări cu sursă)
- Prețuri hardware folosite în calcul: GH5200 176,53 € fără TVA (RRP 224,99 €) [FAPT] — [Ascend](https://shop.ascend.de/en/products/teltonika-gh5200-personal-tracker-gh5200); GH5200 60 € fără TVA (Trialine, sursă slabă) [FAPT] — [Trialine](https://jonys.dev2.trialine.lv/catalogue/teltonika-gh5200-gps-tracker-personal_390/); TMT250 88,50 € fără TVA [FAPT] — [Sectron](https://eshop.sectron.eu/en/teltonika-tmt250-autonomni-osobni-tracker/p-15484/); inReach Mini 2 MSRP 349,99 USD [FAPT] — [SHI](https://www.shi.com/product/46469856/Garmin-inReach-Mini-2); abonament Professional Flex 24,99–64,99 USD/lună + 49,99 USD activare [FAPT] — [Garmin](https://garmin.com.my/minisite/inreach/professional); MSA ALTAIR io4 1.402,90 € fără TVA [FAPT] — [RS DE](https://de.rs-online.com/web/p/gasmelder/0315978); Cat S75 329,90 € [FAPT] — [Arvutitark](https://arvutitark.ee/en/smart-devices/phones/cat-s75-128gb-ds-black-66-5g-android-1255375)
- Garmin IPC Outbound împinge evenimentele către URL-ul integratorului (webhook, JSON cu scheme V2–V4). [FAPT] — [IPC Outbound](https://developer.garmin.com/inReach/IPC_Outbound.pdf)
- Platforme deschise/terțe care decodează deja dispozitivele candidate: Traccar (discuții Teltonika TAT100) [FAPT] — [Traccar forum](https://www.traccar.org/forums/topic/lifestock-tracker-with-long-battery-life/); flespi/GPS-Trace (Twig One) [FAPT] — [flespi](https://flespi.com/devices/twig-one); Navixy/Wialon (Queclink GL320MG) [FAPT] — [Navixy](https://www.navixy.com/devices/?p=6219)

### Inferences (Deducții) – scenariu de pilot recomandat
- Varianta A (recomandată, construcții + forestier, 30 lucrători):
  - 30 × Teltonika GH5200 (man-down, SOS, ecran) la 150–180 € fără TVA = 4.500–5.400 € [ESTIMARE pe baza prețului Ascend; dacă se confirmă prețul Trialine de 60 €, totalul scade la ~1.800 €].
  - Alternativ 30 × TMT250 la ~88,50 € = ~2.655 € fără TVA [FAPT preț unitar Sectron; ESTIMARE total], cu riscul 2G-only [DE VERIFICAT].
  - 5 × Garmin inReach Mini 2 la ~330–350 € = ~1.700 € [ESTIMARE din MSRP USD] pentru șefii de echipă în parchete fără semnal; abonament 5 × 24,99–64,99 USD = 125–325 USD/lună + 250 USD activare [FAPT tarife, ESTIMARE total].
  - Opțional 2 × MSA ALTAIR io4 (spații închise) = ~2.800 € fără TVA [ESTIMARE din preț RS DE]; integrarea API [DE VERIFICAT].
  - SIM IoT multi-rețea pentru 30 trackere: ~1–3 €/lună/SIM → 30–90 €/lună [ESTIMARE, fără sursă].
  - Total hardware pilot: ~4.000–7.000 € fără TVA (fără gaz) / ~7.000–10.000 € cu 2 detectoare [ESTIMARE].
- Varianta B (software-first, construcții, zone cu semnal): 30 × Cat S75 la ~330 € = ~9.900 € [ESTIMARE din preț unitar] + aplicație Android proprie (man-down pe accelerometru, SOS, puls prin ceas BLE opțional, indice de stres termic din meteo + efort). Avantaj: control total asupra algoritmilor și canalului (MQTT/HTTPS); dezavantaj: cost mai mare, validare proprie a algoritmului, telefonul trebuie purtat pe corp.
- Efort de integrare [ESTIMARE, bazat pe natura protocoalelor citate]: server Codec 8 prin Traccar + reguli de alarmă + webhook către platforma proprie: 5–10 zile-om; implementare proprie Codec 8 (TCP, parsare AVL, ACK): 10–15 zile-om; Garmin IPC Outbound (webhook JSON) + Inbound (trimitere mesaje): 3–5 zile-om; aplicație Android proprie cu man-down: 20–40 zile-om pentru un MVP, plus teste de teren.
- Ce ar necesita o soluție completă (după pilot): dispozitiv ATEX (Twig One Ex ~1.700 € fără TVA) pentru clienți din petrochimie/gaz; detector de gaze cu API confirmat (Blackline prin parteneriat, sau MSA/Dräger prin gateway); modul de proximitate UWB/RFID (ZoneSafe/Leica PA10) prin distribuitor; wearable de stres termic validat (Kenzen) sau abordare software-only clar etichetată ca non-medicală; gateway LoRaWAN mobil pentru parchete forestiere, până la apariția D2C comercial (~2027).

### Gaps (Lacune)
- Confirmarea protocolului și a rețelei pentru TMT250/GH5200 (Codec 8, 2G vs LTE) – blocată de lipsa accesului la wiki.teltonika-gps.com.
- Prețuri și disponibilitate la distribuitori din România (Teltonika, Garmin, MSA/Dräger).
- Prețuri reale SIM IoT/M2M în România.
- Date de acuratețe pentru algoritmii man-down (nu există public) – trebuie testate în pilot.

---

## Shortlist recomandată pentru pilot (rezumat)

- Dispozitiv principal (toți lucrătorii): Teltonika GH5200 (sau TMT250 dacă 2G e acceptabil) – man-down + SOS + localizare, protocol deschis Teltonika, 60–180 € fără TVA/buc; 30 buc = ~2.000–5.400 € fără TVA [ESTIMARE din prețuri citate].
- Dispozitiv secundar (zone fără semnal, 3–5 șefi de echipă): Garmin inReach Mini 2 – SOS + mesaje + tracking prin satelit, API IPC public; ~1.700 € hardware + 125–325 USD/lună abonamente [ESTIMARE].
- Opțional gaz (2 buc. partajate): MSA ALTAIR io4 ~1.403 € fără TVA/buc; integrare API [DE VERIFICAT].
- Conectivitate: SIM IoT multi-rețea (~30–90 €/lună pentru 30 SIM) [ESTIMARE]; măsurare de semnal pe teren înainte de pilot; store-and-forward activat; fără LoRaWAN/Meshtastic în faza 1.
- Integrare: Traccar (open-source) ca server Codec 8 + webhook spre platforma proprie; Garmin IPC Outbound ca webhook; ~2–4 săptămâni de dezvoltare [ESTIMARE].
- Buget total pilot (30 lucrători, 6 luni): hardware ~4.000–7.000 € fără TVA (fără gaz) + conectivitate ~1.000–2.500 € pe 6 luni [ESTIMARE]; cu 2 detectoare de gaz +~2.800 €.
- De evitat în pilot: Twig One (24.000+ € pentru 30 buc), Kenzen/SlateSafety (produse închise, ~800 CAD/buc + portal), sisteme de proximitate UWB/RFID (3.500–5.000 £ per utilaj, fără API public), smartwatch-uri de consum ca dispozitiv principal (autonomie, entitlement Apple, lipsă ATEX).
