'''
Simple Tic Tac Toe game as a reference for the Rust version
'''


class Pieces:
    X = 'X'
    O = 'O'
    SPC = ' '

class Game:
    SIZE = 3

    def __init__(self):
        self.board = [
            [ Pieces.SPC for _ in range(Game.SIZE) ]
            for _ in range(Game.SIZE)
        ]

        self.player = Pieces.X
        self.isDone = False
        self.winner = None

    def getOpenSpots(self):
        result = []
        for i in range(Game.SIZE):
            for j in range(Game.SIZE):
                if self.board[i][j] == Pieces.SPC:
                    result.append( str(i * Game.SIZE + j) )

        return result

    def getMove(self):
        validSpots = self.getOpenSpots()
        if not validSpots:
            self.finishGame()
            return None

        validSpotsStr = ", ".join(validSpots)
        while True:
            opt = input(
                f"Player {self.player} please select a move\n"
                f"({validSpotsStr}): "
            ).strip()

            if opt in validSpots:
                return opt

    def makeMove(self, move):
        if self.isDone:
            return

        spot = int(move)

        i, j = spot // Game.SIZE, spot % Game.SIZE
        self.board[i][j] = self.player

        self.player = Pieces.X if self.player == Pieces.O else Pieces.O


    def finishGame(self, winner = None):
        self.isDone = True
        self.winner = winner

    def updateGame(self):
        if self.isDone:
            return

        # rows
        for row in self.board:
            s = set(row)
            if (len(s) == 1) and (Pieces.SPC not in s):
                self.finishGame(row[0])
                return
        
        # cols
        for col in range(Game.SIZE):
            s = { self.board[row][col] for row in range(Game.SIZE) }
            if (len(s) == 1) and (Pieces.SPC not in s):
                self.finishGame( self.board[0][col] )
                return

        # diagonals
        diagL = set()
        diagR = set()
        for row in range(Game.SIZE):
            diagL.add( self.board[row][row] )
            diagR.add( self.board[row][Game.SIZE - row - 1] )

        diagL = list(diagL)
        diagR = list(diagR)

        if len(diagL) == 1 and diagL[0] != Pieces.SPC:
            self.finishGame(diagL[0])
            return
        
        if len(diagR) == 1 and diagR[0] != Pieces.SPC:
            self.finishGame(diagR[0])
            return

    def displayBoard(self):
        print( '+-' * Game.SIZE + '+' )
        for row in self.board:
            print( '|' + '|'.join(row) + '|' )
            print( '+-' * Game.SIZE + '+' )


def main():
    ttt = Game()

    print("Welcome to Tic Tac Toe!\n")    

    while not ttt.isDone:
        ttt.displayBoard()
        move = ttt.getMove()
        ttt.makeMove(move)
        ttt.updateGame()
    
    print(f"""\nGame Over! {
        "Nobody" if ttt.winner == None
        else f"Player {ttt.winner}"
    } wins!""")
    ttt.displayBoard()

if __name__ == "__main__":
    main()
