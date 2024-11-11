#Path: src/commontypes/ref_id_type.py
import re
from dataclasses import dataclass

@dataclass
class RefIdType:
    """
    An object or element identifier

    Atrributes:
        RefId:str - An object or element identifier
    """
    RefId:str
    def __post_init__(self):
        if not isinstance(self.RefId,str):
            raise ValueError("RefId must be of type str")
        
        GUID_2X_PATT = re.compile(r'^[0-9A-F]{32}$', re.IGNORECASE)
        GUID_3X_PATT = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$', re.IGNORECASE)

        if not GUID_2X_PATT.match(self.RefId) and not GUID_3X_PATT.match(self.RefId):
            raise ValueError("RefId must be a valid GUID")
        self.RefId = self.RefId
        return self.RefId


    def __str__(self):
        return self.RefId

    def __repr__(self):
        return f"RefIdType(RefId='{self.RefId}')"

    def __lt__(self, other: "RefIdType") -> bool:
        return self.RefId.casefold() < other.RefId.casefold()

    def __le__(self, other: "RefIdType") -> bool:
        return self.RefId.casefold() <= other.RefId.casefold()

    def __gt__(self, other: "RefIdType") -> bool:
        return self.RefId.casefold() > other.RefId.casefold()

    def __ge__(self, other: "RefIdType") -> bool:
        return self.RefId.casefold() >= other.RefId.casefold()

    def __hash__(self) -> int:
        return hash(self.RefId)

    def __len__(self) -> int:
        return len(self.RefId)

    def __contains__(self, item: str) -> bool:
        return item in self.RefId

    def __format__(self,format_spec:str) -> str:
        if format_spec == "upper":
            return self.RefId.upper()
        if format_spec == "lower":
            return self.RefId.lower()
        return self.RefId
#End of File
