#Path: src/commontypes/other_id_type.py

from dataclasses import dataclass 

@dataclass
class OtherIdType:
    """
    OtherIdType class is a dataclass that represents the OtherIdType object.

    Attributes:
        Type (str): The type of the other id.
        Value (str): The value of the other id.
    """
    Type:str
    Value:str

    def __post_init__(self):
        if not self.Type:
            raise ValueError("OtherIDType:Type is required")
        if not self.Value:
            raise ValueError("OtherIdType:Value is required")
    
    def __str__(self):
        return f"{self.Type}: {self.Value}"

    def __repr__(self):
        return f"OtherIdType(Type='{self.Type}', Value='{self.Value}')"

    def __ge__(self, other: 'OtherIdType') -> bool:
        return self.Type >= other.Type

    def __gt__(self, other: 'OtherIdType') -> bool:
        return self.Type > other.Type
    
    def __le__(self, other: 'OtherIdType') -> bool:
        return self.Type <= other.Type
    
    def __lt__(self, other: 'OtherIdType') -> bool:
        return self.Type < other.Type

    def __hash__(self) -> int:
        return hash(self.Type)
