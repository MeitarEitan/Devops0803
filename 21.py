from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

my_driver = webdriver.Chrome()

my_driver.get("file://C:/Users/omris/OneDrive/שולחן העבודה/DevOps Course/tip_calc/index.html")
# my_driver.find_element_by_id("billamt").send_keys("100")
bill_amt = my_driver.find_element_by_id("billamt")
bill_amt.send_keys("100")
people_amt = my_driver.find_element_by_id("peopleamt")
people_amt.send_keys("5")
result = my_driver.find_element_by_id("tip").text

select_amp = my_driver.find_element_by_id("serviceQual")
select_amp.send_keys("20% - Good")
music_amp = my_driver.find_element_by_id("music")
music_amp.send_keys("5")
button_amp = my_driver.find_element_by_id("calculate")
button_amp.click()

my_driver.find_element_by_id("billamt").send_keys("100" + Keys.TAB)
if result == "5.00":
    print("test passed!")