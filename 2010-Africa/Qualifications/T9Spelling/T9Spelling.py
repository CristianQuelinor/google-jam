def convert(line):
	mapping = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}
	groups = {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1, 'f': 1, 'g': 2, 'h': 2, 'i': 2, 'j': 3, 'k': 3, 'l': 3, 'm': 4, 'n': 4, 'o': 4, 'p': 5, 'q': 5, 'r': 5, 's': 5, 't': 6, 'u': 6, 'v': 6, 'w': 7, 'x': 7, 'y': 7, 'z': 7, ' ': 8, '': 9}
	ret = ''
	prev = ''

	for letter in line:
		if (letter != '\n'):
			if groups[prev] == groups[letter]:
				ret += ' '

			ret += mapping[letter]

			prev = letter

	return ret

def solution(size):
	output = ''
	lines = []
	inputFile = open("C-" + size + "-practice.in", "r")
	lines = inputFile.readlines()

	N = int(lines[0])

	for i in range(1, N + 1):
		output += 'Case #' + str(i) + ': ' + convert(lines[i]) + '\n'

	output = output[:-1]
	outputFile = open("result_" + size + ".out", "w")
	outputFile.write(output)
	outputFile.close()

	print 'Ouput file is "result_' + size + '.out"'

solution('large')
