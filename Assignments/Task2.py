#1
number=int(input("Enter a number:"))
if(number%3==0 and number%5==0):
    print("Consultadd-Python Training")
elif(number%3==0):
    print("Consultadd")
elif(number%5==0):
    print("Python Training")
else:
    print("Number is not divisible by either 3 or 5")
    

#2
def getInput():
    num1=int(input("Enter a number="))
    num2=int(input("Enter a number="))
    return num1,num2
def Addition():
    a,b=getInput()
    output= a + b
    return output
def Subtraction():
    a, b = getInput()
    output= a - b
    return output
def Division():
    a, b = getInput()
    output= a // b
    return output
def Multiplication():
    a, b = getInput()
    output = a * b
    return output
def Average():
    a, b = getInput()
    first = int(input("Enter first number="))
    second = int(input("Enter second number="))
    output = (a + b + first + second) / 4
    return output

print('''  
       1. Addition
       2. Subtraction
       3. Division
       4. Multiplication
       5. Average
''')
entry = int(input("Choose operation you want to perform::"))
operations = {
       1: Addition,
       2: Subtraction,
       3: Division,
       4: Multiplication,
       5: Average
}
output = operations.get(entry)()
print("Result is =" , output)
if(output<0)  :
    print("NEGATIVE")
    

#3
a=10
b=20
c=30
avg=(a+b+c)/3
print("avg=", avg)
if(avg>a and avg>b and avg>c):
    print("avg is higher than a,b,c")
elif(avg>a and avg>b):
    print("avg is higher than a,b")
elif(avg>a and avg>c):
    print("avg is higher than a,c")
elif(avg>b and avg>c):
    print("avg is higher than b,c")
elif(avg>a):
    print("avg is just higher than a")
elif(avg>b):
    print("avg is just higher than b")
elif(avg>c):
    print("avg is just higher than c")
else:
    print("Negative")
    

#4
while True:
    a = int(input("Enter a number="))
    if a>0:
        print("Going Good")
    elif a < 0:
        break
print("It's Over")


#5
for i in range(2000, 3200):
    if i%7==0 and i%5!=0:
        print(i)
        
#6
x=123
for i in x:
    print(i)

#output:
'int' object is not iterable

i=0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

#output:
0
error
1
error
2


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break

#output:
0
1
2
3
4


#7
for i in range(6):
    if(i==3 or i==6):
        continue
    print(i, end='')

    
#8
a=str(input("Enter a String::"))
letters=digits=0
for i in a:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1
    else:
        pass
print("Letters", letters)
print("Digits", digits)


#9
number = input("Guess the lucky number ")
while number != 7:
    print("That is not the lucky number")
    number = input("Guess the lucky number ")

number;
answer = "yes"
while number == 7 and answer == "no":
    number = input("Guess the lucky number: ")
    if number != 7:
        print("That is not the lucky number")
        again = input("Would you like to guess again? ")
        
#10
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if (number==7):
       print("Good guess!")
   else:
       print("Try again.")
   counter = counter +1
else:
   print("Game over")
    
    
#11
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 7:
       print("Try again.")
   else:
       print("Good guess!")
       break
   counter = counter +1
else:
   print("Sorry but that was not very successful")
