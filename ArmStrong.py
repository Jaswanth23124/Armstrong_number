'''
# Write a program to check whether the given number is Armstrong Number or not

n = int(input("Enter a number to check whether it is an Armstrong number or not: "))
num = str(n)
length = len(num)

total = 0
for i in num:
    total += int(i) ** length

if total == n:
    print("It is an Armstrong Number.")
else:
    print("It is not an Armstrong Number")

'''



'''
# Write a program to print Armstrong numbers in the given range

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))

found = False
for  i in range(n1, n2+1):
    num = str(i)
    length = len(num)

    total = 0
    for x in num:
        total += int(x) ** length
    if total == i:
        print(i)
        found = True
if not found:
    print("There are no Armstrong numbers within the range you given.")

'''



'''
# write a program to check whether the number is Armstrong number or not using functions

def Armstrong_Nummber(n):
    num = str(n)
    size = len(num)
    total = 0
    for i in num:
        total += int(i) ** size
    return total == n

x = int(input("Enter a number to check whether it is armstrong or not: "))

if Armstrong_Nummber(x):
    print("It is an armstrong number.")
else:
    print("It is not an Armstrong number.") 

'''


'''
# Write a program to print all Armstrong numbers within the given range using Functions.

def Armstrong_Number(n1,n2):
    found = False
    for i in range(n1,n2+1):
        num = str(i)
        size = len(num)
        total = 0
        for x in num:
            total += int(x) ** size
        if total == i:
            print(i, end = "\n")
            found = True
    if not found:
        print("There are no Armstrong numbers within the given range.")
m1 = int(input("Enter starting number: "))
m2 = int(input("Enter ending number: "))
print(f"Armstrong numbers between {m1} and {m2} are ")
Armstrong_Number(m1,m2)


'''

for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while(i!=0):
        digit = i % 10
        result += digit ** n
        i = i//10
    if num == result:
        print(num)