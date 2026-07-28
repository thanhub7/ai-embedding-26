class Embedding:
    def __init__(self, vector, metadata=None):
        self.vector = vector
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "vector": self.vector,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            vector=data.get("vector"),
            metadata=data.get("metadata")
        )