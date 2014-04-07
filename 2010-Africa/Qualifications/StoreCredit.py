def solveCase(C, I, integers):
	integerList = []
	integersSet = set([])
	cIntegersSet = set([])

	for integer in integers.split(' '):
		integerList.append(int(integer))
		integersSet.add(int(integer))
		cIntegersSet.add(C - int(integer))

	intersectionList = list(integersSet.intersection(cIntegersSet))
	
	firstItemPrice = -1
	secondItemPrice = -1
	
	firstItemIndex = -1
	secondItemIndex = -1

	for price in intersectionList:
		firstItemPrice = price
		secondItemPrice = C - firstItemPrice

		if firstItemPrice != secondItemPrice:
			break
		else:
			i = 0

			for integer in integerList:
				if firstItemPrice == integer:
					i += 1

					if (i == 2):
						break

			if (i == 2):
				break

	for index, integer in enumerate(integerList):
		if firstItemPrice == integer:
			firstItemIndex = index
		if secondItemPrice == integer:
			secondItemIndex = index

	if firstItemPrice == secondItemPrice:
		for index, integer in enumerate(integerList):
			if secondItemPrice == integer and index != firstItemPrice:
				secondItemIndex = index

	if secondItemIndex < firstItemIndex:
		(firstItemIndex, secondItemIndex) = (secondItemIndex, firstItemIndex)

	return (firstItemIndex + 1, secondItemIndex + 1)

def solution(size):
	output = ''
	lines = []
	inputFile = open("A-" + size + "-practice.in", "r")
	lines = inputFile.readlines()

	N = int(lines[0])

	for i in range(1, 3 * N + 1, 3):
		(firstItemIndex, secondItemIndex) = solveCase(int(lines[i]), int(lines[i + 1]), lines[i + 2])
		output += 'Case #' + str(i // 3 + 1) + ': ' + str(firstItemIndex) + ' ' + str(secondItemIndex) + '\n'

	output = output[:-1]
	outputFile = open("result_" + size + ".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + size + '.out"'

solution('large')
