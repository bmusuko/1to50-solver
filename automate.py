from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://zzzscore.com/1to50/en/")

dictionary = {}
time.sleep(1)
# initialized
elements = browser.find_elements_by_xpath("//div/div")
for element in elements:
    arr = element.get_attribute('innerHTML').split('</span>')
    if(len(arr) == 2 and arr[1].isdigit()):
        number = int(arr[1]) 
        dictionary[int(arr[1])] = element

time.sleep(1)
for i in range(1,26):
    dictionary[i].click()


elements = browser.find_elements_by_xpath("//div/div")
for element in elements:
    arr = element.get_attribute('innerHTML').split('</span>')
    if(len(arr) == 2 and arr[1].isdigit()):
        number = int(arr[1]) 
        dictionary[int(arr[1])] = element

for i in range(25,51):
    dictionary[i].click()


time.sleep(0.5)
element = browser.find_element_by_xpath("//div/div/strong")
print(element.get_attribute('innerHTML'))
browser.quit()