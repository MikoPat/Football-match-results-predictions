from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd 
import re

from elo import getElo
from replacments import get_replacement


def team_data(lista, nazwa, data_for_dataframe):

    pattern = r'data-stat="([^"]+)">([^<]+)'

    matches = re.findall(pattern, lista)

    for match in matches:
        data_type, value = match
        data_for_dataframe[nazwa +data_type] = value


def getMatchDate(page_source):
    date_of_match = re.findall(r'data-venue-date=([^ ]+)', page_source)
    date_of_match = date_of_match[0].replace('"', '')

    return date_of_match


def getMatchTime(page_source):
    game_time = re.findall(r'data-venue-time=([^ ]+)', page_source)
    game_time = game_time[0].replace('"', '')

    return game_time

def getClubsNames(page_source):
    teams = re.findall(r'<h1>.*Match', page_source)
    teams = teams[0].replace(' Match', '')
    teams = teams.replace('<h1>','')

    teams_names = teams.split(" vs. ")

    return teams_names


def getData(page_source):

    data_for_dataframe = {}

    data = re.findall("<tfoot>.*<\/tfoot>", page_source)

    home_team = data[0:6]
    away_team = data[6:12]


    home_team_summary = home_team[0]
    home_team_passes = home_team[1]
    home_team_pass_type = home_team[2]
    home_team_defensive = home_team[3]
    home_team_possesion = home_team[4]
    home_team_miscellaneous = home_team[5]

    away_team_summary = away_team[0]
    away_team_passes = away_team[1]
    away_team_pass_type = away_team[2]
    away_team_defensive = away_team[3]
    away_team_possesion = away_team[4]
    away_team_miscellaneous = away_team[5]

    team_data(home_team_summary, 'home_team_summary_', data_for_dataframe)
    team_data(home_team_passes, 'home_team_passes_', data_for_dataframe)
    team_data(home_team_pass_type, 'home_team_pass_type_', data_for_dataframe)
    team_data(home_team_defensive, 'home_team_defensive_', data_for_dataframe)
    team_data(home_team_possesion, 'home_team_possesion_', data_for_dataframe)
    team_data(home_team_miscellaneous, 'home_team_miscellaneous_', data_for_dataframe)

    team_data(away_team_summary, 'away_team_summary_', data_for_dataframe)
    team_data(away_team_passes, 'away_team_passes_', data_for_dataframe)
    team_data(away_team_pass_type, 'away_team_pass_type_', data_for_dataframe)
    team_data(away_team_defensive, 'away_team_defensive_', data_for_dataframe)
    team_data(away_team_possesion, 'away_team_possesion_', data_for_dataframe)
    team_data(away_team_miscellaneous, 'away_team_miscellaneous_', data_for_dataframe)

    df = pd.DataFrame.from_dict(data_for_dataframe, orient ='index')

    df = df.T

    df['game_date'] = getMatchDate(page_source)
    df['game_time'] = getMatchTime(page_source)

    teams_names = getClubsNames(page_source)

    df['home_team'] = teams_names[0]
    df['away_team'] = teams_names[1]

    return df


def getDataFromPage(url):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(options=op)
    driver.get(url)

    page_source = driver.page_source

    driver.quit()

    return page_source




def eloData(df):

    home_team = df['home_team'][0]
    away_team = df['away_team'][0]

    home_team_name_for_elo = get_replacement(home_team).lower().replace(" ", "")
    away_team_name_for_elo = get_replacement(away_team).lower().replace(" ", "")

    df['elo_home_team'] = getElo(get_replacement(home_team_name_for_elo), str(df['game_date'][0]))
    df['elo_away_team'] = getElo(get_replacement(away_team_name_for_elo), str(df['game_date'][0]))

    return df


def singleMatchData(url):

    data = getDataFromPage(url)
    dataframe = getData(data)

    dataframe_with_elo = eloData(dataframe)

    return dataframe_with_elo
    

