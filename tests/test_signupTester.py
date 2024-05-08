from ape import accounts, project, chain
from ape.contracts import ContractInstance
import pytest

@pytest.fixture
def signup_contract() -> ContractInstance:
    # Deploy the Signup contract using the first account
    contract = accounts[0].deploy(project.Signup)
    return contract

def test_register_wallet_id_success(signup_contract: ContractInstance):
    # Use a fresh account to test registration
    wallet = accounts[1]
    
    # Register the wallet ID
    result = signup_contract.register_wallet_id(wallet.address, sender=accounts[0])
    
    # Check the output message
    assert result.return_value == "Wallet ID registered successfully"
    
    # Verify that the ID is registered
    assert signup_contract.registered_ids(wallet.address) == True

def test_register_wallet_id_failure(signup_contract: ContractInstance):
    # Use another fresh account and try to register it twice
    wallet = accounts[2]
    
    # First registration should succeed
    signup_contract.register_wallet_id(wallet.address, sender=accounts[0])
    
    # Second registration should fail
    with pytest.raises(Exception) as excinfo:
        signup_contract.register_wallet_id(wallet.address, sender=accounts[0])
    
    # Check if the error message is correct
    assert str(excinfo.value) == "Wallet ID already registered"
