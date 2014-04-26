################ I/O ################

file_name = "C-small-practice"
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

def solve(permutation, N):
	a = 0
	
	for i, j in enumerate(permutation):
		if j <= i:
			a += 1
	
	if a < 484: # Why 484 ? See stats.py
		return "BAD"
	else:
		return "GOOD"

def solution():
	global output
	lines = read_input()

	T = int(lines[0])
	lines.remove(lines[0])

	for t in range(T): # For each test case
		N = int(lines[0])
		lines.remove(lines[0])
		
		permutation = [int(e) for e in lines[0].split(' ')]
		lines.remove(lines[0])

		output += "Case #" + str(t+1) + ": " + solve(permutation, N) + "\n"
		
	output = output[:-1]
	write_output()

solution()
