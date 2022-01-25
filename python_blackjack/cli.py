from app import Game, Player

def addPlayers():
    num = input("Number of players? ")
    players=[]
    for i in range(int(num)):
        player_num = int(i) + 1

        name=input(f"{player_num} name: ")

        players.append(Player(name))

    return players

def gameLoop(game):
#for every player give the chance to draw card
#before drawing card player total must be less than 21

    for p in game.players:
        print("\n")

        game.nextPlayer()
        hitLoop(game)
        
def hitLoop(game):
        p = game._current_player

        showPlayer(p)

        if game.bust():
            print("\nYou've busted")
            return

        choice=input("Draw Card (y)? ")

        if choice.lower() == "y":
            game.hit()
            hitLoop(game)


def showPlayer(player):
     print(f"{str(player)}: Total is {player.total}")

if __name__=="__main__":
    
    game = Game()
    game.reset()
    players=addPlayers()

    game.addPlayers(players)
    game.dealInitialCards()
    gameLoop(game)