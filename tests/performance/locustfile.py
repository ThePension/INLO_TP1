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
    #       Chaque test doit être executé 2 fois plus de fois que le précédent.
