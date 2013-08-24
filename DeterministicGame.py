class DeterministicGame:
    def __init__(self):
        starting_player = 'X'
        board = ['_', 'X', '_',
                 'O', 'X', '_',
                 'O', '_', '_']
        vectors = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def main():
        run_game()

    def run_game():
        pass

    def make_move(self):
        made_move = False
        won = False

        made_move = win()
        if ~made_move:
            made_move = block()
        else:
            won = True

        '''
        # For the moment don't worry about
        # forking, or about opponents forks,
        # it makes things much more complicated.
        
        if ~made_move:
            made_move = fork()       
        
        if ~made_move:
            made_move = block_fork()
        '''
        
        if ~made_move:
            made_move = center() 

        if ~made_move:
            made_move = opposite_corner() 

        if ~made_move:
            made_move = empty_corner() 

        if ~made_move:
            made_move = empty_side()

        if ~made_move:
            made_move = random_place()        

        print_board_state()

    def win(self):
        action = 'win'
        for vector in vectors:
            if analyse_vector(action):
                return True
        return False

    def block(self):
        action = 'block'
        for vector in vectors:
            if analyse_vector(action):
                return True
        return False

    def fork(self):
        return False

    def block_fork(self):
        return False

    def center(self):
        return False

    def opposite_corner(self):
        return False

    def empty_corner(self):
        return False

    def empty_side(self):
        return False

    def random_place(self):
        return False

    ###################################

    def analyse_vector(self,action):
        pass

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

    ###################################

    if __name__ == '__main__':
        main()
