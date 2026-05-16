import dice

def prepareChange(pDiceList, pDicesToKeep):

    for element in pDicesToKeep:
        currentDice = pDiceList[element - 1]
        currentDice.out = True


def executeChange(pDiceList):

    for element in pDiceList:
        if not element.out:
            element.throw()

    # reset
    for element in pDiceList:
        element.out = False