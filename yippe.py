secretnumber=9
guess=0
limit=3
while guess<limit:
    guess2=int(input("Guess (1 through 10):"))
    guess += 1
    if guess2 == secretnumber:
        print("You won!")
        break
else:
    print("You failed.")