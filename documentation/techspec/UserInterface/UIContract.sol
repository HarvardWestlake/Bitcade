// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract UIDesignContract {
    address private owner;
    uint public registrationFee = 0.01 ether;
    uint public escrowPercentage = 10; // percentage of funds to hold in escrow

    struct UIHost {
        bool isRegistered;
        uint earnings;
        uint escrowBalance;
    }

    mapping(address => UIHost) public hosts;

    event Registered(address indexed walletId);
    event EarningsDistributed(address indexed hostId, uint amount);
    event EscrowDeposited(address indexed hostId, uint amount);
    event EscrowReleased(address indexed hostId, uint amount);
    event PaymentMade(address indexed from, address indexed to, uint amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Registers a new UI host
    function registerUI(address walletId) public payable {
        require(msg.value == registrationFee, "Registration fee must be paid.");
        require(!hosts[walletId].isRegistered, "Host is already registered.");

        hosts[walletId] = UIHost({
            isRegistered: true,
            earnings: 0,
            escrowBalance: 0
        });

        emit Registered(walletId);
    }

    // Distributes earnings to UI host and the house, depositing a portion to escrow
    function distributeEarnings(address hostId, uint totalAmount) public onlyOwner {
        require(hosts[hostId].isRegistered, "Host is not registered.");

        uint escrowAmount = (totalAmount * escrowPercentage) / 100;
        uint earningsToDistribute = totalAmount - escrowAmount;

        hosts[hostId].earnings += earningsToDistribute;
        hosts[hostId].escrowBalance += escrowAmount;

        emit EarningsDistributed(hostId, earningsToDistribute);
        emit EscrowDeposited(hostId, escrowAmount);
    }

    // Releases escrow to the UI host after a specified period or conditions are met
    function releaseEscrow(address hostId) public onlyOwner {
        require(hosts[hostId].escrowBalance > 0, "No escrow balance to release.");

        uint amountToRelease = hosts[hostId].escrowBalance;
        payable(hostId).transfer(amountToRelease);
        hosts[hostId].escrowBalance = 0;

        emit EscrowReleased(hostId, amountToRelease);
    }

    // Allows owner to collect fees stored in the contract
    function collectFees() public onlyOwner {
        uint balance = address(this).balance - totalEscrowBalance();
        payable(owner).transfer(balance);
    }

    // Helper function to calculate total escrow held in the contract
    function totalEscrowBalance() public view returns (uint) {
        uint total = 0;
        // This loop could cause gas limit issues for a large number of hosts
        for(uint i = 0; i < hostAddresses.length; i++) {
            total += hosts[hostAddresses[i]].escrowBalance;
        }
        return total;
    }

    // Accepts payments to the contract
    receive() external payable {
        emit PaymentMade(msg.sender, address(this), msg.value);
    }
}
