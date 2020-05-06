from Parser import Parser
from Locators import Locators
from puzzle import PUZZLE
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
    element=WebDriverWait(chrome,11).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.MAIN_LOCATOR)) )
    print("page is ready")
except TimeoutException:
    print("Page loading took too much")

parser=Parser(chrome)

my_puzzle=PUZZLE(parser.extract_info)
print("***********THIS IS __str__**************")
print(my_puzzle)
print("")
print("***********THIS IS __repr__*************")
print([my_puzzle]
)