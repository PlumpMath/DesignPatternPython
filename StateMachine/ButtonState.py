class ButtonStateInterface:
    _state = 0;
    #State method, the return value defines the next state
    def changeGpioState(self):
        pass

    def __getstate__(self):
        return ButtonStateInterface._state

    def printState(self):
        print('Current State is :'+str(ButtonStateInterface.state))


class ButtonStateOn(ButtonStateInterface):
#Singleton
    __instance=None

    def __new__(cls):
        if ButtonStateOn.__instance is None:
            ButtonStateOn.__instance = object.__new__(cls)
        return ButtonStateOn.__instance


    def changeGpioState(self):
        print('on')
        ButtonStateInterface._state = 1
        return ButtonStateOff()


class ButtonStateOff(ButtonStateInterface):
#Singleton
    __instance=None

    def __new__(cls):
        if ButtonStateOff.__instance is None:
            ButtonStateOff.__instance=object.__new__(cls)
        return ButtonStateOff.__instance

    def changeGpioState(self):
        print('off')
        ButtonStateInterface._state = 0
        return ButtonStateOn()

