from player import Player


class Computer(Player):
    # TODO: implement AI to make moves    
    def __init__(self, table, side):
        super().__init__(table, side)

    def __str__(self):
        return f'Computer {self.side}'
