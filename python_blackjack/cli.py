from app import Game, Player
import os
import time

def addPlayers():
    num = input("Number of players? ")
    players=[]
    for i in range(int(num)):
        player_num = int(i) + 1

        name=input(f"{player_num} name: ")

        players.append(Player(name))

    return players

def gameLoop(game):
    
    game.reset()

    players = [p for p in game.players if p.name != "Dealer"]

    for p in players:
        
        input("..any key to continue to next player")
        os.system("cls")

        print("\n")

        game.nextPlayer()
        hitLoop(game)

    score_to_beat=game.maxPlayerScore()

    print("")

    while (game.dealer.total < score_to_beat):
        input("..any key to continue start Dealer's turn ")

        os.system("cls")

        showPlayer(game.dealer)

        game.dealersTurn()

        recentCard(game)

        time.sleep(3)

    input("..any key to continue and display the winners")

    os.system("cls")

    displayWinners(game)

    nextRound(game)

def recentCard(game):

    p = game._current_player

    card = p.cards[-1]

    total = p.total

    print(f"---{p.name} drew a {str(card).upper()}: total is {p.total}")

    if p.total > 21:
        print(f"---{p.name} busted!")

    print("")


def displayWinners(game):

    print("")
    
    print("Winners are:\n")

    winners = game.checkForWinner()

    for w in winners:
        print(f"---{w.name}")

    print("")

    for p in winners:
        showPlayer(p)

def nextRound(game):

    print("")

    again = input("Again (y/n)? ")

    if (again.lower() == "y"):
        game.nextRound()
        gameLoop(game)
    else:
        print("-----\nGame over")



def hitLoop(game):

        p = game._current_player

        showPlayer(p)

        if game.bust():
            return

        if not game.blackjack():
            choice=input("Draw Card (y)? ")
            print("")

            if choice.lower() == "y":
                game.hit()
                recentCard(game)
                hitLoop(game)


def showPlayer(player):
   
    print(f"{player.name} total is {player.total} with the following cards:")

    for c in player.cards:
        print(f"---{str(c)}: {c.value}")

    print("")

if __name__=="__main__":
    
    game = Game()
    game.reset()
    players=addPlayers()

    game.addPlayers(players)
    game.dealInitialCards()
    gameLoop(game)