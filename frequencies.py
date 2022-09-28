"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(0,len(items)):
        items[i] = str(items[i])
        if frequencies.get(items[i]) == None:
            frequencies.update({items[i]:1})
        else:
            frequencies.update({items[i]:frequencies.get(items[i])+1})
    return frequencies
