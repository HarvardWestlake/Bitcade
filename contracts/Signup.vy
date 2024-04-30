# Signup.vy
@external
def __init__():
    """
    Constructor function that initializes the mapping.
    """
    self.address_to_string_map: HashMap[address, String[64]] = {}


@external
def store_string(user_string: String[64]):
    """
    Stores a string associated with the message sender's address.
    """
    self.address_to_string_map[msg.sender] = user_string


@view
@external
def get_string(user_address: address) -> String[64]:
    """
    Retrieves a string associated with a given address.
    """
    return self.address_to_string_map[user_address]
