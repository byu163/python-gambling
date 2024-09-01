import random
import sys
import time
numbers = ["1","2","3","4","5","6","7","8","9","0"]
gameloop=True
lottery = None
randoms = None
balance = 500
price = 10
while gameloop == True:
    def chooseNumbers():
        global lottery
        num1=random.choice(numbers)
        num2=random.choice(numbers)
        num3=random.choice(numbers)
        lottery=str(num1+num2+num3)
        if lottery == "0":
            chooseNumbers()
        if num1=="0":
            lottery=str(num2+num3)
        if num1 + num2 == "0":
            lottery=str(num3)
    def check():
        if randoms == lottery:
            print("YOU WIN!!!")
            lotteryVal = int(lottery)
            balance + lotteryVal
        else:
            print("You lost >:) Better luck next time.")
            gambleCore()
    def roll():
        chooseNumbers()
        print("Welcome to the slot machine. Please roll 3 times.")
        maininput = input().lower()
        if maininput == "roll":
            r1=random.choice(numbers)
            r2=random.choice(numbers)
            r3=random.choice(numbers)
            randoms=str(r1+r2+r3)
            if r1 == "0":
                randoms=str(r2+r3)
            if r1+r2 == "0":
                randoms=str(r3)
            if randoms == "0":
                roll()
            print("Your number is " + randoms +". Would you like to reroll?")
            input0=input().lower()
            if input0 == "yes":
                r1=random.choice(numbers)
                r2=random.choice(numbers)
                r3=random.choice(numbers)
                randoms=str(r1+r2+r3)
                if r1 == "0":
                    randoms=str(r2+r3)
                if r1+r2 == "0":
                    randoms=str(r3)
                if randoms == "0":
                    print("You landed a zero and lost. Better luck next time. >:)")
                    return
                check()
            if input0 != "yes":
                check()
    def gambleCore():
        global balance
        if balance < 10:
            brokeBoy()
        if balance >= 10:
            print("Your balance is $" + str(balance))
            print("Please insert $10 to play.")
            inputs = input().lower()
            if inputs == "no":
                print("KILL HIM")
                print("Game Over. You died.")
                time.sleep(5)
                sys.exit()
            if inputs != "no":
                balance -= price
                roll()
    if balance >= 1000:
        print("Wow. Impressive. YOU WIN!!! GET OUT OF HERE! GO BACK TO YOUR WIFE AND 3 KIDS STUPID SCAMMER! NEVER COME BACK! YOU CHEATED THE SYSTEM. BYE.")
        print("You win. Good Ending?")
        time.sleep(30)
        sys.exit()
    def brokeBoy():
        if balance <= 10:
            print("KILL HIM FOR BEING BROKE!!")
            print("You died from being broke in a casino.")
            time.sleep(10)
            sys.exit()
    gambleCore()
