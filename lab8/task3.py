# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19VFBjSX1xIt48tp7F3yWWtRg2qknqPee
"""

#task3

task3_input = open(file='input3_1.txt', mode='r')
task3_output = open(file='output3_1.txt', mode='w')

lis = task3_input.readline().split(" ")
tak = int(lis[0])
amm = int(lis[1])

lis2 = task3_input.readline().split(" ")

lis3 = [eval(i) for i in lis2]


def _change_matrix(coin_set, change_amount):
    matrix = [[0 for i in range(change_amount + 1)] for i in range(len(coin_set) + 1)]

    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix


def coin_change(coins, change):
    matrix = _change_matrix(coins, change)
    for c in range(1, len(coins) + 1):
        for r in range(1, change + 1):

            if coins[c-1] == r:
                matrix[c][r] = 1

            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]

            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])

    return matrix[-1][-1]


x = (coin_change(lis3, amm))
if x == "0":
    task3_output.write("-1")
else:
    task3_output.write(str(x))

task3_input.close()
task3_output.close()