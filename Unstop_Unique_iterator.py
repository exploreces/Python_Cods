
"""Ashish is provided with a collection 
of n strings in which some strings are of repeating nature 
but he has been given with a number k. His task is to find the kth unique string. 
Also before finding the kth unique string he has to sort each individual string beforehand. If there 
are fewer unique strings than k return empty string. As his best friend, your task is to help Ashish in accomplishing the task.

Input Format
The first line contains an integer n denoting the number of strings.
The next n lines contain strings.
The next line contains an integer k."""


n = int(input())
lst= []
for i in range(n):
  lst.append(input())

k = int(input())

unique=[]
same =[]

for i in lst:
  if i not in unique:
    unique.append(i)
  else:
    same.append(i)

for j in same:
  unique.remove(j)

if k>len(unique):
  print(" ")
else:
  print(unique[k-1])