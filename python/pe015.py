'''
Starting in the top left corner of a 22 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?

Answer = 137846528820
'''

import time

 
def route_num(cube_length):
	L = [1] * cube_length
	for i in range(cube_length):
		for j in range(i):
			L[j] = L[j]+L[j-1]
		L[i] = 2 * L[i-1]
	return L[-1]
 

if __name__ == "__main__":
	start = time.time()
	n = route_num(20)
	elapsed = (time.time() - start)
	print "%s found in %s seconds" % (n,elapsed)