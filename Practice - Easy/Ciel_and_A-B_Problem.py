#!/usr/bin/env python3

A, B = map(int, input().split())
solution = list(str(A-B))
if solution[0] == '0':
    solution[0] = '1'
elif solution[0] == '9':
    solution[0] = '8'
else:
    solution[0] = str(int(solution[0])+1)

print(''.join(solution))
