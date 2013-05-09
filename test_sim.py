# IMPORTS
import rolls
import percentile
import argparse
from datetime import datetime
import multiprocessing
import time

time_start = datetime.now()

# Predefined Variables
attacks = 100  # How many parses to run
at = 7  # MAT/RAT of Attacker
pow = 11  # POW of Hit
defense = 14  # DEF of Defender
arm = 20  # ARM of Defender
dice_hit = 2  # Number of Hit dice
dice_dmg = 4  # Number of Damage dice
max_result = 51

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

roll_counter = 0
while roll_counter < attacks:
    roll_counter += 1
    if __name__ == '__main__':
        pool = multiprocessing.Pool(processes=4)
        result = pool.apply_async(rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg))
#         while result.ready() == False:
#             time.sleep(0.1)
#         print(result.get())
        
# result_queue = multiprocessing.Queue()
# montecarlos = [MonteCarlo(result_queue, f,fargs) for fargs in farglist]
# obs = [multiprocessing.Process(mc) for mc in montecarlos]
# for job in jobs: job.start()
# for job in jobs: job.join()
# results = [result_queue.get() for mc in montecarlos]
# 
# jobs = [multiprocessing.Process(target=MonteCarlo, args=(f, fargs) for fargs in farglist]

# roll_counter = 0
# while roll_counter < attacks:
#     roll_counter += 1
#     result = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)
#     landing_results.append(result)
# 
# landing_results.sort()  # Order the landing_results for later use
# 
# damage_total = sum(landing_results) # Calculate total damage
# 
# for i in landing_results:
#     results[i] += 1  # Populate the results array
# 
# result_counter = 0
# average = 0
# while result_counter < max_result:
#     if results[result_counter] != 0:
#         print(result_counter, "damage: ", round(results[result_counter] / attacks * 100, 2), "%")
#     result_counter += 1
# 
# print("Total Damage:", damage_total)
# print("Average Damage:", round(damage_total/attacks,2))
# 
# print("25th Percentile:",percentile.percentile(landing_results,0.25))
# print("50th Percentile:",percentile.percentile(landing_results,0.50))
# print("75th Percentile:",percentile.percentile(landing_results,0.75))
# print("90th Percentile:",percentile.percentile(landing_results,0.90))
# 
# 
# 
# print("Execution time:", datetime.now() - time_start)
