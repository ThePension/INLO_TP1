## Exercice 5 - Tests de performance

### a)

**Que constatez-vous ? Y a-t-il une différence entre les temps d’exécutions des 2 fonctions ? Si oui, laquelle est la plus rapide, et pourquoi?**

La deuxième méthode (`array_filling_2()`) est bien plus rapide, avec un temps total (`tottime`) de 0.001 seconde.
La première méthode (`array_filling_1()`), quant à elle, prend 0.021 seconde à s'exécuter.

Cela est principalement dû au fait que la deuxième méthode utilise les fonctions préfinies `range()` et `list()` mises à disposition par Python, au lieu d'une simple boule `for`. Avec une boucle `for`, à chaque ajout d'un élément, la méthode `append` doit être utilisée. Celle-ci est très coûteuse en temps.

### b)

**Combien de routes différentes sont testées?**

3

**Que sont les RPS et pourquoi sont-elles différentes pour chaque route?**

RPS correspond au nombre de requêtes effectués par seconde.

Elles différent en fonction des routes car les informations retournées par la requête ne se sont pas les mêmes et peuvent prendre plus ou moins de temps en fonction de leur taille (champ `average size`).

**Quelle route possède la meilleure performance?**

La home page (`/fr`). Les données sont disponibles dans le fichier `./report.html`, qui se trouve à la racine du projet.
