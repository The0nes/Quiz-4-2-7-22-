import random
for u in range(3,21,+3):
    print(u)



print("Please enter a number")
num = int (input())
while num > 0:
    print("SNURFLE")
    num -= 1
    

def Monster():
    num1 = random.randrange(1,100)
    if num1 < 20:
        print("Husk")
    elif num1 < 50:
        print("Spider")
    elif num1 < 100:
        print("Skeleton")
        


print(Monster())
