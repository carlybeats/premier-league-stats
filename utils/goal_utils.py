import requests
from bs4 import BeautifulSoup


def retrieve_goal_data():
    data = requests.get("https://www.premierleague.com/stats/top/players/goals")
    soup = BeautifulSoup(data.content, 'html.parser')
    player = soup.find('a', class_='playerName').text.strip()
    team = soup.find('a', class_='stats-table__cell-icon-align').text.strip()
    table = soup.find('tbody', class_= 'stats-table__container')
    table_elements = table.find_all('tr')
    player_info = []
    for player in table_elements:
        name = player.find('a', class_='playerName').text.strip()
        team = player.find('a', class_='stats-table__cell-icon-align').text.strip()
        nationality = player.find('div', class_="stats-table__cell-icon-align").text.strip()
        goals = player.find('td', class_="stats-table__main-stat").text.strip()
        player_info.append({'name':name, 'team':team, 'nationality':nationality, 'goals_scored':int(goals)})
    return player_info