"""
PEP-8
"""

# todo Обьяснить типы

# обычный строчный комментарий
# some_variable: int = 1  # int целые числа
# home_number = 22
#
# mass: float = 22  # float число с дробным значением
# street_name = "Ленина 40 122131331"  # str строка
#
hello = int('22')
# mass2 = 344.55
#
# mass3 = mass + mass2
# mass4 = some_variable + mass2

"""
+
-
/
*
**
//
%
"""
this_year = 2020
# name = input('Ваше имя?\n>>>: ')
# surname = input('Ваша фамилия?\n>>>: ')
age = int(input('сколько вам лет?\n>>>: '))

# full_user_data = f'Приветсвие {name} {surname:<2} {this_year - age:^2} года рождения'
# print(full_user_data)

b_one = True
b_two = False

if age >= 18:
    print('Доступ везде включая XXXX')
    if age > 30:
        print('Пока все дома')
elif age >= 16:
    print('Доступ к контенту 16+')
elif age < 12:
    print('можно смотреть мультики')
else:
    print('Доступ к системе')

"""
if
elif
else
in
>
<
>=
<=
!=
not
and
or
"""
