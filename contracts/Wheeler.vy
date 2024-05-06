from vyper.interfaces import ERC20

# Event definitions for logging
event TokenCommitted:
    user: indexed(address)
    amount: uint256
    color: indexed(String[10])

event WheelSpun:
    speed: uint256

event WinPaid:
    user: indexed(address)
    amount: uint256

wheel_speed: public(uint256)
wheel_is_spinning: public(bool)
is_slowing_down: public(bool)
token_amount: public(uint256)
user_address: public(address)
color_selected: public(String[10])
win_multiplier: constant(uint256) = 2
random_slowing_number: public(uint256)

# External to interact with ERC20 tokens
token: public(ERC20)

@external
def __init__(_token: address):
    self.token = ERC20(_token)
    self.wheel_speed = 0
    self.wheel_is_spinning = False
    self.is_slowing_down = False

@external
def spin_wheel():
    assert not self.wheel_is_spinning, "The wheel is already spinning!"
    self.wheel_speed = 1000  # Initial spin speed
    self.wheel_is_spinning = True
    log WheelSpun(self.wheel_speed)

@external
def token_commit(_bet_amount: uint256, _user_address: address, _color: String[10]):
    assert not self.wheel_is_spinning, "Cannot commit tokens while the wheel is spinning."
    self.token.transferFrom(_user_address, self, _bet_amount)
    self.token_amount = _bet_amount
    self.user_address = _user_address
    self.color_selected = _color
    log TokenCommitted(_user_address, _bet_amount, _color)

@external
def win_tokens():
    assert self.wheel_is_spinning, "Spin the wheel first!"
    self.random_outcome()  # Assume this decides the win
    if self.random_outcome():
        win_amount: uint256 = self.token_amount * 2
        self.token.transfer(self.user_address, win_amount)
        log WinPaid(self.user_address, win_amount)
    self.reset_game()

@internal
def reset_game():
    self.wheel_speed = 0
    self.wheel_is_spinning = False
    self.is_slowing_down = False

@internal
def random_outcome() -> bool:
    # Convert block properties to bytes and concatenate them for hashing
    timestamp_bytes: bytes32 = convert(block.timestamp, bytes32)
    difficulty_bytes: bytes32 = convert(block.difficulty, bytes32)
    self.random_slowing_number = convert(keccak256(concat(timestamp_bytes, difficulty_bytes)), uint256)
    # Assuming a simple outcome where 50% chance is considered a win
    return (self.random_slowing_number % 2) == 0
