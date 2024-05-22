# @version ^0.3.10

# Interface definition for WyrmAutoBattler
interface WyrmAutoBattler:
    def getStats(_id: uint256) -> (uint256, uint256, uint256, uint256): view
    def getTotalStats(tokenId: uint256) -> uint256: view

# State variable to hold the ID
id: uint256
struct StackItem:
    low: int128
    high: int128

@external
def quicksort_accounts(wyrm_auto_battler: address, accounts: address[10], ids: uint256[10]) -> address[10]:
    n: int128 = 10  # The length of the accounts array
    
    if n <= 1:
        return accounts

    # Initialize stack for iterative QuickSort
    stack: StackItem[10] = empty(StackItem[10])
    top: int128 = 0

    # Push initial values to stack
    stack[top] = StackItem({low: 0, high: n - 1})

    for _ in range(100):  # Arbitrary large number to avoid while loop
        if top < 0:
            break

        # Pop from stack
        high: int128 = stack[top].high
        low: int128 = stack[top].low
        top -= 1

        # Partition the array
        pivot_index: int128 = self.partition(wyrm_auto_battler, accounts, ids, low, high)

        # Push sub-arrays to stack if they are within range
        if pivot_index - 1 > low:
            top += 1
            stack[top] = StackItem({low: low, high: pivot_index - 1})

        if pivot_index + 1 < high:
            top += 1
            stack[top] = StackItem({low: pivot_index + 1, high: high})

    return accounts

@internal
def partition(wyrm_auto_battler: address, accounts: address[10], ids: uint256[10], low: int128, high: int128) -> int128:
    battler: WyrmAutoBattler = WyrmAutoBattler(wyrm_auto_battler)
    pivot: uint256 = battler.getTotalStats(ids[high])
    i: int128 = low - 1

    for j in range(10):  # Using a fixed-size loop to cover the maximum possible range
        if j >= low and j < high:  # Ensuring we only operate within the valid range
            if battler.getTotalStats(ids[j]) < pivot:
                i += 1
                self.swap(accounts, ids, i, j)

    self.swap(accounts, ids, i + 1, high)
    return i + 1

@internal
def swap(accounts: address[10], ids: uint256[10], i: int128, j: int128):
    temp_account: address = accounts[i]
    temp_id: uint256 = ids[i]
    accounts[i] = accounts[j]
    ids[i] = ids[j]
    accounts[j] = temp_account
    ids[j] = temp_id


# Sort wyrms (placeholder)
@external
def sortWorms():
    pass

# Function to get the total stats from an external contract
@external
def getTotal(wyrm_auto_battler: address, id: uint256) -> uint256:
    # Create an instance of the WyrmAutoBattler interface at the given address
    battler: WyrmAutoBattler = WyrmAutoBattler(wyrm_auto_battler)
    
    # Call getTotalStats on the instance
    total: uint256 = battler.getTotalStats(id)
    
    return total
