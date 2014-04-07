def solution(size):
	output = ''
	lines = []
	inputFile = open("B-" + size + "-practice.in", "r")
	lines = inputFile.readlines()

	N = int(lines[0])

	for i in range(1, N + 1):
		words = lines[i].split(' ')
		words = words[::-1]
		words[0] = words[0][:-1]
		output += 'Case #' + str(i) + ': ' + ' '.join(words) + '\n'

	output = output[:-1]
	outputFile = open("result_" + size + ".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + size + '.out"'

solution('large')
