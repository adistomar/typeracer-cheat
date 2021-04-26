# typeracer-cheat
A program that allows one to achieve extremely high speeds on typeracer.com on all game modes.
### How it looks:
![](https://user-images.githubusercontent.com/59426357/114341733-4dfa5c00-9b0f-11eb-9ae9-9a4145a42e46.gif)
### How to setup:
* First, install Selenium by going to your command line and running `pip install selenium`
* Then, install Chromedriver by visiting the [installation page](https://chromedriver.chromium.org/downloads)
  - To know what version of Chrome you have, click on the three dots at the top right of Chrome
  - Hover over `Help` and click on `About Google Chrome` to see your Chrome version
* Locate and copy the path to the location where you downloaded Chromedriver
* Open the `typeracer.py` file and put the path inside the double quotes: `PATH = ""`
### How to run:
* If you have a typeracer account, enter your username and password inside the double quotes in `typeracer.py`
  - `username = ""`
  - `password = ""`
* Either run it directly from your IDE
* Or open command line and run `python3 typeracer.py` or `python typeracer.py` depending on your OS and python version
### Changing typing speed
* to change the typing speed, locate this line in `typeracer.py`:
```python
time.sleep(.009)
```
* change the value inside the parentheses - `.009` means that the typing speed is 1 character every .009 seconds, or 1 character every 9-thousandth of a second
