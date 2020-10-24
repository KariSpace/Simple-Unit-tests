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


class IntegerStack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        try:
            int(item)
            self.elements.append(item)
        except:
            print("not a string")
            pass


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

    my_stack = IntegerStack()

    print('try to push differ values')
    my_stack.push(45)
    my_stack.push('79')
    my_stack.push('c')
    my_stack.push('0.23')

    print(my_stack)
    print('try to pop')
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()

    print(my_stack)


    if my_stack.isEmpty():
        print("stack empty")
    else:
        print("stack not empty")
    print(my_stack)


if __name__ == '__main__':
    main()