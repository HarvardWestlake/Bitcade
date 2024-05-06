from ape import accounts, project
# Signup.vy
contract Signup:
# Mapping to store whether a wallet ID is registered
registered_ids: public(map(address, bool))

@external
def register_wallet_id(self, wallet_id: address):
    # Check if the wallet ID is already registered
    if self.registered_ids[wallet_id]:
        # Wallet ID is already registered, raise an error
        raise "Wallet ID already registered"
    
    # Register the wallet ID
    self.registered_ids[wallet_id] = True
    return "Wallet ID registered successfully"
