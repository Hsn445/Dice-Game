# Consider variable privating?
import random as rand
from typing import List

# Variables: type -> str: Dice Color
#            face -> int: D6 Value
#            actual -> int: Actual Dice Value

# Basic Dice Class
class Dice:
    type: str
    face: List[int] = []
    actual: List[int] = []

    def roll(self):
        if (self.face != []):
            del self.face[0]
        self.face.append(rand.randint(1, 6))

# White Dice give points equal to a normal d6 during the roll phase. During the draft
# phase, they are used to break ties
class White(Dice):
    def __init__(self):
        self.type = 'White'
        self.actual = self.face

# Black Dice subtract from your total during the roll phase
class Black(Dice):
    def __init__(self):
        self.type = 'Black'
    
    def roll(self):
        super().roll()
        if (self.actual != []):
            del self.actual[0]
        self.actual.append(self.face[0] * -1)

# Red Dice have +1 on their dice roll
class Red(Dice):
    def __init__(self):
        self.type = 'Red'

    def roll(self):
        super().roll()
        if (self.actual != []):
            del self.actual[0]
        self.actual.append(self.face[0] + 1)

# Orange Dice add 6 to your total if you have a run of 5. For each additional dice in
# the run, the total increases by that amount
# PROGRAMMER NOTE: checkorange not implemented due to uncertainty on dice collection structure
class Orange(Dice):
    def __init__(self):
        self.type = 'Orange'
        self.actual = self.face
    
    def checkorange(self):  # (NOT CODED) Automatically runs after any dice is used
        pass

# Yellow Dice can be rerolled once
class Yellow(Dice):
    ifReroll: bool = True # Check if Yellow Dice can be rerolled
    def __init__(self):
        self.type = 'Yellow'
        self.actual = self.face

    def reroll(self):
        if (self.ifReroll): # Not an option if reroll has already been used
            Dice.roll(self)
            self.ifReroll = False

# Green Dice are equal to your highest Green Die
# PROGRAMMER NOTE: subclass not implemented due to uncertainty on dice collection structure
class Green(Dice):
    pass

# Blue Dice can be reduced from its face value to any lower d6 value
class Blue(Dice):
    def __init__(self):
        self.type = 'Blue'
        self.actual = self.face
    
    def spindown(self): # Not an option if blue dice has face value of 1
        if (self.face[0] > 1):
            validInput = False  # Will need to be changed to picture(?) select when UI implemented
            while not(validInput):
                print('Input value to spindown to: ')
                newAct = int(input())
                if(newAct <= self.face[0]):
                    self.actual[0] = newAct
                    validInput = True

# Purple Dice can be made permanent
# PROGRAMMER NOTE: permanent not implemented due to uncertainty on dice collection structure
# INTERACTION CHECK NOTE: permanent dice are un-permanented upon player death?
class Purple(Dice):
    isPermanent: bool = False   # Check if Purple Dice has been made permanent
    def __init__(self):
        self.type = 'Purple'
        self.actual = self.face
    
    def permanent(self):
        pass

# Pink Dice do not give points during the roll phase, but instead double your points
# if the sum of Pink Dice is greater than or equal to 7
# PROGRAMMER NOTE: pinkd not implemented due to uncertainty on dice collection structure
class Pink(Dice):
    def __init__(self):
        self.type = 'Pink'
        self.actual.append(0)

    def pinkd(self):
        pass

# Brown Dice do not give points durint the roll phase and have -1 on their dice roll
# (minimum of 1), but can be attatched to another Dice to increase that Die's value
# PROGRAMMER NOTE: attatch not implemented due to uncertainty on dice collection structure
class Brown(Dice):
    def __init__(self):
        self.type = 'Brown'

# Evolution White Dice ...
class EvoWhite(Dice):
    pass

dice = Red()
print(dice.type)
dice.roll()
print(dice.face)
print(dice.actual)
dice.roll()
print(dice.face)
print(dice.actual)

# Evolution Black Dice ...
class EvoBlack(Dice):
    pass

# Evolution Red Dice ...
class EvoRed(Dice):
    pass

# Evolution Orange Dice ...
class EvoOrange:
    pass

# Evolution Yellow Dice ...
class EvoYellow:
    pass

# Evolution Green Dice ...
class EvoGreen:
    pass

# Evolution Blue Dice ...
class EvoBlue:
    pass

# Evolution Purple Dice ...
class EvoPurple:
    pass

# Evolution Pink Dice ...
class EvoPink:
    pass

# Evolution Brown Dice ...
class EvoBrown:
    pass