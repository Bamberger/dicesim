# IMPORTS
import rolls
import percentile
import argparse
import multiprocessing
import sim

# Predefined Variables
attacks = 10000  # How many parses to run
at = 7  # MAT/RAT of Attacker
pow = 11  # POW of Hit
defense = 14  # DEF of Defender
arm = 20  # ARM of Defender
dice_hit = 3  # Number of Hit dice
dice_dmg = 3  # Number of Damage dice
foc = 1
max_result = 51

# Arguments handler
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foc", help="Attackers FOCUS")
parser.add_argument("-a", "--at", help="Attackers MAT/RAT")
parser.add_argument("-p", "--pow", help="Attackers POW")
parser.add_argument("-d", "--defense", help="Defenders DEF")
parser.add_argument("-r", "--arm", help="Defenders ARM")
parser.add_argument("-i", "--hit", help="Attackers Hit Dice #")
parser.add_argument("-m", "--dmg", help="Attackers Damage Dice #")
parser.add_argument("-c", "--attacks", help="Number of Attacks to sim")
args = parser.parse_args()
if args.at:    
    at = int(args.at)
if args.pow:    
    pow = int(args.pow)
if args.defense:    
    defense = int(args.defense)
if args.arm:    
    arm = int(args.arm)
if args.hit:    
    hit = int(args.hit) 
if args.dmg:    
    dmg = int(args.dmg)
if args.attacks:    
    attacks = int(args.attacks)
if args.foc:    
    attacks = int(args.foc)

# if foc > 0:
#     print("Unboosted")
#     sim.simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg)
#     print("Boosted Attack")
#     sim.simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg)
#     print("Boosted Damage")
#     sim.simroll(attacks,at, pow, defense, arm, dice_hit, dice_dmg + 1)
#     print("Fully Boosted")
#     sim.simroll(attacks,at, pow, defense, arm, dice_hit + 1, dice_dmg + 1)

sim.simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg)
