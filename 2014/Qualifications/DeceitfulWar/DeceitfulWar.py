def solveWar(N, naomi, ken):
	score = 0
	
	for i in range(0, N):
		(chosenNaomi, chosenKen) = choiceWar(naomi, ken)
		naomi.remove(chosenNaomi)
		ken.remove(chosenKen)
		
		if (chosenNaomi> chosenKen):
			score += 1
			
	return score

def choiceWar(naomi, ken):
	chosenNaomi = naomi[0]
	kenPossibilities = [e for e in ken if e > chosenNaomi]
	chosenKen = min(ken) if len(kenPossibilities) == 0 else min(kenPossibilities)
	
	return (chosenNaomi, chosenKen)

def solveDeceitfulWar(N, naomi, ken):
	score = 0
	
	for i in range(0, N):
		(chosenNaomi, chosenKen) = choiceDeceitfulWar(naomi, ken)
		naomi.remove(chosenNaomi)
		ken.remove(chosenKen)


		if (chosenNaomi > chosenKen):
			score += 1
	
	return score

def choiceDeceitfulWar(naomi, ken):
	maxNaomi = max(naomi)
	kenHasBetter = False
	
	for e in ken:
		if e > maxNaomi:
			kenHasBetter = True
			break
			
	# Ken has heavier blocks than the heaviest of Naomi
	# Naomi chooses its lightest block and tells Ken its weight is just under Ken's heaviest block
	if (kenHasBetter == True):
		return (min(naomi), max(ken))
	# Otherwise Naomi has the heaviest block, she gets rid of her lightest block heavier than Ken's lightest
	else:
		kenLightest = min(ken)
		chosenNaomi = min([e for e in naomi if e > kenLightest])
		return (chosenNaomi, min(ken))

def solution(file):
	output = ''
	lines = []
	inputFile = open(file + ".in", "r")
	lines = inputFile.readlines()

	T = int(lines[0])

	for i in range(0, T):
		N = int(lines[1+3*i])
		naomi1 = sorted([float(e) for e in lines[2+3*i].split(' ')])
		ken1 = sorted([float(e) for e in lines[3+3*i].split(' ')])
		naomi2 = list(naomi1)
		ken2 = list(ken1)
		output += 'Case #' + str(i+1) + ': ' + str(solveDeceitfulWar(N, naomi1, ken1)) + " " + str(solveWar(N, naomi2, ken2)) + '\n'

	output = output[:-1]
	outputFile = open("result_" + file + ".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + file + '.out"'

solution("D-large-practice")
