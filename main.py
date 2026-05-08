import dice
import cup
import rules;

becher = cup.Cup()
becher.manageHolding();
regeln = rules.Rules();
regeln.all_singles(becher, 5)
