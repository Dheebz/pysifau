import pytest

from commontypes import LocalIdType


def test_local_id_initialization():
    local_id = LocalIdType("  test_id  ")
    assert local_id.LocalId == "test_id"

def test_local_id_initialization_with_none():
    local_id = LocalIdType(None)
    assert local_id.LocalId is None

def test_local_id_initialization_with_invalid_type():
    with pytest.raises(TypeError):
        LocalIdType(12345)

def test_local_id_str():
    local_id = LocalIdType("test_id")
    assert str(local_id) == "test_id"

def test_local_id_repr():
    local_id = LocalIdType("test_id")
    assert repr(local_id) == "LocalIdType(LocalId='test_id')"

def test_local_id_equality():
    local_id1 = LocalIdType("test_id")
    local_id2 = LocalIdType("test_id")
    assert local_id1 == local_id2

def test_local_id_inequality():
    local_id1 = LocalIdType("test_id1")
    local_id2 = LocalIdType("test_id2")
    assert local_id1 != local_id2

def test_local_id_comparison():
    local_id1 = LocalIdType("a")
    local_id2 = LocalIdType("b")
    assert local_id1 < local_id2
    assert local_id1 <= local_id2
    assert local_id2 > local_id1
    assert local_id2 >= local_id1

def test_local_id_hash():
    local_id = LocalIdType("test_id")
    assert hash(local_id) == hash("test_id")

def test_local_id_length():
    local_id = LocalIdType("test_id")
    assert len(local_id) == len("test_id")

def test_local_id_contains():
    local_id = LocalIdType("test_id")
    assert "test" in local_id
    assert "id" in local_id
    assert "not" not in local_id

def test_local_id_format_upper():
    local_id = LocalIdType("test_id")
    assert format(local_id, "upper") == "TEST_ID"

def test_local_id_format_lower():
    local_id = LocalIdType("TEST_ID")
    assert format(local_id, "lower") == "test_id"

def test_local_id_format_invalid():
    local_id = LocalIdType("test_id")
    assert format(local_id, "invalid") == "test_id"
    