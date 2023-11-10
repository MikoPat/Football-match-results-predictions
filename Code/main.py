
from singleMatch import singleMatchData
from mongo import uploadMongo
from matchesLinks import matchesLinks




def parseData(dane):
    dict_to_mongo = dane.to_dict('records')
    dict_to_mongo = dict_to_mongo[0]

    return dict_to_mongo


def main():


    main_urls = ['https://fbref.com/en/comps/9/2018-2019/schedule/2018-2019-Premier-League-Scores-and-Fixtures',
                 'https://fbref.com/en/comps/9/2017-2018/schedule/2017-2018-Premier-League-Scores-and-Fixtures']
    
    for main_url in main_urls:
        print(main_url)

        urls = matchesLinks(main_url)

        for url in urls:
            data = singleMatchData(url)
            dict_to_mongo = parseData(data)

            uploadMongo(dict_to_mongo)



if __name__ == '__main__':
    main()


#TODO: uzupełnic mecz https://fbref.com/en/matches/e7e969e9/Brentford-Manchester-City-May-28-2023-Premier-League
# 