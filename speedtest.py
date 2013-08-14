from random import randrange, randint, choice, sample, random, uniform
import time

start_time = time.time()

iterations = 6000000

# range = [1, 2, 3, 4, 5, 6]
#  
# loop_range = 0
# tally = 0
# start_range = time.time()
# while loop_range < iterations:   
#     out = randrange(1, 7, 1)
#     loop_range += 1
#     tally = tally + out
# print(tally / iterations, "randrange", round(time.time() - start_range, 2), "seconds") 
#  
# loop_int = 0
# tally = 0
# start_int = time.time()
# while loop_int < iterations:
#     out = randint(1, 6)
#     loop_int += 1
#     tally = tally + out
# print(tally / iterations, "randint", round(time.time() - start_int, 2), "seconds")
#  
# loop_choice = 0
# tally = 0
# start_choice = time.time()
# while loop_choice < iterations:
#     out = choice(range)
#     loop_choice += 1
#     tally = tally + out
# print(tally / iterations, "choice", round(time.time() - start_choice, 2), "seconds")
# 

loop_random = 0
tally = 0
start_random = time.time()
while loop_random < iterations:
    out = int(random() * 6) + 1
    loop_random += 1
#     tally = tally + out
print(tally / iterations, "random", round(time.time() - start_random, 2), "seconds")
 
loop_random = 0
tally = 0
start_random = time.time()
while loop_random < iterations:
    out = int(random() * 6) + 1
    loop_random += 1
    tally = tally + out
print(tally / iterations, "random", round(time.time() - start_random, 2), "seconds")
#  
# loop_uniform = 0
# tally = 0
# start_uniform = time.time()
# while loop_uniform < iterations:
#     out = int(uniform(1, 7))
# #     print(int(uniform(1,7)))
#     loop_uniform += 1
#     tally = tally + out
# print(tally / iterations, "uniform", round(time.time() - start_uniform, 2), "seconds")
#   
# print("runtime:", round(time.time() - start_time, 2), "seconds")

results = [0] * 7
 
loop_random = 0
tally = 0
start_random = time.time()
while loop_random < iterations:
    out = int(random() * 6) + 1
    loop_random += 1
    tally = tally + out
    results[out] += 1
print(tally / iterations, "random", round(time.time() - start_random, 2), "seconds")
print(results)
