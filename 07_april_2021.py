# A core structure of an adventure game created in May 2021
# to practice OOP :)

class Room:
    '''
    Define initial values of atributes.
    Assign text representation of class.
    '''
    def __init__(self, name, coordinates, north=None, south=None, east=None, west=None):
        '''
        Required input:
            name = name of room, string
            coordinates = location of Room, tuple of two numbers (x, y)
            north / south / east / west = intial values are None, supposed to store reference to adjacent Room
        '''
        self.name = name
        self.coordinates = coordinates
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __str__(self):
        return f'{self.name}'


class World:
    '''
    Atributes: "rooms", "current_room"
        - "rooms"
            - used for storing references to all Room objects
            - in format: key = tuple of coordinates (x, y), value = reference to Room object
        - "current_room"
            - used for storing reference to current Room object
    Methods used in initialization of object: "add_room", "connect_rooms", "set_initial_room"
    Methods used for gameplay: "describe_surroundings", "move"
    '''
    rooms = {}   # key = coordinates (x, y), value = reference to Room object
    current_room = ''

    def add_room(self, new_room):
        '''
        Add room into dictionary "rooms",
        in format: key = tuple of coordinates (x, y), value = reference to Room object
        '''
        self.rooms[new_room.coordinates] = new_room


    def connect_rooms(self):
        '''
        Add reference to adjacent objects into each object (variables north, south, east, west).
        '''
        for coordinates, room in self.rooms.items():
            x, y = coordinates
            if (x, y+1) in self.rooms:
                room.east = self.rooms[(x, y+1)]
            if (x, y-1) in self.rooms:
                room.west = self.rooms[(x, y-1)]
            if (x-1, y) in self.rooms:
                room.north = self.rooms[(x-1, y)]
            if (x+1, y) in self.rooms:
                room.south = self.rooms[(x+1, y)]


    def set_initial_room(self, coordinates):
        '''
        Set initial position of player.
        '''
        self.current_room = self.rooms[coordinates]


    def describe_surroundings(self):
        '''
        Describe adjacent rooms to player.
        '''
        if self.current_room.north:
            print(f'In the north there is a {self.current_room.north}.')
        if self.current_room.south:
            print(f'In the south there is a {self.current_room.south}.')
        if self.current_room.east:
            print(f'In the east there is a {self.current_room.east}.')
        if self.current_room.west:
            print(f'In the west there is a {self.current_room.west}.')


    def move(self, direction):
        '''
        Change "current_room" according to given direction.
        In case of invalid input raise ValueError.
        '''
        x, y = self.current_room.coordinates
        if direction == 'north':
            x -= 1
        elif direction == 'south':
            x += 1
        elif direction == 'west':
            y -= 1
        elif direction == 'east':
            y += 1
        else:
            raise ValueError('Invalid direction')
        self.current_room = self.rooms[(x, y)]



def initialize(rooms):
    '''
    Create object "world" using class "World".
    Add objects "room" into "world", object "room" has its unique name and location (x, y).
    Add reference to adjacent objects into each object (variables north, south, east, west).
    Set initial position of player to (0, 0).
    '''
    world = World()
    for room in rooms:
        world.add_room(room)

    world.connect_rooms()
    world.set_initial_room((0,0))

    return world


def game():
    '''Initialize object "world"
    While input from player != "end" or final room is reached, ask for direction.
    Move accordingly (with invalid input ask again). Describe adjacent rooms.
    '''
    world = initialize([
        Room('forest', (0, 0)), Room('deep forest', (0, 1)), Room('even deeper forest', (0, 2)),
        Room('quiet meadow', (0, 3)), Room('shiny lake', (0, 4)), Room('dangerous swamp', (1, 2)),
        Room('castle with princess', (1, 3))
        ])
    print()
    direction = None
    while direction != 'end':
        world.describe_surroundings()
        direction = input(f'{". "* 15}\nWhere do you want to go? ')
        if direction in ['north', 'south', 'east', 'west']:
            try:
                print('- - - - - - - - - - - - - - -')
                world.move(direction)
                if world.current_room.coordinates == (1, 3):
                    print("You won! You've found a lost princess!")
                    exit()
            except ValueError:
                print("You can't go there")
        else:
            if direction != 'end':
                print('Allowed inputs: "north", "south", "east" and "west". Type "end" to end the game.')
            else:
                print('Thanks for game! :)')

game()