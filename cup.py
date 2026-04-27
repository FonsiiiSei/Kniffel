import dice

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