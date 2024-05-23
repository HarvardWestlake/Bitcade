from ape import accounts, project

def test_account_balance(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    contract = project.RockPaperScissors.deploy(sender=owner)

    contract.initBalance(1000, sender=owner)
    assert contract.getAccountBalance(sender=owner) == 1000

    print("Test passed, the balance is 1000")

def test_play(accounts):
    # Deploy the contract
    p1 = accounts[0]  # Assuming the first account is the owner
    p2 = accounts[1]
    contract = project.RockPaperScissors.deploy(sender=p1)


    contract.initBalance(1000, sender=p1)
    contract.initBalance(1000, sender=p2)

    contract.createGame(10, p2, sender=p1)
    
    #dummy random
    contract.joinGame(0, 2, 480291384093284, sender=p1)
    contract.joinGame(0, 1, 480291384093285, sender=p2)

    contract.revealChoice(0, 2, 480291384093284, sender=p1)
    contract.revealChoice(0, 1, 480291384093285, sender=p2)

    assert contract.getAccountBalance(sender=p1) == 1010
    assert contract.getAccountBalance(sender=p2) == 990

    print("Test passed")