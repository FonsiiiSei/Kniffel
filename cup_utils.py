
def prepareChange(pDiceList, pDicesToKeep):
    for element in pDicesToKeep:
        currentDice = pDiceList[element-1];
        currentDice.out = True;

    

    