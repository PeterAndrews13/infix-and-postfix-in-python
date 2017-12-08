class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
stack = Stack()


userInput = input("Enter postfix notation: ")
postArray = list(userInput)
#postArray = ["A","B","C","+","*"]
def postToIn():
    while postArray:
        while postArray[0].isalpha():
            stack.push(postArray[0])
            del postArray[0]
        operator = postArray[0]
        temp = stack.pop()
        new = stack.pop()
        new = "(" + new + operator + temp + ")"
        stack.push(new)
        del postArray[0]
        if not postArray:
            new = new[1:-1]
            print(new)
        else:
            postToIn()

postToIn()
