#Add all the natural numbers below one thousand that are multiples of 3 or 5.
#Answer: 233168


def multiples3and5(x):
	value = 0
	for i in range(x):
		if i % 3 == 0 or i % 5 == 0:
			value += i
	return value

if __name__ == "__main__":
	print multiples3and5(1000)