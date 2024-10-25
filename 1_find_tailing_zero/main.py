"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:

        if number < 0:
            return "number can not be negetive"
        
        #calculate factorial without using math lib
        fact = 1
        for i in range (2,number+1):
            fact = fact * i

        #find tailing zeroes
        count = 0
        while fact % 10 == 0:
            fact //= 10
            count += 1

        return count

