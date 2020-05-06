from Parser import Parser
from Numbers_Draw import Nums

import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


os.chdir('utils')
chrome_driver_path=os.getcwd()
os.chdir('..')

chrome=webdriver.Chrome(executable_path=chrome_driver_path+"/chromedriver")
chrome.get("https://sudoku.com/")


try:
    element=WebDriverWait(chrome,5).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR,'td.game-cell')) )
    print("page is ready")
except TimeoutException:
    print("Page loading took too much")

parser=Parser(chrome)

print(parser.extract_info)
