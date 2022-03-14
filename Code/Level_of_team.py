import pandas as pd

data = pd.read_csv('./Data/Data_Premier_League_20_21.csv')


#data.columns = ['Rk','Squad','MP','W','D','L','GF','GA','GD','Pts','xG','xGA','xGD','xGD/90']
data_array = data.to_numpy()


# Wybór kolumn do przedstawienia na wykresie
team_data = data_array[0,:]
team_data = team_data[0]

team_data_tabel = team_data.split(";")

name = team_data_tabel[1]
number_of_matches = team_data_tabel[2]
points = team_data_tabel[6]
gols_for = team_data_tabel[7]
gols_against = team_data_tabel[8]
gols_difference = team_data_tabel[9]
xG = team_data_tabel[10]
xGAgainst = team_data_tabel[11]
xGDifference = team_data_tabel[12]
xGDifference_90 = team_data_tabel[13]




print(team_data_tabel)
#print('\n')
print('Nazwa: ' + name)
print('Liczba spotkan: '+number_of_matches)
print('Punkty: '+points)
print('Gole zdobyte: '+gols_for)
print('Gole stracone: '+gols_against)
print('Gole roznica: '+gols_difference)
print('xG: '+xG)
print('xGA: '+xGAgainst)
print('xGD: '+xGDifference)
print('xGD/90: '+xGDifference_90)


