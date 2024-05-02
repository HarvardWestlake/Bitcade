from ape import accounts, project
from ape import chain

def test_play(accounts):
    owner = accounts[0]
    RNGcontract = project.RNG.deploy(sender=owner)
    diceContract = project.RNGExampleGame.deploy(RNGcontract, sender=owner, value=100000000000000000000000)
    print("contract before bet:")
    print(diceContract.balance)

    player = accounts[1]

    print("player before bet:")
    print(player.balance)

    diceContract.bet(sender=player, value=1000000000000000000)

    print("balls")

    chain.mine(3)

    firstPlayeReceipt = diceContract.play(75, sender=player)

    for log in diceContract.Play.from_receipt(firstPlayeReceipt):
            print("\n\n\n\n\n\n\n")
            print(log.player)
            print(log.result)
            print(log.randomNumber)
            print(log.multiplier)
            assert log.randomNumber > 0, "too smol"
            assert log.randomNumber < 100, "too big"

    print("contract after bet:")
    print(diceContract.balance)

    print("player after bet:")
    print(player.balance)

    assert 1 > 2

    print("Test passed, the balance is 1000")