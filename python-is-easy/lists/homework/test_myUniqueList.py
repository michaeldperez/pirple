from myUniqueList import *

def test_addsAnItem():
    clearMyUniqueList()
    assert addToMyUniqueList(1) == True

def test_addsUniqueItems():
    clearMyUniqueList()
    assert addToMyUniqueList(2) == True
    assert addToMyUniqueList(3) == True

def test_rejectsNonUniqueItem():
    clearMyUniqueList()
    addToMyUniqueList(1)
    addToMyUniqueList(2)
    assert addToMyUniqueList(2) == False