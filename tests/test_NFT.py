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
    token_uri = "default_token_uri"
    to_address = accounts[0].address  # Use the first test account for minting
    expected_ranks = [0, 1, 2]  # Test all ranks

    for expected_rank in expected_ranks:

        # Check if the token URI is unique
        # unique_hash = hash(token_uri)
        # assert nft_rewards.contains(unique_hash) == 0, "Token URI is not unique"

        # Set the value based on the expected rank
        value = 0
        if expected_rank == 0:
            value = 1000000000000000 #bronzePrice
        elif expected_rank == 1:
            value = 2000000000000000 #silverPrice
        elif expected_rank == 2:
            value = 3000000000000000 #goldPrice
        else:
            raise ValueError("Invalid expected rank")

        # # Call the mint function with the set value

        assert nft_rewards.mint(
            to_address, 
            token_uri, 
            sender=accounts[0], 
            value=1000000000000000
        ) == True

        # # Check if thes token was minted with the correct rank
        #token_id = nft_rewards.tokenCount() - 1
        # if expected_rank == 0:
        #     assert nft_rewards.bronzeNFTs(token_id)
        # elif expected_rank == 1:
        #     assert nft_rewards.silverNFTs(token_id)
        # elif expected_rank == 2:
        #     assert nft_rewards.goldNFTs(token_id)


# def test_rank_assigned_event(nft_rewards: Contract, test_accounts: accounts): # type: ignore
#     """
#     Tests if the RankAssigned event is emitted correctly when minting an NFT.
#     """
#     token_uri = "default_token_uri"
#     to_address = test_accounts[0].address  # Use the first test account for minting
#     expected_ranks = [0, 1, 2]  # Test all ranks

#     for expected_rank in expected_ranks:
#         test_rank_assigned_event_helper(nft_rewards, test_accounts, token_uri, to_address, expected_rank)

# def test_rank_assigned_event_helper(nft_rewards: Contract, test_accounts: accounts, token_uri, to_address, expected_rank): # type: ignore
#     # Check if the token URI is unique
#     unique_hash = nft_rewards.keccak256(token_uri)
#     assert nft_rewards.uniqueHashesForToken(unique_hash) == 0, "Token URI is not unique"

#     # Set the value based on the expected rank
#     value = 0
#     if expected_rank == 0:
#         value = nft_rewards.bronzePrice()
#     elif expected_rank == 1:
#         value = nft_rewards.silverPrice()
#     elif expected_rank == 2:
#         value = nft_rewards.goldPrice()
#     else:
#         raise ValueError("Invalid expected rank")

#     # Call the mint function and capture the emitted events
#     tx = nft_rewards.mint(to_address, token_uri, value=value, sender=test_accounts[0])
#     token_id = nft_rewards.tokenCount() - 1

#     # Check if the RankAssigned event was emitted with the correct parameters
#     assert len(tx.events['RankAssigned']) == 1
#     event = tx.events['RankAssigned'][0]
#     assert event['owner'] == to_address
#     assert event['tokenId'] == token_id
#     assert event['rank'] == expected_rank
