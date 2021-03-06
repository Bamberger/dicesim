from random import random

def roll_hit(at, defense, dice_hit):
    i = 0
    result = 0
    while i < dice_hit:
       i += 1
       result = result + int(random() * 6) + 1
    auto_check = result / dice_hit
    if auto_check == 1:  # Look for an auto-miss
        return(0)
    elif at + result >= defense:  # If we equal or beat the DEF return a hit
       return(1)
    elif auto_check == 6:  # Look for an auto-hit
       return(1)
    else:  # Else return a miss
       return(0)

def roll_dmg(pow, arm, dice_dmg):
    i = 0
    while i < dice_dmg:
       i += 1
       pow = pow + int(random() * 6) + 1
    if pow > arm:
        return(pow - arm)
    else:
        return(0)

def roll_full(at, pow, defense, arm, dice_hit, dice_dmg):
    hit_result = roll_hit(at, defense, dice_hit)
    if hit_result == 1:
        dmg_result = roll_dmg(pow, arm, dice_dmg)
        return(dmg_result)
    else:
         return(-1)
