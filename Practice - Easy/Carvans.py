#!/usr/bin/env python3

for case in range(int(input())):
    N = input()  # num. of cars
    speeds = list(map(int, input().split()))
    limit, solution = speeds[0], 0
    for speed in speeds:
        if speed <= limit:
            solution +=1
            limit = speed
    print(solution)
