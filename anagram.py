import itertools

sample = "rare"
allpossibilities = itertools.permutations(sample)
anagrams = [''.join(i) for i in allpossibilities]
print(anagrams)