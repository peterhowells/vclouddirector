import requests

ACCEPT_HEADER = 'application/*+xml;version=1.5'


class Client(object):
    def __init__(self):
        self.default_headers = {'accept': ACCEPT_HEADER}

    def request(self, method=None, url=None, headers=None, data=None,
                params=None, auth=None, verify=False, response_type=None,
                kwargs=None):

        # Default to empty dictionaries
        headers = headers or {}
        kwargs = kwargs or {}
        params = params or {}

        # add default headers
        req_headers = {}
        req_headers.update(self.default_headers)
        req_headers.update(headers)

        req_kwargs = dict({'headers': req_headers,
                           'params': params,
                           'data': data,
                           'verify': verify,
                           'auth': auth},
                          **kwargs)

        response = requests.request(method, url, **req_kwargs)

        if response_type:
            setattr(response, 'instance', response_type.deserialize(
                response.content))

        return response
