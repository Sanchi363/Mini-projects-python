import random
print("!Start!")
print("User selects the number given before the element to select it")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
a=int(input("Enter the number for the element you selected:"))
if(a==1):
    b="Rock"
elif(a==2):
    b="Paper"
else:
    b="Scissors"
print(f"You selected {b}")            
l=["Rock","Paper","Scissors"]
m=(random.choice(l))
print(f"Computer selected {m}")
print(f"{b} V/s {m}")
if(b==m):
    print("Game draw!!!")
elif(b=="Rock"):
    if(m=="Paper"):
        print("You lost!!😞")
        print("Better try next time👍")
    else:
        print("Hurray! You won!🥳🎆")
elif(b=="Paper"):
    if(m=="Rock"):
        print("Hurray! You won!🥳🎆")
    else:
        print("You lost!!😞")
        print("Better try next time👍")
else:
    if(m=="Rock"):
        print("You lost!!😞")
        print("Better try next time👍")   
    else:
        print("Hurray! You won!🥳🎆")          