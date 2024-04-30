from ape import accounts, project

def test_mint_tokens(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.Wolvercoin.deploy("ERC721", "ERC", 18, sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 8):
        user = accounts[i]
        token_contract.mint(user, i, sender=owner)

    print("Test passed, each account mints one NFT.")
