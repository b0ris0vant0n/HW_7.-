class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.item = item
        self.stack.append(self.item)

    def pop(self):
        self.stack.pop()
        return self.stack

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


BRACKETS = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def balance_checking(string_):
    stack = Stack()
    for item_ in string_:
        if item_ in BRACKETS:
            stack.push(item_)
        elif item_ == BRACKETS.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансированно'
    return 'Сбалансировано'


if __name__ == "__main__":
    print(balance_checking('(({}))'))
