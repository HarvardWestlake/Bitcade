from ape import accounts, project
from ape import chain

def test_play(accounts):
    owner = accounts[0]
    RNGcontract = project.RNGV3.deploy(sender=owner)
    diceContract = project.RNGV3ExampleGame.deploy(RNGcontract, sender=owner, value=100000000000000000000000)

    player = accounts[1]

    startGameReceipt = diceContract.startGame(sender=player, value=1000000000000000000)

    print("\n\n\n\nSTART GAME")
    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    chain.mine(3)

    betReceipt = diceContract.playGame(75, sender=player, value=1000000000000000000)

    print("\n\n\nPLAY GAME")
    for log in diceContract.Play.from_receipt(betReceipt):
        print(log.result) 
        print(log.winnings) 
        print(log.randomNumber)
        print(log.multiplier)
        print(log.player)
    
    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    chain.mine(3)

    betReceipt = diceContract.cashOut(75, sender=player)

    print("\n\n\nEND GAME")
    for log in diceContract.Play.from_receipt(betReceipt):
        print(log.result) 
        print(log.winnings) 
        print(log.randomNumber)
        print(log.multiplier)
        print(log.player)

    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    assert 1 > 2

    print("Test passed, the balance is 1000")
