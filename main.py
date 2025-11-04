import time
from lists import linkedlist


def buildlist(lst, data):
    for item in data:
        lst.append(item)
        

def main():
    
    start_Time = time.time()
    
    petslist = linkedlist()
    petslist.printInOrder()
    buildlist(petslist,['🐶','🐱','🐭'])
    
    petslist.printInOrder()
    petslist.prepend('🐼')
    petslist.append('🐯')
    petslist.printInOrder()
    petslist.printReverse()
    petslist.removeItem('🐱')
    petslist.printInOrder()
    
    for i in range(1000000000000000):
        _ = i * 2 
    End_time = time.time()
    Total_time = start_Time - End_time
    print(f"Code execution time:{Total_time:4f} seconds")
main()
