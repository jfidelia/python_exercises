arr = [45, 67, 87, 23, 5,  32, 60]
new_list = []
#your code below:
for x in range(len(arr) - 1, -1, -1):
    new_list.append(arr[::-1])

print(new_list[x])