"""
File: rocket.py
Name: Irene Chen 陳筱涵
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	To make to rocket from head, belt, upper, lower
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	To make the head and it will be extend by Size
	"""
	for i in range(1, SIZE+1):
		for j in range(SIZE-i+2):
			print(' ', end="")
		for j in range(1, i+1):
			print('/', end="")
		for j in range(1, i+1):
			print('\\', end="")
		print("")


def belt():
	"""
	To build the +==+ by SIZE
	"""
	for i in range(1):
		for j in range(1):
			print(' ', end="")
		for j in range(1):
			print('+', end="")
		for j in range(2, SIZE*2+2):
			print('=', end="")
		for j in range(0, SIZE*3, SIZE*3):
			print('+', end="")
		print("")


def upper():
	"""
	To make the upper and it will be extend by Size
	"""
	for i in range(1, SIZE+1):
		for j in range(1):
			print(' ', end="")
		for j in range(1):
			print('∣', end="")
		for j in range(SIZE-i):
			print('˙', end="")
		for j in range(i):
			print('/', end="")
			print('\\', end="")
		for j in range(SIZE-i):
			print('˙', end="")
		for j in range(0, SIZE+1, SIZE+1):
			print('∣', end="")
		print("")


def lower():
	"""
	To make the lower and it will be extend by Size
	"""
	for i in range(1, SIZE+1):
		for j in range(1):
			print(' ', end="")
		for j in range(1):
			print('∣', end="")
		for j in range(i-1):
			print('˙', end="")
		for j in range(SIZE-i+1):
			print('\\', end="")
			print('/', end="")
		for j in range(i-1):
			print('˙', end="")
		for j in range(0, SIZE+1, SIZE+1):
			print('∣', end="")
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()