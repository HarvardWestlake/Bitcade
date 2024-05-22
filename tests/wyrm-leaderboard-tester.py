from ape import accounts, project

def test_get_total_stats(accounts):
    # Deploy the WyrmSorting contract
    owner = accounts[0]
    wyrm_sorting_contract = project.WyrmSorting.deploy(sender=owner)
    
    # Deploy the MockWyrmAutoBattler contract
    mock_wyrm_auto_battler = project.MockWyrmAutoBattler.deploy(sender=owner)
    
    # Test getTotal function for a few ids
    for wyrm_id in range(1, 4):
        total = wyrm_sorting_contract.getTotal(mock_wyrm_auto_battler.address, wyrm_id, sender=owner)
        expected_total = (100 + wyrm_id) + (200 + wyrm_id) + (300 + wyrm_id) + (400 + wyrm_id)
        assert total == expected_total, f"Total {total} does not match expected {expected_total}"
    
    print("Test passed, getTotal method works correctly.")

# Call the test function
test_get_total_stats(accounts)
