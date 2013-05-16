'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

-------------------------

Math

F_n = phi^n / sqrt(5)
10^999 < (phi^n / sqrt(5))
999 < n*log10(phi) - log10(5)/2
'''


import time
import math

def fibonacci_1():
	f=[1,1]
	while len(str(f[-1]))<1000:
		f.append(f[-1]+f[-2])
	return len(f)

def fibonacci_2(n):
	phi = (1 + 5**0.5) / 2
	n = 1

	while 999 > ( n*math.log10(phi) - math.log10(5)/2 ):
		n += 1
		
	return n


if __name__ == "__main__":
	start = time.time()
	result = fibonacci_2()
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)
	
	
	
	
	
	
