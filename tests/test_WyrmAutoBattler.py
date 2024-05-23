from ape import accounts, project

def test_battle(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.BattleWyrmToken.deploy(sender=owner)
    auto_battler_contract = project.WyrmAutoBattler.deploy("0x5FbDB2315678afecb367f032d93F642f64180aa3", sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 8):
        user = accounts[i]
        token_contract.mint.call(user, i, sender=owner) == True


    assert auto_battler_contract.battle.call(accounts[1], 1, accounts[2], 2, sender=owner) == accounts[1]

    print("Test passed, battle works.")
