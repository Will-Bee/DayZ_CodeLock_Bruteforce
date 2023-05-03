import kbModule as kb
from time import sleep


### There are only 2 types of instruction
### 1: Select digit (You can only move to left and from the last digit to the first digit)
### 2: Change digit (You can only add 1 to the digit, if the digit is 9, it will be 0)
### I need to go through every possible combination of the digits


class CodeLock:

    selectionIndex = 0

    counter = 0

    def __init__(self, digits):
        self.type = digits
        if digits == 3:
            self.digits = [0, 0, 0]
        elif digits == 4:
            self.digits = [0, 0, 0, 0]



    def changeDigit(self):
        digitToChange = self.digits[self.selectionIndex]
        if digitToChange == 9:
            digitToChange = 0
        else:
            digitToChange = digitToChange + 1

        self.digits[self.selectionIndex] = digitToChange

        self.log()
        kb.change()




    def selectDigit(self):
        if self.selectionIndex == self.type - 1:
            self.selectionIndex = 0
        else:
            self.selectionIndex = self.selectionIndex + 1

        self.log()
        kb.select()



    def unlock4(self):
        global pause
        for t in range(0, 10):
            for h in range(0, 10-1):
                self.selectDigit()
                self.selectDigit()
                self.selectDigit()

                for d in range(0, 10):
                    self.changeDigit()
                    self.counter += 1

                for t in range(0, 10):
                    self.selectDigit()
                    self.selectDigit()
                    self.selectDigit()
                    self.changeDigit()
                    self. selectDigit()
                    for d in range(0, 10):
                        self.changeDigit()
                        self.counter += 1
                self.changeDigit()
                self.selectDigit()
                self.selectDigit()
                self.changeDigit()
                self.selectDigit()
                self.changeDigit()
                self.selectDigit()
                self.selectDigit()
                self.counter += 1

            self.changeDigit()
            self.selectDigit()
            self.changeDigit()
            self.selectDigit()
            self.changeDigit()
            self.selectDigit()
            self.changeDigit()
            self.selectDigit()
            self.counter += 1



    def bruteForce(self):

        for i in range(5, 0, -1):
            print("\r[i]Starting in ", i, end="", sep="")
            sleep(1)

        print("\r                      ")
        self.guiHeader()

        if self.type == 3:
            pass
        elif self.type == 4:
            self.unlock4()
            print("Total combinations: " + str(self.counter))



    def guiHeader(self):
        # Cli:

        # [] DayZ Lockpicker ###
        # [] Code type: {X} digits ###
        # [] Lockpicking... ###
        #  0  [0]  0   0

        print('\r', end='')
        print("[ ] DayZ Lockpicker")
        print("[ ] Code type: " + str(self.type) + " digits")
        print("[ ] Lockpicking...")



    def log(self):

        for index, digit in enumerate(self.digits):
            if index == self.selectionIndex:
                print(f"[{self.digits[index]}]", end="")
            else:
                print(f" {self.digits[index]} ", end="")

        print("\r", end="")



if __name__ == "__main__":

    codeLock = CodeLock(4)
    codeLock.bruteForce()
