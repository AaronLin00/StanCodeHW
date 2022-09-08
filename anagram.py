"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dic = []
ans = []


def main():
    """
    TODO:
    """
    # start = time.time()
    ####################
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        enter = input(str('Find anagrams for: '))
        if not enter == EXIT:
            start = time.time()
            find_anagrams(enter)
            print(str(len(ans)) + ' anagrams: '+ str(ans))
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
            ans.clear()
        else:
            break
    ####################
    # end = time.time()
    # print('----------------------------------')
    # print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, "r") as f:
        for line in f:
            line1 = line.strip()
            dic.append(line1)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    s_list = []
    s_num = []
    for i in range(len(s)):
        s_list.append(s[i])
        s_num.append(i)
    # print(s_list)
    # print(s_num)
    helper(s_num, s_list, [], len(s_num))


def helper(s, word, lst, length):
    if len(lst) == length:
        check = ""
        # print(lst)
        for i in range(len(lst)):
            check += word[lst[i]]
        # print(check)
        if check in dic:
            if check not in ans:
                ans.append(check)
                print('Searching...')
                print('Found: '+check)
    else:
        check = ""
        for i in range(len(lst)):
            check += word[lst[i]]
        if len(s) < 6 or has_prefix(check):
            for num in s:
                if num in lst:
                    pass
                else:
                    lst.append(num)
                    helper(s, word, lst, length)
                    lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
