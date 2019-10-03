from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('joel', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def player_action(instructions):
    action = instructions.split()
    if (len(action) == 1):
        if hasattr(player.current_room, f"{instructions}_to"):
            player.move(instructions)
        else:
            print('There is no room that direction, please try again')
    elif (len(action) == 2):
        if (action[0] == 'get' or action[0] == 'take'):
            items = player.current_room.items
            for item in items:


def adventure_game():
    direction = ''
    while(direction != 'q'):
        print(player.current_room.name)
        print(player.current_room.description)
        for index, int in enumerate(player.current_room.items):
            print(f'item #: {index} item: {int}', end=' ')
        # print(f'Items in the current room: {for item in player.current_room.items}')
        direction = input(
            'What direction would you like to walk? [w]est [e]ast [s]outh [n]orth:   ')
        player_action(direction)
        # if hasattr(player.current_room, f"{direction}_to"):
        #     player.move(direction)
        # else:
        #     print('There is no room that direction, please try again')


adventure_game()
