import pytest
from pathlib import Path

@pytest.fixture
def test_projects():
    return 'test/test_projects.yml'

@pytest.fixture
def test_projects_dict():
    return {'Test1':'Building','Test2':'Painting'}


@pytest.fixture
def appended_test_projects():
    return 'test/appended_test_projects.yml'

@pytest.fixture
def appended_test_projects_dict():
    return {'Test1':'Building','Test2':'Painting', 'Test3':'Painting'}

@pytest.fixture
def added_test_project():
    return ('Test3', 'Painting')