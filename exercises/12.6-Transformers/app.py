incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
transformedData = list(map(lambda person: person["name"] + " " + person["lastName"] + ",", incomingAJAXData))
def names(a):
    return a
print(' '.join([str(elem) for elem in transformedData]))

