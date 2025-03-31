import pandas as pd
import os

root_dir = os.path.dirname(os.path.dirname(__file__))

def retrieve_filepath():
    #print(root_dir)
    if os.environ.get("TESTING") != 'True':
        filepath = os.path.join(root_dir, "data/goals.json")
    else:
        filepath = os.path.join(root_dir, "tests/test_goals.json")
    return filepath

def base_dataframe():
    filepath = retrieve_filepath()
    df = pd.read_json(filepath)
    # missing_rows = df[df.team.isnull()]
    # print(missing_rows)
    # Assigning beto a team
    df.loc[df['name'] == 'Beto', 'team'] = 'Everton'
    df.dropna(inplace=True)
    return df

def store_to_csv():
    df = base_dataframe()
    filepath = os.path.join(root_dir, "data/goals.csv")
    df.to_csv(filepath, index=False)  

if __name__ == '__main__':
    store_to_csv()