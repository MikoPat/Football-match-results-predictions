
from singleMatch import singleMatchData
from mongo import uploadMongo
from matchesLinks import matchesLinks
from prepareData import *
from replacments import *

from mongo import getDataFromMongo



def parseData(dane):
    dict_to_mongo = dane.to_dict('records')
    dict_to_mongo = dict_to_mongo[0]

    return dict_to_mongo





def main():

    main_urls = ['https://fbref.com/en/comps/9/2020-2021/schedule/2020-2021-Premier-League-Scores-and-Fixtures',
                'https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures']
    
    for main_url in main_urls:

        print(main_url)

        if main_url in {'https://fbref.com/en/matches/c34bbc21/Bochum-Monchengladbach-March-18-2022-Bundesliga'}:
            continue
        else:
            urls = matchesLinks(main_url)

            for url in urls:
                data = singleMatchData(url)
                dict_to_mongo = parseData(data)

                uploadMongo(dict_to_mongo)



if __name__ == '__main__':
    main()

