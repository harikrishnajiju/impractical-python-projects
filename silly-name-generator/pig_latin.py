"""A program to for Pig Latin."""
import sys

VOWELS = 'aeiou'

while True:
    print("Welcome to Pig Latin Word Converter")
    word = input("enter a word:\n")
    if word[0].lower() in VOWELS:
        pig_latin = word + 'way'
    else:
        pig_latin = word[1:] + word[0] + 'ay'
    print("\n")
    print(f"{pig_latin}", file=sys.stderr)

    try_again = input("Would you like to try again? (press Enter/n to exit)")
    if try_again.lower() == 'n':
        sys.exit()
