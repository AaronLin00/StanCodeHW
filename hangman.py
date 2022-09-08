"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Run the first round and operate hangman fun
    """
    ans = random_word()
    count = N_TURNS
    dashed = '-' * len(ans)
    print("THe word looks like " + str(dashed))
    print("You have " + str(count) + " wrong guesses left.")
    input_ch = str(input("Your guess: "))
    input_ch = input_ch.upper()
    while not len(input_ch) == 1 or not input_ch.isalpha():
        print("Illegal format.")
        input_ch = str(input("Your guess: "))
        input_ch = input_ch.upper()
    hangman(ans, dashed, input_ch, count)


def hangman(ans, dashed, input_ch, count):
    """
    line 45-63 is used to operate first time, this can fill up new_dash.
    line 63-END help update new_dash and show game progress
    """
    new_dash = ""
    if input_ch in ans:
        print("You are correct! ")
        for j in range(len(ans)):
            if input_ch == ans[j]:
                new_dash += input_ch
            else:
                new_dash += dashed[j]
        print("THe word looks like " + str(new_dash))
        print("You have " + str(count) + " wrong guesses left.")
    else:
        count -= 1
        print("There is no " + str(input_ch)+"'s in the word.")
        new_dash = '-' * len(ans)
        print("THe word looks like " + str(new_dash))
        print("You have " + str(count) + " wrong guesses left.")
    input_ch = str(input("Your guess: "))
    input_ch = input_ch.upper()
    while not len(input_ch) == 1 or not input_ch.isalpha():
        print("Illegal format.")
        input_ch = str(input("Your guess: "))
        input_ch = input_ch.upper()
    while count > 0:
        if input_ch in ans:
            new_dash2 = ""
            print("You are correct! ")
            for j in range(len(ans)):
                if new_dash[j] != ans[j]:
                    if input_ch == ans[j]:
                        new_dash2 += input_ch
                    else:
                        new_dash2 += dashed[j]
                else:
                    if new_dash[j].isalpha():
                        new_dash2 += new_dash[j]
                    else:
                        pass
            new_dash = new_dash2
            if not new_dash == ans:
                print("THe word looks like " + str(new_dash))
                print("You have " + str(count) + " wrong guesses left.")
                input_ch = str(input("Your guess: "))
                input_ch = input_ch.upper()
                while not len(input_ch) == 1 or not input_ch.isalpha():
                    print("Illegal format.")
                    input_ch = str(input("Your guess: "))
                    input_ch = input_ch.upper()
            else:
                break
        else:
            count -= 1
            if count != 0:
                print("There is no " + str(input_ch) + "'s in the word.")
                print("THe word looks like " + str(new_dash))
                print("You have " + str(count) + " wrong guesses left.")
                input_ch = str(input("Your guess: "))
                input_ch = input_ch.upper()
                while not len(input_ch) == 1 or not input_ch.isalpha():
                    print("Illegal format.")
                    input_ch = str(input("Your guess: "))
                    input_ch = input_ch.upper()
            else:
                print("There is no " + str(input_ch) + "'s in the word.")
    if new_dash == ans:
        print("You win!!")
    else:
        print("You are completely hung : (")
    print("THe word was: " + str(ans))


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
