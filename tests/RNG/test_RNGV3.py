from ape import accounts, project
from ape import chain

def test_random(accounts):
    #initialize contract and account
    owner = accounts[0] 
    token_contract = project.RNGV3.deploy(sender=owner)

    initialLock = token_contract.lockCurrent(sender=owner)

    #test 5 random numbers, make sure they are within range (i + 1) * 10
    for i in range(9):
        chain.mine(3)
        randomNumber = token_contract.updateLock((i + 1) * 10, sender=owner)
        for log in token_contract.returnRandomNumber.from_receipt(randomNumber):
            assert log.number <= (100)
            assert log.number >= 0
            print (log.number)

    chain.mine(3)

    randomNumber = token_contract.unlockLatest(100, sender=owner)
    for log in token_contract.returnRandomNumber.from_receipt(randomNumber):
            assert log.number <= (100)
            assert log.number >= 0
            print (log.number)

    #stress test!!!!!!!! 
    #uncomment the below code to see average of 100 random numbers 
    #with range 100 - should be around 50
    # initialLock = token_contract.lockCurrent(sender=owner)
    # total = 0

    # for i in range(99):
    #     chain.mine(3)
    #     randomNumber = token_contract.updateLock(100, sender=owner)
    #     for log in token_contract.returnRandomNumber.from_receipt(randomNumber):
    #         total += log.number
    #         print (log.number)

    # chain.mine(3)

    # randomNumber = token_contract.unlockLatest(100, sender=owner)
    # for log in token_contract.returnRandomNumber.from_receipt(randomNumber):
    #         total += log.number
    #         print (log.number)
    
    # print(total/100)

    # assert 1 > 2

    print("Test passed: random numbers generated successfully.")
