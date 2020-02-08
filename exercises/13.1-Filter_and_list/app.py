
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def my_function(letters): 
    return letters == all_names[0]

resulting_names = list(filter(my_function, all_names))
print(resulting_names)




