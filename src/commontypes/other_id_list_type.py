#Path: src/commontypes/other_id_list_type.py

from dataclasses import dataclass , field
from typing import List

from commontypes import OtherIdType

@dataclass
class OtherIdListType:
    """
    OtherIdListType: A dataclass to represent a list of OtherIdType objects

    Attributes:
        OtherIdList (List[OtherIdType]): A list of OtherIdType objects
    """


    OtherIdList: List[OtherIdType] = field(default_factory=list)

    def __post_init__(self):
        if not all(isinstance(item,OtherIdType) for item in self.OtherIdList):
            raise ValueError("OtherIdListType:OtherIdList should be a list of OtherIdType objects")
