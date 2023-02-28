from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class TestSeleniumFunctional:
    """Functional tests class using selenium"""

    # TODO: Implémenter la méthode test_get_research_assistants qui réalise les actions suivantes:
    # - Ouvrir Firefox
    # - Se rendre sur la page www.he-arc.ch
    # - Accepter les cookies
    # - Cliquer sur le bouton "Ra&D"
    # - Cliquer sur le bouton "Domaines de compétences"
    # - Ouvrir la liste "Ingénierie"
    # - Cliquer sur le groupe de compétence "Analyse de données"
    # - Ecrire le nom de chaque professeurs (section "Professeur-e-s" de la page) dans la console

    # Les 3 premières étapes sont déjà implémentées pour vous, il suffit de décommenter les lignes.

    def test_get_teachers(self):
        """Opens the He-Arc website and prints the list of teachers from the 'Analyse de données' competence group."""

        # Loads Geckodriver
        # browser = webdriver.Firefox(
        #    service=Service(executable_path=GeckoDriverManager().install())
        # )

        # Opens HE-Arc website.
        # browser.get("https://www.he-arc.ch")

        # Accept cookies
        # cookies_button = browser.find_element(By.ID, "axeptio_btn_acceptAll")
        # cookies_button.click()

        ##### YOUR CODE HERE #####

        ##########################

        # Close Geckodriver
        # browser.quit()
        assert False
