my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

def find_the_average(a):
    avg = 0
    for x in a:
        avg = sum(a) / len(a)
        return avg

print(find_the_average(my_list))