import pytest
import os
from goal_data import write_to_json_file
from utils.goal_utils import retrieve_goal_data
from unittest.mock import patch
import json

# Set an environment variable
os.environ["TESTING"] = "True"

# Rewrite this test its nonsense
@patch("goal_data.retrieve_goal_data")
def test_write_to_json_returns_in_dict_format(mock_retrieve_goal_data):
    mock_retrieve_goal_data.return_value = [{"name": "Mohamed Salah",
        "team": "Liverpool",
        "nationality": "Egypt",
        "goals_scored": 27}]
    str_result = write_to_json_file()
    list_result = json.loads(str_result)
    result = list_result
    assert type(result) == dict
    assert result['name'] == 'Mohamed Salah'
    assert result['team'] == 'Liverpool'
    assert result['nationality'] == 'Egypt'
    assert result['goals_scored'] == 27

def test_correct_num_of_players_returned():
    #Number of players extracted (result[0]) should match the number of players stored in the table
    #  on premier league website (result[1])
    result = retrieve_goal_data()
    print(result)
    assert len(result[0]) == result[1]




