import random

def bad_algo(N):
	perm = range(N)
	
	for k in range(N):
		p = random.randint(0, N-1)
		(perm[k], perm[p]) = (perm[p], perm[k])
		
	return perm

def good_algo(N):
	perm = range(N)
	
	for k in range(N):
		p = random.randint(k, N-1)
		(perm[k], perm[p]) = (perm[p], perm[k])
		
	return perm

nb_tests = 100	
tot_bad = 0	
tot_good = 0

for i in range(nb_tests):
	perm = bad_algo(1000)
	tot_bad += sum(j<i for i, j in enumerate(perm))
	perm = good_algo(1000)
	tot_good += sum(j<i for i, j in enumerate(perm))
	
print "bad algo", tot_bad // nb_tests
print "good algo", tot_good // nb_tests
print "value to use", (tot_bad // nb_tests)+((tot_good-tot_bad) // (2*nb_tests))
