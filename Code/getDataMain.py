
import pandas as pd
from prepareData import *
from replacments import *

from mongo import getDataFromMongo

def getDataToLearning():

    number_of_games_5 = 5
    number_of_games_3 = 3
    final_data = pd.DataFrame()


    df = getDataFromMongo()
    df = getColumns(df)
    df = cleaningData(df)

    df['home_team'] = df['home_team'].apply(get_replacement)
    df['away_team'] = df['away_team'].apply(get_replacement)



    # tu zaczynamy tworzyć data freme do uczenia

    for index, row in df.iterrows():
        #określnie wyniku meczu
        if row['home_team_summary_goals'] > row['away_team_summary_goals']:
            df.at[index, 'result'] = 2
        elif row['home_team_summary_goals'] == row['away_team_summary_goals']:
            df.at[index, 'result'] = 1
        elif row['home_team_summary_goals'] < row['away_team_summary_goals']:
            df.at[index, 'result'] = 0
        else:
            df.at[index, 'result'] = 0



    for index, row in df.iterrows():

        home_team = df['home_team']
        home_team_elo = df['home_team_elo']
        away_team = df['away_team']
        away_team_elo = df['away_team_elo']

        game_date = df['game_date']

        #home team
        home_last_five = getLastNGames(df, home_team, game_date, number_of_games_5)
        home_data_last_five = getSearchOpponentData(home_last_five, home_team)
        home_data_last_five.columns = ['last_5_' + str(col) for col in home_data_last_five.columns]

        home_last_three = getLastThreeGamesSame(df, home_team, game_date, number_of_games_3, home_team_elo)
        home_data_last_three = getSearchOpponentData(home_last_three, home_team)
        home_data_last_three.columns = ['last_3_' + str(col) for col in home_data_last_three.columns]

        home_result = pd.concat([home_data_last_five, home_data_last_three], axis=1).reindex(home_data_last_five.index)

        #away team
        away_last_five = getLastNGames(df, away_team, game_date, number_of_games_5)
        away_data_last_five = getSearchOpponentData(away_last_five, away_team)
        away_data_last_five.columns = ['last_5_' + str(col) for col in away_data_last_five.columns]

        away_last_three = getLastThreeGamesSame(df, away_team, game_date, number_of_games_3, away_team_elo)
        away_data_last_three = getSearchOpponentData(away_last_three, away_team)
        away_data_last_three.columns = ['last_3_' + str(col) for col in away_data_last_three.columns]

        away_result = pd.concat([away_data_last_five, away_data_last_three], axis=1).reindex(away_data_last_five.index)

        result = pd.concat([home_result, away_result], axis=1).reindex(home_result.index)

        result['home_team_elo'] = df['home_team_elo']

        result['away_team_elo'] = df['away_team_elo']

        final_data = final_data.append(result)

    return final_data

print(getDataToLearning())