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


def friend_mode_check(text):
    for _ in text:
        if 'join' in _.lower():
            return True


def friend_mode_handler(main, text):
    if friend_mode_check(text):
        race_status = main.find_element_by_class_name("gameStatusLabel").text
        while 'waiting' not in race_status.lower() and 'about to start' not in race_status.lower():
            race_status = main.find_element_by_class_name("gameStatusLabel").text
        main = driver.find_element_by_class_name("gameView")
        text = main.text
        text = text.split("\n")
    else:
        pass
    return text


def game():
    try:
        main = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "gameView")))

        text = main.text
        text = text.split("\n")

        text = friend_mode_handler(main, text)

        text = text[-3]  # getting the actual text content from list

        race_status = main.find_element_by_class_name("gameStatusLabel").text

        while "go" not in race_status.lower() and "the race is on" not in race_status.lower():
            race_status = main.find_element_by_class_name("gameStatusLabel").text

        text_box = main.find_element_by_class_name("txtInput")

        for i in text:
            text_box.send_keys(i)
            time.sleep(.01)  # 1 char every 0.01 seconds

    except:
        print("game error")


login()
game()
