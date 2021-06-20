from collections import Counter

def sherlockAndAnagrams(ss):
    counts = Counter(ss)
    anagrams = 0
    for k in counts:
        anagrams += k // 2

    return anagrams
