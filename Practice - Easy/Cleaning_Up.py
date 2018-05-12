#!/usr/bin/env python3

for case in range(int(input())):
    to_complete_count, completed_count = [int(x) for x in input().split()]
    completed = [int(x) for x in input().split()]
    to_do = [str(item) for item in [x for x in range(1,to_complete_count+1)] if item not in completed]
    assistant = [x for x in to_do if to_do.index(x)%2 == 1]
    chef = [x for x in to_do if x not in assistant]
    print(' '.join(chef))
    print(' '.join(assistant))
