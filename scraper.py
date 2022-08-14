#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:11:50 2021

@author: lamberts_888
"""

#Imports
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

#Options

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.headless=True


urls = ['https://www.whoscored.com/Matches/1492147/Live/Spain-LaLiga-2020-2021-Real-Madrid-Barcelona']

len(list(set(urls)))

driver = webdriver.Chrome() 
for i in tqdm(range(len(urls)),desc='Reading Games'):   
    website_URL = urls[i]
    if((i!=0)&(i%10==0)):
        time.sleep(30)
    driver.get(website_URL)

    element = driver.find_element_by_xpath('//*[@id="layout-wrapper"]/script[1]')
    script_content = element.get_attribute('innerHTML')

    script_ls = script_content.split(sep="  ")
    script_ls = list(filter(None, script_ls))
    script_ls = [name for name in script_ls if name.strip()]
    dictstring = script_ls[2][17:-2]
    matchdict = json.loads(dictstring)
    matchdict['id'] = script_ls[1][8:-2]
    matchdict['season_id'] = season_id
    matchdict['competition_id'] = competition_id
    with open(folder+str(matchdict['id'])+'.json', 'w') as fp:
        json.dump(matchdict, fp, sort_keys=True, indent=4)
    
    
    