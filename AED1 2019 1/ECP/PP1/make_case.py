from random import *
import sys

param, tam = sys.argv, len(sys.argv)
pilha, fila = [], []
cmds = ["PUSH","POP"] 

op , lim = randint(0,3), 10**9

if (tam >= 2):
	n = int(param[1])

if (tam >= 3 and param[2]!='5'):
	op = int(param[2])

if (tam >= 4):
	lim = int(param[3])

pacotes = []



if (op==3 or op==0):
	p = randint(0,n//10)
	n -= p
	
	ts, n, impar = [], (n>>1), (n>>1)&1
	while (n):
		t = randint(1,n)
		ts.append(t)
		n -= t
	shuffle(ts)
	for t in ts:
		l = []
		if (t%2==1):
			x = randint(0,lim)
			l = [x]
		for i in range(t//2):
			x = randint(0,lim)
			l = [x]+l+[x]
		
		#print(l,len(l),t)
		for y in l:
			z = y if op else (randint(0,lim) if not randint(0,4) else y)
			pacotes.append([-1,"PUSH",z,-1])
		for y in l:
			z = y if op else (randint(0,lim) if not randint(0,4) else y)
			pacotes.append([-1,"POP",z,-1])
	
	for i in range(p+impar):
		x = randint(0,lim)
		pacotes.append([-1,"PUSH" if (randint(0,4)+op) else "POP",x,-1])
		
		
else :
	for i in range(n):
		cmd = cmds[randint(0,1)]

		if (op==1): #pilha
			if (cmd == "PUSH"): 
				x = randint(0,lim) 
				pilha.append(x)
				pacotes.append([-1,cmd,x,-1])
			else :
				if (pilha):
					x = pilha.pop()
					pacotes.append([-1,cmd,x,-1])
				else :
					x = randint(0,lim)
					pilha.append(x)
					pacotes.append([-1,"PUSH",x,-1])

		elif (op==2): #fila
			if (cmd == "PUSH"):
				x = randint(0,lim)
				fila.append(x)
				pacotes.append([-1,cmd,x,-1])
			else :
				if (fila):
					x = fila.pop(0)
					pacotes.append([-1,cmd,x,-1])
				else :
					x = randint(0,lim)
					fila.append(x)
					pacotes.append([-1,"PUSH",x,-1])

cod = [0]*10**6

pacotes[0][0] = randint(0,10**6-1)
cod[pacotes[0][0]] = 1

pacotes[-1][-1] = randint(0,10**6-1)
while (cod[pacotes[-1][-1]]):
	pacotes[-1][-1] = randint(0,10**6-1)
cod[pacotes[-1][-1]] = 1

for i in range(1,len(pacotes)):
	pacotes[i][0] = pacotes[i-1][-1] = randint(0,10**6-1)
	while (cod[pacotes[i][0]]):
		pacotes[i][0] = pacotes[i-1][-1] = randint(0,10**6-1)
	cod[pacotes[i][0]] = 1

shuffle(pacotes)

print(len(pacotes))
for e,cmd,x,d in pacotes:
	print(e,cmd,x,d)
