#LABWORK1
print("Labwork1:")

#prac1
print("prac1:")

r = int(input("Enter circle radius: "))
print("Circle area:", 3.14 * r * r)


#prac2
print("prac2:")

c = float(input("Enter the temperature in Celsius: "))
print(c, "C =", (c * 9/5) + 32, "F")


#prac3
print("prac3:")

n = int(input("Enter a number: "))
if n % 1 == 0 and n % n == 0:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")


#prac4
print("prac4:")

p = int(input("Enter a number: "))
sum = 0
for i in range(1, int(p/2) + 1):
    if p % i == 0:
        sum += i
if sum == p:
    print(p, "is a perfect number." )
else:
    print(p, "is not a perfect number." )


#prac5
print("prac5:")

l = str(input("What is your favorite color? "))
list_of_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
if l in list_of_colors:
    print("Your favorite color is at index", list_of_colors.index(l), "in the list.")
else:
    print("Sorry, I couldn't find your color.")


#prac6
print("prac6:")

print("Range 1: ", end="")
for i in range(0, 7, 1):
    print(i, end=" ")

print("\nRange 2: ", end="")
for i in range(1, 11, 3):
    print(i, end=" ")

print("\nRange 3: ", end="")
for i in range(5, 0, -1):
    print(i, end=" ")

print("\nRange 4: ", end="")
for i in range(6, -3, -2):
    print(i, end=" ")

#prac7
print("\nprac7:")

def remove_dollar_sign(s):
    s = s.replace("$", "")
    return s
s = str(input("Type your string: "))
new_s = remove_dollar_sign(s)
print(new_s)


#prac8
print("prac8:")

list =[1, 4, 5, -1, 10]
new_list = []
def even(list):
    for k in list:
        if k % 2 == 0:
            new_list.append(k)
    return new_list
print(even(list))

#prac9
print("prac9:")

f = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(f))


#prac10
print("prac10:")

x = int(input("Enter a number: "))
def divisors(q):
    divisors_list = []
    for i in range (1, q + 1):
        if q % i == 0:
            divisors_list.append(i)
    return divisors_list
print(divisors(x)) 


#prac11
print("prac11:")

import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = x2 - x1
b = y2 - y1
d = math.sqrt(a**2 + b**2)
print("the distance between two points:", d ,round(d, 2))


#prac12
print("prac12:")

m, h = map(int, input().split())
for i in range(h): print("*", end =" ")
print("")
for i in range(m - 2):
    for j in range(h):
         if j == 0 or j == h-1: print("*", end =" ")
         else: print(end ="  ")
    print("")
for i in range(h): print("*", end =" ")

