#creating simple stack with default methods
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self): 
        if not (self.isEmpty()):
            return self.elements.pop()
        else:
            # print("stack already empty")
            return self.elements

    def isEmpty(self):
        return len(self.elements) == 0

    def __iter__(self):
        return reversed(self.elements)

    def __str__(self):
        return str(list(iter(self)))


# creating a stack only for integer values with default methods
class IntegerStack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        try:
            self.elements.append(int(item)) # fixed bug with pushing float number with string type like "6.234"
            return self.elements
       
        except:
            # print("not a integer")
            return self.elements



    def pop(self):
        if not (self.isEmpty()):
            return self.elements.pop()
        else:
            # print("stack already empty")
            return self.elements

    def isEmpty(self):
        return len(self.elements) == 0

    def __iter__(self):
        return reversed(self.elements)

    def __str__(self):
        return str(list(iter(self)))


# Executing the IntegerStack class methods
def main():

    my_stack = IntegerStack()

    print('try to push differ values')
    my_stack.push(0.45)
    my_stack.push('46')
    my_stack.push('0.23')

    print(my_stack)
    print('try to pop')
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()

    print(my_stack)


    if my_stack.isEmpty():
        print("stack empty")
    else:
        print("stack not empty")
    print(my_stack)


if __name__ == '__main__':
    main()