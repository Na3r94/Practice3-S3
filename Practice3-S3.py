import random

n = int(input())

x = []
y = 0

while True:

    a = random.randint(1, 1000)

    if a in x:
        y += 1
        print "Tekrari" , y , a

    else:
        x.append(a)
            
        n -= 1
        if n == 0:
            break



print(x)