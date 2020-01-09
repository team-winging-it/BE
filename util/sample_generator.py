import json
import random


class CreateDungeon():
    def __init__(self, GRID_WIDTH=40, GRID_HEIGHT=40, MAX_ROOMS=10, ROOM_SIZE_RANGE=[3, 5], grid=[], room={}):
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
        print("Grid Y" , len(grid))
        if room['y'] < 1 or room['y'] + room['height'] > len(grid) - 1:
            print("isValid False Y ")
            return False
        if room['x'] < 1 or room['x'] + room['width'] > len(grid[0]) - 1:
            print("isValid False X ")
            return False
        yy = room['y']
        xx = room['x']
        for i in range(yy - 1, room['y'] + room['height'] + 1):
            z = range(yy - 1, room['y'] + room['height'] + 1)
            print("Is this Y increaseing", i, z)
            yy += 1
            for j in range(xx - 1 , room['x'] + room['width'] + 1):
                u = range(xx - 1 , room['x'] + room['width'] + 1)
                print("Is this X increaseing", j , u)
                xx += 1

                if grid[i][j]['type'] == 'floor':
                    print("Room is invalid", room, grid[i][j]['type'])
                    return False
            xx = room['x']
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
        for i in range(zz, room['y'] + room['height']):
            u = range(zz, room['y'] + room['height'])
            print("Loop I | y", i,  u)
            zz += 1

            for j in range(xx, room['x'] + room['width']):
                z = range(xx, room['x'] + room['width'])
                print("loop J | x", j, z)
                # print("type", type)
                xx += 1
                if type == 'floor':
                    # breakpoint()
                    # breakpoint()
                    grid[i][j]['type'] = type
                    # print("we got a floor", grid[i][j]['type']
                elif type == 'door':
                    grid[i][j]['type'] = type


            print("next row")
            xx = room['x']

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


    def createRoomsFromSeed(self, grid, room):

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

    def growMap(self, grid, seedRooms, counter=1, maxRooms= 120):
        if counter + len(seedRooms) > maxRooms or len(seedRooms) == 0:
            return grid
        print("Grid in growMap", len(grid))
        if len(seedRooms) > 0:
            print("GROW MAP! does it get here")
            grid = self.createRoomsFromSeed(
                grid, seedRooms.pop(),)
        # seedRooms.append(*grid['placedRooms'])
        items = grid['placedRooms']
        for item in items:
            seedRooms.append(item)

        counter += len(grid['placedRooms'])
        return self.growMap(grid['grid'], grid['placedRooms'], counter)


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
    'x': 10,
    'y': 9,
    'height': 4,
    'width': 4,
    # 'x': random.randrange(1, 40 - maxi - 15),
    # 'y': random.randrange(1, 40 - maxi - 15),
    # 'height': random.randrange(mini, maxi),
    # 'width': random.randrange(mini, maxi)
}
# breakpoint()
dungeon = CreateDungeon()

dungeon.placeCells(grid, firstRoom)



the_grid = dungeon.growMap(grid, [firstRoom])
cell_list = []
tx = 0
ty = 0
for row in grid:
    row_string = ''

    for tile in row:
        if tile['type'] == 'floor':
            row_string += 'f'
        if tile['type'] == 'door':
            row_string += 'D'
        if tile['type'] == 0:
            row_string += '-'
        tile['x'] = tx
        tile['y'] = ty
        cell_list.append(tile)
        tx += 1
    tx = 0
    ty += 1
    print(row_string)

with open('data.json', 'w') as outfile:
    json.dump(cell_list, outfile)



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
