#! /usr/bin/env python3

n = int(input())
product = 1

for i in range(n):
    num = int(input())
    product *= num

print(product)