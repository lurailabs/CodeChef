#!/usr/bin/env python3

for case in range(int(input())):
    horses_count = int(input())
    skill = [int(x) for x in input().split()]
    skill.sort()
    diff = []
    for n in range(len(skill)-1):
        diff.append(skill[n+1]-skill[n])

    print(min(diff))

