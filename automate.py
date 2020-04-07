from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
browser.get("https://zzzscore.com/1to50/en/")

dictionary = {}

for i in range(1,51):
    if i in dictionary:
        dictionary[i].click()
        continue
    elements = browser.find_elements_by_xpath("//div/div")
    for element in elements:
        arr = element.get_attribute('innerHTML').split('</span>')
        if(len(arr) == 2 and arr[1].isdigit()):
            if(int(arr[1]) == i):
                element.click()
                break
            else:
                dictionary[int(arr[1])] = element 