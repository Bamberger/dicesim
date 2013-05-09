# IMPORTS
import rolls
# from multiprocessing import Pool

# VARS
attacks = 10000 #How many parses to run
at = 7 #MAT/RAT of Attacker
pow =11 #POW of Hit
defense = 7 #DEF of Defender
arm = 20 #ARM of Defender
dice_hit = 2 #Number of Hit dice
dice_dmg = 4 #Number of Damage dice
max_result = 51

results = [0] * max_result  # Create an array to handle up to 'max_result' dmg

roll_counter = 0
while roll_counter < attacks:
    roll_counter += 1
    result = rolls.roll_full(at,pow,defense,arm,dice_hit,dice_dmg)
    results[result] += 1

result_counter = 0
average = 0
while result_counter < max_result:
    if results[result_counter] != 0:
#         print(result_counter, "damage: ", results[result_counter], "/", attacks, round(results[result_counter] / attacks * 100,2), "%")
        print(result_counter, "damage: ", round(results[result_counter] / attacks * 100,2), "%")
        average = average + result_counter * round(results[result_counter] / attacks ,2)
    result_counter += 1
print("Average Damage:",round(average,2))