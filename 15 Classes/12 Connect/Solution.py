class ConnectGame:
    def __init__(self, board):
        # Generate 2D array:
        self.board = [[stone for stone in row] for row in board.replace(' ', '').splitlines()]  
        # Hex neighbours relative pos in array:
        self.neighbours = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]  
        
    def get_winner(self):
        # check player 0, then X, if neither win output ' ':
        for player in ['O', 'X']:
            result = self.checker(player)
            if result is True:
                return player
                
        return ''
        
    def checker(self, player):
        # Set parameters for player O:
        if player == 'O':  
            array = self.board
        # Set parameters for player X:
        if player == 'X':  
            array = list(zip(*self.board))
            
        # Get player first and last row stones:
        stones = [(index, 0) for index, stone in enumerate(array[0]) if stone == player]
        ends = [(index, len(array) - 1) for index, stone in enumerate(array[-1]) if stone == player]

        # Search for stones connected to first row stones, loop till exhaustion:
        for stone in stones:  
            for neighbour in self.neighbours:
                row = stone[1] + neighbour[1]
                col = stone[0] + neighbour[0]
                if row >= 0 and col >= 0:
                    try:
                        if array[row][col] == player and (col, row) not in stones:
                            stones.append((col, row))
                    except IndexError:
                        continue

        # Return true if one of the end stones is connected to first row stones:
        for end in ends:  
            if end in stones:
                return True
