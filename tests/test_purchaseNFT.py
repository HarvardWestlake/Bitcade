import brownie
import pytest

# Load the contracts
@pytest.fixture
def NFT(NFT, accounts):
    return NFT.deploy(accounts[0], 12345, {'from': accounts[0]})

@pytest.fixture
def purchaseNFT(purchaseNFT, NFT, accounts):
    contract = purchaseNFT.deploy({'from': accounts[0]})
    contract.addNFTContract(NFT.address, {'from': accounts[0]})
    return contract

def test_purchase_nft(NFT, purchaseNFT, accounts):
    # Mint an NFT to accounts[1]
    mint_tx = NFT.mint(accounts[1], "https://example.com/nft", {'from': accounts[0]})
    token_id = mint_tx.events['Transfer']['tokenId']

    # Set approval for the purchaseNFT contract
    NFT.setApprovalForAll(purchaseNFT.address, True, {'from': accounts[1]})

    # Purchase the NFT
    price = 1000000000000000000  # 1 ETH
    purchase_tx = purchaseNFT.purchaseNFT(NFT.address, price, token_id, {'from': accounts[2], 'value': price})

    # Check the ownership and balance
    assert NFT.ownerOf(token_id) == accounts[2]
    assert NFT.balanceOf(accounts[2]) == 1

    # Check the event
    assert len(purchase_tx.events) == 1
    event = purchase_tx.events['PurchaseConfirmation']
    assert event['buyer'] == accounts[2]
    assert event['NFTAddress'] == NFT.address
    assert event['tokenId'] == token_id
    assert event['price'] == price

def test_invalid_nft_contract(purchaseNFT, accounts):
    # Deploy a new NFT contract
    invalid_nft = accounts[0].deploy(NFT.bytecode)

    # Try to add the invalid contract
    with brownie.reverts("dev: contract at 0x"):
        purchaseNFT.addNFTContract(invalid_nft.address, {'from': accounts[0]})

def test_incorrect_payment(NFT, purchaseNFT, accounts):
    # Mint an NFT
    mint_tx = NFT.mint(accounts[1], "https://example.com/nft", {'from': accounts[0]})
    token_id = mint_tx.events['Transfer']['tokenId']

    # Set approval
    NFT.setApprovalForAll(purchaseNFT.address, True, {'from': accounts[1]})

    # Try to purchase with incorrect payment
    price = 1000000000000000000  # 1 ETH
    with brownie.reverts("Incorrect payment amount"):
        purchaseNFT.purchaseNFT(NFT.address, price, token_id, {'from': accounts[2], 'value': price - 1})