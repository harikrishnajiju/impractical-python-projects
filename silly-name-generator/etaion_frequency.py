"""Map letters from a string into a dictionary and display their frequence in a bar graph."""
# """Poor Man's Bar Graph"""
import sys
import pprint
from collections import defaultdict

TEXT = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly!
mapped = defaultdict(list)
for character in TEXT:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)

# pprint lets you print stacked output
print(f"text= {TEXT}", file=sys.stderr)
print("Alphaet frequency:")
pprint.pprint(mapped, width=110)
