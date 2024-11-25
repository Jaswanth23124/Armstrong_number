'''
# Write a program to print the given pattern 
Example: If n = 4

            *
            * *
            * * *
            * * * *

'''

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()