const ethers = require('ethers');

// Replace 'YourContract' with the actual name of your contract
const contractName = 'YourContract';

// Load the compiled contract artifacts
const contractArtifacts = require(`./build/contracts/${contractName}.json`);

// Replace '<network_id>' with the network ID where your contract is deployed
const networkId = '<network_id>';

// Get the contract address from the artifacts based on the network ID
const contractAddress = contractArtifacts.networks[networkId].address;

// Get the ABI from the artifacts
const abi = contractArtifacts.abi;

document.addEventListener("DOMContentLoaded", async function() {
    const playButton = document.querySelector(".play-game-button");
    // Check if the play button exists
    if (playButton) {
        playButton.addEventListener("click", async function() {
            // Check if MetaMask is installed
            if (typeof window.ethereum !== 'undefined') {
                try {
                    // Request account access if needed
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    
                    // Connect to MetaMask provider
                    const provider = new ethers.providers.Web3Provider(window.ethereum);
                    const signer = provider.getSigner();

                    // Create a contract instance
                    const contract = new ethers.Contract(contractAddress, abi, signer);

                    // Call the function to get the game address
                    const exampleGameAddress = await contract.example_game_address();

                    // Redirect to the example game URL
                    const gameAddress = `examplegame.html?gameAddress=${exampleGameAddress}&contractAddress=${contractAddress}`;
                    window.location.href = gameAddress;
                } catch (error) {
                    console.error('Error:', error);
                    alert('An error occurred. Please try again.');
                }
            } else {
                console.error('MetaMask is not installed');
            }
        });
    } else {
        console.error('Play game button not found');
    }
});
