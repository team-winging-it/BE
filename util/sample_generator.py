import random


class CreateDungeon():
    def __init__(self, GRID_WIDTH=160, GRID_HEIGHT=120, MAX_ROOMS=30, ROOM_SIZE_RANGE=[7, 12], grid=[], room={}):
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.MAX_ROOMS = MAX_ROOMS
        self.ROOM_SIZE_RANGE = ROOM_SIZE_RANGE
        self.grid = grid
        self.room = room

    def isValidRoomPlacement(self, grid, room):
        room['width'] = 1
        room['height'] = 1
        if room['y'] < 1 or room['y'] + room['height'] > len(grid) - 1:
            return False
        if room['x'] < 1 or room['x'] + room['width'] > len(grid[0]) - 1:
            return False

        for i in range(room['y']-1, room['y'] + room['height'] + 1):
            for j in range(room['x']-1, room['x'] + room['width'] + 1):
                if grid[i][j].type == 'floor':
                    return False
        return True

    def placeCells(self, grid, room, type='floor'):
        room['width'] = 1
        room['height'] = 1
        for i in range(room['y'], room['y'] + room['height']):
            for j in range(room['x'], room['x'] + room['width']):
                grid[i][j] = {type, room['id']}
        return grid

    def createRoomsFromSeed(self, grid, room, range):
        range = self.ROOM_SIZE_RANGE
        [min, max] = [range[0], range[1]]

        roomValues = []

        north = {'height': random.randrange(
            min, max+1), 'width': random.randrange(min, max+1)}
        north['x'] = random.randrange(room['x'], room['x'] + room['width'])
        north['y'] = room['y'] - north['height'] - 1
        north['doorx'] = random.randrange(north['x'], min(
            north['x'] + north['width'], room['x'] + room['width']))
        north['doory'] = room['y']-1
        roomValues.append(north)

        east = {'height': random.randrange(
            min, max+1), 'width': random.randrange(min, max+1)}
        east['x'] = room['x'] + room['width'] + 1
        east['y'] = random.randrange(room['y'], room['height'] + room['y'])
        east['doorx'] = east['x'] - 1
        east['doory'] = random.randrange(east['y'], min(
            east['y'] + east['height'], room['y'] + room['height']))
        roomValues.append(east)

        south = {'height': random.randrange(
            min, max+1), 'width': random.randrange(min, max+1)}
        south['x'] = random.randrange(room['x'], room['width'] + room['x'])
        south['y'] = room['y'] + room['height'] + 1
        south['doorx'] = random.randrange(south['x'], min(
            south['x'] + south['width'], room['x'] + room['width']))
        south['doory'] = room['y'] + room['height']
        roomValues.append(south)

        west = {'height': random.randrange(
            min, max+1), 'width': random.randrange(min, max+1)}
        west['x'] = room['x'] - west['width'] - 1
        west['y'] = random.randrange(room['y'], room['height'] + room['y'])
        west['doorx'] = room['x'] - 1
        west['doory'] = random.randrange(west['y'], min(
            west['y'] + west['height'], room['y'] + room['height']))
        roomValues.append(west)

        placedRooms = []
        for room in roomValues:
            if self.isValidRoomPlacement(grid, room):
                grid = self.placeCells(grid, room)

                grid = self.placeCells(
                    grid, {'x': room['doorx'], 'y': room['doory']}, 'door')

                placedRooms.append(room)
        return [{grid, placedRooms}]

    grid = []
    for i in range(0, 120):  # HERE ##################
        grid.append([])
        for j in range(0, 160):  # HERE ##################
            grid[i].append(
                {'type': 0, 'opacity': random.uniform(0.3, 0.8)})

    [min, max] = [7, 12]  # HERE ##################

    firstRoom = {
        'x': random.randrange(1, 160 - max - 15),
        'y': random.randrange(1, 120 - max - 15),
        'height': random.randrange(min, max),
        'width': random.randrange(min, max)
    }

    grid = placeCells( firstRoom)

    # HERE ######################
    def growMap(self, grid, seedRooms, counter=1, maxRooms=30, firstRoom=firstRoom):
        if counter + len(seedRooms) > maxRooms or len(seedRooms) is None:
            return grid

        grid = self.createRoomsFromSeed(grid, seedRooms.pop(), range=[7, 12])
        seedRooms.append(grid)
        return self.growMap(grid, seedRooms)
