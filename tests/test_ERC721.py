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

def test_token_urls(accounts):
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.ERC721.deploy(sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 8):
        user = accounts[i]
        assert token_contract.mint(user, i, sender=owner).status == 1

    for i in range (1, 8):
        assert token_contract.tokenURI.call(i, sender=owner) == "ipfs://QmexVFiUTpkuRJVLmcgKFd5SHVR7doCLipuVRy2kyNWzq2/" + str(i) + ".json"

    print("Test passed, successfully linked urls to tokens.")

def test_transfering_tokens(accounts):
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.ERC721.deploy(sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 4):
        user = accounts[i]
        assert token_contract.mint(user, i, sender=owner).status == 1
        token_contract.transferFrom(user, accounts[i+4], i, sender=user)
    
    for i in range(1, 4):
        user = accounts[i]
        assert token_contract.ownerOf.call(i, sender=owner) == accounts[i+4]
        assert token_contract.balanceOf.call(user, sender=owner) == 0
        assert token_contract.balanceOf.call(accounts[i+4], sender=owner) == 1
        

    print("Test passed, successfully transferred tokens from one account to another.")