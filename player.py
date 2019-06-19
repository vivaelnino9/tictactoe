class Player:
    def __init__(self, table, side):
        self.side = side
        self.table = table

    def __str__(self):
        return f'Player {self.side}'

    def make_move(self):
        while True:
            try:
                row = int(input(f'{self}: Please enter a row number 0-2: '))
                col = int(input(f'{self}: Please enter a column number 0-2: '))
                if row not in range(3) or col not in range(3):
                    print('Number must be between 0 and 2!')
                    continue
            except ValueError:
                print('Input must be a number!')
                continue

            if self.table.rows[row][col]:
                print(f'{row}, {col} is already taken!')
            else:
                return {'row': row, 'col': col, 'side': self.side}
