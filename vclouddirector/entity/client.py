from vclouddirector.common.client import Client
from vclouddirector.entity.models.entity import Entity


class EntityClient(Client):
    def __init__(self, url, auth_token):
        super(EntityClient, self).__init__()
        self.url = url
        self.auth_token = auth_token
        self.default_headers['x-vcloud-authorization'] = self.auth_token

    def get_entity(self, id):
        """
        Gets details about an entity
        :param id: id of the entity
        :type id: string
        :rtype: Entity
        """

        url = "{url}/entity/{id}".format(url=self.url, id=id)
        response = self.request('GET', url, headers=self.default_headers,
                                response_type=Entity)
        return response
