#!/usr/bin/env python3

def dinamic_algorithm(values, m):
    matrix = []
    for x in range(len(values)):
        row = [1]
        for y in range(1, m+1):
            if values[x] == y: row.append(1)
            elif x-1 >= 0 and matrix[x-1][y] == 1: row.append(1)
            elif x-1 >= 0 and y-values[x] >= 0 and matrix[x-1][y-values[x]] == 1: row.append(1)
            else: row.append(0)
        matrix.append(row)
    return 'Yes' if matrix[-1][-1] else 'No'


def main():
    for t in range(int(input())):
        n, m = input().split()
        n, m = int(n), int(m)
        values = []
        for x in range(n):
            values.append(int(input()))
        values.sort()

        if m == 0: print('Yes')
        elif not values: print('No')
        else: print(dinamic_algorithm(values, m))

main()


