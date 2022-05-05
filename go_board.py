#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class GoBoard:
    def __init__(self, board_size=19):
        self.BSize = board_size      # default: 19x19
        self.TopEdgeIdx = 0
        self.LeftEdgeIdx = 0
        self.BottomEdgeIdx = self.BSize - 1
        self.RightEdgeIdx = self.BSize - 1
        
        self.Board = []
        for tmp in range(self.BSize):
            self.Board.append([x for x in range(self.BSize)])
        self._draw_board()
            
    def _draw_board(self):
        for x in range(self.BSize):
            for y in range(self.BSize):
                if x == self.TopEdgeIdx:
                    if y == self.LeftEdgeIdx:
                        self.Board[x][y] = u'\u2554' + u'\u2550'
                    elif  y == self.RightEdgeIdx:
                        self.Board[x][y] = u'\u2557'
                    else:
                        self.Board[x][y] = u'\u2564' + u'\u2550'
                elif x == self.BottomEdgeIdx:
                    if y == self.LeftEdgeIdx:
                        self.Board[x][y] = u'\u255A' + u'\u2550'
                    elif  y == self.RightEdgeIdx:
                        self.Board[x][y] = u'\u255D'
                    else:
                        self.Board[x][y] = u'\u2567' + u'\u2550'
                else:
                    if y == self.LeftEdgeIdx:
                        self.Board[x][y] = u'\u255F' + u'\u254C'
                    elif  y == self.RightEdgeIdx:
                        self.Board[x][y] = u'\u2562'
                    else:
                        # kratka
                        #self.Board[x][y] = u'\u253C' + u'\u254C'
                        # wypełnienie testowe
                        if (y+x)%2:
                            self.Board[x][y] = u'\u26AA'# + u'\u254C'
                        else:
                            self.Board[x][y] = u'\u26AB'# + u'\u254C'


    def show_board(self):
        for x in range(self.BSize):
            for y in range(self.BSize):
                if y == self.RightEdgeIdx:
                    print(self.Board[x][y])
                else:
                    print(self.Board[x][y], end='')

if __name__ == '__main__':
    GB = GoBoard(19)
    GB.show_board()
