import random
number=random.randint(1,100)
guess=0
print("Let's begin the game!!")
while(guess!=number):
    guess=int(input("Enter a number between 1 to 100:"))
    if(guess>number):
        print("Enter a lower value")
        # guess=guess+1
    elif(guess<number):
        print("Enter a higher value")
        # guess=guess+1
    else:
        print('''!!You guessed  it right!!
  Congradulations''')
