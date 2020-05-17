from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_driver = webdriver.Chrome()
my_driver.get("https://www.google.com/")
write_some=my_driver.find_element_by_name("q")
write_some.send_keys("ynet")
press=my_driver.find_element_by_name("btnK")
press.submit()
