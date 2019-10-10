from cs50 import get_string
from sys import argv
import sys


def main():

    while True:  # Checks for correct arguments
        if len(argv) == 2:
            break
        else:
            print("Usage: python bleep.py dictionary")
            sys.exit(1)

    dictionary = sys.argv[1]  # reads dicionary
    infile = open(dictionary, "r")

    banned_words = set()

    for x in infile:  # Adds dictionary to set()
        x = x.strip("\n")
        banned_words.add(x)

    infile.close()

    message = get_string("What message would you like to censor? ")
    tokens = message.split()

    for word in tokens:  # Iterates over words in token and copares them to dictionary
        if word.lower() in banned_words:
            print("*" * len(word), end=" ")
        else:
            print(word, end=" ")

    print()


if __name__ == "__main__":
    main()