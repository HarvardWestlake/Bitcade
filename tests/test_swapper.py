
import boa

def test_swapper_deployed(swapper):
    assert hasattr(swapper, "buy")
    assert hasattr(swapper, "withdraw")

    print("Test passed, the Swapper contract has been deployed.")

def test_buy_tokens(wolvercoin, swapper, kian):
    # Buy tokens
    bad_amount = 0

    with boa.env.prank(kian):
        with boa.reverts():
            swapper.buy(value=bad_amount)

    amount = 1000
    with boa.env.prank(kian):
        swapper.buy(value=amount)

    # Check balance
    assert wolvercoin.balanceOf(kian) == amount

    print("Test passed, the deployer has bought tokens.")

def test_withdraw_eth(deployer, swapper, kian):
    # Buy tokens
    amount = 1000 * 10**18
    
    with boa.env.prank(kian):
        swapper.buy(value=amount)

    with boa.env.prank(kian):
        with boa.reverts():
            swapper.withdraw()

    # Withdraw tokens
    with boa.env.prank(deployer):
        swapper.withdraw()

    # Check balance
    assert boa.env.get_balance(swapper.address) == 0
    assert boa.env.get_balance(deployer) == 2 * amount

    print("Test passed, the deployer has withdrawn tokens.")

def test_wolvercoin_swapper(wolvercoin, swapper, kian):

    assert wolvercoin.swapper() == swapper.address

    with boa.reverts():
        with boa.env.prank(kian):
            wolvercoin.setSwapper(boa.env.eoa)

    with boa.env.prank(swapper.address):
        wolvercoin.setSwapper(kian)

    assert wolvercoin.swapper() == kian

    print("Test passed, the Swapper contract has been set.")

def test_wolvercoin_swapperMint(wolvercoin, swapper, kian):
    # Buy tokens
    amount = 1000

    with boa.env.prank(kian):
        with boa.reverts():
            wolvercoin.swapperMint(boa.env.eoa, amount)

    with boa.env.prank(swapper.address):
        wolvercoin.swapperMint(kian, amount)

    assert wolvercoin.balanceOf(kian) == amount

    print("Test passed, the deployer has minted tokens.")

def test_setOwner(swapper, kian):
    # Change owner
    with boa.env.prank(kian):
        with boa.reverts():
            swapper.setOwner(boa.env.eoa)

    with boa.env.prank(swapper.owner()):
        swapper.setOwner(kian)

    assert swapper.owner() == kian

    print("Test passed, the owner has been changed.")