"""
====================== Palindrome number =============================
---------------------- Description -----------------------------------
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.
"""


def isPalindrome(x):
    negative_number = 0

    # Identify negative number
    if x < 0:
        x *= -1
        negative_number = 1

    # Convert number integer to string
    Temporary_String = str(x)

    # Reverse Number
    if negative_number == 1:
        reverse_number = int(Temporary_String[::-1]) * -1
    else:
        reverse_number = int(Temporary_String[::-1])

    # Return True or False if the number is palindrome.
    if x == reverse_number:
        return True
    else:
        return False
