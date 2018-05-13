#!/usr/bin/env python3

def is_lapidrome(str1, str2):
    if len(str1) == 0 or len(str2) == 0: return 'YES'
    if str1[0] not in str2: return 'NO'
    str2 = str2.replace(str1[0], '', 1)
    return is_lapidrome(str1[1:], str2)


for T in range(int(input())):
    S = input()
    l = len(S)
    s1 = S[0:l//2]
    s2 = S[-len(s1):]
    print(is_lapidrome(s1, s2))