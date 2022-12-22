string = input("Enter string\n")

dict = {}

if(" " in string):
    a = string.split()
    for i in a:
        c = string.count(i)
        dict.update({i : c})
        
else:
    for i in string:
        c = string.count(i)
        dict.update({i : c})
    

print(dict)


d = int(input("Day - "))
m = int(input("Month - "))
y = int(input("Year - "))

long = [1, 3, 5, 7, 8, 10, 12]
short = [4, 6, 9, 11]

if (d<1) | (y>2025) | (y<1800):
    print("Invalid Date!")

elif (m in long) & (d<31):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m in long) & (d==31) & (m!=12):
    print(f"Next date is: 01/{m+1}/{y}")

elif (m==12) & (d==31):
    print(f"Next date is: 01/01/{y+1}")

elif (m in short) & (d<30):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m in short) & (d==30):
    print(f"Next date is: 01/{m+1}/{y}")

elif (m==2) & (y%4==0) & (d<29):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m==2) & (y%4==0) & (d==29):
    print(f"Next date is: 01/{m+1}/{y}")

elif (m==2) & (y%4!=0) & (d<28):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m==2) & (y%4!=0) & (d==28):
    print(f"Next date is: 01/{m+1}/{y}")

else:
    print("Invalid Date!")
    
    my_list = [3, 9, 10, 13, 17, 19, 22, 23]
new_list = []

for i in my_list:
    t = (i, i*i)
    new_list.append(t)

print(new_list)


g = int(input("Enter Your Grade\n"))

if (g==10):
    print("Your Grade is 'A+' and Outstanding Performance")

elif (g==9):
    print("Your Grade is 'A' and Excellent Performance")

elif (g==8):
    print("Your Grade is 'B+' and Very Good Performance")

elif (g==7):
    print("Your Grade is 'B' and Good Performance")

elif (g==6):
    print("Your Grade is 'C+' and Average Performance")

elif (g==5):
    print("Your Grade is 'C' and Below Average Performance")

elif (g==4):
    print("Your Grade is 'D' and Poor Performance")

else:
    print("Error!")
    
    
    string = "ABCDEFGHIJK"
space = " "

length = len(string)

i = 11
j = 11

while(j>=0):
    print((space*(11-i)) + string[0:j] + (space*(11-i)))
    i = i - 1
    j = j - 2
    
    
    from collections import OrderedDict

i = "Y"
dict0 = {}

while(i=="Y"):
    sid = input("Enter Your Sid: ")
    name = input("Enter Your Name: ")
    dict0.update({sid:name})
    print("\nStudent added successfully\n")
    i = input("To add a new student, enter Y\nTo move forward, enter N\n")

# a.
print("Student Details: ", dict0)

# b.
k = list(dict0.keys())
lk = len(k)
v = list(dict0.values())
lv = len(v)

i = 0

dict_rev = {}
while i<lk:
    dict_rev.update({v[i]:k[i]})
    i = i+1

dict_rev1 = OrderedDict(sorted(dict_rev.items()))


k2 = list(dict_rev1.keys())
lk2 = len(k2)
v2 = list(dict_rev1.values())
lv2 = len(v2)

j = 0

dict2 = {}
while j<lk2:
    dict2.update({v2[j]:k2[j]})
    j = j+1

print("\nSorted using names: ", dict2)

# c.
dict3 = OrderedDict(sorted(dict0.items()))
dict3 = dict(dict3)
print("\nSorted using SID's: ", dict3)

# d.
search = input("\nEnter SID to search name\n")
if search in list(dict0.keys()):
    print(f"{search} : {dict0[search]}")
else:
    print("SID not found!")
    
    n = int(input("Enter number of terms of Fibonacci series to be printed\n"))


def fib(n):
    if(n<=0):
        print("Enter a positive number")

    elif(n==1):
        return 0

    elif(n==2):
        return 1

    else:
        return fib(n-1) + fib(n-2)


for i in range(1, n+1):
    print(fib(i))
    
    s1= {1, 2, 3, 4, 5}
s2= {2, 4, 6, 8}
s3= {1, 5, 9, 13, 17}

# a.
sa = s1.intersection(s2)

print("\nElements that are in set1 and set2:", sa)

# b.
sb1_1 = s1 - s1.intersection(s2)
sb1_2 = sb1_1  - sb1_1.intersection(s3)

sb2_1 = s2 - s2.intersection(s1)
sb2_2 = sb2_1  - sb2_1.intersection(s3)

sb3_1 = s3 - s3.intersection(s1)
sb3_2 = sb3_1  - sb3_1.intersection(s2)

sb = sb1_2.union(sb2_2).union(sb3_2)

print("\nElements only one of the three sets Set1, Set2 and Set3:", sb)

# c.
sc1_1 = s1.intersection(s2)
sc1_2 = sc1_1 - sc1_1.intersection(s3)

sc2_1 = s2.intersection(s3)
sc2_2 = sc2_1 - sc2_1.intersection(s1)

sc3_1 = s3.intersection(s1)
sc3_2 = sc3_1 - sc3_1.intersection(s2)

sc = sc1_2.union(sc2_2).union(sc3_2)

print("\nElements that are exactly two of the sets Set1, Set2 and Set3:", sc)

# d.
sd = set()
for i in range(1, 11):
    if i in s1:
        continue
    else:
        sd.add(i)

print("\nSet of all integers in the range 1 to 10 that are not in Set1:", sd)

# e.
su = s1.union(s2).union(s3)
se = set()
for j in range(1, 11):
    if j in su:
        continue
    else:
        se.add(j)

print("\nSet of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:", se,"\n")