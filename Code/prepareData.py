
import pandas as pd

def cleaningData(df): 
    # czyszczenie danych
    df.columns = df.columns.str.replace("elo_home_team", "home_team_elo")
    df.columns = df.columns.str.replace("elo_away_team", "away_team_elo")

    df = df.drop_duplicates(subset=df.columns.difference(["_id"'home_team_elo', 'away_team_elo']), keep='first')
    columns_to_exclude = ["_id","game_date", "game_time", "home_team", "away_team"]
    df = df.apply(lambda col: pd.to_numeric(col, errors='coerce') if col.name not in columns_to_exclude else col)

    df = df[(df['home_team_elo'] > 0) & (df['away_team_elo'] > 0)]
    df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')

    return df

def getColumns(df):

    df = df[["_id",
    "home_team_summary_goals",
    "home_team_summary_shots",
    "home_team_summary_shots_on_target",
    "home_team_summary_xg",
    "home_team_summary_npxg",
    "home_team_summary_xg_assist",
    "home_team_summary_sca",
    "home_team_summary_gca",
    "home_team_passes_xg_assist",
    "home_team_passes_passes_into_final_third",
    "home_team_passes_passes_into_penalty_area",
    "home_team_passes_crosses_into_penalty_area",
    "home_team_possesion_touches_att_3rd",
    "home_team_possesion_touches_att_pen_area",
    "home_team_defensive_tackles_def_3rd",
    "home_team_defensive_tackles_mid_3rd",
    "home_team_defensive_blocked_shots",
    "home_team_defensive_errors",
    "home_team_miscellaneous_ball_recoveries",
    "away_team_summary_goals",
    "away_team_summary_shots",
    "away_team_summary_shots_on_target",
    "away_team_summary_xg",
    "away_team_summary_npxg",
    "away_team_summary_xg_assist",
    "away_team_summary_sca",
    "away_team_summary_gca",
    "away_team_passes_xg_assist",
    "away_team_passes_passes_into_final_third",
    "away_team_passes_passes_into_penalty_area",
    "away_team_passes_crosses_into_penalty_area",
    "away_team_possesion_touches_att_3rd",
    "away_team_possesion_touches_att_pen_area",
    "away_team_defensive_tackles_def_3rd",
    "away_team_defensive_tackles_mid_3rd",
    "away_team_defensive_blocked_shots",
    "away_team_defensive_errors",
    "away_team_miscellaneous_ball_recoveries",
    "game_date",
    "game_time",
    "home_team",
    "away_team",
    "elo_home_team",
    "elo_away_team"]]

    return df



def getLastNGames(df, club_name, game_data, number_of_games):
    club_data = df[(df['home_team'] == club_name) | (df['away_team'] == club_name)]
    club_data = club_data[club_data['game_date'] < game_data]
    sorted_df = club_data.sort_values(by='game_date', ascending=False)

    last_games = sorted_df.head(number_of_games).copy()

    return last_games


def getLastThreeGamesSame(df, club_name, game_data, numebr_of_games, elo_value):
    club_data = df[(df['home_team'] == club_name) | (df['away_team'] == club_name)]
    club_data = club_data[club_data['game_date'] < game_data]
    sorted_df = club_data.sort_values(by='game_date', ascending=False)

    last_games = sorted_df.head(15).copy()

    last_games['elo_rival'] = 0

    for index, row in last_games.iterrows():
        if row['home_team'] == club_name:
            last_games.at[index, 'elo_rival'] = row['away_team_elo']
        else:
            last_games.at[index, 'elo_rival'] = row['home_team_elo']

    closest_rows = last_games.iloc[(last_games['elo_rival'] - elo_value).abs().argsort()[:numebr_of_games]]
    closest_rows = closest_rows.drop(['elo_rival'], axis=1)

    return closest_rows


def getSearchOpponentData(last_games, club_name):

    team_df = pd.DataFrame()

    for index, row in last_games.iterrows():
        if row['home_team'] == club_name:
            # Create a dictionary dynamically for each column
            team_data = {}
            for col in last_games.keys():
                if col.startswith('home_team'):
                    team_data[col.replace('home_team', 'search_team')] = row[col]
                elif col.startswith('away_team'):
                    team_data[col.replace('away_team', 'opponent_team')] = row[col]
                else:
                    team_data[col] = row[col]


            team_df = team_df.append(team_data, ignore_index=True)

        else:
            team_data = {}
            for col in last_games.keys():
                if col.startswith('away_team'):
                    team_data[col.replace('away_team', 'search_team')] = row[col]
                elif col.startswith('home_team'):
                    team_data[col.replace('home_team', 'opponent_team')] = row[col]
                else:
                    team_data[col] = row[col]

            team_df = team_df.append(team_data, ignore_index=True)

    for index, row in team_df.iterrows():
        # wyliczenie 
        team_df.at[index, 'rival_difference_elo'] = row['search_team_elo'] - row['opponent_team_elo']

        #określnie wyniku meczu
        if row['search_team_summary_goals'] > row['opponent_team_summary_goals']:
            team_df.at[index, 'result'] = 3
        elif row['search_team_summary_goals'] == row['opponent_team_summary_goals']:
            team_df.at[index, 'result'] = 1
        elif row['search_team_summary_goals'] < row['opponent_team_summary_goals']:
            team_df.at[index, 'result'] = 0
        else:
            team_df.at[index, 'result'] = 0

    av_team_df = team_df.mean(axis=0)
    df_avg_data = av_team_df.to_frame().T
    
    return df_avg_data
