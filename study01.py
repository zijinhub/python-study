def addsum1(a,b=2,*args):
    sum=0
    print(type(args))
    print(len(args))

    for i in args:
        sum+=i
    return a+b+sum
s=addsum1(1,3,2,3,4)

print(s)

def addsum2(a,b,**args):
    print(type(args))
    pass

s2=addsum2(1,2)
print(s2)
'''*args和**kwargs: 都可以接受可变长度的参数个数 区别一个*是tuple元组类型，两个**是dict类型，
一个，一般约定一个*后面用args作为变量名，**后面用kwagrs表示'''

def addsum3(a,b,**aa):
    print(type(aa))
    pass

s3=addsum2(1,2)
print(s3)


def printInfo(a, c=4, *tup, **dic) :
    print(a)
    print(c)
    print(tup)
    print(dic)
#调用函数printInfo
printInfo(2,3,4,5, x=1, y=2)