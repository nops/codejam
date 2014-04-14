name='practice.in'
file = open(name, 'r')
cases = file.readline()
cases = int(cases)
for x in range(0, cases):
	line = file.readline()
	values = line.split(' ')
	q = int(values[0])
	elements = []
	bases = []
	for a in range(0, q):
		bases.append(values[a+1])
		for e in values[a+1]:
			elements.append(e)
	
	o = int(values[q+1])
	opposes = []
	for b in range(0, o):
		opposes.append(values[q+b+2])
		
	s = int(values[q+o+2])
	sequence = values[q+o+3]
	
	nbases = {}
	for base in bases:
		val1 = base[0:2]
		val2 = base[1:2]+base[0:1]
		nbases[val1] = base[2:3]
		nbases[val2] = base[2:3]
	
	final = []
	i = 0
	sequence = sequence.rstrip('\n')
	combined = False
	rseq = []
	for l in sequence:
		i = i+1
		
		opo = []
		rseq.append(l)
			
		if combined is True:
			combined = False
			rseq.pop()
			continue
			
		if(i >= len(sequence)):
			next = ''
		else:
			next = sequence[i]
			
		t = l+next
		if(t in nbases):
			final.append(nbases[t])
			combined = True
			for el in rseq:
				if el not in elements:
					opo.append(el)
			rseq = []
			
		if t in opposes:
			for el in opo:
				final.remove(el)
			if combined is True:
				final.pop()
			else:
				combined = True
		
		if combined is False:	
			final.append(l)
		
		if len(rseq) > 0:
			t1 = rseq[0]+l
			for el in rseq:
				t1 = el+l
				if t1 in opposes:
					for r in range(0, len(rseq)):
						if len(final) > 0:
							final.pop()
		else:
			t1 = ''
		
	print 'Case #'+str(x+1)+': '+str(final)
			