import math 
import time 
input("press enter to start")
fclasspassenger = int(input("How many people are going First Class?:"))
if fclasspassenger > 950 :
# increase number above by 95 to add 1 more carriage 
   print ("This number is invalid, the maxium number of passengers is 950")
   time.sleep(1)
   print("please restart the programme")
else:
  sclasspassengers = int(input("How many people are going Second Class:"))
if sclasspassengers+fclasspassenger > 950 :
  print ("This number is invalid the maximum number of passengers is 950")
else:
  time.sleep(1)
  print(">>><>>CALCULATING<<><<<")
  fclassprice = 5
  sclassprice = 3.5 
  fclasstotal = (fclasspassenger*fclassprice)
  sclasstotal = (sclasspassengers*sclassprice)
  print("The amount of money from First Class is: \n £",fclasstotal)
  print("The amount of money from Second Class is: \n £",sclasstotal)
  total = (fclasstotal+sclasstotal)
  print("The over all total is: \n £",total)
continueanswere = str(input("would you like to know how many carages you will need?  y/n:"))
if continueanswere == ("y"):
   maxcarridge = 95
   print ("you will have",fclasspassenger//maxcarridge,"First Class carrages")
   print ("you will have",sclasspassengers//maxcarridge,"Second Class carrages")
   print ("In total there will be",(fclasspassenger//maxcarridge)+(sclasspassengers//maxcarridge),"carrages")
   ahhhbigscaryman = str(input("would you like to find the total income from the train?  y/n:"))
   if ahhhbigscaryman == ("y"):
     engine = 800
     carrage = 125
     totalcarrige = int(input("Please enter the total number of carrages given to you prior:"))
     print("The cost for the train is \n £",engine+(totalcarrige*carrage))
     trainprofit = total-(engine+(totalcarrige*carrage))
     print("The over all profit is \n£",trainprofit)
   else:
     print("press enter to finish")
else:
  print("press enter to finish")
