# -*- coding: utf-8 -*-
"""Task1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YOX1foph-bIaD589yPv4grsutqV2wkeZ
"""

task1b_input = open(file='input1b.txt', mode='r')
task1b_output = open(file='output1b.txt', mode='w')

lst = task1b_input.readline().strip().split(" ")
v = int(lst[0])
e = int(lst[1])

adj_list = {}
for i in range(v+1):
    adj_list[i] = []

for i in range(e):
    lst2 = task1b_input.readline().strip().split()
    u = int(lst2[0])
    v = int(lst2[1])
    w = int(lst2[2])
    tup = (v,w)
    adj_list[u].append(tup)

task1b_input.close()

for key in adj_list:
    if(len(adj_list[key]))==0:
        output_line = str(key) + " : " + "\n"
        task1b_output.write(output_line)
    else:
        output_line = str(key) + " : "
        for val in adj_list[key]:
            output_line = output_line + str(val) + " "
        output_line = output_line + "\n"
        task1b_output.write(output_line)
task1b_output.close()