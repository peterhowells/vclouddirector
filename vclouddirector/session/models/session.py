from vclouddirector.common.model import Model


class Session(Model):
    def __init__(self, authorization):
        self.authorization = authorization

    @classmethod
    def deserialize(self, serialized_str):
        """
        Returns a Session based on XML string
        :param serialized_str: Session XML string
        :type serialized_str: str
        :rtype: Session
        """

        element = ET.fromstring(serialized_str)
        return element
