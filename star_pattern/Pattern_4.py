'''
# Write a program to print the below program 

Example if n = 5

                  * 
                * *
              * * *
            * * * *
          * * * * *

'''

n = int(input("Enter a number: "))
for i in range(n): 
  for j in range(i, n): 
     print(' ', end=' ') 
  for j in range(i+1):
     print('*', end=' ')
  print()