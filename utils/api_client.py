import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self, page=1):
        return requests.get(f"{self.base_url}/users", params={"page": page})

    def create_user(self, name, job):
        return requests.post(f"{self.base_url}/users", json={"name": name, "job": job})
