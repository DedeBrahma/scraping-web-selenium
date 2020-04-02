##############################################################
'''
    Auto scraping Youtube Comment with python and selenium
    This code will be running of chrome browser
    Then we try to get data list of comment in Youtube

    ~ Dede Brahma Arianto ~
'''
##############################################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import csv


# -------------- LOAD DRIVER AND URL --------------------
driver = webdriver.Chrome("chromedriver.exe")   # ChromeDriver in folder project
driver.get("https://www.youtube.com/watch?v=Bs6aRHCfFYI")   # Youtube URL
time.sleep(2)


# --------------- FETCH TITLE ---------------------------
title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
print(title)


# --------------- LOAD HTML ELEMENT ---------------------
SCROLL_PAUSE_TIME = 2
CYCLES = 20
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(SCROLL_PAUSE_TIME * 3)
for i in range(CYCLES):
    html.send_keys(Keys.END)
    time.sleep(SCROLL_PAUSE_TIME)


# --------------- GETTING THE COMMENT TEXTS ---------------
name_elems=driver.find_elements_by_xpath('//*[@id="author-text"]')
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
num_of_names = len(name_elems)



# --------------- WRITING TO OUTPUT FILE ---------------
file_name = 'data_comment.csv'  # File Name Data
with open(file_name, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Username', 'Comment'])
    for i in range(num_of_names):
        name = name_elems[i].text
        text = comment_elems[i].text
        text = str(text).replace('\n', '')
        writer.writerow([name, text])

driver.close()