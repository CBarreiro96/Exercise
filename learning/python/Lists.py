#!/usr/bin/python3
'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer  at position .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
8. Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

========================== Example ============================
N = 4
append 1
append 2
insert 3 1
print

* append 1: Append 1 to the list, arr = [1].
* append 2: Append 2 to the list, arr = [1,2]
* insert 3 1: Insert 3 at index 1, arr = [1,3,2].
* print: Print the array.

-------------------------- Output -----------------------------
[1, 3, 2]
======================== Input Format ========================

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

======================== Constraints ========================

* The elements added to the list must be integers.
======================= Output Format =======================

For each command of type print, print the list on a new line.

====================== Sample Input 0 =======================

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

====================== Sample Output 0 ============================

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
if __name__ == '__main__':
    #operation(insert,remove,add)
    Lists = []
    Insert = int(input())
    while Insert:
        Op=str(input()).split()
        if len(Op) == 3:
            #Do the operation Lists.operation(number1, number2)
            eval('Lists.' + Op[0] + "(" + Op[1] + "," + Op[2] + ")")
        elif len(Op) == 2:
            eval('Lists.' + Op[0] + "(" + Op[1] + ")")
        elif Op[0] == 'print':
            print(Lists)
        else:
            eval('Lists.' + Op[0] + "()")
        Insert-=1

