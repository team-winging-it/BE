class CreateDungeon():
    def __init__(self, GRID_WIDTH=160, GRID_HEIGHT=120, MAX_ROOMS=30, ROOM_SIZE_RANGE=[7, 12], grid=[]):
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.MAX_ROOMS = MAX_ROOMS
        self.ROOM_SIZE_RANGE = ROOM_SIZE_RANGE
        self.grid = grid
        self.room = {}

    def isValidRoomPlacement(self, grid, {x, y, width=1, height=1}):
        if y < 1 or y + height > len(grid) - 1:
            return False
        if x < 1 or x + width > len(grid[0]) - 1:
            return False

        for i in range(y-1, y + height + 1):
            for j in range(x-1, x + width + 1):
                if grid[i][j].type == 'floor':
                    return False

        return True

    def placeCells(self, grid, {x, y, width=1, height=1, id}, type='floor'):
        for i in range(y, y + height):
            for j in range(x, x + width):
                grid[i][j] = {type, id}

        return grid

    def createRoomsFromSeed(self, grid, {x, y, width, height}, range=ROOM_SIZE_RANGE):
        [min, max] = [range[0], range[1]]

        roomValues = []

        north = {height: random.randrange(min, max+1)}

    # grid = [[{type:0, opacity: _.random(0.3, 0.8)}], [{type:0, opacity: _.random(0.1, 0.9)}], [], []]
