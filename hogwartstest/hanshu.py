"""
1.没有返回值的函数，返回值为NONE

"""


def test():
    print('a')


print(test())

"""
2.有返回值的函数,t的值为11
"""


def test1(a):
    return a


t = test1(11)
print(t)
"""

3.return语句不带参数，返回值为NONE
total的值为NONE
"""


def test2(a, b):
    total = a + b
    return


total = test2(1, 2)
print(total)
"""
4.有参数的函数
"""


def test3(a):
    return a


print(test3(10))
