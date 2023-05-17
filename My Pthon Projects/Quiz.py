print("Hi Lets Start Quiz Game")
play = input("Do You want to Play Quiz Game: ")

if play != "yes":
    print("Game Over")
    quit()
    
else:
    print("Lets Start The Game")
    
score = 0

# 1     
answer = input("What is the name of National Bird : ")
if answer.lower() == "peacock":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")
    
# 2     
answer = input("What country has won the most World Cups? : ")
if answer.lower().lower() == "brazil":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")
    
# 3     
answer = input("How many bones do we have in an ear? : ")
if answer.lower() == "3":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer") 
    
# 4     
answer = input("What Netflix show had the most streaming views in 2021? : ")
if answer.lower() == "squid game":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer") 
    
# 5    
answer = input("What software company is headquartered in Redmond, Washington? : ")
if answer.lower() == "microsoft":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer") 
    
print("So Here Are The Results : " + str(score))
print("Hope You Enjoyed")
quit()