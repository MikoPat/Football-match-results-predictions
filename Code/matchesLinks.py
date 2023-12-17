from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd 
import re


def getDataFromPage(url):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(options=op)
    driver.get(url)

    page_source = driver.page_source

    driver.quit()

    return page_source

def getData(page_source):
    links_from_table = re.findall(r'data-stat="match_report"><([^<]+)', page_source)

    cleaned_list = [item for item in links_from_table if '/td>' not in item and 'Head-to-Head' not in item]
    cleaned_list_final = ['https://fbref.com/' + item.replace('a href="', '').replace('">Match Report', '') for item in cleaned_list]

    return cleaned_list_final


def matchesLinks(url):

    data = getDataFromPage(url)
    list_of_links = getData(data)

    return list_of_links