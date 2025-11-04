import sys
import os
import importlib.util

# Add parent directory
parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, parent)

# Direct file import
node_file = os.path.join(parent, 'node', 'linked_list_node.py')
spec = importlib.util.spec_from_file_location("linked_list_node", node_file)
linked_list_node_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(linked_list_node_module)
Node = linked_list_node_module.Snode

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, item):
        New_node = Node(item)
        if self.head == None:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next = New_node
            self.tail = New_node
        self.size += 1
        
    def prepend(self,item):
        New_node = Node(item)
        if self.head == None:
            self.head = New_node
            self.tail = New_node
        else:
            New_node.next = self.head 
            self.head = New_node
        self.size += 1
    
    def printInOrder(self):
        
        curNode = self.head
        print("[",end="")
        while curNode != None:
            print(curNode.item, end="")
            curNode = curNode.next
        print("]")

    def printReverse(self):
        
        def recurse(node):
            if node == None: return
            recurse(node.next)
            print(node.item, end="")
            
        print("[",end="")
        recurse(self.head)
        print("}")
        
    def removeItem(self,key):
        if self.head == None: return

        curNode =  self.head
        prevNode = None
        while curNode!= None:
            
            if curNode.item == key:
                if curNode == self.head:
                    self.size -= 1
                    print("")
                elif curNode == self.tail:
                    self.size -= 1 
                    print("")
                else:
                    prevNode = curNode.next
                self.size -= 1
            prevNode = curNode
            curNode = curNode.next