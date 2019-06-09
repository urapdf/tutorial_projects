"""
initial project idea from:
https://www.analyticsvidhya.com/blog/2019/05/scraping-classifying-youtube-video-data-python-selenium/

"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#variable
my_site = "https://www.youtube.com/results?search_query=moloko&sp=EgIQAQ%253D%253D"

#Test code
driver = webdriver.Chrome()
driver.get(my_site)







