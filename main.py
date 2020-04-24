import pygame as pg

## TODO: Add computer moves, checking to see if square is already occupied.

class Board():

    def __init__(self):
        self.state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.player_char = ''
        self.complete = False
        self.last_move = -1
        while self.player_char != 'x' and self.player_char != 'o':
            self.player_char = input("Would you like to be x or o: ").lower()
        self.computer_char = 'o' if self.player_char == 'x' else 'x'
        print("Player will be {0}'s and I will be {1}'s.\nWhat is your first move?".format(self.player_char, self.computer_char))

    def print_board(self):
        s = self.state
        template = ''' -------------
 | {0} | {1} | {2} |
 -------------
 | {3} | {4} | {5} |
 -------------
 | {6} | {7} | {8} |
 -------------'''
        print(template.format(s[0][0], s[0][1], s[0][2], s[1][0], s[1][1], s[1][2], s[2][0], s[2][1], s[2][2]))

    def make_move(self):
        while True:
            try:
                self.print_board()
                pos = int(input("Where would you like to move : "))
                row = self.position_map[pos][0]
                col = self.position_map[pos][1]
                break
            except KeyError:
                print("Bad space selection. Please try again.")
        self.state[row][col] = self.player_char
        self.last_move = pos
        return self.check_state()

    def check_state(self):
        row = self.position_map[self.last_move][0]
        col = self.position_map[self.last_move][1]
        s = self.state
        if s[row][0] == s[row][1] == s[row][2]:
            return True
        elif s[0][col] == s[1][col] == s[2][col]:
            return True
        elif s[1][1] == s[0][0] == s[2][2] or s[1][1] == s[0][2] == s[2][0]:
            return True
        return False

    def play(self):
        while self.complete == False:
            self.complete = self.make_move()
        self.print_board()

    position_map = {1: (0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

board = Board()
board.play()
