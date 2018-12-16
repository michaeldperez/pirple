from if_statements import atLeastTwoEqual

def test_xAndYEqual():
    assert atLeastTwoEqual(1,1,2) == True

def test_xAndZEqual():
    assert atLeastTwoEqual(1,2,1) == True

def test_yAndZEqual(): 
    assert atLeastTwoEqual(2,1,1) == True

def test_AllEqual():
    assert atLeastTwoEqual(1,1,1) == True

def test_noneEqual():
    assert atLeastTwoEqual(1,2,3) == False

def test_stringTest():
    assert atLeastTwoEqual("hello", "world", "world") == True

def test_stringTestTwo():
    assert atLeastTwoEqual("foo", "bar", "baz") == False