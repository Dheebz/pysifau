import pytest
from commontypes import OtherIdListType
from commontypes import OtherIdType

# Path: src/commontypes/test_other_id_list_type.py

def test_other_id_list_type_initialization():
    other_id_1 = OtherIdType(Type="ID1", Value="Value1")
    other_id_2 = OtherIdType(Type="ID2", Value="Value2")
    other_id_list = OtherIdListType([other_id_1, other_id_2])
    
    assert len(other_id_list.OtherIdList) == 2
    assert other_id_list.OtherIdList[0] == other_id_1
    assert other_id_list.OtherIdList[1] == other_id_2

def test_other_id_list_type_empty_initialization():
    other_id_list = OtherIdListType([])
    assert len(other_id_list.OtherIdList) == 0

def test_other_id_list_type_invalid_initialization():
    with pytest.raises(ValueError):
        OtherIdListType(["InvalidID"])
