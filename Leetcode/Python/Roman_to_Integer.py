"""
====================================== Roman to Integer =======================================
Given a roman numeral, convert it to an integer.
"""


def romanToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    A = 0
    # List in reverse order
    for i in reversed(range(0, len(s))):
        # Compare number and add or subtract the number
        if dic[s[i]] > dic[s[i - 1]] and i != 0:
            number += (dic[s[i]] - dic[s[i - 1]])
            A += 1
        elif A != 1 or (i == 0 and A != 1):
            number += dic[s[i]]
        else:
            A = 0
    return number


if __name__ == '__main__':
    print(romanToInt('MCMXCIV'))
