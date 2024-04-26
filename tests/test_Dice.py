import pytest
from vyper import compile_code

# Define the Vyper contract code
vyper_code = """
@internal
def _calculate_multiplier(sliderInt: int128) -> decimal:
    return 98.0 / (100.0 - abs(50 - sliderInt) * 2.0)
"""

# Compile the Vyper contract to get the bytecode and ABI
contract = compile_code(vyper_code, ['bytecode', 'abi'])

# Contract class simulator for testing
class TestDiceContract:
    def __init__(self, contract):
        self.contract = contract

    def calculate_multiplier(self, sliderInt):
        # Simulate calling the internal Vyper method _calculate_multiplier
        # In real test, you would interact with a deployed contract instance
        return self.contract._calculate_multiplier(sliderInt)

# Initialize the test contract class with compiled contract
test_contract = TestDiceContract(contract)

# Test cases for the _calculate_multiplier method
def test_calculate_multiplier():
    # Test with different sliderInt values to cover various edge cases
    assert test_contract.calculate_multiplier(50) == pytest.approx(1.96, 0.01), "Expected multiplier for 50%"
    assert test_contract.calculate_multiplier(60) == pytest.approx(2.45, 0.01), "Expected multiplier for 60%"
    assert test_contract.calculate_multiplier(40) == pytest.approx(2.45, 0.01), "Expected multiplier for 40%"
    assert test_contract.calculate_multiplier(30) == pytest.approx(3.27, 0.01), "Expected multiplier for 30%"
    assert test_contract.calculate_multiplier(70) == pytest.approx(3.27, 0.01), "Expected multiplier for 70%"

# Run the test
if __name__ == "__main__":
    test_calculate_multiplier()
