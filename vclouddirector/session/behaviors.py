from vclouddirector.session.client import SessionClient


class SessionBehaviors(object):
    def __init__(self, url):
        self.client = SessionClient(url)

    def authenticate(self, user, org, password):
        """
        :param user: username for authentication
        :type user: String
        :param org: organization for user authentication
        :type org: String
        :param password: password for user authentication
        :type password: String
        :rtype: string
        """
        response = self.client.get_session(user, org, password)
        return response.headers['x-vcloud-authorization']
