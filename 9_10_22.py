'''
Q1. Find the largest number from the given list, use for loop.

numbers = [12, 75, 150, 180, 145, 525, 50]
'''

numbers = [12, 75, 150, 180, 145, 525, 50]
    
# Can't be able to solve this problem please discuss in next class 


"""
 Q2. Print all the even number between (1, 12).

"""


for i in range(2,13,2):
    print(f"The even numbers between 1 and 12 is : {i}")

"""
Q3. Calculate the sum of all numbers from 1 to a given number

Expected Output:

Enter number 10

Sum is:  55
    
"""

n = int(input("Enter the number : "))
for i in range(1,n+1):
    pass
print(f"The sum of all the numbers upto {i} is :{n*(n+1)/2}")


'''
Q4. Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five

If the number is greater than 150, then skip it and move to the next number

If the number is greater than 500, then stop the loop

[ ]
# Given:

numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]

'''

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5 == 0:
        if i == 150:
            continue
        elif i >=500:
            break
    else:
        continue
    print(f"The desired list of the numbers is : {i}")


'''
Q5. Print the given list in reverse order.

list1 = [10, 20, 30, 40, 50]

'''

list1 = [10, 20, 30, 40, 50]
list = list1[::-1]
print(list)