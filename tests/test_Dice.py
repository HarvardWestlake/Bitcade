import pytest
from ape import project, accounts
from decimal import Decimal  # Import Decimal class from decimal module

@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def dice_contract(project, owner):
    # Ensure contract is deployed using the owner account
    return owner.deploy(project.Dice)

from ape.exceptions import ContractLogicError

def test_calculate_payout_edge_cases(dice_contract, owner):
    with pytest.raises(ContractLogicError):
        dice_contract.calculate_payout(100, True, sender=owner)  # Should fail as chance = 0
    with pytest.raises(ContractLogicError):
        dice_contract.calculate_payout(1, False, sender=owner)   # Should fail as chance = 0
