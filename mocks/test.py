#!/usr/bin/python3



def push_stack(stack, pos, valor, s):
        if s == 1:
                if stack[0+pos[0]] == None:
                        stack[0+pos[0]] = valor
                        print(stack)
                        pos[0] += 1
                else:
                        print("no more space")
        if s == 2:
                if stack[len(stack)-1-pos[1]] == None:
                        stack[len(stack)-1-pos[1]] = valor
                        print(stack)
                        pos[1] += 1
                else:
                        print("no more space")

def pop_stack(stack, pos, s):
        if s == 1:
                a = pos[0] - 1
                stack[a] = None
        print(stack)

stack = []
for i in range(5):
        stack.append(None)
pos = [0, 0]
valor = 1
s = 1

push_stack(stack, pos, valor, s)
valor = 1
s = 2
push_stack(stack, pos, valor, s)

valor = 5
s = 2
push_stack(stack, pos, valor, s)

valor = 8
s = 1
push_stack(stack, pos, valor, s)

valor = "a"
s = 1
push_stack(stack, pos, valor, s)



pop_stack(stack, pos, s)

