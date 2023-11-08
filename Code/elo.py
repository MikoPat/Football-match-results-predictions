import requests
import datetime
from datetime import datetime
import pandas as pd 
  
from replacments import get_replacement


def noneParser(variable, parseFunc):
    if (variable == 'None' or variable == ''):
        return None
    return parseFunc(variable)

def dateParser(variable):
    try:
        return datetime.datetime.strptime(variable, "%Y-%m-%d")
    except:
        return None

def dataFrame(dataRows):

    data = []

    for row in dataRows[1:]:
        if row == '':
            continue
        columns = row.split(',')
        entry = {}
        entry['rank'] = noneParser(columns[0], int)
        entry['club'] = noneParser(columns[1], str)
        entry['country'] = noneParser(columns[2], str)
        entry['level'] = noneParser(columns[3], int)
        entry['elo'] = noneParser(columns[4], float)
        entry['from'] = noneParser(columns[5], str)
        entry['to'] = noneParser(columns[6], str)
        data.append(entry)

    df = pd.DataFrame(data)

    return df

def get_row(match_date, df):
    #date_to_check = pd.to_datetime('2023-08-11')
    date_to_check = pd.to_datetime(match_date)
    filtered_row = df[(pd.to_datetime(df['from']) <= date_to_check) & (pd.to_datetime(df['to']) >= date_to_check)]

    elo_value = float(filtered_row['elo'])
    
    return elo_value



def getElo(club_name, match_date):

    try:

        replacement_club_name = get_replacement(club_name).lower()

        url_elo = "http://api.clubelo.com/"
        url = url_elo + replacement_club_name

        response = requests.get(url)
        dataRows = response.text.split('\n')
        df = dataFrame(dataRows)
        elo_ranking_vlaue = get_row(match_date, df)

        return str(elo_ranking_vlaue)

    except:
        return str(0.0)


#club_name = "Burnley"
#match_date = '2023-08-11'
#print(getElo(club_name, match_date))
