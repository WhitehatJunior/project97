import random
randNum = random.randint(1,9)
print("Number guessing game")
print("Guess a number (between 1 9)")
chances=0
while chances < 5:
    guess = int(input("Enter your guess: - "))
    if(guess<randNum):
        print("Your guess was too low: Guess a number higher than",guess)
    elif(guess>randNum):
        print("Your guess was too high: Guess a number lower than",guess)
    elif(randNum==guess):
        print("CONGRATULATIONS YOU WON!!!")
        break
    chances+=1
if not chances<5:
    print("YOU LOSE!!! The number is", randNum)