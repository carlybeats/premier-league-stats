import json
import os
from utils.goal_utils import scrape_goal_data

script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file path relative to the script's directory


def write_to_json_file():
    goals_data = scrape_goal_data()
    if os.environ.get("TESTING") != 'True':
        filepath = os.path.join(script_dir, "data/goals.json")
        with open(filepath, 'w') as f:
            json.dump(goals_data[0], f, indent=4)
    else:
        filepath = os.path.join(script_dir, "tests/test_goals.json")
        with open(filepath, 'w') as f:
            json.dump(goals_data, f, indent=4)

    return "Write to JSON file successful!"



if __name__ == "__main__":
    write_to_json_file()