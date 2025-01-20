from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


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
    busname = item.find_elements(By.XPATH,".//div[@class ='travels lh-24 f-bold d-color']")
    for name in busname:
       Name.append(name.text)
       
    bustype = item.find_elements(By.XPATH,".//div[@class ='bus-type f-12 m-top-16 l-color evBus']")
    for type in busname:
       Type.append(type.text)


    departing = item.find_elements(By.XPATH,".//div[@class ='dp-time f-19 d-color f-bold']")
    for name in departing:
       Start.append(name.text)   

    duration = item.find_elements(By.XPATH,".//div[@class ='dur l-color lh-24']")
    for name in duration:
       Duration.append(name.text)  
   
    arrival = item.find_elements(By.XPATH,".//div[@class ='bp-time f-19 d-color disp-Inline']")
    for arr in arrival:
       End.append(arr.text)
    
    try:
       if len(item.find_elements(By.XPATH,".//span[@class='']")) > 0:
        rating = item.find_elements(By.XPATH,".//span[@class='']")
       for rate in rating:
          Rating.append(rate.text)
       else:
          Rating.append("NA")
    except:
       pass      
          

    prices = item.find_elements(By.XPATH,".//div[@class ='f-19 f-bold']")
    for price in prices:
       Cost.append[price.text]
 
    try:
       if len(item.find_element(By.XPATH,"//div[@class ='seat-left m-top-30']")) > 0:
        seats_avail = item.find_element(By.XPATH,"//div[@class ='seat-left m-top-30']")
       for seat in seats_avail:
          Seats_avail.append(seat.text)
       else:
          Seats_avail.append("0")
    except:
       pass      
    
    
print(Name)






