import pytest
from django_chinese_medicine.models import (Result, Etiologie, DiseasePattern,
    Therapy)


@pytest.mark.django_db
def test_result(result):
    """Instances become fixtures automatically."""
    assert isinstance(result, Result)


@pytest.mark.django_db
def test_etiologie(etiologie):
    """Instances become fixtures automatically."""
    assert isinstance(etiologie, Etiologie)


@pytest.mark.django_db
def test_disease_pattern(disease_pattern):
    assert isinstance(disease_pattern, DiseasePattern)


@pytest.mark.django_db
def test_therapy(therapy):
    assert isinstance(therapy, Therapy)
