"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

number = 2**1000

number = str(number)
totalSum = 0
for i in range(len(number)):
    totalSum += int(number[i])
print(totalSum)
