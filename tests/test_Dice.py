import pytest
from ape import project, accounts, chain
from decimal import Decimal

@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def dice_contract(project, owner):
    return owner.deploy(project.Dice)

def test_calculate_payout_above(dice_contract):
    # Testing with rollAbove = True
    sliderInt = 70
    expected_chance = 30  # 100 - 70
    expected_multiplier = Decimal('98') / Decimal(expected_chance)
    calculated_multiplier = dice_contract.calculate_payout(sliderInt, True)
    
    assert calculated_multiplier == pytest.approx(expected_multiplier, abs=1e-2), "Multiplier mismatch for roll above"

def test_calculate_payout_below(dice_contract):
    # Testing with rollAbove = False
    sliderInt = 30
    expected_chance = 29  # 30 - 1
    expected_multiplier = Decimal('98') / Decimal(expected_chance)
    calculated_multiplier = dice_contract.calculate_payout(sliderInt, False)
    
    assert calculated_multiplier == pytest.approx(expected_multiplier, abs=1e-2), "Multiplier mismatch for roll below"

def test_calculate_payout_edge_cases(dice_contract):
    # Test edge cases where payout calculation might be at risk of division by zero or boundary issues
    with pytest.raises(AssertionError):
        dice_contract.calculate_payout(100, True)  # Should fail as chance = 0
    with pytest.raises(AssertionError):
        dice_contract.calculate_payout(1, False)   # Should fail as chance = 0

    # Valid edge cases
    sliderInt = 1
    if sliderInt != 100:  # Check for non-error scenario with rollAbove=True
        calculated_multiplier = dice_contract.calculate_payout(sliderInt, True)
        assert calculated_multiplier == Decimal('98'), "Multiplier mismatch at lower edge"
    
    sliderInt = 100
    if sliderInt != 1:    # Check for non-error scenario with rollAbove=False
        calculated_multiplier = dice_contract.calculate_payout(sliderInt, False)
        assert calculated_multiplier == Decimal('98'), "Multiplier mismatch at upper edge"
