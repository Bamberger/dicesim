# IMPORTS
import rolls
import percentile
import argparse
from datetime import datetime
import multiprocessing

time_start = datetime.now()

# Predefined Variables
attacks = 10000  # How many parses to run
at = 7  # MAT/RAT of Attacker
pow = 11  # POW of Hit
defense = 14  # DEF of Defender
arm = 20  # ARM of Defender
dice_hit = 3  # Number of Hit dice
dice_dmg = 3  # Number of Damage dice
max_result = 51

# Arguments handler
parser = argparse.ArgumentParser()
parser.add_argument("-a","--at", help="Attackers MAT/RAT")
parser.add_argument("-p","--pow", help="Attackers POW")
parser.add_argument("-d","--defense", help="Defenders DEF")
parser.add_argument("-r","--arm", help="Defenders ARM")
parser.add_argument("-i","--hit", help="Attackers Hit Dice #")
parser.add_argument("-m","--dmg", help="Attackers Damage Dice #")
parser.add_argument("-c","--attacks", help="Number of Attacks to sim")
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

results = [0] * max_result  # Create an array to handle up to 'max_result' dmg
landing_results = []  # Create an array for results to land in before sorting

roll_counter = 0 # Run a roll set for each attack
while roll_counter < attacks:
    roll_counter += 1
    result = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg) # Calls rolls.roll_full
    landing_results.append(result)

landing_results.sort()  # Order the landing_results for later use

damage_total = sum(landing_results) # Calculate total damage

for i in landing_results:
    results[i] += 1  # Populate the results array

result_counter = 0
average = 0
while result_counter < max_result:
    if results[result_counter] != 0:
        print(result_counter, "damage: ", round(results[result_counter] / attacks * 100, 2), "%")
    result_counter += 1

print("Total Damage:", damage_total)
print("Average Damage:", round(damage_total/attacks,2))

print("25th Percentile:",percentile.percentile(landing_results,0.25))
print("50th Percentile:",percentile.percentile(landing_results,0.50))
print("75th Percentile:",percentile.percentile(landing_results,0.75))
print("90th Percentile:",percentile.percentile(landing_results,0.90))

print("Execution time:", datetime.now() - time_start)
