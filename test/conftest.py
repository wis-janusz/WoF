import pytest
import pandas as pd
import wop.utils as utils


@pytest.fixture
def test_projects():
    return "test/test_projects.json"


@pytest.fixture
def appended_test_projects():
    return "test/appended_test_projects.json"


@pytest.fixture
def test_projects_df():
    return pd.DataFrame(
        {
            "Name": ["Test1", "Test2"],
            "Type": ["Painitng", "Building"],
            "Completed": ["No", "Yes"],
        }
    )


@pytest.fixture
def appended_test_projects_df():
    return pd.DataFrame(
        {
            "Name": ["Test1", "Test2", "Test3"],
            "Type": ["Painitng", "Building", "Painting"],
            "Completed": ["No", "Yes", "No"],
        }
    )


@pytest.fixture
def added_test_project():
    return {"Name": "Test3", "Type": "Painting", "Completed": "No"}
