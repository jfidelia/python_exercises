def lyrics_generator(beat):
    items = []

    count = 0
    for x in beat:
        if x == 0:
            count = 0
            items.append("Boom")
        if x == 1:
            count = count + 1
            items.append("Drop the base")
        if count == 3:
            items.append("!!!Break the base!!!")
    return ' '.join([str(elem) for elem in items])
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))