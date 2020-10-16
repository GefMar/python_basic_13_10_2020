var_int = 1
var_str = 'СТРОКА'  # итерируемые
var_bool = True
var_float = 12.234

"""
Изменяемые
Не изменяемые
"""

# Коллекции итерируемые
var_list = [1, 2, 'hello', 'world', True, ]  # список изменяемый
var_tuple = (1, 2, 'hello', 'world', True,)  # не изменяемый
var_set = {1, 2, 3, 4, 5, 5, 5, 6, 7}  # множество изменяемо
var_frozenset = frozenset({1, 2, 3, 4, 5, 5, 5, 6, 7})  # множество не изменяемо

user = {'name': 'serg', 'surname': 'rom'}

users = [user, {'name': 'serg', 'surname': 'rom'}, {'name': 'fhfgj', 'surname': 'fhgfgf'},
         {'name': 'bill', 'surname': 'g'}]

test = {
    'a': 2,
    'b': 3,
    'c': 4,
    'd': 5,
}

for item in test:
    print(item)

# while True:
#     user_template = {}
#     user_template['name'] = input('name')
#     user_template['surname'] = input('surname')
#     users.append(user_template)
#     q = input('out?')
#     if q == 'q':
#         break

# for item in users:
#     if item['name'].islower():
#         item['name'] = item['name'].title()
# print(users)

# users.append(user)
#
# users[0]['name'] = 'SOME'
#
# print(user)
# print(users)
