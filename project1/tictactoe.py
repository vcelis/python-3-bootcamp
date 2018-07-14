MOVES_MAP = {1: (1, 1), 2: (1, 5), 3: (1, 9), 4: (5, 1), 5: (5, 5),
             6: (5, 9), 7: (9, 1), 8: (9, 5), 9: (9, 9)}
WINNING_PATERNS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8),
                   (3, 6, 9), (1, 5, 9), (3, 5, 7)]


class TicTacToe:

    def __init__(self):
        self.reset_game()

    def reset_game(self, player1=None, player2=None):
        self.board = [[' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' '],
                      [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
                      [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
                      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      [' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' '],
                      [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
                      [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
                      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                      [' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' '],
                      [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
                      [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']]
        self.moves = ['#', '', '', '', '', '', '', '', '', '']
        self.player1 = player1
        self.player2 = player2
        self.current_player = 1

    def run(self):
        print('\n'*100)
        print('Welcome to Tic Tac Toe!\n')
        self.configure_players()
        print(f'\nPlayer {self.current_player} will go first and is {self.player1}\n')
        if self.confirm_play():
            self.play()

    def play(self):
        self.draw_board()
        while self.moves_remaining() and not self.check_winner():
            print(f'Player {self.current_player}:')
            answer = input('Choose your next position: (1-9) ')
            if self.invalid_move(answer):
                self.draw_board()
                print('Invalid move! Try again.')
            else:
                self.moves[int(answer)] = self.player1 if self.current_player == 1 else self.player2
                self.current_player = 2 if self.current_player == 1 else 1
                self.draw_board()
        else:
            if self.check_winner():
                winner = 2 if self.current_player == 1 else 1
                print('We got a winner!')
                print(f'Congrats player {winner}!')
            else:
                print('No more moves available!')
            if self.play_again():
                self.reset_game(player1=self.player1, player2=self.player2)
                self.play()
            else:
                print('Thanks for playing!')

    def play_again(self):
        answer = input('Do you want to play again? Enter Yes or No. ').lower()
        while answer not in ['yes', 'no']:
            print('\n'*100)
            print('Only Yes or No is accepted! Please try again. \n')
            answer = input('Do you want to play again? Enter Yes or No. ').lower()
        else:
            return answer == 'yes'

    def check_winner(self):
        for a, b, c in WINNING_PATERNS:
            tmp = set([self.moves[a], self.moves[b], self.moves[c]])
            if tmp == {'X'} or tmp == {'O'}:
                return True
        return False

    def configure_players(self):
        answer = input('Player 1: Do you want to be X or O? ').upper()
        if answer not in ['X', 'O']:
            print('\n'*100)
            print('Only X or O is accepted! Please try again. \n')
            self.configure_players()
        else:
            self.player1 = answer
            self.player2 = 'X' if answer == 'O' else 'O'

    def confirm_play(self):
        answer = input('Are you ready to play? Enter Yes or No. ').lower()
        while answer not in ['yes', 'no']:
            print('\n'*100)
            print('Only Yes or No is accepted! Please try again. \n')
            answer = input('Are you ready to play? Enter Yes or No. ').lower()
        else:
            return answer == 'yes'

    def draw_board(self):
        # Fill in board
        for i in range(1, len(self.moves)):
            if self.moves[i] != '':
                self.board[MOVES_MAP[i][0]][MOVES_MAP[i][1]] = self.moves[i]

        # Draw board
        print('\n'*100)
        for row in self.board:
            line = ''
            for column in row:
                line += column
            print(line)
        print('\n'*5)

    def moves_remaining(self):
        remaining_moves = ((len(self.moves) - 1) -
                           (self.moves.count('X') + self.moves.count('O')))
        return remaining_moves > 0

    def invalid_move(self, num):
        try:
            return self.moves[int(num)] in ['X', 'O']
        except (IndexError, ValueError):
            return True


if __name__ == '__main__':
    game = TicTacToe()
    game.run()
