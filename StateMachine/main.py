from ButtonState import ButtonStateOff
import time

#Defines the programm start state
state = ButtonStateOff()

while True:
    time.sleep(1)
    state = state.changeGpioState()
