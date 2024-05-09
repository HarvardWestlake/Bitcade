const ethers = require('ethers');

document.addEventListener("DOMContentLoaded", async function() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Connect to MetaMask provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Placeholder for the ExampleGame contract
        const exampleGameContract = {
            example_game_address: async function() {
                // Placeholder for fetching example game address
                return 'http://examplegame.com';
            }
        };

        // Add event listener to the playGame button
        const playButton = document.querySelector(".play-game-button");
        playButton.addEventListener("click", async function() {
            try {
                // Placeholder for getting the contract address (you can customize this)
                const contractAddress = prompt("Enter the contract address:");
                
                // Get the example game address
                const exampleGameAddress = await exampleGameContract.example_game_address();
                
                // Redirect to the example game URL
                window.location.href = `examplegame.html?gameAddress=${exampleGameAddress}&contractAddress=${contractAddress}`;
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });

        // Log user address
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log("User Address:", userAddress);
    } else {
        console.error('MetaMask is not installed');
    }
});
