from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


PATH = "C:\Program Files\Drivers\chromedriver.exe"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)

route_details = []
Link = []

driver.get('https://www.redbus.in/online-booking/bihar-state-road-transport-corporation-bsrtc?utm_source=rtchometile%22')
driver.maximize_window()
wait = wait(driver,10)

all_routes =  driver.find_elements(By.XPATH,'//*[@class="DC_117_paginationTable"]')

for route in all_routes:
        try:
            route_name = route.find_element(By.XPATH,'//div[@class="DC_117_pageTabs "]')
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", route_name)
            driver.execute_script("arguments[0].style.border='3px solid red'", route_name) 
            time.sleep(5)
        except NoSuchElementException:
            print("error")

# for i in range(1,11):
        
#         # retrive the route links 
            
#         try:
#             # Wait for the pagination element to be present
#             pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
#             next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
#             time.sleep(4)
#             next_button.click()
            
#         except NoSuchElementException:
            
#             break


    
    
