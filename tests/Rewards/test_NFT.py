import pytest
from web3.exceptions import ValidationError
from brownie import Contract

DEFAULT_GAS = 100000


@pytest.fixture
def NFT(accounts):

    #The following code returns a recursive dependency error and has been commented out
    # return NFT.deploy(
    #     accounts[0],
    #     12345, # password
    #     {'from': accounts[3]} )

    # Load the contract from the build artifact
    nft_contract = Contract.from_abi("NFT", "contracts/Rewards/NFT.vy", owner=accounts[0])
    # Deploy the contract
    # _bronzePrice: 1000, _silverPrice: 2000, _goldPrice: 3000 (placeholder prices)
    tx = nft_contract.deploy(accounts[0], 12345, 1000, 2000, 3000, {'from': accounts[3]})
    return nft_contract
    

def testApprove_OwnerOf(NFT, accounts):
    #coverage for approve, balanceOf, getApproved, ownerOf
    mintResult = NFT.mint(accounts[3], "https://example.com?ricepurity", {'from': accounts[3]})
    mintedTokenId = mintResult.events["Transfer"]["tokenId"]
    assert NFT.ownerOf(mintedTokenId) == accounts[3]
    NFT.approve(accounts[0], mintedTokenId)
    assert NFT.getApproved(mintedTokenId) == accounts[0]
    assert NFT.balanceOf(accounts[3]) == 1

def testTokenByIndex(NFT, accounts):
    #coverage for tokenOfOwnerByIndex
    mintResult = NFT.mint(accounts[3], "https://example.com?ricepurity", {'from': accounts[3]})
    mintedTokenId = mintResult.events["Transfer"]["tokenId"]
    mintResult2 = NFT.mint(accounts[3], "https://example.com?ricepurity2", {'from': accounts[3]})
    mintedTokenId2 = mintResult.events["Transfer"]["tokenId"]
    assert NFT.tokenOfOwnerByIndex(accounts[3], 1) == 2


def testMintWithRanks(NFT, accounts):
    # Test minting a bronze NFT
    mint_tx = NFT.mint(accounts[3], "https://example.com?bronze", {'from': accounts[3], 'value': 1000})
    minted_token_id = mint_tx.events["Transfer"]["tokenId"]
    assert NFT.getTokenURIByTokenId(minted_token_id) == "https://example.com?bronze"
    bronze_nfts = NFT.getBronzeNFTs()
    assert minted_token_id in bronze_nfts

    # Test minting a silver NFT
    mint_tx = NFT.mint(accounts[3], "https://example.com?silver", {'from': accounts[3], 'value': 2000})
    minted_token_id = mint_tx.events["Transfer"]["tokenId"]
    assert NFT.getTokenURIByTokenId(minted_token_id) == "https://example.com?silver"
    silver_nfts = NFT.getSilverNFTs()
    assert minted_token_id in silver_nfts

    # Test minting a gold NFT
    mint_tx = NFT.mint(accounts[3], "https://example.com?gold", {'from': accounts[3], 'value': 3000})
    minted_token_id = mint_tx.events["Transfer"]["tokenId"]
    assert NFT.getTokenURIByTokenId(minted_token_id) == "https://example.com?gold"
    gold_nfts = NFT.getGoldNFTs()
    assert minted_token_id in gold_nfts

    # Test invalid price
    with pytest.raises(ValueError):
        NFT.mint(accounts[3], "https://example.com?invalid", {'from': accounts[3], 'value': 4000})

def testRankAssignedEvent(NFT, accounts):
    # Test RankAssigned event emission
    mint_tx = NFT.mint(accounts[3], "https://example.com?bronze", {'from': accounts[3], 'value': 1000})
    minted_token_id = mint_tx.events["Transfer"]["tokenId"]
    rank_assigned_event = mint_tx.events["RankAssigned"]
    assert rank_assigned_event["owner"] == accounts[3]
    assert rank_assigned_event["tokenId"] == minted_token_id
    assert rank_assigned_event["rank"] == 0  # Bronze rank