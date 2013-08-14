# IMPORTS
import rolls
import percentile
import argparse
import multiprocessing
import sim
import time

start_time = time.time()

# Predefined Variables
cycles = 10000  # How many attack cycles to sim
attacks = 2  # How many attacks to sim
at = 9  # MAT/RAT of Attacker
pow = 12  # POW of Hit
defense = 14  # DEF of Defender
arm = 18  # ARM of Defender
cycles = 1000000  # How many attack cycles to sim
attacks = 1  # How many attacks to sim
at = 7  # MAT/RAT of Attacker
pow = 9  # POW of Hit
defense = 14  # DEF of Defender
arm = 15  # ARM of Defender
dice_hit = 2  # Number of Hit dice
dice_dmg = 3  # Number of Damage dice
full = 1
foc = 0
max_result = 100

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

# delta_hit = defense - at
# delta_arm = arm - pow

def calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc, boostflag):
    results = [0] * max_result  # Create an array to handle up to 'max_result' dmg
    ordered_results = []  # Create an array for results to land in before sorting
    input_foc = foc  # Grab the foc now before we manipulate it
    out = 0 
    counter_cycle = 0
    
    while counter_cycle < cycles:
        result = 0
        counter_cycle += 1
#         if full == 1:
#             process = counter_cycle / cycles * 10
#             if process == int(process):
#                 print(int(process * 10), "% Complete",round(time.time() - start_time,2), "seconds")           
        if input_foc == 0:  # If we are not in focus mode...
            cycle_attacks = attacks
            while cycle_attacks > 0:          
                out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)  # Do initial attacks
                if out == -1:
                    out = 0
                result = result + out
                cycle_attacks -= 1
        elif boostflag == 0:
            cycle_attacks = attacks + foc
            while cycle_attacks > 0:          
                out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)  # Do initial attacks
                if out == -1:
                    out = 0
                result = result + out
                cycle_attacks -= 1
        elif boostflag == 1:
            cycle_attacks = attacks + foc
            while cycle_attacks > 0:
                if cycle_attacks >= 2:    
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit + 1, dice_dmg)  # Do initial attacks
                    if out == -1:
                        out = 0
                    cycle_attacks -= 2
                else:
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)
                    if out == -1:
                        out = 0
                    cycle_attacks -= 1
                result = result + out
        elif boostflag == 2:
            cycle_attacks = attacks + foc
            while cycle_attacks > 0:
                if cycle_attacks >= 2:    
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg + 1)  # Do initial attacks
                    if out == -1:
                        out = 0
                        cycle_attacks += 1
                    cycle_attacks -= 2
                else:
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)
                    if out == -1:
                        out = 0
                    cycle_attacks -= 1
                result = result + out
        elif boostflag == 3:
            cycle_attacks = attacks + foc
            while cycle_attacks > 0:
                if cycle_attacks >= 3:    
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit + 1, dice_dmg + 1)  # Do initial attacks
                    if out == -1:
                        out = 0
                        cycle_attacks += 1
                    cycle_attacks -= 3                 
                elif cycle_attacks == 2:    
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg + 1)  # Do initial attacks
                    if out == -1:
                        out = 0
                        cycle_attacks += 1
                    cycle_attacks -= 2                  
                else:
                    out = rolls.roll_full(at, pow, defense, arm, dice_hit, dice_dmg)
                    if out == -1:
                        out = 0
                    cycle_attacks -= 1
                result = result + out
        
#         if input_foc == 1:  # If one foc is left, buy an attack
#             out = sim.simroll(1, at, pow, defense, arm, dice_hit, dice_dmg)
#             if out == -1:
#                 out = 0
#             result = result + out
        ordered_results.append(result)
        
    ordered_results.sort()  # Order the ordered_results for later use
    
    for index, i in enumerate(ordered_results):
        results[i] += 1  # Populate the results array
        
    damage_total = sum(ordered_results)
    # print("Total Damage:", damage_total)
    if full == 1:
        print("*** Full results for", attacks, "attacks ***")
    
    print("Average Damage:", "\t", round(damage_total / cycles, 2))
     
    print("25th Percentile:", "\t", percentile.percentile(ordered_results, 0.25))
    print("50th Percentile:", "\t", percentile.percentile(ordered_results, 0.50))
    print("75th Percentile:", "\t", percentile.percentile(ordered_results, 0.75))
    print("90th Percentile:", "\t", percentile.percentile(ordered_results, 0.90))
    
    if full == 1:
        print("DAMAGE\t", "CONFIDENCE\t", "SPECIFIC")
        result_counter = 0
        while result_counter < max_result:
            if results[result_counter] != 0:
                ordered_index = ordered_results.index(result_counter)
                confidence = cycles - ordered_index
                print(result_counter, "\t", round(confidence / cycles * 100, 2), "%", "\t", round(results[result_counter] / cycles * 100, 2), "%")
            result_counter += 1
            
if foc > 0:
    print("*** Unboosted with",foc,"Focus ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc , 0)
    print("\n*** Boosted Attack with",foc,"Focus ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc , 1)
    print("\n*** Boosted Damage ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, foc , 2)
    print("\n*** Fully Boosted ***")
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg , foc , 3)
    
#     print("\n*** REFERENCE - SINGLE HIT ***")
#     calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, 0, 0)
    
else:
    calculate(cycles, attacks, at, pow, defense, arm, dice_hit, dice_dmg, 0, 0)


#     if __name__ == "__main__":
#         work_queue = multiprocessing.Queue()      
#         processes = [multiprocessing.Process(target=calculate, args=(cycles, i + 1, at, pow, defense, arm, dice_hit, dice_dmg, foc, 0)) for i in range(attacks)]
#         for p in processes:
#             p.start()
#         for p in processes:
#             p.join()
# if full == 1:
print(round(time.time() - start_time,2), "seconds")
