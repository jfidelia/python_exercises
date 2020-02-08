list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(item):
        return type(item)

new_list = map(type_list, list_Strings)
print(list(new_list))