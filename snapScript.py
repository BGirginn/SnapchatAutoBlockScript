from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# write your username and password snapchat account
username = "snapchat username"
password = "password"

# blocked friends list 
friends_to_block = ["blocked username 1, blocked username 2,"]

driver = webdriver.Chrome()

driver.get("https://web.snapchat.com")

# doing log in in from this moment dont touch anything in this BUT IF YOUR NETWORK SPEED IS SLOW CHANGE SLEEP TIME MORE THAN 10
time.sleep(10)

username_input = driver.find_element(By.ID, "ai_input")
username_input.send_keys(username)

login_button = driver.find_element(By.CLASS_NAME, "sidebar_submitBtnWrapper__iIUeq")
login_button.click()

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)

login_button = driver.find_element(By.CLASS_NAME, "sidebar_submitBtnWrapper__iIUeq")
login_button.click()

time.sleep(30)

# blocking
for friend in friends_to_block:
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_input.clear()
    search_input.send_keys(friend)
    time.sleep(10)  

    friend_profile = driver.find_element(By.XPATH, f"//span[contains(text(), '{friend}')]")
    friend_profile.click()
    time.sleep(10)

    settings_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Settings')]")
    settings_button.click()
    time.sleep(10)

    block_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Block')]")
    block_button.click()
    time.sleep(10)

    confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Block')]")
    confirm_button.click()
    time.sleep(10)

    driver.get("https://web.snapchat.com")
    time.sleep(10)

# if u want close your chrome tab dont touch last code bu if u dont want u can delete or add # before the all command on last command line
driver.quit()
