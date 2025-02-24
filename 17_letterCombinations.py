"""
LeetCode#17
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.
"""

def letterCombinations(digits):
    if not digits:
        return []
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    def backtrack(combination, next_digits):
        if not next_digits:  # Base case: all digits processed
            result.append(combination)
            return
        digit = next_digits[0]
        letters = mapping.get(digit)
        if letters:
            for letter in letters:
                backtrack(combination + letter, next_digits[1:])
    print("dig:", digits)
    backtrack("", digits)
    return result

print("Letter Combinations:=>", letterCombinations("23"))


