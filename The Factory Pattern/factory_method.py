class A(object):
    pass


if __name__ == '__main__':
    a = A()
    b = A()
    print(id(a) == id(b))  ## False
    print(a, b)  ## <__main__.A object at 0x0060C4B0> <__main__.A object at 0x023F7510>
