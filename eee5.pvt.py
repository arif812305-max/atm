'''
d={"ir":200,"kkk":200,"ddd":564,}
print(d.items())
print(type(d))
     
l=[1,2,3,4,5,6,7]
l.append(1)
print(l)
ATM P

l=[1,2,3,4,5,6,7]
l.pop(1)
print(l)

d={"name":"kaif","age":"19","status":"unmarried",}
print(d)
print(d["name"])
d["age"]
print(d.keys)
print(d.values())
print(d.items())
d.update({"gender":"male"})
print(d)

print("**********************************"

i={12,14,15,48,5,9,15}
l=list(map(int,input().split()))
even_count=0
odd_count=0
for i in l:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print("no of even elements",even_count)
print("no of odd elements",odd_count)


print("++++++++++++++++++++++++++++++++++++++++++++++")


s=set(map(int,input().split()))
l=list(s)
l.sort()
print(l)





s={}
for i in range(0,3,1):
    key=(input("enter key"))
    value=int(input("marks="))
    s[key]=value
print(s)
sum=0
for value in s.values():
    sum=sum+value
    avg=sum/3
print(sum)
print(avg)


s="thosif "
for i in range(0,len(s),1):
    print(s[i],end="")



s="ccdhchc hccbb"
for i in range(0,len(s),1):
    for i in s:
        if(i=='A' or i=='E'
        


t=input("enter string")
print("the given staring",t)
print(t.upper())
print(t.lower())


def hi():
    for i in range(1,5,1):
         print("hi bro")

hi()         

def uskababkabeta():
    for i in range(3,12,1):
         print("thosif hi")

uskababkabeta()          

def nam(name,age):
    print("my name is",name)
    print("my age is",age)
nam("rohit",23)#positional arguments
nam(age=67,name="thosif lgtv")#keyword arguments
nam("kaif",20)#default arguments
nam("suhail",22)


def sum (a,b):
    return a+b,a-b
a,b=sum(4,5)
print("sum of two nuymbers",a)
print("difference of two numambers",b)


def sum (g,h):
    return g*h,g/h
g,h=sum(8,5)
print("sum of two variables",g)
print("difference of two variables",h)


c=lambda a:a**2
i=c(8)
print(i)

n=int(input("enter number"))
if(n==0):
    print("fcatorial of 0 is 1")
else:
    p=1
    for i in range(1,n+1,1):
        p=p*i
        print(p)    

def fact(n):
    if(n==1 or n==o):
        return 1
    else:
      n*fact(n-1) 


def ser(a,b):
    for i in range(0,10,1):
        c=a+b
        a=b
        b=c
        print(c)
ser(0,1)



def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-1)

class car:
    brand= "supra"
    colour="blue"
    def speed(self):
        print("car speed is upto350kmph")
    def miles(self):
        print("the miles of car is 20km/1")
c1=car()
print(c1.brand)
print(c1.colour)
c1.speed()
c1.miles()
c1.colour="blue"
print(c1.colour)
        


class animal:
    def drink(self):
        print("animal drinks milk")
class cat(animal):
    def meawoo(self):
        print("cat meawoo")
a=animal()
c=cat()
a.drink()
c.meawoo()
c.drink()




class animal:
    def drink(self):
        print("thosif is ghop ghop")
class cat(animal):
    def meawoo(self):
        print("lg tv boy")
class dog(cat):
    def run (self):
        print("mittha boy")
class thosif(dog):
    def fall(self):
        print("thosif ghop ghop")   
    
a=animal()
c=cat()
a.drink()
c.meawoo()
c.drink()
d=dog()
d.drink()
d.meawoo()
t=thosif()
t.drink()
t.meawoo()
t.run()
t.fall()


class animal:
    def drink(self):
        print("ddddd")
class cat(animal):
    def meawoo(self):
        print("ccccc")
class dog(animal):
    def run (self):
        print("bbbbb")
class kaif(dog,cat):
    def fall(self):
        print("aaaaa")
s=kaif()
s.fall()
s.run()
s.meawoo()
s.drink()

'''





















'''
from abc import ABC,abstractmethod

class ATMBase(ABC):

   @abstractmethod
   def check_balance(self):
      pass

   @abstractmethod
   def deposit(self):
      pass

   @abstractmethod
   def withdraw(self):
      pass

#ATM class
class ATM(ATMBase):

   def __init__(self):
      self.__balance = 1000
      self.transaction = []


   def check_balance(self):
         print("your balance", self.__balance)

   def deposit(self):
         amount = int(input("enter amount to deposit: "))
         self.__balance = self.__balance + amount
         self.transaction.append("deposited"+ str(amount))

         print("deposit successful")
   def withdraw(self):
         amount = int(input("enter amount to withdraw: ")) 
         if amount <=self.__balance:
            self.__balance = self.__balance - amount
            self.transaction.append("withdraw" + str(amount))
            print("please collect your money")
         else:
            print("insufficient balance")
   def showtransaction(self):
         print("transaction history")
         for t in self.transaction:
            print(t)

atm = ATM()

while True:
   print("\n===== ATM MENU =====")
   print("1. check balance")
   print("2.deposit")
   print("3.withdraw")
   print("4.transaction")
   print("5.exit")


   choice = int(input("enter your choice:"))
   if choice == 1:
      atm.check_balance()
   elif choice == 2:
      atm.deposit()
   elif choice == 3:
      atm.withdraw()
   elif choice == 4:
      atm.showtransaction()
   elif choice == 5:
      print("thank you for using ATM")
      break

   else:
      print("invalid option")
   
         

         


   
















from abc import ABC, abstractmethod

class CalculatorBase(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass

class Calculator(CalculatorBase):
    def __init__(self):
        self.history = []

    def get_inputs(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2

    def add(self):
        n1, n2 = self.get_inputs()
        result = n1 + n2
        self.history.append(f"{n1} + {n2} = {result}")
        print(f"Result: {result}")

    def subtract(self):
        n1, n2 = self.get_inputs()
        result = n1 - n2
        self.history.append(f"{n1} - {n2} = {result}")
        print(f"Result: {result}")

    def multiply(self):
        n1, n2 = self.get_inputs()
        result = n1 * n2
        self.history.append(f"{n1} * {n2} = {result}")
        print(f"Result: {result}")

    def divide(self):
        n1, n2 = self.get_inputs()
        if n2 != 0:
            result = n1 / n2
            self.history.append(f"{n1} / {n2} = {result}")
            print(f"Result: {result}")
        else:
            print("Error: Cannot divide by zero!")

    def show_history(self):
        print("\nCalculation History:")
        if not self.history:
            print("No calculations yet.")
        for entry in self.history:
            print(entry)

calc = Calculator()

while True:
    print("\n===== CALCULATOR MENU =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. History")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            calc.add()
        elif choice == 2:
            calc.subtract()
        elif choice == 3:
            calc.multiply()
        elif choice == 4:
            calc.divide()
        elif choice == 5:
            calc.show_history()
        elif choice == 6:
            print("haat boos d ke!")
            break
        else:
            print("Invalid option. Try again.")
    except ValueError:
        print("Please enter a valid number.")





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node inserted at beginning")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("Node inserted as first node")
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print("Node inserted at end")

    def delete(self, key):
        temp = self.head
        prev = None

        
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            print("Node deleted")
            return

        
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None
        print("Node deleted")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("Element found")
                return
            temp = temp.next
        print("Element not found")

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()

while True:
    print("\n-----LINKED LIST MENU-----")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete Node")
    print("4. Search Element")
    print("5. Display list")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        ll.insert_begin(val)
    elif choice == 2:
        val = int(input("Enter value: "))
        ll.insert_end(val)
    elif choice == 3:
        val = int(input("Enter value to delete: "))
        ll.delete(val)
    elif choice == 4:
        val = int(input("Enter value to search: "))
        ll.search(val)
    elif choice == 5:
        ll.display()
    elif choice == 6:
        print("program ended...")
        break
    else:1 
        print("Invalid choice!")

'''
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doubleLinkedList:
    def __init__(self):
        serlf.head =None


    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head



        self.head = new_node
        print("inserted at beginning")

     def insert_end(self, data):
         new_node =Node(data)
         
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        print("inserted at end")



     def delete_end(self):

         if self.head is None:
             print("List is empty")
             return

         temp = self.head

         if temp.next is None:
             self.head = None
             print("deleted Last node")
             return

         while temp.next is not None:
             temp = temp.next

         temp.prev.next = None
         print("Deleted from end")


     def display_forward(self):

         if self.head is None:
             print("List is empty")
             return

            temp = self.head

            print("Forward Traversal:")

            while temp is not None:
                print (temp.data, end="<->")
                temp = temp.next

            print("None")


     def display_backward(self):

         if self.head is None:
             print("List is empty")


        
         temp = self.head

         while temp.next is not None:
             temp = temp.next

         print("Backward traversal:")

         while temp is not None:
             print(temp.data, end=" <-> ")
             temp = temp.prev
             print("None")

ll = doublyLinkedList()
while True:

    print("\n--- doubly Linked List Menu ---")
    print("1.insert at Beginning")
    print("2.insert at End")
    print("3.Delete from Beginning")
    print("4.Delete from End")
    print("5.Display Forward")
    print("6.display Backward")
    print("7.Exit")


    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Enter value: ")
        ll.insert_begin(val)
    elif choice == '2':
        val = input("Enter value: ")
        ll.insert_end(val)
    elif choice == '3':
        ll.delete_begin()
    elif choice == '4':
        ll.delete_end()
    elif choice == '5':
        ll.display_forward()
    elif choice == '6':
        ll.display_backward()
    elif choice == '7':
        print("program ended...")
        break
    else:
        print("Invalid choice, try again.")

            

             
    '''


''' 

          
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print(f"Inserted {data} at beginning")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the first node")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp
        print(f"Inserted {data} at end")

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        
        print(f"Deleted {self.head.data} from beginning")
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        if temp.next is None:
            print(f"Deleted {temp.data}, list is now empty")
            self.head = None
            return

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None
        print(f"Deleted {temp.data} from end")

    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        print("Forward Traversal: ", end="")
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print("Backward Traversal: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


ll = DoublyLinkedList()
while True:
    print("\n--- Doubly Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display Forward")
    print("6. Display Backward")
    print("7. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Enter value: ")
        ll.insert_begin(val)
    elif choice == '2':
        val = input("Enter value: ")
        ll.insert_end(val)
    elif choice == '3':
        ll.delete_begin()
    elif choice == '4':
        ll.delete_end()
    elif choice == '5':
        ll.display_forward()
    elif choice == '6':
        ll.display_backward()
    elif choice == '7':
        print("program ended...")
        break
    else:
        print("Invalid choice, try again.")

            
'''
'''

stack = []
def push():
    x = int(input("Enter element to push:"))
    stack.append(x)
    print(x, "pushed into stack")
def pop():
    if len (stack) == 0:
        print("stack is Empty")
    else:
        re_ele = stack.pop()
        print(re_ele,"popped from stack")

def peak():
    if len (stack) == 0:
        print("stack is empty ")
    else:
        print("top element is:", stack[-1])

def display():
    if len(stack) == 0:
        print("stack is Empty")
    else:
        print("stack elements(top to bottom):")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])
def lenght():
    print("number of elements in stack:", len(stack))
while True:
    print("\n--- stack  operations ---")
    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. display")
    print("5. lenght")
    print("6. exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        lenght()

    elif choice == 6:
        print("program ended")
        break
    else:
        print("invalid choice")
    
'''
'''

def enqueue():
    x = int(input("enter element to enqueue: "))
    queue.append(x)
    print(x, "inserted into queue")

def dequeue():
    if len(queue) == 0:
        print("queue is empty")
    else:
        removed _element = queue.pop(0)
        print(removed _element, "removed from queue")
def front():
    if len(queue) == 0:
        print ("queue is empty")
    else:
        print("front element is:", queue[0])
def display():
    if len(queue) == 0:
        print ("queue is empty")
    else:
        print("queue elements(front to reae):")
        for i in queue:
            print(i)
def lenght():
    print("number of element in queue:", len(queue))
while True:
    print("\n--- queue menu ---")
    print("1. enqueue")
    print("2. dequeue")
    print("3. front")
    print("4. display")
    print("5. lenght")
    print("6. exit")

    choice = int(input("Enter your choice: "))

'''
'''
queue = []

def enqueue():
    try:
        x = int(input("Enter element to enqueue: "))
        queue.append(x)
        print(x, "inserted into queue")
    except ValueError:
        print("Invalid input! Please enter an integer.")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        
        removed_element = queue.pop(0)
        print(removed_element, "removed from queue")

def front():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element is:", queue[0])

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements (front to rear):")
        for i in queue:
            print(i)


def length():
    print("Number of elements in queue:", len(queue))


while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Length")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            front()
        elif choice == 4:
            display()
        elif choice == 5:
            length()
        elif choice == 6:
            print("ended program.")
            break
        else:
            print("Invalid choice! Please select 1-6.")
    except ValueError:
zswqd        print("Please enter a valid number.")

'''
'''        
def selection_sort(arr):
    print("\n selection sort working steps:")
    n = len (arr)
    for i in range(n):
        min_indox = 1
        for j in range(i + 1, n):
            if arr[j]<arr[min_index]:
                min_index = j
            print(f"round {i + 1}: samallest element is {arr[min_index]},swapping with {arr[i]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print("current list:" , arr)
        return arr

num = list (map(int,input("enter element").split()))
print("\nselection sort result:" ,selection_sort(num[:]))
'''
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in  arr if x < pivot]
    middle  = [x for x in  arr if x == pivot]
    right = [x for x in  arr if x > pivot]
    print(f"pivot: {pivot}, left: {left}, middle: {middle}, right: {right}")
    return quick_sort(left) + middle + quick_sort(right)
nums = list(map(int,input("enter elements").split()))
print("\quick sort result:", quick_sort(nums[:]))

'''

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
nums = list(map(int,input("enter elements").split()))
print(f"\nmerge sort result:", merge_sort(nums[:])) 




























