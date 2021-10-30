# typeracer-cheat
A program that allows one to achieve extremely high speeds on typeracer.com on all game modes.
### How it looks:
![](https://user-images.githubusercontent.com/59426357/114341733-4dfa5c00-9b0f-11eb-9ae9-9a4145a42e46.gif)
### How to setup:
* Install Selenium by going to terminal and running `pip install selenium`
### How to run:
* Open terminal
* Locate the folder where you downloaded the program: `cd <folder>/typeracer-cheat/` where folder is Downloads, Documents, etc.
* Run `python3 typeracer.py`
### Changing typing speed
* To change the typing speed, locate this line in `typeracer.py`:
```python
time.sleep(.009)
```
* Change the value inside the parentheses - `.009` means that the typing speed is 1 character every .009 seconds, or 1 character every 9-thousandth of a second
