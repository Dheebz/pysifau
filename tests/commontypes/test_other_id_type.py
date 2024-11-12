# Path: src/commontypes/test_other_id_type.py
import pytest
from commontypes import OtherIdType


VALID_TYPE = "ExampleType"
VALID_VALUE = "ExampleValue"
EMPTY_TYPE = ""
EMPTY_VALUE = ""

def test_valid_other_id_type():
    other_id_instance = OtherIdType(VALID_TYPE, VALID_VALUE)
    assert other_id_instance.Type == VALID_TYPE
    assert other_id_instance.Value == VALID_VALUE

def test_empty_type():
    with pytest.raises(ValueError):
        OtherIdType(EMPTY_TYPE, VALID_VALUE)

def test_empty_value():
    with pytest.raises(ValueError):
        OtherIdType(VALID_TYPE, EMPTY_VALUE)

def test_str_method():
    other_id_instance = OtherIdType(VALID_TYPE, VALID_VALUE)
    assert str(other_id_instance) == f"{VALID_TYPE}: {VALID_VALUE}"

def test_repr_method():
    other_id_instance = OtherIdType(VALID_TYPE, VALID_VALUE)
    assert repr(other_id_instance) == f"OtherIdType(Type='{VALID_TYPE}', Value='{VALID_VALUE}')"

def test_comparison_methods():
    other_id_instance_1 = OtherIdType("a", "value1")
    other_id_instance_2 = OtherIdType("b", "value2")

    assert other_id_instance_1 < other_id_instance_2
    assert other_id_instance_2 > other_id_instance_1
    assert other_id_instance_1 <= other_id_instance_2
    assert other_id_instance_2 >= other_id_instance_1

def test_hash_method():
    other_id_instance = OtherIdType(VALID_TYPE, VALID_VALUE)
    assert hash(other_id_instance) == hash(VALID_TYPE)
