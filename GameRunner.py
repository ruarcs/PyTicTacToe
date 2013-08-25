from Game import *

class GameRunner:
    'This class contains main and runs the game'
        
    def main():
        starting_player = 'O'
        board = ['O', 'X', 'O',
                 ' ', ' ', ' ',
                 'X', ' ', ' ']
        limit_depth = True
        game = Game(starting_player, board, limit_depth)
        game.run_game()
        
    if __name__ == '__main__':
        main()
    
