"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""

from typing import Union

class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        
        if numbers == []:
            return "list can not blank"
        
        n = len(numbers)
        max_index = 0
        max_value = numbers[0]
        for i in range (1,n):
            if numbers[i] > max_value:
                max_value = numbers[i]
                max_index = i
            
        return max_index
    

