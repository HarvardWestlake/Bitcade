
# from ape import accounts, project
# import pytest

# # Load the contracts
# @pytest.fixture
# def NFT(NFT):
#     owner = accounts[0]
#     return NFT.deploy(owner, 12345, sender=owner)

# @pytest.fixture
# def purchaseNFT(purchaseNFT, NFT):
#     contract = purchaseNFT.deploy(sender=accounts[0])
#     contract.addNFTContract(NFT.address, sender=accounts[0])
#     return contract

# def test_purchase_nft(NFT, purchaseNFT):
#     # Mint an NFT to accounts[1]
#     mint_tx = NFT.mint(accounts[1], "https://example.com/nft", sender=accounts[0])
#     token_id = mint_tx.events['Transfer']['tokenId']

#     # Set approval for the purchaseNFT contract
#     NFT.setApprovalForAll(purchaseNFT.address, True, sender=accounts[1])

#     # Purchase the NFT
#     price = 1000000000000000000  # 1 ETH
#     purchase_tx = purchaseNFT.purchaseNFT(NFT.address, price, token_id, sender=accounts[2], value=price)

#     # Check the ownership and balance
#     assert NFT.ownerOf(token_id) == accounts[2]
#     assert NFT.balanceOf(accounts[2]) == 1

#     # Check the event
#     assert len(purchase_tx.events) == 1
#     event = purchase_tx.events['PurchaseConfirmation']
#     assert event['buyer'] == accounts[2]
#     assert event['NFTAddress'] == NFT.address
#     assert event['tokenId'] == token_id
#     assert event['price'] == price

# def test_invalid_nft_contract(purchaseNFT):
#     # Deploy a new invalid NFT contract
#     invalid_nft = accounts[0].deploy(NFT.bytecode)

#     # Try to add the invalid contract
#     with pytest.raises(Exception):
#         purchaseNFT.addNFTContract(invalid_nft.address, sender=accounts[0])

# def test_incorrect_payment(NFT, purchaseNFT):
#     # Mint an NFT
#     mint_tx = NFT.mint(accounts[1], "https://example.com/nft", sender=accounts[0])
#     token_id = mint_tx.events['Transfer']['tokenId']

#     # Set approval
#     NFT.setApprovalForAll(purchaseNFT.address, True, sender=accounts[1])

#     # Try to purchase with incorrect payment
#     price = 1000000000000000000  # 1 ETH
#     with pytest.raises(Exception):
#         purchaseNFT.purchaseNFT(NFT.address, price, token_id, sender=accounts[2], value=price - 1)