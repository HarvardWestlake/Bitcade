import pytest
from ape import accounts, project

@pytest.fixture
def nft_rewards(accounts):
    
    # Deploy the NFT contract with default parameters
    return project.NFT.deploy(
        accounts[0], 
        12345, 
        1000000000000000, 
        2000000000000000, 
        3000000000000000, 
        sender=accounts[0]
        )
        

@pytest.fixture
def test_accounts():
    return accounts

def test_mint_with_ranks(accounts, nft_rewards): # type: ignore
    """
    Tests the minting function with different ranks.
    """
    token_uri = "1234567890123456789012345678901234567890123456789012345678901234"
    to_address = accounts[0]  # Use the first test account for minting

    #test bronze minting
    nft_rewards.mint(
        to_address, 
        token_uri, 
        sender=accounts[0], 
        value=1000000000000000
    )

    assert nft_rewards.getBronzeNFT(
        0, 
        sender=accounts[0]
    ) == True

    # #test silver minting
    # nft_rewards.mint(
    #     to_address, 
    #     token_uri+"a", 
    #     sender=accounts[0], 
    #     value=2000000000000000
    # )

    # assert nft_rewards.getSilverNFT(
    #     1, 
    #     sender=accounts[0]
    # ) == True

    # #test gold minting
    # nft_rewards.mint(
    #     to_address, 
    #     token_uri+"b", 
    #     sender=accounts[0], 
    #     value=3000000000000000
    # )

    # assert nft_rewards.getGoldNFT(
    #     2, 
    #     sender=accounts[0]
    # ) == True

