import pytest

from commontypes import RefIdType


ref_id_types = [
    RefIdType
]

VALID_2X_GUID = "0123456789ABCDEF0123456789ABCDEF"
VALID_3X_GUID = "01234567-89AB-CDEF-0123-456789ABCDEF"
INVALID_GUID = "INVALID_GUID"

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_valid_2x_guid(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert ref_id.RefId == VALID_2X_GUID

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_valid_3x_guid(RefIdType):
    ref_id = RefIdType(VALID_3X_GUID)
    assert ref_id.RefId == VALID_3X_GUID

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_invalid_guid(RefIdType):
    with pytest.raises(ValueError):
        RefIdType(INVALID_GUID)

    with pytest.raises(ValueError,match="RefId must be of type str"):
        RefIdType(123456)
    
    with pytest.raises(ValueError,match="RefId must be a valid GUID"):
        RefIdType("INVALID_GUID")


@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_str_method(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert str(ref_id) == VALID_2X_GUID

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_repr_method(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert repr(ref_id) == f"RefIdType(RefId='{VALID_2X_GUID}')"

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_comparison_methods(RefIdType):
    VALID_2X_GUID_2 = "0B23456789ABCDEF0123456789ABCDEF"
    VALID_3X_GUID_2 = "0B234567-89AB-CDEF-0123-456789ABCDEF"

    ref_id = RefIdType(VALID_2X_GUID)
    ref_id_2 = RefIdType(VALID_2X_GUID_2)
    ref_id_3 = RefIdType(VALID_3X_GUID)
    ref_id_4 = RefIdType(VALID_3X_GUID_2)

    assert ref_id < ref_id_2
    assert ref_id_2 > ref_id
    assert ref_id <= ref_id_2
    assert ref_id_2 >= ref_id

    assert ref_id_3 < ref_id_4
    assert ref_id_4 > ref_id_3
    assert ref_id_3 <= ref_id_4
    assert ref_id_4 >= ref_id_3



@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_hash_method(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert hash(ref_id) == hash(VALID_2X_GUID)

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_len_method(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert len(ref_id) == len(VALID_2X_GUID)

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_contains_method(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert "0123" in ref_id
    assert "ZZZZ" not in ref_id

@pytest.mark.parametrize("RefIdType", ref_id_types)
def test_format_method(RefIdType):
    ref_id = RefIdType(VALID_2X_GUID)
    assert format(ref_id, "upper") == VALID_2X_GUID.upper()
    assert format(ref_id, "lower") == VALID_2X_GUID.lower()
    assert format(ref_id, "") == VALID_2X_GUID
