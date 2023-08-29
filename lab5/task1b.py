# -*- coding: utf-8 -*-
"""Task1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l8hWPKm3tH_rrYw82iZM3rpkC6WCXk8Y
"""

task1b_input = open(file='input1b.txt', mode='r')
task1b_output = open(file='output1b.txt', mode='w')

lst = task1b_input.readline().strip().split(" ")
v = int(lst[0])
e = int(lst[1])

adj_list = {}
parent = [0]*(v+1)

for i in range(1,v+1):
    adj_list[i] = []

for i in range(e):
    lst2 = task1b_input.readline().strip().split()
    u = int(lst2[0])
    v = int(lst2[1])
    adj_list[u].append(v)


count = 0
queue = []
lis = ""

for i in adj_list:
    for j in adj_list[i]:
        parent[j] += 1

for i in range(1,v+1):
            if parent[i] == 0:
                queue.append(i)

while queue:
    x = queue.pop(0)
    lis += str(x) + " "

    for i in adj_list[x]:
        parent[i] -= 1
        if parent[i] == 0:
            queue.append(i)

    count += 1

if count != v:
    task1b_output.write("IMPOSSIBLE")
else:
    task1b_output.write(lis)

task1b_input.close()
task1b_output.close()