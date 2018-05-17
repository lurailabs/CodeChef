#!/usr/bin/env python3

# A -> num. of particles bombarded (0 - 1.000.000.000)
# N -> max. particles per chamber (0 - 100)
# K -> num. of chambers (1 - 100)

A, N, K = map(int, input().split())

result = [0]*K
base = N + 1

for i in range(K):
    result[i] = A % base
    A = A//base

print(' '.join(str(x) for x in result))
