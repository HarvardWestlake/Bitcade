from ape import accounts, project
from ape import chain

def test_random(accounts):
    #initialize contract and account
    owner = accounts[0] 
    token_contract = project.RNG.deploy(sender=owner)

    for i in range(5):
        print((i + 1) * 10)
        lockedNumberReceipt = token_contract.lock(sender=owner)
        chain.mine(2)
        randomNumberReceipt = token_contract.unlock((i + 1) * 10, sender=owner)
        for log in token_contract.returnRandomNumber.from_receipt(randomNumberReceipt):
            assert log.number <= ((i + 1) * 10)

    print("Test passed: random numbers generated successfully.")


