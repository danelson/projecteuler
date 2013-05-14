#A palindromic number reads the same both ways. The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91  99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#Answer = 906609

def palindrome():
	value = 0
	a = 100
	b = 100
	for i in range(100,999):
		for j in range(100,999):
			str_value_f = str(i*j)
			str_value_b = str_value_f[::-1]
			if str_value_f == str_value_b and i*j > value:
				value = i*j
	return value
				
if __name__ == "__main__":
	print palindrome()