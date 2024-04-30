from ape import accounts, project
from ape import chain

def test_random(accounts):
    #initialize contract and account
    owner = accounts[0] 
    token_contract = project.RNG.deploy(sender=owner)

    #test 5 random numbers, make sure they are within range (i + 1) * 10
    for i in range(10):
        lockedNumberReceipt = token_contract.lock(sender=owner)
        chain.mine(2)
        randomNumberReceipt = token_contract.unlock((i + 1) * 10, sender=owner)
        for log in token_contract.returnRandomNumber.from_receipt(randomNumberReceipt):
            assert log.number <= ((i + 1) * 10)
            assert log.number >= 0
            print (log.number)
    
    #The below code shows the average of 100 random numbers
    #After running test, scroll up past all the INFO statements
    #It will be the last number printed
    #Takes a while to run... Ctrl + c to end
    total = 0
    for i in range(100):
        lockedNumberReceipt = token_contract.lock(sender=owner)
        chain.mine(2)
        randomNumberReceipt = token_contract.unlock(100, sender=owner)
        for log in token_contract.returnRandomNumber.from_receipt(randomNumberReceipt):
            total += log.number
    print(total/100)
    
    #print statmeents will only show if test fails, hence:
    #assert 1 > 2

    print("Test passed: random numbers generated successfully.")


