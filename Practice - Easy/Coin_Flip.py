#!/usr/bin/env python3

for case in range(int(input())):
    for g in range(int(input())):
        game = list(map(int, input().split()))
        if game[1] % 2 == 0 or game[0] == game[2]:
            solution = game[1]//2
        else:
            solution = game[1]-game[1]//2
        print(solution)




