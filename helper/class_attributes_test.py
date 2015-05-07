#!/bin/bash/env python

class MyObj:
    class_var = 1


if __name__ == '__main__':
    a = MyObj()
    print(a.class_var)    # 1

    b = MyObj()
    print(b.class_var)    # 1

    b.class_var = 10      # create a instance variable named 'class_var' for b

    print('')             

    print(a.class_var)    # 1
    print(b.class_var)    # 10
    print(MyObj.class_var)# 1

    print('')

    MyObj.class_var = 3   # change class attribute affect instance a, but not b

    print(a.class_var)    # 3
    print(b.class_var)    # 10
    print(MyObj.class_var)# 3

    print(a.__dict__)
    print(b.__dict__)
    print(MyObj.__dict__)
