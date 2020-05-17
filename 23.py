from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_driver = webdriver.Chrome()
my_driver.get("file://C:/Users/omris/OneDrive/שולחן העבודה/DevOps Course/tip_calc/index.html")

my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("music").send_keys("5")
my_driver.find_element_by_id("calculate").click()
result = my_driver.find_element_by_id("tip").text
if result == "5.00":
    print("test passed!")
