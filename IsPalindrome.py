# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def isPalindrome(x: int) -> bool:

    if x < 0:
        return False

    original = x
    reverse = 0

    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    return original == reverse


a = isPalindrome(121)
print(a)