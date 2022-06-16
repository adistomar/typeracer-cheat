from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
from tkinter.ttk import *
import sys
import os
import chromedriver_autoinstall


root = Tk()

root.title("TypeRacer Cheat")
Label(root).grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

username = ""
password = ""
chromedriver_autoinstall.install()
if chromedriver_autoinstall.get_platform() == "mac":
   os.chmod('./chromedriver', 0o755)
PATH = "./chromedriver"
driver = None
started = False

usr_txt = Label(root, text="username: ")
pass_txt = Label(root, text="password: ")

usr_txt.grid(row=0, column=0, sticky="W", pady=2)
pass_txt.grid(row=1, column=0, sticky="W", pady=2)

usr_e = Entry(root)
pass_e = Entry(root)
pass_e.config(show="*")
usr_e.grid(column=1, row=0)
pass_e.grid(column=1, row=1)


def get(event):
   global username
   global password
   global driver
   username = str(event.widget.get())
   password = str(event.widget.get())
   driver = webdriver.Chrome(PATH)
   driver.get("https://play.typeracer.com/")
   login()


usr_e.bind('<Return>', get)
pass_e.bind('<Return>', get)


def play_as_guest():
   global username
   global password
   global driver
   global started
   username = ""
   password = ""
   root.destroy()
   started = True
   driver = webdriver.Chrome(PATH)
   driver.get("https://play.typeracer.com/")
   login()


guest_btn = Button(root, text="Play as guest", command=play_as_guest)
guest_btn.grid(column=1, row=3)


def quit_btn():
   root.destroy()
   sys.exit()


button_quit = Button(root, text="Exit", command=quit_btn)
button_quit.grid(column=3, row=3)


def login():
   global username
   global password
   global driver
   if not username or not password:
      print("no username/password")
   else:
      try:
         login_ = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "acctButtons")))
         loginbtn = login_.find_element_by_xpath("//a[@class='promptBtn signIn']")
         loginbtn.click()

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


def friend_mode_handler(driver, main, text):
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
   global driver
   try:
      main = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "gameView")))

      text = main.text
      text = text.split("\n")

      text = friend_mode_handler(driver, main, text)

      text = text[-3]  # getting the actual text content from list

      race_status = main.find_element_by_class_name("gameStatusLabel").text

      while "go" not in race_status.lower() and "the race is on" not in race_status.lower():
         race_status = main.find_element_by_class_name("gameStatusLabel").text

      text_box = main.find_element_by_class_name("txtInput")

      for i in text:
         text_box.send_keys(i)
         time.sleep(.009)  # 1 char every 0.009 seconds

   except:
      pass


def isDriverClosed():
   global driver
   if driver:
      if not driver.window_handles:
         return True
      else:
         return False

def main():
   while True:
      game()
      if not started:
         root.update_idletasks()
         root.update()
      else:
         pass
      if isDriverClosed():
         exit()