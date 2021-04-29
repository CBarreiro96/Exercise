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

