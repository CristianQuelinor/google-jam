################ I/O ################

file_name = "B-small-practice"
output = ""

def read_input():
	global file_name
	lines = []
	inputFile = open(file_name+".in", "r")
	lines = inputFile.readlines()
	inputFile.close()
	return lines

def write_output():
	global file_name
	global output
	outputFile = open(file_name+".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + file_name + '.out"'

################ END OF I/O ################

def depth_first_search(root, tree, parents, nbChildrens):
	for e in tree[root]:
		if parents[e] == -1:
			parents[e] = root
			depth_first_search(e, tree, parents, nbChildrens)
	
		max_children_node = 0
		max1 = -float("inf")
		max2 = -float("inf")
	
		# Search for the graph with the more children
		for f in tree[root]:
			if (nbChildrens[f] > max1 and parents[f] == root):
				(max1, max_children_node) = (nbChildrens[f], f)
		
		# Search for the graph with the second more children		
		for f in tree[root]:
			if (nbChildrens[f] > max2 and parents[f] == root and f != max_children_node):
				max2 = nbChildrens[f]

	        nbChildrens[root] = max(1, 1+max1+max2)

def solve(tree, N):
	ret = 0
	
	for root in range(N):
		nbChildrens = [1 for i in range(N)]
		parents = [-1 for i in range(N)]
		parents[root] = root
		depth_first_search(root, tree, parents, nbChildrens)
		ret = max(ret, nbChildrens[root])
		
	return str(N-ret)

def solution():
	global output
	lines = read_input()

	T = int(lines[0])
	lines.remove(lines[0])

	for t in range(T): # For each test case
		N = int(lines[0])
		lines.remove(lines[0])
		
		tree = [[] for j in range(N)]
		
		for n in range(N-1):
			tmp = [int(e) for e in lines[0].split(' ')]
			tree[tmp[0]-1].append(tmp[1]-1)
			tree[tmp[1]-1].append(tmp[0]-1)
			lines.remove(lines[0])

		output += "Case #" + str(t+1) + ": " + solve(tree, N) + "\n"
		
	output = output[:-1]
	write_output()

solution()
