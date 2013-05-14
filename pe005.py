#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?

#Answer = 232792560

def multiple():
	value = 2520
	while True:
		for i in range(2,21):
			if (value % i) != 0:
				break
			if i == 20:
				return value
		value += 2520


if __name__ == "__main__":
	print multiple()