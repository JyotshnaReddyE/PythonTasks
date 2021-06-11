#1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.

a , b , c = 1, 2.01, "string"
print(a)
print(b)
print(c)


#2. Create a variable of type complex and swap it with another variable of type integer.

x= 1+3j
y= 2
print("The value of x before swap =", x)
print("The value of y before swap =", y)
temp=x
x=y
y=temp
print("The value of x after swap =", x)
print("The value of y after swap =", y)


#3. Swap two numbers using a third variable and do the same task without using any third variable.

x= 10
y= 20
#using third variable
temp=x
x=y
y=temp
print("The value of x after swap =", x)
print("The value of y after swap =", y)
#without using third variable
x=30
y=40
x=x+y
y=x-y
x=x-y
print("The value of x after swap =", x)
print("The value of y after swap =", y)


#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

#Python 3.x
x=input("Enter a String")
print(x)

#Python 2.x
# y=raw_input("Enter a String")
# print(x)


#5. Write a program to complete the task given below:Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum inanother variable called z. Add 30 to z and store the output in variable result and print result as thefinal output.

x = int(input("Enter first number between 1-10:"))
y = int(input("Enter second number between 1-10:"))
z = x+y
print("z=",z)
result=z+30
print("Final output:", result)


#6. Write a program to check the data type of the entered values.

a=3
print("The data type of the input value is :", type(a))
b = 7.0
print("The data type of the input value is :", type(b))
c = 2 + 4j
print("The data type of the input value is :", type(c))
d= True
print("The data type of the input value is :", type(d))
e= "Hello"
print("The data type of the input value is :", type(e))


#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

Upper_CamelCase = " HelloWorld\n"
Lower_CamelCase = "helloWorld\n"
SnakeCase = "hello_world\n"
UPPERCASE = "HELLOWORLD\n"

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’again. Will it change the value? If Yes then Why?
a=3
a=4
print(a)

#Explanation: Yes the value will be changed and prints the one which you have entered last. when the value is assigned to a variable it stores that value and when you reassign it, old value moves out and it stores the new value.

print(Upper_CamelCase, Lower_CamelCase, SnakeCase, UPPERCASE)
