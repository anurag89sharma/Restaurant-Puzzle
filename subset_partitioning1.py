import time
import pprint
from itertools import chain, combinations

def subsets(arr):
	""" Note this only returns non empty subsets of arr"""
	return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])

def k_subset(arr, k):
	s_arr = sorted(arr)
	return set([frozenset(i) for i in combinations(subsets(arr),k) if sorted(chain(*i)) == s_arr])


'''
print all the subset partitions of a given list and calculate time to execute it
'''
def test():
	lis = [1,2,3,4,5]
	print lis
	start = time.time()
	for i in xrange(1,len(lis)+1):
		# get all the subset patitions of length i
		partitions = k_subset(lis,i)
		print "Number of partitions of length %s: %s" % (i, len(partitions))
		#pprint.pprint(k_subset(lis,i))

	end = time.time()
	print "Time elapsed: %s" % (end-start)

if __name__ == '__main__':
	test()


