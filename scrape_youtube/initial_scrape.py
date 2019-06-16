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
#driver.get(travel_search_string)

#Loop through all catagories
my_cat = ["Dog","Cat"]
my_frames =[]
for kat in my_cat:
    youtube_test_site = "https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D".format(kat)
    print(youtube_test_site)
    driver.get(youtube_test_site)


    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    #print (user_data)

    links = []
    for i in user_data:

        links.append(i.get_attribute('href'))

        df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])
        wait = WebDriverWait(driver,10)
        v_category = kat



    for x in links[1:]:
        #driver.get(x)
        v_id = x.strip('https://www.youtube.com/watch?v=')
        #v_title = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"h1.title yt-formatted-string")).text
        v_title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text
        v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#description yt-formatted-string"))).text

        df.loc[len(df)] = [v_id, v_title, v_description, v_category]

    my_frames.append(df)
    uber_df = pd.concat(my_frames)
    print(uber_df)









