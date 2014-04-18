################ I/O ################

file_name = "B-large-practice"
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

def solve(N, M, prefs, malted):
	sol = [0] * N
	m = 0
	while (m < M):
		satisfied = False
		
		if (malted[m] != -1):
			if (sol[malted[m]] == 1):
				m += 1
				continue
		
		for n in range(N):
			if (prefs[m][n] == 1) and sol[n] == 0:
				satisfied = True
				break
				
		if (satisfied == True):
			m += 1
			continue
			
		if (malted[m] == -1):
			return "IMPOSSIBLE"
		else:
			sol[malted[m]] = 1
			m = 0
			
	return ' '.join([str(e) for e in sol])

def solution():
	global output
	lines = read_input()

	C = int(lines[0])
	lines.remove(lines[0])

	for c in range(C): # For each test case
		N = int(lines[0]) # Number of milshakes
		lines.remove(lines[0])
		M = int(lines[0]) # Number of customers
		lines.remove(lines[0])

		prefs = [[0 for n in range(N)] for m in range(M)]
		malted = [-1 for e in range(M)]

		for m in range(M):
			tmp = [int(e) for e in lines[0].split(' ')]
			T = tmp[0]
			tmp.remove(tmp[0])
			
			for t in range(T):
				X = tmp[0]
				tmp.remove(tmp[0])
				Y = tmp[0]
				tmp.remove(tmp[0])

				if (Y == 1):
					malted[m] = X-1
				else:
					prefs[m][X-1] = 1

			lines.remove(lines[0])

		output += "Case #" + str(c+1) + ": " + solve(N, M, prefs, malted) + "\n"
		
	output = output[:-1]
	write_output()

solution()
		
