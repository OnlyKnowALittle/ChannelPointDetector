#Button Pusher - Random Digits Generator
import random

#Our PassCode - Will be given 8 random numbers
NewPassCode = []

def NewCode():
    #Get 8 numbers
    for i in range(1,8):
        #Add four random numbers to PassCode
        NewPassCode.append(random.randrange(0,4))
        
NewCode()
print("New Passcode:")
print(NewPassCode)

""""
#Much more efficient - https://www.tutorialspoint.com/generating-random-number-list-in-python
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
print(randomlist)
"""