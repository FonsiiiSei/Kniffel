import dice
import cup_utils

class Cup:
    def __init__(self):
        self.dicelist = []

        for i in range(5):
            würfel = dice.Dice(0, False)
            würfel.throw()
            self.dicelist.append(würfel)

    def get_values(self):
        values = []

        for element in self.dicelist:
            values.append(element.value)

        return values

    def displayCup(self):
        print(self.get_values())

    def change_dices(self, pDicesToKeep):
        cup_utils.prepareChange(self.dicelist, pDicesToKeep)
        cup_utils.executeChange(self.dicelist)

    def manageHolding(self):
        self.displayCup()

        for i in range(0, 2):
            dices_to_keep = input("Welche Würfel sollen behalten werden?")
            dices_to_keep = [
                int(element.strip())
                for element in dices_to_keep.split(",")
            ]

            self.change_dices(dices_to_keep)
            self.displayCup()