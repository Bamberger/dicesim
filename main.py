# IMPORTS
import rolls
import percentile
import argparse
import multiprocessing
import sim

# Predefined Variables
cycles = 10000  # How many attack cycles to sim
attacks = 1  # How many attacks to sim
at = 7  # MAT/RAT of Attacker
pow = 11  # POW of Hit
defense = 14  # DEF of Defender
arm = 20  # ARM of Defender
dice_hit = 3  # Number of Hit dice
dice_dmg = 3  # Number of Damage dice
full = 1
foc = 0
max_result = 51

# Arguments handler
parser = argparse.ArgumentParser()
# parser.add_argument("-f", "--foc", help="Attackers FOCUS")
parser.add_argument("-a", "--at", help="Attackers MAT/RAT")
parser.add_argument("-p", "--pow", help="Attackers POW")
parser.add_argument("-d", "--defense", help="Defenders DEF")
parser.add_argument("-r", "--arm", help="Defenders ARM")
parser.add_argument("-i", "--hit", help="Attackers Hit Dice #")
parser.add_argument("-m", "--dmg", help="Attackers Damage Dice #")
parser.add_argument("-t", "--attacks", help="Number of Attacks to sim")
parser.add_argument("-c", "--cycles", help="Number of Attack cycles to run")
parser.add_argument("-f", "--full", help="Print a full output table")
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
if args.cycles:
    cycles = int(args.parses)
if args.full:
    full = 1
# if args.foc:    
#     attacks = int(args.foc)

def calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc, boostflag):
    results = [0] * max_result  # Create an array to handle up to 'max_result' dmg
    ordered_results = []  # Create an array for results to land in before sorting
    input_foc = foc  # Grab the foc now before we manipulate it
    out = 0
    result = 0
    
    counter_cycle = 0
    while counter_cycle < cycles:
        counter_cycle += 1
        if input_foc == 0:  # If we are not in focus mode...
            result = sim.simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg)  # Do initial attacks
            if result == -1:
                result = 0
        if input_foc >= 1:
            if boostflag == 0:
                result = sim.simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg)  # Do initial attacks
                while input_foc >= 1:
                    out = sim.simroll(1, at, pow, defense, arm, dice_hit, dice_dmg)
                    result = result + out
                    input_foc -= 1
            if boostflag == 1:
                attacks_remaining = attacks
                while input_foc > 0:
                    out = sim.simroll(1, at, pow, defense, arm, dice_hit + 1, dice_dmg)
                    if out == -1:
                        out = 0
                    result = result + out
                    input_foc -= input_foc
                    attacks_remaining -= 1
                if attacks_remaining > 0:
                    out = sim.simroll(1, at, pow, defense, arm, dice_hit + 1, dice_dmg)
                    if out == -1:
                        out = 0
                    result = out 
                    attacks_remaining -= 1                 
                while input_foc >= 2:
                    buy = buy + sim.simroll(1, at, pow, defense, arm, dice_hit + 1, dice_dmg)
                    input_foc -= 2        
            if boostflag == 2:
#                 if input_foc >= attacks:
#                     result = sim.simroll(attacks, at, pow, defense, arm, dice_hit, dice_dmg + 1)  # Do initial attacks
#                     input_foc = input_foc - attacks
#                 else:
                attacks_remaining = attacks
                while input_foc > 0:
                    result = result + sim.simroll(attacks_remaining, at, pow, defense, arm, dice_hit, dice_dmg + 1)
                    input_foc -= input_foc
                    attacks_remaining -= attacks_remaining
                if attacks_remaining > 0:
                    attacks_remaining -= attacks_remaining
                    result = result + sim.simroll(attacks_remaining, at, pow, defense, arm, dice_hit, dice_dmg)                   
                while input_foc >= 2:
                    buy = buy + sim.simroll(1, at, pow, defense, arm, dice_hit, dice_dmg + 1)
                    input_foc -= 2       


        if input_foc == 1:  # If one foc is left, buy an attack
            out = sim.simroll(1, at, pow, defense, arm, dice_hit, dice_dmg)
            if out == -1:
                out = 0
        result = result + out
        ordered_results.append(result)
    
    
    ordered_results.sort()  # Order the ordered_results for later use
    
    for index, i in enumerate(ordered_results):  # simroll returns -1 for a miss, we need to replace that
        if i == -1:
            i = 0
            ordered_results[index] = 0
        results[i] += 1  # Populate the results array
        
    damage_total = sum(ordered_results)
     
    # print("Total Damage:", damage_total)
    print("Average Damage:", round(damage_total / cycles, 2))
     
    print("25th Percentile:", percentile.percentile(ordered_results, 0.25))
    print("50th Percentile:", percentile.percentile(ordered_results, 0.50))
    print("75th Percentile:", percentile.percentile(ordered_results, 0.75))
    print("90th Percentile:", percentile.percentile(ordered_results, 0.90))
    
    if full == 1:
        result_counter = 0
        while result_counter < max_result:
            if results[result_counter] != 0:
                ordered_index = ordered_results.index(result_counter)
                confidence = cycles - ordered_index
                print(result_counter, "damage: ", round(confidence / cycles * 100, 2), "%,", round(results[result_counter] / cycles * 100, 2), "%")
            result_counter += 1
            
if foc > 0:
    print("*** Unboosted ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc , 0)
    print()
    print("*** Boosted Attack ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc , 1)
    print()
    print("*** Boosted Damage ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc , 2)
    print()
    print("*** Fully Boosted ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg , foc , 3)
    print()
else:
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, 0, 0)
