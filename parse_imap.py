def parse_imap(IMAP):
	'''parse the IMAP string into a int list'''
	## e.g.'1,3:5,7,10:12,15'
	tokens_1 = IMAP.split(',')
	## tokens = ['1', '3:5', '7', '10:12', '15'] 
	tokens = [token.split(':') for token in tokens_1]
	## tokens = [['1'], ['3', '5'], ['7'], ['10', '12'], ['15']]
	
	imap_list = list()
	for token in tokens:
		imap_list += range(int(token[0]), int(token[-1]) + 1)

	return imap_list
	## finally we will get imap_list = [1, 3, 4, 5, 7, 10, 11, 12, 15]


