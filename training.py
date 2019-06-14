

a = [1,2,3,4,5]

b = [n ** 2 for n in range(10) if n % 2 == 0]

c = {n: n ** 2 for n in range(10)}

d = (n ** 2 for n in range(10))


def ania_decorate(func):
    def wrapper(name):
        return "<p> {} <p>".format(name)
    return wrapper

@ania_decorate
def print_cos(input_):
    return input_


def generation(n:int):
    for i in range(n):
        yield i

diction = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e'
}

myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)

aaa = {}
aaa[myTuple] = 5



g,*h,i = [1,2,3,4,5]


_, _, _ = [1, 2, 3]


def fibb(n):
    a,b = 0,1
    i=0
    while n>1:
        a, b = b, a+b
        n -= 1


def foo(n,list=[]):
    for i in range(n):
        list.append(i*i)
    print(list)
foo(1)
foo(3,[1,2,3])
foo(2)

