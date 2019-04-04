n = int(input())

cmds, xs, proxs, cods = 10**6*[""], 10**6*[-1], 10**6*[-1], []

xall = 0

esqs, dirs = [], []

for i in range(n):
	cod_esq, cmd, x, cod_dir = input().split()
	cod_esq, x, cod_dir = map(int,[cod_esq, x, cod_dir])
	cmds[cod_esq] , xs[cod_esq], proxs[cod_esq] = cmd, x, cod_dir
	esqs.append(cod_esq) 
	dirs.append(cod_dir)
	xall ^= (cod_esq ^ cod_dir)
	

for x in esqs:
	if (not (x in dirs)):
		first = x
		break
for x in dirs:
	if (not (x in esqs)):
		last = x
		break

mask = 3
pilha, fila = [], []

ind = first
while (ind != last):
	
	x = xs[ind]
	
	#print(ind, cmd, x)#debug
	
	if (cmds[ind]=="PUSH"):
		pilha.append(x)
		fila.append(x)
	else :
		if (pilha and pilha[-1]==x):
			pilha.pop()
		else : 
			mask &= 2
		
		if (fila and fila[0]==x):
			fila.pop(0)
		else : 
			mask &= 1
		
	ind = proxs[ind]

if (mask ==1):
	print("pilha")
elif (mask == 2):
	print("fila")
elif (mask == 3):
	print("ambas")
else : 
	print("nenhuma")
	
