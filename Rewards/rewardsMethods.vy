# @version ^0.3.7

from vyper.interfaces import ERC721

interface NFTContract:
    def transferFrom(_from: address, _to: address, _tokenId: uint256, _sender: address): nonpayable
    def ownerOf(_tokenId: uint256) -> address: view
    def balanceOf(_owner: address) -> uint256: view
    def isApprovedForAll(_owner: address, _operator: address) -> bool: view

event PurchaseConfirmation:
    buyer: indexed(address)
    NFTAddress: indexed(address)
    tokenId: indexed(uint256)
    price: uint256

nft_contracts: public(map(address, NFTContract))

@external
def purchaseNFT(NFT_address: address, price: uint256, NFT_ID: uint256):
    """
    @notice Purchase an NFT by transferring ownership and payment
    @param NFT_address The address of the NFT contract
    @param price The price of the NFT in Wei
    @param NFT_ID The ID of the NFT to purchase
    """
    # Check if the NFT contract address is valid
    assert NFT_address in self.nft_contracts

    # Get the current owner of the NFT
    owner: address = NFTContract(NFT_address).ownerOf(NFT_ID)

    # Prompt user to confirm the purchase (you can implement this using a frontend UI)
    # After confirmation, transfer the payment from the buyer's account
    send_value: uint256 = msg.value
    assert send_value == price, "Incorrect payment amount"

    # Check if the NFT contract approves this contract for the transfer
    approved: bool = NFTContract(NFT_address).isApprovedForAll(owner, self)

    # Transfer the NFT ownership to the buyer
    NFTContract(NFT_address).transferFrom(owner, msg.sender, NFT_ID, self)

    # Emit the PurchaseConfirmation event
    log PurchaseConfirmation(msg.sender, NFT_address, NFT_ID, price)

@external
def addNFTContract(nft_address: address):
    """
    @notice Add a new NFT contract to the list of supported contracts
    @param nft_address The address of the NFT contract
    """
    self.nft_contracts[nft_address] = NFTContract(nft_address)

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
    assert rank_assigned_event["rank"] == 1  # Bronze rank