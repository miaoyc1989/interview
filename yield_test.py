#!/usr/bin/python
# encoding:utf-8


def Iterables():
    mylist = [x * x for x in range(3)]
    for i in mylist:
        print(i)


def Generators():
    mygenerator = (x * x for x in range(3))
    for i in mygenerator:
        print(i)


def Yield():
    def createGenerator():
        mylist = range(3)
        for i in mylist:
            yield i * i
    mygenerator = createGenerator()  # create a generator
    print(mygenerator)  # mygenerator is an object!
    for i in mygenerator:
        print(i)


if __name__ == "__main__":
    print "Iterables()"
    Iterables()

    print "Generators()"
    Generators()

    print "Yield()"
    Yield()

