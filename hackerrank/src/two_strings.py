from collections import Counter

inp = [['hello', 'world'], ['hi', 'world'],
        ['wouldyoulikefries', 'abcabcabcabcabcabc'],
        ['hackerrankcommunity', 'cdecdecdecde'],
        ['jackandjill', 'wentupthehill'],
        ['writetoyourparents', 'fghmqzldbc'],
        ['beetroot', 'sandals'],
        ['aardvark', 'apple'],
    ]

def twoStrings(s1, s2):
    count_s1, count_s2 = list(map(Counter, [s1, s2]))
    for k in count_s1:
        if count_s2.get(k):
            return 'YES'
    return 'NO'

print(list(map(lambda x: twoStrings(*x), inp)))
