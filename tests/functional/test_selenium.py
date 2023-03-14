import time
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
        browser = webdriver.Firefox(
            service=Service(executable_path=GeckoDriverManager().install())
        )

        browser.maximize_window()

        # Opens HE-Arc website.
        browser.get("https://www.he-arc.ch")

        time.sleep(1)

        # Accept cookies
        cookies_button = browser.find_element(By.ID, "axeptio_btn_acceptAll")
        cookies_button.click()

        ##### YOUR CODE HERE #####

        # Click on Ra&D
        rad_button = browser.find_element(By.ID, "w-dropdown-toggle-3")
        rad_button.click()

        time.sleep(0.1)

        # Click on domain
        domain_button = browser.find_element(
            By.XPATH,
            "/html/body/header/div/div[1]/div[1]/div/nav[2]/div/div[2]/div[2]/nav/div/div[2]/div/div/div[1]/div[2]/a",
        )
        domain_button.click()

        # Click on engineer list
        engineer_button = browser.find_element(By.ID, "accordion-block_619259e970051")
        engineer_button.click()

        # Click on data science
        data_button = browser.find_element(
            By.XPATH,
            "/html/body/main/article/section/div[2]/div[1]/div/div/div[3]/div[2]/div/div/ul[5]/li[1]/a",
        )
        data_button.click()

        # Prof cards
        prof_cards = browser.find_elements(
            By.XPATH,
            "/html/body/main/article/section[1]/div[2]/div[1]/div/div[3]/descendant::h3",
        )

        teachers = [
            "Dr Fabrizio Albertetti",
            "Cédric Bilat",
            "Dr Stefano Carrino",
            "Dr Hatem Ghorbel",
            "Dr Marcelo Pasin",
        ]
        for i in range(0, len(teachers)):
            assert prof_cards[i].text == teachers[i]

        ##########################

        # Close Geckodriver
        browser.quit()
