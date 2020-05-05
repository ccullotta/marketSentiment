from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
import datetime
import pickle
import time
class Googler:
    def __init__(self, start):
        date = start.split('/')
        self.inputStart = datetime.datetime(int(date[2]),int(date[0]),int(date[1]))
        self.driver = webdriver.Chrome()
        # self.day = datetime.timedelta(days=1)

    def initializeDate(self):
        # open up webpage and navifate shit 
        self.driver.get("https://www.google.com/search?q=bitcoin&sxsrf=ALeKk012Is_PiC_ZtFubsEEa3UEW9qjCYQ:1588696355719&source=lnms&tbm=nws&sa=X&ved=2ahUKEwir0cCPk53pAhWFK80KHbPWAQYQ_AUoAXoECB4QAw&biw=1920&bih=1008")
        # WebDriverWait(self.driver,5).until(cond.element_to_be_clickable((By.LINK_TEXT, 'News')))
        # self.driver.find_element_by_link_text("News").click() #get us into the news section
        WebDriverWait(self.driver,5).until(cond.presence_of_element_located((By.LINK_TEXT, 'Tools')))
        self.driver.find_element_by_link_text("Tools").click() #search tools 
        WebDriverWait(self.driver,5).until(cond.visibility_of_element_located((By.XPATH, '//div[@aria-label="Recent"]')))
        WebDriverWait(self.driver,5).until(cond.visibility_of_element_located((By.XPATH, '//div[@class="hdtb-mitem hdtb-msel hdtb-imb"]')))
        time.sleep(0.2)
        self.driver.find_element_by_xpath('//div[@class="hdtbna notl"]/div[@class="hdtb-td-o"]/div[@class="hdtb-mn-cont"]/div[@aria-label="Recent"]').click()
        WebDriverWait(self.driver,5).until(cond.presence_of_element_located((By.ID, 'cdr_opt')))
        self.driver.find_element_by_xpath('//div[@jscontroller="Uuupec"]').click()

        startDate = self.driver.find_element_by_xpath('//input[@class="OouJcb ktf mini"]')
        endDate = self.driver.find_element_by_xpath('//input[@class="rzG2be ktf mini"]')

        startDate.send_keys(str(self.inputStart))
        endDate.send_keys(str(self.inputStart+datetime.timedelta(days=1)))
        self.driver.find_element_by_xpath('//input[@value="Go"]').click()
    
    def returnLinks(self):
        links = []
        raw = self.driver.find_elements_by_xpath('//div[@class="dbsr"]/a')
        for a in raw:
            links.append(a.get_attribute('href'))
        # print(links)
        links.append(str(self.inputStart))
        # self.driver.get("https://www.google.com/search?q=bitcoin&oq=bitcoin&aqs=chrome..69i57j35i39j0l6.1184j1j8&sourceid=chrome&ie=UTF-8")
        return links


    def returnAllNewsFromStart(self):
        linksPerDay = []
        while self.inputStart < datetime.datetime.today():
            self.initializeDate()
            linksPerDay.append(self.returnLinks())
            self.inputStart = self.inputStart + datetime.timedelta(days=1)
        return linksPerDay

# date = datetime.datetime(2016, 7, 24)
# date1 = datetime.datetime.today()
# delta = datetime.timedelta(days=1)
# print(date)
# print(date1)
# date = date1 - delta
# if date < date1:
#     print("olddate")
# print((date+delta))


testG = Googler("2/3/2020")
# testG.initializeDate()
list = testG.returnAllNewsFromStart()
# for a in list:
#     print(a)

# with open("urls.dat", 'rb') as f:
#     list = pickle.load(f)
#     print(list)
# #     pickle.dump(list, f)