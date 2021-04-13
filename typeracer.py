from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = ""
username = ""
password = ""

driver = webdriver.Chrome(PATH)

driver.get("https://play.typeracer.com/")


def login():
    if not username or not password:
        print("no username/password")
    else:
        try:
            login_ = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "MainUserInfoEditor")))
            login_window = login_.find_element_by_class_name("gwt-Anchor")
            login_window.click()

            username_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "username")))

            password_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "password")))

            username_box.send_keys(username)
            password_box.send_keys(password)

            login_btn = driver.find_element_by_class_name("gwt-Button")
            login_btn.click()

        except:
            print("login error")


def game():
    try:
        main = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "gameView")))

        text = main.text
        text = text.split("\n")[-3]  # getting the actual text content

        race_status = main.find_element_by_class_name("gameStatusLabel").text

        while "Go" not in race_status and "The race is on" not in race_status:
            race_status = main.find_element_by_class_name("gameStatusLabel").text

        text_box = main.find_element_by_class_name("txtInput")

        for i in text:
            text_box.send_keys(i)
            time.sleep(.01)  # 1 char every 0.01 seconds

    except:
        print("game error")


login()
game()
