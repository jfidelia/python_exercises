arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
total= 0
def sumOdds(odd):
    for x in range(0, len(odd), 1):
        if x % 2 != 0:
            total += odd[x]
    return (total)

print(sumOdds)
