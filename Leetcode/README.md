# Problem in Leetcode
## :scroll::book: Description :book::scroll:
### :memo: Activities :memo:
<details>
<summary><b>1. Two sum</b></summary>

## Two sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
### Example

---
#### INPUT
>nums = [2,7,11,15], target = 9
#### OUTPUT
>[0,1]
---
#### INPUT
>nums = [3,2,4], target = 6
#### OUTPUT
>[0,1]
---

### Whiteboard
* In the lost case (O(**n<sup>2</sup>**))
<div align="center">
<img src="https://user-images.githubusercontent.com/66263776/116494229-02151a00-a866-11eb-971c-6752ed3718f4.png" width="600" height= "600">
</div>
<div align="center">
    <table>
        <tr>
            <th><center>Runtime</center></th>
            <th><center>Memory</center></th>
        </tr>
        <tr>
            <td align="center">464 ms</td>
            <td align="center">14.4 MB</td>
        </tr>
    </table>
</div>

<div align="center">

[Check code](https://github.com/CBarreiro96/PlatformWeb_Exercise/commit/2aaaee9a18c0cbb4abaa0dcdcaa811952186067f#diff-24c60a2d6f3815ab6f252e4ba704a7ff0f5f813ce4b8fb3cb9a9676acf2256bd)

</div>

* The best case O(**n**)
<div align="center">
<img src="https://user-images.githubusercontent.com/66263776/116566410-5ce15c80-a8cc-11eb-9ce1-f4688e93b9fe.png" width="600" height= "600">
</div>
<div align="center">
    <table>
        <tr>
            <th><center>Runtime</center></th>
            <th><center>Memory</center></th>
        </tr>
        <tr>
            <td align="center">40 ms</td>
            <td align="center">14.5 MB</td>
        </tr>
    </table>
</div>

<div align="center">

[Check code](https://github.com/CBarreiro96/PlatformWeb_Exercise/blob/master/Leetcode/Python/Two_Sum.py)

</div>

</details>

<details>
    <summary><b>2. Reverse_Integer</b></summary>
    
## Reverse Integer
### :scroll: Description :scroll:

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then return 0.

---
### INPUT
>x = 123
### OUTPUT
>321
---
### INPUT
>x = -123
### OUTPUT
>-321
---
### INPUT
>x = 0
### OUTPUT
>0
---
## WHiteboard

<div align="center">
<img src="https://user-images.githubusercontent.com/66263776/116604605-f5d79e00-a8f3-11eb-9e72-4ba8eaa54c41.png" width="600" height= "600">
</div>

<div align="center">
    <table>
        <tr>
            <th><center>Runtime</center></th>
            <th><center>Memory</center></th>
        </tr>
        <tr>
            <td align="center">32 ms</td>
            <td align="center">14.2 MB</td>
        </tr>
    </table>
</div>

</details>

<details>
<summary><b>3. Palindrome number</b></summary>

## :scroll: Description :Scroll:
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

---
### INPUT
>x = 121
### OUTPUT
> true
---
### INPUT
>x = -121
### OUTPUT
>false
---
### INPUT
>x = 10
### OUTPUT
>false
---
### INPUT
>x = -101
### OUTPUT
>false

## WHITEBOARD
<div align="center">
<img src="https://user-images.githubusercontent.com/66263776/116754448-5d621c00-a9ce-11eb-8773-3387473e970d.png" width="600" height= "600">
</div>
</details>

<details>
    <summary><b>4. Roman to Integer</b></summary>

## :scroll: Description :Scroll:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9. 
* X can be placed before L (50) and C (100) to make 40 and 90. 
* C can be placed before D (500) and M (1000) to make 400 and 900.<br>
Given a roman numeral, convert it to an integer.

---
### INPUT
>s = "III"
### OUTPUT
> 3

---

### INPUT
>s = "IV"
### OUTPUT
> 4

---

### INPUT
>s = "LVIII"
### OUTPUT
> 58

---

### INPUT
>s = "MCMXCIV"
### OUTPUT
> 1994

---

## WHITEBOARD
<div align="center">
<img src="https://user-images.githubusercontent.com/66263776/116800166-24a46e80-aac4-11eb-9b0d-df0dd0475fb5.png" width="600" height= "600">
</div>
</details>