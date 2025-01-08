"""A stack is a linear data structure
that stores items in a Last-In/First-Out (LIFO)
or First-In/Last-Out (FILO) manner.
In stack, a new element is added at one end
and an element is removed from that end only.
The insert and delete operations are
often called push and pop."""

#A data structure described as LIFO is actually a:
#stack


# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty