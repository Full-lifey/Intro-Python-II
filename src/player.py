# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room='outside', items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'Player {self.name} is in room {self.current_room}'

    def move(self, direction):
        if direction in self.current_room.check_directions():
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('There is no room that direction, please try again')

    def change_room(self, new_room):
        self.current_room = new_room
