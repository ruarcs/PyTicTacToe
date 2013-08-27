from Game import *

class GameRunner:
    'This class contains main and runs the game'
        
    def main():
        
        limit_depth = True
        from_file = True
        
        filename = raw_input("Enter the name of your game file of choice:")
        file = open(filename, 'r')
        
        num_games = int(file.read(1))
        games = []
        starting_player = ''
        
        for game_number in range(0,num_games):
            board = []
            file.seek(1,1)
            starting_player = file.read(1)
            file.seek(1,1)
            
            for position in range(0,3):
                board.append(file.read(1))
            file.seek(1,1)          
            for position in range(3,6):
                board.append(file.read(1))
            file.seek(1,1)   
            for position in range(6,9):
                board.append(file.read(1))      
                   
            game = Game(starting_player, board, limit_depth, from_file)
            games.append(game)
            
        file.close()
        file = open('output.txt', 'w')
            
        game_count = 1
        for game in games:
            game_result = game.run_game()
            result = 'Case {}'.format(game_count) + ': ' + game_result
            file.write(result)
            file.write('\n')
            game_count = game_count + 1
            
        file.close()
        
    if __name__ == '__main__':
        main()
    
