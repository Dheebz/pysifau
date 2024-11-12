#Path: src/commontypes/local_id_type.py

from dataclasses import dataclass

@dataclass
class LocalIdType:
    """
    LocalIdType: A dataclass to represent a LocalIdType object

    Attributes:
        LocalId (str): A string representing a LocalIdType object
    """
    LocalId: str

    def __post_init__(self):
        if isinstance(self.LocalId, str):
            self.LocalId = self.LocalId.strip()
        if self.LocalId is None:
            self.LocalId = None #FIXME: This probably isn't actually going to work. None is not assignable to a string
        if not isinstance(self.LocalId, str | None):
            raise TypeError(f"LocalId must be a string, not {type(self.LocalId)}")
    def __str__(self) -> str:
        return self.LocalId

    def __repr__(self) -> str:
        return f"LocalIdType(LocalId='{self.LocalId}')"

    def __lt__(self, other:"LocalIdType") -> bool:
        return self.LocalId < other.LocalId

    def __le__(self, other:"LocalIdType") -> bool:
        return self.LocalId <= other.LocalId

    def __gt__(self, other:"LocalIdType") -> bool:
        return self.LocalId > other.LocalId

    def __ge__(self, other:"LocalIdType") -> bool:
        return self.LocalId >= other.LocalId

    def __hash__(self) -> int:
        return hash(self.LocalId)

    def __len__(self) -> int:
        return len(self.LocalId)

    def __contains__(self, item:str) -> bool:
        return item in self.LocalId

    def __format__(self, format_spec:str) -> str:
        if format_spec == "upper":
            return self.LocalId.upper()
        if format_spec == "lower":
            return self.LocalId.lower()
        return self.LocalId

__slots__ = ["LocalId"]
#End of file

