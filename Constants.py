WHITE_COLOR_RGB = (255, 255, 255)
BLACK_COLOR_RGB = (0, 0, 0)
RED_COLOR_RGB = (255, 0, 0)
GREEN_COLOR_RGB = (0, 255, 0)
BLUE_COLOR_RGB = (0, 0, 255)
WIDTH = 500
NUM_ROWS = 5
NUM_EPISODES = 1000
EPSILON = 3  # Integer 1-10. 2 = 20% random, 3 = 30% random ...
CELL_SIZE = WIDTH / NUM_ROWS
ACTIONS = ['left', 'right', 'up', 'down']
TERMINAL_CELLS = [(4, 4), (2, 2)]
CELL_VALUES = [((1, 0), -10),
               ((1, 1), -10),
               ((1, 2), -10),
               ((1, 3), -10),
               ((4, 4), 30),
               ((2, 2), 50)]
