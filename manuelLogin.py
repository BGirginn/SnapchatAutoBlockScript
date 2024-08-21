from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Snapchat hesap bilgileri
username = "bora"
password = "bora"

# Engellenecek arkadaşların listesi
friends_to_block = ["blocked username 1", "blocked username 2"]

# Chrome opsiyonlarını ayarla
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# WebDriver'ı başlat
driver = webdriver.Chrome(options=chrome_options)

# Snapchat web sitesine git
driver.get("https://web.snapchat.com")

# Eğer oturum açık değilse, oturum aç
if "Login" in driver.title:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ai_input"))
    )
    username_input.send_keys(username)
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "sidebar_submitBtnWrapper__iIUeq"))
    )
    login_button.click()
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(password)
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "sidebar_submitBtnWrapper__iIUeq"))
    )
    login_button.click()

    # Oturum açma işlemi tamamlanana kadar bekle
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
    )

# Arkadaşları engelleme
for friend in friends_to_block:
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
    )
    search_input.clear()
    search_input.send_keys(friend)
    
    friend_profile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{friend}')]"))
    )
    friend_profile.click()
    
    settings_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Settings')]"))
    )
    settings_button.click()
    
    block_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Block')]"))
    )
    block_button.click()
    
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Block')]"))
    )
    confirm_button.click()
    
    # Ana sayfaya dön
    driver.get("https://web.snapchat.com")
    time.sleep(5)