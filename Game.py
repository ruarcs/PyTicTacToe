class Game:
    'This class encapsulates one particular game.'  
    
    # These are the 'vectors' across which we can get three in a row.
    vectors = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    # This is the maximum depth we'll go to before taking the heuristic score.
    MAX_DEPTH = 3   
    # Some results
    VICTORY = 1000
    DRAW = 0
    DEFEAT = -1000



    def __init__(self, starting_player, board, limit_depth, from_file):
        self.starting_player = starting_player
        self.board = board
        self.winner = ''
        self.limit_depth = limit_depth
        self.from_file = from_file 



    def get_free_spaces(self, board):
        """ Get a list of the free spaces available on the board. """
        free_spaces = []
        count = 0
        
        for entry in board:
            if entry == '_':
                free_spaces.append(count)
            count = count + 1
        return free_spaces



    def copy_board(self, board):
        new_board = ['_','_','_','_','_','_','_','_','_']    #dummy entries
        count = 0
        for entry in board:
            new_board[count] = entry
            count = count + 1
        return new_board



    def all_possible_child_boards(self, board, player):
        """ Generate a list of all of the possible child boards given the current board state. """
        free_spaces = self.get_free_spaces(board)
        all_boards = []
        
        for space in free_spaces:
            board[space] = player
            new_board = self.copy_board(board)
            all_boards.append(new_board)
            board[space] = '_'
        return all_boards

    
        
    def other_player(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'
      
      
            
    # Check to see if there is a winner and if so set the state
    # of the member variable.    
    def check_for_win(self, board, current_player):
        test_count = 1
        for player in ['X','O']:
            for vector in Game.vectors:
                winning_line = True
                for entry in vector:
                    if board[entry] != player:
                        winning_line = False
                if winning_line == True:
                    if current_player == player:
                        return Game.VICTORY
                    else:
                        return Game.DEFEAT
                test_count = test_count + 1
        return Game.DRAW
            
        
     
        
    def run_game(self):
        
        if self.from_file == False:
            print 'Starting board state is:'
            self.print_board_state()
            print 'First player to go is: {}'.format(self.starting_player)
            print 'Predicting the output now...'
        
        # Call the minimax algorithm with the starting board we're given.
        # We'll get returned to us the best possible score we can manage,
        # assuming our opponent tries to minimize our gain.
        result = self.minimax_recursive(0, self.starting_player, self.board)

        if result  == Game.VICTORY:
            output = '{} wins'.format(self.starting_player)
        elif result == Game.DEFEAT:
            output = '{} wins'.format(self.other_player(self.starting_player))
        else:
            output = 'Draw'
            
        if self.from_file == False:
            print output
        else:
            return output

    def count_entries_in_vector(self, board, vector, player):
        count = 0
        for index in vector:
            if board[index] == player:
                count = count + 1
        return count    



    def analyse_vector(self, board, vector, player):
        """Analyse a single vector"""
        entries = self.count_entries_in_vector(board, vector, player)
        entries_opponent = self.count_entries_in_vector(board, vector, self.other_player(player))
 
        if entries == 1 and entries_opponent == 0:
            return 10
        elif entries == 2 and entries_opponent == 0:
            return 100
        elif entries == 0 and entries_opponent == 1:
            return -10
        elif entries == 0 and entries_opponent == 2:
            return -100
        else:
            return 0    # we have one of one player and one of the other, or an empty row,
                        # or two of one and one of the other (a drawn row), so it's a neutral result
      
    def heuristic_score(self, board, player):
        """ Return a score between -1000 and 1000"""
        score = 0
        modifier = 1 if (player == self.starting_player) else -1
        for vector in Game.vectors:  #check each vector
            score += modifier*(self.analyse_vector(board, vector, player))
        return score


    def minimax_recursive(self, depth, player, board):
        if self.limit_depth and depth > Game.MAX_DEPTH:
            return self.heuristic_score(board, player)
        else:           
            lowest_score = 0;
            highest_score = 0;

            # Get all possible moves that could occur at this board state.
            boards = self.all_possible_child_boards(board, player)
            
            if not boards:  #if no boards remaining then return 0
                return Game.DRAW
          
            # For all possible boards get the optimum score we can:  
            for current_board in boards:
                
                # Winner will be 'X' or 'O' or ''
                result = self.check_for_win(current_board, player)
                if result != Game.DRAW:
                    # If we have a winner then return the result
                    return result
                
                #Switch perspective and look at all possible moves from the other players point of view.
                temp = self.minimax_recursive(depth+1, self.other_player(player), current_board) 
                
                if player == self.starting_player:
                    temp = (-1)*temp    #high score BAD for starting player.
                    if temp < lowest_score:
                        lowest_score = temp
                else:
                    if temp > highest_score:
                        highest_score = temp
                        
        # They will try to MAXIMIZE our disadvantage,
        # i.e. try to maximize their score          
        if player == self.starting_player:                
            return min(lowest_score,highest_score)
        else:
        # We will try to maximize our score.
            return max(lowest_score, highest_score)
     
     
     
            
    ################################################
    ############### Utility Methods ################
    ################################################
        
    # print the board state each time a move is made
    def print_board_state(self):
        print(self.board[0]),
        print('|'),
        print(self.board[1]),
        print('|'),
        print(self.board[2])
        print(self.board[3]),
        print('|'),
        print(self.board[4]),
        print('|'),
        print(self.board[5])
        print(self.board[6]),
        print('|'),
        print(self.board[7]),
        print('|'),
        print(self.board[8])
                    
     
     
     
     
     
     
     

