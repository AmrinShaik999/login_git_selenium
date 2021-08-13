from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
import time
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://accounts.datoms.io/login')
driver.find_element(By.ID,"email").send_keys("skamrin999@gmail.com")
driver.find_element(By.ID,"password").send_keys("12345678")
login=driver.find_element(By.XPATH,'//*[@id="form_submit_btn"]')

login.click()
time.sleep(5)



