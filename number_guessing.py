import random
print("WELCOME TO NUMBER GUESSING GAME")
print("Select Difficulty Level:")
print("1.Easy(1-50)")
print("2.Medium(1-100)")
print("3.Hard(1-500)")
choice=int(input("Enter Choice(1/2/3):"))
if(choice==1):
    max=50
elif(choice==2):
    max=100
elif(choice==3):
    max=500
else:
    print("Invalid choice, defaulting to Easy level")
    max=50
number=random.randint(1,max)
attempt=0
while True:
    guess=int(input(f"enter you guess between 1 and {max}:"))
    attempt+=1
    if(guess<number):
        print("Too low! Try again")
    elif(guess>number):
        print("Too high! Try again")
    else:
        print("Congratulations!! you guessed correct number in",attempt,"attempts")
        break