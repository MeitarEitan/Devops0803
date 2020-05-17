from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome()

my_driver.get("https://github.com")
for i in range(5):
    #my_driver.back()
    #my_driver.forward()
    my_driver.refresh()
    sleep(5)
my_driver.close()
