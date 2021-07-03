import pytest
from core.prediction import get_prediction

@pytest.fixture(scope = 'module')
def json()
    json=get_prediction("./assets/test/testfile.txt")
    return json

def test_fields_count(json):
    assert len(json['resource']) ==4, "should be 4 fileds"

def test_incoprporation_number(json):
    assert json['resource']['incoprpotration_number'] =='280935','280935'

def test_incoprporation_date(json):
    assert json['resource']['incoprpotration_date'] == "18 april 1993"
