# IMPORTS
import rolls
import percentile
import argparse
import multiprocessing

max_result = 51


results = [0] * max_result  # Create an array to handle up to 'max_result' dmg
landing_results = []  # Create an array for results to land in before sorting

def simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg):
    roll_counter = 0  # Run a roll set for each attack
    while roll_counter < attacks:
        roll_counter += 1
        result = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)  # Calls rolls.roll_full
        landing_results.append(result)

    landing_results.sort()  # Order the landing_results for later use
    
    damage_total = sum(landing_results)  # Calculate total damage
    
    for i in landing_results:
        results[i] += 1  # Populate the results array
    
    result_counter = 0
    average = 0
    while result_counter < max_result:
        if results[result_counter] != 0:
            print(result_counter, "damage: ", round(results[result_counter] / attacks * 100, 2), "%")
        result_counter += 1
    
    print("Total Damage:", damage_total)
    print("Average Damage:", round(damage_total / attacks, 2))
    
    print("25th Percentile:", percentile.percentile(landing_results, 0.25))
    print("50th Percentile:", percentile.percentile(landing_results, 0.50))
    print("75th Percentile:", percentile.percentile(landing_results, 0.75))
    print("90th Percentile:", percentile.percentile(landing_results, 0.90))