    
class Snode:
    def __init__(self, item):
        self.item = None
        self.next = None
        self.set_item(item)
        
    def get_item(self):
        return self.item
    
    def set_item(self, item):
        self.item = item
        
    def __str__(self):
        return str(self.item)
    