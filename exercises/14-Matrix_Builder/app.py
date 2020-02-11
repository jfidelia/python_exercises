import random

#Create the function below:
def matrixBuilder(number):
    item = []
    
    for i in range(number):
        item.append([])
        for j in range(number):
            item[i].append(random.randint(0,1))
    return item


print(matrixBuilder(3))
    
    




    

