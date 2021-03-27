"""
================================= Diagonal difference ======================================================
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is |15-17|=2.

------------------------ Function description ----------------------------------------------

Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

   * int arr[n][m]: an array of integers

-------------------------------- Return -------------------------------------------------------

   * int: the absolute diagonal difference

------------------------------- Input Format ----------------------------------------------
The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row, arr(i), and consists of space-separated integers arr[i][j].

-------------------------------- Constraints -------------------------------------------------
* -100<= arr[i][j] <= 100

------------------------------- Output Format -------------------------------------------
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
"""
import os


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    a = 0
    b = 0
    j = len(arr) - 1
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][j]
        j = j - 1
    return abs(a - b)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')