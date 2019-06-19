import random
from table import Table
from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.table = Table()
        self.player1 = None
        self.player2 = None
        self.set_up()

    def __str__(self):
        return 'Tik-Tac-Toe!'

    def set_up(self):
        while True:
            player1 = input('Player 1: Please choose a side! "X" or "O"?').upper()
            if player1.lower().strip() != 'x' and player1.lower().strip() != 'o':
                print('Invalid Input!')
                continue

            self.player1 = Player(self.table, player1)
            print(f'Player 1 is "{self.player1.side}"')

            player2_side = 'X' if player1 == 'O' else 'O'
            player2 = input(f'Player 2: Press "Y" to confirm playing as "{player2_side}". '
                            f'Or press any key to play against a computer!').upper()

            if player2.lower().strip() != 'y':
                self.player2 = Computer(self.table, player2_side)
            else:
                self.player2 = Player(self.table, player2_side)
            break

        self.play()

    def play(self):
        player_turn = random.choice([self.player1, self.player2])
        print(f'Time to play! {player_turn} first!')
        print(self.table)
        while not self.table.check_full():
            move = player_turn.make_move()
            self.table.make_move(move)

            winner = self.table.check_win(player_turn.side)
            print(self.table)

            if winner:
                print(f'{player_turn} wins!')
                return

            player_turn = self.player2 if player_turn == self.player1 else self.player1

        print('Tie!')


if __name__ == '__main__':
    Game()
