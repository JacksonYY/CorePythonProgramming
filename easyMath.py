#!/usr/bin/env python

from operator import add, sub
from random import randint, choice

ops = {'+':add, '-':sub}
MAXTRIES = 2

def doprob():
    ops = choice('+-')
    nums = [randint(1,10) for i in range(2)]
    ans = ops[choice]
    pr = "%d %s %d" % (nums[0], ops, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_int(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer of %s is %d' % (pr, ans)
                break
            else:
                print 'incorrect...try again'
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError):
            print 'invalid input....try again'

