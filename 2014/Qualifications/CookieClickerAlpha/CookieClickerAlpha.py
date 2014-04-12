def solve(C, F, X):
	nbCookies = float(0)
	time = float(0)
	productionRate = 2
	
	# If buying a farm is more expensive than the required number of cookie
	
	if X <= C:
		return str(round(float(X / 2), 7))
	
	while (nbCookies < X):
		diff = C - nbCookies
		
		if (diff > 0):
			nbCookies += diff
			time += diff/productionRate
			
		# At this point we have enough cookie to buy a farm if it's worth it
		
		remainingCookiesWithoutBuyingFarm = X - nbCookies
		remainingTimeWithoutBuyingFarm = remainingCookiesWithoutBuyingFarm / productionRate
		
		remainingCookiesWhenBuyingFarm = X - nbCookies + C
		remainingTimeWhenBuyingFarm = remainingCookiesWhenBuyingFarm / (productionRate + F)
		
		if (remainingTimeWhenBuyingFarm < remainingTimeWithoutBuyingFarm): # If it's strictly better to buy a farm
			nbCookies -= C
			productionRate += F
		else: # It is not going to get better later, so we can just wait the end with what we have
			return str(round(time + remainingTimeWithoutBuyingFarm, 7))

def solution(file):
	output = ''
	lines = []
	inputFile = open(file + ".in", "r")
	lines = inputFile.readlines()

	N = int(lines[0])

	for i in range(1, N + 1):
		line = lines[i].split(' ')
		output += 'Case #' + str(i) + ': ' + solve(float(line[0]), float(line[1]), float(line[2])) + '\n'

	output = output[:-1]
	outputFile = open("result_" + file + ".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + file + '.out"'

solution("B-large")
