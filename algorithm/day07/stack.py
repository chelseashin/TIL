def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("Stack is empty!")
        return
    else:
        return s.pop(-1)
        # return s.pop()  # 위와 같은 의미

s = []
push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())