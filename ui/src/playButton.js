const ethers = require('ethers');
const { ExampleGameContract } = require('./contracts/exampleGame');

async function main() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Connect to MetaMask provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Load the contract
        const contractAddress = prompt("Enter the contract address:");
        const exampleGameContract = new ethers.Contract(contractAddress, ExampleGameContract.interface, signer);

        // Get the example game address
        const exampleGameAddress = await exampleGameContract.example_game_address();

        // Add event listener to the button
        const playButton = document.querySelector(".play-game-button");
        playButton.addEventListener("click", function() {
            // Redirect to the example game URL
            window.location.href = "examplegame.html?gameAddress=" + exampleGameAddress;
        });

        // Log user address and example game address
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log("User Address:", userAddress);
        console.log("Example Game Address:", exampleGameAddress);
    } else {
        console.error('MetaMask is not installed');
    }
}

main().catch(console.error);
