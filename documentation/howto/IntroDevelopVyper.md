# Vyper Contract Development Guide

This guide outlines the step-by-step process for programming, compiling, and testing a Vyper smart contract, followed by extracting the ABI for use in a user interface.

## Prerequisites

Ensure that you have a Python environment set up with Vyper and the Ape framework installed. You can install these using pip if they are not already installed.

## Step 1: Program the Contract

Start by writing your Vyper contract. Save your contract with a `.vy` extension, such as `ExampleGame.vy`, in a dedicated contracts folder.

## Step 2: Compile the Contract

To compile your contract, navigate to your project directory and run:
```bash
(ape) theiss@Theiss:~/Documents/Github/Blocade$ ape compile
or 
(ape) theiss@Theiss:~/Documents/Github/Blocade$ vyper compile ./contracts/MyContactName.vy
```

## Step 3 : Fix Any Compilation Errors
If the compiler reports any errors, fix them before proceeding. Errors must be resolved to successfully compile the contract.

## Write Tests
Create tests for your contract to ensure it behaves as expected. Place your tests in the `tests` directory.  Make sure they are using vyper test framework pytest and both the names of the files and methods start with 'test_'

Most tests should start with compiling the project
```python
from ape import accounts, project

def test_mint_tokens(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.Wolvercoin.deploy("Wolvercoin", "WVC", 18, sender=owner)
    ...
```

## Step 5: Verify Tests
Run your tests using the Ape testing framework with the following command:
```bash
(ape) theiss@Theiss:~/Documents/Github/Blocade$ ape test
```
Make sure all tests pass before moving to the next step.


## Step 6: Extract the Application-Binary Interface (ABI)
```bash
(ape) theiss@Theiss:~/Documents/Github/Blocade$ vyper -f abi ./contracts/ExampleGame.vy
```

## Step 7: Copy ABI to UI
Copy the ABI output from the console and place it in the ui/abi folder under the appropriate name, ensuring it matches the contract name for easy reference.

By following these steps, you will have successfully compiled a Vyper contract, tested it, and prepared its ABI for integration into a user interface.