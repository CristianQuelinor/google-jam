################ I/O ################

file_name = "B-large"
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

def solve(a, b, k):
	ret = 0
	
	for i in range(a):
		for j in range(b):
			if i&j < k:
				ret += 1
				
	return str(ret)

def solution():
	global output
	lines = read_input()

	T = int(lines[0])
	lines.remove(lines[0])

	for t in range(T): # For each test case
		[a, b, k] = [int(e) for e in lines[0].split(' ')]
		lines.remove(lines[0])

		output += "Case #" + str(t+1) + ": " + solve(a, b, k) + "\n"
		
	output = output[:-1]
	write_output()

solution()
