theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def number(a):
    if a == 1:
        return("wiki")
    else:
        return("woko")
new_list = list(map(number, theBools))
print(new_list)
