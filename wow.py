# from fractions import Fraction
#
# a = Fraction(4) ** Fraction(2)
# b = Fraction(4) ** Fraction(1, 2)
#
# print(type(a).__name__, type(b).__name__)

# class A:
#     value = 0
#
# class B(A):
#     pass
#
# b = B()
# b.value = 1
# c = B()
#
# print(c.value)

# f = open('text_300.txt', 'w')
# if f:
#     print(0)
# f.close()
# if f:
#     print(1)
# else:
#     print(2)

# def generator():
#     yield from (x for x in range(3))
#     yield from (x for x in range(3, 6))
#
# for i in generator():
#     print(i)

# dictionary = dict(one=1, two=2)
# keys = dictionary.keys()
# dictionary['three'] = 3
# print(keys)

from functools import wraps


def val_checker(l_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')
        return wrapper
    return  _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-4)