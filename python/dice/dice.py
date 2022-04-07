import random
import re

pattern = r'(\d+)[dD](\d+)([+-])?(\d*)'

def roll_dice(num_dice,dice_faces):
    roll_results = []
    for _ in range(int(num_dice)):
        roll = random.randint(1, int(dice_faces))
        roll_results.append(roll)
    
    return roll_results


reg = re.compile(pattern)
input_dice = input("Dado:")
dice = reg.search(input_dice)
roll_results = roll_dice(dice.group(1),dice.group(2))
print(roll_results)