
from singleMatch import singleMatchData
from mongo import uploadMongo




def parseData(dane):
    dict_to_mongo = dane.to_dict('records')
    dict_to_mongo = dict_to_mongo[0]

    return dict_to_mongo


def main():

    url = 'https://fbref.com/en/matches/3a6836b4/Burnley-Manchester-City-August-11-2023-Premier-League'

    urls = ['https://fbref.com/en/matches/3a6836b4/Burnley-Manchester-City-August-11-2023-Premier-League',
    'https://fbref.com/en/matches/d8f8f8ad/Arsenal-Fulham-August-26-2023-Premier-League']


    for url in urls:
        data = singleMatchData(url)
        dict_to_mongo = parseData(data)

        uploadMongo(dict_to_mongo)


if __name__ == '__main__':
    main()