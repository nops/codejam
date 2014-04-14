name='practice.in'
file = open(name, 'r')
cases = file.readline()
cases = int(cases)
for case in range(0, cases):
	answer1 = int(file.readline())
	grid1 = [[0 for x in xrange(4)] for x in xrange(4)]
	for i in range(0, 4):
		line = file.readline()
		grid1[i] = line.rstrip('\n').split(' ')
		
	answer2 = int(file.readline())
	grid2 = [[0 for x in xrange(4)] for x in xrange(4)] 
	for i in range(0, 4):
		line = file.readline()
		grid2[i] = line.rstrip('\n').split(' ')
		
	answer = list(set(grid1[answer1-1]).intersection(set(grid2[answer2-1])))
	if len(answer) == 1:
		print 'Case #'+str(case+1)+': '+answer[0]
	elif len(answer) > 1:
		print 'Case #'+str(case+1)+': Bad magician!'    
	else:
		print 'Case #'+str(case+1)+': Volunteer cheated!'