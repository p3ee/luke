import math 
import time 
mana = 100
energy = 100
health = 100
enemyhp = 250 
hppotion = 0
print ("here is your sword\n\n*You recived a diamond sword*\nskills:\nRegular Hit, 10 damage, 0energy, 0 mana\nThrow , 25 damage 10 energy, 20 mana\nMega Hit, 50 damage, 50 energy, 50 mana \n ")
time.sleep(1)
print("\n*you recived 25 health potions*")
hppotion += 25
time.sleep(0.5)
print("\ngood luck adventure")
input("press enter to begin ")
time.sleep(1)
print("A almighty sheep popped out the ground")
print("the sheep attacks but misses")
choice1 = str(input("what do you do\nattack\ninventory"))
if choice1 == ("attack"):
  attack1 = str(input("regualar hit\nthrow\nmega hit"))
  if attack1 == ("regualr hit"):
    enemyhp -=10
    print("You deal 10 damage to the sheep")
  elif attack1 == ("throw"):
    energy -=10
    mana -=20
    enemyhp -=25
    time.wait(1)
    print("attacking")
    time.wait(1)
    print("you deal 25 damage to the sheep")
  elif attack1 == ("mega hit"):
    energy -=50
    mana -=50
    enemyhp -=50
    print("you delt 50 damage to the sheep")
  else:
    print("you messed up and missed")
