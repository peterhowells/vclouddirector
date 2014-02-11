import xml.etree.ElementTree as ET

from vclouddirector.common.model import Model
from vclouddirector.common.model import ListModel


class Entity(Model):
    def __init__(self, href, xs_type, name, xs_id, vcloud_extension, link,
                 description, tasks):
        self.href = href
        self.xs_type = xs_type
        self.name = name
        self.xs_id = xs_id
        self.vcloud_extension = vcloud_extension
        self.link = link
        self.description = description
        self.tasks = tasks

    @classmethod
    def deserialize(self, serialized_str):
        """
        Returns a Entity based on XML string
        :param serialized_str: Entity XML string
        :type serialized_str: str
        :rtype: Entity
        """

        element = ET.fromstring(serialized_str)
        return element
