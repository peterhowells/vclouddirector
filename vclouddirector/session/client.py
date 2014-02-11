from vclouddirector.common.client import Client
from vclouddirector.session.models.session import Session


class SessionClient(Client):
    def __init__(self, url):
        super(SessionClient, self).__init__()
        self.url = url

    def get_session(self, user, org, password):
        """
        Gets a new session
        :param user: username for authentication
        :type user: String
        :param org: organization for user authentication
        :type org: String
        :param password: password for user authentication
        :type password: String
        :rtype: Session
        """

        url = "{url}/sessions".format(url=self.url)
        auth = ("{user}@{org}".format(user=user, org=org), password)
        response = self.request('POST', url, headers=self.default_headers,
                                auth=auth)
        return response
