from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import re


service = Service("/snap/bin/firefox.geckodriver")
options = webdriver.FirefoxOptions()
options.add_argument('-headless')


driver = webdriver.Firefox(service=service, options=options)

def scrape_goal_data():
    start = time.time()
    driver.get("https://www.premierleague.com/stats/top/players/goals")
    time.sleep(1) 
    player_info = []
    print("Starting extraction of data...")
    try:
    # Wait for the "Accept All Cookies" button and click it
            accept_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_button.click()
    except Exception:
        print("No cookie pop-up found, continuing...")

    try:
    # Wait for the "Close Advert" button and click it
        close_ad_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "advertClose"))
        )
        close_ad_button.click()
    except Exception:
        print("No ad found, continuing...")
    while True:
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('tbody', class_= 'stats-table__container')
        table_elements = table.find_all('tr')
        for player in table_elements:
            rank = int(player.find('td', class_='stats-table__rank').text.strip("."))
            name = player.find('a', class_='playerName').text.strip()
            try:
                team = player.find('a', class_='stats-table__cell-icon-align').text.strip()
            except:
                team = None
            nationality = player.find('div', class_='stats-table__cell-icon-align').text.strip()
            goals = int(player.find('td', class_='stats-table__main-stat').text.strip())
            player_info.append({'rank':rank, 'name':name, 'team':team, 'nationality':nationality, 'goals_scored':goals})
        try:
        #Pressing the 'next' button to access the next batch of 10 rows in the table
            next_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME,'paginationNextContainer:not(.inactive)')))
            next_button.click()
        except:
            break  
    end = time.time()
    time_taken = end - start
    
    # The number stored in data-num-entries on HTML is retrieved with this block of code
    # The number represents how many rows there are in the table
    # The length of the player_info table should match with this number, if not there is a problem somewhere
    wrapper = soup.find('div', class_="wrapper col-12")
    data_num_entries = str(wrapper.contents[1])[50:75]
    driver.quit()
    expected_num_of_players = get_num_of_players_in_table(data_num_entries)
    actual_num_of_extracted_players = len(player_info)
    print(f"Expected: {expected_num_of_players}. Actual: {actual_num_of_extracted_players}")
    if expected_num_of_players == actual_num_of_extracted_players:
        print(f"Extraction complete! {actual_num_of_extracted_players} players extracted from Premier League Goals Stats")
        print(f"Extraction took {time_taken:.2f} seconds")
    else:
        raise Exception("Erroneous amount of players extracted. Please run program again")

    return player_info, expected_num_of_players

def get_num_of_players_in_table(data_num_entries):
    pattern = re.compile(r'\d+')
    results = re.findall(pattern, data_num_entries)
    expected_num_of_extracted_players = int(results[0])
    return expected_num_of_extracted_players


