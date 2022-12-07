#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ans = []
    for i in matrix:
        nums = []
        for j in i:
            nums.append(j ** 2)
        ans.append(nums)
    return ans
