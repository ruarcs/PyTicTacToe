class Game:
    'This class encapsulates one particular game.'  
    
    # These are the 'vectors' across which we can get three in a row.
    vectors = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    # This is the maximum depth we'll go to before taking the heuristic score.
    MAX_DEPTH = 5     
    # Some results
    VICTORY = 1
    DRAW = 0
    DEFEAT = -1



    def __init__(self, starting_player, board):
        self.starting_player = starting_player
        self.board = board
        self.winner = ''



    def get_free_spaces(self, board):
        """ Get a list of the free spaces available on the board. """
        free_spaces = []
        count = 0
        
        for entry in board:
            if entry == ' ':
                free_spaces.append(count)
            count = count + 1
        return free_spaces



    def copy_board(self, board):
        new_board = ['','','','','','','','','']    #dummy entries
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
            board[space] = ' '
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
        
        print 'Starting board state is:'
        self.print_board_state()
        print 'First player to go is: {}'.format(self.starting_player)
        print 'Predicting the output now...'
        
        # Call the minimax algorithm with the starting board we're given.
        # We'll get returned to us the best possible score we can manage,
        # assuming our opponent tries to minimize our gain.
        result = self.minimax_recursive(0, self.starting_player, self.board)

        if result  == 1:
            print '{} WINS!'.format(self.starting_player)
        elif result == -1:
            print '{} WINS!'.format(self.other_player(self.starting_player))
        else:
            print('DRAW!')
      



    def minimax_recursive(self, depth, player, board):
        if depth > Game.MAX_DEPTH:
            #return self.heuristic_score(board) # "-1" indicates no valid move
            return 0 #for the moment return 0 to indicate draw if we get too far down the tree.
        else:           
            lowest_score = 0;
            highest_score = 0;

            # Get all possible moves that could occur at this board state.
            boards = self.all_possible_child_boards(board, player)
            
            if not boards:  #if no boards remaining then return 0
                return 0
          
            # For all possible boards get the optimum score we can:  
            for current_board in boards:
                
                # Winner will be 'X' or 'O' or ''
                result = self.check_for_win(current_board, player)
                if result != 0:
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
                        
        return max(lowest_score,highest_score)
     
     
     
            
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
                    
     
     
     
     
     
     
     
     
     
     
#################### UNUSED CODE ######################################     
        
    '''
    def count_entries_in_vector(self, board, vector, player):
        count = 0
        for index in vector:
            if board[index] == player:
                count = count + 1
        return count    



    def analyse_vector(self, board, vector, player):
        entries = self.count_entries_in_vector(board, vector, player)
        if entries == 3:
            return VICTORY
        elif entries == 2:
            return 100
        elif entries == 1:
            return 10
 
 
 
    def heuristic_score(self, board, player):
        alpha = 0
        beta = 0
        for vector in Game.vectors:  #check each vector
            alpha += self.analyse_vector(board, vector, player)
            beta -= self.analyse_vector(board, vector, self.other_player(player))
        return alpha + beta
    '''
