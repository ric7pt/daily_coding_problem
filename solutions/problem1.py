#21-01-2021 problem1
#Good morning! Here's your coding interview problem for today.
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

def isthere(array, k):
    solution = [];
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i]+array[j]==k:
                return True
    return False

assert isthere([10, 15, 3, 7], 17)
