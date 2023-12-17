"""
Author - Kaneel Senevirathne
Date - 12/5/2023
"""

import numpy as np
import minimax

class ConnectFour:
    
    def __init__(self):
        self.rows = 5
        self.columns = 6
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'
        self.winner = None
        import pdb; pdb.set_trace()

    def print_board(self):
        for row in self.board:
            print("| " + " | ".join(row) + " |")

    def is_move_valid(self, col):
        return 0 <= col < self.columns and self.board[0][col] == ' '

    def make_move(self, col):
        if not self.is_move_valid(col):
            return False
        
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = self.current_player
                break
        return True
    
    def check_winner(self):
        for row in self.board:
            for i in range(self.columns - 3):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != ' ':
                    self.winner = row[i]
                    return True
                
        for col in range(self.columns):
            for i in range(self.rows - 3):
                if self.board[i][col] == self.board[i + 1][col] == self.board[i + 2][col] == self.board[i + 3][col] != ' ':
                    self.winner = self.board[i][col]
                    return True

        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != ' ':
                    self.winner = self.board[i][j]
                    return True
                if self.board[i][j + 3] == self.board[i + 1][j + 2] == self.board[i + 2][j + 1] == self.board[i + 3][j] != ' ':
                    self.winner = self.board[i][j + 3]
                    return True
                
        return False

    def play_game(self):
        while not self.winner:
            self.print_board()
            col = int(input(f"Player {self.current_player}, enter column (1-{self.columns}): ")) - 1
            if self.make_move(col):
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if all(cell != ' ' for row in self.board for cell in row):
                    self.print_board()
                    print("It's a tie!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_move(self, col, print = True):
        '''
        Play move manually.
        '''
        if self.make_move(col):
            if self.check_winner():
                if print:
                    self.print_board()
                return self.winner
                
            if all(cell != ' ' for row in self.board for cell in row):
                if print:    
                    self.print_board()
                return 'draw'
                
            self.current_player = 'O' if self.current_player == 'X' else 'X'

            if print:
                self.print_board()



        
        

        
        



if __name__ == "__main__":
    c4 = ConnectFour()
    c4.play_game()