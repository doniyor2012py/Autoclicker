from keyboard import add_hotkey, wait, is_pressed
from mouse import click
from time import sleep


wait("a")
while True:
    click("left")
    sleep(0.01)
    if is_pressed("q"):
        break

