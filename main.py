# 1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None    #pointer to the next node


# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1    # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
        self.size = 0
        return

#display the content of the list
    # def printList(self):
    #     temp = self.head
    #     if temp != None:
    #         print("The list contains:", end=" ")
    #         while temp != None:
    #             print(temp.data, end=" ")
    #             temp = temp.next
    #         print()
    #     else:
    #         print("The list is empty.")


List = SinglyLinkedList()

node1 = Node(1)
node2 = Node(2)

List.append(node1)
List.append(node2)

#print(List.size)
#List.printList()
List.clear()
#List.printList()
#print(List.size)



# 2

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None    # pointer to the next node


# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1    # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        print('this is current:')
        while current:
            val = current.data
            current = current.next
            print('this is current:', val, 'this is next', current.next)

            yield val

    def get_size(self):
        print("The size of the list is: ", self.size)
        return self.size

    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
        return

    def get_data(self, data):
        current = self.head  # start from head
        while current:
            val = current.data.data  # 1.node=head node1=1
            current = current.next  # 2. node node2=2, 3. node node3=3 etc.
            #print('this is current:', val)
            #print("This is the given data to compare to:", data.data)
            if val == data.data:
                #print("True return:", val)
                return val

        return False



#  display the content of the list
    def printList(self):
        temp = self.head
        if temp != None:
            print("The list contains:", end=" ")
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


List = SinglyLinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node('er')
nodeTest = Node(42)
#print(node1.data)

List.append(node1)
List.append(node2)
List.append(node3)

#print('the list size is: ', List.size)
#List.get_size()
#List.printList()
#List.clear()
print(List.get_data(node3))



# 3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None    #pointer to the next node


# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1    # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        print('this is current:')
        while current:
            val = current.data
            current = current.next
            print('this is current:', val, 'this is next', current.next)

            yield val

    def get_size(self):
        print("The size of the list is: ", self.size)
        return self.size

    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
        return

    def get_data(self, data):
        current = self.head  # start from head
        while current:
            val = current.data.data  # 1.node=head node1=1
            current = current.next  # 2. node node2=2, 3. node node3=3 etc.
            #print('this is current:', val)
            #print("This is the given data to compare to:", data.data)
            if val == data.data:
                #print("True retrun:", val)
                return val

        return False

    def delete(self, data):
        #if 1st element da eliminare:
        if self.head.data.data == data.data:
            self.head = self.head.next  # pointer! va da head a nodo dopo
            self.size -= 1
            return
        #if element middle da eliminare
        else:
            current = self.head  # si parte dalla testa
            currentNext = self.head.next    # pointer zeigt su nodo dopo testa

            while currentNext != None:  # fino a che pointer non zeigt auf void

                prev = current                  #prev=current(node) - Erster Schleifendurchlauf: node1, Zweiter node2, ...
                current = current.next          #current=current(pointer) - Erster Schleifendurchlauf: 1 zeigt auf node2, Zweiter node3, ...
                currentNext = currentNext.next  #Erster Schleifendurchlauf: 2 zeigt auf node3, , Zweiter node4, ...
                #print('prev = ', prev.data.data)
                #print('current = ', current.data.data)
                #print('currentNext = ', currentNext.data.data)

                if current.data.data == data.data:
                    #if last element da eliminare
                    if currentNext == None:     # if next pointer zeigt auf void, then pointer of previous node deve zeigen auf void x delete last node
                        prev.next = None
                        List.size -= 1
                        return
                    #"Normaler" Fall, Element mitten aus der Liste loeschen
                    else:
                        prev.next = prev.next.next  # pointers!
                        #print('Current node = ', current.data.data)
                        #print('currentNext node = ', currentNext.data.data)
                        List.size -= 1
                        return

            return

#  display the content of the list
    def printList(self):
        temp = self.head
        if temp != None:
            print("The list contains:", end=" ")
            while temp != None:
                print(temp.data.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


List = SinglyLinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
#print(node1.data)

List.append(node1)
List.append(node2)
List.append(node3)
List.append(node4)
List.append(node5)
List.append(node6)
List.append(node7)

#print('the list size is: ', List.size)
#List.get_size()
#List.printList()
#List.clear()
#List.get_data(node2)
List.delete(node2)
#List.printList()
#List.get_size()



# 4

class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None    #pointer to the next node
        self.prev = None    #pointer to the previous node

# Class for managing the list and nodes
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = NodeDLL(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
            self.tail = node
            #print("The new node is: ", node.data.data, "The prev Node is", node.prev,"The tail Node is: ", node.data.data)
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            current.prev = current
            self.tail = node
            self.tail.prev = current
            #print("The new node is: ", current.next.data.data, "The prev Node is", current.prev.data.data, "The tail Node is: ", node.data.data)
        self.size += 1    # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        print('this is current:')
        while current:
            val = current.data
            current = current.next
            print('this is current:', val, 'this is next', current.next)

            yield val

    def get_size(self):
        print("The size of the list is: ", self.size)
        return self.size

    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
        return

    def get_data(self, data):
        current = self.head  # start from head
        while current:
            val = current.data.data  # 1.node=head node1=1
            current = current.next  # 2. node node2=2, 3. node node3=3 etc.
            #print('this is current:', val)
            #print("This is the given data to compare to:", data.data)
            if val == data.data:
                #print("True retrun:", val)
                return val

        return False

    def delete(self, data):
        #if 1st element da eliminare:
        if self.head.data.data == data.data:
            self.head = self.head.next  # pointer! va da head a nodo dopo
            self.size -= 1
            return
        #if element middle da eliminare
        else:
            current = self.head  # si parte dalla testa
            currentNext = self.head.next    # pointer zeigt su nodo dopo testa

            while currentNext != None:  # fino a che pointer non zeigt auf void

                prev = current                  #prev=current(node) - Erster Schleifendurchlauf: node1, Zweiter node2, ...
                current = current.next          #current=current(pointer) - Erster Schleifendurchlauf: 1 zeigt auf node2, Zweiter node3, ...
                currentNext = currentNext.next  #Erster Schleifendurchlauf: 2 zeigt auf node3, , Zweiter node4, ...

                if current.data.data == data.data:
                    #if last element da eliminare
                    if currentNext == None:     # if next pointer zeigt auf void, then pointer of previous node deve zeigen auf void x delete last node
                        prev.next = None
                        List.size -= 1
                        return
                    #"Normaler" Fall, Element mitten aus der Liste loeschen
                    else:
                        prev.next = prev.next.next  # pointers!
                        #print('Current node = ', current.data.data)
                        #print('currentNext node = ', currentNext.data.data)
                        List.size -= 1
                        return

            return

    def delete_new(self, data):
        node = NodeDLL(data)

        if self.head.data.data == data.data:
            self.head = self.head.next  # pointer! va da head a nodo dopo
            self.size -= 1
            print("First")
            return
        elif self.tail.data.data == data.data:
            current = self.tail.prev
            current.next = None
            self.tail = current
            print("Last")
            #print(self.tail.data.data)
            #print("The new node is: ", current.data.data, "The prev Node is", currentPrev, "The tail Node is: ", node.data.data)
            #self.tail.next = None
            self.size -= 1
            return
        else:
            print("hhghgk")
            current = self.head
            while current.next:
                current = current.next
                if current.data.data == data.data:
                    temp = current.prev
                    current.next = temp.next.next
                    current.prev = temp
                    #current.next = temp.next
                    #print("The prev node is: ", current.prev.data.data, "The next Node is", current.data.data)
                    List.size -= 1
                    return
            #current.next = node
            #current.prev = current


#  display the content of the list
    def printList(self):
        temp = self.head
        if temp != None:
            print("The list contains:", end=" ")
            while temp != None:
                print(temp.data.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


List = DoublyLinkedList()

node1 = NodeDLL(1)
node2 = NodeDLL(2)
node67 = NodeDLL("gasda")
node3 = NodeDLL(3)
node4 = NodeDLL(4)
node5 = NodeDLL(5)
#print(node1.data)

List.append(node1)
List.append(node2)
List.append(node67)
List.append(node3)
List.append(node4)
List.append(node5)

#print('the list size is: ', List.size)
List.get_size()
List.printList()
#List.clear()
#List.get_data(node2)
#List.delete(node2)
List.delete_new(node4)
List.printList()
List.get_size()


# 5

class MyStack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
        #print(element)
        return element

    def pop(self):
        try:                            # 'try' prova a vedere se funziona e ti da' alternativa se no
            return self.items.pop()
        except:
            print("Stack is empty")
        return

    def top(self):
        try:
            #print(self.items[-1])
            return self.items[-1]
        except:
            print('wrong')
            return

    def size(self):
        #print(len(self.items))
        return len(self.items)


stack = MyStack()

stack.push('smelly')
stack.push('cat')
stack.push('aiaiai')
stack.push(34)

# stack.top()
print(stack.pop())
# stack.top()

stack.size()


# 6

class MyQueue:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
        # print('items in queue: ', element)
        return element

    def show_left(self):
        try:
            # print('last element added: ', self.items[-1])
            return self.items[-1]
        except:
            print('wrooong')
            return

    def show_right(self):
        try:
            # print('first element added: ', self.items[0])
            return self.items[0]
        except:
            print('do it again')
            return

    def pop(self):
        try:
            # print(self.items.pop(0))
            return self.items.pop(0)
        except:
            print("Queue is empty")
        return


queue = MyQueue()

queue.push('smelly')
queue.push('cat')
queue.push('aiaiai')
queue.push(34)

queue.show_left()
queue.show_right()

print(queue.pop())
