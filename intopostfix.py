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
        


def inToPost(finalExpression):
     global inArray                         
     while inArray:
          if inArray[0] == "(":
               stack.push(inArray[0])
               del inArray[0]
               return inToPost(finalExpression)
          elif inArray[0] == ")":
               currentToken = stack.peek()
               while currentToken != "(":
                    finalExpression = finalExpression + stack.pop()
                    currentToken = stack.peek()
               openingBracket = stack.pop()
               del openingBracket
               del inArray[0]
               return inToPost(finalExpression)
          else:
               pass
     
          while inArray[0].isalpha():
               finalExpression = finalExpression + inArray[0]
               del inArray[0]
               return inToPost(finalExpression)
          if not stack.isEmpty():
               if (bodmas[inArray[0]] <= bodmas[stack.peek()]):
                    stack.push(inArray[0])
                    del inArray[0]
                    return inToPost(finalExpression)

               else:
                    while (stack.peek() != "(") and (not stack.isEmpty()) and (bodmas[inArray[0]] > bodmas[stack.peek()]):
                         finalExpression = finalExpression + stack.pop()
                    stack.push(inArray[0])
                    del inArray[0]
                    return inToPost(finalExpression)
          else:
               stack.push(inArray[0])
               del inArray[0]
               return inToPost(finalExpression)
     for i in range(stack.size()):
          finalExpression = finalExpression + stack.pop()
     print(finalExpression)


stack = Stack()
userInput = input("Enter infix notation: ")
inArray = list(userInput)
finalExpression = ""

bodmas = {"(":0,"*":1,"/":1,"+":2,"-":2}         
inToPost(finalExpression)


            
            
        
    
