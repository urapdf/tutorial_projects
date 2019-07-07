"""
initial project idea from:
https://www.analyticsvidhya.com/blog/2019/05/scraping-classifying-youtube-video-data-python-selenium/

"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


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
    for i in user_data: #  fetch the “href” attribute of the anchor tag we searched for

        links.append(i.get_attribute('href'))

        # fetch the “href” attribute of the anchor tag we searched for
        df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])
        wait = WebDriverWait(driver,10)
        v_category = kat



    for x in links[1:]: # scrape the video details from YouTube.
        driver.get(x)
        wait = WebDriverWait(driver, 10)
        v_id = x.strip('https://www.youtube.com/watch?v=')



        v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text
        print (v_title)
        v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#description yt-formatted-string"))).text
        #print(v_description)


        df.loc[len(df)] = [v_id, v_title, v_description, v_category]

    print (df)
    my_frames.append(df)
    uber_df = pd.concat(my_frames)
    #print(uber_df)

#Cleaning the Scraped Data using the NLTK Library
#store all the columns separately so that we can perform different operations quickly and easily

df_link = pd.DataFrame(columns = ["link"])
df_title = pd.DataFrame(columns = ["title"])
#print ( 1,df_title )
df_description = pd.DataFrame(columns = ["description"])
df_category = pd.DataFrame(columns = ["category"])
df_link["link"] = uber_df['link']
df_title ["title"]= uber_df['title']
#print(2,df_title )
df_description["description"] = uber_df['description']
df_category["category"] = uber_df['category']

# data cleaning title
corpus = []
for i in uber_df.index:
    print (uber_df.shape[0]-1)
    #print(df_title['title'])
    review = re.sub('[^a-zA-Z]', ' ', str(df_title['title'][i]))
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# data cleaning description
corpus1 = []
for i in range(0, uber_df.shape[0]-1):
  review = re.sub('[^a-zA-Z]', ' ', df_description['description'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus1.append(review)

driver.quit()









