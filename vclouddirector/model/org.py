import xml.etree.ElementTree as ET

from vclouddirector.common.model import Model
from vclouddirector.common.model import ListModel


class Org(Model):
    def __init__(self, href, xs_type, name, id):
        self.href = href
        self.xs_type = xs_type
        self.name = name

    @classmethod
    def deserialize(self, serialized_str):
        """
        Returns a Org based on XML string
        :param serialized_str: Entity XML string
        :type serialized_str: str
        :rtype: Entity
        """

        element = ET.fromstring(serialized_str)
        return element
