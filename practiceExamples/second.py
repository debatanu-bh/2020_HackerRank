import cmath

# a=['2','3','5','1','2','6','7','8']
# b=[]
# numbers = [ 1 , 3 , 4 , 2 ]
#
# numbers.sort()
#
# print(numbers)
# print(numbers[-2])

# if __name__ == '__main__':
#     numbers=[]
#     n = int ( input ( ) )
#     arr = map ( int, input ( ).split ( ) )
#     numbers=arr
#     # numbers.sort()
#     print ( numbers )
# c=1+2j
# modulus = abs(c)
# phase = cmath.phase(c)
# polar = cmath.polar(c)
#
# print( modulus)
# print(phase)
# # print('Polar Coordinates =', polar)

# print('Rectangular Coordinates =', cmath.rect(modulus, phase))




# r=int(input())
# for i in range(1,r+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#    # print(i)
#    # print ( [0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i] )
#    # print(pow(((pow(10,i)-1)//9),2))
#    print(i*((  10**i - 1 )//9))


sum=0
a=int(input())
b=int(input())
c=int(input())
d=int(input())

sum=(pow(a,b))+(pow(c,d))
print(sum)



import itertools

(K, N) = map(int, input().split())

L = list()
for i in range(K):
    l = map(int, input().split())
    n = l[0]
    L.append(l[1:])
    assert len(L[i]) == n

S_max = 0
L_max = None

for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print (S_max)