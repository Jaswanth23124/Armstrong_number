'''
# Write a program to print square using stars:
Example : If Size 5 then the output should be: 

                * * * * *
                * * * * *
                * * * * *
                * * * * * 
                * * * * *

'''
Size = int(input("Enter number of rows: "))
for i in range(Size):
    for j in range(Size):
        print("*",end= " ")
    print()