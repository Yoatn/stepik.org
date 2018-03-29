


def anagrams(word, words):
    ListOut = []
    for i in words:
        if sorted(i) == sorted(word):
            ListOut.append(i)
    return ListOut

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))