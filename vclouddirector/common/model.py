class Model(object):
    def __init__(self):
        pass

    def serialize(self, deserialized_obj):
        raise NotImplementedError

    def deserialize(self, serialized_str):
        raise NotImplementedError


class ListModel(object):
    def __init__(self):
        pass
