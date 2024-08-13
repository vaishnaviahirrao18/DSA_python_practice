stack1 = []
stack2 = []
stack3 = []

def push(stack, item):
    if item is not None:  # Only push non-None items
        stack.append(item)

def pop(stack):
    if stack:
        return stack.pop()

push(stack1, 3)
push(stack1, 2)
push(stack1, 1)
print("Before")
print(stack1)
print(stack2)
print(stack3)
push(stack3, pop(stack1))   
print("stack1",stack1)
print("stack2",stack2)
print("stack3",stack3)

push(stack2, pop(stack1))   
print("pass2")
print("stack1",stack1)
print("stack2",stack2)
print("stack3",stack3)
push(stack2, pop(stack3))  
print("pass3")
print("stack1",stack1)
print("stack2",stack2)
print("stack3",stack3)
push(stack3, pop(stack1))  
print("pass4")
print("stack1",stack1)
print("stack2",stack2)
print("stack3",stack3)
push(stack1, pop(stack2))  
print("pass5")
print("stack1",stack1)
print("stack2",stack2)
print("stack3",stack3)
push(stack3, pop(stack2))  
print("pass6")
print("stack1",stack1)
print("stack2",stack2)
print("stack3",stack3)
push(stack3, pop(stack1))  

print("\nFinal stacks:")
print("Stack 1:", stack1)
print("Stack 2:", stack2)
print("Stack 3:", stack3)

