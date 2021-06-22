#1 Question
def reverse(str):
    reversestr = ''
    index = len(str)
    while index>0:
        reversestr += str[index-1]
        index = index-1
    return  reversestr
print(reverse('1234abcd'))

#2 Question
string=input("Enter string:")
lowercount=0
uppercount=0
for i in string:
      if(i.islower()):
            lowercount=lowercount+1
      elif(i.isupper()):
            uppercount=uppercount+1
print("The number of lowercase characters is:", lowercount)
print("The number of uppercase characters is:", uppercount)

#3 Question
def unique_list(l):
  x = []
  for i in l:
    if i not in x:
      x.append(i)
  return x

print(unique_list([1,2,2,3,3,3,4,5]))

#4 Question
string=input("Enter the String :")
newstring=string.split('-')
newstring.sort()
print('-'.join(newstring))

#5 Question
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

#6 Question
def calculateSum (a,b):
	s = int(a) + int(b)
	return s
num1 = "10"
num2 = "20"
sum = calculateSum (num1, num2)
print("Sum = ", sum)

#7 Question
str1=input("Enter first string:")
str2=input("Enter second string:")
a=len(str1)
print("Length of first string", a)
b=len(str2)
print("Length of second string", b)
if a>b:
    print(str1)
elif b>a:
    print(str2)
else:
    print(str1)
    print(str2)

#8 Question
l=list()
for i in range(1,21):
    l.append(i**2)
print(l)

# 9 Question
def shownumber(limit):
    for i in range(0, limit):
        if i==0:
            print(i,end=" ")
            print("EVEN")

        elif i%2==0:
            print(i,end=" ")
            print("EVEN")

        else:
            print(i,end=" ")
            print("ODD")
print(shownumber(4))

# 10 Question
list1 = [1, 2, 3, 4, 5]
is_even = lambda x: x % 2 == 0
list2 = list(filter(is_even, list1))
print(list2)


#11 Question
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eve_num = map(lambda x:x**2, filter(lambda x:x%2==0, list))
print(eve_num)

#12 Question
try:
    x = 5 / 0
except:
    print("Error dividing by zero")

#13 Question
import operator
from functools import reduce
if __name__ == '__main__':
    lists = [[1, 2, 3], [4, 5], [6, 7]]
    joinedlist = reduce(operator.add, lists)

    print(joinedlist)

#14 Question
def result(N):
    for num in range(N):
        if num % 3 != 0 and num % 7 == 0:
            print(str(num) + " ", end="")
        else:
            pass
if __name__ == "__main__":
    N = 100
    result(N)

#15 Question
def multiplication(n):
    return n * n
numbers = (1, 2, 3, 4)
result = map(multiplication, numbers)
print(list(result))


#16 Question
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#output : 2

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

#output :
# First it shows error since f is not defined in try block.
# For finally block, it prints after f and after f?
