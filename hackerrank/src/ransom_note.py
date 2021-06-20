from collections import Counter

def ransomeNote(magazine, note):
    if Counter(note) - Counter(magazine) == {}:
        return 'Yes'
    return 'No'
