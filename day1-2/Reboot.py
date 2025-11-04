class Node(object):

	def __init__ (self, d, n = None):
		self.data = d
		self.next_node = n

	def get_next (self):
		return self.next_node

	def set_next (self, n):
		self.next_node = n
		
	def get_data (self):
		return self.data

	def set_data (self, d):
		self.data = d
		
	def has_next (self):
		if self.get_next() is None:
			return False
		return True
		
	def to_string (self):
		return "Node value: " + str(self.data)

		
class LinkedList (object):

	def __init__ (self, r = None):
		self.root = r
		self.size = 0

	def get_size (self):
		return self.size

	def add (self, d):
		new_node = Node (d, self.root)
		self.root = new_node
		self.size += 1

	def add_node (self, n):
		n.set_next(self.root)
		self.root = n
		self.size += 1
		
	def remove (self, d):
		this_node = self.root
		prev_node = None

		while this_node is not None:
			if this_node.get_data() == d:
				if prev_node is not None:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node.get_next()
				self.size -= 1
				return True     # data removed
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		return False  # data not found

	def find (self, d):
		this_node = self.root
		while this_node is not None:
			if this_node.get_data() == d:
				return d
			elif this_node.get_next() == None:
				return False
			else:
				this_node = this_node.get_next()
				
def print_list (self):
	print ("Print List..........")
	if self.root is None:
		return
	this_node = self.root
	print (this_node.to_string())
	while this_node.has_next():
		this_node = this_node.get_next()
		print (this_node.to_string())

def append(self, d):
	new_node = Node(d)
	if self.root is None:
		self.root = new_node
	else:
		this_node = self.root
		while this_node.has_next():
			this_node = this_node.get_next()
		this_node.set_next(new_node)
	self.size += 1
       
def prepend(self, d):
    new_node = Node(d)
    if self.root is None:
        self.root = new_node
    else:
        new_node.set_next(self.root)
        self.root = new_node
    self.size += 1
    
def map(self, func):
    this_node = self.root
    while this_node is not None:
        this_node.set_data(func(this_node.get_data()))
        this_node = this_node.get_next()
        
def filter(self, func):
    dummy_root = Node(0)
    dummy_root.set_next(self.root)
    prev_node = dummy_root
    this_node = self.root

    while this_node is not None:
        if not func(this_node.get_data()):
            prev_node.set_next(this_node.get_next())
            self.size -= 1
        else:
            prev_node = this_node
        this_node = this_node.get_next()
    
    self.root = dummy_root.get_next()
        
def reduce(self, func, initial):
    result = initial
    this_node = self.root
    while this_node is not None:
        result = func(result, this_node.get_data())
        this_node = this_node.get_next()
    return result
			
		
def main():
	myList = LinkedList()
	myList.add(5)
	myList.add(9)
	myList.add(3)
	myList.add(8)
	myList.add(9)
	
	myList.print_list()
    myList.append(12)
    myList.prepend(1)
    myList.print_list()
    myList.map(lambda x: x * 2)
    myList.print_list()
    total = myList.reduce(lambda x, y: x + y, 0)
    print("Total after reduce:", total)
    # Note: filter method requires a condition to be defined for it to work properly.
	
main()









