# main.py

import cup
import game

# Becher erzeugen
becher = cup.Cup()

# Game / Oberfläche erzeugen
feld = game.Game()

# Oberfläche starten
feld.build_field(becher)