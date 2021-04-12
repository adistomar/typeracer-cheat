from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "YOUR_PATH_TO_CHROMEDRIVER"
driver = webdriver.Chrome(PATH)

driver.get("https://play.typeracer.com/")

try:
    main = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gameView"))
    )

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
    print("error")
