from ape import accounts, project
from ape import chain

def test_random(accounts):
    #initialize contract and account
    owner = accounts[0] 
    token_contract = project.RNGV2.deploy(sender=owner)

    #test 5 random numbers, make sure they are within range (i + 1) * 10
    for i in range(10):
        blockNumberReceipt = token_contract.lock(sender=owner)
        blockNumber : int = blockNumberReceipt.block_number
        print(blockNumber)

        chain.mine(3)

        balanceBefore = owner.balance

        randomNumber = token_contract.unlock(blockNumber, (i + 1) * 10, sender=owner)
        assert randomNumber >= 0
        assert randomNumber <= (i + 1) * 10

        balanceAfter = owner.balance
        assert balanceAfter == balanceBefore
        print(randomNumber)


    #assert 1 > 2

    print("Test passed: random numbers generated successfully.")
