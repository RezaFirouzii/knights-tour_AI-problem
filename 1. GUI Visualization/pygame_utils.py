import pygame
import random

# creates input boxes for getting input
class InputBox:

    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(300, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+15))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


# creates the grid and handles the drawings on it
class Grid:

    def __init__(self, surface, cellSize, labels):
        self.surface = surface
        self.cols = surface.get_width() // cellSize
        self.rows = surface.get_height() // cellSize
        self.cellSize = cellSize
        self.labels = labels
        self.grid = [[() for _ in range(self.cols)] for _ in range(self.rows)]
        self.font = pygame.font.SysFont('arial', 12, False)

    def drawRect(self, pos, value, color):
        x, y = pos
        x *= self.cellSize
        y *= self.cellSize

        fill, border = color

        rect = pygame.Rect(x, y, self.cellSize, self.cellSize)
        self.surface.fill(fill, rect)
        pygame.draw.rect(self.surface, border, rect, 1)

        if value:
            font = pygame.font.SysFont('arial', 60 - 2 * self.rows - len(str(self.rows)) * 5, True)
            text = font.render(str(value), True, Color.WHITE)
            coord = (3 * self.cellSize) // 10
            self.surface.blit(text, (x + coord + 5, y + coord))

        label = str((y + x * self.rows) // self.cellSize + 1)
        text = pygame.font.SysFont('Arial', 12, True).render(label, True, Color.WHITE)
        self.surface.blit(text, (x + 5, y + 5))

    def drawUseRect(self, pos, visited, pointer_color, cell_color):
        for row in range(self.rows):
            x_axis = row * self.cellSize
            for col in range(self.cols):
                y_axis = col * self.cellSize
                key = (row, col)
                if key in visited:
                    self.drawRect(key, visited[key], cell_color)
                else:
                    if self.labels:
                        indent = ' '
                        if col < 10:
                            indent += ' '
                        text = self.font.render(indent + str(col + row * self.rows + 1), True, Color.BLACK)
                        self.surface.blit(text, (x_axis, y_axis + 5))
                    rect = pygame.Rect(x_axis, y_axis, self.cellSize, self.cellSize)
                    pygame.draw.rect(self.surface, Color.BLACK, rect, 1)

        self.drawRect(pos, 0 if pos not in visited else visited[pos], pointer_color)


# usefull class
class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 128, 255)
    GREEN = (0, 153, 0)
    YELLOW = (255, 255, 0)
    BROWN = (204, 102, 0)
    PINK = (255, 102, 178)
    PURPLE = (153, 51, 255)

    colors = {
        1: WHITE,
        2: YELLOW,
        3: RED,
        4: BLUE,
        5: GREEN,
        6: BLACK,
        7: BROWN,
        8: PINK,
        9: PURPLE,
    }
