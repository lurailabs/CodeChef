#!/usr/bin/env python3

for case in range(int(input())):
    songs_count = int(input())
    lengths = list(map(int, input().split()))
    songs_length = {v+1: k for v, k in enumerate(lengths)}
    position = int(input())
    lengths.sort()
    print(lengths.index(songs_length[position])+1)

