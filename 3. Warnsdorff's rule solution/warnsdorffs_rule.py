
# knight's tour problem solved using Warnsdorffs rule
# https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorf.27s_rule

def output(table):
    for arr in table:
        for num in arr:
            print(num, end=' ')
        print()


# check if the position is valid
def isvalid(table, pos):
    size = len(table)
    i, j = pos
    return 0 <= i < size and 0 <= j < size and not table[i][j]


# returns all possible moves for a position
def getmoves(pos):
    x, y = pos
    return [(x + 1, y + 2), (x + 1, y - 2), (x + 2, y + 1), (x + 2, y - 1),
            (x - 1, y + 2), (x - 1, y - 2), (x - 2, y + 1), (x - 2, y - 1)]


# returns the number of valid and empty spots
# among all the possible moves for a position
def getaccessiblities(table, pos):
    moves = getmoves(pos)
    count = 0
    for move in moves:
        if isvalid(table, move):
            count += 1

    return count


# for every neighbor or spot in shape of "L", get the accessible spots
# choose the spot with minimum accessible neighbors and return its position
def getminimumaccessible(table, pos):
    moves = getmoves(pos)
    minVal = 8
    minPos = ()
    for move in moves:
        if isvalid(table, move):
            value = getaccessiblities(table, move)
            if value < minVal:
                minVal = value
                minPos = move
    
    return minPos

# main function for finding the right spot at each step
def tourExists(table):
    import random
    size = len(table)
    # starting the tour from a random position
    pos = (random.randrange(size), random.randrange(size))
    value = 1
    
    while pos:
        x, y = pos
        table[x][y] = value
        value += 1
        pos = getminimumaccessible(table, pos)
    
    if value > size ** 2:
        return True
    return False


# driver code
if __name__ == "__main__":    
    size = 8
    # or get input in console
    # size = int(input())
    table = [[0] * size for _ in range(size)]
    if tourExists(table):
        output(table)
    else:
        print("No solution found!")