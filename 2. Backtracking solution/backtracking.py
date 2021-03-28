
# knight's tour problem solved using backtracking
# https://en.wikipedia.org/wiki/Knight%27s_tour
# Runtime complexity: O(SIZE ^ (SIZE ^ 2))

def output(table):
    for arr in table:
        for num in arr:
            print(num, end=' ')
        print()


# recursive function
def tourExists(table, move=(0, 0), count=2):

    if count > len(table) ** 2:
        return True

    x, y = move
    moves = [(x + 2, y + 1), (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1),
             (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)]

    for move in moves:
        x, y = move
        if 0 <= x < len(table) and 0 <= y < len(table) and not table[x][y]:
            
            table[x][y] = count
            if tourExists(table, move, count + 1):
                return True

            table[x][y] = 0
        
    return False


# driver code
if __name__ == "__main__":
    size = int(input())
    table = [[0] * size for _ in range(size)]
    table[0][0] = 1
    if tourExists(table):
        output(table)
    else:
        print("No solution found!")