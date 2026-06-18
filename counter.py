counter = 1

def incrementCount(): 
    counter += 1

def decremntCount():
    if(not counter > 0):
        counter -= 1

    return counter

def divide(n, m):
    return n // m

print(divide(4,2))