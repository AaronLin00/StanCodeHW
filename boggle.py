"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = []
enter = [[], [], [], []]
def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	read_dictionary()
	enter_word()
	find_word()
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def enter_word():
	for i in range(4):
		enter_alpha = input(str(str(i+1) + ' row of letters: '))
		enter_alpha = enter_alpha.lower()
		if len(enter_alpha) == 7:
			if enter_alpha[1] == " " and enter_alpha[3] == " " and enter_alpha[5] == " ":
				enter[i].append(enter_alpha[0])
				enter[i].append(enter_alpha[2])
				enter[i].append(enter_alpha[4])
				enter[i].append(enter_alpha[6])
			else:
				print('Illegal input')
				break
		else:
			print('Illegal input')
			break


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, "r") as f:
		for line in f:
			line1 = line.strip()
			dic.append(line1)


def find_word():
	visited = []
	ans = []
	for i in range(4):
		for j in range(4):
			for x in range(4):
				visited.append([])
				for y in range(4):
					visited[x].append(False)
			cur_lst = enter[j][i]
			helper(i, j, cur_lst, visited, ans)
	print('There are ' + str(len(ans)) + ' words in total.')


def helper(x, y, cur_word, visited, ans):
	# print(x, y)
	# print(cur_word)
	visited[y][x] = True
	if cur_word in dic and len(cur_word) >= 4:
		if cur_word not in ans:
			print('Found: ' + cur_word)
			ans.append(cur_word)
	next1 = get_coordinate(x, y)
	# print("x, y= {}, {}, next cord = {}".format(x, y, next1))
	for next_coordinate in next1:
		next_x = next_coordinate[0]
		next_y = next_coordinate[1]
		if visited[next_y][next_x] == True:
			continue
		next_word = cur_word + enter[next_y][next_x]
		if has_prefix(next_word) == False:
			continue
		helper(next_x, next_y, next_word, visited, ans)
	visited[y][x] = False


def get_coordinate(x, y):
	ans = []
	if 0 <= x-1 < 4 and 0 <= y-1 < 4:
		ans.append((x - 1, y - 1))
	if 0 <= x < 4 and 0 <= y-1 < 4:
		ans.append((x, y - 1))
	if 0 <= x+1 < 4 and 0 <= y - 1 < 4:
		ans.append((x+1, y-1))
	if 0 <= x-1 < 4 and 0 <= y < 4:
		ans.append((x-1, y))
	if 0 <= x+1 < 4 and 0 <= y < 4:
		ans.append((x+1, y))
	if 0 <= x-1 < 4 and 0 <= y + 1 < 4:
		ans.append((x-1, y+1))
	if 0 <= x <4 and 0 <= y+1 < 4:
		ans.append((x, y + 1))
	if 0 <= x+1 < 4 and 0 <= y + 1 < 4:
		ans.append((x+1, y + 1))
	return ans


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
