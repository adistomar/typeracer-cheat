# typeracer-cheat
A program that allows one to achieve extremely high speeds on typeracer.com. This works only for the online races and the practice races - not for the race your friend mode.
### How to setup:
* First, make sure you have Selenium installed
  - To install Selenium, go to your command line and run `pip install selenium`
* Then, make sure to have Chromedriver installed
  - To install Chromedriver, follow this [video](https://youtu.be/Xjv1sY630Uc?t=259)
* Locate and copy the path to the location where you downloaded Chromedriver
* Open the `typeracer.py` file and replace the path in the string: `PATH = "YOUR_PATH_TO_CHROMEDRIVER"`
### How to run:
* either run it direclty from your IDE
* or open command line and run `python3 typeracer.py` or `python typeracer.py` depending on your OS and python version
### Changing typing speed
* to change the typing speed, locate this line in `typeracer.py`:
```python
time.sleep(.01)
```
* change the value inside the parentheses - `.01` means that the typing speed is 1 character every .01 seconds, or 1 character every one-hundredth of a second
#### Note that this program only works for the online races and the practice races - it doesn't work for the race your friends mode.
