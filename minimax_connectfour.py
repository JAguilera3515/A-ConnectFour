import copy
import time
import abc
import random
"""
Jose Aguilera
"""
class Game(object):
    """A connect four game."""

    def __init__(self, grid):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()
    def possible_moves(self):
        """Return a list of possible moves given the current board."""
        # YOU FILL THIS IN
        moves = []
        for r in range(8):
            flag = True
            if self.grid[0][r] == "R" or self.grid[0][r] == "B":
                    flag = False

            if flag:
                moves.append(r)

        return moves

    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        # YOU FILL THIS IN
        tmpG = self
        for r in range(len(tmpG.grid)-1, -1, -1):
            if r < 8 and col < 8 and tmpG.grid[r][col] == "-":
                tmpG.grid[r][col] = color
                break
        return tmpG
    def utility(self):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN
        numR = 0
        numB = 0
        state = self.winning_state()

        #Number of rows, cols, and diagonals
        if state == float("inf"):
            return 100
        if state == float("-inf"):
            return -100
        if state == []:
            return 0
        for row in range(len(self.grid)-1, -1, -1):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "B":
                    if col < 7 and self.grid[row][col+1] == "-":
                        #right
                        if row < 7:
                            if self.grid[row + 1][col + 1] != "-":
                                numB += 1
                        else:
                            numB += 1
                    if row > 0 and self.grid[row-1][col] == "-":
                        #up
                        numB += 1
                    if col > 0 and self.grid[row][col-1] == "-":
                        #left
                        if row < 7:
                            if self.grid[row + 1][col - 1] != "-":
                                numB += 1
                        else:
                            numB += 1
                    #handle diagnole cases
                    if col < 7 and self.grid[row][col+1] != "-":
                        if col < 8 and row > 0 and self.grid[row-1][col+1] == "-":
                            numB += 1
                    if col > 0 and self.grid[row][col - 1] != "-":
                        if row > 0 and col > 0 and self.grid[row-1][col-1] == "-":
                            numB += 1
                if self.grid[row][col] == "R":
                    if col < 7 and self.grid[row][col+1] == "-":
                        #right
                        #numR += 1
                        if row < 7:
                            if self.grid[row + 1][col + 1] != "-":
                                numR += 1
                        else:
                            numR += 1
                    if row > 0 and self.grid[row-1][col] == "-":
                        #up
                        numR += 1
                    if col > 0 and self.grid[row][col-1] == "-":
                        #left
                        #numR += 1
                        if row < 7:
                            if self.grid[row + 1][col - 1] != "-":
                                numR += 1
                        else:
                            numR += 1
                    # handle diagnole cases
                    if col < 7 and self.grid[row][col + 1] != "-":
                        if col < 7 and row > 0 and self.grid[row - 1][col + 1] == "-":
                            numR += 1
                    if col > 0 and self.grid[row][col - 1] != "-":
                        if row > 0 and col > 0 and self.grid[row-1][col-1] == "-":
                            numR += 1

        return numR - numB
    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        # YOU FILL THIS IN
        #horizental
        for row in range(len(self.grid)-1, -1, -1):
            for col in range(len(self.grid[row])):
                if col <= 4 and self.grid[row][col] == "B" and self.grid[row][col+1] == "B" and self.grid[row][col+2] == "B" and self.grid[row][col+3] == "B":
                    #print("-")
                    return float("-inf")
                if col <= 4 and self.grid[row][col] == "R" and self.grid[row][col+1] == "R" and self.grid[row][col+2] == "R" and self.grid[row][col+3] == "R":
                    #print("-")
                    return float("inf")
        #vertical
        for col in range(len(self.grid)):#0-7
            for row in range(len(self.grid)-1, -1, -1):#7-0
                if row <= 4 and self.grid[row][col] == "B" and self.grid[row+1][col] == "B" and self.grid[row+2][col] == "B" and self.grid[row+3][col] == "B":
                    #print("|")
                    return float("-inf")
                if row <= 4 and self.grid[row][col] == "R" and self.grid[row+1][col] == "R" and self.grid[row+2][col] == "R" and self.grid[row+3][col] == "R":
                    #print("|")
                    return float("inf")

        for row in range(len(self.grid) - 1, -1, -1):
            for col in range(len(self.grid[row])):
                if col <= 4 and self.grid[row][col] == "B" and self.grid[row-1][col+1] == "B" and self.grid[row-2][col+2] == "B" and self.grid[row-3][col+3] == "B":
                    #print("/")
                    return float("-inf")
                if col <= 4 and self.grid[row][col] == "R" and self.grid[row - 1][col+1] == "R" and self.grid[row - 2][col+2] == "R" and self.grid[row - 3][col+3] == "R":
                    #print("/")
                    return float("inf")
        # \
        for row in range(len(self.grid) - 1, -1, -1):
            for col in range(len(self.grid) - 1, -1, -1):
                if col >= 4 and self.grid[row][col] == "B" and self.grid[row - 1][col - 1] == "B" and self.grid[row - 2][col - 2] == "B" and self.grid[row - 3][col - 3] == "B":
                    #print("\\")
                    return float("-inf")
                if col >= 4 and self.grid[row][col] == "R" and self.grid[row - 1][col - 1] == "R" and self.grid[row - 2][col - 2] == "R" and self.grid[row - 3][col - 3] == "R":
                    #print("\\")
                    return float("inf")

        if self.possible_moves() == []:
            return 0
        return None
class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass


class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        # YOU FILL THIS IN
        mov = game.possible_moves()
        return random.choice(mov)
class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""
    #Min in MiniMac
    def move(self, game, depth):
        """Returns the first possible move"""
        # YOU FILL THIS IN
        games = copy.deepcopy(game)
        if games.winning_state() is not None:
            return games.utility()
        if depth == 5:
            return games.utility()
        v = float("inf")
        for s in games.possible_moves():
            l = games.neighbor(s, 'B')
            ya = MinimaxAgent('R').max(l, depth+1)
            if ya < v:
                v = ya
            games = copy.deepcopy(game)
        return v

class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""
    def max(self, game, depth):
        games = copy.deepcopy(game)
        if games.winning_state() is not None:
            return games.utility()
        if depth == 5:
            return games.utility()
        v = float("-inf")
        for s in games.possible_moves():
            l = games.neighbor(s, self.color)
            ya = FirstMoveAgent('B').move(l, depth + 1)
            if ya > v:
                v = ya
            games = copy.deepcopy(game)

        return v
    def move(self, game):
        """Returns the best move using minimax"""
        # YOU FILL THIS IN
        choice = 0
        games = copy.deepcopy(game)
        v = float("-inf")
        for s in games.possible_moves():
            l = games.neighbor(s, self.color)
            ya = FirstMoveAgent('B').move(l, 1 + 1)
            if ya > v:
                choice = s
                v = ya
            games = copy.deepcopy(game)
        #print(choice)
        return choice

        #return self.max(game, 7)

def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0, 0, 0
    for i in range(simulations):
        game = single_game(io=False)

        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1
    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" %
          (redwin, redwin / simulations * 100, blackwin, blackwin / simulations * 100, tie))
    return redwin / simulations


def single_game(io=True):
    """Create a game and have two agents play it."""
    game = Game([['-' for i in range(8)] for j in range(8)])  # 8x8 empty board

    if io:
        game.display()
    maxplayer = MinimaxAgent('R')
    minplayer = RandomAgent('B')
    #minplayer = MinimaxAgent('B')
    while True:
        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game


if __name__ == '__main__':
    single_game(io=True)
    #tournament(simulations=50)


