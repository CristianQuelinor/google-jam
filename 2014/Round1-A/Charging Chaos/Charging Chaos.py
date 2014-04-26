################ I/O ################

file_name = "A-large-practice"
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

def solve(L, outlets, devices):
	xor_map = [[[(device[l]+outlet[l])%2 for l in range(L)] for device in devices] for outlet in outlets]
	
	inter = xor_map[0]
	
	# Not optimal but it works
	for e in xor_map:
		inter = [x for x in e if x in inter]
		
	mini = L+1
	
	for xor in inter:
		mini = min(sum(xor), mini)

	return "NOT POSSIBLE" if mini == L+1 else str(mini)

def solution():
	global output
	lines = read_input()

	T = int(lines[0])
	lines.remove(lines[0])

	for t in range(T): # For each test case
		tmp = [int(e) for e in lines[0].split(' ')]
		(N, L) = (tmp[0], tmp[1])
		lines.remove(lines[0])
		
		outlets = [[int(e[l]) for l in range(L)] for e in lines[0].split(' ')]
		lines.remove(lines[0])

		devices = [[int(e[l]) for l in range(L)] for e in lines[0].split(' ')]
		lines.remove(lines[0])

		output += "Case #" + str(t+1) + ": " + solve(L, outlets, devices) + "\n"
		
	output = output[:-1]
	write_output()

solution()
