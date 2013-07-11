'''
In England the currency is made up of the pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 100p, and 200p
It is possible to make 200p in the following way:

1x100p + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 200p be made using any number of coins?

Answer = 
'''

import time

def fifthPowers(power):
	amount = 200
	coins  = [1,2,5,10,20,50,100,200]
	ways = [1]+[0]*amount
	
	for coin in coins:
		for i in range(coin, amount+1):
			ways[i] += ways[i-coin]
			
	return ways[amount]

if __name__ == "__main__":
	start = time.time()
	result = fifthPowers(5)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)
	