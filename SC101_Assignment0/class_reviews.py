"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    Use eight variables to find max, min and avg. The function can also detect whether the scores were entered
    """
    max001 = 0
    min001 = 0
    count001 = 0
    total001 = 0
    max101 = 0
    min101 = 0
    count101 = 0
    total101 = 0
    while True:
        c = str(input("Which class? "))
        c = c.upper()
        if c != "-1":
            s = int(input("Score: "))
            if c == "SC001":
                total001 += s
                count001 += 1
                if not max001 == 0:
                    if s >= max001:
                        max001 = s
                    if s <= min001:
                        min001 = s
                else:
                    max001 = s
                    min001 = s
            if c == "SC101":
                total101 += s
                count101 += 1
                if not max101 == 0:
                    if s > max101:
                        max101 = s
                    if s < min101:
                        min101 = s
                else:
                    max101 = s
                    min101 = s
        elif count001 == 0 and count101 == 0:
            print("No class scores were entered")
            break
        else:

            if count001 != 0:
                print("=============SC001=============")
                print("Max (001): " + str(max001))
                print("Min (001): " + str(min001))
                print("Avg (001): " + str((total001/count001)))
            else:
                print("=============SC001=============")
                print("No score for SC001")
            if count101 != 0:
                print("=============SC101=============")
                print("Max (101): " + str(max101))
                print("Min (101): " + str(min101))
                print("Avg (101): " + str((total101/count101)))
            else:
                print("=============SC101=============")
                print("No score for SC101")
            break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
