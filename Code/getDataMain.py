
import pandas as pd
from prepareData import *
from replacments import *

from mongo import getDataFromMongo

def getDataToLearning():

    number_of_games_5 = 5
    number_of_games_3 = 3

    df = getDataFromMongo()
    df = getColumns(df)
    df = cleaningData(df)

    df['home_team'] = df['home_team'].apply(get_replacement)
    df['away_team'] = df['away_team'].apply(get_replacement)

    final_data = pd.DataFrame()

    for index, row in df.iterrows():

        game_data = row['game_date']

        home_team_name = row['home_team']
        home_elo_value = row['home_team_elo']

        away_team_name = row['away_team']
        away_elo_value = row['away_team_elo']
        

        #home
        home_team_games_n = getLastNGames(df, home_team_name, game_data, number_of_games_5)
        home_team_games_n_data = getSearchOpponentData(home_team_games_n, home_team_name)
        home_team_games_n_data.columns = ['home_team_last_5_' + str(col) for col in home_team_games_n_data.columns]

        home_team_games_3 = getLastThreeGamesSame(df, home_team_name, game_data, number_of_games_3, home_elo_value)
        home_team_games_3_data = getSearchOpponentData(home_team_games_3, home_team_name)
        home_team_games_3_data.columns = ['home_team_last_3_' + str(col) for col in home_team_games_3_data.columns]

        home_result = pd.concat([home_team_games_n_data, home_team_games_3_data], axis=1)

        #away
        away_team_games_n = getLastNGames(df, away_team_name, game_data, number_of_games_5)
        away_team_games_n_data = getSearchOpponentData(away_team_games_n, away_team_name)
        away_team_games_n_data.columns = ['away_team_last_5_' + str(col) for col in away_team_games_n_data.columns]
        
        away_team_games_3 = getLastThreeGamesSame(df, away_team_name, game_data, number_of_games_3, away_elo_value)
        away_team_games_3_data = getSearchOpponentData(away_team_games_3, away_team_name)
        away_team_games_3_data.columns = ['away_team_last_3_' + str(col) for col in away_team_games_3_data.columns]


        result = pd.DataFrame()

        #określnie wyniku meczu
        if row['home_team_summary_goals'] > row['away_team_summary_goals']:
            result.at[index, 'result'] = 3
        elif row['home_team_summary_goals'] == row['away_team_summary_goals']:
            result.at[index, 'result'] = 1
        elif row['home_team_summary_goals'] < row['away_team_summary_goals']:
            result.at[index, 'result'] = 0
        else:
            result.at[index, 'result'] = 0

        fianl_data_rows = pd.concat([home_team_games_n_data.reset_index(drop=True), 
                                home_team_games_3_data.reset_index(drop=True), 
                                away_team_games_n_data.reset_index(drop=True), 
                                away_team_games_3_data.reset_index(drop=True), 
                                result.reset_index(drop=True)], axis=1)

        final_data = final_data.append(fianl_data_rows, ignore_index=True)

        #display(fianl_data)


    #czyszczenie 
    final_data = final_data.dropna()

    final_data.to_csv('../Data/fianl_data_for_neural_network.csv', sep='\t', encoding='utf-8')

    return "Yeee"
    
print(getDataToLearning())