import pytest
from ape import project, accounts
from decimal import Decimal  # Ensure Decimal is imported

@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def dice_contract(project, owner):
    # Assuming deployment is done here, if not adjust accordingly
    return owner.deploy(project.Dice)

def test_calculate_payout_above(dice_contract, owner):
    sliderInt = 70
    expected_chance = 30  # 100 - 70
    expected_multiplier = Decimal('98') / Decimal(expected_chance)

    # Execute the payout calculation and check the stored result
    dice_contract.calculate_payout(sliderInt, True, sender=owner)
    calculated_multiplier = dice_contract.last_calculated_multiplier()

    assert calculated_multiplier == pytest.approx(expected_multiplier, abs=1e-2), "Multiplier mismatch for roll above"

def test_calculate_payout_below(dice_contract, owner):
    sliderInt = 30
    expected_chance = 29  # 30 - 1
    expected_multiplier = Decimal('98') / Decimal(expected_chance)

    # Execute the payout calculation and check the stored result
    dice_contract.calculate_payout(sliderInt, False, sender=owner)
    calculated_multiplier = dice_contract.last_calculated_multiplier()

    assert calculated_multiplier == pytest.approx(expected_multiplier, abs=1e-2), "Multiplier mismatch for roll below"


from ape.exceptions import ContractLogicError

def test_calculate_payout_edge_cases(dice_contract, owner):
    with pytest.raises(ContractLogicError):
        dice_contract.calculate_payout(100, True, sender=owner)  # Should fail as chance = 0
    with pytest.raises(ContractLogicError):
        dice_contract.calculate_payout(1, False, sender=owner)   # Should fail as chance = 0
