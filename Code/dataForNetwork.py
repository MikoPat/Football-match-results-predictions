import pandas as pd

italy = pd.read_csv('../Data/fianl_data_for_neural_network_italy.csv', sep='\t')
spain = pd.read_csv('../Data/fianl_data_for_neural_network_spain.csv', sep='\t')
france = pd.read_csv('../Data/fianl_data_for_neural_network_france.csv', sep='\t')
germany = pd.read_csv('../Data/fianl_data_for_neural_network_germany.csv', sep='\t')
england = pd.read_csv('../Data/fianl_data_for_neural_network_england.csv', sep='\t')


# England
england['game_date'] = pd.to_datetime(england['game_date'], errors='coerce')

england.drop(england[(england['game_date'] >= '2022-08-05') & (england['game_date'] < '2022-10-14')].index, inplace = True)
england.drop(england[(england['game_date'] >= '2021-08-13') & (england['game_date'] < '2021-11-05')].index, inplace = True)
england.drop(england[(england['game_date'] >= '2020-09-12') & (england['game_date'] < '2020-12-05')].index, inplace = True)
england.drop(england[(england['game_date'] >= '2019-08-09') & (england['game_date'] < '2019-11-02')].index, inplace = True)
england.drop(england[(england['game_date'] >= '2018-08-10') & (england['game_date'] < '2018-11-03')].index, inplace = True)
england.drop(england[(england['game_date'] >= '2017-08-11') & (england['game_date'] < '2017-11-04')].index, inplace = True)


# Germany
germany['game_date'] = pd.to_datetime(germany['game_date'], errors='coerce')

germany.drop(germany[(germany['game_date'] >= '2022-08-05') & (germany['game_date'] < '2022-10-21')].index, inplace = True)
germany.drop(germany[(germany['game_date'] >= '2021-08-13') & (germany['game_date'] < '2021-11-05')].index, inplace = True)
germany.drop(germany[(germany['game_date'] >= '2020-09-18') & (germany['game_date'] < '2020-12-11')].index, inplace = True)
germany.drop(germany[(germany['game_date'] >= '2019-08-16') & (germany['game_date'] < '2019-11-08')].index, inplace = True)
germany.drop(germany[(germany['game_date'] >= '2018-08-24') & (germany['game_date'] < '2018-11-09')].index, inplace = True)
germany.drop(germany[(germany['game_date'] >= '2017-08-18') & (germany['game_date'] < '2017-11-03')].index, inplace = True)


# France
france['game_date'] = pd.to_datetime(france['game_date'], errors='coerce')

france.drop(france[(france['game_date'] >= '2022-08-05') & (france['game_date'] < '2022-10-14')].index, inplace = True)
france.drop(france[(france['game_date'] >= '2021-08-06') & (france['game_date'] < '2021-10-22')].index, inplace = True)
france.drop(france[(france['game_date'] >= '2020-08-21') & (france['game_date'] < '2020-11-20')].index, inplace = True)
france.drop(france[(france['game_date'] >= '2019-08-09') & (france['game_date'] < '2019-10-25')].index, inplace = True)
france.drop(france[(france['game_date'] >= '2018-08-10') & (france['game_date'] < '2018-10-26')].index, inplace = True)
france.drop(france[(france['game_date'] >= '2017-08-04') & (france['game_date'] < '2017-10-27')].index, inplace = True)


# Spain
spain['game_date'] = pd.to_datetime(spain['game_date'], errors='coerce')

spain.drop(spain[(spain['game_date'] >= '2022-08-12') & (spain['game_date'] < '2022-10-22')].index, inplace = True)
spain.drop(spain[(spain['game_date'] >= '2021-08-13') & (spain['game_date'] < '2021-10-26')].index, inplace = True)
spain.drop(spain[(spain['game_date'] >= '2020-09-12') & (spain['game_date'] < '2020-11-27')].index, inplace = True)
spain.drop(spain[(spain['game_date'] >= '2019-08-16') & (spain['game_date'] < '2019-10-29')].index, inplace = True)
spain.drop(spain[(spain['game_date'] >= '2018-08-17') & (spain['game_date'] < '2018-11-03')].index, inplace = True)
spain.drop(spain[(spain['game_date'] >= '2017-08-18') & (spain['game_date'] < '2017-11-03')].index, inplace = True)


# Italia
italy['game_date'] = pd.to_datetime(italy['game_date'], errors='coerce')

italy.drop(italy[(italy['game_date'] >= '2022-08-13') & (italy['game_date'] < '2022-10-22')].index, inplace = True)
italy.drop(italy[(italy['game_date'] >= '2021-08-21') & (italy['game_date'] < '2021-10-30')].index, inplace = True)
italy.drop(italy[(italy['game_date'] >= '2020-09-19') & (italy['game_date'] < '2020-12-11')].index, inplace = True)
italy.drop(italy[(italy['game_date'] >= '2019-08-24') & (italy['game_date'] < '2019-11-02')].index, inplace = True)
italy.drop(italy[(italy['game_date'] >= '2018-08-18') & (italy['game_date'] < '2018-11-02')].index, inplace = True)
italy.drop(italy[(italy['game_date'] >= '2017-08-19') & (italy['game_date'] < '2017-10-28')].index, inplace = True)


dane = pd.concat([england, germany, france, spain, italy], ignore_index=True, sort=False)

dane = dane.drop('Unnamed: 0', axis=1)

dane.to_csv('../Data/fianl_data_for_neural_network_3.csv', sep='\t', encoding='utf-8')

print('File created')