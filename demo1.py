from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd


PATH = "C:\Program Files\Drivers\chromedriver.exe"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)

Name = []
Type = []
Start = []
Duration = []
End = []
Rating = []
Cost = []
Seats_avail = []

driver.get('https://www.redbus.in/bus-tickets/kozhikode-to-ernakulam?fromCityId=74661&toCityId=216&fromCityName=Kozhikode&toCityName=Ernakulam&busType=Any&srcCountry=IND&destCountry=IND&onward=20-Jan-2025')

time.sleep(10)

# driver.find_element(By.XPATH,"//a[@class='route']").click()

all_items = driver.find_elements(By.XPATH,"//li[@class='row-sec clearfix']")

for item in all_items:
        try:
            busname = item.find_element(By.XPATH,".//div[@class ='travels lh-24 f-bold d-color']").text
            Name.append(busname)
        except NoSuchElementException:
            Name.append("NA")
        
        try:
            bustype = item.find_element(By.XPATH, ".//div[@class ='bus-type f-12 m-top-16 l-color evBus']").text
            Type.append(bustype)
        except NoSuchElementException:
            Type.append("NA")
        

        try:
            busdeparturetime = item.find_element(By.XPATH,".//div[@class ='dp-time f-19 d-color f-bold']").text
            Start.append(busdeparturetime)
        except NoSuchElementException:
            Start.append("NA")               

        try:
            busduration = item.find_element(By.XPATH,".//div[@class ='dur l-color lh-24']").text
            Duration.append(busduration)
        except NoSuchElementException:
            Duration.append("NA")
        

        try:
            busarraivaltime = item.find_element(By.XPATH,".//div[@class ='bp-time f-19 d-color disp-Inline']").text
            End.append(busarraivaltime)
        except NoSuchElementException:
            End.append("NA")
        

        try:
            busrating = item.find_element(By.XPATH, ".//span[@class='']").text
            Rating.append(busrating)
        except NoSuchElementException:
            Rating.append("NA")
    
        try:
            busprice = item.find_element(By.XPATH, ".//span[@class ='f-19 f-bold']").text
            Cost.append(busprice)
        except NoSuchElementException:
            Cost.append("0")
        
        try:
            busseats = item.find_element(By.XPATH,"//div[@class ='seat-left m-top-30']").text
            Seats_avail.append(busseats)
        except NoSuchElementException:
            Seats_avail.append("0")

# df = pd.DataFrame(zip(Name,Type,Start,Duration,End,Rating,Cost,Seats_avail),columns=["Name","Type","Start","Duration","End","Rating","Cost","Seats_avail"])

print(Cost)