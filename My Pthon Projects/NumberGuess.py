import random

top = input("Type a Number: ")

if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Type a number larger than zero")
        quit()
else:
    print("Type a Number Not a Alphabet,Symbol")
    quit()
    
random_num = random.randint(0, top)
Guess = 0

while True:
    Guess += 1
    user_num = input("Guess a number: ")
    if user_num.isdigit():
        user_num = int(user_num)
    else:
        print("Guess Another Number")
        continue
    
    if user_num == random_num:
        print("You Have Guess The Correct Number")
        break
    
    elif user_num > random_num:
        print("Take Larger Number")
        
    else:
        print("Take Smaller Number")    
        
print("Total Guess :", Guess)    
        