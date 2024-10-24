class Solution:
    def intToRoman(self, num: int) -> str:

        roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        # Result string to store the Roman numeral
        result = []

        # Iterate over the Roman numeral table
        for value, symbol in roman_map:
            # Append the symbol as many times as it fits in the num
            while num >= value:
                result.append(symbol)
                num -= value

        # Join the result list into a single string and return it
        return ''.join(result)

        