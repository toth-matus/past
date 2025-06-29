# Štatistický projekt – Matúš Tóth – Students’ Social Media Addiction

Tieto dáta pochádzajú z datasetu: [Student Social Media & Relationships](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)
Dataset obsahuje anonymizované záznamy o správaní študentov na sociálnych sieťach a súvisiacich životných výsledkoch.

Všetky python skripty, ako aj dáta, nájdete v GitHub repozitári:
https://github.com/toth-matus/past

## Test dobrej zhody

V tejto sekcii sa budeme sústrediť na premenné *Affects_Academic_Performance* vzhľadom k *Most_Used_Platform*.
**Nulová hypotéza:** Respondenti pociťujú vplyv na svoje akademické výsledky bez ohľadu na platformu, na ktorej trávia čas.

Zdrojový kód sa nachádza v súbore `src/chi2_test.py` (alebo kliknite [sem](src/chi2_test.py))

Výsledky vyššie uvedeného skriptu sú:

```bash
All data chi^2 test:
Calculated chi^2: 29.33
Table value chi^2: 12.59
(With significance level: 0.05 and degree of freedom: 6)

Chi^2 test without LinkedIn users:
Calculated chi^2: 8.02
Table value chi^2: 11.07
(With significance level: 0.05 and degree of freedom: 5)
```

Pre všetky dáta nulovú hypotézu **zamietame**, keďže naša nameraná hodnota $\chi^2$ bola vyššia ako tabuľková hodnota pre $\alpha = 0.05$.

Keď však zopakujeme predchádzajúci postup pre dáta, z ktorých sme odstránili používateľov platformy **LinkedIn**, nulovú hypotézu **nemôžeme zamietnuť**.

## Statisika korelacie

<!-- TODO -->
