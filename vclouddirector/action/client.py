from vclouddirector.common.client import Client


class ActionClient(Client):
    """
This will be the client that will take in the url to hit and the auth header value
"""
    def __init__(self, url):
        super(ActionClient, self).__init__()
        self.url = url

    def execute_get(self, headers):
        """
        GET the url provided
        """

        response = self.request('GET', self.url, headers=headers)
        return response

    def execute_post(self, headers, payload=None):
        """
        GET the url provided
        """
        req_kwargs = dict({'data': payload})

        response = self.request('POST', self.url, headers=headers, kwargs=req_kwargs)
        return response

    def execute_delete(self, headers, payload=None):
        """
        DELETE the url provided
        """
        req_kwargs = dict({'data':payload})

        response = self.request('DELETE', self.url, headers=headers, kwargs=req_kwargs)
        return response

    def execute_put(self, headers, payload=None):
        """
        PUT the url provided
        """

        req_kwargs = dict({'data':payload})

        response = self.request("PUT", self.url, headers=headers, kwargs=req_kwargs)
        return response
