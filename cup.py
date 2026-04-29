import dice
import cup_utils

class Cup:
    def __init__(self):
        self.dicelist = []

        for i in range(5):
            würfel = dice.Dice(0, False)
            würfel.throw()
            self.dicelist.append(würfel)

    def displayCup(self):
        display = []
        for element in self.dicelist:
            display.append(element.show());
        print(display)

    def manageHolding(self):
        self.displayCup();
        dices_to_keep = input("Welche Würfel sollen behalten werden?")
        dices_to_keep = [int(element.strip()) for element in dices_to_keep.split(",")]
        cup_utils.prepareChange(self.dicelist, dices_to_keep)
        self.displayCup();
        

        