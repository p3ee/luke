import math 
import time 
mana = 100
energy = 100
health = 100
enemyhp = 100
hppotion = 0
print ("here is your sword\n\n*You recived a diamond sword*\nskills:\nRegular Hit, 10 damage, 0energy, 0 mana\nThrow , 25 damage 10 energy, 20 mana\nMega Hit, 50 damage, 50 energy, 50 mana \n ")
time.sleep(1)
print("\n*you recived 25 health potions*")
hppotion += 25

print("\ngood luck adventure")
input("press enter to begin ")
time.sleep(1)
print("A almighty sheep popped out the ground")
print("the sheep attacks but misses")
choice1 = str(input("what do you do\n1.attack"))
if choice1 == ("1"):
  attack1 = str(input("1.regualar hit\n2.throw\n"))
if attack1.lower() == ("1"):
    enemyhp -=10
    print("attacking")
elif attack1.lower() == ("2"):
    energy -=10
    mana -=20
    enemyhp -=25
    time.sleep(1)
    print("attacking")
    time.sleep(1)
    print("you deal 25 damage to the sheep")
elif attack1 == ("3"):
    energy -=50
    mana -=50
    enemyhp -=50
    print("you delt 50 damage to the sheep")
else:
  print("you entered wrong enter in a th number corisponding to the attack ")
print("the sheep uses COOLDUDE and deals 10 damage to you")
health -=10
print("health:",health, "\nmana:",mana,"\nenemyhp:",enemyhp,)
time.sleep(1)
attack2 = str(input("1.regualar hit\n2.throw\n"))
if attack2.lower() == ("1"):
    enemyhp -=10
    print("attacking")
elif attack2.lower() == ("2"):
    energy -=10
    mana -=20
    enemyhp -=25
    time.sleep(1)
    print("attacking")
    time.sleep(1)
    print("you deal 25 damage to the sheep")
elif attack2 == ("3"):
    energy -=50
    mana -=50
    enemyhp -=50
    print("you delt 50 damage to the sheep")
    if enemyhp == 0:
      print("you have defeated the sheep")

if enemyhp >0:
  print("the sheep uses COOLDUDE and deals 10 damage to you")
  health -=10
print("health:",health,"\nmana:",mana,"\nenemyhp:",enemyhp)
time.sleep(1)
attack3 = str(input("1.regualar hit\n2.throw\n3.mega hit"))
if attack3.lower() == ("1"):
    enemyhp -=10
    print("attacking")
elif attack3.lower() == ("2"):
    energy -=10
    mana -=20
    enemyhp -=25
    time.sleep(1)
    print("attacking")
    time.sleep(1)
    print("you deal 25 damage to the sheep")
elif attack3 == ("3"):
    energy -=50
    mana -=50
    enemyhp -=50
    print("you delt 50 damage to the sheep")
    if enemyhp == 0:
     print("you have defeated the sheep")
