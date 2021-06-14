#Question 1:
List = [37, 77, "Python", "Training", 3.5, 9.7, True, False, 1+2j, 3+7j]
print(List)

# Question 2:
List = [10,20,30,40,50]
print(List)
# selecting the items in the specified range with start and stop
print(List[2:4])
# selecting the items while omitting stop.
print(List[2:])
# selecting the items while omitting start.
print(List[:4])

#Question 3:
import math

List = [3,5,7,9,77,2]
result = sum(List)
print("Sum of all the elements in list =" ,result)
result1 = math.prod(List)
print("Multiplication of all the elements in list =" ,result1)

#Question 4:
List = [20, 77, 35, 2, 7,9]
print("Smallest Element is=", min(List))
print("Largest Element is=", max(List))

#Question 5:
List = [20, 77, 35, 2, 7,9]
Newlist = [ele for ele in List if ele%2!=0]
print(Newlist)

#Question 6:
def squares():
    l = list()
    for i in range(1,31):
     l.append(i**2)
    print(l[:5])
    print(l[-5:])
squares()

#Question 7:
List1 = [1,3,5,7,9,10]
List2 = [2,4,6,8]
List1[-1:] = List2
print(List1)

#Question 8:
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

#Question 9:
n=int(input("Enter how many numbers you want in dictionary="))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)

#Question 10:
elements = input("Enter some comma seperated numbers :")
list = elements.split(",")
tuple = tuple(list)
print('List :', list)
print('Tuple :', tuple)
