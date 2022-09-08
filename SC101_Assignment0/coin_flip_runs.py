"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Use 0 and 1 to represent T and H, randrange can give out 0 or 1 in random.
	Use True and False as a switch to control whether the numbers is continuous.
	"""
	print("Let's flip a coin!")
	run = int(input("Number of runs: "))
	roll1 = r.randrange(0, 2)
	if roll1 == 0:
		print("T", end="")
	else:
		print("H", end="")
	count = 0
	switch = False
	while count != run:
		roll2 = r.randrange(0, 2)
		if roll2 == 0:
			print("T", end="")
		else:
			print("H", end="")
		if roll1 == roll2:
			if not switch:
				count += 1
				switch = True
		else:
			switch = False
		roll1 = roll2


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
