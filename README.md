# typeracer-cheat
A program that allows one to achieve extremely high speeds on typeracer.com on all game modes.

## Demo:
https://user-images.githubusercontent.com/59426357/174093466-ce797f7b-86ba-4228-a056-cb46d174a1b9.mp4

## Install:
#### Python 3.6 or higher is required
```sh
pip3 install typeracer_cheat
```

## Usage:
To run cheat, enter `type_cheat` in command line.


## Change typing speed
To change the typing speed, locate this line in [`main.py`](https://github.com/RoastSea8/typeracer-cheat/blob/master/typeracer_cheat/main.py):
```python
time.sleep(.009)
```
Change the value inside the parentheses: `.009` means that the typing speed is 1 character every .009 seconds, or 1 character every 9-thousandth of a second.
