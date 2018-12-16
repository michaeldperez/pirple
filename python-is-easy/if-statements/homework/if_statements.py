def atLeastTwoEqual(x, y, z):
    if (x == y) or (x == z) or (y == z):
        return True
    else:
        return False


''' More concise
def atLeastTwoEqual(x, y, z):
    return (x == y) or (x == z) or (y == z)
'''