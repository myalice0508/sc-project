"""
File: boggle.py
Name: 陳筱涵
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it

import time
FILE = 'dictionary.txt'

# Global
dictionary = []
word_dic = {}


def main():
	"""
	TODO: the user will key in the 4 letters four times, and the system will automatic to link the letter and to find
	      the word whether is in the dictionary.
	"""

	read_dictionary()
	count = 0
	row1 = str(input('1 row of letters: '))
	row1 = row1.lower()
	count = 0
	column = 0
	if check_the_letter(row1, count, column):
		row2 = str(input('2 row of letters: '))
		row2 = row2.lower()
		column += 1
		if check_the_letter(row2,  count, column):
			row3 = str(input('3 row of letters: '))
			row3 = row3.lower()
			column += 1
			if check_the_letter(row3,  count, column):
				row4 = str(input('4 row of letters: '))
				row4 = row4.lower()
				column += 1
				if check_the_letter(row4,  count, column):
					find_list = []
					# x = time.time()
					for i in range(4):
						for j in range(4):
							game_start(i, j, "", find_list, {})
					# y = time.time()
					# print(y-x)
					for word in find_list:
						count += 1
						# print(f'Found "{word}"')
					print(f'There are {count} word in total')

				else:
					print('Illegal input')
			else:
				print('Illegal input')
		else:
			print('Illegal input')
	else:
		print('Illegal input')


def game_start(x, y, word, find_list,  take_out):
	"""
	:param x: it's x position coordinate
	:param y: it's y position coordinate
	:param word: find the word that I would like to comparison
	:param find_list: the list is through the game and get the word and also in dictionary
	:param take_out: to avoid the letter duplicate use
	:return: not need to return
	"""
	if word in dictionary and len(word) >= 4 and word not in find_list:
		find_list.append(word)
		print(f'Found "{word}"')
		game_start(x, y, word, find_list, take_out)

	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 4 > i + x >= 0:
					if 4 > j + y >= 0:
						x1 = x + i
						y1 = y + j
						if (x1, y1) in word_dic:
							word += word_dic[(x1, y1)]
							if has_prefix2(word, find_list) is False:
								take_out[(x1, y1)] = word_dic[(x1, y1)]
								word_dic.pop((x1, y1))
								if has_prefix(word):
									game_start(x1, y1, word, find_list, take_out)
								word = word[0:-1]
								word_dic[(x1, y1)] = take_out[(x1, y1)]
								take_out.pop((x1, y1))


def check_the_letter(word, count, column):
	"""
	:param word: the word which is the user key in
	:param count: it's x position coordinate
	:param column: it's y position coordinate
	:return: if the word is meet the principle, return True
	"""
	last = ""
	global word_dic
	for letter in word:
		if letter.isalpha():
			word_dic[(count, column)] = letter
			count += 1
		if last == "":
			last = letter
		else:
			if last.isalpha() is True and letter == " ":
				last = letter
			elif last == " " and letter.isalpha() is True:
				last = letter
			else:
				return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for w in dictionary:
		if w.startswith(sub_s):
			return True
	return False


def has_prefix2(word, find):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for w in find:
		if w.startswith(word):
			return True
	return False


if __name__ == '__main__':
	main()
