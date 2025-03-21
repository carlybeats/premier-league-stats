from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from bs4 import BeautifulSoup


service = Service("/snap/bin/firefox.geckodriver")
options = webdriver.FirefoxOptions()
options.add_argument('-headless')


driver = webdriver.Firefox(service=service, options=options)

def retrieve_goal_data():
    driver.get("https://www.premierleague.com/stats/top/players/goals")
    time.sleep(2) 
    print(driver.page_source)
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        time.sleep(2) 
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

        try:
            next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "paginationBtn paginationNextContainer"))
        )
            next_button.click()  # Wait for new data to load
        except:
            print("button not found")
            break  # Exit if no 'Next' button is found

    #
    return player_info


# /html/body/main/div[2]/div[1]/div[1]/table/tbody