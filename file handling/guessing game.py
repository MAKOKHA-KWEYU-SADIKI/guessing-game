import random
gues=0
count=0
l=1
u=20
correct=random.randint(l,u)
while count<5:
    gues=int(input("enter the number: "))
    if gues>correct:
       print("too large")
    elif gues<correct:
       print("too small")
    else:
      print("conratulations you made it")
      break  
    atempt_left=5-count-1
    print(f"{atempt_left} attempt left")
    count=count+1     
if count==5:
   print("out of attemp")
   
   
     
