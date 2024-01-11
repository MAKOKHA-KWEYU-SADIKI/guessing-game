import random
gues=0
count=0
correct=random.randint(1,10)
while count<5:
    gues=int(input("enter the number within the range 1-10: "))
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
   
   
     
