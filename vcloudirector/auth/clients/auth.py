from vclouddirector.common.client import Client
from vclouddirector.auth.models import Versions


class AuthClient(Client):
    def __init__(self, url):
        self.url = url

    def versions(self):
        url = "{0}/versions".format(self.url)
        resp = self.request('GET', url, response_type=Versions)
        return resp
