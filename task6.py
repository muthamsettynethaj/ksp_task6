print("TASK-6")
#operators
print("---Arthmetical operators---")
a=10
b=15
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a**b)
print(a%b)
print("---Relational operators---")
a=7
b=8
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
print("---Assignmental operators---")
a=int(input())#reading integer input from user
a+=1
print(a)
a-=2
print(a)
a*=4
print(a)
a/=2
print(a)
a%=3
print(a)
a**=3
print(a)
print("---Logical operators---")
a=3
b=4
c=8
print(a<4 and c<=100)
print(a<=1 or b>c)
print(a!=3)
print("--Identity operators--")
a=9
b=9
print(a is b)
a=["Car","Bike"]
b=["Car","Bike"]
print(a is not b)
print("--Membership Operators---")
name="Muthamsetty Nethaji"
print("nethaji" in name)
print("muthamsetty" not in name)
#Type casting
print("---Type casting---")
n=9
print(type(n))
print(float(n))
print(str(n))
d=True
print(d)

k=9.8
print(type(k))
print(int(k))
print(str(k))
#String Slicing
print("---String Slicing---")
str1="Slicing the string"
print(str1[1:7])
print(str1[:10])
print(str1[0:])
#conditional statements
print("---conditional statements---")
a=9
b="String"
if(a<15 and b[1:2]=="t"):
    print("True")
elif(a!=0 and b=="string"):
    print("Checkit")
else:
    print("False")
#LOOPS
print("For Loop")
n=10
sum=0
for i in range(n):
    sum+=i
print(sum)
print("while loop")
n=2
while(n<4):
    print("this is while loop")
    n+=1