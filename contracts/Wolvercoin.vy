# @version ^0.3.10
from vyper.interfaces import ERC20

implements: ERC20
# Define Events
event Approval:
    owner: indexed(address)
    spender: indexed(address)
    value: uint256

event Transfer:
    sender: indexed(address)
    receiver: indexed(address)
    amount: uint256

# State variables with public getters
name: public(String[64])
symbol: public(String[32])
decimals: public(uint256)
totalSupply: public(uint256)
balanceOf: public(HashMap[address, uint256])
allowance: public(HashMap[address, HashMap[address, uint256]])


# Initialize the Token
@external
def __init__(_name: String[64], _symbol: String[32], _decimals: uint256):
    self.name = _name
    self.symbol = _symbol
    self.decimals = _decimals
    self.totalSupply = 0  # Initialize total supply

# Mint new tokens
@external
def mint(_to: address, _amount: uint256):
    assert self.balanceOf[_to] + _amount >= self.balanceOf[_to], "Overflow"
    self.balanceOf[_to] += _amount
    self.totalSupply += _amount
    log Transfer(ZERO_ADDRESS, _to, _amount)

# Transfer tokens to another address
@external
def transfer(_to: address, _amount: uint256) -> bool:
    assert self.balanceOf[msg.sender] >= _amount, "Insufficient balance"
    self.balanceOf[msg.sender] -= _amount
    self.balanceOf[_to] += _amount
    log Transfer(msg.sender, _to, _amount)
    return True

# Approve the spender to withdraw from your account multiple times, up to the _value amount.
@external
def approve(_spender: address, _value: uint256) -> bool:
    self.allowance[msg.sender][_spender] = _value
    log Approval(msg.sender, _spender, _value)
    return True

# Transfer tokens from one address to another
@external
def transferFrom(_from: address, _to: address, _amount: uint256) -> bool:
    assert self.allowance[_from][msg.sender] >= _amount, "Allowance too low"
    assert self.balanceOf[_from] >= _amount, "Insufficient balance"
    self.balanceOf[_from] -= _amount
    self.balanceOf[_to] += _amount
    self.allowance[_from][msg.sender] -= _amount
    log Transfer(_from, _to, _amount)
    return True

# Try creating a new method called playArcade which will be used to play games in the arcade
# The method should take in the amount of tokens to be used to play the game
# This method should reduce the balance of the user by the amount of tokens used to play the game
# Commit after you get this working!