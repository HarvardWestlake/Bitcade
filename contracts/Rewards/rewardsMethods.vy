# @version ^0.3.7

# from vyper.interfaces import ERC721

# interface NFTContract:
#     def transferFrom(_from: address, _to: address, _tokenId: uint256, _sender: address): nonpayable
#     def ownerOf(_tokenId: uint256) -> address: view
#     def balanceOf(_owner: address) -> uint256: view
#     def isApprovedForAll(_owner: address, _operator: address) -> bool: view

# event PurchaseConfirmation:
#     buyer: indexed(address)
#     NFTAddress: indexed(address)
#     tokenId: indexed(uint256)
#     price: uint256

# nft_contracts: public(map(address, NFTContract))

# @external
# def purchaseNFT(NFT_address: address, price: uint256, NFT_ID: uint256):
#     """
#     @notice Purchase an NFT by transferring ownership and payment
#     @param NFT_address The address of the NFT contract
#     @param price The price of the NFT in Wei
#     @param NFT_ID The ID of the NFT to purchase
#     """
#     # Check if the NFT contract address is valid
#     assert NFT_address in self.nft_contracts

#     # Get the current owner of the NFT
#     owner: address = NFTContract(NFT_address).ownerOf(NFT_ID)

#     # Prompt user to confirm the purchase (you can implement this using a frontend UI)
#     # After confirmation, transfer the payment from the buyer's account
#     send_value: uint256 = msg.value
#     assert send_value == price, "Incorrect payment amount"

#     # Check if the NFT contract approves this contract for the transfer
#     approved: bool = NFTContract(NFT_address).isApprovedForAll(owner, self)

#     # Transfer the NFT ownership to the buyer
#     NFTContract(NFT_address).transferFrom(owner, msg.sender, NFT_ID, self)

#     # Emit the PurchaseConfirmation event
#     log PurchaseConfirmation(msg.sender, NFT_address, NFT_ID, price)

# @external
# def addNFTContract(nft_address: address):
#     """
#     @notice Add a new NFT contract to the list of supported contracts
#     @param nft_address The address of the NFT contract
#     """
#     self.nft_contracts[nft_address] = NFTContract(nft_address)
    