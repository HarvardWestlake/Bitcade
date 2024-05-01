from ape import accounts, project

def test_mint_tokens(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.ERC721.deploy(sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 8):
        user = accounts[i]
        assert token_contract.mint(user, i, sender=owner).status == 1

    for i in range (1, 8):
        assert token_contract.ownerOf.call(i, sender=owner) == accounts[i]

    print("Test passed, successfully minted NFTs and updated owner.")
