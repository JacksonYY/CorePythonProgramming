#!/usr/bin/env Python

def convert(func, seq):
    'conv sequence of numbers to same type'
    return [func(num) for num in seq]

myseq = [123, 45.67, -6.2e8, 99999999]
print (convert(int, myseq))
print (convert(float, myseq))