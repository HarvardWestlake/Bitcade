const ethers = require('ethers');

async function main() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0]; // Assuming the user has at least one account connected
        
        // Connect to MetaMask provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Load the contract
        const ExampleGameContract = require('.contracts/ExampleGame.vy');
        const contractAddress = prompt("Enter the contract address:");
        const contract = new ethers.Contract(contractAddress, ExampleGameContract.abi, signer);

        // Get the example game address
        const exampleGameAddress = await contract.example_game_address();

        // Add event listener to the button
        document.getElementById("playButton").addEventListener("click", function() {
            // Redirect to the example game URL
            window.location.href = "examplegame.html?gameAddress=" + exampleGameAddress;
        });

        // Log user address and example game address
        console.log("User Address:", userAddress);
        console.log("Example Game Address:", exampleGameAddress);
    } else {
        console.error('MetaMask is not installed');
    }
}

main().catch(console.error);