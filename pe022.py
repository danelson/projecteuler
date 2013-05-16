'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

Answer = 871198282
'''


import time

def sum_names(names):
	position = 1
	sum = 0
	for name in names:
		temp = 0
		for ch in name:
			temp += ord(ch) - 96
		sum += temp*position
		position += 1
	return sum

if __name__ == "__main__":
	start = time.time()
	
	#clean up data
	fp = open("names.txt","r")
	names = fp.readlines()[0].lower()
	names = names.replace('"','').split(",")
	names.sort()
	
	result = sum_names(names)
	
	elapsed = (time.time() - start)
	 
	print "result %s returned in %s seconds." % (result,elapsed)