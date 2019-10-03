# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'Room name: {self.name}. description: {self.description}'

    def check_directions(self):
        exits = []
        if self.n_to:
            exits.append('n')
        if self.s_to:
            exits.append('s')
        if self.e_to:
            exits.append('e')
        if self.w_to:
            exits.append('w')
        return exits
