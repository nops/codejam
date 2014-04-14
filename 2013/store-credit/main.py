name='A-large-practice.in'
file = open(name, 'r')
cases = file.readline()
cases = int(cases)
for x in range(0, cases):
    c = int(file.readline())
    i = int(file.readline())
    prices = file.readline()
    p = prices.replace("\n",'').split(' ')
    pos = [0,0]
    for a in range(0,i):
        for b in range(0,i):
            if((int(p[a])+int(p[b]))==c and a<>b):
                if(a+1<b+1):
                    pos = [a+1,b+1]
                else:
                    pos = [b+1,a+1]
    print 'Case #',x+1,':',pos[0],pos[1]
        