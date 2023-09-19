x = 10
nev = "Béla"
nev_empty = ""
print('Hello ' + nev)
str(10)
print(x)
x = "Uj"
print(x, type(x))
x = 3.14E-2
z = 6.66
print(x, type(x))
x = 1 + 4j
print(x, type(x))
num = 1 / 3
#print("num=(0)".format(num))
#print('num=(0.2f)'.format(num))

h = 2 + 4j
k = 5 + 1j
l = 6 + 7j
com1 = h * k
print(com1)
print("alma", end="")
print("dinnye")
print("eper")
"""
#var_a=input()
for i in range(0,11,2):
    print(i)

for i in range(10,-1,-1):
    print(i)

i=0
while i<=10:
    print(i)
    i=i+1

i=0
while True:
    print(i)
    if i==1:
        break #to not be inf.loop
    i=i+1

"""
x = range(5, 10)
for i in x:
  print(i)

li = [1, 2, 3, 4, 5]
for j in li:
  print(j)

nev = ["Anna", "Bela", 1, 3, True]
for i in nev:
  print(i)

a = input("Egész szám:")

if a % 2 == 0:
  print('{} páros'.format(a))
else:
  print('{}nem páros'.format(a))

import math
"""
a=b=c=0

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

d1=math.pow(a,b)
print(d1)

print("Begin")
a=2
b=4
c=3

d=b*b-4*a*c
if d>0:
    print("Megoldások száma:")
    x1=(-b+math.pow(d,0.5)/(2*a))
    x2=(-b-math.pow(d,0.5)/(2*a))
    print("x1={x1} x2={x2}".format(x1,x2))
elif d==0:
    print("Megoldások száma: 1")
    x1=(-b/(2*a))
    print("x1=x2={x1}".format(x1))
else:
    print("Nincs valós megoldás")

x=0+1j
print(x**2) #power

#prímek
eg=int(input("Adj meg egy számot:"))
db=0 #osztók száma
for i in range(2,eg):  #2=< .. <(eg-1) az intervallum
    if  eg%i==0:
        db=db+1
print("Osztók száma: {}".format(db))
if db==0:
    print("{} prímszám".format(eg))
else:
    print("{} NEM prím".format(eg))

#jelszó megfelelőség (8 kar.,nagy/kisbetű,szám)
    #ps=input()
jelszo="123A456b"
db_nagy=0
db_kis=0
db_szam=0
#c=jelszo[0:5]
n=len(jelszo)
for i in range(0,n):
    ch=jelszo[i:i+1] 
    if ch >='A' and ch<='Z':
        db_nagy=db_nagy+1
    elif ch >='a' and ch<='z':
        db_kis=db_kis+1
    elif ch >='0' and ch<='9':
        db_szam=db_szam+1
    else:
        pass
jo=(db_nagy>0) and (db_kis>0)and (db_szam>0) and (len(jelszo)>=8)
if jo==True:
    print("A jelszó megfelelő.")
else:
    print("Nem megfelelő jelszó")


#palindrom check
var="abba"
n=len(var)
for i in range(0,int(n/2)):
    if n!=str(n-i+1):
        #return False
        print("{} is a palindrome".format(var))
    else:
        print("{} is NOT a palindrome".format(var))
    print(var[i])
"""

x = "abba"
n = len(x)
pa = True
for i in range(0, n // 2):
  a = x[i:i + 1]
  b = x[n - i - 1:n - 1]
  if a != b:
    p = False
if p == False:
  print("{} is a palindrome".format(x))
else:
  print("{} is NOT a palindrome".format(x))

s = ""
for i in range(0, len(x)):
  ch = x[i:i + 1]
  s = ch + s
if s == x:
  print("{} is a palindrome".format(x))
else:
  print("{} is NOT a palindrome".format(x))

#
h = ''
new = "erre"
for i in new:
  s = i + s
if s == new:
  print("{} is a palindrome".format(new))
else:
  print("{} is NOT a palindrome".format(new))
