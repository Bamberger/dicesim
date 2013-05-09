# IMPORTS
import rolls
from datetime import datetime
# from multiprocessing import Pool

time_start = datetime.now()

# VARS
attacks = 10000000 # How many parses to run
at = 7 # MAT/RAT of Attacker
pow =11 # POW of Hit
defense = 7 # DEF of Defender
arm = 20 # ARM of Defender
dice_hit = 2 # Number of Hit dice
dice_dmg = 4 # Number of Damage dice
max_result = 51

results = [0] * max_result  # Create an array to handle up to 'max_result' dmg
landing_results = [] # Create an array for results to land in before sorting

# 
# roll_counter = 0
# while roll_counter < attacks:
#     roll_counter += 1
#     result = rolls.roll_full(at,pow,defense,arm,dice_hit,dice_dmg)
#     results[result] += 1
    
roll_counter = 0
while roll_counter < attacks:
    roll_counter += 1
    result = rolls.roll_full(at,pow,defense,arm,dice_hit,dice_dmg)
    landing_results.append(result)
# print(landing_results)

for i in landing_results:
    results[i] += 1

result_counter = 0
average = 0
while result_counter < max_result:
    if results[result_counter] != 0:
#         print(result_counter, "damage: ", results[result_counter], "/", attacks, round(results[result_counter] / attacks * 100,2), "%")
        print(result_counter, "damage: ", round(results[result_counter] / attacks * 100,2), "%")
        average = average + result_counter * round(results[result_counter] / attacks ,2)
    result_counter += 1
print("Average Damage:",round(average,2))

print("Execution time:", datetime.now() - time_start)