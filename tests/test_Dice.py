import pytest
from ape import project, accounts
from decimal import Decimal

@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def rng_contract(owner):
    contract = owner.deploy(project.RNGV3)
    return contract

@pytest.fixture
def dice_contract(project, owner, rng_contract):
    contract = owner.deploy(project.Dice)
    contract.set_random_number_generator(rng_contract.address, sender=owner)
    return contract

def test_calculate_payout_above(dice_contract, owner):
    sliderInt = 70
    expected_chance = 30  # 100 - 70
    expected_multiplier = Decimal('98') / Decimal(expected_chance)

    dice_contract.calculate_payout(sliderInt, True, sender=owner)
    calculated_multiplier = dice_contract.last_calculated_multiplier()

    assert calculated_multiplier == pytest.approx(expected_multiplier, abs=1e-2), "Multiplier mismatch for roll above"

def test_calculate_payout_below(dice_contract, owner):
    sliderInt = 30
    expected_chance = 29  # 30 - 1
    expected_multiplier = Decimal('98') / Decimal(expected_chance)

    dice_contract.calculate_payout(sliderInt, False, sender=owner)
    calculated_multiplier = dice_contract.last_calculated_multiplier()

    assert calculated_multiplier == pytest.approx(expected_multiplier, abs=1e-2), "Multiplier mismatch for roll below"

from ape.exceptions import ContractLogicError

def test_calculate_payout_edge_cases(dice_contract, owner):
    with pytest.raises(ContractLogicError):
        dice_contract.calculate_payout(100, True, sender=owner)  # Should fail as chance = 0
    with pytest.raises(ContractLogicError):
        dice_contract.calculate_payout(1, False, sender=owner)   # Should fail as chance = 0

def test_place_bet(dice_contract, rng_contract, owner, chain):
    sliderInt = 50
    rollAbove = True
    bet_amount = 100  # Example bet amount

    initial_balance = owner.balance

    assert initial_balance > bet_amount, "Insufficient balance to place the bet"

    transfer_tx = owner.transfer(dice_contract.address, bet_amount)
    place_bet_tx = dice_contract.place_bet(sliderInt, rollAbove, sender=owner, value=bet_amount)

    gas_used_transfer = transfer_tx.gas_used * transfer_tx.gas_price
    gas_used_place_bet = place_bet_tx.gas_used * place_bet_tx.gas_price

    stored_bet = dice_contract.bets(owner.address)
    assert stored_bet == bet_amount, "Bet amount mismatch"

    lock_tx = rng_contract.lockCurrent(sender=owner)

    chain.mine(3)

    locked_block_receipt = rng_contract.updateLock(100, sender=owner)

    gas_used_lock = lock_tx.gas_used * lock_tx.gas_price
    gas_used_update_lock = locked_block_receipt.gas_used * locked_block_receipt.gas_price

    locked_block_events = list(rng_contract.returnRandomNumber.from_receipt(locked_block_receipt))

    assert len(locked_block_events) > 0, "No returnRandomNumber event emitted"

    locked_block_event = locked_block_events[0]
    locked_block = locked_block_event.number
    assert locked_block > 0, "Random number generator did not lock the block"

    final_balance = owner.balance

    gas_cost = gas_used_transfer + gas_used_place_bet + gas_used_lock + gas_used_update_lock
    expected_final_balance = initial_balance - bet_amount - gas_cost

    tolerance = 100  # Allow for a minor discrepancy of 100 wei
    assert abs(final_balance - expected_final_balance) <= tolerance, "Funds not transferred correctly"

def test_resolve_bet(dice_contract, rng_contract, owner, chain):
    sliderInt = 50
    rollAbove = True
    bet_amount = 100  # Example bet amount

    initial_balance = owner.balance

    assert initial_balance > bet_amount, "Insufficient balance to place the bet"

    owner.transfer(dice_contract.address, bet_amount)
    dice_contract.place_bet(sliderInt, rollAbove, sender=owner, value=bet_amount)

    chain.mine(3)

    dice_contract.resolve_bet(sliderInt, rollAbove, sender=owner)

    event_filter = dice_contract.BetResult
    events = list(event_filter(owner.address, bet_amount, sliderInt, rollAbove, None, None, None))
    assert len(events) > 0, "No BetResult event emitted"

    stored_bet = dice_contract.bets(owner.address)
    assert stored_bet == 0, "Bet not cleared after resolution"

    final_balance = owner.balance
