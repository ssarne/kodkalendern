#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs

words = codecs.open("dec06.txt", "r", "utf-8").readlines()
vowels = 'aeiouyåäö'
dissallow = 'cywh'

n = 0
for word in words:
    m0 = True
    for c in word:
        if c in dissallow:
            m0 = False

    m1 = False
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            m1 = True

    m2 = False
    for c in word:
        if c in vowels:
            m2 = True

    if m0 and m1 and m2:
        n += 1

print(n)



