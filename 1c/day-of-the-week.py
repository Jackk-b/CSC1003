#!/usr/bin/env python3

month = ((int(input()) - 1) * 30)
day = int(input())
day_of_year = (month + day)

print(((day_of_year + 6) % 7) + 1)
