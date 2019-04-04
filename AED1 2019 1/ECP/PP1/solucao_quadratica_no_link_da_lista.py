def proximo(ind, pkg):
	for i in range(len(pkg)):
		if (pkg[i][0] == ind):
			return i
	return -1
		
pacotes, es, ds = [], [], []

n = int(input())
for i in range(n):
	e, cmd, x, d = input().split()
	e , x , d = int(e), int(x), int(d)
	pacotes.append((e,cmd,x,d))
	es.append(e)
	ds.append(d)
	
for i in range(n):
	if (not (es[i] in ds)):
		first = i
		break

pilha, fila = [], []
mask = 3

atual = first
while (atual != -1):
	e, cmd, x, d = pacotes[atual]
	if (cmd == "PUSH"):
		fila.append(x)
		pilha.append(x)
	else :
		if ((not pilha) or pilha.pop()!=x):
			mask &= 2
		if ((not fila) or fila.pop(0)!=x):
			mask &= 1
	atual = proximo(d, pacotes)
	
if (mask == 1):
	print("pilha")
elif (mask == 2):
	print("fila")
elif (mask == 3):
	print("ambas")
else : 
	print("nenhuma")
