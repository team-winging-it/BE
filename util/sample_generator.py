import json
import random


class CreateDungeon():
    def __init__(self, GRID_WIDTH=40, GRID_HEIGHT=40, MAX_ROOMS=10, ROOM_SIZE_RANGE=[5, 5], grid=[], room={}):
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.MAX_ROOMS = MAX_ROOMS
        self.ROOM_SIZE_RANGE = ROOM_SIZE_RANGE
        self.grid = grid
        self.room = room

    def isValidRoomPlacement(self, grid, room):


        # room['width'] = 1
        # room['height'] = 1
        print("isValid", room)

        if room['y'] < 1 or room['y'] + room['height'] > len(grid) - 1:
            return False
        if room['x'] < 1 or room['x'] + room['width'] > len(grid[0]) - 1:
            return False

        for i in range(room['y']-1, room['y'] + room['height'] + 1):
            for j in range(room['x']-1, room['x'] + room['width'] + 1):
                if grid[i][j]['type'] == 'floor':

                    return False
        return True

    def placeCells(self, grid, room, type='floor'):
        # print('grid', grid)
        # print('room', room)
        # print('type', type)
        # room['width'] = 3
        # room['height'] = 5
        print("Our Room", room, type)
        print("--------------------------------------------------")
        zz = room['y']
        xx = room['x']
        # breakpoint()
        for i in range(room['y'], zz + room['height']):
            u = range(room['y'], zz + room['height'])
            print("Loop I | y", room['y'],  u)
            room['y'] += 1

            for j in range(room['x'], xx + room['width']):
                z = range(room['x'], xx + room['width'])
                print("loop J | x", j, z)
                # print("type", type)
                room['x'] += 1
                if type == 'floor':
                    # breakpoint()

                    grid[i][j]['type'] = type
                    # print("we got a floor", grid[i][j]['type']
                elif type == 'door':
                    grid[i][j]['type'] = type


            print("next row")
            room['x'] = xx

        print("--------------------------------------------------")
        return grid

        # i = room['y']
        # j = room['x']
        # while i < (room['y'] + room['height']):
        #     i += 1
        #     u = range(room['y'], room['y'] + room['height'])
        #     print("Loop I | y", room['y'],  u)
        #     while j < (room['x'] + room['width']):
        #         zz = range(room['x'], room['x'] + room['width'])
        #         print("loop J | x", j, zz)
        #         print("type", type)
        #         if type == 'floor':
        #             # breakpoint()
        #
        #             grid[i][j]['type'] = type
        #             print("we got a floor", grid[i][j]['type'])
        #         j += 1


    def createRoomsFromSeed(self, grid, room, range):

        range = self.ROOM_SIZE_RANGE
        [mini, maxi] = [range[0], range[1]]

        roomValues = []

        north = {'height': random.randrange(
            mini, maxi+1), 'width': random.randrange(mini, maxi+1)}

        north['x'] = random.randrange(room['x'], room['x'] + room['width'])
        north['y'] = room['y'] - north['height'] - 1
        # breakpoint()
        north['doorx'] = random.randrange(north['x'], min(
            north['x'] + north['width'], room['x'] + room['width']))
        north['doory'] = room['y']-1

        roomValues.append(north)

        east = {'height': random.randrange(
            mini, maxi+1), 'width': random.randrange(mini, maxi+1)}
        east['x'] = room['x'] + room['width'] + 1
        east['y'] = random.randrange(room['y'], room['height'] + room['y'])
        east['doorx'] = east['x'] - 1
        east['doory'] = random.randrange(east['y'], min(
            east['y'] + east['height'], room['y'] + room['height']))
        roomValues.append(east)

        south = {'height': random.randrange(
            mini, maxi+1), 'width': random.randrange(mini, maxi+1)}
        south['x'] = random.randrange(room['x'], room['width'] + room['x'])
        south['y'] = room['y'] + room['height'] + 1
        south['doorx'] = random.randrange(south['x'], min(
            south['x'] + south['width'], room['x'] + room['width']))
        south['doory'] = room['y'] + room['height']
        roomValues.append(south)

        west = {'height': random.randrange(
            mini, maxi+1), 'width': random.randrange(mini, maxi+1)}
        west['x'] = room['x'] - west['width'] - 1
        west['y'] = random.randrange(room['y'], room['height'] + room['y'])
        west['doorx'] = room['x'] - 1
        west['doory'] = random.randrange(west['y'], min(
            west['y'] + west['height'], room['y'] + room['height']))
        roomValues.append(west)
        placedRooms = []
        print('room values', roomValues)
        for room in roomValues:
            if self.isValidRoomPlacement(grid, room):
                print('it is vaild')
                grid = self.placeCells(grid, room)

                grid = self.placeCells(
                    grid, {'x': room['doorx'], 'y': room['doory'], 'height': 1, 'width': 1}, 'door')
                placedRooms.append(room)
                print(grid)

        dicti = {}
        dicti['grid'] = grid
        dicti['placedRooms'] = placedRooms

        return dicti
    # HERE ######################

    def growMap(self, grid, seedRooms, counter=1, maxRooms=5):
        if counter + len(seedRooms) > maxRooms or len(seedRooms) == 0:
            return grid

        if len(seedRooms) > 0:
            grid = self.createRoomsFromSeed(
                grid, seedRooms.pop(), range=[7, 12])
        # seedRooms.append(*grid['placedRooms'])
        items = grid['placedRooms']
        for item in items:
            seedRooms.append(item)

        counter += len(grid['placedRooms'])
        return self.growMap(grid, seedRooms, counter)


grid = []
GRID_HT = 40
GRID_WH = 40
ii = 0
jj = 0
while ii < GRID_HT:
    grid.append([])
    for jj in range(GRID_WH):

        grid[ii].append(
            {'type': 0, 'opacity': random.uniform(0.3, 0.8)}
        )

    ii += 1

[mini, maxi] = [7, 12]  # HERE ##################

firstRoom = {
    'x': random.randrange(1, 40 - maxi - 15),
    'y': random.randrange(1, 40 - maxi - 15),
    'height': random.randrange(mini, maxi),
    'width': random.randrange(mini, maxi)
}
# breakpoint()
dungeon = CreateDungeon()

# dungeon.placeCells(grid, firstRoom)



the_grid = dungeon.growMap(grid, [firstRoom])

with open('data.json', 'w') as outfile:
    json.dump(the_grid, outfile)



#     print(json.dumps(the_grid, indent=4, sort_keys=True))
# #
# z = 0
# with open('data.json', 'w') as outfile:
#     while z < GRID_HT:
#         for n in range(GRID_WH):
#             json.dump(argg[z][n]['type'], outfile)
#
#         z += 1
#
#     print(json.dumps(argg, indent=4, sort_keys=True))
