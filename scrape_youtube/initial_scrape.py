"""
initial project idea from:
https://www.analyticsvidhya.com/blog/2019/05/scraping-classifying-youtube-video-data-python-selenium/

"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#variables
youtube_test_site = "https://www.youtube.com/results?search_query=moloko&sp=EgIQAQ%253D%253D"
travel_search_string = "https://www.youtube.com/results?search_query=Travel&sp=EgIQAQ%253D%253D"

#Test code
driver = webdriver.Chrome()
driver.get(travel_search_string)


user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))

print(len(links))








