#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Answer = 31875000

'''
a^2 + b^2 = c^2
a + b + c = 1000
c = 1000 - (a+b)
a^2 + b^2 = (1000 - (a+b))^2
a^2 + b^2 = 1000000 - 2000(a+b) + (a+b)^2
a^2 + b^2 = 1000000 - 2000(a+b) + a^2 + 2ab + b^2
0 = 1000000 - 2000(a+b) + 2ab
2000(a+b) - 2ab = 1000000
1000(a+b) - ab = 500000
a(1000-b) + 1000b = 500000
a(1000-b) = 500000 - 1000b
a = (500000 - 1000b) / (1000-b)
'''



def find_triplets(n):
	triplets = []
	for i in range(1,n/2):
		for j in range(i+1,n/2):
			#print i,j
			k = 1000 - j - i
			if (i**2 + j**2 == k**2):
				return i*j*k
	return triplets
				
				
if __name__ == "__main__":
	print find_triplets(1000)
	
	