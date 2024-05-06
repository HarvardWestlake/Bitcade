from ape import accounts, project
from ape import chain

def test_play(accounts):
    owner = accounts[0]
    RNGcontract = project.RNGV2.deploy(sender=owner)
    diceContract = project.RNGV2ExampleGame.deploy(RNGcontract, sender=owner, value=100000000000000000000000)

    player = accounts[1]

    betReceipt = diceContract.bet(sender=player, value=1000000000000000000)

    for log in diceContract.Betted.from_receipt(betReceipt):
        print(log.blockNumber)
        print(log.msgValue)

    print("balls")

    chain.mine(3)

    playResult = diceContract.play.call(betReceipt.block_number, 99, sender=player)

    print(playResult)

    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    assert 1 > 2

    print("Test passed, the balance is 1000")