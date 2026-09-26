# Code — Day 244: Game-Playing AI Foundations

class TicTacToeAI:
    def __init__(self):
        self.board = [' '] * 9

    def is_moves_left(self):
        return ' ' in self.board

    def evaluate(self):
        # Winning combinations
        lines = [
            (0,1,2), (3,4,5), (6,7,8), # Rows
            (0,3,6), (1,4,7), (2,5,8), # Cols
            (0,4,8), (2,4,6)           # Diagonals
        ]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                if self.board[a] == 'X':
                    return +10
                elif self.board[a] == 'O':
                    return -10
        return 0

    def alphabeta(self, depth, alpha, beta, is_max):
        score = self.evaluate()
        if score == 10 or score == -10:
            return score
        if not self.is_moves_left():
            return 0

        if is_max:
            best = -1000
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    val = self.alphabeta(depth + 1, alpha, beta, False)
                    self.board[i] = ' '
                    best = max(best, val)
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        break
            return best
        else:
            best = 1000
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    val = self.alphabeta(depth + 1, alpha, beta, True)
                    self.board[i] = ' '
                    best = min(best, val)
                    beta = min(beta, best)
                    if alpha >= beta:
                        break
            return best

    def find_best_move(self):
        best_val = -1000
        best_move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                move_val = self.alphabeta(0, -1000, 1000, False)
                self.board[i] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        return best_move

if __name__ == "__main__":
    game = TicTacToeAI()
    # Sample board state: X is about to win
    # X | O | X
    # O | X |  
    #   |   | O
    game.board = ['X', 'O', 'X', 'O', 'X', ' ', ' ', ' ', 'O']
    print("Current Board State:")
    for row in range(3):
        print(game.board[row*3:(row+1)*3])
        
    best = game.find_best_move()
    print(f"\nAI (X) Optimal Next Move Index: {best}")
