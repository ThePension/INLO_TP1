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

## Exercice 6 - Coverage

Name                         Stmts   Miss  Cover
------------------------------------------------
src\__init__.py                  0      0   100%
src\matrix_calulation.py         7      0   100%
src\string_manipulation.py      12      1    92%
src\wallet.py                   19      0   100%
------------------------------------------------
TOTAL                           38      1    97%


**Que représentent les pourcentages affichés?**
Le pourcentage du code qui est testé, pour chaque fichier.

Ici, le fichier `string_manipulation.py` n'est pas testé à 100%.


**Comment pytest sait-il quels fichiers analyser et quels fichiers ne pas analyser?**

Il analyse probablement les fichiers qui contiennent des functions préfixés par `test_`. et donc leurs dépendances.

Un fichier `__init__.py` doit également se trouver à la racine du répertoire à tester et analyser.

L'option `--cov=<path>` peut également être spécifié avec la commande `pytest` pour définir le répertoire à analyser.

### b)

Le fichier `string_manipulation.py` n'est pas testé à 100%. En effet, le levage d'exception pour la méthode `invert()` en cas d'argument de type non-string n'est pas testé.

Cela peut être remedié en ajoutant une méthode de test `test_raises_exception_on_non_string_arguments_invert()`.

Voici les résultats des tests après l'ajout de cette fonction :

Name                         Stmts   Miss  Cover
------------------------------------------------
src\__init__.py                  0      0   100%
src\matrix_calulation.py         7      0   100%
src\string_manipulation.py      12      0   100%
src\wallet.py                   19      0   100%
------------------------------------------------
TOTAL                           38      0   100%
