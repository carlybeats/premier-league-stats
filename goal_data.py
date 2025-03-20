import json
import os
from utils.goal_utils import retrieve_goal_data


def write_to_json_file():
    goals_data = retrieve_goal_data()
    if os.environ.get("TESTING") != 'True':
        with open('data/goals.json', 'w') as f:
            json.dump(goals_data, f, indent=4)
    return json.dumps(goals_data)

write_to_json_file()

