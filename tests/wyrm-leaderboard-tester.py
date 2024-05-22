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

def test_sort_accounts(accounts):
    # Deploy the WyrmSorting contract
    owner = accounts[0]
    wyrm_sorting_contract = project.WyrmSorting.deploy(sender=owner)

    # Deploy the MockWyrmAutoBattler contract
    mock_wyrm_auto_battler = project.MockWyrmAutoBattler.deploy(sender=owner)

    # Set up accounts and corresponding IDs
    test_accounts = accounts[:10]
    test_ids = [i for i in range(1, 11)]

    # Set total stats for each ID in the MockWyrmAutoBattler contract
    for i, acc_id in enumerate(test_ids):
        mock_wyrm_auto_battler.setTotalStats(acc_id, 10 - i, sender=owner)  # Decreasing totals for simplicity

    # Call quicksort_accounts in the Vyper contract
    sorted_accounts = wyrm_sorting_contract.quicksort_accounts(mock_wyrm_auto_battler.address, test_accounts, test_ids, sender=owner)

    # Retrieve the sorted totals for validation
    sorted_totals = [mock_wyrm_auto_battler.getTotalStats(test_ids[i], sender=owner) for i in range(10)]
    expected_sorted_totals = sorted(sorted_totals)

    # Verify the accounts are sorted correctly by their totals
    assert sorted_totals == expected_sorted_totals, f"Sorted totals {sorted_totals} do not match expected {expected_sorted_totals}"

    print("Test passed, quicksort_accounts method works correctly.")

# Call the test functions
test_get_total_stats(accounts)
test_sort_accounts(accounts)
