from collections import Counter

class Rules:

    def full_house(self, diceList):
        counter = Counter(diceList)

        if sorted(counter.values()) == [2,3]:
            return True

        return False
    
    def all_singles(self, cup, pSingleDice):
        sumSingle = 0;

        for element in cup.dicelist:
            if int(element.value) == pSingleDice:
                sumSingle = sumSingle + pSingleDice;

        print(sumSingle);
        return sumSingle;