import pytest
from commontypes import TypeType

# Path: src/commontypes/test_type_type.py


VALID_TYPE = "ExampleType"
INVALID_TYPE = 12345
EMPTY_TYPE = ""

def test_valid_type():
    type_instance = TypeType(VALID_TYPE)
    assert type_instance.Type == VALID_TYPE

def test_invalid_type():
    with pytest.raises(TypeError):
        TypeType(INVALID_TYPE)

def test_empty_type():
    with pytest.raises(ValueError):
        TypeType(EMPTY_TYPE)

def test_str_method():
    type_instance = TypeType(VALID_TYPE)
    assert str(type_instance) == VALID_TYPE

def test_repr_method():
    type_instance = TypeType(VALID_TYPE)
    assert repr(type_instance) == f"TypeType({VALID_TYPE})"

def test_comparison_methods():
    type_instance_1 = TypeType("a")
    type_instance_2 = TypeType("b")

    assert type_instance_1 < type_instance_2
    assert type_instance_2 > type_instance_1
    assert type_instance_1 <= type_instance_2
    assert type_instance_2 >= type_instance_1

def test_hash_method():
    type_instance = TypeType(VALID_TYPE)
    assert hash(type_instance) == hash(VALID_TYPE)

def test_len_method():
    type_instance = TypeType(VALID_TYPE)
    assert len(type_instance) == len(VALID_TYPE)

def test_contains_method():
    type_instance = TypeType(VALID_TYPE)
    assert "Example" in type_instance
    assert "Invalid" not in type_instance