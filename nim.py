#!/usr/bin/env python
import sys
import string


def check(key, xor):
	if key <= 1:
		return False
	for i in range(1, key):
		if i^xor == 0:
			return i
	return False

len = len(sys.argv)
if len < 2:
	print "Usage : nim.py [num1|num2|num3|...]"
	sys.exit()

nums = 0
numbers = list()
for i in range(1, len):
	nums += 1
	numbers.append(string.atoi(sys.argv[i]))

for i in range(nums):
	xor=-1
	for j in range(nums):
		if(j != i):
			if xor == -1:
				xor = numbers[j]
			else:
				xor ^= numbers[j]
	ret = check(numbers[i], xor)
	if ret != False:
		tmp=list(numbers)
	  	tmp[i] = ret
	  	print tmp

sys.exit()

