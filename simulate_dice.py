'''
Author Notes:
It took me a while to understand how to update the dictionary with the outcomes. The use of the method get() was useful here and worked well for that purpose.
The instructor used the module collections in his solution, which was also important to learn.

Briefing:
Rolling dice simulation
Input: variable number of arguments for sides of a dice
Output: table of probability for each possible outcome
'''
import random

def roll_dice(*dice_sides, sampling=1000000):
    n = 0
    probabilities = {}

    while n < sampling:
        outcome = 0
        for sides in dice_sides:
            outcome = outcome + random.randint(1,sides)
        probabilities[outcome] =  probabilities.get(outcome,0) + (100 / sampling)
        n += 1
    
    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice_sides),sum(dice_sides) + 1):
        print(f'{outcome:02d}\t{probabilities[outcome] :.2f}%')

# Please, uncomment the line below to execute the code with the example given
# roll_dice(4,6,6,20)