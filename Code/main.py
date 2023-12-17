
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

    main_urls = ['https://fbref.com/en/comps/20/2017-2018/schedule/2017-2018-Bundesliga-Scores-and-Fixtures']

    for main_url in main_urls:
        print(main_url)
        urls = matchesLinks(main_url)

        for url in urls:
            if url in {'https://fbref.com/en/matches/c34bbc21/Bochum-Monchengladbach-March-18-2022-Bundesliga',
                        'https://fbref.com//en/matches/e0a20cfe/Hellas-Verona-Roma-September-19-2020-Serie-A',
                        'https://fbref.com//en/matches/82c5d82c/Monchengladbach-Bayern-Munich-August-13-2021-Bundesliga',
                        'https://fbref.com//en/matches/51fae469/Stuttgart-Greuther-Furth-August-14-2021-Bundesliga',
                        'https://fbref.com//en/matches/5d7bd7fa/Union-Berlin-Bayer-Leverkusen-August-14-2021-Bundesliga',
                        'https://fbref.com//en/matches/d1f94768/Wolfsburg-Bochum-August-14-2021-Bundesliga',
                        'https://fbref.com//en/matches/5dc40876/Wolfsburg-Holstein-Kiel-May-17-2018-German-12-RelegationPromotion-Play-offs',
                        'https://fbref.com//en/matches/9c6a24db/Holstein-Kiel-Wolfsburg-May-21-2018-German-12-RelegationPromotion-Play-offs'}:
                print(url + ' NO!')
            else:
                print(url)
                data = singleMatchData(url)
                dict_to_mongo = parseData(data)

                uploadMongo(dict_to_mongo)



if __name__ == '__main__':
    main()

