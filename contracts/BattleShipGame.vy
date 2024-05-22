# Define the board size
board_size: constant(int128) = 10

# Define ship sizes
ship_sizes: constant(int128[5]) = [5, 4, 3, 3, 2]

# Define the Battleship game contract
contract Battleship:
    # Define the boards for each player
    player1_board: public(map(int128, map(int128, int128)))

    player2_board: public(map(int128, map(int128, int128)))

    # Define the players
    player1: public(address)
    player2: public(address)

    # Define the current player
    current_player: public(address)

    # Define the game state
    game_started: public(bool)
    game_over: public(bool)

    # Event to signal a move
    MoveMade: event({_player: address, _x: int128, _y: int128, _hit: bool})

    # Event to signal the end of the game
    GameOver: event({_winner: address})

    # Initialize the game
    def __init__(player2: address):
        self.player1 = msg.sender
        self.player2 = player2
        self.current_player = msg.sender
        self.game_started = False
        self.game_over = False

    @public
    bool take_bets(player1: address, player2: address, stake: int128):
        if self.balanceOf(player1) < stake:
            return False
        if self.balanceOf(player2) < stake:
            return False
        return True


    # Function to place ships on the board
    @public
    def place_ship(x: int128, y: int128, size: int128, horizontal: bool):
        # Check if the game has already started
        assert not self.game_started, "Game has already started"
        # Check if the player placing the ship is valid
        assert msg.sender == self.player1 or msg.sender == self.player2, "Invalid player"

        # Place the ship on the board
        for i in range(size):
            if horizontal:
                assert 0 <= x + i < board_size, "Invalid ship position"
                if msg.sender == self.player1:
                    self.player1_board[x + i][y] = 1
                else:
                    self.player2_board[x + i][y] = 1
            else:
                assert 0 <= y + i < board_size, "Invalid ship position"
                if msg.sender == self.player1:
                    self.player1_board[x][y + i] = 1
                else:
                    self.player2_board[x][y + i] = 1

    # Function to start the game
    @public
    def start_game():
        assert msg.sender == self.player1 or msg.sender == self.player2, "Invalid player"
        
        #place holder val for stake
        assert take_bets(self.player1, self.player2, 100), "Balance Insufficient"
        self.game_started = True

    #Function to visualize board
    @public
    def display_board(player: int128):
        # Determine the board
        board: map(int128, map(int128, int128)) = empty(map(int128, map(int128, int128)))
        if player == 1:
            board = self.player1_board
        else:
            board = self.player2_board
        
        for j in range(10):
            for k in range(10):
                print(board [j][k] + " "),
            print("\n")

    # Function to make a move
    @public
    def make_move(x: int128, y: int128):
        # Check if the game is over
        assert not self.game_over, "Game is over"
        # Check if the game has started
        assert self.game_started, "Game has not started"
        # Check if it's the player's turn
        assert msg.sender == self.current_player, "Not your turn"
        # Check if the move is valid
        assert 0 <= x < board_size and 0 <= y < board_size, "Invalid move"

        # Determine the opponent's board
        opponent_board: map(int128, map(int128, int128)) = empty(map(int128, map(int128, int128)))
        if self.current_player == self.player1:
            opponent_board = self.player2_board
        else:
            opponent_board = self.player1_board

        # Check if the move hits a ship
        hit: bool = opponent_board[x][y] == 1

        # Update the board with the move
        opponent_board[x][y] = -1 if hit else -2

        # Emit event for the move made
        self.MoveMade(msg.sender, x, y, hit)

        # Check if the move resulted in a win
        if self.check_win(opponent_board):
            self.game_over = True
            self.GameOver(msg.sender)
        else:
            # Switch to the other player
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    # Function to check for a win
    def check_win(self, board: map(int128, map(int128, int128))) -> bool:
        for x in range(board_size):
            for y in range(board_size):
                if board[x][y] == 1:
                    return False
        return True
