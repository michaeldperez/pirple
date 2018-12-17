myUniqueList = []

def addToMyUniqueList(item):
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else:
        return False

def clearMyUniqueList():
    """ Test helper method 
    used in test_myUniqueList.py
    """
    myUniqueList.clear()
    
addToMyUniqueList(1)
addToMyUniqueList(2)
addToMyUniqueList(3)
addToMyUniqueList(1)
addToMyUniqueList(2)
print(myUniqueList) # [1, 2, 3]
