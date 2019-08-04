from selenium import webdriver
import time


def test_google_launch():

    #driver = webdriver.Chrome()
    driver = webdriver.Safari()
    driver.set_page_load_timeout(10)
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("Automation Step by Step")
    time.sleep(20)
    driver.find_element_by_name("btnK").click()
    time.sleep(20)
    driver.close()

test_google_launch()