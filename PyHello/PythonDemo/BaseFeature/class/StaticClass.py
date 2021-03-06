﻿class A:
    a1 = 1
    __MyPrivate = 10
    _MyPrivate = 20

    def __init__(self, a2):
        self.a2 = a2

    def setData(self, a3):
        self.a3 = a3

    def show(self):
        print('A1:%s,a1:%s,a2:%s,a3:%s' % (A.a1, self.a1, self.a2, self.a3))

    @staticmethod
    def showMyPrivate():
        print('__MyPrivate:%d ' % (A.__MyPrivate))


if __name__ == '__main__':
    c1 = A(1)
    print(c1.a1)
    print(A.a1)
    c1.a1 = 2
    print(A.a1)
    A.a1 = 3
    A.a2 = 3

    obj1 = A(1)
    obj2 = A(2)
    obj3 = A(3)

    obj1.setData(1)
    obj2.setData(2)
    obj3.setData(3)

    obj1.a1 = 1
    obj2.a1 = 2
    obj3.a1 = 3

    A.a1 = 1
    A.a2 = 2
    A.a3 = 3
    obj1.show()
    obj2.show()
    obj3.show()
    print('A1:%s,A2:%s,A3:%s' % (A.a1, A.a2, A.a3))
    # print('__MyPrivate:%d,_MyPrivate:%d' % (A.__MyPrivate, A._MyPrivate))  A.__MyPrivate在类的外部无法访问
    print('__MyPrivate:%d,_MyPrivate:%d' % (A._MyPrivate, A._MyPrivate))
    A.showMyPrivate()
