from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver'ı ayarlayın (örneğin, Chrome)
driver = webdriver.Chrome()

# Bir web sayfasını açın
driver.get("https://www.google.com")

# Arama kutusunu bulun
search_box = driver.find_element(By.NAME, "q")

# Arama terimini girin ve Enter tuşuna basın
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

# Bir süre bekleyin
time.sleep(5)

# Tarayıcıyı kapatın
driver.quit()
