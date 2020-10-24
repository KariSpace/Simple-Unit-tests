class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if not (self.isEmpty()):
            return self.elements.pop()
        else:
            print("stack already empty")
            return self.elements

    def isEmpty(self):
        return len(self.elements) == 0

    def __iter__(self):
        return reversed(self.elements)

    def __str__(self):
        return str(list(iter(self)))

def main():

    my_stack = Stack()

    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')

    print(my_stack)

    my_stack.pop()
    my_stack.pop()
    my_stack.pop()

    print(my_stack)
    if my_stack:
        print("stack not empty")
    my_stack.pop()

    if my_stack.isEmpty():
        print("stack empty")

if __name__ == '__main__':
    main()