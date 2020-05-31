

file = open('test.lik', 'r')
for line in file:
    noenter = line.replace('\n','')
    noenter =noenter.rstrip()
   
    noenter =noenter.split(' ')
    shape= noenter[0]
    boja = noenter[1]
    tocke = noenter[2:]
    tocke =[float(item) for item in tocke]
    print(boja)
    print(shape)
    print(tocke)