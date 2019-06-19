class Table:
    def __init__(self):
        self.rows = [['', '', ''], ['', '', ''], ['', '', '']]

    def __str__(self):
        table = '\n'
        for row in self.rows:
            r = ' '.join(f'| {c if c else "_"} |' for c in row)
            table += f'{r}\n\n'
        return table

    def make_move(self, move):
        # Place player's side in row/column entered. Either 'X' or 'O'.
        self.rows[move['row']][move['col']] = move['side']

    def check_full(self):
        # Checks to see if Table is all spaces have been used
        for row in self.rows:
            if not all(row):
                return False
        return True

    def check_win(self, side):
        # Check to see if there is a winner. If there is return that side.

        table = self.rows
        # Check for a vertical win
        for val in [[row[col] for row in table] for col in range(3)]:
            if val.count(side) == 3:
                return True
        # Check for a horizontal win
        for row in table:
            if row.count(side) == 3:
                return True

        # Check for diagonal win
        diags = [
            [table[0][0], table[1][1], table[2][2]],
            [table[2][0], table[1][1], table[0][2]]
        ]

        for diag in diags:
            if diag.count(side) == 3:
                return True

        return False

