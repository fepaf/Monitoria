#constants
CMD = 0
ARG = 1
COD_DIR = 2

#classes
class Stack:
    def __init__(self):
        self.size = 0
        self.stack = []
    def push(self,element):
        self.stack.append(element)
        self.size += 1
    def pop(self):
        try:
            self.stack.pop()
            self.size -= 1
            return True
        except:
            return False
    def top(self):
        try:
            return self.stack[self.size-1]
        except:
            return 'nan'

class Queue:
    def __init__(self):
        self.size = 0
        self.queue = []
    def push(self,element):
        self.queue.append(element)
        self.size += 1
    def pop(self):
        try:
            self.queue.pop(0)
            self.size -= 1
            return True
        except:
            return False
    def front(self):
        try:
            return self.queue[0]
        except:
            return 'nan'
         
#### end classes ###

#variables
n = int(input())
message = {}
aux = ''
first = ''
last = ''
potential_first = []

#building message
for i in range(n):
    cod_esq, cmd, arg, cod_dir = input().split()
    message[cod_esq] = (cmd, arg, cod_dir)
    potential_first.append(cod_esq)

#figuring out the first
for pack in message:
    try:
        potential_first.remove(message[pack][COD_DIR])
    except:
        last = message[pack][COD_DIR]
first = potential_first[0]

#doing magic
stack = Stack()
queue = Queue()
is_stack = True
is_queue = True
iterator = first

while True:
    if(message[iterator][CMD] == 'POP'):
        if(stack.top() != 'nan' and stack.top()==message[iterator][ARG]):
            stack.pop()
        else:
            is_stack = False

        if(queue.front() != 'nan' and queue.front()==message[iterator][ARG]):
            queue.pop()
        else:
            is_queue = False
    else:
        queue.push(message[iterator][ARG])
        stack.push(message[iterator][ARG])
        
    iterator = message[iterator][COD_DIR]
    if iterator == last:
        break

if(is_queue == True and is_stack == False):
    print('fila')
elif(is_queue == False and is_stack == True):
    print('pilha')
elif(is_queue == True and is_stack == True):
    print('ambas')
else:
    print('nenhuma')
