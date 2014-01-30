from vclouddirector.common.model import Model
from vclouddirector.common.model import ListModel


class Version(Model):
    def __init__(self, version=None, login_url=None, media_type_mappings=None):
        self.version = version
        self.login_url = login_url
        self.media_type_mappings = media_type_mappings

    def serialize(self, version):
        pass

    def deserialize(self, serialized_str):
        pass


class Versions(ListModel):

    version_type = Version

    @classmethod
    def serialize(cls, version, login_url, e_mappings):
        pass
