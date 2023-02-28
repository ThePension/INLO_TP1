"""cProfile test package"""
import cProfile, pstats


def array_filling_1():
    """Creates an array and fill it with values from 0 to 10'000"""
    arr = []
    for i in range(100000):
        arr.append(i)
    print("Array created successfully")


def array_filling_2():
    """Creates an array and fill it with values from 0 to 10'000"""
    arr = list(range(100000))
    print("Array created successfully")


# TODO: Implémenter la méthode main.
# - Démarrer le profilage de CProfile
# - Appeler les 2 méthodes array_filling_<n>
# - Stopper le profilage
# - Utiliser pstats pour trier le profilage suivant la colonne 'ncalls'
# - Afficher les résultats dans la console.
def main():
    """Main function"""
    pass


# NOTE
# contrairement aux autres exercices, ici pour tester vous pouvez
# simplement appeler le fichier avec la commande python. Notez
# qu'il suffirait de renomer ce fichier et la fonction main() avec
# "test_" comme préfixe pour qu'elle soit automatiquement executée
# par la commande pytest.
if __name__ == "__main__":
    main()
