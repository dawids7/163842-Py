import random
import os

class Game2048:
    def __init__(self):
        self.board = [[0]*4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = random.choice([2, 4])

    def can_move(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return True
                if i < 3 and self.board[i][j] == self.board[i+1][j]:
                    return True
                if j < 3 and self.board[i][j] == self.board[i][j+1]:
                    return True
        return False

    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (4 - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(3):
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2
                row[i+1] = 0
                self.score += row[i]
        return row

    def move_left(self):
        new_board = []
        for row in self.board:
            compressed_row = self.compress(row)
            merged_row = self.merge(compressed_row)
            new_row = self.compress(merged_row)
            new_board.append(new_row)
        self.board = new_board

    def move_right(self):
        new_board = []
        for row in self.board:
            row.reverse()
            compressed_row = self.compress(row)
            merged_row = self.merge(compressed_row)
            new_row = self.compress(merged_row)
            new_row.reverse()
            new_board.append(new_row)
        self.board = new_board

    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print('+----'*4 + '+')
            print(''.join(f'|{num:^4}' if num != 0 else '|    ' for num in row) + '|')
        print('+----'*4 + '+')
        print(f'Score: {self.score}')

    def play(self):
        while self.can_move():
            self.draw_board()
            move = input("Enter move (W/A/S/D): ").upper()
            if move == 'W':
                self.move_up()
            elif move == 'A':
                self.move_left()
            elif move == 'S':
                self.move_down()
            elif move == 'D':
                self.move_right()
            else:
                print("Invalid move! Use W/A/S/D keys.")
                continue
            self.add_new_tile()
        self.draw_board()
        print("Game over! Your final score is:", self.score)
        input("Press Enter to exit...")

if __name__ == "__main__":
    game = Game2048()
    game.play()
