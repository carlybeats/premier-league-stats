import pytest
import os
from goal_data import write_to_json_file
from utils.goal_utils import scrape_goal_data, get_num_of_players_in_table
from analysis.goal_analysis import retrieve_filepath, base_dataframe
from unittest.mock import patch
import json
import pandas as pd

# Set an environment variable
os.environ["TESTING"] = "True"
script_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.mark.skip
@patch("goal_data.scrape_goal_data")
def test_write_to_json_success(mock_scrape_goal_data):
    mock_scrape_goal_data.return_value = [{"rank": 1,
        "name": "Mohamed Salah",
        "team": "Liverpool",
        "nationality": "Egypt",
        "goals_scored": 100}]
    result = write_to_json_file()
    filepath = os.path.join(script_dir, "test_goals.json")
    print(filepath)
    with open(filepath, 'r') as f:
        test_data = json.load(f)
    assert result == "Write to JSON file successful!"
    assert test_data[0]['name'] == "Mohamed Salah"
    
@pytest.mark.skip
def test_correct_num_of_players_returned():
    #Number of players extracted (result[0]) should match the number of players stored in the table
    #  on premier league website (result[1])
    result = scrape_goal_data()
    print(result)
    assert len(result[0]) == result[1]

@pytest.mark.skip
@patch("utils.goal_utils.get_num_of_players_in_table")
def test_wrong_num_of_players_extracted_raises_exception(mock_get_num_of_players_in_table):
    mock_get_num_of_players_in_table.return_value = 67199
    with pytest.raises(Exception) as e:
        scrape_goal_data()
    assert str(e.value) == "Erroneous amount of players extracted. Please run program again"


def test_retrieve_filepath_returns_correct_path():
    result = retrieve_filepath()
    desired_filepath = os.path.join(script_dir, "test_goals.json")
    assert result == desired_filepath

def test_base_dataframe_returns_valid_format():
    result = base_dataframe()
    assert result['rank'][0] == 1
    assert result['name'][0] == "Mohamed Salah"
    assert result['team'][0] == 'Liverpool'
    assert result['nationality'][0] == 'Egypt'
    assert result['goals_scored'][0] == 100
