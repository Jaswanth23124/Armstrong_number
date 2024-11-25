'''
# Write a program to print the below pattern:
Example If n = 5

                * * * * *
                * * * *
                * * *
                * *
                *

'''

n = int(input("Enter a number: "))
for i in range(n):
    for j in  range(n-i):
        print("*", end = " ")
    print()
