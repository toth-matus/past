# Štatistický projekt – Matúš Tóth – Students’ Social Media Addiction

Tieto dáta pochádzajú z datasetu: [Student Social Media & Relationships](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)  
Dataset obsahuje anonymizované záznamy o správaní študentov na sociálnych sieťach a súvisiacich životných výsledkoch.

Všetky python skripty, ako aj dáta, nájdete v GitHub repozitári:
https://github.com/toth-matus/past

## Test dobrej zhody

V tejto sekcii sa budeme sústrediť na vzťah premenných *Affects_Academic_Performance* a *Most_Used_Platform*.  
**Nulová hypotéza:** Respondenti pociťujú vplyv na svoje akademické výsledky bez ohľadu na platformu, na ktorej trávia čas.

Zdrojový kód sa nachádza v súbore `src/chi2_test.py` (alebo kliknite [sem](src/chi2_test.py))

Výsledky vyššie uvedeného skriptu sú:

```bash
All data chi^2 test:
Calculated chi^2: 29.33
Table value chi^2: 12.59
(With significance level: 0.05 and degree of freedom: 6)
```

Pre všetky dáta nulovú hypotézu **zamietame**, keďže naša nameraná hodnota $\chi^2$ bola vyššia ako tabuľková hodnota pre $\alpha = 0.05$.

Keď však zopakujeme predchádzajúci postup pre dáta, z ktorých sme odstránili používateľov platformy **LinkedIn**, nulovú hypotézu **nemôžeme zamietnuť**.

```bash
Chi^2 test without LinkedIn users:
Calculated chi^2: 8.02
Table value chi^2: 11.07
(With significance level: 0.05 and degree of freedom: 5)
```

K tomuto záveru som prišiel viac-menej náhodou. Môže to byť spôsobené tým, že:

- LinkedIn je platforma, na ktorej trávia používatelia relatívne málo času (viď `src/platform_time_spent.py` alebo kliknite [sem](src/platform_time_spent.py)),
- trávenie času na LinkedIn je častejšie u študentov, ktorí excelujú v škole,
- alebo úplne iným dôvodom.

Priemerný strávený čas na platformách:  
![Priemerný čas](img/platform_average.png)

## Štatistika korelácie

V tejto sekcii sa budeme sústrediť na koreláciu premenných *Avg_Daily_Usage_Hours* a *Sleep_Hours_Per_Night*.  
**Nulová hypotéza:** Medzi *Avg_Daily_Usage_Hours* a *Sleep_Hours_Per_Night* nie je korelácia.

Zdrojový kód sa nachádza v súbore `src/correlation_test.py` (alebo kliknite [sem](src/correlation_test.py)).

Výsledok vyššie uvedeného skriptu je:

```bash
Spearman rho value: -0.96
p-value: 1.5570570249936598e-62
```

Z hodnoty $\rho$ vyplíva, že existuje silná inverzná závislosť medzi *Avg_Daily_Usage_Hours* a *Sleep_Hours_Per_Night*.(Samozrejme, nejde o dôkaz kauzality)  
Z hodnoty $p < 0.05$ môžeme zamietnuť nulovú hypotézu (pre $\alpha = 0.05$) a predpokladať, že medzi dátami existuje korelácia.

Naplottované dáta:  
![Korelácia](img/correlation.png)
