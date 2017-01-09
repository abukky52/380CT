from random import randint
import time
import random

def randoma(n):
    li = []
    for f in range(n):
        o = random.randrange(1,100,1)
        li.append(o)
    li = sorted(li)
    li.reverse()
    print (li)
    return li

def greedy(n):
    solution = []
    target = random.randrange(1,100,1)
    print ("target: ", target)
    li = randoma(n)
    print (li)

    for i in li:
        if i <= target:
            target = target - i
            solution.append(i)
            print ("solution: " , solution , sum(solution))
    return solution

start_time = time.time()
print (greedy(34))
a = time.time() - start_time
print("---%s seconds ---" % (a))
