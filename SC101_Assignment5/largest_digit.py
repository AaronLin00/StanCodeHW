"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	helper(n, 0)
	return helper(n, 0)


def helper(n, big):
	if n < 0:
		n = -n
	if n == 0:
		ans = big
		return ans

	else:
		num = n % 10
		if big < num:
			big = num
		return helper(n//10, big)



if __name__ == '__main__':
	main()
