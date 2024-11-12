#Path: src/commontypes/state_provinceid_type.py
from dataclasses import dataclass

@dataclass
class StateProvinceIdType:
    """
    This is a common element used to define the state or province assigned identifier associated with an entity.

    Attributes:
        StateProvinceId (str): The identifier for this entity as assigned by the state or province.
    """
    StateProvinceId: str

    def __post_init__(self):
        if not isinstance(self.StateProvinceId, str | None):
            raise ValueError("StateProvinceId must be a string")
        if self.StateProvinceId is None:
            self.StateProvinceId = None
        if isinstance(self.StateProvinceId, str):
            self.StateProvinceId = self.StateProvinceId.strip()

    def __str__(self):
        return self.StateProvinceId

    def __repr__(self):
        return f"StateProvinceIdType(StateProvinceId='{self.StateProvinceId}')"

    def __lt__(self, other: "StateProvinceIdType") -> bool:
        return self.StateProvinceId < other.StateProvinceId

    def __le__(self, other: "StateProvinceIdType") -> bool:
        return self.StateProvinceId <= other.StateProvinceId

    def __gt__(self, other: "StateProvinceIdType") -> bool:
        return self.StateProvinceId > other.StateProvinceId

    def __ge__(self, other: "StateProvinceIdType") -> bool:
        return self.StateProvinceId >= other.StateProvinceId
    
    def __len__(self):
        return len(self.StateProvinceId)

    def __hash__(self):
        return hash(self.StateProvinceId)

    def __contains__(self, item):
        return item in self.StateProvinceId

    def __format__(self, format_spec):
        if format_spec == "upper":
            return self.StateProvinceId.upper()
        if format_spec == "lower":
            return self.StateProvinceId.lower()
        return self.StateProvinceId
