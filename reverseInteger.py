'''
Reverse Integer
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:
-2^31 <= x <= 2^31 - 1
'''

def reverse(x):
    tmpX=x
    numbers=[]
    reversedNumber=0
    if x>=0:
        numberLen=len(str(x))
    else:
        numberLen=len(str(x))-1
        tmpX=-1*tmpX
    
    multiplier=pow(10,numberLen-1)
    for i in range(0,numberLen):
        numbers.append(tmpX%10)
        tmpX=int(tmpX/10)
    for i in range(0,numberLen):
        reversedNumber+=(numbers[i]*multiplier)
        multiplier/=10
    if x>=0:
        return int(reversedNumber)
    else:

        return int(-1*reversedNumber)
    
print(reverse(167231235234))