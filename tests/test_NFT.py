import brownie
import pytest

@pytest.fixture
def nft_rewards(project):
    # Deploy the NFTRewards contract with default parameters
    return project.NFTRewards.deploy(
        activeUserAddress="0x0000000000000000000000000000000000000000",
        _password=12345,
        _bronzePrice=1000000000000000,  # 1 Ether
        _silverPrice=2000000000000000,  # 2 Ether
        _goldPrice=3000000000000000,    # 3 Ether
    )

@pytest.fixture
def accounts(nft_rewards):
    return brownie.accounts

def test_mint_with_ranks(nft_rewards, accounts):
    """
    Tests the minting function with different ranks.
    """
    token_uri = "default_token_uri"
    to_address = accounts[0].address  # Use the first test account for minting
    expected_ranks = [0, 1, 2]  # Test all ranks

    for expected_rank in expected_ranks:
        test_mint_with_ranks_helper(nft_rewards, accounts, token_uri, to_address, expected_rank)

def test_mint_with_ranks_helper(nft_rewards, accounts, token_uri, to_address, expected_rank):
    # Check if the token URI is unique
    uniqueHash = nft_rewards.keccak256(token_uri)
    assert nft_rewards.uniqueHashesForToken(uniqueHash) == 0, "Token URI is not unique"

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
    nft_rewards.mint(to_address, token_uri, {'from': accounts[0], 'value': value})

    # Check if the token was minted with the correct rank
    tokenId = nft_rewards.tokenCount() - 1
    if expected_rank == 0:
        assert nft_rewards.bronzeNFTs(tokenId)
    elif expected_rank == 1:
        assert nft_rewards.silverNFTs(tokenId)
    elif expected_rank == 2:
        assert nft_rewards.goldNFTs(tokenId)

def test_rank_assigned_event(nft_rewards, accounts):
    """
    Tests if the RankAssigned event is emitted correctly when minting an NFT.
    """
    token_uri = "default_token_uri"
    to_address = accounts[0].address  # Use the first test account for minting
    expected_ranks = [0, 1, 2]  # Test all ranks

    for expected_rank in expected_ranks:
        test_rank_assigned_event_helper(nft_rewards, accounts, token_uri, to_address, expected_rank)

def test_rank_assigned_event_helper(nft_rewards, accounts, token_uri, to_address, expected_rank):
    # Check if the token URI is unique
    uniqueHash = nft_rewards.keccak256(token_uri)
    assert nft_rewards.uniqueHashesForToken(uniqueHash) == 0, "Token URI is not unique"

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
    tx = nft_rewards.mint(to_address, token_uri, {'from': accounts[0], 'value': value})
    tokenId = nft_rewards.tokenCount() - 1

    # Check if the RankAssigned event was emitted with the correct parameters
    assert len(tx.events['RankAssigned']) == 1
    event = tx.events['RankAssigned'][0]
    assert event['owner'] == to_address
    assert event['tokenId'] == tokenId
    assert event['rank'] == expected_rank

#old code

# import pytest
# from web3.exceptions import ValidationError
# from brownie import Contract

# DEFAULT_GAS = 100000


# @pytest.fixture
# def NFT(accounts):

#     #The following code returns a recursive dependency error and has been commented out
#     # return NFT.deploy(
#     #     accounts[0],
#     #     12345, # password
#     #     {'from': accounts[3]} )

#     # Load the contract from the build artifact
#     nft_contract = Contract.from_abi("NFT", "contracts/Rewards/NFT.vy", owner=accounts[0])
#     # Deploy the contract
#     # _bronzePrice: 1000, _silverPrice: 2000, _goldPrice: 3000 (placeholder prices)
#     tx = nft_contract.deploy(accounts[0], 12345, 1000, 2000, 3000, {'from': accounts[3]})
#     return nft_contract

# def testMintWithRanks(NFT, accounts):
#     # Test minting a bronze NFT
#     mint_tx = NFT.mint(accounts[3], "https://example.com?bronze", {'from': accounts[3], 'value': 1000})
#     minted_token_id = mint_tx.events["Transfer"]["tokenId"]
#     assert NFT.getTokenURIByTokenId(minted_token_id) == "https://example.com?bronze"
#     bronze_nfts = NFT.getBronzeNFTs()
#     assert minted_token_id in bronze_nfts

#     # Test minting a silver NFT
#     mint_tx = NFT.mint(accounts[3], "https://example.com?silver", {'from': accounts[3], 'value': 2000})
#     minted_token_id = mint_tx.events["Transfer"]["tokenId"]
#     assert NFT.getTokenURIByTokenId(minted_token_id) == "https://example.com?silver"
#     silver_nfts = NFT.getSilverNFTs()
#     assert minted_token_id in silver_nfts

#     # Test minting a gold NFT
#     mint_tx = NFT.mint(accounts[3], "https://example.com?gold", {'from': accounts[3], 'value': 3000})
#     minted_token_id = mint_tx.events["Transfer"]["tokenId"]
#     assert NFT.getTokenURIByTokenId(minted_token_id) == "https://example.com?gold"
#     gold_nfts = NFT.getGoldNFTs()
#     assert minted_token_id in gold_nfts

#     # Test invalid price
#     with pytest.raises(ValueError):
#         NFT.mint(accounts[3], "https://example.com?invalid", {'from': accounts[3], 'value': 4000})

# def testRankAssignedEvent(NFT, accounts):
#     # Test RankAssigned event emission
#     mint_tx = NFT.mint(accounts[3], "https://example.com?bronze", {'from': accounts[3], 'value': 1000})
#     minted_token_id = mint_tx.events["Transfer"]["tokenId"]
#     rank_assigned_event = mint_tx.events["RankAssigned"]
#     assert rank_assigned_event["owner"] == accounts[3]
#     assert rank_assigned_event["tokenId"] == minted_token_id
#     assert rank_assigned_event["rank"] == 0  # Bronze rank