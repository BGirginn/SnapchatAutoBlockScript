from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Snapchat giriş bilgilerinizi tanımlayın
username = "your_snapchat_username"
password = "your_snapchat_password"

# Engellenecek arkadaşların listesi
friends_to_block = ["friend1_username", "friend2_username", "friend3_username"]

# WebDriver'ı ayarlayın (örneğin, Chrome)
driver = webdriver.Chrome()

# Snapchat giriş sayfasını açın
driver.get("https://web.snapchat.com")

# Snapchat'e giriş yapın
time.sleep(2)  # Sayfanın yüklenmesi için bekleyin

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)

login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")
login_button.click()

# Girişin tamamlanmasını bekleyin
time.sleep(10)

# Listedeki her bir arkadaşı engelleme
for friend in friends_to_block:
    # Arkadaşı arayın
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_input.clear()
    search_input.send_keys(friend)
    time.sleep(2)  # Arama sonuçlarının yüklenmesi için bekleyin

    # Arkadaşın profilini tıklayın
    friend_profile = driver.find_element(By.XPATH, f"//span[contains(text(), '{friend}')]")
    friend_profile.click()
    time.sleep(2)

    # Ayarlar menüsünü açın
    settings_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Settings')]")
    settings_button.click()
    time.sleep(2)

    # Engelleme düğmesini tıklayın
    block_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Block')]")
    block_button.click()
    time.sleep(2)

    # Engelleme işlemini onaylayın
    confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Block')]")
    confirm_button.click()
    time.sleep(2)

    # Ana sayfaya geri dönün
    driver.get("https://web.snapchat.com")
    time.sleep(5)

# Tarayıcıyı kapatın
driver.quit()
