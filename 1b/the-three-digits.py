#!/usr/bin/env python3

n = int(input())

hundred = (n // 100)
ten = ((n - (hundred * 100)) // 10)
one = (n - (hundred * 100) - (ten * 10))

print(hundred)
print(ten)
print(one)
