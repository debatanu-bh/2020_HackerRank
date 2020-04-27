import re


def mapping(x,y):
    print( "====MAP----")

    # lambda arguments: expression
    # x=int(input())
    # y=int(input())
    s=str(lambda x,y:x+y)
    return s


print(mapping(2,3))

def mapper(n):
    return n*n
a=[1,3,5,6,7,8]
print(list(map(mapper,a)))
numbers=(7,9,89,76,88,54)
print(list(map(lambda a:a,numbers)))
print(list(map(lambda a:a*a,numbers)))
# print()


import email.utils
print (email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
print (email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))
a=[]


def run(string):
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile ( '[@_!#$%^&*()<>?/\|}{~:]' )

    # Pass the string in search
    # method of regex object.
    if (regex.search ( string ) == None):
        print ( "String is accepted" )

    else:
        print ( "String is not accepted." )


n=int(input())
for i in range(0,n):
    b=input()
    a.append(b)

for g in a:
    # print (g)
    # user=g.split("@)")
    print(user)
    test=g.split(".")
    # print(len(test[1]))
    if(len(test[1]))==4:
        print(g)
# print(a)



