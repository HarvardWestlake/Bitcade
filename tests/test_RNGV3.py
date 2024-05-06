from ape import accounts, project
from ape import chain

def test_random(accounts):
    #initialize contract and account
    owner = accounts[0] 
    token_contract = project.RNGV3.deploy(sender=owner)

    initialLock = token_contract.lock(sender=owner)

    #test 5 random numbers, make sure they are within range (i + 1) * 10
    for i in range(9):
        accounts[i].transfer(accounts[i + 1], i * 100000)
        for k in range(3):
            chain.mine(1)
            accounts[k].transfer(accounts[k + 1], (k + i) * 100000)
        accounts[i + 1].transfer(accounts[i], (i * 200000))

        randomNumber = token_contract.lockAndUnlock.call((i + 1) * 10, sender=owner)
        #assert randomNumber >= 0
        #assert randomNumber <= (i + 1) * 10
        print(randomNumber)
        #print(token_contract.getLockedBlock(sender=owner))
    
    finalUnlock = token_contract.unlock.call(100, sender=owner)

    assert 1 > 2

    print("Test passed: random numbers generated successfully.")
