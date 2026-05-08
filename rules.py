from collections import Counter

class Rules:

    def full_house(self, diceList):
        counter = Counter(diceList)

        if sorted(counter.values()) == [2,3]:
            return True

        return False
    
    