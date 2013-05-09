import random
def roll_hit(at, defense, dice_hit):
   i = 0
   result = 0
   while i < dice_hit:
      i += 1
#      print(result)
      result = result + random.randrange(1, 7, 1)
      #    print(result)
   auto_check = result / dice_hit
   if auto_check == 1:
       return(0)
   elif auto_check == 6:
       return(1)
   elif at + result >= defense:
      return(1)
   else:
      return(0)

def roll_dmg(pow, arm, dice_dmg):
   i = 0
   result = 0
   while i < dice_dmg:
      i += 1
#      print(result)
      result = result + random.randrange(1, 6, 1)
#    print(result)
   if pow + result > arm:
      return(pow + result - arm)
   else:
      return(0)
  
def roll_full(at, pow, defense, arm, dice_hit, dice_dmg):
    hit_result = roll_hit(at, defense, dice_hit)
    if hit_result == 1:
        dmg_result = roll_dmg(pow, arm, dice_dmg)
        return(dmg_result)
    else:
         return(0)
