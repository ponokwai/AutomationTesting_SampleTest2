from selenium import webdriver
import os
from pathlib import Path
import time

#folder_path = str(Path(__file__).parents[0])
print("starting test")
def test_my_very_first_test():
    #driver = webdriver.Chrome(os.path.join(folder_path, 'chromedriver'))
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    driver.maximize_window()
    time.sleep(3)

#test_my_very_first_test()
#driver = webdriver.Chrome(r"C:\Users\Patrick.Onokwai\PycharmProjects\AutomationTesting_SampleTest2\Browsers\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(3)
driver.close()
print("End test")