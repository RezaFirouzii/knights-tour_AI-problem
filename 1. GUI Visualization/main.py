
# The GUI is made using "Warndorff's rule"
# check "https://github.com/RezaFirouzii/knights-tour_AI-problem/blob/main/3.%20Warnsdorff's%20rule%20solution/warnsdorffs_rule.py"
# for this algorithm implementation

from pygame_utils import *
import os

# Constants
TITLE = "Knight's Tour (Warnsdorff's rule)"
WINDOWS_LOCATION = '350,70'
SIZE = 8
WIDTH = 750
HEIGHT = 750
FPS = 20

CELL_SIZE = 100

#############   Warnsdorff's rule   #############
def isvalid(table, pos):
    size = len(table)
    i, j = pos
    return 0 <= i < size and 0 <= j < size and not table[i][j]


def getmoves(pos):
    x, y = pos
    return [(x + 1, y + 2), (x + 1, y - 2), (x + 2, y + 1), (x + 2, y - 1),
            (x - 1, y + 2), (x - 1, y - 2), (x - 2, y + 1), (x - 2, y - 1)]


def getaccessiblities(table, pos):
    moves = getmoves(pos)
    count = 0
    for move in moves:
        if isvalid(table, move):
            count += 1

    return count


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

#################################################

# driver code
if __name__ == '__main__':
    # setting Pygame window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = WINDOWS_LOCATION

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True
    axisLabels = True

    input_box1 = InputBox(100, 100, 250, 50, ' Table Size (default=8): ')
    input_box2 = InputBox(100, 300, 250, 50, ' Row (optional) ')
    input_box3 = InputBox(100, 400, 250, 50, ' Col (optional): ')
    input_boxes = [input_box1, input_box2, input_box3]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    break
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    # validating inputs
    try:
        SIZE = int(input_box1.text.split(' ')[-1])
        if not 5 <= SIZE <= 20:
            raise ValueError
    except ValueError:
        SIZE = 8

    CELL_SIZE = HEIGHT // SIZE
    grid = Grid(surface=screen, cellSize=CELL_SIZE, labels=axisLabels)
    hover = False
    running = True

    pos = [random.randrange(SIZE), random.randrange(SIZE)]
    x, y = input_box2.text.split(' ')[-1], input_box3.text.split(' ')[-1]
    if x.isalnum() and 0 < int(x) <= SIZE:
        pos[0] = int(x) - 1
    if y.isalnum() and 0 < int(y) <= SIZE:
        pos[1] = int(y) - 1

    table = [[0] * SIZE for _ in range(SIZE)]
    pos = tuple(pos)
    last_pos = pos
    value = 1
    visited = {pos: value}
    flag = True

    # choosing random colors
    pointer_color = (Color.colors[random.randrange(3, 10)], Color.colors[random.randrange(1, 10)])
    cell_color = (Color.colors[random.randrange(3, 10)], Color.colors[random.randrange(1, 10)])

    # main loop
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        if flag:
            x, y = pos
            last_pos = pos
            table[x][y] = value
            visited.update({pos: value})
            value += 1
            pos = getminimumaccessible(table, pos)
            flag = False

            if value > SIZE ** 2:
                screen.fill(Color.WHITE)
                grid.drawUseRect(last_pos, visited, pointer_color, cell_color)
                pygame.display.flip()

        if pos and not flag:

            screen.fill(Color.WHITE)
            grid.drawUseRect(last_pos, visited, pointer_color, cell_color)
            pygame.display.flip()

            last_x, last_y = last_pos
            x, y = pos

            if last_x < x:
                last_x += 1
            elif last_x > x:
                last_x -= 1
            else:
                if last_y < y:
                    last_y += 1
                elif last_y > y:
                    last_y -= 1
                else:
                    flag = True

            last_pos = (last_x, last_y)

    print(value)
    pygame.quit()
