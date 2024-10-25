"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        
        if number < 0:
            return "number can not less than 0"
        if number > 10000000:
            return "number out of range"
        
        thai_word = ""
        
        numbers = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]

        if number < 10:
            return numbers[number]

        if number >= 1000000:
            thai_word += numbers[number // 1000000] + "ล้าน"
            number %= 1000000
        
        if number >= 100000:
            thai_word += numbers[number // 100000] + "แสน"
            number %= 100000
        
        if number >= 10000:
            thai_word += numbers[number // 10000] + "หมื่น"
            number %= 10000

        if number >= 1000:
            thai_word += numbers[number // 1000] + "พัน"
            number %= 1000

        if number >= 100:
            thai_word += numbers[number // 100] + "ร้อย"
            number %= 100
        
        if number >= 10:
            thai_word += tens[number // 10]
            number %= 10
        
        if number > 0:
            #check the end with one case
            if number == 1:
                thai_word += "เอ็ด"
            else: thai_word += numbers[number]

        return thai_word
    