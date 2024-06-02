# Define the event for registering a UI
event RegisterUI:
    wallet_id: address
    distributor_id: int128

# Mapping to track registered UI distributors
ui_distributors: public(map(address, bool))

@external
def register_ui(wallet_id: address):
    """
    Register a new UI distributor with the provided wallet ID.
    Args:
        wallet_id (address): The wallet address of the UI distributor.
    Raises:
        AssertionError: If the wallet_id is already registered.
    """
    assert not self.ui_distributors[wallet_id], "This wallet is already registered as a UI distributor."
    
    # Register the UI distributor
    self.ui_distributors[wallet_id] = True
    
    # Emit the registration event
    emit RegisterUI(wallet_id, len(self.ui_distributors))
