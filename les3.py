"""
ДЗ Любую встроенную функцию перед использованием надо написать
map
zip
reduce
sorted
max
min
sum
range
round
divmod
"""

a = [1, 2, 3, 4]
z = 22


def some(x):
    return x ** 3



def my_map(funk, iter_obj):
    print('SOME 1')
    for itm in iter_obj:
        print('SOME 2')
        yield funk(itm)
        print('SOME 3')
        yield f'HELLO {itm}'
    print('SOME 4')


def some_f(x):
    z = x
    return z


def some_zip(*some, **home):
    """Эта функция что-то делает я опишу это
    :param some: параметры которые принимает
    """
    print(some)


# for itm in my_map(some, [1, 2, 3, 4, 5, 6]):
#     print('Cycle 1')
#     print(itm)
#     print('Cycle 2')

# some_list = [1, 2, 3, 4, 5]
# some_iter = some_list.__iter__()
# while True:
#     try:
#         itm = next(some_iter)
#         print(itm)
#     except StopIteration:
#         break
#
# for itm in some_list:
#     print(itm)

# l_some = lambda x: \
#     x ** 3


some_list = [1, 2]


def some_indexer(index, iter_object):
    try:
        print(iter_object[index])
        return iter_object[index]
    except IndexError:
        pass
    except ValueError:
        pass
    except KeyError:
        pass
    finally:
        print('ФИНАЛ')


idx = 0
while idx < 10:
    print(idx)
    if idx == 6:
        break
    idx += 1
else:
    print('END CYCLE')

for itm in range(10):
    print(itm)
else:
    print('END CYCLE')

# some_indexer(1, some_list)
