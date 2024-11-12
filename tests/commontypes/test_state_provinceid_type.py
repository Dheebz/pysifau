import pytest

from commontypes import StateProvinceIdType


def test_state_provinceid_initialization():
    state_provinceid = StateProvinceIdType("  test_id  ")
    assert state_provinceid.StateProvinceId == "test_id"

def test_state_provinceid_initialization_with_none():
    state_provinceid = StateProvinceIdType(None)
    assert state_provinceid.StateProvinceId is None

def test_state_provinceid_initialization_with_invalid_type():
    with pytest.raises(ValueError):
        StateProvinceIdType(12345)

def test_state_provinceid_str():
    state_provinceid = StateProvinceIdType("test_id")
    assert str(state_provinceid) == "test_id"

def test_state_provinceid_repr():
    state_provinceid = StateProvinceIdType("test_id")
    assert repr(state_provinceid) == "StateProvinceIdType(StateProvinceId='test_id')"

def test_state_provinceid_equality():
    state_provinceid1 = StateProvinceIdType("test_id")
    state_provinceid2 = StateProvinceIdType("test_id")
    assert state_provinceid1 == state_provinceid2

def test_state_provinceid_inequality():
    state_provinceid1 = StateProvinceIdType("test_id1")
    state_provinceid2 = StateProvinceIdType("test_id2")
    assert state_provinceid1 != state_provinceid2

def test_state_provinceid_comparison():
    state_provinceid1 = StateProvinceIdType("a")
    state_provinceid2 = StateProvinceIdType("b")
    assert state_provinceid1 < state_provinceid2
    assert state_provinceid1 <= state_provinceid2
    assert state_provinceid2 > state_provinceid1
    assert state_provinceid2 >= state_provinceid1

def test_state_provinceid_hash():
    state_provinceid = StateProvinceIdType("test_id")
    assert hash(state_provinceid) == hash("test_id")

def test_state_provinceid_length():
    state_provinceid = StateProvinceIdType("test_id")
    assert len(state_provinceid) == len("test_id")

def test_state_provinceid_contains():
    state_provinceid = StateProvinceIdType("test_id")
    assert "test" in state_provinceid
    assert "id" in state_provinceid
    assert "not" not in state_provinceid

def test_state_provinceid_format_upper():
    state_provinceid = StateProvinceIdType("test_id")
    assert format(state_provinceid, "upper") == "TEST_ID"

def test_state_provinceid_format_lower():
    state_provinceid = StateProvinceIdType("TEST_ID")
    assert format(state_provinceid, "lower") == "test_id"

def test_state_provinceid_format_invalid():
    state_provinceid = StateProvinceIdType("test_id")
    assert format(state_provinceid, "invalid") == "test_id"
