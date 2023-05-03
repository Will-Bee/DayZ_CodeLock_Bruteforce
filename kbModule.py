# Import whats needed to press keys from pynput
import pydirectinput
from time import sleep
from random import randint



key = "f"

# Function to press a key for a certain amount of time
def select():
    pydirectinput.keyDown(key)
    sleep(    randint(0, 2)/10    )
    pydirectinput.keyUp(key)



def change():
    pydirectinput.keyDown(key)
    sleep(    randint(135, 160)/100    )
    pydirectinput.keyUp(key)
    sleep(1)


# TODO Implement into main code


if __name__ == "__main__":
    sleep(5)

    change()
    select()

