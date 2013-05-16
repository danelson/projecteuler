'''
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By mathematical
analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any
further by analysis even though it is known that the greatest number that cannot
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
'''

import time
import math

'''
#slow
def abundant_numbers(n):
	L = []
	for i in range(12,n):
		if sum_multiples(i) > i:
			L.append(i)
	return L
	
def sum_multiples(n):
	total = 0
	for i in range(1,n):
		if n%i == 0:
			total += i
	
	return total
	
def non_abudant_sum(n,L):
	total = [i for i in range(n)]
	sum_abundant = []
	
	for j in range(len(L)):
		for k in range(j,len(L)):
			if L[j]+L[k] < n:
				total[L[j]+L[k]] = 0				
	return sum(total)
	
def main1():
	start = time.time()
	result = abundant_numbers(28124)
	result = non_abudant_sum(28124,result)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)
'''

'''
#medium
def abundant_numbers(n):
	S = set()
	for i in range(12,n):
		if sum_multiples(i) > i:
			S.add(i)
	return S
	
def sum_multiples(n):
	total = set()
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0:
			total.add(i)
			total.add(n/i)
	return sum(total)

def non_abudant_sum(n,S):
	total = set(range(0,n))
	abundant_sums = set(a+b for a in S for b in S)
	return sum(total - abundant_sums)
	
def main2():
	start = time.time()
	result = abundant_numbers(28124)
	result = non_abudant_sum(28124,result)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)
'''


#fast
def divisor_sums(n):
	sum = [0] * (n)
	for i in range(1, n/2):
		for j in range(i*2, n, i):
			sum[j] += i
	return sum
		
def non_abudant_sum(n):
	abundants = set()
	sum = 0
	for i, s in enumerate(divisor_sums(n)):
		if s > i:
			abundants.add(i)
		for a in abundants:
			if i - a in abundants:
				break
		else:
			sum+= i
	return sum

def main3():
	start = time.time()
	result = non_abudant_sum(28124)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)

	

if __name__ == "__main__":
	main3()