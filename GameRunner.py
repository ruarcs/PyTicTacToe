from Game import *

class GameRunner:
    'This class contains main and runs the game'
        
    def main():
        starting_player = 'O'
        board = ['X', ' ', ' ',
                 'O', ' ', ' ',
                 'O', ' ', 'X']
        game = Game(starting_player, board)
        game.run_game()
        
    if __name__ == '__main__':
        main()
    