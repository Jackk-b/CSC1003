#!/usr/bin/env python3

n = int(input())

x = n // 100000
n = n - (100000 * x)

x = n // 10000
n = n - (10000 * x)

x = n // 1000
n = n - (1000 * x)

y = n // 100

print((y * 10) + x)
