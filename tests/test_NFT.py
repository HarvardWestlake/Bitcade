import pytest
import brownie
from web3.exceptions import ValidationError

DEFAULT_GAS = 100000


@pytest.fixture
def NFT(NFT, accounts):
    return NFT.deploy(
        accounts[0],
        12345, # password
        {'from': accounts[3]}
    )

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