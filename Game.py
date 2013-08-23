class Game:
    'This class encapsulates one particular game.'
    def __init__(self, game_file):
        #specify the file to read the game description from
        self.game_file = game_file
        

    #imported code
    def __init__(self):
        starting_player = 'X'
        board = ['_', 'X', '_',
                 'O', 'X', '_',
                 'O', '_', '_']
        vectors = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]



    def run(self):
        minimax_recursive(0, 0, 0, self.starting_player, self.board)
        


    def minimax_recursive(self, depth, a, b, player, board):
        if depth > MAX_DEPTH:
            return heuristic_score(board, player)
        else:           
            alpha = a;
            beta = b;
            moves = all_possible_moves(board) #generate all possible moves at this board state
            if player == starting_player:   #min layer
                for move in moves:
                    alpha = minimax_recursive(depth+1,alpha,beta,player,board)
            else:
                for move in moves:
                    beta = minimax_recursive(depth+1,alpha,beta,player,board)

    def all_possible_moves(self, board):
        possible_moves = []
        count = 0
        for position in board:
            if position == '_':
                possible_moves.append(count)
            count++
        return possible_moves    

    
    def heuristic_score(board, player):
        alpha = 0
        beta = 0
        for vector in vectors:  #check each vector
            alpha += analyse_vector(board, vector, player)
            beta -= analyse_vector(board, vector, other_player(player))
        return alpha + beta



    def analyse_vector(board, vector, player):
        entries = count_entries_in_vector(board, vector, player)
        if entries == 3:
            return 1000
        else if entries == 2:
            return 100
        else if entries == 1:
            return 10



    def count_entries_in_vector(board, vector, player):
        count = 0
        for index in vector:
            if board[index] == player:
                count++
        return count



    def other_player(player):
        if player == 'X':
            return 'O'
        else:
            return 'X'
            
    ################################################
    ############### Utility Methods ################
    ################################################
        
    # print the board state each time a move is made
    def print_board_state(self):
        print(board[0]),
        print('|'),
        print(board[1]),
        print('|'),
        print(board[2]),
        print('----')
        print(board[3]),
        print('|'),
        print(board[4]),
        print('|'),
        print(board[5]),
        print('----')
        print(board[6]),
        print('|'),
        print(board[7]),
        print('|'),
        print(board[8])
                    
        
