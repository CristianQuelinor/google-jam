def solution():
	output = ''
	lines = []
	inputFile = open("A-small-attempt0.in", "r")
	lines = inputFile.readlines()

	N = int(lines[0])

	firstRowIndex = 0
	secondRowIndex = 0

	for i in range(0, N):
		firstRowIndex = 1 + i * 10 + int(lines[i * 10 + 1])
		secondRowIndex = i * 10 + 6 + int(lines[i * 10 + 6])
		firstRow = lines[firstRowIndex].split(' ')
		secondRow = lines[secondRowIndex].split(' ')
		firstRow[3] = firstRow[3][:-1]
		secondRow[3] = secondRow[3][:-1]
		intersection = list(set(firstRow).intersection(set(secondRow)))

		if (len(intersection) == 0):
			s = "Volunteer cheated!"
		if (len(intersection) == 1):
			s = str(intersection[0])
		if (len(intersection) > 1):
			s = "Bad magician!"

		output += 'Case #' + str(i + 1) + ': ' + s + '\n'

	output = output[:-1]
	outputFile = open("result_A-small-attempt0.out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_A-small-attempt0.out"'

solution()
