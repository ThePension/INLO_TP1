"""Locust test package"""
from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    """Test class for Locust"""

    @task
    def home(self):
        """Tests the home page"""
        self.client.get("/fr/")

    # TODO: implémenter 3 tests de plus
    #       Chaque test doit tester une route différente
    @task
    def about1(self):
        """Tests the about page"""
        self.client.get("/fr/aide-et-contact.html")

    @task
    def about2(self):
        """Tests the about page"""
        self.client.get("/fr/aide-et-contact.html")

    @task
    def subscribing1(self):
        """Tests the subscribing page"""
        self.client.get("/fr/abonnements-et-billets.html")

    @task
    def subscribing2(self):
        """Tests the subscribing page"""
        self.client.get("/fr/abonnements-et-billets.html")

    @task
    def subscribing3(self):
        """Tests the subscribing page"""
        self.client.get("/fr/abonnements-et-billets.html")

    @task
    def subscribing4(self):
        """Tests the subscribing page"""
        self.client.get("/fr/abonnements-et-billets.html")

    #       Chaque test doit être executé 2 fois plus de fois que le précédent.
