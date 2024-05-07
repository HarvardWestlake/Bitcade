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
        randomNumberReceipt = token_contract.unlock(100, sender=owner)
        #print(randomNumberReceipt)
        for log in token_contract.returnRandomNumber.from_receipt(randomNumberReceipt):
            assert log.number <= (100)
            assert log.number >= 0
            print (log.number)
    
    #The below code shows the average of 100 random numbers
    #After running test, scroll up past all the INFO statements
    #It will be the last number printed
    #Takes a while to run... Ctrl + c to end
    #total = 0
    #for i in range(100):
       # lockedNumberReceipt = token_contract.lock(sender=owner)
       # chain.mine(2)
       # randomNumberReceipt = token_contract.unlock(100, sender=owner)
       # for log in token_contract.returnRandomNumber.from_receipt(randomNumberReceipt):
       #     total += log.number
    #print(total/100)
    
    #print statmeents will only show if test fails, hence:
    assert 1 > 2

    print("Test passed: random numbers generated successfully.")

# def test_random_between(accounts):
#     owner = accounts[0]
#     rng_contract = project.RNG.deploy(sender=owner)

#     test_ranges = [(1, 10), (20, 30), (100, 110)]

#     for min_range, max_range in test_ranges:
#         rng_contract.lock(sender=owner)
#         chain.mine(2)
#         random_number_receipt = rng_contract.random_between(min_range, max_range, sender=owner)
#         for log in rng_contract.returnRandomNumber.from_receipt(random_number_receipt):
#             assert log.number >= min_range and log.number <= max_range
#             print(f"Generated random number: {log.number} in range ({min_range}, {max_range})")

#         rng_contract.reset_lock(sender=owner)

#     for _ in range(10):
#         min_val, max_val = 50, 60
#         rng_contract.lock(sender=owner)
#         chain.mine(2)
#         random_number_receipt = rng_contract.random_between(min_val, max_val, sender=owner)
#         for log in rng_contract.returnRandomNumber.from_receipt(random_number_receipt):
#             assert log.number >= min_val and log.number <= max_val
#             print(f"Repeated test - random number: {log.number}")

#         rng_contract.reset_lock(sender=owner)

    print("All tests passed successfully.")
