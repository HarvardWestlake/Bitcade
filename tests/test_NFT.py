import pytest
from ape import accounts
from ape import project as ape_project

@pytest.fixture
def nft_rewards():
    # Deploy the NFTRewards contract with default parameters
    project = ape_project.load()
    return project.NFTRewards.deploy(
        activeUserAddress="0x0000000000000000000000000000000000000000",
        _password=12345,
        _bronzePrice=1000000000000000,  # 1 Ether
        _silverPrice=2000000000000000,  # 2 Ether
        _goldPrice=3000000000000000,    # 3 Ether
        sender=accounts[0]
    )

@pytest.fixture
def test_accounts():
    return accounts

def test_mint_with_ranks(nft_rewards, test_accounts):
    """
    Tests the minting function with different ranks.
    """
    token_uri = "ipfs.io/ipfs/Qmboteb8nEohW5HXprrXeVvYiSFLArh3dYMgX2o7sHi2ai"
    to_address = test_accounts[0].address  # Use the first test account for minting
    expected_ranks = [0, 1, 2]  # Test all ranks

    for expected_rank in expected_ranks:
        test_mint_with_ranks_helper(nft_rewards, test_accounts, token_uri, to_address, expected_rank)

def test_mint_with_ranks_helper(nft_rewards, test_accounts, token_uri, to_address, expected_rank):
    # Check if the token URI is unique
    unique_hash = nft_rewards.keccak256(token_uri)
    assert nft_rewards.uniqueHashesForToken(unique_hash) == 0, "Token URI is not unique"

    # Set the value based on the expected rank
    value = 0
    if expected_rank == 0:
        value = nft_rewards.bronzePrice()
    elif expected_rank == 1:
        value = nft_rewards.silverPrice()
    elif expected_rank == 2:
        value = nft_rewards.goldPrice()
    else:
        raise ValueError("Invalid expected rank")

    # Call the mint function with the set value
    tx = nft_rewards.mint(to_address, token_uri, value=value, sender=test_accounts[0])

    # Check if the token was minted with the correct rank
    token_id = nft_rewards.tokenCount() - 1
    if expected_rank == 0:
        assert nft_rewards.bronzeNFTs(token_id)
    elif expected_rank == 1:
        assert nft_rewards.silverNFTs(token_id)
    elif expected_rank == 2:
        assert nft_rewards.goldNFTs(token_id)

def test_rank_assigned_event(nft_rewards, test_accounts):
    """
    Tests if the RankAssigned event is emitted correctly when minting an NFT.
    """
    token_uri = "default_token_uri"
    to_address = test_accounts[0].address  # Use the first test account for minting
    expected_ranks = [0, 1, 2]  # Test all ranks

    for expected_rank in expected_ranks:
        test_rank_assigned_event_helper(nft_rewards, test_accounts, token_uri, to_address, expected_rank)

def test_rank_assigned_event_helper(nft_rewards, test_accounts, token_uri, to_address, expected_rank):
    # Check if the token URI is unique
    unique_hash = nft_rewards.keccak256(token_uri)
    assert nft_rewards.uniqueHashesForToken(unique_hash) == 0, "Token URI is not unique"

    # Set the value based on the expected rank
    value = 0
    if expected_rank == 0:
        value = nft_rewards.bronzePrice()
    elif expected_rank == 1:
        value = nft_rewards.silverPrice()
    elif expected_rank == 2:
        value = nft_rewards.goldPrice()
    else:
        raise ValueError("Invalid expected rank")

    # Call the mint function and capture the emitted events
    tx = nft_rewards.mint(to_address, token_uri, value=value, sender=test_accounts[0])
    token_id = nft_rewards.tokenCount() - 1

    # Check if the RankAssigned event was emitted with the correct parameters
    assert len(tx.events['RankAssigned']) == 1
    event = tx.events['RankAssigned'][0]
    assert event['owner'] == to_address
    assert event['tokenId'] == token_id
    assert event['rank'] == expected_rank
