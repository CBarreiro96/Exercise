"""
============================= Reverse Integer ==================================
Given a signed 32-bit integer x, return x with its digits reversed. If reversing
x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.
"""


def reverse(x):
    new_number = 0
    a = 0
    if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0
    if x < 0:
        x *= -1
        a = 1
    if x > 0:
        while x > 0:
            Mod = x % 10
            new_number = (new_number * 10) + Mod
            x //= 10
            if int(new_number) >= 2 ** 31 - 1 or int(new_number) <= -2 ** 31: return 0
        if a == 1:
            return new_number * (-1)
        else:
            return new_number
    else:
        return 0


if __name__ == '__main__':
    n = int(input("Ingrese un numero:\n"))
    print(reverse(n))
