import pandas as pd
import os


def retrieve_filepath():
    script_dir = os.path.dirname(__file__)
    root_dir = os.path.dirname(script_dir)
    #print(root_dir)
    if os.environ.get("TESTING") != 'True':
        filepath = os.path.join(root_dir, "data/goals.json")
    else:
        filepath = os.path.join(root_dir, "tests/test_goals.json")
    return filepath

def base_dataframe():
    filepath = retrieve_filepath()
    df = pd.read_json(filepath)
    return df

#base_dataframe()