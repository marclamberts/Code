#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:56:26 2021

@author: lamberts_888
"""
from selenium import webdriver 
import time 
from bs4 import BeautifulSoup
import pandas as pd
import os; import sys;
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import time
import json
from tqdm import tqdm

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path = "/Users/lamberts_888/Desktop/chromedriver", options=options)

# subf='SA\\'
urllist = ['https://www.whoscored.com/Matches/1492274/Live/Spain-LaLiga-2020-2021-Real-Sociedad-Barcelona']
# filename = 'LL200910.csv'
# if filename[:3]=='EPL':
season_id = 2020  #int(filename[3:7])
competition_id = 1
subf=str(competition_id)+'-'+str(season_id)
subf


#Options
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.headless=True
# folder = subf+'\\'

folder = '/Users/lamberts_888/Desktop/'+subf+'\\'  #'D:\\'+filename[3:9]+'\\'+subf+'\\'
folder

urls = urllist

len(list(set(urls)))

def check_exists_by_xpath():
    try:
        driver.find_element_by_xpath("//script[contains(.,'matchCentreData')]")
    except NoSuchElementException:
        return False
    return True


driver = webdriver.Chrome() 
for i in tqdm(range(len(urls)),desc='Reading Games'):
    website_URL = urls[i]
    if((i!=0)&(i%10==0)):
        time.sleep(30)
    driver.get(website_URL)
    if check_exists_by_xpath():
        matchdict = driver.execute_script("return matchCentreData;")
        matchdict['id'] = driver.execute_script("return matchId;")
        matchdict['season_id'] = season_id
        matchdict['competition_id'] = competition_id
        with open("/Users/lamberts_888/Desktop/chromedriver"+str(matchdict['id'])+'.json', 'w') as fp:
            json.dump(matchdict, fp, sort_keys=True, indent=4)