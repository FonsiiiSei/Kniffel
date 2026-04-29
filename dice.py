import pygame
import random

class Dice:
    def __init__(self, value, out):
        self.value = value
        self.out = out;

    def throw(self):
        self.value = random.randint(1,6)

    def show(self):
        return f"{self.value} - {self.out}" 