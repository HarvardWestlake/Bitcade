from ape import accounts, project

def test_sort_worms(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    wyrm_sorting_contract = project.WyrmSorting.deploy(sender=owner)
    
    # Mock WyrmAutoBattler contract
    class MockWyrmAutoBattler:
        def getStats(self, _id):
            # Return mock stats: attack, defense, speed, health
            return (100 + _id, 200 + _id, 300 + _id, 400 + _id)
    
    # Assign mock WyrmAutoBattler to the contract
    wyrm_sorting_contract.WyrmAutoBattler = MockWyrmAutoBattler()
    
    # Test getTotal function indirectly by calling a public function that uses it
    def test_get_total(id):
        # Call the internal getTotal function through the public sortWorms
        total = wyrm_sorting_contract.getTotal(id)
        expected_total = (100 + id) + (200 + id) + (300 + id) + (400 + id)
        assert total == expected_total, f"Total {total} does not match expected {expected_total}"
    
    # Test for a few ids
    for wyrm_id in range(1, 4):
        test_get_total(wyrm_id)
    
    print("Test passed, getTotal method works correctly.")

# Call the test function
test_sort_worms(accounts)
