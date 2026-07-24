import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(abc.ABC):
    def __init__(self, is_transformed: bool = False):
        self.is_transformed = is_transformed

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass