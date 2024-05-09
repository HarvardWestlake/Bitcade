from ape import accounts, project
from ape import chain

def test_play(accounts):
    owner = accounts[0]
    RNGcontract = project.RNGV3.deploy(sender=owner)
    diceContract = project.RNGV3ExampleGame.deploy(RNGcontract, sender=owner, value=100000000000000000000000)

    player = accounts[1]

    #start a "betting session"
    #set an inital bet value
    #stake and pay for your first bet
    startGameReceipt = diceContract.startGame(sender=player, value=1000000000000000000)

    print("\n\n\n\nSTART GAME")
    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    #Play the game 9 times
    for i in range(9):
        chain.mine(3)
        betReceipt = diceContract.playGame((i + 1) * 10, sender=player, value=1000000000000000000 * (i + 1))

        print("\n\n\nPLAY GAME")
        for log in diceContract.Play.from_receipt(betReceipt):
            print(log.randomNumber)
            print((i + 1) * 10)
            assert log.randomNumber <= 100
            assert log.randomNumber >= 0
            print(log.result) 
            if (log.randomNumber >= (i + 1) * 10):
                assert log.result == False
            else:
                assert log.result == True
            print(log.winnings) 
            print(log.multiplier)
            print(log.player)
        
            print("contract after bet:")
            print(diceContract.balance)

            print("player after bet:")
            print(player.balance)

    chain.mine(3)

    #cashOut game by submitting your last bet
    #no payment needed because you've already (only gas fees)
    #staked your bet on the previous turn
    betReceipt = diceContract.cashOut(99, sender=player)

    print("\n\n\nEND GAME")
    for log in diceContract.Play.from_receipt(betReceipt):
        print(log.randomNumber)
        print((i + 1) * 10)
        print(log.result) 
        print(log.winnings) 
        print(log.multiplier)
        print(log.player)

    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    assert 1 > 2

    print("Test passed, all bets worked")