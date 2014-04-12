def scalarProduct(v1, v2):
	ret = 0

	for i, j in zip(v1, v2):
		ret += i * j

	return ret

def minimize(size, v1, v2):
	vector1 = v1.split(' ')
	vector2 = v2.split(' ')
	
	for i in range(0, size):
		vector1[i] = int(vector1[i])
		vector2[i] = int(vector2[i])

	vector1.sort()
	vector1 = vector1[::-1]
	vector2.sort()

	return scalarProduct(vector1, vector2)

def solution(size):
	output = ''
	lines = []
	inputFile = open("A-" + size + "-practice.in", "r")
	lines = inputFile.readlines()

	N = int(lines[0])

	for i in range(1, 3 * N + 1, 3):
		minimalScalarProduct = minimize(int(lines[i]), lines[i + 1], lines[i + 2])
		output += 'Case #' + str(i // 3 + 1) + ': ' + str(minimalScalarProduct) + '\n'

	output = output[:-1]
	outputFile = open("result_" + size + ".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + size + '.out"'

solution('large')
