def push(item):
    global top
    if top > size - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack in empty!")
        return 0;
    else:
        result = stack[top]
        top -= 1
        return result

push(1)
push(2)
push(3)
item = pop()

print(pop())
print(pop())
print(pop())