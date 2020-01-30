chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:]
    new_list = []
    for x,y in range(0, len(chunk_one), len(chunk_two), 1):
        new_list.append(chunk_one,chunk)

    return new_list
print(merge_list(chunk_one, chunk_two))
