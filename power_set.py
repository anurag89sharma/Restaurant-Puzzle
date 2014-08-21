import pprint
from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))


lis1 = [1,2,3]
lis2 = [[1,2],[2,3],[3],[1],[2]]
set1 = list(powerset(lis2))

# get all combinations of lis2 such that all items of lis1 should present in the combination
list_subset1 = filter(lambda s: set(sum(s,[])) == set(lis1), powerset(lis2))
print len(list_subset1)

# generate powerset of lis2
list_subset2 = list(powerset(lis2))
print len(list_subset2)
