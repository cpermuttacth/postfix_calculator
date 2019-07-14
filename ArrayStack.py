class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if(self.is_empty() == True):    
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]

    def remove_even_stack(s):
        nums = []
        while not s.is_empty():
            x = s.pop()
            if x % 2 == 1:
                nums.append(x)
        for i in range(len(nums)-1,-1,-1):
            s.push(val)

    def __repr__(self):
        cur = '['
        for a in self.data:
            cur += str(a) + ', '
        cur += ']'
        return cur

    def is_balanced(input_str):
        left = "'([{'"
        right = ")]}'"
        s = ArrayStack()
        
        for char in input_str:
            if char in left:
                s.push(char)
            elif char in right:
                if s.is_empty():
                    return False
                peek = s.top()
                if right.index(char) == left.index(peek):
                    s.pop()
                else:
                    return False
        return s.is_empty()

        




