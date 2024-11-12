#Path: src/commontypes/type_type.py

from dataclasses import dataclass

@dataclass
class TypeType:
    """
    A class to represent generic Types

    Attributes
        Type (str): The type of the object
    """
    Type:str

    def __post_init__(self):
        if not isinstance(self.Type, str):
            raise TypeError(f"Type must be a string, not {type(self.Type)}")
        
        if isinstance(self.Type, str):
            self.Type = self.Type.strip()   

        if not self.Type:
            raise ValueError("Type must not be empty")

        self.Type = self.Type.strip()

    def __str__(self):
        return self.Type

    def __repr__(self):
        return f"TypeType({self.Type})"
 
    def __lt__(self, other: 'TypeType'):
        return self.Type.casefold() < other.Type.casefold()

    def __le__(self, other: 'TypeType'):
        return self.Type.casefold() <= other.Type.casefold()

    def __gt__(self, other: 'TypeType'):
        return self.Type.casefold() > other.Type.casefold()

    def __ge__(self, other: 'TypeType'):
        return self.Type.casefold() >= other.Type.casefold()

    def __hash__(self):
        return hash(self.Type)

    def __len__(self):
        return len(self.Type)

    def __contains__(self, item):
        return item in self.Type
