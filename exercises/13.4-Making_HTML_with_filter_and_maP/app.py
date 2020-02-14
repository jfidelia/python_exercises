all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(items):
    return items["sexy"] == True
new_list = list(filter(filter_colors, all_colors))


def generate_li(item):
    return "<li>" + item["label"] + "</li>"



array_of_lis = list(map(generate_li,new_list))

string_of_lis = ''.join([str(elem) for elem in array_of_lis]) 

print("<ul>"+string_of_lis+"</ul>")


    #
# html = list(map(lambda color: "<ul><li>" + color["label"] + "</li><li>", all_colors))
# print(html)